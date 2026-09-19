# Q-AHBN2 Design Freeze

**Document ID:** QAHBN2-DOC-02  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/02_QAHBN2_DESIGN_FREEZE.md`  
**Status:** PARTIAL DESIGN FREEZE — Sections 02.1–02.4 FROZEN  
**Freeze date for Sections 02.1–02.4:** 2026-09-19  
**Scope:** Q-AHBN2 learning-layer design only. The canonical AHBN boundary in `docs/01_CANONICAL_AHBN_CONTRACT.md` is immutable.

---

## 02.1 Design Principles — FROZEN

### 02.1.1 Governing objective

Q-AHBN2 is a learning enhancement over the frozen canonical AHBN, not a replacement controller and not an opportunity to retune AHBN.

The design objective is:

> Preserve the canonical AHBN decision path unchanged, then allow a separately identifiable Q-learning layer to refine the canonical proposal within an explicitly defined Q-AHBN2 action boundary.

The governing rule is **minimum scientifically justified adaptation**. Historical Q-AHBN mechanisms are retained only where they remain compatible with the canonical AHBN contract and the Q-AHBN2 research objective. Historical mechanisms that redefine, bypass, or constrain the canonical controller incorrectly are removed or redesigned.

### 02.1.2 Canonical-first principle

Every Q-AHBN2 decision MUST begin by executing canonical AHBN exactly as frozen in `docs/01_CANONICAL_AHBN_CONTRACT.md`.

For each decision opportunity, canonical AHBN first produces:

```text
AHBN observations
    d,l,u,c
        ↓
canonical EWMA
    d_hat,l_hat,u_hat,c_hat
        ↓
z = -d_hat + l_hat + u_hat + c_hat
        ↓
w = sigmoid(z)
        ↓
AHBN mode ∈ {Gossip, Structured}
        ↓
AHBN k_request ∈ {2,3,4,5,6}
```

The resulting mode and requested fanout form the **AHBN base proposal**. They MUST be preserved in trace data before any Q-learning intervention.

Q-AHBN2 MUST NOT alter:

- the four canonical AHBN observation meanings;
- environment-specific canonical observation adapters;
- EWMA formulation or `α=0.30`;
- score coefficients or zero centres;
- sigmoid definition or scale;
- mode threshold or two-mode semantics;
- final S5 thresholds;
- canonical AHBN requested-fanout set `{2,3,4,5,6}`;
- canonical mode-specific eligible-target semantics.

Thus, the canonical AHBN proposal remains reproducible independently of Q-AHBN2.

### 02.1.3 Meta-controller principle

Q-AHBN2 retains the scientifically valid architectural idea from historical Q-AHBN: Q-learning operates as a **meta-controller after AHBN**, rather than replacing AHBN.

The historical ControlSim implementation explicitly called the base AHBN decision first and then selected/applied a Q meta-action. The historical GKE implementation similarly preserved `ahbn_mode` and `ahbn_fanout` before applying the learner.

This architectural ordering is retained.

However, historical state definitions, action effects, reward terms, Q-learning hyperparameters, failure heuristics, tau manipulation, and fanout bounds are NOT inherited by this architectural freeze. They are subject to later sections of this document.

### 02.1.4 Mandatory removal of the historical Q-layer fanout cap

Historical Q-AHBN implementations clipped the learner-modified fanout to a configured `max_fanout`, commonly 6:

```text
historical final fanout
    = max(min_fanout,
          min(max_fanout,
              ahbn_fanout + q_delta))
```

That Q-layer upper cap is **REMOVED in Q-AHBN2**.

This does **not** modify canonical AHBN. Canonical AHBN remains required to produce:

```text
k_AHBN ∈ {2,3,4,5,6}
```

The distinction is:

```text
canonical AHBN proposal:
    k_AHBN ∈ {2,3,4,5,6}
             │
             ▼
Q-AHBN2 intervention:
    may later modify k_AHBN according to the frozen Q-AHBN2 action contract
             │
             ▼
