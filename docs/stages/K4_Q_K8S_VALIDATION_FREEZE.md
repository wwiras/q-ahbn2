# K4-Q — K8s-VAL-Q / Exp13-Q-K8s Protocol Freeze

**Status:** PASS / FROZEN — 2026-09-29

## Objective
Prospectively freeze the minimum bounded Kubernetes validation matrix after K0-Q through K3-Q established scope, mapping, parity and real-GKE runtime readiness.

## Scientific basis
This protocol is frozen before K5-Q formal outcomes are inspected. It reuses the pinned canonical Kubernetes lineage `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` and the frozen Q-AHBN2 learner. No ControlSim result is used to tune Kubernetes parameters.

The matched Kubernetes scenario is deliberately the closest **implementation-valid counterpart**, not a literal scale replication of Exp13-Q-Sim. The inherited, already validated K7 churn lineage established N=20, BA(m=2), 240 messages at 0.4 s, four absolute churn events at +1/+26/+51/+76 s, and seeds 42--46. Reusing that validated deployment realization is scientifically safer than introducing an unvalidated BA(100,m=3), 1,000-message Kubernetes protocol solely to mimic ControlSim scale.

## Frozen protocol

### 1. Evidence roles and one shared run matrix
One 25-run Kubernetes matrix is executed:

```text
5 methods x 5 seeds = 25 unique formal runs
methods = Gossip, Structured, DC-SoC, AHBN, Q-AHBN2
seeds   = 42, 43, 44, 45, 46
```

The five AHBN and five Q-AHBN2 cells simultaneously constitute **K8s-VAL-Q** (10 matched cells) and remain part of **Exp13-Q-K8s**. They are not rerun as a duplicate 10-run campaign.

Thus:
- K8s-VAL-Q evidence role: AHBN versus Q-AHBN2, 5 paired seeds / 10 cells;
- Exp13-Q-K8s evidence role: all five methods, 25 cells;
- unique K5-Q execution count: **25 runs**, no more and no less.

### 2. Topology and source
- Kubernetes peers: **N=20**.
- topology family: **Barabasi-Albert**.
- BA attachment parameter: **m=2**.
- source peer: **deterministic inherited K7 common non-structural source selected per seed**; it is excluded from both Structured CHs and DC-SoC COREs and from the frozen churn targets.
- seed controls topology/randomized scenario realization: **42--46**.
- each method at a given seed uses the same generated topology and churn-target schedule.

### 3. Churn condition
- one high-churn deployment condition only;
- four leave/rejoin cycles;
- absolute leave offsets from one common experiment epoch: **+1 s, +26 s, +51 s, +76 s**;
- churn target semantics and target-selection mechanism are inherited unchanged from the validated K7 lineage;
- target schedule must be generated prospectively from the seed/validated target-selection contract and recorded before the corresponding method outcomes are inspected;
- replacement pod readiness, gRPC liveness, leave/rejoin synchronization and method-specific maintenance follow the inherited validated runtime semantics;
- DC-SoC alone uses its frozen dynamic structural maintenance; no comparator receives another method's maintenance behavior.

The four-event deployment condition is the Kubernetes counterpart of the frozen Exp13-Q-Sim churn=0.40 scenario. The numeric 0.40 label is retained only as **scenario correspondence**; Kubernetes does not claim literal equivalence to the ControlSim fractional-churn mechanism.

### 4. Workload and timing
- **240 sequential messages**;
- **0.4 s planned message interval**;
- one absolute common-epoch injection grid;
- late blocking injections are sent as soon as the scheduler becomes available; lateness is logged and does not shift subsequent planned timestamps;
- no performance-dependent early stopping;
- existing inherited settle/health checks remain operational controls and must be recorded.

### 5. Methods and provenance
Exactly:
1. Gossip — inherited standalone GKE implementation;
2. Structured — inherited standalone GKE implementation;
3. DC-SoC — inherited frozen GKE implementation plus its validated churn maintenance;
4. AHBN — canonical GKE AHBN with final S5 requested-fanout actuator;
5. Q-AHBN2 — frozen Q-AHBN2 meta-controller above that same canonical AHBN/S5 proposal.

No comparator redesign, no new dissemination rule, no legacy Q-AHBN scientific semantics.

Q-AHBN2 remains frozen:
- state/action/reward/transition contract unchanged;
- alpha_Q=0.25;
- gamma=0.70;
- epsilon_0=0.30;
- epsilon_min=0.03;
- epsilon decay=0.995;
- canonical AHBN EWMA alpha=0.30 and S5 mapping unchanged.

### 6. Images and Git provenance
Before K5 execution:
- formal runtime must be built from the then-current K4-frozen `wwiras/q-ahbn2` Git commit;
- build target must be `linux/amd64`;
- use immutable formal image tag(s), never overwrite a formal tag;
- record registry digest, Git SHA, Dockerfile/provenance and Kubernetes cluster metadata;
- the K3 smoke image is validation provenance only and is not silently relabelled as the formal image.

### 7. Primary dissemination metrics
For every run:
- delivery_ratio;
- propagation_delay;
- duplicates;
- total_forwards.

