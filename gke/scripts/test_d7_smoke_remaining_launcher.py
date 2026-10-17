#!/usr/bin/env python3
"""No-cloud exact-launcher regression: fake kubectl, git, helm, Python and runner."""
import hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"gke/scripts/run_d7_smoke_remaining.sh"
RUNNER=ROOT/"gke/scripts/run_k7_experiment.sh"
NOW=datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))
OUT=ROOT/"output/evidence"/("JCC-R1A-C3-D7-SM-P1-LAUNCHER_"+NOW.strftime("%Y%m%d%H%M%S"))
METHODS=["structured","dcsoc","ahbn","qahbn2"]
CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"

KUBECTL=r'''#!/bin/bash
set -e
printf 'kubectl %s\n' "$*" >> "$MOCK_LOG"
case "$1" in
 config) if [[ "$MOCK_CASE" == wrong_context ]]; then echo wrong-context; else echo "$MOCK_CONTEXT"; fi;;
 get) if [[ "$2" == namespace && "$MOCK_CASE" == namespace_exists && "$3" == qahbn2-d7-smoke-ahbn ]]; then echo "namespace/$3"; fi;;
 *) echo "UNEXPECTED kubectl" >&2; exit 81;;
esac
'''
HELM='#!/bin/bash\necho "UNEXPECTED helm" >&2\nexit 82\n'
GIT=r'''#!/bin/bash
printf 'git %s\n' "$*" >> "$MOCK_LOG"
case "$1" in
 status) if [[ "$MOCK_CASE" == dirty_git ]]; then echo ' M file'; fi;;
 rev-parse) echo 1111111111111111111111111111111111111111;;
 ls-remote) if [[ "$MOCK_CASE" == wrong_remote ]]; then echo '2222222222222222222222222222222222222222 refs/heads/main'; else echo '1111111111111111111111111111111111111111 refs/heads/main'; fi;;
 *) exit 83;;
esac
'''
PYTHON=r'''#!/bin/bash
set -e
printf 'python %s\n' "$*" >> "$MOCK_LOG"
case "$1" in
 *k5_q_prep_audit.py) echo '{"mock":true}';;
 *k7_gen_topology.py)
   while (( $# )); do if [[ "$1" == --out ]]; then shift; echo '{"mock":true}' > "$1"; exit 0; fi; shift; done; exit 84;;
 *k7_exp11_tools.py)
   action="$2"
   if [[ "$action" == config ]]; then
     while (( $# )); do if [[ "$1" == --out ]]; then shift; echo 'mock: true' > "$1"; exit 0; fi; shift; done
   elif [[ "$action" == contract ]]; then
     shift 3
     [[ "$#" -eq 4 ]] || exit 85
     for m in structured dcsoc ahbn qahbn2; do
       [[ "$1" == *"/\${m}_seed42.json" && -s "$1" ]] || exit 86
       shift
     done
     echo 'MOCK CONTRACT PASS'
   elif [[ "$action" == run ]]; then
     [[ "$MOCK_CASE" != validation_failure ]] || exit 87
     echo 'MOCK VALIDATION PASS'
   else exit 88; fi;;
 *) exit 89;;
esac
'''
FAKE_RUNNER=r'''#!/bin/bash
set -Eeuo pipefail
[[ "\${MOCK_RUNNER_OK:-}" == YES ]] || exit 90
method="\${NAMESPACE#qahbn2-d7-smoke-}"
printf 'runner %s\n' "$method" >> "$MOCK_LOG"
printf '{"changed":"%s"}\n' "$method" > "$(dirname "$0")/../helm/ahbn/topology.json"
echo 'mock log' > "$OUTDIR/experiment.log"
echo 0 > "$OUTDIR/experiment_exit_status.txt"
echo PASS > "$OUTDIR/cleanup_status.txt"
if [[ "$MOCK_CASE" == runner_failure && "$method" == structured ]]; then
  echo 17 > "$OUTDIR/experiment_exit_status.txt"
  exit 17
fi
if [[ "$MOCK_CASE" == cleanup_hold && "$method" == structured ]]; then
  echo HOLD > "$OUTDIR/cleanup_status.txt"
fi
'''

def write(path,s):
    path.write_text(s)
    path.chmod(0o700)

