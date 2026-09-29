"""S11-B-1 formal release runner for the frozen Exp13-Q external benchmark.

Writes deterministic aggregation evidence only. It does not interpret, rank, score,
or select algorithms.
"""
from __future__ import annotations
import argparse, csv, json, subprocess
from datetime import datetime
from pathlib import Path
from scripts.aggregate_s11b_exp13q import (
    DEFAULT_CSV, METHODS, PRIMARY_METRICS, aggregate_csv, compute_file_sha256
)

SUMMARY_COLUMNS=("method","metric","n","mean","sd","ci95_low","ci95_high",
                 "seed_42","seed_43","seed_44","seed_45","seed_46")

def git_head()->str:
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    except Exception:
        return "UNAVAILABLE"

def summary_rows(data):
    rows=[]
    for method in METHODS:
        for metric in PRIMARY_METRICS:
            s=data["method_summaries"][method][metric]
            rows.append({"method":method,"metric":metric,"n":s["n"],"mean":s["mean"],
              "sd":s["sd"],"ci95_low":s["ci95_low"],"ci95_high":s["ci95_high"],
              **{f"seed_{seed}":s["seed_values"][str(seed)] for seed in (42,43,44,45,46)}})
    return rows

def run_formal(source=DEFAULT_CSV, output_root=Path("output/evidence"))->Path:
    stamp=datetime.now().strftime("%d%m%Y%H%M%S")
    out=Path(output_root)/f"q-ahbn-{stamp}-s11b-aggregation-formal"
    if out.exists(): raise FileExistsError(out)
    data=aggregate_csv(source)
    out.mkdir(parents=True,exist_ok=False)
    agg=out/"s11b_exp13q_aggregation.json"
    summary=out/"s11b_exp13q_summary.csv"
    agg.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    with summary.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=SUMMARY_COLUMNS); w.writeheader(); w.writerows(summary_rows(data))
    manifest={"stage":"S11-B-1","classification":"deterministic aggregation evidence",
      "scope":"Exp13-Q external benchmark only","source_csv":str(source),
      "source_sha256":data["source_sha256"],"runs":25,"churn_level":0.40,
      "methods":list(METHODS),"primary_metrics":list(PRIMARY_METRICS),
      "p_values_calculated":False,"omnibus_score_calculated":False,
      "git_head":git_head(),"artifacts":{
        agg.name:compute_file_sha256(agg),summary.name:compute_file_sha256(summary)}}
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    run=("S11-B-1 Exp13-Q deterministic five-method external benchmark aggregation\n"
         f"Source: {source}\nSource SHA-256: {data['source_sha256']}\n"
         "Runs: 25/25; churn=0.40; methods: gossip, structured, dcsoc, ahbn, qahbn2\n"
         "Boundary: descriptive and predeclared same-seed contrasts only; no interpretation, ranking, omnibus score, or p-values.\n")
    (out/"RUN.md").write_text(run,encoding="utf-8")
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",type=Path,default=DEFAULT_CSV)
    p.add_argument("--output-root",type=Path,default=Path("output/evidence"))
    a=p.parse_args()
    print(run_formal(a.source,a.output_root))

if __name__=="__main__": main()
