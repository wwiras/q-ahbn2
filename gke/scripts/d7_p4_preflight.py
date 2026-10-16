#!/usr/bin/env python3
"""D7-P4 read-only/local-only contract audit. Never deploys or runs experiments."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from gke.app.k5_q_formal_contract import (METHODS, SEEDS, NUM_NODES, BA_M,
    MESSAGE_COUNT, MESSAGE_INTERVAL_S, CHURN_OFFSETS_S, coordinates)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    out = ROOT / "output" / "evidence" / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-D7-P4-readonly")
    out.mkdir(parents=True, exist_ok=False)
    checks = []
    def check(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
    def source(path):
        p = ROOT / path
        check("exists:"+path, p.is_file())
        return p.read_text() if p.is_file() else ""
    c = source("gke/app/k5_q_formal_contract.py")
    base = source("gke/experiments/k5_q_formal.yaml")
    formal = source("gke/scripts/run_k5_q_formal.sh")
    runner = source("gke/scripts/run_k7_experiment.sh")
    tools = source("gke/app/k7_exp11_tools.py")
    helm = source("gke/helm/ahbn/templates/job-controller.yaml")
    stateful = source("gke/helm/ahbn/templates/statefulset.yaml")
    validator = source("gke/scripts/validate_k5_q_artifacts.py")
    check("matrix_25_unique", len(coordinates()) == 25 and len(set(coordinates())) == 25)
    check("five_frozen_methods", METHODS == ("gossip","structured","dcsoc","ahbn","qahbn2"))
    check("five_frozen_seeds", SEEDS == (42,43,44,45,46))
    check("frozen_topology", (NUM_NODES, BA_M) == (20, 2))
    check("frozen_workload", (MESSAGE_COUNT,MESSAGE_INTERVAL_S) == (240,0.4))
    check("frozen_churn", CHURN_OFFSETS_S == (1.,26.,51.,76.))
    check("base_configuration_tokens", all(x in base for x in ("numNodes: 20","baM: 2","messageCount: 240","messageInterval: 0.4","plannedLeaveOffsetsSec: [1.0, 26.0, 51.0, 76.0]")))
    check("formal_matrix_same_methods", "METHODS=(gossip structured dcsoc ahbn qahbn2)" in formal)
    check("formal_matrix_same_seeds", "SEEDS=(42 43 44 45 46)" in formal)
    check("generated_config_and_topology", "k7_exp11_tools.py config" in formal and "k7_gen_topology.py" in formal)
    check("common_target_topology_contract", "k7_exp11_tools.py contract" in formal)
    check("timing_validator_present", "validate_churn_timeline" in tools and "validate_planned_message_grid" in tools)
    check("per_run_artifact_validation", "k7_exp11_tools.py run" in formal and "matrix_manifest.json" in validator)
    check("pod_image_and_id_check", 'containerStatuses' in runner and 'imageID' in runner)
    check("logs_collection_present", "logs.jsonl" in runner and "controller.log" in runner)
    check("helm_controller_template", 'command: ["python", "controller.py"]' in helm)
    check("helm_peer_template", "image: {{ .Values.image }}" in stateful)
    # Explicit gating limitations: none can be considered verified by static inspection.
    blockers = [
        "No live GKE validation of generated Helm manifests/controller job, pod scheduling, events or workload/churn timing.",
        "No demonstrated separate 5-method smoke-only runner or isolation from the 25 formal runs.",
        "Experiment runner EXIT trap collects evidence but does not reliably uninstall release/delete namespace on early failure.",
        "No proven complete per-run trace/metric artifact collection and preservation following interrupted runs.",
        "No runtime test of schedule drift validity or four churn leave/down/rejoin cycles in this gate.",
        "Existing run_k5_q_formal.sh uses ddmmyyyy timestamps; ensure new evidence follows approved UTC naming.",
        "No live assessment of namespace uniqueness, role permissions and safe rollback for smoke tests.",
    ]
    paths = [
        "gke/app/k5_q_formal_contract.py", "gke/experiments/k5_q_formal.yaml",
        "gke/scripts/run_k5_q_formal.sh", "gke/scripts/run_k7_experiment.sh",
        "gke/app/k7_exp11_tools.py", "gke/scripts/validate_k5_q_artifacts.py",
        "gke/helm/ahbn/templates/job-controller.yaml",
        "gke/helm/ahbn/templates/statefulset.yaml",
    ]
    hashes = {p:sha(ROOT/p) for p in paths if (ROOT/p).exists()}
    git = subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,capture_output=True,text=True)
    result = {
        "gate": "JCC-R1A-C3-D7-P4",
        "scope": "LOCAL READ-ONLY PREFLIGHT; NO GKE ACTION",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git.stdout.strip() if git.returncode == 0 else "UNKNOWN",
        "checks": checks,
        "source_sha256": hashes,
        "unresolved": blockers,
        "decision": "HOLD / REMEDIATION REQUIRED",
        "smoke_runs": "0/5",
        "formal_runs": "0/25",
    }
    (out/"preflight.json").write_text(json.dumps(result,indent=2)+"\n")
    (out/"SHA256SUMS").write_text(f'{sha(out/"preflight.json")}  preflight.json\n')
    print(json.dumps({"checks_passed":sum(x["pass"] for x in checks),
                      "checks_total":len(checks),"decision":result["decision"],
                      "evidence":str(out.relative_to(ROOT))},indent=2))
    if not all(x["pass"] for x in checks):
        sys.exit(2)

if __name__ == "__main__":
    main()