def test(case):
    with tempfile.TemporaryDirectory(prefix="p1-launcher-") as tmp:
        t=Path(tmp)
        for name in ("gke/scripts","gke/helm/ahbn","gke/app","gke/experiments","mockbin","output/evidence"):
            (t/name).mkdir(parents=True,exist_ok=True)
        shutil.copy2(SRC,t/"gke/scripts/run_d7_smoke_remaining.sh")
        write(t/"gke/scripts/run_k7_experiment.sh",FAKE_RUNNER)
        original='{"original":"PRESERVE"}\n'
        (t/"gke/helm/ahbn/topology.json").write_text(original)
        log=t/"calls.log"
        for name,script in (("kubectl",KUBECTL),("helm",HELM),("git",GIT),("mockpython",PYTHON)):
            write(t/"mockbin"/name,script)
        dest=t/"output/evidence/mock-run"
        env=dict(os.environ,PATH=str(t/"mockbin")+":/usr/bin:/bin",PYTHON=str(t/"mockbin/mockpython"),
                 MOCK_LOG=str(log),MOCK_CASE=case,MOCK_CONTEXT=CONTEXT,MOCK_RUNNER_OK="YES",
                 RESULT_ROOT=str(dest),SMOKE_REMAINING_AUTHORIZED="YES")
        env.pop("SMOKE_AUTHORIZED",None)
        if case=="no_auth":env.pop("SMOKE_REMAINING_AUTHORIZED",None)
        if case=="legacy_auth":env["SMOKE_AUTHORIZED"]="YES"
        if case=="wrong_image":env["IMAGE"]="unapproved-image"
        p=subprocess.run(["/bin/bash",str(t/"gke/scripts/run_d7_smoke_remaining.sh")],
                         cwd=t,env=env,capture_output=True,text=True,timeout=20)
        calls=log.read_text().splitlines() if log.exists() else []
        methods=[x.split(" ",1)[1] for x in calls if x.startswith("runner ")]
        restored=(t/"gke/helm/ahbn/topology.json").read_text()==original
        exitfile=dest/"smoke_exit_status.txt"
        sums=dest/"SHA256SUMS"
        hashes_ok=False
        if sums.exists():
            hashes_ok=True
            for line in sums.read_text().splitlines():
                digest,path=line.split("  ",1)
                f=dest/path.removeprefix("./")
                if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:
                    hashes_ok=False
        expected={"success_all":METHODS,"runner_failure":["structured"],
                  "cleanup_hold":["structured"],"validation_failure":["structured"]}.get(case,[])
        if case in ("success_all","runner_failure","cleanup_hold","validation_failure"):
            ok=dest.is_dir() and hashes_ok and exitfile.is_file() and restored and methods==expected
            if case=="success_all":
                ok=ok and p.returncode==0 and exitfile.read_text().strip()=="0" and (dest/"status.txt").exists()
            else:
                ok=ok and p.returncode!=0 and exitfile.read_text().strip()!="0"
                ok=ok and (dest/"runs/structured/experiment.log").exists()
            if case=="runner_failure":
                ok=ok and (dest/"runs/structured/experiment_exit_status.txt").read_text().strip()=="17"
            if case=="cleanup_hold":
                ok=ok and (dest/"runs/structured/cleanup_status.txt").read_text().strip()=="HOLD"
        else:
            ok=p.returncode!=0 and not dest.exists() and restored and not methods
        return {"case":case,"pass":bool(ok),"exit_code":p.returncode,"runner_methods":methods,
                "topology_restored":restored,"evidence_created":dest.exists(),
                "checksum_verified":hashes_ok,"stderr":p.stderr[-700:]}

def main():
    assert SRC.is_file() and RUNNER.is_file()
    OUT.mkdir(parents=True,exist_ok=False)
    cases=("no_auth","legacy_auth","wrong_context","dirty_git","wrong_remote",
           "namespace_exists","wrong_image","runner_failure","cleanup_hold",
           "validation_failure","success_all")
    rows=[test(x) for x in cases]
    commit=subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,capture_output=True,text=True)
    result={"gate":"JCC-R1A-C3-D7-SM-REMAINING-P1-LAUNCHER",
            "test_type":"EXACT SOURCE LAUNCHER; SANDBOX MOCK; NO GKE",
            "timestamp_myt":NOW.isoformat(),
            "commit":commit.stdout.strip() if commit.returncode==0 else "UNKNOWN",
            "launcher_sha256":hashlib.sha256(SRC.read_bytes()).hexdigest(),
            "runner_sha256":hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
            "test_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "cases":rows,"passed":sum(x["pass"] for x in rows),"total":len(rows),
            "decision":"MOCK PASS / LIVE HOLD" if all(x["pass"] for x in rows) else "MOCK FAIL / HOLD",
            "limitations":["Shared runner covered by separate 9/9 mock suite.",
                           "The actual GKE cluster is never contacted.","SIGKILL cannot guarantee cleanup."]}
    payload=json.dumps(result,indent=2)+"\n"
    (OUT/"launcher_mock.json").write_text(payload)
    (OUT/"SHA256SUMS").write_text(hashlib.sha256(payload.encode()).hexdigest()+"  launcher_mock.json\n")
    print(json.dumps({"passed":result["passed"],"total":result["total"],
                      "decision":result["decision"],"evidence":str(OUT.relative_to(ROOT)),
                      "failed":[x["case"] for x in rows if not x["pass"]]},indent=2))
    if result["passed"]!=result["total"]:sys.exit(2)

if __name__=="__main__":main()
