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


## K3-Q-D1 — Container Architecture Diagnostic — 2026-09-29

### Observed deployment failure
The first real GKE attempt did not reach Q-AHBN2 execution. Pods `peer-0` and `peer-1` entered restart/crash behavior with:

`exec /usr/local/bin/python: exec format error`

The failure occurred at container process startup, before the Python runtime could execute the Q-AHBN2 wrapper.

### Diagnosis
The K3 preparation instructions used a plain local `docker build` without an explicit target platform. On an Apple-silicon development host this can produce/push a Linux ARM64 image, whereas the established GKE e2-medium deployment lineage is x86-64/AMD64. The observed kernel-level `exec format error` is consistent with that architecture mismatch.

### Scientific classification
**Operational infrastructure/build-provenance defect; not scientific algorithm evidence.**

Therefore:
- no Q-AHBN2 result was produced;
- no K3 scientific criterion failed;
- no learner/controller/comparator/topology/parameter change is justified;
- the failed startup is retained as diagnostic provenance;
- rerunning the same bounded smoke after correcting image architecture is valid and does not constitute outcome-driven experimental rerunning.

### Corrective action
Added `gke/scripts/build_k3_q_image.sh` to build and push explicitly for `linux/amd64`, then inspect the pushed manifest. The K3 smoke runner now also refuses deployment unless the supplied image advertises `linux/amd64` and records the image manifest in its evidence directory.

## Current result after D1
$$\boxed{\textbf{K3-Q-D1 = PASS; K3-Q = HOLD — CORRECTED AMD64 SMOKE RERUN REQUIRED}}$$

## Next permitted action
Use the corrected build script to push a fresh immutable smoke tag, then rerun the unchanged bounded K3-Q smoke. No scientific configuration change is permitted.


## K3-Q-D2 — Registry Manifest Verification Correction — 2026-09-29

The corrected AMD64 build was pushed successfully as `wwiras/q-ahbn2:k3q-smoke-amd64-20260929`, digest `sha256:51f3473c1fdf9bbe8cfe7e0981be2cb5b4b2235c1114abd74dc1dfe847ba74b2`. Docker reported a single `application/vnd.docker.distribution.manifest.v2+json` manifest.

The prior K3 preflight incorrectly required the human-readable `docker buildx imagetools inspect` output to contain the literal string `linux/amd64`. A single-platform Docker v2 manifest need not print that string, so this was a verifier false negative.

Corrective action: `gke/scripts/verify_k3_q_image.sh` now parses the raw registry manifest and verifies architecture semantically. Both the build and smoke scripts use this verifier.

**Scientific classification:** operational verification correction only; no scientific configuration changed.

$$\boxed{\textbf{K3-Q-D2 = PASS; K3-Q remains HOLD pending unchanged smoke rerun}}$$
