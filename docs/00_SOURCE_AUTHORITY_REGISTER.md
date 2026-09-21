# Q-AHBN2 Source Authority Register

**Document ID:** QAHBN2-DOC-00  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/00_SOURCE_AUTHORITY_REGISTER.md`  
**Status:** FROZEN SOURCE-AUTHORITY BASELINE  
**Freeze date:** 2026-09-19  
**Scope:** Source authority, reconciliation, provenance, and inheritance control only.

---

## 1. Purpose

This register defines the authoritative evidence hierarchy for Q-AHBN2 before any new controller design, implementation, parity testing, experiment execution, or manuscript claim is permitted.

It prevents three classes of error:

1. mixing legacy Q-AHBN semantics with the frozen canonical AHBN;
2. treating historically different ControlSim and Kubernetes Q-AHBN implementations as one parity-preserved learner; and
3. allowing historical experimental results to validate design choices that have not yet been reconstructed and tested under Q-AHBN2.

This document records the conclusions of the completed read-only reconciliation gates R1, R2, and R3. It does **not** define the redesigned Q-AHBN2 state, action values, reward equation, hyperparameters, training lifecycle, or implementation.

---

## 2. Authoritative Source Inventory

| Authority level | Source | Pinned reference | Role |
|---|---|---|---|
| 1 | `wwiras/ahbn` | `936a79480bc1252c79b6ee01f65c88c740af2844` [ahbn repo](https://github.com/wwiras/ahbn) | Normative canonical AHBN implementation boundary. Represents the v0.63 baseline plus later canonical S5/parity corrections for control sim |
| 2 | `wwiras/ahbn2_gke` | `cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` [ahbn2_gke](https://github.com/wwiras/ahbn2_gke) | Normative canonical Kubernetes AHBN repository snapshot. The final GKE AHBN runtime is composite: the parity-validated controller/observation/dispatch base plus the frozen S5 actuator runtime used by the later K6/K7/K8 experiment images. |
| 3 | Revised AHBN Scientific Reports manuscript, 17 Sep 2026 | [AHBN17Sept2026_manuscriptSRpt.pdf](https://drive.google.com/file/d/1YarltXx8bZf0QWlIJeaKIIX6KCsCMPYJ/view?usp=drive_link) | Normative scientific description and interpretation of the frozen AHBN mechanism and its limitations. |
| 3A | RO2 characterization manuscript draft, 04 Apr 2026 | [Characterizing Latency Duplication Trade-off in Blockchain Dissemination A Systematic Study of Gossip and Structured Broadcast](https://drive.google.com/file/d/1fIpDLWE2pMTJMnnUXVXzYWRNUFFIJ0jS/view?usp=sharing) | Authoritative RO2 evidentiary source for the dissemination trade-off characterization used to justify Q-AHBN2 state/action design decisions, including fanout, Gossip-vs-Structured behavior, failure/overload, churn, and heterogeneity findings. Exact Drive/GitHub URL to be recorded when the artifact is archived at a durable project location. |
| 4 | `wwiras/q-ahbn` | `7bca26213cbfb2099cff8b2f659008b8e040b238` [q-ahbn repo](https://github.com/wwiras/q-ahbn) | Historical ControlSim Q-AHBN implementation and evidence only. |
| 5 | `wwiras/q-ahbn_gke` | `a9af5ccb9b564d5f2c2daaeeb9a04b191780cdbe` [q-ahbn_gke repo](https://github.com/wwiras/q-ahbn_gke) | Historical Kubernetes/GKE Q-AHBN implementation and evidence only. |
| 6 | Historical Q-AHBN manuscript draft | [Q_AHBN_FirstDraft.pdf](https://drive.google.com/file/d/1NahEY5sZPdwhpg2uduBxIxqyS3ikMGqj/view?usp=drive_link) | Historical design narrative and experiment context only; non-authoritative where it conflicts with levels 1–4. |
| 7 | Q-AHBN2 Master Research, Development, Experiment and Publication Contract v1.0 | `docs/00_QAHBN2_MASTER.md` | Authoritative Q-AHBN2 operating/workflow contract: project governance, stage/freeze sequence, evidence handling, experiment/publication workflow, and new-session bootstrap. It does not override Levels 1–2 scientific AHBN authority or independently define the future Q-AHBN2 RL specification. |

### 2.1 Canonical AHBN reference boundary

The canonical implementation reference is **not** the 1 Sep 2026 v0.63 commit alone. The normative boundary is the v0.63 baseline plus the later canonical S5 and parity corrections through:

`936a79480bc1252c79b6ee01f65c88c740af2844`

Relevant history includes:

- `1502589e50173711a0275470968ab829ecb3062a` — v0.63 Exp09 density final freeze;
- `ffdadca3bebe995d32d1f11e961f4dbf5adf7ee4` — CR-1 canonical S5 freeze/regression protection;
- `936a79480bc1252c79b6ee01f65c88c740af2844` — remove AHBN fanout cap and validate canonical `k=2..6`.

Older stage documentation that describes an earlier 2/3/4 fanout mapping is superseded by the current canonical implementation, regression validator, and later reconciliation history.

For Kubernetes, the pinned repository snapshot is `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`. Its provenance is intentionally composite. `app/ahbn_controller.py` preserves the earlier parity-validated S0 controller core with fanout 2/3/4, while the final S5 actuator was validated in K5 and is applied by the frozen stage runtime wrappers (`k5_final_actuator_runtime.py`, inherited by the K6/K7/K8 experiment images) using the same controller score and mode but the final requested-fanout mapping 2/3/4/5/6. Therefore, the old `AHBNParams.max_fanout=4` in the GKE base module must not be misread as the final scientific actuator boundary.

---

## 3. Authority and Precedence Rules

When two sources disagree, Q-AHBN2 uses the following precedence:

```text
canonical AHBN implementation
        >