Q-AHBN2 requested fanout:
    k_Q
             │
             ▼
canonical execution constraint:
    k_real <= min(k_Q, |N_e|)
```

Therefore, **6 remains the maximum canonical AHBN proposal, but it is not an upper cap on a later Q-AHBN2 request**.

No arbitrary replacement Q-layer maximum is introduced in Sections 02.1–02.2. Any action semantics affecting `k_Q` must be defined and justified in the later action-space section. Physical/topological realization remains naturally bounded by the eligible set `N_e`.

This separation is mandatory because clipping a learned positive intervention back to the canonical AHBN maximum would make some Q actions ineffective whenever AHBN already proposes `k_AHBN=6`, while incorrectly presenting the clipping rule as part of canonical AHBN.

### 02.1.5 Proposal-versus-intervention principle

The following quantities are scientifically distinct and MUST never be conflated:

- `mode_AHBN`: untouched canonical AHBN proposed mode;
- `k_AHBN`: untouched canonical AHBN S5 requested fanout;
- `a_Q`: selected Q-AHBN2 action;
- `mode_Q`: final Q-AHBN2 requested mode;
- `k_Q`: final Q-AHBN2 requested fanout after the learning intervention;
- `k_real`: realized number of forwarding targets after eligibility/topology constraints.

A Q-AHBN2 intervention does not retroactively change what AHBN proposed.

### 02.1.6 No hidden deterministic learner substitutions

Historical GKE Q-AHBN contained rule-based adaptive/failure logic and could label a deterministic failure reaction with a Q-action name. That behavior is not retained as part of the Q-AHBN2 architecture.

A Q-AHBN2 action must result from the frozen Q-learning decision process unless a later explicitly approved safety boundary overrides it. Any safety override must be:

1. outside canonical AHBN;
2. outside the learned-action attribution;
3. explicitly named;
4. independently logged; and
5. excluded from claims that the learner selected that behavior.

### 02.1.7 No tau actuator

Historical ControlSim Q-AHBN meta-actions modified `tau`. Canonical AHBN has no tau-based suppression actuator. Therefore tau manipulation is architecturally incompatible and is removed from Q-AHBN2.

### 02.1.8 Local-learning principle

Q-AHBN2 remains a lightweight decentralized learning layer. It must not require a centralized coordinator to choose dissemination actions at runtime.

The exact logical RL state is deliberately **not frozen here**. Section 02.3 must determine which locally available canonical quantities and permitted local outcome signals form the Q-AHBN2 state.

### 02.1.9 Environment-separation principle

ControlSim and Kubernetes may differ in raw sensing and execution mechanics, as canonical AHBN already permits. Q-AHBN2 must nevertheless expose the same logical learning-layer contract wherever cross-platform parity is claimed.

Environment-specific shortcuts must not silently become different RL algorithms.

### 02.1.10 Evidence-first principle

Q-AHBN2 is not designed to guarantee improvement over AHBN. Its purpose is to test whether learning can improve adaptation over the frozen AHBN under the evaluated conditions.

Poor, neutral, condition-dependent, or beneficial results are all scientifically admissible. AHBN must not be reopened and Q-AHBN2 must not be post-hoc redesigned merely because an outcome is unattractive.

---

## 02.2 Learning-Layer Architecture — FROZEN

### 02.2.1 Frozen architecture

The Q-AHBN2 decision path is:

```text
LOCAL ENVIRONMENT
      │
      ▼
canonical observation adapter
      │
      ▼
┌──────────────────────────────────────┐
│       FROZEN CANONICAL AHBN          │
│ d,l,u,c                              │
│   ↓                                  │
│ d_hat,l_hat,u_hat,c_hat              │
│   ↓                                  │
│ z → w                                │
│   ↓                                  │
│ mode_AHBN + k_AHBN                   │
└──────────────────────────────────────┘
      │
      │ untouched AHBN base proposal
      ▼