Kubernetes-native recovery/timing diagnostics may be preserved where already emitted, but they are secondary deployment evidence and do not become a new primary superiority endpoint.

For Q-AHBN2 additionally preserve:
- Q decision/update traces;
- reward closures and NEW/DUPLICATE/FAILED attribution where naturally observed;
- action distribution;
- AHBN proposal versus Q refinement;
- requested/refined versus realized targets/fanout where available.

No composite Adaptation Efficiency score is introduced.

### 8. Pairing and analysis boundary
Seed is the blocking factor.

For K8s-VAL-Q:
- pair AHBN and Q-AHBN2 by seed;
- report method means, sample SD and two-sided 95% Student-t CI;
- report Q-AHBN2-minus-AHBN paired differences and 95% t-CI for each primary metric.

For Exp13-Q-K8s:
- report each method separately with n=5, mean, sample SD and 95% t-CI;
- Q-AHBN2-versus-reference paired seed contrasts may be reported under the already frozen Exp13-Q statistical rules;
- no omnibus score, winner ranking or pooling across unlike environments.

### 9. Validity, exclusions and reruns
A run is invalid only for independently documented operational/protocol defects, including:
- wrong method/seed/topology/source/churn schedule;
- image/Git provenance mismatch;
- incomplete workload caused by infrastructure/harness failure;
- missing/corrupt required artifacts;
- pod/runtime failure that prevents execution of the frozen protocol;
- failed required churn orchestration/maintenance invariant.

Rules:
- preserve every invalid original artifact;
- performance is never an invalidity reason;
- rerun the same frozen coordinate, never a replacement seed;
- if a shared seed-level scenario-generation defect affects comparability, rerun all affected method coordinates for that seed;
- no post-hoc parameter, timing, target, topology or workload changes after outcome inspection;
- all exclusions/reruns must be registered at K6-Q.

### 10. Required run artifacts
Each formal coordinate must preserve enough machine-readable evidence to establish:
- experiment/run ID, method and seed;
- Git SHA and image digest;
- topology and source;
- planned/actual message schedule;
- planned/actual churn milestones and targets;
- pod/runtime health;
- dissemination metrics;
- method-specific traces/maintenance;
- Q-AHBN2 learning traces for Q cells;
- completion/validity status.

All generated evidence remains under repository-local `output/evidence/` until K6-Q validity/completeness audit and deliberate Drive promotion.

## Explicit ControlSim <-> Kubernetes differences

| Dimension | Exp13-Q-Sim | Exp13-Q-K8s |
|---|---|---|
| Environment | ControlSim | real GKE deployment |
| N | 100 | 20 |
| BA m | 3 | 2 |
| workload | 1,000 sequential messages | 240 sequential messages |
| pacing | simulator event semantics | 0.4 s absolute injection grid |
| churn | target fraction 0.40, four cycles | four validated leave/rejoin cycles at +1/+26/+51/+76 s |
| infrastructure recovery | abstract simulator lifecycle | Kubernetes delete/replacement/Ready/gRPC lifecycle |
| method family | five methods | same five methods |
| seeds | 42--46 | 42--46 |
| source | 0 | deterministic inherited K7 common non-structural source per seed |
| principal metrics | delivery, delay, duplicates, forwards | same four |

Therefore Exp13-Q-K8s is a **matched cross-environment reference benchmark**, not a literal replication or numerical-equivalence test.

## Freeze decision
All K4-Q requirements are now prospectively specified without inspecting a K5 formal outcome.

$$\boxed{\textbf{K4-Q = PASS / FROZEN}}$$

## Next permitted action
**K5-Q-PREP — Formal Kubernetes Harness/Artifact Preparation and Pre-Execution Audit.**

K5-Q-PREP may implement only this frozen protocol and run local/static/preflight validation. It may not inspect formal performance outcomes. Real GKE formal execution remains a human/manual step after the preparation audit passes.

## K4-Q-A1 — Prospective source/orchestration reconciliation — 2026-09-29

Before any K5 formal coordinate was executed, formal-runner preparation exposed a contradiction in the initial K4 text: fixed Kubernetes `source=0` conflicts with the inherited validated K7 frozen churn target set `(0,5,10,15)`, where peer 0 is the first leave/rejoin target.

The pinned K7 authority already resolves this by deterministically selecting, for each seed, a common source that is neither a Structured cluster head nor a DC-SoC CORE and does not collide with the frozen churn targets. K4-Q is therefore prospectively amended to use that inherited source-selection rule. The target set, seeds, topology family/scale, workload, churn offsets and all algorithm semantics remain unchanged.

This correction occurred at 0/25 formal runs and before any formal outcome inspection. It prevents a source/churn-role confound and restores exact compatibility with the validated Kubernetes churn harness.

Formal-runner preparation also confirms that K5 must package the inherited K7 controller Job/orchestration assets and must route standalone AHBN through the final S5 actuator. K3 did not require those broader formal-comparison assets.

$$\boxed{\textbf{K4-Q-A1 = PASS / PROSPECTIVE AMENDMENT; no formal outcome existed}}$$