revised 17-Sep-2026 AHBN scientific description
        >
future explicitly frozen Q-AHBN2 design contract
        >
new Q-AHBN2 implementation
        >
legacy ControlSim/GKE Q-AHBN implementations
        >
historical Q-AHBN manuscript draft
```

Additional rules:

1. Legacy Q-AHBN repositories may explain historical design choices but may not override canonical AHBN.
2. The revised AHBN manuscript controls scientific terminology and interpretation where legacy drafts differ.
3. A future Q-AHBN2 design contract may define the learning layer but may not silently redefine the frozen AHBN mechanism.
4. Environment-specific sensing/normalization is permitted only where the logical observation semantics remain explicit and compatible with the canonical boundary.
5. Historical results remain historical evidence. They are not prospective validation of Q-AHBN2.\n6. `docs/00_QAHBN2_MASTER.md` governs Q-AHBN2 workflow and project operation. Where it refers to scientific AHBN mechanism details, the pinned canonical AHBN implementation and revised AHBN manuscript remain controlling.

---

## 4. R1 — Canonical AHBN Mechanism Reconciliation

**Gate result: PASS.**

R1 reconciled both frozen implementation environments—ControlSim (`wwiras/ahbn`) and Kubernetes (`wwiras/ahbn2_gke`)—with the 17-Sep-2026 revised AHBN manuscript. The original R1 established the ControlSim side; the 19-Sep-2026 R1-GKE delta reconciliation added the canonical Kubernetes implementation without reopening AHBN design.

The canonical scientific object is:

```text
raw local measurements
        ↓
environment-specific normalization to [0,1]
        ↓
d, l, u, c
        ↓
EWMA α = 0.30
        ↓
d_hat, l_hat, u_hat, c_hat
        ↓
z = -d_hat + l_hat + u_hat + c_hat
        ↓
w = sigmoid(z)
        ↓
canonical mode + requested fanout
        ↓
mode-specific eligible-target selection
        ↓
realized forwarding
        ↓
