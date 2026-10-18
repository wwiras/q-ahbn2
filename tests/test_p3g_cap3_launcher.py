"""Offline P3G CAP3 launcher guards; never contacts Kubernetes."""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "gke/scripts/run_k7_experiment.sh"
DIGEST = "sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f"
IMAGE = "docker.io/wwiras/q-ahbn2@" + DIGEST

class P3GCap3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code = SCRIPT.read_text(encoding="utf-8")

    def run_guard(self, recovery, namespace, image=IMAGE, digest=DIGEST):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, OUTDIR=tmp, NAMESPACE=namespace,
                       IMAGE=image, EXPECTED_IMAGE_DIGEST=digest,
                       PYTHON=sys.executable, P3G_RECOVERY_ENABLED=recovery)
            # All negative guards precede even the first kubectl invocation.
            return subprocess.run(["bash", str(SCRIPT), "unused.yaml"], env=env,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  text=True, timeout=15)

    def test_01_bash_syntax(self):
        r = subprocess.run(["bash", "-n", str(SCRIPT)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_02_default_disabled(self):
        self.assertIn('P3G_RECOVERY_ENABLED="${P3G_RECOVERY_ENABLED:-0}"', self.code)
        self.assertIn('enabled: "0"', (ROOT / "gke/helm/ahbn/values.yaml").read_text())

    def test_03_reject_invalid_flag(self):
        r = self.run_guard("true", "qahbn2-d7-smoke-p3g-ahbn")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("recovery flag must be 0 or 1", r.stderr)

    def test_04_reject_non_p3g_namespace(self):
        r = self.run_guard("1", "qahbn2-d7-smoke-ahbn")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("P3G-specific namespace", r.stderr)

    def test_05_reject_unapproved_image(self):
        wrong = "sha256:" + "a" * 64
        r = self.run_guard("1", "qahbn2-d7-smoke-p3g-ahbn",
                           "docker.io/wwiras/q-ahbn2@" + wrong, wrong)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("not approved P3G image", r.stderr)

    def test_06_helm_install_flag(self):
        self.assertIn('--set-string "recovery.enabled=${P3G_RECOVERY_ENABLED}"', self.code)
        self.assertIn("--set controller.enabled=false", self.code)

    def test_07_peer_state_and_image_verification(self):
        self.assertIn('get statefulset peer -o json', self.code)
        self.assertIn('recovery flag mismatch', self.code)
        self.assertIn('expected 20 pods', self.code)
        self.assertIn('imageID', self.code)

    def test_08_controller_verification(self):
        self.assertIn('get job ahbn-controller -o json', self.code)
        self.assertIn('controller image mismatch', self.code)
        self.assertIn("--reuse-values --set controller.enabled=true", self.code)

    def test_09_precreate_peer_count(self):
        self.assertIn('P3G requires exactly 20 peers', self.code)
        self.assertLess(self.code.index('P3G requires exactly 20 peers'),
                        self.code.index('kubectl create namespace'))

    def test_10_ownership_and_cleanup(self):
        for guard in ('namespace already exists', 'OWNERSHIP_MISMATCH',
                      '"${current_uid}" != "${NS_UID}"',
                      '"${current_owner}" != "${RUN_OWNER}"',
                      'cleanup_exit_status.txt', 'kubectl delete namespace'):
            self.assertIn(guard, self.code)

    def test_11_no_explicit_resource_change(self):
        self.assertNotIn('resources:', self.code)

if __name__ == "__main__":
    unittest.main()
