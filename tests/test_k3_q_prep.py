import ast
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestK3QPrep(unittest.TestCase):
    def test_runtime_and_smoke_assets_exist(self):
        for p in [
            ROOT/"gke/app/qahbn2_runtime.py",
            ROOT/"gke/app/Dockerfile.qahbn2",
            ROOT/"gke/experiments/k3_q_smoke.yaml",
            ROOT/"gke/scripts/run_k3_q_smoke.sh",
            ROOT/"gke/PROVENANCE.md",
        ]:
            self.assertTrue(p.exists(), p)

    def test_runtime_compiles(self):
        ast.parse((ROOT/"gke/app/qahbn2_runtime.py").read_text())

    def test_dockerfile_includes_inherited_runtime_imports(self):
        dockerfile=(ROOT/"gke/app/Dockerfile.qahbn2").read_text()
        self.assertIn("COPY gke/app/gen_topology.py gen_topology.py", dockerfile)
        maintenance=(ROOT/"gke/app/dcsoc_maintenance.py").read_text()
        self.assertIn("from gen_topology import", maintenance)

    def test_inherited_files_are_pinned_copies(self):
        expected={
            "peer.py":"2433404c55d0df5e1e341f6e6ffcb22660db1d74",
            "ahbn_controller.py":"7e5e681bd3228ecf505170f236ea90e3098f747a",
            "observations.py":"7e0318d53118bf1d9c192602ba0c305884250bc3",
            "k5_final_actuator_policy.py":"48d49c553008d0a395e41be59d895b5ded14b6d1",
            "peer.proto":"0bf8b06eb7622f9ea4b0c43a2c965f1d848bd027",
        }
        # Blob SHA pins are documented here to catch accidental mutation in Git history.
        provenance=(ROOT/"gke/PROVENANCE.md").read_text()
        self.assertIn("cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689",provenance)
        self.assertEqual(len(expected),5)

    def test_smoke_is_bounded_qahbn2_only(self):
        text=(ROOT/"gke/experiments/k3_q_smoke.yaml").read_text()
        self.assertIn("strategy: qahbn2",text)
        self.assertIn("numNodes: 4",text)
        self.assertIn("messageCount: 4",text)
        self.assertIn("mode: none",text)

    def test_no_formal_claim_language_in_runner(self):
        text=(ROOT/"gke/scripts/run_k3_q_smoke.sh").read_text().lower()
        self.assertNotIn("formal",text)
        self.assertIn("k3-q smoke pass",text)

if __name__=="__main__":
    unittest.main()