outcomes / next observations
```

### 4.1 Frozen controller semantics

- observations: duplicate, latency, utilization/processing pressure, churn/instability;
- all logical observations normalized to `[0,1]`;
- EWMA `alpha = 0.30`;
- centres are zero;
- score: `z = -d_hat + l_hat + u_hat + c_hat`;
- weight: `w = sigmoid(z)`;
- `w >= 0.5` / `z >= 0` selects Gossip;
- otherwise Structured mode (implementation label `cluster`);
- requested fanout belongs to `{2,3,4,5,6}`;
- S5 mapping:
  - `z <= -0.25 -> 2`
  - `-0.25 < z < 0.25 -> 3`
  - `0.25 <= z < 0.90 -> 4`
  - `0.90 <= z < 1.50 -> 5`
  - `z >= 1.50 -> 6`.

The requested action and realized forwarding are distinct:

`0 <= k_real <= min(k_request, |N_e|)`.

Equality is not guaranteed because topology, immediate-sender exclusion, node activity, and mode-specific structural eligibility constrain realization.

### 4.2 R1 interpretation guards

- `w` is **not** a probabilistic Gossip/Structured mixture.
- There is no third dissemination mode.
- Observation cadence is environment-specific. In ControlSim, an omitted optional observation retains its previous EWMA state; absence of a supplied observation is not equivalent to a zero observation. In the canonical GKE adapter, every controller update supplies a complete interval snapshot, and an interval component with no observed event can legitimately be `0.0` (for example, no churn events in that window). These semantics must not be conflated.
- The controller latency observation is local one-hop latency and must not be conflated with experiment-level propagation delay.
- Controller utilization pressure must not be conflated with experiment-level total forwards.
- Trace `fanout` is the controller-requested fanout unless explicitly recorded otherwise.
- Canonical AHBN does not use tau-based suppression.

### 4.3 R1-GKE delta reconciliation (19 Sep 2026)

**Result: PASS, with environment-specific observation semantics explicitly recorded.**

The pinned Kubernetes repository was inspected read-only at `cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`. No Q-AHBN2 code was modified.

The GKE logical controller agrees with the frozen scientific contract on the four normalized observations, EWMA `alpha=0.30`, zero centres, coefficient signs, `z=-d_hat+l_hat+u_hat+c_hat`, sigmoid, `weight >= 0.5` Gossip / otherwise Structured, and the final S5 requested-fanout mapping. Repository K1/K2/K3.1 evidence records controller, observation, dispatch, trace, and ControlSim/Kubernetes parity checks for the base port. K5 then validated and froze S5 as the final actuator, and the later K6/K7/K8 images execute through the S5 runtime wrapper.

The GKE observation adapter is intentionally environment-specific:

| Logical input | Canonical GKE acquisition/normalization |
|---|---|
| duplicate `d` | interval duplicates / interval received; 0 when no receives |
| latency `l` | mean local one-hop latency in the interval divided by the fixed 1.0 s reference and clipped to [0,1] |
| utilization `u` | binary local overload pressure: 1 when `overload_ms > 0`, otherwise 0 |
| churn `c` | interval joins + leaves divided by current neighbour count (minimum denominator 1), clipped to [0,1] |

`snapshot_and_reset()` closes and resets the local observation window. A duplicate receipt records its observation, updates AHBN, and returns without forwarding. A first receipt records its local one-hop latency and reaches `target_peers()`, which performs the AHBN update before target selection. Failed/recovered neighbour communication changes the unavailable-neighbour set and records leave/join observations; `trigger_failure_reaction()` itself logs the observation and does not directly force mode or fanout.

Final S5 GKE execution preserves the controller score and mode and replaces only the requested forwarding budget using:

`z <= -0.25 -> 2`; `-0.25 < z < 0.25 -> 3`; `0.25 <= z < 0.90 -> 4`; `0.90 <= z < 1.50 -> 5`; `z >= 1.50 -> 6`.

Gossip eligibility excludes self, the immediate sender, and unavailable neighbours, then samples up to the requested budget. Structured head forwarding prioritizes one eligible gateway, then eligible local members, then additional gateways within the budget; a Structured member forwards only to its eligible cluster head. Consequently realized forwarding remains topology/availability constrained and can be below the requested fanout.

The S5 runtime trace explicitly distinguishes `requested_fanout` from `actual_fanout`. The underlying base-controller field named `canonical_fanout` is the earlier S0 2/3/4 proposal and is retained only as provenance; it is **not** the final S5 requested fanout. Q-AHBN2 must use the final S5 requested action as the canonical AHBN base proposal.

R1-GKE classification:

- controller equation, EWMA, sigmoid and mode rule: **MATCH**;
- logical observation meanings `d,l,u,c`: **MATCH**;
- raw sensing/normalization and update-window semantics: **DIFFERENT-BUT-VALID / environment-specific**;
- final S5 requested fanout: **MATCH**, implemented as a validated runtime layer over the earlier S0 base module;
- Gossip/Structured eligibility and budget realization: **MATCH** at the scientific-contract level;
- failure handling: **MATCH** with the no-controller-bypass rule;
- requested-versus-realized fanout observability: **MATCH**, with the GKE-specific `canonical_fanout` provenance-name guard;
- experiment-level outcome metrics versus controller observations: **MUST REMAIN DISTINCT**.

**R1-GKE gate: PASS.** No canonical AHBN redesign or Q-AHBN2 implementation change is required. The R1 amendment changes source completeness and environment-specific interpretation, not the frozen AHBN scientific law.

---

## 5. R2 — Legacy Q-AHBN Reconstruction

**Legacy reconstruction: PASS.**  
**ControlSim-to-GKE RL parity: NOT ESTABLISHED.**

Both legacy systems share the architectural intention:

`AHBN proposal -> Q-learning meta-action -> final decision`.

However, they do **not** implement one common RL agent.

### 5.1 Historical ControlSim

The historical learner uses a seven-component discrete state involving `d_hat`, `l_hat`, `u_hat`, `rho_hat`, `r_hat`, historical `c_hat`, and a failure phase. Its six actions modify combinations of fanout, controller weight, and tau. Its active reward is a multi-component delivery/overhead/recovery formulation. It uses standard tabular Q-learning with historical defaults including `alpha=0.25`, `gamma=0.90`, and epsilon-greedy exploration.

The historical meanings of `rho_hat`, `r_hat`, and particularly `c_hat` are not the R1 canonical semantics. Canonical R1 reserves `c_hat` for churn/instability.

### 5.2 Historical GKE

The historical GKE learner uses a four-component state based on duplicate ratio, failure pressure, overload/bottleneck pressure, and phase. Its six action names resemble ControlSim but their effects differ. Its reward is materially different from ControlSim.

The GKE base `adaptive_update()` is not the R1 canonical AHBN chain. It therefore cannot be inherited as the Q-AHBN2 base controller.

The historical GKE implementation also contains a hard-coded failure reaction outside ordinary Q-table action selection that forces Gossip and increases fanout, while a Q-AHBN path may log the behavior as `recovery_push`. Such behavior cannot be used as evidence of a learned action in Q-AHBN2.

Its target-realization path also differs from R1 by adding structural-backbone targets after Gossip sampling.

### 5.3 R2 scientific conclusion

The legacy work establishes a **design antecedent**, not a frozen cross-platform RL specification.

It supports:

- AHBN-first meta-control;
- tabular Q-learning;
- local/discrete state;
- bounded intervention concepts;
- epsilon-greedy exploration;
- dissemination-effectiveness versus overhead reward intent;
- explicit learning/intervention observability.

It does not establish a common ControlSim/Kubernetes state, action semantics, reward, recovery mechanism, or realization path.

### 5.4 R2-GKE delta reconciliation (19 Sep 2026)

**Result: PASS. Existing R2 conclusions are strengthened; two classifications are narrowed and one lifecycle fact is resolved for the historical GKE core.**

The historical Kubernetes learner at `wwiras/q-ahbn_gke@a9af5ccb9b564d5f2c2daaeeb9a04b191780cdbe` was compared directly against the canonical Kubernetes AHBN boundary at `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`. No Q-AHBN2 implementation was changed.

The comparison confirms that the historical GKE Q-AHBN was not layered over the now-canonical GKE AHBN implementation. Its `adaptive_update()` derives cumulative duplicate pressure plus explicit fail/bottleneck/overload pressures and applies hand-written mode/fanout rules. The canonical GKE implementation instead acquires interval `d,l,u,c` through `KubernetesObservationAdapter`, applies the frozen EWMA/score/sigmoid/mode law, and uses the final S5 requested-fanout runtime. Consequently the historical GKE `ahbn_mode`/`ahbn_fanout` fields record the proposal of the historical rule-based baseline, not the R1 canonical AHBN proposal.

The historical four-component Q state remains a useful antecedent only. It uses duplicate ratio, fail pressure, combined overload+bottleneck pressure, and a disturbance phase. These variables do not constitute the canonical GKE `d_hat,l_hat,u_hat,c_hat` state. Historical `fail_pressure` is a decaying ad-hoc failure signal, historical overload/bottleneck pressure is not the canonical EWMA utilization state, and canonical local one-hop latency is absent from the historical RL state. The existing **REDESIGN** classification for GKE state/discretization is therefore confirmed.

The historical six action names remain candidate semantic labels only. They apply direct fanout deltas and optional forced mode preferences to the historical proposal. They were not defined relative to the final canonical S5 requested action. Exact effects therefore remain **REDESIGN**, while numerical magnitudes remain **REJECT as authority**. The no-intervention `ahbn_base` concept remains **RETAIN**, but in Q-AHBN2 it must mean leaving the actual canonical S5 AHBN proposal unchanged.

The historical reward remains **REDESIGN**. It uses a local new-reception ratio, duplicate pressure, cumulative forwarding-count normalization, and a positive failure-pressure term. Direct comparison with canonical GKE confirms these are learner-specific historical signals rather than canonical AHBN observations or experiment-level delivery/recovery metrics.

The historical Q update remains a retained learning-family antecedent: zero-initialized tabular Q values, one-step previous-state/action update, epsilon-greedy choice, and per-decision epsilon decay. Exact `alpha`, `gamma`, epsilon values and schedules remain **DEFER**, not frozen by historical agreement.

The canonical comparison strengthens two prior rejections. Historical `trigger_failure_reaction()` directly raises fail pressure, forces Gossip, changes fanout, and for Q-AHBN logs `q_action="recovery_push"` outside `GKEQLearner.choose()`; canonical GKE `trigger_failure_reaction()` only logs the failed-neighbour observation while join/leave sensing feeds the ordinary controller path. The historical behavior is therefore **REJECT** as learned-action evidence and **REJECT** as canonical AHBN inheritance. Historical Gossip target realization also samples up to fanout and then appends structural-backbone targets, so realized forwarding can exceed the requested budget; canonical GKE keeps selection within the requested budget. Historical target realization therefore remains **REJECT**.

One earlier R2 statement can now be narrowed: the historical GKE learner's **core in-process lifecycle is resolved**. One `GKEQLearner` is constructed per Q-AHBN pod at `PeerState` initialization, its Q-table and previous transition are in memory, and the inspected core contains no persistence/load mechanism. Thus a fresh process starts a fresh learner unless an external runner restores state; no such restoration is established by the inspected core. Experiment-runner/pod-replacement lifecycle beyond this core remains unresolved and must be audited separately if needed.

R2-GKE disposition delta:

| R2 item | Previous disposition | R2-GKE amendment |
|---|---|---|
| AHBN-first meta-controller architecture | RETAIN | RETAIN, but base proposal must explicitly mean canonical GKE S5 AHBN, not historical `adaptive_update()` |
| historical GKE state/discretization | REDESIGN | unchanged; strengthened by direct canonical observation comparison |
| six action labels/semantics | REDESIGN | unchanged; redefine relative to canonical S5 proposal |
| `ahbn_base` no-intervention action | RETAIN | unchanged; narrowed to leave canonical S5 proposal unchanged |
| historical GKE reward | REDESIGN | unchanged |
| tabular one-step Q update / epsilon-greedy concept | RETAIN | unchanged |
| exact learning hyperparameters | DEFER | unchanged |
| historical simplified `adaptive_update()` as AHBN | REJECT | unchanged; direct canonical GKE comparison confirms incompatibility |
| hard-coded `recovery_push` failure reaction | REJECT | unchanged; canonical GKE proves failure observation need not bypass controller |
| historical target realization | REJECT | unchanged; canonical GKE budget semantics contradict backbone append |
| proposal/final-decision/intervention logging | RETAIN | RETAIN concept, but historical AHBN proposal fields are not canonical-proposal evidence |
| per-pod in-memory learner construction | UNRESOLVED | **RESOLVED for core implementation** |
| persistence across external run/pod lifecycle | DEFER / UNRESOLVED | remains unresolved outside inspected core |

**R2-GKE gate: PASS.** No R3 disposition category needs reversal. R3 remains valid, with these semantic clarifications carried forward to the future Q-AHBN2 design contract.

---

## 6. R3 — Reconciliation Decision Register

**Gate result: PASS — CONSOLIDATED AFTER R1-GKE AND R2-GKE.**

R3 converts the completed ControlSim and Kubernetes reconciliation findings into controlled inheritance dispositions without selecting redesigned Q-AHBN2 values. The 19-Sep-2026 consolidation incorporates the canonical GKE and historical GKE delta audits. **No original R3 disposition category is reversed.** The amendments clarify what “canonical AHBN base proposal,” “environment-specific sensing,” “no intervention,” and GKE lifecycle mean across both environments.

### 6.1 RETAIN

The following concepts may cross into the Q-AHBN2 design stage:

- Q-AHBN as a meta-controller layered after canonical AHBN;
- canonical AHBN as the source of the unmodified base proposal in both environments: ControlSim uses the frozen canonical controller directly; Kubernetes uses the parity-validated controller/observation/dispatch base plus the frozen final S5 runtime actuator;
- tabular Q-learning as the baseline learning family;
- epsilon-greedy exploration as an admissible mechanism;
- decentralized/local operation;
- a no-intervention / AHBN-base action capability, defined as leaving the **actual canonical AHBN proposal unchanged**;
- reward objective balancing dissemination effectiveness with overhead rather than minimizing forwarding alone;
- one-step previous-state/action Q-learning lifecycle;
- requested-versus-realized fanout distinction;
- logging the canonical base AHBN proposal;
- logging the final post-Q decision;
- explicit learner-intervention indicators;
- Q-state/action/reward/update observability;
- environment-specific raw sensing/normalization and observation cadence where they map into the explicit common logical AHBN contract;
- mode-specific eligible-target realization under the canonical requested-fanout budget.

### 6.2 REDESIGN

The following functions remain scientifically relevant but no legacy implementation is authoritative:

- RL state representation;
- state discretization;
- action-space semantics;
- fanout intervention semantics relative to the canonical S5 requested fanout;
- mode intervention semantics relative to the canonical AHBN mode proposal;
- any possible Q-layer weight intervention, which must remain semantically separate from the untouched canonical `sigmoid(z)`;
- reward equation and coefficients;
- common ControlSim/Kubernetes RL contract;
- any mapping from environment-specific raw measurements to additional RL-only state beyond the frozen AHBN observations.

**REDESIGN does not mean “copy the legacy mechanism and change its numbers.”** It means the function/problem is retained while its new definition requires independent justification and cross-environment semantics.

### 6.3 REJECT

The following must not be inherited as Q-AHBN2 design authority:

- the legacy seven-variable ControlSim state copied verbatim;
- the historical four-component GKE state copied verbatim;
- historical `c_hat = capacity` semantics;
- treating historical GKE `fail_pressure` as canonical churn `c`;
- treating historical GKE overload/bottleneck pressure as canonical EWMA utilization `u_hat`;
- the old latency-derived failure-phase formula;
- tau as a Q-AHBN2 actuator inherited from legacy ControlSim;
- legacy numerical action magnitudes as authoritative values;
- legacy GKE `adaptive_update()` as canonical AHBN;
- interpreting historical GKE `ahbn_mode` / `ahbn_fanout` logs as canonical AHBN proposal evidence;
- hard-coded GKE recovery behavior represented as learned Q-action evidence;
- legacy GKE target realization that can append structural-backbone targets beyond the requested fanout budget;
- using the earlier GKE S0 `canonical_fanout` provenance field as though it were the final S5 requested fanout;
- historical Q-AHBN experimental results as validation of the future Q-AHBN2 controller.

### 6.4 DEFER

The following remain later design decisions:

- whether additional RL-only variables analogous to historical `rho_hat` or `r_hat` are scientifically justified;
- whether an explicit disturbance/recovery phase is needed;
- exact delivery proxy/estimate used during learning;
- whether/how a recovery-sensitive reward term is used;
- learning rate `alpha`;
- discount factor `gamma`;
- epsilon schedule;
- online-learning versus train/freeze/evaluate lifecycle;
- Q-table persistence/reset policy across experiment runs and pod/process replacement;
- whether a separately identified deterministic safety override is necessary.

The historical GKE **core in-process construction** is no longer unresolved: one `GKEQLearner` is created per Q-AHBN pod/process and its inspected Q-table/transition state is in memory. What remains deferred is the future Q-AHBN2 persistence/reset policy and any external run/pod lifecycle behavior.

No redesigned value is frozen by this document.

### 6.5 Cross-environment invariants carried into Q-AHBN2 design

The following are now mandatory interpretation constraints for the next design stage:

1. The learning layer starts from the canonical AHBN proposal, never from either legacy Q-AHBN rule-based substitute.
2. The canonical logical AHBN variables remain `d,l,u,c`, but raw acquisition, normalization and update-window mechanics may remain environment-specific as established by R1.
3. The final canonical fanout proposal is S5 `k_request ∈ {2,3,4,5,6}`; Q-AHBN2 must not use the GKE S0 2/3/4 provenance value as its base action.
4. Requested fanout and realized forwarding remain separate quantities throughout learning, execution, logging, analysis and manuscript claims.
5. A no-intervention action must reproduce the canonical AHBN proposal exactly at the Q-layer boundary.
6. Deterministic event/safety handling, if later approved, must be separately named, logged and attributed; it cannot masquerade as a learned Q action.
7. A common Q-AHBN2 logical RL contract must be defined before platform-specific implementations; platform-specific sensing may differ, but claimed RL semantics must not.
8. Historical ControlSim/GKE results remain antecedent evidence only and cannot establish parity or validate the future Q-AHBN2 implementation.

### 6.6 Consolidated R3 gate

- original R3 decision register: **PASS**;
- R1-GKE impact on R3: **CLARIFICATION ONLY**;
- R2-GKE impact on R3: **CLARIFICATION / ONE CORE-LIFECYCLE RESOLUTION**;
- disposition reversals: **NONE**;
- redesigned Q-AHBN2 values frozen: **NONE**;
- Q-AHBN2 implementation authorized by this pass: **NO**.

**R3 CONSOLIDATED GATE: PASS.** The R1–R3 evidence base is now complete across canonical ControlSim, canonical Kubernetes, historical ControlSim Q-AHBN, and historical Kubernetes Q-AHBN. The next permitted artifact is `docs/01_CANONICAL_AHBN_CONTRACT.md`, derived only from the canonical R1/R1-GKE boundary.

---

## 7. Prohibited Legacy Inheritance

Until superseded by an explicitly reviewed Q-AHBN2 design contract, the following are prohibited:

1. copying legacy ControlSim or GKE Q-learning code and treating it as the Q-AHBN2 controller;
2. substituting historical GKE `adaptive_update()` for canonical AHBN;
3. changing canonical AHBN equations, EWMA, S5 thresholds, mode rule, or eligible-target realization to accommodate the learner;
4. reusing historical `c_hat` with capacity semantics;
5. introducing tau suppression into canonical AHBN;
6. treating `weight` modified by a learning layer as though it were the untouched canonical `sigmoid(z)`;
7. labelling deterministic failure/recovery overrides as learned Q actions;
8. conflating requested fanout with realized forwarding;
9. claiming ControlSim/GKE parity from the legacy repositories;
10. using legacy Q-AHBN outcomes as proof that the future Q-AHBN2 design is valid or superior.

---

## 8. Q-AHBN2 Boundary Established by R1-R3

The source reconciliation establishes the following boundary:

```text
FROZEN / AUTHORITATIVE
────────────────────────────────────
canonical local observations
canonical EWMA
canonical score
canonical sigmoid/mode rule
canonical S5 requested fanout
canonical mode-specific realization
requested-vs-realized distinction
             │
             ▼
      AHBN base proposal
             │
             ▼
