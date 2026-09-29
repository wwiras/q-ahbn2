#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from gke.app.k5_q_formal_contract import frozen_summary, coordinates

ROOT=Path(__file__).resolve().parents[2]
required=[
    ROOT/'gke/app/qahbn2_runtime.py',
    ROOT/'gke/app/Dockerfile.qahbn2',
    ROOT/'gke/app/gen_topology.py',
    ROOT/'gke/app/dcsoc_maintenance.py',
    ROOT/'gke/app/k5_final_actuator_policy.py',
    ROOT/'gke/helm/ahbn/Chart.yaml',
    ROOT/'docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md',
]
missing=[str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    raise SystemExit('MISSING: '+', '.join(missing))
coords=coordinates()
assert len(coords)==25
assert len(set(coords))==25
summary=frozen_summary()
assert summary['unique_runs']==25
print(json.dumps({'status':'PASS','coordinates':len(coords),'contract':summary},indent=2))