┌──────────────────────────────────────┐
│       Q-AHBN2 LEARNING LAYER         │
│                                      │
│ construct frozen RL state s_t        │
│   ↓                                  │
│ choose learned action a_t            │
│   ↓                                  │
│ refine AHBN proposal                 │
│   ↓                                  │
│ mode_Q + k_Q                         │
└──────────────────────────────────────┘
      │
      ▼
canonical mode-specific
eligible-target realization
      │
      ▼
k_real <= min(k_Q, |N_e|)
      │
      ▼
forwarding / local outcomes
      │
      ├──────────────► observability
      │
      ▼
reward / Q update
at the lifecycle point later frozen
```

Sections 02.1–02.2 freeze this ordering only. They do not yet freeze the state, action set, reward, learning coefficients, exploration schedule, or update cadence.

### 02.2.2 AHBN/Q-AHBN2 ownership boundary

| Component | Owner | Status |
|---|---|---|
| raw observation acquisition | canonical environment adapter | inherited |
| logical `d,l,u,c` | canonical AHBN | immutable |
| EWMA `d_hat,l_hat,u_hat,c_hat` | canonical AHBN | immutable |
| `z`, `w` | canonical AHBN | immutable |
| `mode_AHBN` | canonical AHBN | immutable proposal |
| `k_AHBN ∈ {2,3,4,5,6}` | canonical AHBN | immutable proposal |
| RL state `s_t` | Q-AHBN2 | to freeze in 02.3 |
| discretization | Q-AHBN2 | to freeze after state |
| learned action `a_t` | Q-AHBN2 | to freeze later |
| `mode_Q` | Q-AHBN2 | permitted intervention output; semantics not yet frozen |
| `k_Q` | Q-AHBN2 | permitted intervention output; no historical upper fanout cap |
| eligible-target construction/realization | canonical execution boundary | inherited |
| `k_real` | execution outcome | bounded by eligible set |
| reward | Q-AHBN2 | to freeze later |
| Q update/lifecycle | Q-AHBN2 | to freeze later |

### 02.2.3 Intervention point

The only permitted learning intervention point is **after canonical AHBN has produced its complete base proposal and before eligible-target realization**.

Q-AHBN2 MUST NOT intervene inside:

- observation normalization;
- EWMA updates;
- score calculation;
- sigmoid calculation;
- AHBN mode selection;
- S5 fanout calculation.

This ensures that AHBN can always be run, traced, tested, and compared independently.

### 02.2.4 Fanout semantics after cap removal

Three fanout quantities are mandatory:

```text
k_AHBN  = canonical AHBN requested fanout
k_Q     = Q-AHBN2 requested fanout after intervention
k_real  = realized target count
```

Required invariants:

```text
k_AHBN ∈ {2,3,4,5,6}

k_Q is NOT upper-clipped to 6 merely because
6 is the maximum canonical AHBN S5 proposal.

