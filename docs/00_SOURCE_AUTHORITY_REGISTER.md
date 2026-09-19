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
| 2 | `wwiras/ahbn2_gke` | `936a79480bc1252c79b6ee01f65c88c740af2844` [ahbn2_gke](https://github.com/wwiras/ahbn2_gke) | Normative canonical AHBN implementation boundary. Represents later canonical S5/parity corrections for GKE |
| 3 | Revised AHBN Scientific Reports manuscript, 17 Sep 2026 | [AHBN17Sept2026_manuscriptSRpt.pdf](https://drive.google.com/file/d/1YarltXx8bZf0QWlIJeaKIIX6KCsCMPYJ/view?usp=drive_link)` | Normative scientific description and interpretation of the frozen AHBN mechanism and its limitations. |
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

R1 reconciled the frozen implementation with the 17-Sep-2026 revised AHBN manuscript.

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
- Missing observations retain their previous EWMA state; absence of a new observation is not equivalent to a zero observation.
- The controller latency observation is local one-hop latency and must not be conflated with experiment-level propagation delay.
- Controller utilization pressure must not be conflated with experiment-level total forwards.
- Trace `fanout` is the controller-requested fanout unless explicitly recorded otherwise.
- Canonical AHBN does not use tau-based suppression.

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

---

## 6. R3 — Reconciliation Decision Register

**Gate result: PASS.**

R3 converts R2 findings into controlled inheritance dispositions without selecting redesigned values.

### 6.1 RETAIN

The following concepts may cross into the Q-AHBN2 design stage:

- Q-AHBN as a meta-controller layered after canonical AHBN;
- R1 canonical AHBN as the source of the unmodified base proposal;
- tabular Q-learning as the baseline learning family;
- epsilon-greedy exploration as an admissible mechanism;
- decentralized/local operation;
- a no-intervention / AHBN-base action capability;
- reward objective balancing dissemination effectiveness with overhead rather than minimizing forwarding alone;
- one-step previous-state/action Q-learning lifecycle;
- requested-versus-realized fanout distinction;
- logging the base AHBN proposal;
- logging the final post-Q decision;
- explicit learner-intervention indicators;
- Q-state/action/reward/update observability;
- environment-specific sensing where the common logical contract remains explicit.

### 6.2 REDESIGN

The following functions remain scientifically relevant but no legacy implementation is authoritative:

- RL state representation;
- state discretization;
- action-space semantics;
- fanout intervention semantics;
- mode intervention semantics;
- any possible Q-layer weight intervention;
- reward equation and coefficients;
- common ControlSim/Kubernetes RL contract.

**REDESIGN does not mean “copy the legacy mechanism and change its numbers.”** It means the function/problem is retained while its new definition requires independent justification.

### 6.3 REJECT

The following must not be inherited as Q-AHBN2 design authority:

- the legacy seven-variable ControlSim state copied verbatim;
- historical `c_hat = capacity` semantics;
- the old latency-derived failure-phase formula;
- tau as a Q-AHBN2 actuator inherited from legacy ControlSim;
- legacy numerical action magnitudes as authoritative values;
- legacy GKE `adaptive_update()` as canonical AHBN;
- hard-coded GKE recovery behavior represented as learned Q-action evidence;
- legacy GKE target-realization behavior as canonical Q-AHBN2 realization;
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
- Q-table persistence/reset policy;
- whether a separately identified deterministic safety override is necessary.

No value for these items is frozen by this document.

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
| R1 — Canonical AHBN mechanism reconciliation | PASS | Code/manuscript mechanism reconciled without requiring controller modification. |
| R2 — Legacy Q-AHBN reconstruction | PASS | ControlSim and GKE historical learners reconstructed separately. |
| R2 — Legacy RL parity | NOT ESTABLISHED | Historical ControlSim and GKE are not one parity-preserved RL specification. |
| R3 — Reconciliation Decision Register | PASS | Legacy inheritance classified as RETAIN / REDESIGN / REJECT / DEFER. |
| Q-AHBN2 design | NOT YET FROZEN | No redesigned state/action/reward/hyperparameter values are authorized by this register. |
| Q-AHBN2 implementation | NOT YET AUTHORIZED | Implementation follows later contracts and parity gates. |

---

## 11. Next Controlled Artifact

The next document is:

`docs/01_CANONICAL_AHBN_CONTRACT.md`

It must be derived from the R1 canonical boundary and authoritative sources in Sections 2–4 of this register. It must **not** import legacy Q-AHBN state, action, reward, recovery, or target-realization semantics.

Only after the canonical AHBN contract is independently frozen should Q-AHBN2 learning-layer design be specified.
