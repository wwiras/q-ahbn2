#!/usr/bin/env python3
"""D7-P4 local fault injection: fake kubectl, helm and Python in an isolated sandbox.
Run: python3 gke/scripts/test_d7_p4_cleanup.py
No GKE credentials, live namespace, or real cloud command is used.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "gke/scripts/run_k7_experiment.sh"
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
OUT = ROOT / "output/evidence" / f"{STAMP}-D7-P4-cleanup-mock"
IMAGE = "docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
CONTEXT = "gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"

KUBECTL = r'''#!/usr/bin/env bash
set -e
printf 'kubectl %s\n' "$*" >> "$MOCK_LOG"
case "$1" in
  config)
    if [[ "$MOCK_CASE" == wrong_context ]]; then echo wrong-context; else echo "$EXPECTED_CONTEXT"; fi
    exit 0;;
  create)
    [[ "$2" == namespace ]] && { touch "$MOCK_STATE"; exit 0; };;
  label)
    [[ "$2" == namespace ]] && { echo "$RUN_OWNER" > "$MOCK_OWNER"; exit 0; };;
  get)
    if [[ "$2" == namespace ]]; then
      if [[ "$*" == *jsonpath* || "$*" == *go-template* ]]; then
        if [[ -f "$MOCK_STATE" ]]; then
          if [[ "$*" == *qahbn2-run-owner* ]]; then cat "$MOCK_OWNER" 2>/dev/null || true; else echo mock-namespace-uid; fi
        fi
      elif [[ -f "$MOCK_STATE" ]]; then echo "namespace/$3"; fi
      exit 0
    fi
    if [[ "$*" == *"get pods"* ]]; then echo '{"items":[]}'; fi
    exit 0;;
  delete)
    if [[ "$2" == namespace ]]; then
      if [[ "$MOCK_CASE" == delete_failure ]]; then echo 'mock delete failed' >&2; exit 51; fi
      rm -f "$MOCK_STATE"; echo 'namespace deleted'; exit 0
    fi;;
  -n)
    if [[ "$*" == *"rollout status"* ]]; then echo 'mock rollout failure' >&2; exit 43; fi
    exit 0;;
  logs) exit 0;;
  *) exit 0;;
esac
'''
HELM = r'''#!/usr/bin/env bash
set -e
printf 'helm %s\n' "$*" >> "$MOCK_LOG"
case "$1" in
  install)
    touch "$MOCK_STATE"
    if [[ "$MOCK_CASE" == install_failure ]]; then echo 'mock helm install failed' >&2; exit 42; fi;;
  uninstall) echo 'mock helm uninstall';;
esac
'''
PYTHON = r'''#!/usr/bin/env bash
set -e
printf 'python %s\n' "$*" >> "$MOCK_LOG"
if [[ "$1" == *k7_gen_topology.py ]]; then
  out=''
  while (( $# )); do
    if [[ "$1" == --out ]]; then shift; out="$1"; break; fi
    shift
  done
  [[ -n "$out" ]] || exit 71
  printf '{"num_nodes":20}\n' > "$out"
  exit 0
fi
if [[ "$1" == -c ]]; then printf '20\n'; exit 0; fi
exit 72
'''

def put(path: Path, data: str) -> None:
    path.write_text(data)
    path.chmod(0o700)

def run_case(case: str, *, preexisting: bool=False) -> dict:
    with tempfile.TemporaryDirectory(prefix="d7-p4-mock-") as tmp:
        t = Path(tmp)
        for part in ("gke/scripts", "gke/app", "gke/helm/ahbn", "configs", "results", "mockbin"):
            (t/part).mkdir(parents=True, exist_ok=True)
        shutil.copy2(RUNNER, t/"gke/scripts/run_k7_experiment.sh")
        (t/"gke/helm/ahbn/topology.json").write_text('{}\n')
        (t/"configs/input.yaml").write_text('experiment: mock\n')
        for name, code in (("kubectl",KUBECTL),("helm",HELM),("mockpython",PYTHON)):
            put(t/"mockbin"/name,code)
        state, log = t/"namespace_state", t/"mock_calls.txt"
        owner = t/"namespace_owner"
        if preexisting:
            state.write_text('PREEXISTING\n')
        env = dict(os.environ, PATH=str(t/"mockbin")+os.pathsep+"/usr/bin:/bin",
                   MOCK_STATE=str(state), MOCK_OWNER=str(owner), MOCK_LOG=str(log), MOCK_CASE=case,
                   RUN_OWNER="d7-smoke-qahbn2-d7-smoke-gossip",
                   EXPECTED_CONTEXT=CONTEXT, OUTDIR=str(t/"results"),
                   NAMESPACE="qahbn2-d7-smoke-gossip", RELEASE="qahbn2",
                   IMAGE=IMAGE, EXPECTED_IMAGE_DIGEST=IMAGE.partition('@')[2],
                   PYTHON=str(t/"mockbin/mockpython"))
        assert shutil.which('kubectl',path=env['PATH']) == str(t/"mockbin/kubectl")
        assert shutil.which('helm',path=env['PATH']) == str(t/"mockbin/helm")
        proc = subprocess.run(["/bin/bash",str(t/"gke/scripts/run_k7_experiment.sh"),"configs/input.yaml"],
                              env=env,cwd=t,capture_output=True,text=True,timeout=25)
        events=log.read_text().splitlines() if log.exists() else []
        namespace_exists=state.exists()
        result=t/"results/experiment_exit_status.txt"
        code_recorded=result.read_text().strip() if result.exists() else None
        mutated=any(e.startswith(("helm install","helm uninstall","kubectl delete","kubectl create","kubectl label")) for e in events)
        if case in ("install_failure","rollout_failure"):
            ok = (proc.returncode!=0 and not namespace_exists
                  and any(e.startswith("helm uninstall") for e in events)
                  and any(e.startswith("kubectl delete namespace") for e in events)
                  and code_recorded not in (None,"0"))
        elif case=="delete_failure":
            ok=(proc.returncode!=0 and namespace_exists
                and "HOLD: namespace remains" in proc.stderr
                and code_recorded not in (None,"0"))
        elif case in ("preexisting","wrong_context"):
            ok=(proc.returncode!=0 and not mutated
                and namespace_exists==preexisting and code_recorded is None)
        else:
            raise AssertionError(case)
        return {"case":case,"pass":ok,"exit_code":proc.returncode,
                "recorded_exit":code_recorded,"namespace_remains":namespace_exists,
                "mock_calls":events,"stderr":proc.stderr[-1200:]}

def main():
    if not RUNNER.is_file():
        raise SystemExit("Missing repository experiment runner")
    OUT.mkdir(parents=True,exist_ok=False)
    cases=[run_case("install_failure"),run_case("rollout_failure"),
           run_case("delete_failure"),run_case("preexisting",preexisting=True),
           run_case("wrong_context")]
    git=subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,capture_output=True,text=True)
    result={"gate":"D7-P4 MOCK CLEANUP","scope":"LOCAL MOCKS ONLY; NO GKE CALLS",
            "timestamp_utc":datetime.now(timezone.utc).isoformat(),
            "git_commit":git.stdout.strip() if git.returncode==0 else "UNKNOWN",
            "runner_sha256":hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
            "cases":cases,"passed":sum(bool(c["pass"]) for c in cases),
            "total":len(cases),
            "decision":"MOCK PASS / LIVE GKE HOLD" if all(c["pass"] for c in cases) else "MOCK FAIL / HOLD",
            "limitations":[
                "Mocks do not verify GKE admission, RBAC, scheduling, networking, churn or metrics.",
                "SIGKILL, network partitions and lost runner processes cannot guarantee cleanup.",
                "Namespace existence check and subsequent creation are not atomic."
            ]}
    payload=json.dumps(result,indent=2)+"\n"
    (OUT/"mock_cleanup.json").write_text(payload)
    (OUT/"SHA256SUMS").write_text(hashlib.sha256(payload.encode()).hexdigest()+"  mock_cleanup.json\n")
    print(json.dumps({"passed":result["passed"],"total":result["total"],
                      "decision":result["decision"],"evidence":str(OUT.relative_to(ROOT))},indent=2))
    if result["passed"]!=result["total"]:
        sys.exit(2)

if __name__=="__main__":
    main()