0 <= k_real <= min(k_Q, |N_e|)
```

The later action-space freeze must define how actions transform `k_AHBN` into `k_Q`, including legal lower-bound behavior. Sections 02.1–02.2 intentionally do not pre-empt that decision.

### 02.2.5 Mode semantics

Canonical AHBN always produces one of:

```text
{Gossip, Structured}
```

Q-AHBN2 may be designed to retain or alter that proposal only through the later frozen action contract. No third dissemination mode is introduced.

Regardless of the final requested mode, target realization must use the corresponding canonical mode-specific eligibility semantics.

### 02.2.6 Required observability boundary

Even before the detailed observability section is frozen, the architecture requires sufficient trace separation to reconstruct:

```text
canonical inputs/state
→ z,w
→ mode_AHBN,k_AHBN
→ RL state
→ Q action
→ mode_Q,k_Q
→ eligible set / realization
→ k_real
→ outcome
→ reward/update
```

At minimum, future implementation must never expose only a generic `mode` or `fanout` field where doing so would make the AHBN proposal indistinguishable from the Q-AHBN2 intervention.

### 02.2.7 Historical architecture reconciliation

| Historical element | Q-AHBN2 disposition | Reason |
|---|---|---|
| AHBN decides before Q layer | **RETAIN** | correct meta-controller architecture |
| preserve AHBN proposal before Q intervention | **RETAIN / STRENGTHEN** | required for attribution and comparison |
| Q layer may refine mode/fanout | **RETAIN AS ARCHITECTURAL CAPABILITY** | exact actions deferred to action-space freeze |
| Q-layer `max_fanout=6` clipping | **REMOVE — MANDATORY** | canonical S5 maximum is an AHBN proposal bound, not a learner-output cap |
| canonical AHBN S5 `k∈{2..6}` | **RETAIN IMMUTABLY** | canonical contract |
| tau modification | **REMOVE** | not part of canonical AHBN |
| historical rule-based GKE `adaptive_update()` as AHBN | **REMOVE / REPLACE WITH CANONICAL AHBN** | conflicts with canonical contract |
| historical `fail_pressure` direct controller | **DO NOT INHERIT** | failure/churn must enter through approved canonical observations / later RL design |
| deterministic failure reaction labelled `recovery_push` | **REMOVE** | cannot attribute deterministic override to Q learning |
| append structural targets beyond requested budget | **REMOVE** | violates canonical requested-budget realization contract |
| ControlSim/GKE historical RL differences | **DO NOT PRESERVE AS PARITY** | Q-AHBN2 requires one logical learning-layer contract |

### 02.2.8 Architectural invariants

The following are now frozen:

**A1 — Canonical-first:** canonical AHBN executes completely before Q-AHBN2.

**A2 — Immutable proposal:** `mode_AHBN` and `k_AHBN` are recorded unchanged.

**A3 — Post-AHBN learning:** Q-AHBN2 acts only after the AHBN proposal.

**A4 — Canonical S5 preserved:** AHBN itself remains restricted to `k_AHBN∈{2,3,4,5,6}`.

**A5 — Historical Q fanout cap removed:** Q-AHBN2 `k_Q` is not upper-clipped to AHBN's maximum of 6.

**A6 — Realization remains bounded:** actual forwarding remains constrained by eligible peers, `k_real <= min(k_Q, |N_e|)`.

**A7 — No tau:** Q-AHBN2 does not introduce tau as an AHBN/Q actuator.

**A8 — No hidden learned actions:** deterministic safety/event handling cannot be reported as Q-selected behavior.

**A9 — Two modes only:** final dissemination uses Gossip or Structured semantics; no third mode.

**A10 — Attribution:** AHBN proposal, Q intervention, and realized execution remain separately observable.

### 02.2.9 Boundary freeze decision

The architectural boundary is accepted as:

```text
IMMUTABLE CANONICAL AHBN
        ↓
(mode_AHBN, k_AHBN ∈ {2..6})
        ↓
Q-AHBN2 META-CONTROLLER
        ↓
(mode_Q, k_Q)
        ↓
NO HISTORICAL Q-LAYER UPPER FANOUT CAP
        ↓
CANONICAL MODE-SPECIFIC ELIGIBLE-TARGET REALIZATION
        ↓
