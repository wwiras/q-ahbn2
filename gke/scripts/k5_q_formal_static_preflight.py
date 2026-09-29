#!/usr/bin/env python3
from __future__ import annotations
import json,sys,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
APP=ROOT/"gke/app"
sys.path.insert(0,str(APP))
import k7_exp11_tools as tools
import k7_gen_topology  # noqa: F401
import gen_topology

base=ROOT/"gke/experiments/k5_q_formal.yaml"
report=[]
with tempfile.TemporaryDirectory(prefix="k5q-static-") as td:
    tmp=Path(td)
    for seed in tools.SEEDS:
        target=tools.write_target_selection(base,tmp/f"target_seed{seed}.json",seed)
        generated=[]
        sources=[]
        for method in tools.ALGORITHMS:
            cfg=tmp/f"{method}_seed{seed}.yaml"
            topo=tmp/f"{method}_seed{seed}.json"
            tools.write_config(base,cfg,method,seed)
            old=sys.argv
            try:
                sys.argv=["gen_topology.py","--config",str(cfg),"--out",str(topo)]
                gen_topology.main()
            finally:
                sys.argv=old
            tools.enrich_topology(topo,cfg)
            generated.append(topo)
            sources.append(json.loads(topo.read_text())["message_source"])
        tools.validate_topologies(generated)
        if len(set(sources))!=1:
            raise SystemExit(f"seed {seed}: source mismatch across methods: {sources}")
        if sources[0] in tools.FROZEN_TARGETS:
            raise SystemExit(f"seed {seed}: source collides with frozen churn target: {sources[0]}")
        report.append({"seed":seed,"source":sources[0],"targets":list(tools.FROZEN_TARGETS),
                       "methods":list(tools.ALGORITHMS),"target_selection_hash":target["selection_hash"]})
print(json.dumps({"status":"PASS","seeds":report,"coordinates":25},indent=2))
