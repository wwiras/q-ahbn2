# K5-Q — K8s-VAL-Q / Exp13-Q-K8s Formal Execution

**Status:** K5-Q-PREP PASS / MANUAL FORMAL GKE EXECUTION NOT YET STARTED

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