k_real <= min(k_Q, |N_e|)
```

**02.1 DESIGN PRINCIPLES GATE: PASS / FROZEN.**

**02.2 LEARNING-LAYER ARCHITECTURE GATE: PASS / FROZEN.**

This freeze does not authorize implementation yet and does not freeze the RL state, discretization, action semantics, reward, Q-learning parameters, lifecycle, safety policy, or complete observability schema.

---

## 02.3 State Representation — FROZEN

### 02.3.1 State-design objective

The Q-AHBN2 state MUST be the **minimum sufficient logical representation of the local dissemination condition already exposed by canonical AHBN**. It must not expand merely because historical Q-AHBN implementations contained additional variables.

The state-design rule is:

> Reuse the frozen canonical AHBN adaptive observations unless an additional state variable contributes decision-relevant information that is neither already represented nor deterministically derivable from those observations.

This rule minimizes state-space growth, removes historical environment-specific heuristics, preserves decentralization, and makes one logical RL state portable across ControlSim and Kubernetes.

### 02.3.2 Historical state reconciliation

Historical Q-AHBN did not have one stable cross-platform state contract.

The historical ControlSim learner used seven discrete components derived from:

```text
d_hat
l_hat
u_hat
rho_hat
r_hat
c_hat
failure_phase(l_hat)
```

The historical GKE learner instead used four components derived from:

```text
duplicate_ratio
fail_pressure
overload_pressure + bottleneck_pressure
disturbance phase
```

These states are not semantically equivalent. They mix different generations of controller variables, environment-specific heuristics, and derived phase labels.

Q-AHBN2 therefore does **not** inherit either historical state tuple.

### 02.3.3 Frozen logical state

The Q-AHBN2 logical state is frozen as the four canonical AHBN EWMA observations:

```text
s_t = (
    d_hat_t,
    l_hat_t,
    u_hat_t,
    c_hat_t
)
```

where:

- `d_hat_t` = canonical EWMA duplicate pressure;
- `l_hat_t` = canonical EWMA latency pressure;
- `u_hat_t` = canonical EWMA processing/utilization pressure;
- `c_hat_t` = canonical EWMA churn/dynamic-membership pressure.

These are the **continuous logical state variables**. Section 02.4 will define how they are discretized for tabular Q-learning.

No discretization thresholds are frozen in Section 02.3.

### 02.3.4 Why the canonical four are sufficient

Canonical AHBN already establishes these four quantities as the local information required to characterize the dissemination trade-off that drives adaptation:

```text
duplicate pressure     → efficiency/redundancy condition
latency pressure       → propagation-performance condition
utilization pressure   → processing/resource condition
churn pressure         → topology/dynamic-membership condition
```

The Q-AHBN2 learner is a refinement layer over that same adaptive problem. Giving it the same canonical condition vector provides a consistent information boundary while allowing Q-learning to learn different long-term action values for different combinations of those conditions.

This is intentionally more conservative than introducing new sensors or historical recovery heuristics.

### 02.3.5 Variables explicitly excluded from the RL state

The following are **not** independent Q-AHBN2 state dimensions.

#### A. `z`

Excluded because:

```text
z = -d_hat + l_hat + u_hat + c_hat
```

It is deterministically derivable from the four frozen state variables. Including it would add no new information.

#### B. `w`

Excluded because:

```text
w = sigmoid(z)
```

It is deterministically derivable from `z`, which is itself derivable from the four state variables.

#### C. `mode_AHBN`

Excluded from the RL state because canonical mode is deterministically derived from `w`. It remains a mandatory **base-proposal input to action application** and a mandatory observability field, but it is not an additional Q-table state dimension.

This distinction is important:

```text
used by action application ≠ independent RL state dimension
```

#### D. `k_AHBN`

Excluded from the RL state because S5 deterministically derives it from canonical `z`. It remains the immutable fanout proposal that the selected Q action may later refine.

Removing the historical Q-layer fanout cap does not justify adding `k_AHBN` as another state dimension; the learner already receives the underlying canonical condition vector from which S5 produced it.

#### E. failure/recovery phase labels

Historical ControlSim derived `failure_phase` from latency thresholds, while historical GKE derived a disturbance phase from fail/overload/bottleneck pressures.

These are excluded because they are derived labels rather than independent observations and because the GKE form depends on historical noncanonical heuristics.

#### F. `fail_pressure`, `overload_pressure`, and `bottleneck_pressure`

Excluded as independent state variables.

Q-AHBN2 must not reintroduce the historical GKE direct-control path through the RL state. Effects of failure, overload, and bottleneck conditions must reach the learner through the approved canonical observation semantics where applicable, particularly latency, utilization, and churn/dynamic-membership pressure.

#### G. historical `rho_hat`, `r_hat`, and old `c_hat` semantics

These are not inherited merely because they existed in old ControlSim Q-AHBN.

Q-AHBN2 uses the notation and meanings frozen by the canonical AHBN contract. In Q-AHBN2, `c_hat` means canonical **churn/dynamic-membership pressure**. Historical variables with different meanings must not be silently mapped onto it.

#### H. counters and outcome variables

Raw `recv_count`, `duplicate_count`, `forward_count`, delivery estimates, reward history, previous reward, Q-values, epsilon, action counts, and experiment labels are excluded from the environmental state.

Some may later be used for reward calculation, learning lifecycle, or observability, but that does not make them state dimensions.

### 02.3.6 Proposal context versus environmental state

Q-AHBN2 has two distinct inputs at a decision opportunity:

```text
Environmental RL state:
    s_t = (d_hat,l_hat,u_hat,c_hat)

