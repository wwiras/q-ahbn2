#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path
from gke.app.k5_q_formal_contract import METHODS,SEEDS

if len(sys.argv)!=2:
    raise SystemExit('usage: validate_k5_q_artifacts.py <formal-output-dir>')
root=Path(sys.argv[1])
if not root.exists():
    raise SystemExit('formal output directory not found')
manifest=root/'matrix_manifest.json'
if not manifest.exists():
    raise SystemExit('missing matrix_manifest.json')
data=json.loads(manifest.read_text())
rows=data.get('runs',[])
coords={(int(r['seed']),str(r['method'])) for r in rows}
expected={(s,m) for s in SEEDS for m in METHODS}
if coords != expected or len(rows)!=25:
    raise SystemExit(f'matrix mismatch: expected 25 exact coordinates, got {len(rows)} rows / {len(coords)} unique')
required=('git_sha','image','image_digest','topology','status')
for r in rows:
    missing=[k for k in required if not r.get(k)]
    if missing:
        raise SystemExit(f"run {r.get('seed')}/{r.get('method')} missing {missing}")
print(json.dumps({'status':'PASS','runs':25,'coordinates':'complete'},indent=2))
