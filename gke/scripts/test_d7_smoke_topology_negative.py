#!/usr/bin/env python3
"""Local-only real-validator smoke topology negative checks; never invokes kubectl."""
import hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[2]
NOW=datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))
OUT=ROOT/"output/evidence"/("JCC-R1A-C3-D7-SM-P1-TOPOLOGY_"+NOW.strftime("%Y%m%d%H%M%S"))
METHODS=("structured","dcsoc","ahbn","qahbn2")
ENV=dict(os.environ,PYTHONPATH=str(ROOT/"gke/app"))
def run(*args):
    return subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,env=ENV,capture_output=True,text=True,timeout=90)
def main():
    OUT.mkdir(parents=True,exist_ok=False)
    rows=[]
    with tempfile.TemporaryDirectory(prefix="d7-topology-contract-") as temp:
        t=Path(temp)
        paths=[]
        for method in METHODS:
            cfg=t/(method+".yaml")
            topo=t/(method+".json")
            a=run("gke/app/k7_exp11_tools.py","config","--base","gke/experiments/k5_q_formal.yaml","--out",cfg,"--algorithm",method,"--seed","42")
            if a.returncode: raise RuntimeError("config "+method+": "+a.stderr[-1500:])
            b=run("gke/app/k7_gen_topology.py","--config",cfg,"--out",topo)
            if b.returncode: raise RuntimeError("topology "+method+": "+b.stderr[-1500:])
            paths.append(topo)
        def check(name,inputs,expect_pass):
            p=run("gke/app/k7_exp11_tools.py","contract","--remaining-four-seed42",*inputs)
            ok=(p.returncode==0)==expect_pass
            rows.append({"case":name,"pass":ok,"exit_code":p.returncode,
                         "expected":"ACCEPT" if expect_pass else "REJECT",
                         "stderr":p.stderr[-1000:]})
        check("four_ordered_seed42",paths,True)
        altered=t/"wrong_seed.json"
        obj=json.loads(paths[0].read_text())
        obj["k7_exp11"]["seed"]=43
        altered.write_text(json.dumps(obj))
        check("wrong_seed",[altered,*paths[1:]],False)
        check("five_topologies",[*paths,paths[0]],False)
        check("three_topologies",paths[:3],False)
        check("wrong_order",[paths[1],paths[0],*paths[2:]],False)
    git=subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,capture_output=True,text=True)
    result={"gate":"JCC-R1A-C3-D7-SM-REMAINING-P1-FINAL-NEGATIVE",
            "scope":"REAL TOPOLOGY VALIDATOR / LOCAL ONLY / NO GKE",
            "timestamp_myt":NOW.isoformat(),"git_commit":git.stdout.strip(),
            "validator_sha256":hashlib.sha256((ROOT/"gke/app/k7_exp11_tools.py").read_bytes()).hexdigest(),
            "test_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "cases":rows,"passed":sum(x["pass"] for x in rows),"total":len(rows)}
    result["decision"]="LOCAL PASS / LIVE HOLD" if result["passed"]==result["total"] else "FAIL / HOLD"
    payload=json.dumps(result,indent=2)+"\n"
    (OUT/"topology_negative.json").write_text(payload)
    (OUT/"SHA256SUMS").write_text(hashlib.sha256(payload.encode()).hexdigest()+"  topology_negative.json\n")
    print(json.dumps({"passed":result["passed"],"total":result["total"],"decision":result["decision"],
                      "evidence":str(OUT.relative_to(ROOT)),"failed":[x["case"] for x in rows if not x["pass"]]},indent=2))
    if result["passed"]!=result["total"]:sys.exit(2)
if __name__=="__main__":main()