Canonical base proposal:
    p_t = (mode_AHBN,k_AHBN)
```

The Q policy selects an action using the frozen RL state:

```text
a_t = policy(s_t)
```

The selected action is then applied **relative to the preserved canonical proposal**:

```text
(mode_Q,k_Q)
    = Apply(
        mode_AHBN,
        k_AHBN,
        a_t
      )
```

The exact `Apply` semantics are intentionally deferred to the action-space freeze.

This separation avoids duplicating deterministic AHBN outputs inside the Q-table key while preserving the meta-controller architecture frozen in Section 02.2.

### 02.3.7 Cross-platform state contract

ControlSim and Kubernetes MUST expose the same logical Q-AHBN2 state:

```text
(d_hat,l_hat,u_hat,c_hat)
```

The raw measurements used to produce these quantities may differ only as permitted by the canonical AHBN environment adapters.

Q-AHBN2 MUST NOT define a ControlSim-only state dimension or a Kubernetes-only state dimension if cross-platform parity is claimed.

Thus:

```text
environment-specific raw sensing
            ↓
canonical adapter
            ↓
canonical EWMA state
(d_hat,l_hat,u_hat,c_hat)
            ↓
same logical Q-AHBN2 state
```

### 02.3.8 Temporal semantics

The state at decision time `t` is the current canonical AHBN EWMA snapshot **after the canonical observation update used for that AHBN decision and before Q-AHBN2 action selection**.

Required ordering:

```text
raw local observations at t
        ↓
canonical normalization
        ↓
canonical EWMA update
        ↓
canonical AHBN proposal
        ↓
capture s_t=(d_hat,l_hat,u_hat,c_hat)
        ↓
