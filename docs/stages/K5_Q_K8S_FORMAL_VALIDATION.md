# K5-Q — K8s-VAL-Q / Exp13-Q-K8s Formal Execution

**Status:** K5-Q-FORMAL-PREFLIGHT PASS / FORMAL 25-RUN EXECUTION RELEASED

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

## K5-Q-FORMAL-PREP — Locked formal runner reconciliation — 2026-09-29

Before formal run 1/25, inspection of the pinned `ahbn2_gke` K7 authority found that the K3 smoke assembly was intentionally narrower than the K5 five-method churn requirement. K5 therefore required additional inherited deployment assets before execution:
- K7 absolute-grid churn controller/orchestration;
- K7 target-selection/config/topology contract tooling;
- Helm controller Job;
- controller-side DC-SoC maintenance tracing;
- final-S5 routing for standalone AHBN;
- forwarding-attempt tracing required by inherited K7 validation;
- explicit Q-AHBN2 decision/outcome/reward evidence validation.

These assets were imported from pinned `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` and adapted only for repository layout plus the fifth `qahbn2` treatment. No new churn mechanism was designed.

### Prospective K4 source correction
The inherited K7 target set is `(0,5,10,15)`, so the earlier K4 statement `source=0` was internally inconsistent. At 0/25 formal runs, K4-Q-A1 prospectively replaced it with the inherited deterministic common non-structural source-selection rule. This prevents source/target collision and preserves the validated K7 design.

### Locked runner
`gke/scripts/k5_q_formal_static_preflight.py` prospectively generates all 25 configs/topologies without GKE, validates the inherited five-method matched-topology contract, and proves the per-seed source is common across methods and does not collide with `(0,5,10,15)`.

`gke/scripts/run_k5_q_formal.sh` is now the only prepared formal matrix runner. It:
- locks methods to Gossip, Structured, DC-SoC, AHBN, Q-AHBN2;
- locks seeds to 42--46;
- prospectively generates/validates target selection, configs and matched topologies;
- executes the inherited validated churn controller for each coordinate;
- validates each run before advancing;
- creates `matrix_manifest.json` only after 25 validated coordinates;
- runs the K5 artifact completeness validator;
- writes only under repository-local `output/evidence/`.

### Release hold
The previously built K5 image predates these required formal-controller/runtime additions. Therefore its successful preflight remains valid historical pre-execution evidence but it is **not the final K5 formal image**. A new immutable formal image must be built from the reconciled formal-runner/runtime HEAD and must pass the expanded container preflight (including controller import) before run 1/25.

$$\boxed{\textbf{K5-Q-FORMAL-PREP = PASS; K5-Q-FORMAL = HOLD pending rebuilt image + local static/preflight verification}}$$

## K5-Q-FORMAL-PREFLIGHT-S1 — Static 25-coordinate contract verification — 2026-09-29

Researcher-executed local verification after pulling the reconciled formal-runner commits:
- `tests.test_k5_q_prep`: **5/5 PASS**;
- K5 preparation audit: **PASS** with exactly 25 coordinates;
- no-GKE formal static preflight: **PASS**;
- all five methods generated and matched for each seed before any formal GKE execution;
- frozen targets for every seed: `(0,5,10,15)`;
- deterministic common non-structural source mapping:
  - seed 42 -> peer 1;
  - seed 43 -> peer 1;
  - seed 44 -> peer 1;
  - seed 45 -> peer 2;
  - seed 46 -> peer 1;
- each seed uses one identical source across Gossip, Structured, DC-SoC, AHBN and Q-AHBN2;
- no source collides with a frozen churn target;
- five distinct prospective target-selection hashes were recorded, one per seed.

This verifies the prospective matrix/source reconciliation without consuming cluster time and without inspecting any performance outcome.

$$\boxed{\textbf{K5-Q-FORMAL-PREFLIGHT-S1 = PASS}}$$

Remaining hold: build a fresh immutable formal image from the reconciled formal runtime/controller HEAD and pass the expanded image/controller import preflight before run 1/25.

## K5-Q-FORMAL-PREFLIGHT-D1 — Expanded import-preflight newline correction — 2026-09-29

The rebuilt v2 formal image completed build/push and registry platform verification as `linux/amd64`, with digest:
`sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`.

The subsequent container import preflight did not execute its imports because the host wrapper contained the literal characters `\\n` between `import qahbn2_runtime` and `import controller`, producing a Python `SyntaxError` before runtime import evaluation.

Classification: preflight-wrapper defect only. The registry image exists and its architecture verification passed; no formal GKE coordinate was executed and no scientific outcome was inspected.

Correction: replace the escaped literal with a genuine newline and add a regression guard preventing recurrence.

$$\boxed{\textbf{K5-Q-FORMAL-PREFLIGHT-D1 = PASS; S2 remains HOLD pending corrected container import preflight}}$$

## K5-Q-FORMAL-PREFLIGHT-S2 — Rebuilt immutable image/runtime/controller verification — 2026-09-29

