#!/usr/bin/env python3
from pathlib import Path
from gke.app.k5_q_formal_contract import SEEDS, NUM_NODES, BA_M, MESSAGE_COUNT, MESSAGE_INTERVAL_S, CHURN_OFFSETS_S

ROOT = Path(__file__).resolve().parents[2]
runner = (ROOT / "gke/scripts/run_s17_qahbn2_remediation.sh").read_text()
base = (ROOT / "gke/experiments/k5_q_formal.yaml").read_text()

assert 'METHOD="qahbn2"' in runner
assert 'SEEDS=(42 43 44 45 46)' in runner
for forbidden in ('gossip structured dcsoc ahbn qahbn2', 'METHODS=(', 'FORMAL_SEED'):
    assert forbidden not in runner
assert 'output/evidence/q-ahbn-gke-${STAMP}-s17-qahbn2-remediation' in runner
assert 'gke/experiments/k5_q_formal.yaml' in runner
assert '--algorithm qahbn2' in runner
assert 's17_protocol_manifest.json' in runner
assert 'remediation_manifest.json' in runner
assert 'F_success' in runner and 'F_attempt' in runner

assert NUM_NODES == 20
assert BA_M == 2
assert MESSAGE_COUNT == 240
assert MESSAGE_INTERVAL_S == 0.4
assert tuple(CHURN_OFFSETS_S) == (1.0, 26.0, 51.0, 76.0)
assert tuple(SEEDS) == (42,43,44,45,46)

required = [
    'numNodes: 20',
    'baM: 2',
    'messageCount: 240',
    'messageInterval: 0.4',
    'plannedLeaveOffsetsSec: [1.0, 26.0, 51.0, 76.0]',
]
for token in required:
    assert token in base, token

print("S17-5 PREP AUDIT PASS")
print("scope=qahbn2-only seeds=42,43,44,45,46")
print("protocol=identical frozen K5 base")
print("namespace=separate post-remediation evidence family")