Q-AHBN2 action selection
```

Q-AHBN2 must not maintain a second, differently smoothed copy of these four observations for its state unless a later controlled artifact explicitly reopens the design. The canonical EWMA already supplies temporal smoothing.

### 02.3.9 State invariants

The following are now frozen:

**S1 — Four-dimensional logical state:** `s_t=(d_hat,l_hat,u_hat,c_hat)`.

**S2 — Canonical meanings only:** each dimension uses the exact canonical AHBN semantics.

**S3 — Canonical EWMA only:** Q-AHBN2 does not introduce a second smoothing layer for these state variables.

**S4 — No redundant AHBN derivatives:** `z`, `w`, `mode_AHBN`, and `k_AHBN` are not additional Q-table state dimensions.

**S5 — Proposal preserved separately:** `mode_AHBN` and `k_AHBN` remain available to the action-application layer and observability.

**S6 — No historical disturbance phase:** failure/recovery phase labels are not independent state dimensions.

**S7 — No historical direct-pressure state:** `fail_pressure`, `overload_pressure`, and `bottleneck_pressure` are not Q-AHBN2 state dimensions.

**S8 — No outcome leakage:** reward/outcome counters and learning internals are not environmental state dimensions.

**S9 — Cross-platform parity:** ControlSim and Kubernetes use the same logical four-dimensional state wherever parity is claimed.

**S10 — Discretization deferred:** Section 02.3 freezes variables and semantics only; binning belongs to Section 02.4.

### 02.3.10 State-space rationale

This four-variable state is deliberately minimal.

It is smaller and more defensible than the historical seven-component ControlSim state, while being semantically richer and more canonical than the historical four-component GKE disturbance state.

Most importantly, it does not give Q-AHBN2 privileged information unavailable to canonical AHBN merely to improve results. The scientific question remains clean:

> Given the same canonical local condition vector used by AHBN, can a Q-learning meta-controller learn useful refinements to AHBN's deterministic proposal?

That question directly preserves the relationship:

```text
AHBN = frozen deterministic adaptive baseline
Q-AHBN2 = learned refinement over the same canonical condition space
```

### 02.3.11 State representation freeze decision

The Q-AHBN2 state representation is accepted as:

```text
s_t = (
    d_hat_t,
    l_hat_t,
    u_hat_t,
    c_hat_t
)
```

with `mode_AHBN` and `k_AHBN` retained separately as the immutable canonical proposal on which the selected learned action operates.

**02.3 STATE REPRESENTATION GATE: PASS / FROZEN.**

This freeze does not define the discrete Q-table key. The next controlled decision is the discretization of these four canonical state variables.

---

## 02.4 State Discretization — FROZEN

### 02.4.1 Objective

Section 02.3 froze the continuous logical Q-AHBN2 state as:

```text
s_t = (d_hat,l_hat,u_hat,c_hat), each in [0,1]
```

Section 02.4 freezes only the mapping from that continuous state to the finite key used by tabular Q-learning.

The governing rule remains **minimum scientifically justified adaptation**. Discretization must be simple, platform-independent, reproducible, and fixed before learning experiments. It must not be tuned retrospectively to improve Q-AHBN2 results.

### 02.4.2 Historical discretization is not inherited

Historical ControlSim used heterogeneous three-bin thresholds tied to obsolete controller parameters and variable-specific heuristics. Historical GKE used different three-bin thresholds over a different state definition plus a derived disturbance phase.

Those historical thresholds are not portable to the canonical Q-AHBN2 state because all four Q-AHBN2 dimensions are now canonical normalized pressures in [0,1].

Therefore Q-AHBN2 does not inherit either historical binning scheme.

### 02.4.3 Frozen discretization

Each canonical EWMA dimension is discretized independently into three equal-width ordinal bins:

```text
L (Low)    : 0 <= x < 1/3
M (Medium) : 1/3 <= x < 2/3
H (High)   : 2/3 <= x <= 1
```

Equivalently, for any canonical state component x:

```text
B(x) =
    L, if 0 <= x < 1/3
    M, if 1/3 <= x < 2/3
    H, if 2/3 <= x <= 1