Researcher-executed corrected preflight passed against the rebuilt formal image:
- image: `wwiras/q-ahbn2:k5q-formal-v2-20260929`;
- registry platform: `linux/amd64` PASS;
- immutable repo digest: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`;
- Q-AHBN2 runtime import: PASS;
- inherited formal controller import: PASS;
- container import preflight: PASS;
- image preflight: PASS.

The D1 wrapper syntax defect is therefore closed. No formal GKE coordinate has yet executed.

Final runner readback confirms fail-closed checks for exact image digest, expected GKE context, clean working tree, exact five methods x five seeds, prospective topology/target validation, per-coordinate inherited K7 validation, and final 25-coordinate `matrix_manifest.json` validation.

$$\boxed{\textbf{K5-Q-FORMAL-PREFLIGHT = PASS / CLOSED}}$$

### Released action
`K5-Q-FORMAL — execute exactly the locked 25-coordinate GKE matrix using the v2 image/digest above.`

## K5-Q-FORMAL-PREFLIGHT-D3 — Newline regression-test assertion correction — 2026-09-29

The final local regression reported 6/7 PASS with only `test_preflight_controller_import_is_real_line` failing. The traceback showed the production preflight file already contained genuine separate lines `import qahbn2_runtime` and `import controller`; therefore the runtime correction itself remained valid.

Root cause: the regression assertion used an escaped `\\n` expectation rather than a genuine newline expectation, so it tested for the defect instead of the correction. The test was repaired to require a genuine newline and reject the literal backslash-n form.

Classification: test-only defect. No runtime/image/controller/formal protocol change; v2 digest remains frozen; 0/25 formal GKE runs.

$$\boxed{\textbf{K5-Q-FORMAL-PREFLIGHT-D3 = PASS; final regression rerun required}}$$

## K5-Q-FORMAL-PREFLIGHT closure — 2026-09-29

Final researcher-executed local verification after all D1--D3 corrections:
- `tests.test_k5_q_prep`: **7/7 PASS**;
- K5 preparation audit: **PASS**;
- exact methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2;
- exact seeds: 42--46;
- exact unique formal coordinates: **25**;
- exact scenario: N=20, BA(m=2), 240 messages, 0.4 s planned interval, churn offsets +1/+26/+51/+76 s;
- inherited per-seed common-source policy confirmed;
- v2 image: `wwiras/q-ahbn2:k5q-formal-v2-20260929`;
- platform: `linux/amd64`;
- pinned digest: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`;
- real-container Q-AHBN2 runtime and formal-controller imports: PASS;
- formal host runner and Helm paths regression-guarded;
- formal runs executed before closure: **0/25**.

All known pre-execution implementation, provenance and orchestration gates are therefore satisfied.

$$\boxed{\textbf{K5-Q-FORMAL-PREFLIGHT = PASS / CLOSED}}$$

## Released action
**K5-Q-FORMAL — execute exactly the frozen 25-coordinate GKE matrix using the pinned v2 image digest.**

No scientific interpretation, selective stopping, seed substitution, performance-triggered rerun, or Drive promotion is authorized during K5-Q execution.

## K5-Q-FORMAL-D4 — Generated Helm topology provenance guard — 2026-09-29

The first released formal invocation stopped before coordinate execution because the clean-tree guard found one untracked file: `gke/helm/ahbn/topology.json`. `git diff` and `git diff --stat` were empty; no tracked file was modified.

This path is an inherited generated deployment artifact: the formal helper replaces it with each coordinate topology and restores its prior contents after execution. It is not source authority or formal evidence and must not make repository provenance dirty.

Prospective correction at 0/25 runs:
- explicitly ignore `gke/helm/ahbn/topology.json`;
- move the runner clean-tree check before evidence-directory creation or other formal-run mutation;
- capture the clean pre-run Git SHA and status for the evidence package;
- regression-guard both properties.

No scientific protocol, runtime image, topology-generation rule, coordinate, outcome, or frozen image digest changed.

$$\boxed{\textbf{K5-Q-FORMAL-D4 = PASS / administrative provenance correction; 0/25 runs}}$$

## K5-Q-FORMAL-D5 — Q-AHBN2 adaptive-trace validator reconciliation — 2026-09-29

The formal campaign progressed through seed 42 Gossip, Structured, DC-SoC and AHBN validation, then completed the seed42/Q-AHBN2 controller job but stopped in post-run validation at inherited line 360 with `ValueError: AHBN trace isolation failed`.

Code audit established a validator-contract inconsistency: the inherited isolation predicate admitted `ahbn_controller_trace` + `k5_final_actuator_decision` only when `algorithm == "ahbn"`, while the frozen Q-AHBN2 architecture explicitly executes canonical AHBN/S5 first and records `mode_ahbn`/`k_ahbn` before Q refinement. Therefore canonical AHBN/S5 traces are required evidence for both adaptive methods, not leakage in Q-AHBN2.

Minimal prospective validator correction:
- define adaptive methods as `{ahbn, qahbn2}`;
- require AHBN/S5 traces for both adaptive methods;
- continue forbidding them for Gossip, Structured and DC-SoC;
- apply the existing AHBN causal-field and selected-target checks to both adaptive methods;
- retain all existing Q-AHBN2-specific decision/outcome/reward checks unchanged.

No forwarding logic, controller logic, reward, learning parameter, topology, workload, image, method outcome or collected raw evidence was modified.

The stopped evidence directory must be preserved. The completed seed42/Q-AHBN2 artifacts may be revalidated in place only if complete; otherwise any rerun must follow the frozen same-coordinate operational-rerun rule. No full-campaign restart is authorized.

$$\boxed{\textbf{K5-Q-FORMAL-D5 = validator defect identified/corrected; execution HOLD pending local tests and stopped-run artifact revalidation}}$$
