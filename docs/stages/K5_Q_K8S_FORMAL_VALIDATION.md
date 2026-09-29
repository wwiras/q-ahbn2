# K5-Q — K8s-VAL-Q / Exp13-Q-K8s Formal Execution

**Status:** K5-Q-PREEXEC PASS / FORMAL GKE EXECUTION RELEASED

## Objective
Execute only the Kubernetes deployment-validation and matched reference-benchmark matrix frozen at K4-Q.

## Authorized evidence families
1. K8s-VAL-Q: AHBN versus Q-AHBN2 deployment validation.
2. Exp13-Q-K8s: Gossip, Structured, DC-SoC, AHBN and Q-AHBN2 matched reference benchmark.

## Frozen unique run matrix
The K4-Q protocol authorizes exactly:

```text
5 methods x 5 seeds = 25 unique formal GKE runs
methods = Gossip, Structured, DC-SoC, AHBN, Q-AHBN2
seeds   = 42, 43, 44, 45, 46
```

The AHBN and Q-AHBN2 cells serve both K8s-VAL-Q and Exp13-Q-K8s; they are not duplicated.

Frozen Kubernetes scenario:
- N=20;
- BA(m=2);
- source=0;
- 240 sequential messages;
- 0.4 s absolute planned injection interval;
- four absolute leave/rejoin offsets +1/+26/+51/+76 s;
- inherited validated GKE churn target/schedule semantics;
- exact K4-Q method/provenance boundaries.

## K5-Q-PREP — Harness / Artifact Preparation — 2026-09-29

### Repository reconciliation
Preparation began only after GitHub readback confirmed:
- K4-Q = PASS / FROZEN;
- K5-Q formal execution = not yet released;
- K6-Q remains the evidence-integrity/freeze gate;
- GitHub controls source/control state;
- repository-local `output/evidence/` is working output until K6 deliberate Drive promotion/readback.

No formal K5 outcome was inspected during preparation.

### Added preparation controls

`gke/app/k5_q_formal_contract.py`
- single executable representation of the 25 frozen coordinates;
- exact method set and seeds;
- exact N, BA m, source, workload and churn offsets;
- explicit shared evidence roles.

`gke/scripts/k5_q_prep_audit.py`
- fail-closed repository asset audit;
- verifies the exact 25-coordinate contract;
- verifies required inherited/runtime/deployment assets exist.

`gke/scripts/build_k5_q_formal_image.sh`
- requires a fresh formal image tag;
- runs the preparation audit before build;
- builds/pushes only `linux/amd64`;
- invokes the platform verifier;
- invokes the real-container import preflight before formal GKE use.

`gke/scripts/validate_k5_q_artifacts.py`
- post-execution completeness/provenance validator for the exact 25-coordinate matrix;
- requires a machine-readable `matrix_manifest.json`;
- rejects missing/extra coordinates and missing Git/image/digest/topology/status provenance.

`tests/test_k5_q_prep.py`
- guards exact methods/seeds;
- guards 25 unique coordinates;
- guards N=20, BA(m=2), source 0;
- guards 240 x 0.4 s workload;
- guards +1/+26/+51/+76 s churn offsets;
- rejects unapproved seed/method expansion.

### Scientific boundary
K5-Q-PREP does not:
- execute a formal GKE coordinate;
- inspect formal performance outcomes;
- change a method, learner parameter or canonical AHBN rule;
- change K4 topology/workload/churn/seeds;
- add a comparator, condition, metric or repetition;
- promote working output to authoritative Google Drive evidence.

The local Drive-synchronized repository remains the execution workspace only. Deliberate evidence promotion remains K6-Q work.

## K5-Q-PREP result
Preparation assets and fail-closed guards are present in GitHub and are suitable for local pre-execution verification.

$$\boxed{\textbf{K5-Q-PREP = PASS}}$$

## Remaining release boundary
Before the first formal GKE coordinate, the researcher must:
1. pull the current GitHub HEAD into the designated local synchronized workspace;
2. run the K5 preparation/unit tests locally;
3. build/push one fresh immutable formal `linux/amd64` image from that exact HEAD;
4. pass the real-container preflight;
5. return those pre-execution outputs for verification.

Only after those checks pass may the 25-run K5-Q formal matrix start.

## Boundary
Purpose: operational realization, bounded deployment behavior, and RO1-supported cross-environment reference evaluation. This is not a full replication of the ControlSim matrix and does not authorize redesign, retuning, selective reruns based on performance, or universal deployment claims.

Exp10-Q, Exp11-Q, Exp12-Q and Exp13-Q-Sim remain unchanged.

## Next permitted action
**K5-Q-PREEXEC — Human local regression + formal-image build/preflight.**

No formal GKE scientific coordinate is authorized until K5-Q-PREEXEC passes.

## K5-Q-PREEXEC-D1 — Formal-image build audit import-path correction — 2026-09-29

The local K5 preparation tests passed 4/4 and the standalone preparation audit passed with the exact 25-coordinate frozen contract. The subsequent formal-image build wrapper failed before Docker execution with:

`ModuleNotFoundError: No module named 'gke'`.

Root cause: `build_k5_q_formal_image.sh` invoked `python3 gke/scripts/k5_q_prep_audit.py` without placing the repository root on `PYTHONPATH`. This is an operational wrapper defect only; the same audit had already passed when invoked with `PYTHONPATH=.`.

Corrective action: the build wrapper now prepends the repository root to `PYTHONPATH` when invoking the preparation audit.

Scientific classification:
- no formal GKE coordinate executed;
- no Docker build started before the failure;
- no performance outcome inspected;
- no frozen K4-Q method/seed/topology/workload/churn/metric/learner rule changed.

$$\boxed{\textbf{K5-Q-PREEXEC-D1 = PASS; K5-Q-PREEXEC remains HOLD pending corrected image build/preflight}}$$

## K5-Q-PREEXEC closure — 2026-09-29

Researcher-executed pre-execution evidence:
- K5-Q preparation regression: 4/4 PASS;
- exact 25-coordinate preparation audit: PASS;
- immutable formal tag: `wwiras/q-ahbn2:k5q-formal-20260929`;
- registry/runtime platform: `linux/amd64` PASS;
- registry digest: `sha256:dc6c6ceeec0220e51b03f76313a3cfa6448be9647c00e0a68a8a6abccbf33f52`;
- real-container runtime import preflight: PASS;
- formal-image wrapper completion: `K5-Q FORMAL IMAGE PREP PASS`.

The digest equals the earlier K3 smoke-image digest because no containerized runtime content changed between those builds. This is acceptable content identity, not evidence that the later K5 control/harness commits are embedded in the image. Formal evidence must therefore record both the immutable image digest and the exact Git/control HEAD used to launch the K5 matrix.

Current Git/control release HEAD at closure: `a6cea140604a268fc0c781c8dcc2130eb1923efa`.

$$\boxed{\textbf{K5-Q-PREEXEC = PASS / CLOSED}}$$

## Released next action
**K5-Q-FORMAL — execute exactly the frozen 25-coordinate GKE matrix.**

No additional method, seed, condition, repetition, metric or tuning is authorized. Working output remains under `output/evidence/` and is not authoritative Drive evidence until K6-Q.