```

The discrete Q-AHBN2 state is:

```text
S_t = (
    B(d_hat_t),
    B(l_hat_t),
    B(u_hat_t),
    B(c_hat_t)
)
```

Boundary ownership is explicit: exactly 1/3 belongs to M and exactly 2/3 belongs to H.

### 02.4.4 Example

For:

```text
(d_hat,l_hat,u_hat,c_hat)
= (0.72,0.18,0.43,0.09)
```

the mapping is:

```text
0.72 -> H
0.18 -> L
0.43 -> M
0.09 -> L
```

therefore:

```text
S_t = (H,L,M,L)
```

### 02.4.5 State-space size

There are four state dimensions and three possible bins per dimension.

Therefore the maximum logical tabular state space is:

```text
|S| = 3^4 = 81 states
```

This is the Cartesian state-space ceiling. It does not imply that every one of the 81 combinations must be observed in every experiment.

The eventual Q-table size will be:

```text
|Q| = |S| x |A| = 81 x |A|
```

where |A| will be determined only after the action-space contract is frozen.

### 02.4.6 Why three bins

Two bins would yield only:

```text
2^4 = 16 states
```

but would collapse each canonical pressure into only low/high and remove a distinct intermediate operating region.

Four bins would yield:

```text
4^4 = 256 states
```

before actions are even introduced, increasing tabular sparsity and learning burden without current evidence that the additional resolution is scientifically necessary.

Three bins retain an interpretable low/medium/high distinction while keeping the state space at 81 states. This is the minimum resolution adopted for Q-AHBN2's lightweight tabular-learning objective.

### 02.4.7 Why equal-width thresholds

The thresholds 1/3 and 2/3 are chosen because the four canonical state variables share a normalized [0,1] logical domain.

Equal-width bins provide:

1. one common discretization rule for all four canonical dimensions;
2. no dependence on obsolete ControlSim baseline parameters;
3. no dependence on historical GKE disturbance heuristics;
4. no environment-specific thresholds;
5. no thresholds fitted to Q-AHBN2 outcome data;
6. simple reproducibility and parity testing.

These thresholds are a representation choice, not a claim that 1/3 or 2/3 is a physical phase transition in network behavior.

### 02.4.8 Relationship to canonical AHBN thresholds

Q-AHBN2 discretization thresholds MUST NOT be confused with canonical AHBN's controller thresholds.

Canonical AHBN still computes its proposal from the continuous EWMA values:

```text
z = -d_hat + l_hat + u_hat + c_hat
w = sigmoid(z)
mode_AHBN from z/w
k_AHBN from canonical S5 z thresholds
```

The Q-AHBN2 bins are used only to form the tabular Q-learning key.

Therefore:

```text
continuous canonical state
        |
        +--> canonical AHBN calculations (unchanged)
        |
        +--> Q-AHBN2 discretizer --> (L/M/H)^4 Q-table key
```

Q-AHBN2 binning never quantizes the values used internally by canonical AHBN.

### 02.4.9 No derived phase bin

No extra failure, recovery, disturbance, normal, or other phase label is appended after discretization.

A discrete state is exactly four components:

```text
(d_bin,l_bin,u_bin,c_bin)
```

not:

```text
(d_bin,l_bin,u_bin,c_bin,phase)
```

This preserves the Section 02.3 minimum-state decision.

### 02.4.10 Discretization invariants

**D1 — Three bins per dimension:** L, M, H.

**D2 — Common thresholds:** 1/3 and 2/3 for every canonical state dimension.

**D3 — Fixed boundary rule:** [0,1/3), [1/3,2/3), [2/3,1].

**D4 — Four-component key only:** no derived phase component.

**D5 — Maximum logical state space:** 81 states.

**D6 — Canonical AHBN remains continuous:** discretization affects only the Q-table key.

**D7 — Cross-platform identity:** ControlSim and Kubernetes use the same binning contract wherever Q-AHBN2 parity is claimed.

**D8 — No post-hoc threshold tuning:** formal outcomes cannot be used to move bin boundaries merely to improve performance.

**D9 — Reachability is empirical:** unvisited combinations do not invalidate the 81-state logical definition.

**D10 — Action count deferred:** total Q-table cells are 81 x |A| and remain unresolved until action-space freeze.

### 02.4.11 State discretization freeze decision

The Q-AHBN2 discrete state is accepted as:

```text
S_t = (
    B(d_hat_t),
    B(l_hat_t),
    B(u_hat_t),
    B(c_hat_t)
)

B(x):
    L : 0 <= x < 1/3
    M : 1/3 <= x < 2/3
    H : 2/3 <= x <= 1
```

with a maximum logical state space of:

```text
3^4 = 81 states
```

**02.4 STATE DISCRETIZATION GATE: PASS / FROZEN.**

This freeze does not define Q-AHBN2 actions, reward, learning coefficients, exploration, update lifecycle, or training/evaluation protocol.

---

## 02.5 Next Controlled Decision — Action Space

The next permitted design task is to reconcile the historical Q-AHBN action sets against the frozen post-AHBN intervention boundary and define the minimum scientifically justified Q-AHBN2 action space.

That decision must preserve canonical AHBN's untouched proposal, retain the mandatory removal of the historical Q-layer upper fanout cap, avoid tau, and prevent deterministic recovery heuristics from being represented as learned actions.