TO BE DESIGNED
────────────────────────────────────
Q-AHBN2 logical RL state
Q-AHBN2 state discretization
Q-AHBN2 action semantics
Q-AHBN2 reward
Q-AHBN2 learning hyperparameters
Q-AHBN2 training/evaluation lifecycle
             │
             ▼
      final Q-AHBN2 action
             │
             ▼
CANONICAL EXECUTION / OBSERVABILITY
────────────────────────────────────
eligible-target realization
outcome measurement
AHBN proposal trace
Q intervention trace
learning trace
```

The governing interpretation is:

> **Q-AHBN2 inherits the architecture and learning family from the legacy work, not the legacy RL specification.**

---

## 9. Change-Control Rule

This register is the source-authority baseline for subsequent Q-AHBN2 work.

A later correction is permitted only when supported by stronger source evidence, a discovered reconstruction error, or an explicitly approved design decision. Any such change must:

1. identify the affected R1/R2/R3 finding;
2. cite the evidence causing the change;
3. state whether canonical AHBN is affected;
4. state whether prior Q-AHBN2 code/tests/results are affected; and
5. be committed as an explicit authority-register revision rather than silently changing interpretation.

No future implementation commit may retroactively redefine what a legacy source meant.

---

## 10. Gate Record

| Gate | Result | Meaning |
|---|---|---|
| Source identification | PASS | Required canonical and historical sources identified and pinned. |
| Canonical AHBN identification | PASS | Normative AHBN implementation boundary identified. |
| Canonical S5 verification | PASS | Requested fanout set and thresholds reconciled. |
| R1 — Canonical AHBN mechanism reconciliation | PASS | ControlSim code, canonical GKE code/runtime, and manuscript mechanism reconciled without requiring AHBN redesign. |\n| R1-GKE delta reconciliation | PASS | GKE controller law and final S5 semantics match the canonical scientific contract; sensing/normalization/window semantics are environment-specific and explicitly bounded. |
| R2 — Legacy Q-AHBN reconstruction | PASS | ControlSim and GKE historical learners reconstructed separately. |
| R2 — Legacy RL parity | NOT ESTABLISHED | Historical ControlSim and GKE are not one parity-preserved RL specification. |\n| R2-GKE delta reconciliation | PASS | Historical GKE Q-AHBN compared directly with canonical GKE AHBN; existing R2/R3 dispositions remain valid with clarified canonical-proposal semantics and core learner lifecycle. |
| R3 — Reconciliation Decision Register | PASS — CONSOLIDATED | R1/R2 ControlSim and GKE findings incorporated; no disposition reversal; one historical GKE core-lifecycle fact resolved; no redesigned values frozen. |
| Q-AHBN2 design | NOT YET FROZEN | No redesigned state/action/reward/hyperparameter values are authorized by this register. |
| Q-AHBN2 implementation | NOT YET AUTHORIZED | Implementation follows later contracts and parity gates. |

---

## 11. Next Controlled Artifact

The next document is:

`docs/01_CANONICAL_AHBN_CONTRACT.md`

It must be derived from the R1 canonical boundary and authoritative sources in Sections 2–4 of this register. It must **not** import legacy Q-AHBN state, action, reward, recovery, or target-realization semantics.

Only after the canonical AHBN contract is independently frozen should Q-AHBN2 learning-layer design be specified.


---

## 12. S02-F Learning-Parameter Historical Reconciliation — 2026-09-21

This amendment records the required comparison of the Q-AHBN2 learning-parameter decision against the historical ControlSim and Kubernetes Q-AHBN sources. It does **not** promote either historical implementation to design authority.

| Parameter | Historical ControlSim Q-AHBN | Historical GKE Q-AHBN | Q-AHBN2 disposition |
|---|---:|---:|---|
| learning rate `alpha_Q` | 0.25 | 0.25 | **RETAIN 0.25** |
| discount factor `gamma` | 0.90 | 0.90 | **RETAIN 0.90** |
| epsilon start | 0.30 | 0.20 | **RECONCILE to 0.30** |
| epsilon minimum | 0.03 | 0.03 | **RETAIN 0.03** |
| multiplicative epsilon decay | 0.995 | 0.995 | **RETAIN 0.995** |
| historical decay trigger | each learner decision/update cycle | each learner decision/update cycle | **RETAIN logical per-decision decay; exact lifecycle placement must remain consistent with H** |

Evidence:
- historical ControlSim: `wwiras/q-ahbn@7bca26213cbfb2099cff8b2f659008b8e040b238`, especially `v1.0/ahbn/q_learning.py` and Exp10/11/12 Q-AHBN configs;
- historical Kubernetes: `wwiras/q-ahbn_gke@a9af5ccb9b564d5f2c2daaeeb9a04b191780cdbe`, especially `app/q_learning_gke.py` and Exp10/11/12 Q-AHBN configs.

Reconciliation rationale:
1. `alpha_Q=0.25`, `gamma=0.90`, `epsilon_min=0.03`, and `epsilon_decay=0.995` are common historical values across both environments and no canonical-AHBN incompatibility was found.
2. The only cross-platform numerical disagreement is epsilon start (0.30 versus 0.20). Q-AHBN2 uses **0.30** as the single logical contract because the ControlSim learning-validation stage is the primary learning environment and the higher of the two already-used historical values provides bounded initial exploration without inventing a new tuned value.
3. RO2 establishes that the target dissemination problem changes materially across failure/overload, churn, heterogeneity, and fanout-related trade-offs. That evidence supports retaining non-zero exploration and temporal learning; it does **not** identify a uniquely optimal RL hyperparameter. Therefore the minimum-adaptation rule is used rather than parameter tuning.
4. These are Q-learning-layer parameters only. They do not alter canonical AHBN EWMA `alpha=0.30`; implementation MUST use distinct naming to prevent ambiguity.

L1 arithmetic check for the retained epsilon schedule:

```text
epsilon_n = max(0.03, 0.30 * 0.995^n)
floor is reached after approximately 460 decay steps.
```

This is a bounded sanity check, not an optimization claim. The exact episode/reset/persistence semantics remain governed by S02-H.

**Authority impact:** no R1/R2/R3 disposition reversal. Historical implementations remain Level-3 evidence; Q-AHBN2 parameter values become authoritative only through the frozen DOC-02 design contract.
