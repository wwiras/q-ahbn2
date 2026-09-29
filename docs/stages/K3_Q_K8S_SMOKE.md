# K3-Q — Bounded GKE Smoke

**Status:** PREP COMPLETE / MANUAL DOCKER+GKE SMOKE REQUIRED

## Objective
Run one bounded deterministic deployment smoke after K2-Q passes, verifying AHBN proposal, Q intervention, forwarding, outcome attribution, reward closure, transition handling, trace output, and deployment behavior.

## Boundary
Operational verification only; no formal performance claim.


## K3-Q-PREP — Deployable Runtime Assembly — 2026-09-29

### Scientific decision
Reuse the pinned `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` deployment/runtime lineage and add only the frozen Q-AHBN2 layer. No Gossip, Structured, DC-SoC or AHBN redesign is permitted.

### Assembly completed
Added under `q-ahbn2/gke/`:
- pinned inherited peer/runtime dependencies;
- pinned Helm deployment assets;
- `app/qahbn2_runtime.py` additive strategy wrapper;
- `app/Dockerfile.qahbn2`;
- `experiments/k3_q_smoke.yaml`;
- `scripts/run_k3_q_smoke.sh`;
- `PROVENANCE.md`;
- static preparation tests in `tests/test_k3_q_prep.py`.

The bounded smoke is intentionally tiny: 4 peers, BA(m=2), seed 42, source 0, four messages, no failure/churn/overload. Its purpose is end-to-end operational proof only, not performance evaluation.

### Required K3-Q operational evidence
A PASS requires deployed evidence for:
1. peer pods ready with no startup failure;
2. canonical AHBN update/proposal executes;
3. Q-AHBN2 decision trace exists;
4. realized targets exist under inherited semantics;
5. direct attempt outcome traces exist;
6. reward closure trace exists;
7. transition/Q-update path is operational across repeated decisions;
8. smoke summary is generated;
9. namespace cleanup succeeds;
10. artifacts remain under repository-local `output/evidence/`.

### Boundary
K3-Q cannot be closed from source inspection alone. A Docker image build/push plus real GKE smoke is required because this gate exists specifically to validate deployment/runtime behavior.

No K4 protocol freeze, K5 formal run, performance claim or result interpretation is authorized until K3-Q passes.

## Current result
$$\boxed{\textbf{K3-Q-PREP = PASS; K3-Q = HOLD — MANUAL DOCKER/GKE SMOKE REQUIRED}}$$

## Next permitted action
Build the Q-AHBN2 image from the current `q-ahbn2` commit, push it to the registry used by the GKE cluster, then execute only `gke/scripts/run_k3_q_smoke.sh`. Return the terminal output and generated smoke directory for verification.
