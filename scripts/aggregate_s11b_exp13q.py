"""Deterministic S11-B PREP aggregator for frozen Exp13-Q reference benchmark.

PREP only: defines/validates aggregation logic. Formal execution belongs to S11-B-1.
No ranking, omnibus score, p-value selection, or S11-A input is permitted.
"""
from __future__ import annotations
import csv, hashlib, math, statistics
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

STUDENT_T_95_DF4=2.7764451051977987
FROZEN_SEEDS:Tuple[int,...]=(42,43,44,45,46)
METHODS:Tuple[str,...]=("gossip","structured","dcsoc","ahbn","qahbn2")
PRIMARY_METRICS:Tuple[str,...]=("delivery_ratio","propagation_delay","duplicates","total_forwards")
CHURN_LEVEL=0.40
EXPECTED_RUNS=25
DEFAULT_CSV=Path("output/evidence/Exp13-Q/q-ahbn-29092026081836-exp13q-formal/exp13q_formal.csv")

def compute_file_sha256(path:Path|str)->str:
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(65536),b""): h.update(chunk)
    return h.hexdigest()

def load_csv_rows(path:Path|str)->List[Dict[str,str]]:
    with open(Path(path),"r",encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def metric_summary(values:Dict[int,float],seeds:Sequence[int]=FROZEN_SEEDS)->Dict[str,Any]:
    if tuple(seeds)!=FROZEN_SEEDS or set(values)!=set(FROZEN_SEEDS):
        raise ValueError("Exp13-Q requires exactly frozen seeds 42-46")
    xs=[float(values[s]) for s in seeds]
    if not all(math.isfinite(x) for x in xs): raise ValueError("non-finite metric")
    mean=statistics.mean(xs); sd=statistics.stdev(xs)
    margin=STUDENT_T_95_DF4*sd/math.sqrt(5)
    return {"n":5,"mean":mean,"sd":sd,"ci95_low":mean-margin,"ci95_high":mean+margin,
            "seed_values":{str(s):values[s] for s in seeds}}

def paired_contrast(q:Dict[int,float],ref:Dict[int,float],reference_method:str,
                    seeds:Sequence[int]=FROZEN_SEEDS)->Dict[str,Any]:
    if reference_method not in ("gossip","structured","dcsoc","ahbn"):
        raise ValueError("reference method must be one of four frozen comparators")
    if set(q)!=set(FROZEN_SEEDS) or set(ref)!=set(FROZEN_SEEDS):
        raise ValueError("same-seed pairing incomplete")
    ds=[float(q[s])-float(ref[s]) for s in seeds]
    if not all(math.isfinite(x) for x in ds): raise ValueError("non-finite paired difference")
    mean=statistics.mean(ds); sd=statistics.stdev(ds)
    margin=STUDENT_T_95_DF4*sd/math.sqrt(5)
    return {"reference_method":reference_method,"n":5,"mean":mean,"sd":sd,
            "ci95_low":mean-margin,"ci95_high":mean+margin,
            "seed_differences_Q_minus_reference":{str(s):float(q[s])-float(ref[s]) for s in seeds}}

def validate_rows(rows:List[Dict[str,str]])->None:
    if len(rows)!=EXPECTED_RUNS: raise ValueError(f"expected 25 rows, got {len(rows)}")
    seen=set()
    for i,r in enumerate(rows):
        if r.get("method") not in METHODS: raise ValueError(f"unexpected method at row {i}")
        try: seed=int(r["seed"]); churn=float(r["churn_level"])
        except Exception as e: raise ValueError(f"invalid seed/churn at row {i}") from e
        if seed not in FROZEN_SEEDS: raise ValueError(f"unexpected seed {seed}")
        if not math.isclose(churn,CHURN_LEVEL,rel_tol=0,abs_tol=1e-12):
            raise ValueError(f"unexpected churn {churn}")
        key=(r["method"],seed)
        if key in seen: raise ValueError(f"duplicate cell {key}")
        seen.add(key)
        for m in PRIMARY_METRICS:
            if r.get(m,"")=="": raise ValueError(f"missing {m} at row {i}")
            x=float(r[m])
            if not math.isfinite(x): raise ValueError(f"non-finite {m}")
            if m=="delivery_ratio" and not 0<=x<=1: raise ValueError("delivery_ratio out of range")
            if m=="propagation_delay" and x<=0: raise ValueError("propagation_delay must be >0")
            if m in ("duplicates","total_forwards") and x<0: raise ValueError(f"{m} must be >=0")
    expected={(m,s) for m in METHODS for s in FROZEN_SEEDS}
    if seen!=expected: raise ValueError("incomplete frozen five-method matrix")

def aggregate_rows(rows:List[Dict[str,str]])->Dict[str,Any]:
    validate_rows(rows)
    by_method={m:{} for m in METHODS}
    for r in rows: by_method[r["method"]][int(r["seed"])]=r
    summaries={}
    for method in METHODS:
        summaries[method]={}
        for metric in PRIMARY_METRICS:
            vals={s:float(by_method[method][s][metric]) for s in FROZEN_SEEDS}
            summaries[method][metric]=metric_summary(vals)
    # Predeclared comparator family retained structurally; no p-values calculated.
    contrasts={}
    for ref in ("ahbn","gossip","structured","dcsoc"):
        contrasts[ref]={}
        for metric in PRIMARY_METRICS:
            q={s:float(by_method["qahbn2"][s][metric]) for s in FROZEN_SEEDS}
            r={s:float(by_method[ref][s][metric]) for s in FROZEN_SEEDS}
            contrasts[ref][metric]=paired_contrast(q,r,ref)
    return {"schema_version":"1.0.0","scope":"S11-B Exp13-Q bounded external reference benchmark",
            "churn_level":CHURN_LEVEL,"total_runs":25,"methods":list(METHODS),
            "frozen_seeds":list(FROZEN_SEEDS),"primary_metrics":list(PRIMARY_METRICS),
            "method_summaries":summaries,"qahbn2_paired_contrasts":contrasts,
            "p_values_calculated":False,"omnibus_score_calculated":False}

def aggregate_csv(path:Path|str=DEFAULT_CSV)->Dict[str,Any]:
    before=compute_file_sha256(path); rows=load_csv_rows(path); out=aggregate_rows(rows)
    after=compute_file_sha256(path)
    if before!=after: raise RuntimeError("source CSV mutated during read-only aggregation")
    out["source_csv"]=str(path); out["source_sha256"]=before
    return out

if __name__=="__main__":
    raise SystemExit("S11-B-PREP only: formal execution is intentionally disabled until S11-B-1.")
