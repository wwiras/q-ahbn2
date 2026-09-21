# Q-AHBN2 Design Freeze

**Document ID:** QAHBN2-DOC-02  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/02_QAHBN2_DESIGN_FREEZE.md`  
**Status:** PARTIAL DESIGN FREEZE — Sections 02.1–02.4 FROZEN  
**Freeze date for Sections 02.1–02.4:** 2026-09-19  
**Scope:** Q-AHBN2 learning-layer design only. The canonical AHBN boundary in `docs/01_CANONICAL_AHBN_CONTRACT.md` is immutable.  
**Math notation policy:** Mathematical variables, sets, inequalities, mappings, and equations use GitHub Markdown LaTeX (`$...# Q-AHBN2 Design Freeze

**Document ID:** QAHBN2-DOC-02  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/02_QAHBN2_DESIGN_FREEZE.md`  
**Status:** PARTIAL DESIGN FREEZE — Sections 02.1–02.4 FROZEN  
**Freeze date for Sections 02.1–02.4:** 2026-09-19  
 inline and `$...$` for display mathematics). Code identifiers, file paths, literal implementation snippets, status blocks, and ASCII architecture diagrams remain fenced/code-formatted where mathematical rendering would reduce precision or readability.

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
- EWMA formulation or $\\alpha=0.30$;
- score coefficients or zero centres;
- sigmoid definition or scale;
- mode threshold or two-mode semantics;
- final S5 thresholds;
- canonical AHBN requested-fanout set $\\{2,3,4,5,6\\}$;
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

$$
k_{\mathrm{AHBN}} \in \{2,3,4,5,6\}
$$

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

No arbitrary replacement Q-layer maximum is introduced in Sections 02.1–02.2. Any action semantics affecting $k_Q$ must be defined and justified in the later action-space section. Physical/topological realization remains naturally bounded by the eligible set $N_e$.

This separation is mandatory because clipping a learned positive intervention back to the canonical AHBN maximum would make some Q actions ineffective whenever AHBN already proposes $k_{\\mathrm{AHBN}}=6$, while incorrectly presenting the clipping rule as part of canonical AHBN.

### 02.1.5 Proposal-versus-intervention principle

The following quantities are scientifically distinct and MUST never be conflated:

- $mode_{\\mathrm{AHBN}}$: untouched canonical AHBN proposed mode;
- $k_{\\mathrm{AHBN}}$: untouched canonical AHBN S5 requested fanout;
- $a_Q$: selected Q-AHBN2 action;
- $mode_Q$: final Q-AHBN2 requested mode;
- $k_Q$: final Q-AHBN2 requested fanout after the learning intervention;
- $k_{\\mathrm{real}}$: realized number of forwarding targets after eligibility/topology constraints.

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

Historical ControlSim Q-AHBN meta-actions modified $\\tau$. Canonical AHBN has no tau-based suppression actuator. Therefore tau manipulation is architecturally incompatible and is removed from Q-AHBN2.

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
| $z$, $w$ | canonical AHBN | immutable |
| $mode_{\\mathrm{AHBN}}$ | canonical AHBN | immutable proposal |
| `k_AHBN ∈ {2,3,4,5,6}` | canonical AHBN | immutable proposal |
| RL state $s_t$ | Q-AHBN2 | to freeze in 02.3 |
| discretization | Q-AHBN2 | to freeze after state |
| learned action $a_t$ | Q-AHBN2 | to freeze later |
| $mode_Q$ | Q-AHBN2 | permitted intervention output; semantics not yet frozen |
| $k_Q$ | Q-AHBN2 | permitted intervention output; no historical upper fanout cap |
| eligible-target construction/realization | canonical execution boundary | inherited |
| $k_{\\mathrm{real}}$ | execution outcome | bounded by eligible set |
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

The later action-space freeze must define how actions transform $k_{\\mathrm{AHBN}}$ into $k_Q$, including legal lower-bound behavior. Sections 02.1–02.2 intentionally do not pre-empt that decision.

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
| canonical AHBN S5 $k\\in\\{2,\\ldots,6\\}$ | **RETAIN IMMUTABLY** | canonical contract |
| tau modification | **REMOVE** | not part of canonical AHBN |
| historical rule-based GKE `adaptive_update()` as AHBN | **REMOVE / REPLACE WITH CANONICAL AHBN** | conflicts with canonical contract |
| historical `fail_pressure` direct controller | **DO NOT INHERIT** | failure/churn must enter through approved canonical observations / later RL design |
| deterministic failure reaction labelled `recovery_push` | **REMOVE** | cannot attribute deterministic override to Q learning |
| append structural targets beyond requested budget | **REMOVE** | violates canonical requested-budget realization contract |
| ControlSim/GKE historical RL differences | **DO NOT PRESERVE AS PARITY** | Q-AHBN2 requires one logical learning-layer contract |

### 02.2.8 Architectural invariants

The following are now frozen:

**A1 — Canonical-first:** canonical AHBN executes completely before Q-AHBN2.

**A2 — Immutable proposal:** $mode_{\\mathrm{AHBN}}$ and $k_{\\mathrm{AHBN}}$ are recorded unchanged.

**A3 — Post-AHBN learning:** Q-AHBN2 acts only after the AHBN proposal.

**A4 — Canonical S5 preserved:** AHBN itself remains restricted to $k_{\\mathrm{AHBN}}\\in\\{2,3,4,5,6\\}$.

**A5 — Historical Q fanout cap removed:** Q-AHBN2 $k_Q$ is not upper-clipped to AHBN's maximum of 6.

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

$$
s_t = \left(\hat d_t,\hat \ell_t,\hat u_t,\hat c_t\right)
$$

where:

- $\\hat d_t$ = canonical EWMA duplicate pressure;
- $\\hat \\ell_t$ = canonical EWMA latency pressure;
- $\\hat u_t$ = canonical EWMA processing/utilization pressure;
- $\\hat c_t$ = canonical EWMA churn/dynamic-membership pressure.

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

#### A. $z$

Excluded because:

$$
z=-\hat d+\hat \ell+\hat u+\hat c
$$

It is deterministically derivable from the four frozen state variables. Including it would add no new information.

#### B. $w$

Excluded because:

$$
w=\sigma(z)=\frac{1}{1+e^{-z}}
$$

It is deterministically derivable from $z$, which is itself derivable from the four state variables.

#### C. $mode_{\\mathrm{AHBN}}$

Excluded from the RL state because canonical mode is deterministically derived from $w$. It remains a mandatory **base-proposal input to action application** and a mandatory observability field, but it is not an additional Q-table state dimension.

This distinction is important:

```text
used by action application ≠ independent RL state dimension
```

#### D. $k_{\\mathrm{AHBN}}$

Excluded from the RL state because S5 deterministically derives it from canonical $z$. It remains the immutable fanout proposal that the selected Q action may later refine.

Removing the historical Q-layer fanout cap does not justify adding $k_{\\mathrm{AHBN}}$ as another state dimension; the learner already receives the underlying canonical condition vector from which S5 produced it.

#### E. failure/recovery phase labels

Historical ControlSim derived `failure_phase` from latency thresholds, while historical GKE derived a disturbance phase from fail/overload/bottleneck pressures.

These are excluded because they are derived labels rather than independent observations and because the GKE form depends on historical noncanonical heuristics.

#### F. `fail_pressure`, `overload_pressure`, and `bottleneck_pressure`

Excluded as independent state variables.

Q-AHBN2 must not reintroduce the historical GKE direct-control path through the RL state. Effects of failure, overload, and bottleneck conditions must reach the learner through the approved canonical observation semantics where applicable, particularly latency, utilization, and churn/dynamic-membership pressure.

#### G. historical $\\hat\\rho$, $\\hat r$, and old $\\hat c$ semantics

These are not inherited merely because they existed in old ControlSim Q-AHBN.

Q-AHBN2 uses the notation and meanings frozen by the canonical AHBN contract. In Q-AHBN2, $\\hat c$ means canonical **churn/dynamic-membership pressure**. Historical variables with different meanings must not be silently mapped onto it.

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

**S4 — No redundant AHBN derivatives:** $z$, $w$, $mode_{\\mathrm{AHBN}}$, and $k_{\\mathrm{AHBN}}$ are not additional Q-table state dimensions.

**S5 — Proposal preserved separately:** $mode_{\\mathrm{AHBN}}$ and $k_{\\mathrm{AHBN}}$ remain available to the action-application layer and observability.

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

$$
s_t = \left(\hat d_t,\hat \ell_t,\hat u_t,\hat c_t\right)
$$

with $mode_{\\mathrm{AHBN}}$ and $k_{\\mathrm{AHBN}}$ retained separately as the immutable canonical proposal on which the selected learned action operates.

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

## 02.5 Action Space — FROZEN

The next permitted design task is to reconcile the historical Q-AHBN action sets against the frozen post-AHBN intervention boundary and define the minimum scientifically justified Q-AHBN2 action space.

That decision must preserve canonical AHBN's untouched proposal, retain the mandatory removal of the historical Q-layer upper fanout cap, avoid tau, and prevent deterministic recovery heuristics from being represented as learned actions.

### 02.5.1 RO2 design rationale — why the action space exists

The Q-AHBN2 action-space decision MUST be grounded in the dissemination problem established by RO2, rather than treated as an isolated reinforcement-learning design choice.

**RO2 source artifact used for this design decision:**

```text
Characterizing_Latency_Duplication_Trade_off_in_Blockchain_Dissemination__A_Systematic_Study_of_Gossip_and_Structured_Broadcast_04Apr2026_2304.pdf
```

This exact 04 Apr 2026 RO2 draft is the evidentiary source for the RO2-grounded action-space rationale and counterfactual analysis in this section. Future reconciliation SHALL use this exact artifact/version unless a later source-authority decision explicitly supersedes it.

The RO2 draft, *Characterizing Latency–Duplication Trade-off in Blockchain Dissemination: A Systematic Study of Gossip and Structured Broadcast* (04 Apr 2026 draft), characterizes dissemination as a multi-objective trade-off among propagation delay, communication redundancy/overhead, and delivery robustness. Its experiments show that static Gossip and Structured dissemination occupy different operating regions and that their behavior changes with fanout, topology density, cluster-head configuration/stress, churn, and forwarding-capacity heterogeneity.

The relevant RO2 design chain is:

```text
RO2 CHARACTERIZATION
Gossip:
    parallel forwarding
    -> potentially lower delay
    -> higher duplicate/communication overhead
    -> graceful behavior under instability in evaluated scenarios

Structured:
    controlled forwarding
    -> lower redundancy
    -> structural/coordinator dependence
    -> sensitivity to overload, failure, and churn

Dynamic network conditions:
    no single static operating point remains balanced across all evaluated regimes
            |
            v
RO3 / AHBN
    deterministic adaptation of mode + requested fanout
            |
            v
RO4 / Q-AHBN2
    learn whether a bounded post-AHBN refinement is useful
    for the current canonical local condition state
```

Therefore Q-AHBN2 does not exist merely because Q-learning is available. It exists because RO2 provides the empirical problem basis: dissemination involves competing objectives whose useful operating point changes with network conditions.

The RO2 draft expresses this interpretation using a reduced trade-off objective:

$$
\min J_{LD}=\alpha\widetilde L+\beta\widetilde D
\qquad\text{subject to}\qquad
\mathrm{DeliveryRatio}\ge\rho_{\min}
$$

and a broader formulation that also accounts for total transmissions and incomplete delivery. Q-AHBN2 does not directly inherit or optimize these equations unless a later reward contract explicitly does so; they are retained here only as the scientific motivation for adaptive control.

### 02.5.2 Required action-space justification method

Before Section 02.5 can be frozen, the proposed Q-AHBN2 action space SHALL undergo an **Action-Space Counterfactual Analysis**.

The analysis holds constant:

1. the canonical continuous state;
2. the resulting discrete Q-state;
3. the canonical AHBN computation;
4. the immutable AHBN proposal `(mode_AHBN,k_AHBN)`;

and varies only the action-space contract.

Conceptually:

```text
same canonical condition
        |
        v
same Q-state + same frozen AHBN
        |
        v
same (mode_AHBN,k_AHBN)
        |
        +--------------------------+
        |                          |
        v                          v
historical action contract    proposed action contract
        |                          |
        v                          v
permitted output changes      permitted output changes
        +-------------+------------+
                      |
                      v
compare transformation properties
```

This is a design-level counterfactual comparison, not a performance experiment. It may establish properties such as action redundancy, bundled versus isolated intervention, boundary effectiveness, canonical compatibility, cross-platform semantic consistency, and attribution clarity. It MUST NOT be used by itself to claim that the proposed action space improves dissemination performance.

Representative cases SHALL include at least:

- a low-pressure/ordinary canonical condition;
- a duplicate-dominant condition motivated by RO2 Gossip redundancy;
- a latency/utilization/churn pressure condition motivated by RO2 dynamic-condition findings;
- the canonical upper fanout boundary $k_{\\mathrm{AHBN}}=6$;
- the canonical lower fanout boundary $k_{\\mathrm{AHBN}}=2$;
- at least one Gossip proposal and one Structured proposal.

Where useful, an action transform may be written as:

```text
T_a(mode_AHBN,k_AHBN) -> (mode_Q,k_Q)
```

and compared using explicit properties such as whether an action changes the proposal and how many independent control dimensions it modifies.

### 02.5.3 RO2 consistency criterion for candidate actions

A candidate Q-AHBN2 action is scientifically relevant only if it refines a control dimension connected to the RO2 dissemination problem while preserving the frozen AHBN boundary.

The candidate action space should therefore be assessed against these questions:

1. Does it allow the learner to preserve AHBN when AHBN's deterministic operating point is already suitable?
2. Does it permit a bounded change in forwarding intensity, given RO2's demonstrated fanout/duplication/delay relationship?
3. Does it permit a bounded change between Gossip and Structured behavior, given RO2's demonstrated complementary robustness/efficiency characteristics?
4. Does it avoid encoding the desired outcome in an action label such as `recovery_push` or `duplicate_suppression`?
5. Can the effect of the learned intervention be distinguished from the untouched AHBN proposal?
6. Is the same action semantics implementable in ControlSim and Kubernetes?
7. Does it avoid reopening canonical AHBN?

The action-space freeze will be made only after this RO2-grounded counterfactual analysis is recorded.

### 02.5.4 RO2-grounded Action-Space Counterfactual Analysis

#### Purpose

This analysis compares the historical ControlSim action contract, the historical GKE action contract, and the candidate Q-AHBN2 primitive action contract while holding the canonical condition and canonical AHBN proposal fixed.

It is a design-level counterfactual analysis. It evaluates what each action contract is capable of changing; it does not claim that one contract produces better dissemination performance.

#### Contracts compared

Historical ControlSim actions:
- `ahbn_base`: fanout 0, weight 0, tau x1.00
- `more_structured`: fanout -1, weight -0.12, tau x0.90
- `more_gossip`: fanout +1, weight +0.12, tau x1.08
- `duplicate_suppression`: fanout 0, weight -0.08, tau x0.95
- `recovery_push`: fanout +1, weight +0.18, tau x1.15
- `resource_conservative`: fanout 0, weight -0.05, tau x0.95

Historical ControlSim recomputed mode after modifying weight and clipped fanout to configured historical minimum/maximum bounds.

Historical GKE actions:
- `ahbn_base`: fanout 0, no preferred mode
- `more_structured`: fanout -1, force Structured
- `more_gossip`: fanout +1, force Gossip
- `duplicate_suppression`: fanout -1, force Structured
- `recovery_push`: fanout +2, force Gossip
- `resource_conservative`: fanout -1, preserve mode

Historical GKE clipped the resulting fanout to its configured minimum/maximum bounds.

Candidate Q-AHBN2 primitives under analysis:
- `KEEP`: preserve mode and fanout
- `FANOUT_DOWN`: preserve mode, fanout -1
- `FANOUT_UP`: preserve mode, fanout +1
- `SET_GOSSIP`: set Gossip, preserve fanout
- `SET_STRUCTURED`: set Structured, preserve fanout

These five actions are the action-space candidates evaluated by this counterfactual analysis and are frozen by the final contract in Section 02.5.5.

#### Controlled situations

Six situations are selected to represent the RO2 problem structure and canonical AHBN boundaries. Continuous examples are illustrative canonical inputs; the AHBN proposal follows the frozen controller.

| Case | Canonical continuous state (d,l,u,c) | Discrete state | z | AHBN proposal | RO2 purpose |
|---|---|---|---:|---|---|
| C1 | (0.10,0.10,0.10,0.10) | (L,L,L,L) | +0.20 | Gossip, k=3 | ordinary/low pressure |
| C2 | (0.72,0.18,0.43,0.09) | (H,L,M,L) | -0.02 | Structured, k=3 | duplicate-dominant pressure |
| C3 | (0.10,0.70,0.70,0.40) | (L,H,H,M) | +1.70 | Gossip, k=6 | latency/utilization/churn pressure + upper S5 boundary |
| C4 | (0.80,0.10,0.10,0.10) | (H,L,L,L) | -0.50 | Structured, k=2 | duplicate pressure + lower S5 boundary |
| C5 | (0.20,0.45,0.35,0.20) | (L,M,M,L) | +0.80 | Gossip, k=4 | intermediate Gossip operating point |
| C6 | (0.60,0.10,0.10,0.10) | (M,L,L,L) | -0.30 | Structured, k=2 | Structured operating point near low fanout |

C1 is not interpreted as a physical “normal” regime; it is simply a low-bin test vector. C2-C6 are likewise controlled design vectors, not claims that these exact values reproduce an RO2 experiment.

#### Case C2 — same state, same AHBN proposal, different action semantics

For C2:

```text
state = (H,L,M,L)
AHBN = (Structured,3)
```

Historical ControlSim can alter fanout, canonical weight-derived mode, and tau in one selected action. Historical GKE can simultaneously force a mode and alter fanout. The candidate contract separates these interventions:

```text
KEEP            -> (Structured,3)
FANOUT_DOWN     -> (Structured,2)
FANOUT_UP       -> (Structured,4)
SET_GOSSIP      -> (Gossip,3)
SET_STRUCTURED  -> (Structured,3)
```

Thus the candidate contract can distinguish a mode refinement from a fanout refinement. Historical bundled actions cannot always provide that attribution.

#### Case C3 — upper fanout boundary

For C3:

```text
AHBN = (Gossip,6)
```

A historical implementation with `max_fanout=6` maps a positive fanout request back to 6:

```text
6 + 1 -> clip -> 6
```

and historical GKE `recovery_push` can similarly request `6+2` but be clipped by its configured maximum.

Under the candidate primitive semantics:

```text
FANOUT_UP: 6 + 1 -> 7
```

The value 7 is not a new arbitrary global cap; it is the direct result of the +1 refinement applied to the canonical S5 maximum. Actual forwarding remains eligibility bounded.

This case exposes why the historical Q-layer upper cap can make a nominal positive action ineffective at the canonical boundary.

#### Case C4/C6 — lower fanout boundary

For an AHBN proposal with $k_{\\mathrm{AHBN}}=2$, a -1 primitive produces a requested fanout of 1 if the candidate contract permits the direct unit refinement:

```text
2 - 1 -> 1
```

Historical implementations instead depend on their configured minimum-fanout clipping. This boundary therefore requires an explicit Q-AHBN2 contract rather than silently inheriting historical bounds.

#### Transformation-property comparison

Let:

```text
T_a(p_AHBN) -> p_Q
```

denote the post-AHBN action transformation.

For design analysis define:

```text
E(a,p) = 1 if T_a(p) != p, otherwise 0
```

for proposal-level effectiveness, and define intervention dimensionality over the controlled quantities:

```text
D(a) =
    I(mode changes) +
    I(fanout changes) +
    I(weight changes) +
    I(tau changes)
```

The candidate primitive contract is designed so that `D(a) <= 1` for each action, with `D(KEEP)=0`. Historical ControlSim actions may have `D(a)>1`; historical GKE mode-preferring actions may simultaneously alter mode and fanout.

This does not prove better performance. It establishes cleaner intervention attribution.

#### RO2-grounded interpretation

RO2 identifies two control-relevant dissemination mechanisms:

1. forwarding intensity affects the latency/duplication/communication-cost trade-off;
2. Gossip and Structured dissemination expose complementary robustness/efficiency characteristics under changing conditions.

The candidate action contract maps directly onto those two control dimensions:

```text
RO2 forwarding-intensity trade-off
        -> FANOUT_DOWN / FANOUT_UP

RO2 Gossip-vs-Structured trade-off
        -> SET_GOSSIP / SET_STRUCTURED

AHBN already suitable
        -> KEEP
```

This provides a direct RO2 -> RO3 -> RO4 trace without importing historical tau, weight manipulation, disturbance labels, or outcome-named heuristics.

#### Findings

F1 — Historical ControlSim and GKE do not provide one parity-preserved action specification.

F2 — Historical ControlSim bundles multiple control dimensions in several actions, weakening attribution.

F3 — Historical GKE also bundles mode preference and fanout change in several actions.

F4 — Historical semantic labels such as `recovery_push` and `duplicate_suppression` encode intended effects/contexts rather than neutral primitive operations.

F5 — Historical fanout clipping can make positive actions ineffective at the canonical S5 upper boundary.

F6 — A primitive candidate contract can preserve AHBN, adjust forwarding intensity, or adjust dissemination mode independently.

F7 — The candidate controls map directly to the two dissemination-control dimensions motivated by RO2: forwarding intensity and Gossip/Structured operating behavior.

F8 — This analysis supports interpretability, canonical compatibility, and cross-platform parity; it does NOT establish empirical performance superiority.

#### Counterfactual-analysis decision

The counterfactual analysis supports carrying the five primitive actions forward as the preferred candidate for final Section 02.5 freeze:

```text
KEEP
FANOUT_DOWN
FANOUT_UP
SET_GOSSIP
SET_STRUCTURED
```

The lower-bound semantics and final invariants are resolved in the final contract below.

### 02.5.5 Final Q-AHBN2 Action-Space Contract — FROZEN

#### Action set

The Q-AHBN2 action space is frozen as:

```text
A = {
    KEEP,
    FANOUT_DOWN,
    FANOUT_UP,
    SET_GOSSIP,
    SET_STRUCTURED
}
```

Let the untouched canonical AHBN proposal be:

$$
p_{\mathrm{AHBN}}=(mode_{\mathrm{AHBN}},k_{\mathrm{AHBN}})
$$

where:

$$
mode_{\mathrm{AHBN}}\in\{\mathrm{Gossip},\mathrm{Structured}\},\qquad
k_{\mathrm{AHBN}}\in\{2,3,4,5,6\}
$$

Q-AHBN2 applies exactly one selected action after the complete AHBN proposal and before canonical eligible-target realization.

The frozen action transforms are:

$
(mode_Q,k_Q)=
\begin{cases}
(mode_{\mathrm{AHBN}},k_{\mathrm{AHBN}}), & a=\mathrm{KEEP},\\
(mode_{\mathrm{AHBN}},k_{\mathrm{AHBN}}-1), & a=\mathrm{FANOUT\_DOWN},\\
(mode_{\mathrm{AHBN}},k_{\mathrm{AHBN}}+1), & a=\mathrm{FANOUT\_UP},\\
(\mathrm{Gossip},k_{\mathrm{AHBN}}), & a=\mathrm{SET\_GOSSIP},\\
(\mathrm{Structured},k_{\mathrm{AHBN}}), & a=\mathrm{SET\_STRUCTURED}.
\end{cases}
$

Equivalently:

```text
T_a(m,k) =
    (m,k)            if a = KEEP
    (m,k-1)          if a = FANOUT_DOWN
    (m,k+1)          if a = FANOUT_UP
    (Gossip,k)       if a = SET_GOSSIP
    (Structured,k)   if a = SET_STRUCTURED
```

#### Scientific derivation

RO2 establishes the dissemination problem and identifies two control-relevant dimensions used by the subsequent AHBN design:

1. forwarding intensity, represented operationally by requested fanout; and
2. Gossip-versus-Structured dissemination behavior.

RO3 canonical AHBN operationalizes these dimensions as $k_{\\mathrm{AHBN}}$ and $mode_{\\mathrm{AHBN}}$.

RO4 Q-AHBN2 therefore does not introduce unrelated dissemination controls. Its learned intervention is restricted to:

- preserving the complete AHBN proposal;
- changing forwarding intensity by one unit while preserving mode; or
- changing dissemination mode while preserving requested fanout.

Thus four refinement actions derive from the two RO2/RO3 control dimensions, while `KEEP` exists because Q-AHBN2 is an enhancement over AHBN and must be able to leave an already-suitable AHBN proposal untouched.

This derivation establishes scientific relevance and attribution; it does not claim that any action is optimal or that Q-AHBN2 will outperform AHBN. Those are empirical questions for later learning validation and formal experiments.

#### Frozen fanout boundary

Canonical AHBN remains unchanged:

$$
k_{\mathrm{AHBN}} \in \{2,3,4,5,6\}
$$

The Q layer is a one-step refinement:

$$
\Delta k_Q\in\{-1,0,+1\}
$$

Therefore the reachable Q-requested fanout is:

$$
k_Q\in\{1,2,3,4,5,6,7\}
$$

or:

$$
1\le k_Q\le 7
$$

This range is derived from the frozen AHBN range plus the frozen unit refinement:

$$
[2,6]+[-1,+1]\rightarrow[1,7]
$$

The values 1 and 7 are therefore not newly tuned AHBN parameters and do not alter S5.

Lower boundary:

```text
k_AHBN = 2
FANOUT_DOWN
2 - 1 -> k_Q = 1
```

This is permitted. RO2 independently evaluated $k=1$ as a meaningful forwarding-intensity operating point; this does not imply that $k=1$ is always beneficial.

Upper boundary:

```text
k_AHBN = 6
FANOUT_UP
6 + 1 -> k_Q = 7
```

This is permitted. The historical Q-layer upper clip to 6 SHALL NOT be inherited.

Q-AHBN2 does not define a learned $k_Q=0$ action. A zero requested fanout would constitute intentional forwarding suppression rather than the frozen one-step refinement. Realized forwarding may nevertheless be zero when no eligible target exists.

#### Requested-versus-realized forwarding

The three fanout quantities SHALL remain distinct:

$$
k_{\mathrm{AHBN}}\rightarrow k_Q\rightarrow k_{\mathrm{real}}
$$

where:

- $k_{\\mathrm{AHBN}}$ is the untouched canonical S5 proposal;
- $k_Q$ is the post-AHBN Q-AHBN2 requested fanout;
- $k_{\\mathrm{real}}$ is the actual realized forwarding count after canonical mode-specific eligibility.

The execution bound remains:

$$
0 \le k_{\mathrm{real}} \le \min\!\left(k_Q, |N_e|\right)
$$

Q-AHBN2 changes only the requested post-AHBN proposal. It does not bypass canonical eligible-target realization.

#### Frozen action-space invariants

A1 — Canonical AHBN SHALL complete its full deterministic computation before any Q-AHBN2 action is applied.

A2 — The untouched `(mode_AHBN,k_AHBN)` proposal SHALL remain separately observable and reconstructable.

A3 — Exactly one Q-AHBN2 action SHALL be selected per Q decision event.

A4 — `KEEP` SHALL modify neither mode nor requested fanout.

A5 — `FANOUT_DOWN` and `FANOUT_UP` SHALL modify requested fanout only and SHALL NOT modify mode.

A6 — `SET_GOSSIP` and `SET_STRUCTURED` SHALL modify mode only and SHALL NOT modify requested fanout.

A7 — A mode-setting action MAY be a proposal-level no-op when AHBN already selected that mode. The selected action and whether the proposal changed SHALL be logged separately.

A8 — The Q layer SHALL NOT modify canonical $z$, $w=\\sigma(z)$, EWMA state, normalization, S5 thresholds, or canonical AHBN mode computation.

A9 — The Q layer SHALL NOT introduce or modify $\\tau$.

A10 — Historical outcome-labelled actions such as `recovery_push`, `duplicate_suppression`, and `resource_conservative` SHALL NOT be inherited as Q-AHBN2 actions.

A11 — Deterministic failure/recovery overrides SHALL NOT be represented or logged as learned Q actions.

A12 — The historical Q-layer upper fanout cap of 6 SHALL NOT be inherited. `FANOUT_UP` applied to $k_{\\mathrm{AHBN}}=6$ SHALL yield $k_Q=7$.

A13 — `FANOUT_DOWN` applied to $k_{\\mathrm{AHBN}}=2$ SHALL yield $k_Q=1$.

A14 — Q-AHBN2 SHALL NOT deliberately request $k_Q=0$ under this action contract.

A15 — Realized forwarding SHALL remain bounded by canonical mode-specific eligible-target realization: `0 <= k_real <= min(k_Q, |N_e|)`.

A16 — Action semantics SHALL be identical across ControlSim and Kubernetes.

A17 — The implementation and trace SHALL distinguish $mode_{\\mathrm{AHBN}}$, $k_{\\mathrm{AHBN}}$, selected $a_Q$, $mode_Q$, $k_Q$, and $k_{\\mathrm{real}}$.

A18 — No action in this frozen contract is interpreted as intrinsically beneficial. Which action is useful in a state is an empirical learning question.

#### Q-table consequence

Section 02.4 freezes 81 discrete Q states and this section freezes 5 actions. Therefore the tabular learner contains:

$$
|\mathcal S|=81,\qquad |\mathcal A|=5,\qquad |Q|=81\times5=405
$$

This is a structural consequence of the frozen state and action contracts, not evidence of learning quality or convergence.

### 02.5.6 Action Space Gate

```text
02.5 ACTION SPACE GATE: PASS / FROZEN
```

The Q-AHBN2 action space SHALL NOT be changed during later reward, hyperparameter, implementation, smoke, pilot, or formal-experiment stages merely to improve observed performance.

Reopening Section 02.5 requires a documented contradiction with a higher-authority frozen contract, an implementation impossibility that invalidates the specified semantics, or another genuine scientific inconsistency. Any reopening SHALL be explicit and auditable.

The next permitted design task is:

```text
02.6 REWARD DESIGN
```

Reward design SHALL be reconciled from the RO2 scientific objective, historical ControlSim reward, historical GKE reward, and the frozen Q-AHBN2 state/action architecture. No Q-AHBN2 implementation is authorized merely by freezing Section 02.5.


---

## 02.6 Reward Design — Evidence Reconstruction and Reconciliation

**Status:** PENDING — evidence reconstruction only. No Q-AHBN2 reward equation is proposed or frozen in this subsection.

### 02.6.1 Controlled question

The reward-design question is:

> What outcome signal should Q-AHBN2 use to learn whether a post-AHBN refinement was useful, given the RO2 scientific objective and the incompatible historical ControlSim and GKE reward implementations?

The method is evidence-first:

```text
RO2 scientific objective
        |
        +--> historical ControlSim reward
        |
        +--> historical GKE reward
        |
        v
semantic reconciliation
        |
        v
requirements / incompatibilities
        |
        v
candidate Q-AHBN2 reward     [NOT YET]
```

No historical reward is inherited merely because it existed in code.

### 02.6.2 RO2 scientific objective

Authoritative RO2 source artifact:

```text
Characterizing_Latency_Duplication_Trade_off_in_Blockchain_Dissemination__A_Systematic_Study_of_Gossip_and_Structured_Broadcast_04Apr2026_2304.pdf
```

RO2 treats dissemination as a multi-objective trade-off among propagation performance, communication redundancy/cost, delivery/coverage, and robustness under changing network conditions.

Its reduced analytical formulation is:

$$
\min J_{LD}=\alpha\widetilde L+\beta\widetilde D
\qquad\text{subject to}\qquad
\mathrm{DeliveryRatio}\ge\rho_{\min}
$$

The manuscript also expresses the trade-off as minimizing expected propagation delay and duplicate transmissions subject to a minimum expected delivery ratio.

This formulation is an analytical framework for characterizing static dissemination operating points. It is NOT itself a Q-AHBN2 reward function, and its alpha/beta terms SHALL NOT be copied into Q-AHBN2 without a separate reward-design justification.

RO2 provides three important reward-design constraints:

1. lower duplication alone is not sufficient evidence of improvement;
2. lower delay alone is not sufficient evidence of improvement;
3. delivery/coverage must not be sacrificed merely to obtain apparently lower redundancy or delay.

This is particularly important under heterogeneous forwarding capacity, where RO2 observed that fewer duplicates can result from weaker dissemination rather than genuine efficiency improvement.

### 02.6.3 Historical ControlSim reward reconstruction

Source:

```text
wwiras/q-ahbn
v1.0/ahbn/q_learning.py
```

The active historical ControlSim reward computes:

```text
dup   = clip(d_hat, 0, 1)
lat   = clip(l_hat / latency_ref, 0, 2)
load  = clip(u_hat / load_ref, 0, 2)
red   = clip(r_hat, 0, 2)
churn = clip(rho_hat, 0, 2)
cap   = clip(c_hat, 0, 2)

delivery_estimate = clip(state.delivery_estimate, 0, 1)

recovery_pressure =
    min(1,
        0.5 * min(1, lat)
      + 0.5 * min(1, churn))
```

The active base reward is:

$
R_{CS}=15.00\,delivery_{estimate}
-0.15\,dup-0.10\,lat-0.05\,load-0.05\,red-0.05\,churn-0.05\,cap
$

with an additional poor-delivery penalty:

```text
if delivery_estimate < 0.80:
    R_CS -= 2.0
```

and a dynamic-condition bonus:

```text
if churn >= 0.20 or lat >= 1.20:
    R_CS += 4.0 * recovery_pressure
```

Important reconstruction notes:

- delivery is deliberately dominant in the active historical weights;
- the file comments state that this was a redesign after an earlier behavior reduced duplicates while also reducing delivery;
- the historical reward includes variables that are not part of the frozen canonical Q-AHBN2 state semantics, including $\\hat r$, historical $\\hat\\rho$, and historical capacity-semantic $\\hat c$;
- its historical $\\hat c$ MUST NOT be confused with canonical AHBN $\\hat c$, which means churn/instability pressure;
- the dynamic recovery bonus embeds an explicit heuristic preference under high historical churn/latency;
- the historical 0.80 delivery threshold and all numerical coefficients are historical evidence, not Q-AHBN2 defaults.

### 02.6.4 Historical GKE reward reconstruction

Source:

```text
wwiras/q-ahbn_gke
app/q_learning_gke.py
```

The historical GKE learner computes:

```text
new_count = max(0, recv_count - duplicate_count)

delivery_proxy =
    new_count / max(1, recv_count)

dup =
    clip(duplicate_ratio, 0, 1)

f_norm =
    min(2, forward_count / 20)

recovery =
    clip(fail_pressure, 0, 1)
```

and:

$
R_{GKE}=8.00\,delivery_{proxy}-0.30\,dup-0.10\,f_{norm}+2.00\,recovery
$

Important reconstruction notes:

- `delivery_proxy` is a local new-reception fraction, not the experiment-level delivery ratio;
- `fail_pressure` is historical GKE state semantics and is not part of canonical AHBN;
- forwarding count is explicitly penalized as a local communication-cost proxy;
- propagation latency is not an explicit term in this reward;
- the coefficients differ materially from ControlSim;
- the GKE reward therefore does not preserve reward parity with the historical ControlSim learner.

### 02.6.5 Three-way comparison

| Dimension | RO2 scientific objective | Historical ControlSim reward | Historical GKE reward |
|---|---|---|---|
| Delivery / coverage | Constraint / robustness requirement | Strong positive `delivery_estimate` + penalty below 0.80 | Positive local `delivery_proxy` |
| Duplication | Explicit objective to reduce | Explicit penalty | Explicit penalty |
| Propagation latency | Explicit objective to reduce | Explicit penalty | Not explicit |
| Forwarding / transmissions | Communication cost considered in experiments/broader interpretation | No active forwarding term in final reward | Explicit normalized forwarding penalty |
| Utilization/load | Dynamic-condition concern, not reduced RO2 objective term | Explicit penalty | Not explicit in reward |
| Churn/failure | Robustness condition affecting dissemination | Churn penalty + conditional recovery bonus | Positive failure-pressure bonus |
| Capacity/heterogeneity | Evaluated dynamic condition | Historical capacity penalty | Not explicit in reward |
| Special threshold/bonus | Minimum delivery concept in analytical formulation; no RL coefficient prescribed | delivery < 0.80 penalty; high-churn/high-latency bonus | failure-pressure bonus |
| Semantics portable to canonical AHBN? | Scientific objective is portable; metric realization still requires contract | No — contains obsolete/historical state semantics | No — contains GKE-specific fail-pressure/local proxy semantics |

### 02.6.6 Reconciliation findings

RWD-F1 — The two historical implementations do NOT define one parity-preserved reward specification.

RWD-F2 — Both historical rewards prioritize dissemination effectiveness positively and penalize duplication, which is directionally consistent with the RO2 requirement that redundancy reduction must not be achieved by simply weakening dissemination.

RWD-F3 — Only the historical ControlSim reward explicitly penalizes latency, despite latency being a central RO2 objective.

RWD-F4 — Only the historical GKE reward explicitly penalizes forwarding count, providing a local communication-cost signal distinct from duplicate ratio.

RWD-F5 — Historical ControlSim $\\hat r$, $\\hat\\rho$, and capacity-semantic $\\hat c$, and historical GKE `fail_pressure`, cannot be imported directly because their semantics do not match the frozen canonical Q-AHBN2 contract.

RWD-F6 — The historical ControlSim 0.80 poor-delivery threshold, recovery bonus, and all historical numerical weights are design choices from the old learner; RO2 does not independently validate those values.

RWD-F7 — RO2's reduced objective is not a ready-made RL reward. It is an analytical statement that delay and duplication should be reduced subject to adequate delivery/coverage.

RWD-F8 — RO2 warns against interpreting reduced duplication as improvement when dissemination becomes weaker. Therefore a future Q-AHBN2 reward must contain a mechanism that prevents the learner from receiving a misleadingly favorable signal merely by reducing forwarding and consequently reducing coverage.

RWD-F9 — Reward inputs and evaluation metrics must remain semantically distinguished. In particular, a local online learning signal must not be called experiment-level `delivery_ratio` unless it actually measures that quantity.

RWD-F10 — No new Q-AHBN2 reward equation or coefficient is justified by this reconstruction alone.

### 02.6.RD Reward-design requirements derived from evidence

Before proposing a candidate equation, the Q-AHBN2 reward SHALL satisfy the following requirements:

```text
RD1  Preserve dissemination effectiveness / coverage as a primary concern.
RD2  Penalize unnecessary duplication/redundancy.
RD3  Represent latency only through a clearly defined online signal if such a signal
     is available at the learning decision/update lifecycle.
RD4  Do not reward apparent efficiency obtained by dissemination collapse.
RD5  Use signals whose semantics can be made equivalent across ControlSim and Kubernetes.
RD6  Do not import obsolete r_hat, rho_hat, capacity-c_hat, fail_pressure, or hidden
     recovery-phase semantics.
RD7  Do not embed action labels or deterministic recovery heuristics in the reward.
RD8  Distinguish online/local reward signals from experiment-level evaluation metrics.
RD9  Normalize or bound reward components so numerical scale, rather than scientific
     priority, does not accidentally dominate learning.
RD10 Treat all coefficients, thresholds, penalties, and bonuses as new design decisions
     requiring explicit justification rather than historical inheritance.
```

### 02.6.1A Action Lifetime — FROZEN

Reconciliation against the historical ControlSim and Kubernetes execution paths supports the same logical decision unit: a peer makes its forwarding decision when handling a **new** message; a duplicate reception is recorded and dropped rather than initiating another forwarding decision for that duplicate.

For peer $i$ handling message $m$:

$$
(i,m)\rightarrow s_t^{(i)}\rightarrow p_t^{(i)}\rightarrow a_t^{(i,m)}
\rightarrow(mode_Q,k_Q)\rightarrow Targets(i,m).
$$

Therefore,

$$
\boxed{\text{Action unit = one new-message forwarding decision at one peer}}
$$

and $a_t^{(i,m)}$ governs the post-AHBN forwarding treatment of message $m$ at peer $i$. It does not represent a separate Q decision for each outgoing link and does not implicitly govern an arbitrary multi-message control interval.

The action lifetime ends once the corresponding requested forwarding treatment and target realization have been determined:

$$
a_t^{(i,m)}\rightarrow(mode_Q,k_Q)\rightarrow Targets(i,m)
\rightarrow\boxed{\text{action lifetime ends}}.
$$

#### Historical reward/update timing is NOT inherited

This freeze defines only **what the action controls**. It does not freeze when reward is produced or which later observations belong to that action.

The historical ControlSim and GKE learners updated a previous state-action pair at a later controller invocation, and historical GKE reward inputs included cumulative peer counters. Those mechanisms do not provide clean per-$(i,m,a_t)$ causal attribution and are **not inherited** by this freeze.

$$
\boxed{\text{02.6.1A freezes action lifetime only; historical reward/update timing is NOT frozen or inherited.}}
$$

The next controlled decision is **02.6.1B — Reward Attribution Window**:

$$
\boxed{\text{After }a_t^{(i,m)}\text{ governs }m,\text{ which subsequent events belong to it, and when is }R_t\text{ closed?}}
$$

Only 02.6.1B may establish whether and how subsequent $NEW$, $DUPLICATE$, $FAILED$, and forwarding-effort $F$ events are attributable to the frozen $(i,m,a_t)$ decision. Reward signs, weights, coefficients, thresholds, bonuses, penalties, and equations remain blocked.

$$
\boxed{\text{02.6.1A ACTION LIFETIME GATE = PASS / FROZEN}}
$$

---

### 02.6.1B-1 Terminal Outcome Semantics — FROZEN

This sub-decision freezes the semantics of the direct outcomes attributable to one forwarding attempt. It does **not** define reward signs, weights, coefficients, thresholds, bonuses, penalties, or the reward equation.

The forwarding lifecycle is separated as:

$$
\boxed{
\text{requested fanout}
\rightarrow
\text{realized targets}
\rightarrow
\text{attempts}
\rightarrow
\{NEW,DUPLICATE,FAILED\}
}
$$

For a direct forwarding attempt from peer $i$ to target peer $j$ for message $m$:

$$
\boxed{
\begin{aligned}
NEW &: \text{attempt delivered }m\text{ to a peer that had not seen it},\\
DUPLICATE &: \text{attempt delivered }m\text{ to a peer that had already seen it},\\
FAILED &: \text{initiated attempt did not successfully deliver }m,\\
F_t &: \text{number of direct forwarding attempts initiated},\\
F_t &= NEW_t+DUPLICATE_t+FAILED_t.
\end{aligned}
}
$$

Each initiated direct attempt MUST terminate in exactly one mutually exclusive outcome:

$$
o_{ijm}\in\{NEW,DUPLICATE,FAILED\}.
$$

A target that is not realized because of the existing eligibility/realization constraint does not create a forwarding attempt and therefore does not create a synthetic $FAILED$ outcome. The existing realization rule remains authoritative:

$$
k_{\mathrm{real}}=\min(k_Q,|N_e|).
$$

Accordingly, $F_t$ counts **actual direct forwarding attempts initiated**, not requested fanout and not unrealized target slots.

The semantic distinction is:

$$
\begin{aligned}
NEW &: \text{delivered and new information},\\
DUPLICATE &: \text{delivered but already-known information},\\
FAILED &: \text{not successfully delivered}.
\end{aligned}
$$

Therefore $FAILED\neq DUPLICATE$, and the accounting invariant

$$
\boxed{F_t=NEW_t+DUPLICATE_t+FAILED_t}
$$

MUST hold for the terminal outcomes associated with the direct attempts in one attribution set.

This freeze is implementation-independent. ControlSim and Kubernetes instrumentation must subsequently be reconciled to expose these same semantics; historical counters or transport-specific labels do not override this contract.

$$
\boxed{\text{02.6.1B-1 TERMINAL OUTCOME SEMANTICS = PASS / FROZEN}}
$$

The next controlled decision remains within **02.6.1B — Reward Attribution Window** and must determine the minimal cross-platform instrumentation and closure rule needed to observe these frozen outcomes for all direct attempts.

---

### 02.6.1B-2 Outcome Instrumentation and Closure Rule — FROZEN

This sub-decision freezes the minimum cross-platform accounting and closure semantics required to observe the terminal outcomes defined in 02.6.1B-1. It does **not** assign reward values, signs, weights, coefficients, thresholds, bonuses, or penalties.

For every direct forwarding attempt initiated by $a_t^{(i,m)}$, the implementation MUST create one pending attempt record. Each pending attempt MUST resolve exactly once to one frozen terminal outcome:

$$
o_{ijm}\in\{NEW,DUPLICATE,FAILED\}.
$$

Conceptually:

$$
a_t^{(i,m)}
\rightarrow
\{\text{pending direct attempts}\}
\rightarrow
\{NEW,DUPLICATE,FAILED\}
\rightarrow
\text{close attribution window}.
$$

The attribution window closes only when no initiated direct attempt remains pending. Equivalently:

$$
\boxed{
NEW_t+DUPLICATE_t+FAILED_t=F_t
}
$$

where $F_t$ is the number of direct forwarding attempts initiated, as frozen in 02.6.1B-1.

This closure rule is outcome-based rather than based on an arbitrary fixed reward-window duration. A platform-specific transport timeout MAY determine that an individual attempt has reached the terminal state $FAILED$, but such a timeout does not define the reward attribution window itself.

#### Zero-attempt edge case

A valid Q-AHBN2 decision can produce no actual forwarding attempts when no eligible target can be realized. In that case:

$$
F_t=0.
$$

No synthetic $FAILED$ outcome is created because no forwarding attempt was initiated. Therefore:

$$
\boxed{
F_t=0
\Rightarrow
NEW_t=DUPLICATE_t=FAILED_t=0
\Rightarrow
\text{close immediately}
}
$$

The completed action record MUST still be retained as a valid decision with zero realized attempts. This subsection makes **no statement about the eventual reward value** of such an action.

#### Minimum cross-platform instrumentation contract

ControlSim and Kubernetes MUST expose sufficient per-attempt identity and outcome information to associate every initiated direct attempt with:

$$
(\text{source peer},\text{message},\text{target peer})
\rightarrow
\{NEW,DUPLICATE,FAILED\}.
$$

Existing platform-specific counters, ACKs, exceptions, event labels, or transport mechanisms MAY be used to implement this contract, but they do not redefine the frozen semantics.

For ControlSim, a direct attempt that cannot be delivered MUST be recorded explicitly as $FAILED$ rather than disappearing through a silent return. For Kubernetes, receiver responses and sender-side rejection/timeout/exception paths MUST be mapped onto the same canonical terminal outcomes.

No new network-failure model is introduced by this requirement; this is outcome accounting needed to make the same reward-event semantics observable on both platforms.

$$
\boxed{\text{02.6.1B-2 OUTCOME INSTRUMENTATION AND CLOSURE RULE = PASS / FROZEN}}
$$

Reward signs, weights, coefficients, thresholds, bonuses, penalties, and the reward equation remain **BLOCKED**.

---

### 02.6.2 Reward Component Selection

The reward-event boundary is now sufficiently defined to evaluate candidate reward components for scientific admissibility. Component selection MUST proceed one component at a time:

$$
02.6.2.1\;NEW
\rightarrow
02.6.2.2\;DUPLICATE
\rightarrow
02.6.2.3\;FAILED
\rightarrow
02.6.2.4\;F
\rightarrow
02.6.2.5\;\text{component decision matrix}.
$$

At this stage, inclusion/admissibility is evaluated independently of sign, normalization, weight, coefficient, threshold, bonus, penalty, or final reward equation.

#### 02.6.2.1 `NEW` — INCLUDE / ADMISSIBLE — FROZEN

The frozen event semantics define $NEW_t$ as the number of direct forwarding attempts generated by the action that successfully delivered message $m$ to target peers that had not previously seen that message.

$NEW_t$ is scientifically admissible because it provides direct local evidence that the selected post-AHBN forwarding action expanded dissemination coverage:

$$
a_t^{(i,m)}
\rightarrow
\text{direct forwarding attempt}
\rightarrow
NEW.
$$

This signal is deliberately distinct from the experiment-level delivery ratio:

$$
\boxed{NEW_t\neq\mathrm{DeliveryRatio}}.
$$

Rather,

$$
\boxed{
NEW_t=
\text{local evidence that }a_t^{(i,m)}
\text{ successfully expanded message coverage}
}.
$$

This satisfies the requirement that dissemination effectiveness remain represented in the learning signal without substituting an experiment-level evaluation metric for an online local observation.

Raw $NEW_t$ may be affected by the number of forwarding attempts: a larger fanout can create more opportunities for new deliveries. That issue does **not** invalidate $NEW_t$ as an admissible component; it must instead be handled later when the relationships among $NEW_t$, $DUPLICATE_t$, $FAILED_t$, and $F_t$ are considered and when normalization/reward construction is explicitly opened.

Accordingly:

$$
\boxed{\text{02.6.2.1 }NEW=\text{ INCLUDE / ADMISSIBLE / FROZEN}}
$$

This decision freezes **component admissibility only**. It does not assert that $NEW_t$ receives a positive sign, nor does it freeze a normalization, coefficient, weight, threshold, bonus, penalty, or equation.

Therefore:

$$
\boxed{
\text{sign, normalization, weight, and reward equation remain BLOCKED}
}
$$

The next controlled component decision is **02.6.2.2 — `DUPLICATE`**.

---

#### 02.6.2.2 `DUPLICATE` — INCLUDE / ADMISSIBLE — FROZEN

The frozen event semantics define $DUPLICATE_t$ as the number of direct forwarding attempts generated by the action that successfully delivered message $m$ to target peers that had already seen that message.

$DUPLICATE_t$ is scientifically admissible because it provides direct local evidence of redundant dissemination produced by the selected post-AHBN action:

$$
\boxed{
DUPLICATE_t=
\text{local evidence of redundant dissemination produced by }a_t^{(i,m)}
}.
$$

This information is relevant to the RO2 latency--duplication trade-off and is distinct from both successful coverage expansion and forwarding effort:

$$
DUPLICATE_t\neq NEW_t,
\qquad
DUPLICATE_t\neq F_t.
$$

A lower duplicate count MUST NOT by itself be interpreted as better dissemination. An action can produce few or zero duplicates simply because it forwards little or nothing. The already-admissible $NEW_t$ component preserves information about useful coverage expansion, while the later component-selection and reward-construction stages must preserve the distinction between reducing redundancy and collapsing dissemination.

Accordingly:

$$
\boxed{\text{02.6.2.2 }DUPLICATE=\text{ INCLUDE / ADMISSIBLE / FROZEN}}
$$

This decision freezes **component admissibility only**. It deliberately does not assert

$$
DUPLICATE_t\rightarrow -R_t.
$$

Therefore:

$$
\boxed{
\text{sign, normalization, weight, coefficient, and reward equation remain BLOCKED}
}
$$

The next controlled component decision is **02.6.2.3 — `FAILED`**.

---

#### 02.6.2.3 `FAILED` — INCLUDE / ADMISSIBLE — FROZEN

The frozen event semantics define $FAILED_t$ as the number of initiated direct forwarding attempts generated by the action that did not successfully deliver message $m$ to the selected target peer.

$FAILED_t$ is scientifically admissible because it provides direct local evidence that initiated forwarding effort did not successfully deliver:

$$
\boxed{
FAILED_t=
\text{local evidence that initiated forwarding effort did not successfully deliver}
}.
$$

A failed attempt is semantically distinct from a duplicate delivery and from forwarding effort itself:

$$
FAILED_t\neq DUPLICATE_t,
\qquad
FAILED_t\neq F_t.
$$

It also contains information not completely represented by $NEW_t$. Two actions can produce the same number of new deliveries while the remaining attempts differ between successful-but-redundant deliveries and unsuccessful deliveries.

This distinction is relevant to Q-AHBN2 because the learning layer operates under dynamic conditions including failures, churn, overload, and heterogeneity. Nevertheless, an individual failure may arise from network dynamics that the selected action could not predict or prevent. How strongly such an outcome should influence reward is therefore a later reward-construction question and is not decided by admissibility.

Accordingly:

$$
\boxed{\text{02.6.2.3 }FAILED=\text{ INCLUDE / ADMISSIBLE / FROZEN}}
$$

This decision freezes **component admissibility only**. It deliberately does not assert

$$
FAILED_t\rightarrow -R_t.
$$

Therefore:

$$
\boxed{
\text{sign, normalization, weight, coefficient, and reward equation remain BLOCKED}
}
$$

The next controlled component decision is **02.6.2.4 — forwarding effort $F_t$**.

---

#### 02.6.2.4 Forwarding effort $F_t$ — INCLUDE / ADMISSIBLE — FROZEN

The frozen event semantics define $F_t$ as the number of direct forwarding attempts initiated by the selected action:

$$
F_t=NEW_t+DUPLICATE_t+FAILED_t.
$$

$F_t$ is scientifically admissible as a local forwarding-effort signal:

$$
\boxed{
F_t=
\text{admissible local evidence of forwarding effort initiated by }a_t
}
$$

Its semantic role is different from the terminal outcome categories. $NEW_t$, $DUPLICATE_t$, and $FAILED_t$ describe what happened to initiated attempts, whereas $F_t$ describes how much direct forwarding effort the action initiated.

However, $F_t$ is algebraically determined by the three terminal outcome counts and therefore does not provide an independent outcome count once those components are known. This creates an explicit reward-construction constraint:

$$
\boxed{
F_t=NEW_t+DUPLICATE_t+FAILED_t
\Rightarrow
\text{later reward construction MUST check for double counting}
}
$$

Accordingly:

$$
\boxed{\text{02.6.2.4 }F=\text{ INCLUDE / ADMISSIBLE / FROZEN}}
$$

This freezes **component admissibility only**. It does not assert that $F_t$ must appear in the final reward equation, nor does it assert

$$
F_t\rightarrow -R_t.
$$

Sign, normalization, weight, coefficient, and the reward equation remain **BLOCKED**.

The next controlled step is **02.6.2.5 — Component Decision Matrix**.

---

#### 02.6.2.5 Component Decision Matrix — PASS / FROZEN

The four component-admissibility decisions are consolidated below. This matrix freezes admissibility and dependency only.

| Component | Frozen semantic meaning | Admissibility | Dependency / constraint |
|---|---|---|---|
| $NEW_t$ | New/previously unseen successful dissemination outcomes attributable to $a_t$ within the frozen attribution boundary | **INCLUDE / ADMISSIBLE** | Terminal outcome component; obeys the frozen action-attribution and closure semantics |
| $DUPLICATE_t$ | Duplicate dissemination outcomes attributable to $a_t$ within the frozen attribution boundary | **INCLUDE / ADMISSIBLE** | Terminal outcome component; distinct from $NEW_t$ |
| $FAILED_t$ | Initiated forwarding attempts attributable to $a_t$ that did not successfully deliver | **INCLUDE / ADMISSIBLE** | Terminal outcome component; admissibility does not imply a negative reward contribution |
| $F_t$ | Local evidence of forwarding effort initiated by $a_t$ | **INCLUDE / ADMISSIBLE** | Algebraically dependent on the three terminal outcomes; later reward construction MUST check for double counting |

The explicit dependency constraint remains:

$$
\boxed{
F_t=NEW_t+DUPLICATE_t+FAILED_t
}
$$

Therefore, the four admissible components are not four independent signals. $NEW_t$, $DUPLICATE_t$, and $FAILED_t$ classify the terminal outcomes of initiated forwarding attempts, while $F_t$ is their aggregate forwarding-effort quantity.

The admissible candidate set is:

$$
\boxed{
\mathcal{C}_R=\{NEW_t,\;DUPLICATE_t,\;FAILED_t,\;F_t\}
}
$$

with the governing interpretation:

$$
\boxed{
\text{ADMISSIBLE}\neq\text{necessarily an independent additive reward term}
}
$$

In particular, admissibility of $F_t$ does not authorize treating all four quantities as independent additive terms. Any later reward construction MUST explicitly account for the identity $F_t=NEW_t+DUPLICATE_t+FAILED_t$ and prevent unintended double counting.

This freeze assigns **no signs, normalization, weights, coefficients, thresholds, bonuses, penalties, aggregation form, or reward equation**.

Accordingly:

$$
\boxed{
\textbf{02.6.2.5 Component Decision Matrix = PASS / FROZEN}
}
$$

with **four admissible components and one explicit dependency constraint**, and **no reward mathematics beyond the already established semantic identity for $F_t$**.

Therefore:

$$
\boxed{
\textbf{02.6.2 Reward Component Selection = PASS / FROZEN}
}
$$

The next and only controlled step is **02.6.3**. No sign, normalization, weight, coefficient, aggregation form, or reward equation is pre-authorized by closing 02.6.2.


---

### 02.6.3 Reward Component Direction — PASS / FROZEN

This stage freezes only the qualitative reward direction of the four components already admitted in 02.6.2. It assigns no numerical magnitude and does not construct the reward equation.

#### 02.6.3.1 Direction of $NEW_t$ — POSITIVE / FROZEN

$NEW_t$ is local, action-attributable evidence of successful coverage expansion. Therefore:

$$
\boxed{
NEW_t \uparrow
\Rightarrow
\text{directionally more favorable reward evidence}
}
$$

Accordingly:

$$
\boxed{
\textbf{02.6.3.1 }NEW_t=\textbf{ POSITIVE / FROZEN}
}
$$

This direction does not make $NEW_t$ equivalent to experiment-level delivery ratio and assigns no magnitude, normalization, weight, coefficient, or reward term.

#### 02.6.3.2 Direction of $DUPLICATE_t$ — NEGATIVE / FROZEN

$DUPLICATE_t$ is local evidence of successful but redundant dissemination. Therefore:

$$
\boxed{
DUPLICATE_t \uparrow
\Rightarrow
\text{directionally less favorable reward evidence}
}
$$

Accordingly:

$$
\boxed{
\textbf{02.6.3.2 }DUPLICATE_t=\textbf{ NEGATIVE / FROZEN}
}
$$

A lower duplicate count does not by itself establish a better action, because forwarding collapse could also reduce duplicates.

#### 02.6.3.3 Direction of $FAILED_t$ — NEGATIVE / FROZEN

$FAILED_t$ is local evidence that an initiated direct forwarding attempt did not successfully deliver. Therefore:

$$
\boxed{
FAILED_t \uparrow
\Rightarrow
\text{directionally less favorable reward evidence}
}
$$

Accordingly:

$$
\boxed{
\textbf{02.6.3.3 }FAILED_t=\textbf{ NEGATIVE / FROZEN}
}
$$

This direction does not assert that the selected action caused the underlying network failure and does not determine the relative severity of a failure.

#### 02.6.3.4 Direction of forwarding effort $F_t$ — NEUTRAL / NON-DIRECT / FROZEN

The frozen identity is:

$$
F_t=NEW_t+DUPLICATE_t+FAILED_t.
$$

$F_t$ measures the total direct forwarding effort initiated, but its magnitude alone does not establish whether that effort was useful, redundant, or unsuccessful. Therefore neither an unconditional positive nor an unconditional negative direction is justified:

$$
\boxed{
F_t \uparrow
\not\Rightarrow
\text{intrinsically more favorable or less favorable reward evidence}
}
$$

Accordingly:

$$
\boxed{
\textbf{02.6.3.4 } F_t = \textbf{NEUTRAL / NON-DIRECT / FROZEN}
}
$$

This does not exclude $F_t$ from later reward construction. It remains admissible evidence, but it has no unconditional direct reward direction. Any later mathematical use of $F_t$ must also respect its algebraic dependency on the three terminal outcome counts and prevent unintended double counting.

#### 02.6.3.5 Reward Component Direction Decision Matrix — PASS / FROZEN

The four individually frozen direction decisions are consolidated below.

| Component | Frozen semantic role | Admissibility | Direction | Directional interpretation |
|---|---|---|---|---|
| $NEW_t$ | New/previously unseen successful dissemination attributable to $a_t$ | **INCLUDE / ADMISSIBLE** | **POSITIVE** | More $NEW_t$ is directionally more favorable because it expands coverage |
| $DUPLICATE_t$ | Successful but redundant dissemination attributable to $a_t$ | **INCLUDE / ADMISSIBLE** | **NEGATIVE** | More $DUPLICATE_t$ is directionally less favorable because it represents redundancy |
| $FAILED_t$ | Initiated forwarding attempt attributable to $a_t$ that did not successfully deliver | **INCLUDE / ADMISSIBLE** | **NEGATIVE** | More $FAILED_t$ is directionally less favorable because initiated effort produced no successful delivery |
| $F_t$ | Total direct forwarding attempts initiated by $a_t$ | **INCLUDE / ADMISSIBLE** | **NEUTRAL / NON-DIRECT** | Forwarding volume alone does not establish whether dissemination was useful or wasteful |

The resulting directional structure is:

$$
\boxed{
NEW_t:+,\qquad
DUPLICATE_t:-,\qquad
FAILED_t:-,\qquad
F_t:\varnothing_{\mathrm{direct}}
}
$$

where $\varnothing_{\mathrm{direct}}$ means **no unconditional direct reward direction**, not exclusion from later reward construction.

The structural dependency remains authoritative:

$$
\boxed{
F_t=NEW_t+DUPLICATE_t+FAILED_t
}
$$

Therefore:

$$
\boxed{
\text{ADMISSIBLE}
\neq
\text{DIRECTLY SIGNED}
\neq
\text{INDEPENDENT ADDITIVE TERM}
}
$$

In particular, $F_t$ remains admissible but MUST NOT be treated casually as an independent fourth outcome with an additional signed contribution. Any later use must explicitly account for the frozen identity and avoid unintended double counting.

The qualitative directions frozen by 02.6.3 are:

$$
\boxed{
\begin{aligned}
\text{NEW}_t &:\ \textbf{POSITIVE}\\
\text{DUPLICATE}_t &:\ \textbf{NEGATIVE}\\
\text{FAILED}_t &:\ \textbf{NEGATIVE}\\
\text{F}_t &:\ \textbf{NEUTRAL / NON-DIRECT}
\end{aligned}
}
$$

Accordingly:

$$
\boxed{
\textbf{02.6.3.5 Reward Component Direction Decision Matrix = PASS / FROZEN}
}
$$

and:

$$
\boxed{
\textbf{02.6.3 Reward Component Direction = PASS / FROZEN}
}
$$

This freeze assigns **no normalization, transformation, magnitude, relative severity, weight, coefficient, threshold, bonus, penalty magnitude, aggregation form, or final reward equation**.

Those remain:

$$
\boxed{\textbf{BLOCKED}}
$$

Accordingly, **02.6.3 is complete**. The next stage must begin by deciding how these differently structured raw counts can be represented comparably before any weights or final $R_t$ are introduced.


---

### 02.6.4 Reward Component Representation — PASS / FROZEN

This stage freezes the representation needed to compare the three terminal forwarding outcomes before any reward weights, relative severities, aggregation coefficients, or final reward equation are introduced.

For reward-bearing actions with \(F_t>0\), the terminal outcome counts are represented as action-local outcome proportions:

$
\boxed{
\widehat{NEW}_t=\frac{NEW_t}{F_t},\qquad
\widehat{DUPLICATE}_t=\frac{DUPLICATE_t}{F_t},\qquad
\widehat{FAILED}_t=\frac{FAILED_t}{F_t}
}
$

Using the already-frozen identity

$
F_t=NEW_t+DUPLICATE_t+FAILED_t,
$

the represented outcome components satisfy

$
0\leq\widehat{NEW}_t,\widehat{DUPLICATE}_t,\widehat{FAILED}_t\leq1
$

and

$
\boxed{
\widehat{NEW}_t+\widehat{DUPLICATE}_t+\widehat{FAILED}_t=1
\qquad(F_t>0)
}
$

This converts the differently scaled raw terminal counts into comparable within-action outcome shares while preserving the directions frozen in 02.6.3:

$
\widehat{NEW}_t:\textbf{ POSITIVE},\qquad
\widehat{DUPLICATE}_t:\textbf{ NEGATIVE},\qquad
\widehat{FAILED}_t:\textbf{ NEGATIVE}.
$

#### 02.6.4.4 Representation of forwarding effort \(F_t\)

\(F_t\) remains **ADMISSIBLE** and **NEUTRAL / NON-DIRECT** evidence of the forwarding effort initiated by \(a_t\). Raw \(F_t\) is **not** accepted as a directly comparable fourth reward component alongside the three normalized outcome proportions.

The exact representation or normalization of forwarding effort, if it is later used mathematically, remains unresolved. In particular:

- no \(\widehat F_t\) definition is frozen;
- direct inclusion of effort in the final reward equation is not authorized;
- \(F_t=0\) handling remains unresolved and must be settled before a final reward equation is constructed;
- the identity \(F_t=NEW_t+DUPLICATE_t+FAILED_t\) remains authoritative.

#### 02.6.4.5 Reward Component Representation Decision Matrix — PASS / FROZEN

| Evidence | Frozen representation | Direction | Status / constraint |
|---|---|---|---|
| \(NEW_t\) | \(\widehat{NEW}_t=NEW_t/F_t\), for \(F_t>0\) | **POSITIVE** | Comparable terminal-outcome proportion |
| \(DUPLICATE_t\) | \(\widehat{DUPLICATE}_t=DUPLICATE_t/F_t\), for \(F_t>0\) | **NEGATIVE** | Comparable terminal-outcome proportion |
| \(FAILED_t\) | \(\widehat{FAILED}_t=FAILED_t/F_t\), for \(F_t>0\) | **NEGATIVE** | Comparable terminal-outcome proportion |
| \(F_t\) | Retained as forwarding-effort evidence; no final normalized representation frozen | **NEUTRAL / NON-DIRECT** | Raw \(F_t\) rejected as a directly comparable fourth outcome term; later use must avoid double counting |

Accordingly:

$
\boxed{\textbf{02.6.4.5 Reward Component Representation Decision Matrix = PASS / FROZEN}}
$

and:

$
\boxed{\textbf{02.6.4 Reward Component Representation = PASS / FROZEN}}
$

This freeze assigns **no reward weights, coefficient magnitudes, relative severities, tuning values, aggregation architecture, or final \(R_t\) equation**. Those remain:

$
\boxed{\textbf{BLOCKED}}
$

The next controlled stage is **02.6.5 Reward Component Aggregation Structure**. Only its first sub-decision is opened:

### 02.6.5.1 Component Dependency Audit — PASS / FROZEN

The dependency audit freezes one simple structural fact:

$
\boxed{
F_t=NEW_t+DUPLICATE_t+FAILED_t
}
$

\(NEW_t\), \(DUPLICATE_t\), and \(FAILED_t\) are the three terminal outcomes of the direct forwarding attempts attributable to action \(a_t\), whereas \(F_t\) is the total number of those forwarding attempts. Therefore \(F_t\) is dependent on the three terminal outcome counts and MUST NOT be treated as an independent fourth terminal outcome.

Under the 02.6.4 representation, for \(F_t>0\),

$
\boxed{
\widehat{NEW}_t+\widehat{DUPLICATE}_t+\widehat{FAILED}_t=1
}
$

so the represented terminal outcomes describe the composition of the same forwarding effort.

This distinction is consistent with RO2: the reward evidence must retain useful dissemination outcomes and redundant dissemination outcomes separately because RO2 established the dissemination trade-off between effectiveness/latency and duplication. Forwarding effort \(F_t\) describes how much forwarding was initiated; it does not constitute a separate dissemination outcome and MUST NOT obscure that RO2 trade-off by being treated as independent evidence.

Accordingly:

$
\boxed{
\begin{aligned}
NEW_t,\ DUPLICATE_t,\ FAILED_t
&=\text{three terminal outcomes of forwarding attempts},\\
F_t
&=\text{total number of those forwarding attempts},\\
F_t
&=NEW_t+DUPLICATE_t+FAILED_t.
\end{aligned}
}
$

The constraint carried forward is:

$
\boxed{
\textbf{Later reward construction MUST NOT treat all four quantities as independent evidence.}
}
$

This stage identifies the dependency only. It does **not** decide how \(F_t\) will be used or whether it will appear in the final reward equation.

$
\boxed{\textbf{02.6.5.1 Component Dependency Audit = PASS / FROZEN}}
$

No weight, coefficient, relative severity, aggregation architecture, or final reward equation is authorized.

### 02.6.5.2 Double-Counting Audit — PASS / FROZEN

The frozen dependency is:

$
\boxed{
F_t=NEW_t+DUPLICATE_t+FAILED_t
}
$

Therefore \(F_t\) MUST NOT be treated as an independent directly signed fourth outcome term when doing so would reward or penalize forwarding evidence already represented by \(NEW_t\), \(DUPLICATE_t\), and \(FAILED_t\).

$
\boxed{
\begin{aligned}
&F_t=NEW_t+DUPLICATE_t+FAILED_t;\\
&\text{therefore }F_t\text{ MUST NOT be treated as an independent}\\
&\text{directly signed fourth outcome term when doing so}\\
&\text{would reward or penalize forwarding evidence already}\\
&\text{represented by }NEW_t,DUPLICATE_t,FAILED_t.
\end{aligned}
}
$

The RO2 safeguard is:

$
\boxed{
\text{Reward construction must preserve the RO2 distinction between}
}
$

$
\boxed{
\text{productive dissemination effort}
\quad\text{and}\quad
\text{redundant/unsuccessful dissemination effort}.
}
$

This safeguard follows the RO2 trade-off evidence: dissemination effort can contribute to propagation effectiveness while also creating redundant forwarding. Forwarding volume alone therefore MUST NOT be interpreted as intrinsically favorable or unfavorable.

Importantly, this freeze **does not remove \(F_t\)**. It does not decide whether \(F_t\) will eventually serve as a modifier, efficiency reference, constraint, normalization quantity, or be absent from the final reward equation.

It also introduces **no weight, coefficient, relative severity, aggregation architecture, or reward equation**.

Accordingly:

$
\boxed{
\textbf{02.6.5.2 Double-Counting Audit = PASS / FROZEN}
}
$

### 02.6.5.3 Aggregation Architecture Decision — OPEN

> Given the dependency and double-counting constraints frozen in 02.6.5.1--02.6.5.2, what structural role, if any, should \(F_t\) have relative to the three represented outcome components?

No weight, coefficient, relative severity, tuning value, or final \(R_t\) equation is authorized.

#### 02.6.5.3A — \(F_t\) as an Independent Direct Reward Term — REJECT / FROZEN

\(F_t\) MUST NOT enter the reward as an independent directly signed fourth outcome term.

$
\boxed{\textbf{02.6.5.3A — Direct reward term = REJECT / FROZEN}}
$

The rejection applies **only to the direct-term role**. \(F_t\) remains admissible evidence. This follows from \(F_t=NEW_t+DUPLICATE_t+FAILED_t\), the 02.6.5.2 double-counting safeguard, and the RO2 requirement to preserve productive versus redundant/unsuccessful dissemination effort.

No decision is made here about normalization, modifier/reference, constraint/context, or no-final-reward roles.

#### 02.6.5.3B — \(F_t\) as Normalization Basis — OPEN

For \(F_t>0\), the candidate role is the already-frozen 02.6.4 representation:
$
\widehat{NEW}_t=\frac{NEW_t}{F_t},\quad
\widehat{DUPLICATE}_t=\frac{DUPLICATE_t}{F_t},\quad
\widehat{FAILED}_t=\frac{FAILED_t}{F_t}.
$

##### 02.6.5.3B.1(a) — Can \(F_t=0\) Occur? — YES / PASS / FROZEN

Requested fanout does not guarantee realized forwarding. If no eligible forwarding target exists, no direct forwarding attempt is initiated.

$
\boxed{|N_e|=0\Rightarrow F_t=0\Rightarrow NEW_t=DUPLICATE_t=FAILED_t=0}
$

No eligible forwarding target does **not** constitute a failed initiated transmission:
$
\boxed{F_t=0\not\Rightarrow FAILED_t>0}
$

$
\boxed{\textbf{02.6.5.3B.1(a) — Can }F_t=0\textbf{ occur? = YES / PASS / FROZEN}}
$

##### 02.6.5.3B.1(b) — Zero-Effort Representation Semantics — NO FORWARDING-OUTCOME EVIDENCE / PASS / FROZEN

When \(F_t=0\), no forwarding attempts were initiated; therefore no empirical forwarding-outcome distribution exists for that decision interval.

$
\boxed{F_t=0\Rightarrow\textbf{NO FORWARDING-OUTCOME EVIDENCE}}
$

Thus the three normalized outcomes have no empirical proportion for that interval. This does not imply \(FAILED_t>0\), \(R_t=0\), or that the Q-learning update is skipped. Those reward and learning decisions remain BLOCKED.

$
\boxed{\textbf{02.6.5.3B.1(b) Zero-Effort Representation Semantics}=\textbf{NO FORWARDING-OUTCOME EVIDENCE / PASS / FROZEN}}
$

##### 02.6.5.3B.1(c) — Computational Encoding — CONDITIONAL REPRESENTATION / PASS / FROZEN

$
\boxed{
\mathcal{O}_t=
\begin{cases}
\left(\dfrac{NEW_t}{F_t},\dfrac{DUPLICATE_t}{F_t},\dfrac{FAILED_t}{F_t}\right),&F_t>0,\\[8pt]
\text{NO\_FORWARDING\_EVIDENCE},&F_t=0.
\end{cases}}
$

NO_FORWARDING_EVIDENCE is an **implementation condition**, not a numerical reward value, state variable, additional reward component, or fourth outcome.

$
\boxed{
\begin{aligned}
&\text{No artificial }0/0=0;\\
&\text{no new scientific signal or reward component};\\
&\text{no reward value assigned for }F_t=0;\\
&\text{no Q-update behaviour decided here.}
\end{aligned}}
$

$
\boxed{\textbf{02.6.5.3B.1(c) Computational Encoding}=\textbf{CONDITIONAL REPRESENTATION / PASS / FROZEN}}
$

The zero-effort boundary and computational representation have now been resolved. Together with 02.6.4 and the 02.6.5.1--02.6.5.2 safeguards, these results are sufficient to close the normalization-basis role.

> **02.6.5.3B — \(F_t\) as Normalization Basis = ACCEPT / FROZEN**

The accepted role is strictly:

$
F_t > 0
\quad\Rightarrow\quad
\left(
\widehat{NEW}_t,\,
\widehat{DUPLICATE}_t,\,
\widehat{FAILED}_t
\right)
=
\left(
\frac{NEW_t}{F_t},\,
\frac{DUPLICATE_t}{F_t},\,
\frac{FAILED_t}{F_t}
\right)
$

and:

$
F_t = 0
\quad\Rightarrow\quad
\mathrm{NO\_FORWARDING\_EVIDENCE}
$

Acceptance as a normalization basis does **not** authorize \(F_t\) as a direct reward or penalty. No weight, coefficient, relative severity, reward for \(F_t=0\), Q-update behaviour, or final reward equation is introduced.

#### 02.6.5.3C — Additional Modifier / Reference Role — COMPLETE / FROZEN

##### 02.6.5.3C.1 — Information Necessity Audit — PASS / FROZEN

Normalization preserves forwarding-outcome quality but removes absolute realized forwarding-effort magnitude. Therefore \(F_t\) carries information that is lost when only the normalized outcome proportions are retained.

That absolute-effort information is relevant to the RO2 dissemination-efficiency trade-off. However, relevance alone does **not** establish that \(F_t\) must alter reward magnitude.

$
\boxed{
\begin{aligned}
&\text{Normalization by }F_t\text{ removes absolute forwarding-effort magnitude;}\\
&\text{absolute effort is relevant to the RO2 dissemination-efficiency trade-off;}\\
&\text{however, relevance alone does not establish the necessity of}\\
&\text{an additional }F_t\text{-based reward modifier.}
\end{aligned}}
$

$
\boxed{\textbf{02.6.5.3C.1 Information Necessity Audit = RELEVANT BUT ADDITIONAL REWARD ROLE NOT YET JUSTIFIED / PASS / FROZEN}}
$

##### 02.6.5.3C.2 — Information Coverage Audit — PASS / FROZEN

The selected action \(a_t\) represents forwarding intent, while the normalized \(NEW_t\), \(DUPLICATE_t\), and \(FAILED_t\) outcomes represent forwarding-outcome quality. Neither fully preserves the absolute number of forwarding attempts actually realized.

Accordingly, \(F_t\) contains distinct realized-effort information that is not fully represented elsewhere in the frozen action/outcome structure.

$
\boxed{
\begin{aligned}
&\text{action }a_t:\ \text{forwarding intent};\\
&(\widehat{NEW}_t,\widehat{DUPLICATE}_t,\widehat{FAILED}_t):\ \text{forwarding-outcome quality};\\
&F_t:\ \text{absolute realized forwarding effort}.
\end{aligned}}
$

$
\boxed{\textbf{02.6.5.3C.2 Information Coverage Audit = DISTINCT INFORMATION REMAINS / PASS / FROZEN}}
$

This finding does **not** authorize \(F_t\) as a reward term or modifier.

##### 02.6.5.3C.3 — Reference-vs-Modifier Necessity — PASS / FROZEN

The distinct absolute realized-effort information in \(F_t\) can be retained as contextual/reference evidence without requiring \(F_t\) to alter reward magnitude.

$
\boxed{
\begin{aligned}
&F_t\text{ contains distinct absolute realized-effort information;}\\
&\text{that information SHOULD be retained as contextual/reference evidence;}\\
&\text{retaining it does not require }F_t\text{ to modify reward magnitude;}\\
&\text{no scientific necessity for an additional reward-modifying role}\\
&\text{has been established.}
\end{aligned}}
$

$
\boxed{\textbf{02.6.5.3C.3 Reference-vs-Modifier Necessity = REFERENCE SUFFICIENT; MODIFIER NOT JUSTIFIED / PASS / FROZEN}}
$

Therefore the overall C role is frozen as:

$
\boxed{\textbf{02.6.5.3C — Modifier/Reference Role = REFERENCE ACCEPTED; REWARD MODIFIER REJECTED / FROZEN}}
$

$
\boxed{\textbf{02.6.5.3C = COMPLETE / FROZEN}}
$

The resulting role boundary is:

$
\boxed{
F_t:
\begin{cases}
\text{contextual/reference evidence} & \textbf{ACCEPT},\\
\text{reward-magnitude modifier} & \textbf{REJECT}.
\end{cases}}
$

Together with the earlier freezes, \(F_t\) is accepted as a normalization basis and as realized-effort reference/context, while it is rejected as an independent direct reward term and as a reward-magnitude modifier.

No weight, coefficient, threshold, modifier function, relative severity, reward equation, or Q-update behaviour is authorized by this C freeze.

The next controlled action is **not** to accept or reject candidate D automatically. First determine whether **D — constraint/context only** defines any scientifically distinct role for \(F_t\) that has not already been resolved by the frozen A--C decisions.

#### 02.6.5.3D — Constraint / Context Only — REDUNDANT / NO ADDITIONAL ROLE / FROZEN

The frozen C decision already retains \(F_t\) as realized-effort reference/context. The role-redundancy audit found no scientifically distinct additional context function for candidate D, and no separate \(F_t\)-based threshold, cap, gating condition, or other constraint mechanism has been shown necessary.

> **02.6.5.3D.1 Role Redundancy Audit = NO DISTINCT ROLE / PASS / FROZEN**

Accordingly:

> **02.6.5.3D — Constraint/Context Only = REDUNDANT / NO ADDITIONAL ROLE / FROZEN**

> **02.6.5.3D = COMPLETE / FROZEN**

This closure does not discard \(F_t\) and introduces no new constraint mechanism.

#### 02.6.5.3E — No Final Reward Role — SUPERSEDED BY A--D / NO SEPARATE ROLE / FROZEN

Complete exclusion of \(F_t\) is incompatible with the frozen normalization-basis and reference/context roles. Conversely, the interpretation that \(F_t\) should not independently alter reward magnitude is already resolved by A and C.

> **02.6.5.3E.1 Alternative Viability Audit = NO INDEPENDENT ALTERNATIVE REMAINS / PASS / FROZEN**

Accordingly:

> **02.6.5.3E — No Final Reward Role = SUPERSEDED BY A--D / NO SEPARATE ROLE / FROZEN**

> **02.6.5.3E = COMPLETE / FROZEN**

#### 02.6.5.3 Overall Closure — PASS / COMPLETE / FROZEN

All candidate structural roles for \(F_t\) have now been resolved.

$
\begin{aligned}
F_t &: \text{normalization basis} && \textbf{ACCEPTED},\\
F_t &: \text{realized-effort reference/context} && \textbf{ACCEPTED},\\
F_t &: \text{independent direct reward term} && \textbf{REJECTED},\\
F_t &: \text{reward-magnitude modifier} && \textbf{REJECTED},\\
F_t &: \text{additional constraint mechanism} && \textbf{NO ADDITIONAL ROLE}.
\end{aligned}
$

The conditional representation remains:

$
\mathcal O_t=
\begin{cases}
\left(
\dfrac{NEW_t}{F_t},
\dfrac{DUPLICATE_t}{F_t},
\dfrac{FAILED_t}{F_t}
\right), & F_t>0,\\[6pt]
\mathrm{NO\_FORWARDING\_EVIDENCE}, & F_t=0.
\end{cases}
$

> **02.6.5.3 Aggregation Architecture Decision = PASS / COMPLETE / FROZEN**

#### 02.6.5 Parent Closure — PASS / COMPLETE / FROZEN

Completion of the dependency audit, double-counting audit, and aggregation-architecture decision is sufficient to close the parent stage.

The frozen structural contract is:

$
\begin{aligned}
&F_t=NEW_t+DUPLICATE_t+FAILED_t;\\
&F_t\text{ is dependent, not a fourth independent outcome;}\\
&F_t\text{ normalizes the three forwarding outcomes when }F_t>0;\\
&F_t\text{ remains available as realized-effort reference/context;}\\
&F_t\text{ does not independently alter reward magnitude;}\\
&F_t=0\Rightarrow\mathrm{NO\_FORWARDING\_EVIDENCE}.
\end{aligned}
$

> **02.6.5 — Reward Component Aggregation Structure = PASS / COMPLETE / FROZEN**

Weights, coefficients, relative severity, thresholds, bonuses, penalties, executable reward mathematics, and final \(R_t\) remain **BLOCKED**. No 02.6.5.4 is required.

The next stage is **not inferred from numbering**. The existing 02.6 roadmap/current-gate plan must be inspected to determine the minimum already-planned post-02.6.5 decision before any hypothetical 02.6.6 design stage is opened.

---

### 02.6.6 Reward Magnitude and Zero-Evidence Handling — IN PROGRESS

This gate resolves only the minimum reward-magnitude and zero-forwarding-evidence decisions required after the frozen 02.6.5 aggregation architecture. It does **not** freeze the final executable \(R_t\).

#### 02.6.6.1 Equal-vs-Differentiated Magnitude Principle — PASS / FROZEN

RO2 establishes that productive (`NEW`), redundant (`DUPLICATE`), and unsuccessful (`FAILED`) forwarding have different operational meanings, but it does not establish a quantitative or ordinal relative severity suitable for unequal reward weighting. Therefore, equal initial absolute magnitude is adopted as the minimum-assumption choice rather than introducing unsupported relative weighting.

At the relative-magnitude level only:

$$
\boxed{
NEW:+1,\qquad DUPLICATE:-1,\qquad FAILED:-1
}
$$

These are **relative units**, not yet an executable final reward equation. Equal magnitude does not mean that the three outcomes are semantically or operationally equivalent.

$$
\boxed{\textbf{02.6.6.1 Equal-vs-Differentiated Magnitude Principle = EQUAL INITIAL ABSOLUTE MAGNITUDE / PASS / FROZEN}}
$$

#### 02.6.6.2 Common Reward Scale — PASS / FROZEN

The outcome components are already normalized for \(F_t>0\), and 02.6.6.1 freezes equal initial absolute magnitude. No scientific requirement justifies introducing an additional common multiplier. Unit scale is therefore retained as the minimum-assumption choice and no extra tuning parameter is introduced.

$$
\boxed{
\textbf{02.6.6.2 Common Reward Scale}
=
\textbf{UNIT SCALE / NO ADDITIONAL SCALING / PASS / FROZEN}
}
$$

This is not a claim that a coefficient of one has been empirically optimized; it means that no additional common reward-scaling parameter is introduced.

#### 02.6.6.3 \(F_t=0\) / NO_FORWARDING_EVIDENCE Handling — PASS / FROZEN

The frozen 02.6.5 semantics establish:

$$
F_t=0
\Rightarrow
NEW_t=DUPLICATE_t=FAILED_t=0
\Rightarrow
\mathrm{NO\_FORWARDING\_EVIDENCE}.
$$

No forwarding outcome exists from which the selected action can be evaluated. Absence of evidence is not equivalent to observing a neutral reward:

$$
\boxed{\text{NO EVIDENCE}\neq\text{ZERO REWARD}}
$$

Therefore:

$$
\boxed{
\begin{aligned}
F_t=0
&\Rightarrow \texttt{NO\_FORWARDING\_EVIDENCE}\\
&\Rightarrow \textbf{NO REWARD VALUE ASSIGNED}\\
&\Rightarrow \textbf{NO REWARD-BEARING Q-UPDATE}.
\end{aligned}}
$$

Accordingly:

$$
\boxed{
\textbf{02.6.6.3}
=
\textbf{SKIP REWARD-BEARING Q-UPDATE WHEN }F_t=0
\ /\ \textbf{PASS / FROZEN}
}
$$

This introduces no synthetic `FAILED`, artificial \(0/0=0\) convention, special bonus, penalty, coefficient, or additional reward component. Q-AHBN2 neither rewards nor penalizes an action when no forwarding-outcome evidence exists.

The final \(R_t\) remains **NOT FROZEN**.

#### 02.6.6.4 Reward Bounds / Range and Numerical Safety — PASS / FROZEN

For every reward-bearing interval, \(F_t>0\), the frozen normalized forwarding outcomes satisfy:

$
\widehat{NEW}_t+\widehat{DUPLICATE}_t+\widehat{FAILED}_t=1,
\qquad
0\leq\widehat{NEW}_t,\widehat{DUPLICATE}_t,\widehat{FAILED}_t\leq1.
$

Together with the frozen equal initial absolute magnitude and unit scale, the signed reward structure is intrinsically bounded:

$
\boxed{-1\leq R_t\leq+1\qquad(F_t>0)}
$

Accordingly:

$
\boxed{
\textbf{NATURAL RANGE }[-1,+1]
\ /\
\textbf{NO ADDITIONAL REWARD CLIPPING}
}
$

The range requirement is an **implementation invariant/assertion to verify**, not a clipping transformation:

$
\boxed{
F_t>0\Rightarrow -1\leq R_t\leq1
}
$

If an implementation produces a reward outside this range, it MUST be treated as an implementation/semantic error rather than silently clipped. The already-frozen \(F_t=0\) case remains outside the reward-bearing range because it produces no reward value and no reward-bearing Q-update.

$
\boxed{
\textbf{02.6.6.4 Reward Bounds / Numerical Safety}
=
\textbf{NATURAL RANGE }[-1,+1]
\ /\
\textbf{NO ADDITIONAL REWARD CLIPPING}
\ /\
\textbf{PASS / FROZEN}
}
$

This freeze does **not** start the deterministic micro-case suite and does **not** freeze the final executable \(R_t\). The next unresolved controlled area is the deterministic micro-case validation.



---

### 02.6.7 Deterministic Micro-Case Validation — IN PROGRESS

This gate validates consequences of the already-frozen 02.6.1--02.6.6 reward decisions using deterministic known-answer cases. It introduces no new reward signal, direction, weight, coefficient, threshold, bonus, penalty, clipping rule, or final executable reward equation.

#### 02.6.7.1 All-NEW Micro-Case — PASS / FROZEN
NEW=1, DUPLICATE=0, FAILED=0, F=1. Expected: R=+1. This verifies the positive boundary.

#### 02.6.7.2 All-DUPLICATE Micro-Case — PASS / FROZEN
NEW=0, DUPLICATE=1, FAILED=0, F=1. Expected: R=-1. This verifies the negative boundary for a fully redundant outcome. DUPLICATE and FAILED remain operationally distinct despite equal initial absolute reward magnitude.

#### 02.6.7.3 All-FAILED Micro-Case — PASS / FROZEN
NEW=0, DUPLICATE=0, FAILED=1, F=1. Expected: R=-1.

The distinction remains: F=0 means no forwarding evidence and no reward-bearing Q-update; FAILED=1 means forwarding was attempted and failed, providing negative evidence.

#### 02.6.7.4 Balanced NEW/DUPLICATE Micro-Case — PASS / FROZEN
NEW=1, DUPLICATE=1, FAILED=0, F=2. Expected: R=0.

This preserves ZERO REWARD != NO REWARD: F>0 with R=0 means observed positive and negative evidence balance; F=0 means no forwarding-outcome evidence.

#### 02.6.7.5 Balanced NEW/FAILED Micro-Case — PASS / FROZEN
NEW=1, DUPLICATE=0, FAILED=1, F=2. Expected: R=0. This separately verifies mixed NEW and FAILED handling.

#### 02.6.7.6 Three-Outcome Mixed Micro-Case — PASS / FROZEN
NEW=2, DUPLICATE=1, FAILED=1, F=4. Normalized proportions are 0.50, 0.25, 0.25. Expected: R=0. This verifies common F normalization and aggregation without double-counting F.


#### 02.6.7.7 Interior Non-Zero Mixed Outcome — PASS / FROZEN
A deterministic mixed case produces an interior non-zero reward of \(R_t=+0.50\). This confirms proportional reward behavior away from the pure boundaries and exact-balance cases without introducing a new coefficient or scaling rule.

#### 02.6.7.8 Zero-Forwarding-Evidence Execution Case — PASS / FROZEN
For \(F_t=0\), `NEW=DUPLICATE=FAILED=0`. The frozen execution semantics apply: `NO_FORWARDING_EVIDENCE`, no numerical reward value, and no reward-bearing Q-update. This preserves the distinction between a valid zero reward with evidence and absence of a reward-bearing event.

#### 02.6.7.9 Proportional-Scaling Invariance Case — PASS / FROZEN
Two attribution sets with the same normalized outcome proportions but different absolute \(F_t>0\) produce the same reward, \(R_t=+0.50\). This confirms that \(F_t\) is a normalization basis and realized-effort reference, not a reward-magnitude modifier.

#### 02.6.7.10 Micro-Case Suite Closure Audit — PASS / COMPLETE / FROZEN
The complete deterministic suite 02.6.7.1--02.6.7.9 was reconciled against all reward decisions frozen in 02.6.1--02.6.6.

The closure audit confirms:
- all admitted outcome classes are exercised;
- `NEW` remains positive, `DUPLICATE` negative, and `FAILED` negative;
- \(F_t=NEW_t+DUPLICATE_t+FAILED_t\) remains a dependency/normalization identity rather than a fourth independent reward term;
- normalized outcome representation is preserved for every reward-bearing case;
- equal initial absolute magnitude and unit scale remain sufficient;
- `ZERO REWARD != NO REWARD`;
- every numerical reward lies naturally in \([-1,+1]\);
- no clipping, extra coefficient, multiplier, bonus, penalty, threshold, or corrective term is required;
- no deterministic case double-counts \(F_t\);
- proportional scaling of absolute forwarding effort does not alter reward magnitude when outcome proportions are unchanged;
- no inconsistency requiring an additional micro-case category was found.

**02.6.7.10 MICRO-CASE SUITE CLOSURE AUDIT: PASS / COMPLETE / FROZEN.**

**02.6.7 DETERMINISTIC MICRO-CASE VALIDATION: PASS / COMPLETE / FROZEN.**

This closure does not yet freeze the final executable \(R_t\). The next documented task is final executable reward-contract reconciliation, followed by the 02.6 closure audit. No `02.6.7.11` is planned or authorized unless a validity-critical inconsistency is discovered and recorded through change control.

---



### 02.6.8A Final Executable Reward-Contract Reconciliation — PASS / COMPLETE / FROZEN

**Work-package classification:** L1 bounded reconciliation under the delegated scientific execution protocol. No new scientific assumption or reward preference is introduced.

#### Authoritative inputs checked

The reconciliation was performed against:

- `docs/00_SOURCE_AUTHORITY_REGISTER.md`, including the retained objective of balancing dissemination effectiveness with overhead and the rule that historical reward equations/coefficients are redesign evidence rather than authority;
- `docs/01_CANONICAL_AHBN_CONTRACT.md`, which keeps canonical AHBN immutable and defines no Q-learning reward;
- frozen Sections 02.6.1--02.6.7 of this document;
- the RO2 dissemination trade-off authority registered as Source 3A, which requires productive dissemination to remain distinguishable from redundant/unsuccessful forwarding evidence.

#### Executable derivation

For every reward-bearing decision interval, \(F_t>0\) and:

$$
F_t=NEW_t+DUPLICATE_t+FAILED_t.
$$

The frozen representation is:

$$
\hat N_t=\frac{NEW_t}{F_t},\qquad
\hat D_t=\frac{DUPLICATE_t}{F_t},\qquad
\hat X_t=\frac{FAILED_t}{F_t},
$$

with:

$$
\hat N_t+\hat D_t+\hat X_t=1.
$$

The frozen directions and equal unit magnitudes are:

$$
NEW:+1,\qquad DUPLICATE:-1,\qquad FAILED:-1.
$$

Therefore the direct linear aggregation implied by the frozen contract is:

$$
\boxed{
R_t=
\frac{NEW_t-DUPLICATE_t-FAILED_t}{F_t}
}
\qquad \text{for }F_t>0.
$$

Equivalently:

$$
R_t=
\frac{NEW_t}{F_t}
-
\frac{DUPLICATE_t}{F_t}
-
\frac{FAILED_t}{F_t}.
$$

The algebraic simplification \(R_t=2(NEW_t/F_t)-1\) is valid when \(F_t>0\), but it is **not** the preferred scientific/implementation representation because the explicit form preserves the operational distinction between redundant DUPLICATE and unsuccessful FAILED forwarding evidence.

For \(F_t=0\):

```text
NO_FORWARDING_EVIDENCE
→ no numerical R_t
→ no reward-bearing Q-update
```

No artificial numerical reward is assigned.

#### Reconciliation checks

| Check | Result |
|---|---|
| locally attributable evidence only | PASS |
| canonical AHBN changed | NO |
| new reward signal introduced | NO |
| new coefficient/weight introduced | NO |
| \(F_t\) used as independent fourth reward term | NO |
| \(F_t\) modifies reward magnitude independently | NO |
| duplicate/failed negative evidence preserved | PASS |
| RO2 productive-vs-overhead distinction preserved | PASS |
| natural reward range | \([-1,+1]\) / PASS |
| additional clipping required | NO |
| \(F_t=0\) semantics preserved | PASS |
| 02.6.7 deterministic suite preserved | PASS |
| contradiction with frozen 02.6 decisions | NONE FOUND |

Because \(\hat N_t,\hat D_t,\hat X_t\ge0\) and sum to one, the executable reward is a signed convex combination of \(+1,-1,-1\), hence:

$$
-1\le R_t\le +1.
$$

No clipping is mathematically required under valid inputs.

**02.6.8A FINAL EXECUTABLE REWARD-CONTRACT RECONCILIATION: PASS / COMPLETE / FROZEN.**

---

### 02.6.8B Final 02.6 Closure Audit — PASS / COMPLETE / FROZEN

The complete reward-construction contract was reconciled end-to-end.

| Closure criterion | Result |
|---|---|
| 02.6.1 event semantics and attribution | PASS |
| 02.6.2 component admissibility | PASS |
| 02.6.3 component directions | PASS |
| 02.6.4 normalized representation | PASS |
| 02.6.5 dependency / no double counting / aggregation architecture | PASS |
| 02.6.6 equal unit magnitude / zero evidence / natural range | PASS |
| 02.6.7 deterministic validation suite | PASS |
| final executable formula consistent with all frozen decisions | PASS |
| zero reward distinguished from no reward | PASS |
| canonical AHBN remains immutable | PASS |
| source-authority register contradicted | NO |
| RO2 trade-off contradicted | NO |
| hidden reward parameter introduced | NO |
| unstated implementation choice required for reward calculation | NO |
| unresolved validity-critical reward issue | NONE FOUND |

No additional gate is scientifically required to make the reward contract executable and reproducible.

The frozen executable contract is:

$$
\boxed{
R_t=
\frac{NEW_t-DUPLICATE_t-FAILED_t}{F_t},
\qquad F_t>0
}
$$

and:

$$
\boxed{
F_t=0
\Rightarrow
\mathrm{NO\_FORWARDING\_EVIDENCE}
\Rightarrow
\text{no numerical }R_t
\Rightarrow
\text{no reward-bearing Q-update}
}
$$

with:

$$
\boxed{-1\le R_t\le+1}
$$

for every reward-bearing interval.

**02.6 REWARD CONSTRUCTION: PASS / COMPLETE / FROZEN.**

This freeze defines the reward contract only. It does not modify canonical AHBN, does not select learning hyperparameters, and does not authorize post-hoc reward tuning based on experimental performance.

---

### 02.6.8 Current Gate and Progress Checklist

This subsection is the operational master list for the current `02.6 Reward Construction` stage. It summarizes the authoritative frozen decisions above and is updated whenever a gate closes. It does **not** replace or modify their scientific content.

> **Current position:** `02.6 Reward Construction = PASS / COMPLETE / FROZEN`. The executable reward contract is frozen and the 02.6 closure audit has passed.

#### 02.6.8.1 Master completion contract

| Gate / task | Purpose | Status |
|---|---|---|
| 02.6.1 | Reward event semantics and attribution lifecycle | **PASS / FROZEN** |
| 02.6.2 | Reward component selection | **PASS / FROZEN** |
| 02.6.3 | Reward component direction | **PASS / FROZEN** |
| 02.6.4 | Reward component representation | **PASS / FROZEN** |
| 02.6.5 | Aggregation architecture and double-counting control | **PASS / COMPLETE / FROZEN** |
| 02.6.6 | Relative magnitude, unit scale, zero-evidence handling, natural range | **PASS / COMPLETE / FROZEN** |
| 02.6.7.1--02.6.7.6 | Boundary and balanced/mixed deterministic cases | **PASS / FROZEN** |
| 02.6.7.7 | Interior non-zero mixed outcome | **PASS / FROZEN** |
| 02.6.7.8 | Zero-forwarding-evidence execution | **PASS / FROZEN** |
| 02.6.7.9 | Proportional-scaling invariance | **PASS / FROZEN** |
| 02.6.7.10 | Micro-case suite closure audit | **PASS / COMPLETE / FROZEN** |
| 02.6.7 | Deterministic micro-case validation | **PASS / COMPLETE / FROZEN** |
| **02.6.8A** | **Final executable reward-contract reconciliation** | **PASS / COMPLETE / FROZEN** |
| **02.6.8B** | **02.6 closure audit** | **PASS / COMPLETE / FROZEN** |
| **02.6 overall** | **Reward Construction** | **PASS / COMPLETE / FROZEN** |

The labels `02.6.8A` and `02.6.8B` are operational checklist identifiers for the two already-documented remaining tasks; they do not create new scientific requirements.

#### 02.6.8.2 Frozen reward constraints entering final reconciliation

The final executable reward contract MUST reconcile, without reopening, the following frozen constraints:

1. reward evidence is locally attributable to the acting decision interval;
2. \(F_t=NEW_t+DUPLICATE_t+FAILED_t\);
3. for \(F_t>0\), forwarding outcomes are represented as \(NEW_t/F_t\), \(DUPLICATE_t/F_t\), and \(FAILED_t/F_t\);
4. `NEW` is positive; `DUPLICATE` and `FAILED` are negative;
5. the initial absolute magnitudes are equal and use unit scale;
6. \(F_t\) is neutral/non-direct, is accepted as normalization basis and realized-effort reference/context, and is not an independent reward term or reward-magnitude modifier;
7. \(F_t=0\) means `NO_FORWARDING_EVIDENCE`, with no numerical reward and no reward-bearing Q-update;
8. the natural numerical reward range is \([-1,+1]\), with no additional clipping;
9. `ZERO REWARD` with \(F_t>0\) is distinct from `NO REWARD` at \(F_t=0\);
10. the complete deterministic suite 02.6.7.1--02.6.7.10 is PASS / FROZEN.

#### 02.6.8.3 Immediate next gate

> **COMPLETED: Final executable reward-contract reconciliation and 02.6 closure audit.**

The executable \(R_t\) has been derived and verified from the frozen 02.6.1--02.6.7 decisions without introducing a new signal, coefficient, weight, threshold, bonus, penalty, clipping rule, or \(F_t\)-based magnitude modifier.

The reconciliation must remain aligned with:
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/01_CANONICAL_AHBN_CONTRACT.md`;
- the frozen Q-AHBN2 architecture and reward decisions in this document;
- the RO2 dissemination trade-off: productive dissemination evidence must remain distinguishable from redundant and unsuccessful forwarding effort.

#### 02.6.8.4 Final 02.6 exit condition

After the executable reward contract is reconciled, perform one final 02.6 closure audit covering:
- internal mathematical consistency;
- consistency with every frozen 02.6 gate;
- no reward double counting;
- no leakage or attribution violation;
- canonical AHBN remains unchanged and independently traceable;
- deterministic cases remain satisfied;
- executable edge-case semantics are explicit;
- implementation can reproduce the contract without an unstated design choice.

Only if that audit passes may the section be marked:

```text
02.6 Reward Construction = PASS / COMPLETE / FROZEN
```

No additional gate may be inserted merely for completeness, optimization, or extra assurance. If an unexpected validity-critical check is required, it must be logged with its reason, evidence, result, scientific impact, and roadmap impact under the execution protocol in `docs/02A_QAHBN2_ACCELERATED_FREEZE_PLAN.md`.



---

## 02.7 Learning Parameters — PASS / COMPLETE / FROZEN

### 02.7.1 Gate contract

S02-F freezes the conventional Q-learning parameters required by Section 15 of the master contract:

```text
F1 learning rate (alpha_Q)
F2 discount factor (gamma)
F3 epsilon start
F4 epsilon minimum
F5 epsilon decay factor
F6 cross-source / RO2 / AHBN-boundary reconciliation
F7 bounded numerical sanity check
F8 block closure
```

This is a Category-B conventional design block under the accelerated protocol. It is not a hyperparameter-optimization study.

### 02.7.2 Frozen values

The Q-AHBN2 logical learning-parameter contract is:

$$
\alpha_Q = 0.25,\qquad
\gamma = 0.90,\qquad
\epsilon_0 = 0.30,\qquad
\epsilon_{\min}=0.03,\qquad
\lambda_{\epsilon}=0.995.
$$

The exploration schedule is multiplicative:

$$
\epsilon_{n+1}=\max\left(\epsilon_{\min},\lambda_{\epsilon}\epsilon_n\right).
$$

Here $n$ counts learner decision/decay steps. The precise lifecycle placement, episode definition, and reset/persistence behavior remain owned by S02-H and MUST NOT change these frozen numerical values.

### 02.7.3 Source-authority reconciliation

The required historical comparison is recorded in `docs/00_SOURCE_AUTHORITY_REGISTER.md`, Section 12.

- ControlSim historical Q-AHBN: `alpha=0.25`, `gamma=0.90`, `epsilon=0.30`, `epsilon_min=0.03`, `epsilon_decay=0.995`.
- GKE historical Q-AHBN: `alpha=0.25`, `gamma=0.90`, `epsilon=0.20`, `epsilon_min=0.03`, `epsilon_decay=0.995`.

The common values are retained. The epsilon-start disagreement is reconciled to **0.30**, preserving the historical ControlSim learning-validation value rather than inventing a newly tuned value. Q-AHBN2 requires one logical learning contract across platforms.

### 02.7.4 RO2 alignment

RO2 is used as the scientific problem constraint, not as false evidence for a unique RL optimum.

RO2 established condition-dependent dissemination trade-offs: increasing fanout reduces propagation delay while increasing duplication; failure/overload and churn expose fragility in structured dissemination while gossip remains more robust; heterogeneous conditions reduce efficiency. These findings justify a learner that can remain responsive, value future consequences, and continue bounded exploration across changing conditions.

Accordingly:

- `alpha_Q=0.25` provides moderate incremental adaptation rather than replacing learned values wholesale;
- `gamma=0.90` retains substantial future-outcome value, appropriate to temporally evolving dissemination conditions;
- non-zero epsilon exploration is retained because RO2 shows that no single static dissemination behavior dominates all evaluated conditions;
- the exact numerical values are inherited/reconciled from historical Q-AHBN evidence under the minimum-adaptation rule, **not claimed to be optimized by RO2**.

### 02.7.5 Canonical-AHBN protection

The Q-learning learning rate is written `alpha_Q` in the Q-AHBN2 contract to distinguish it from the immutable canonical AHBN EWMA smoothing coefficient:

$$
\alpha_{AHBN}=0.30.
$$

Therefore:

```text
alpha_AHBN = 0.30   FROZEN CANONICAL EWMA
alpha_Q    = 0.25   Q-AHBN2 Q-learning rate
```

No learning parameter modifies AHBN observations, EWMA, score, sigmoid, mode rule, S5 thresholds, or canonical proposal generation.

### 02.7.6 Bounded sanity verification

For the frozen epsilon schedule:

$$
\epsilon_n=\max(0.03,0.30(0.995)^n).
$$

The floor is reached after approximately 460 decay steps. This confirms that the schedule is finite, monotone, bounded in $[0.03,0.30]$, and preserves residual exploration.

This check establishes numerical semantics only. Whether epsilon resets per episode/run or persists is deliberately deferred to S02-H.

### 02.7.7 Gate results

| Subgate | Result |
|---|---|
| F1 learning rate | PASS / FROZEN — `alpha_Q=0.25` |
| F2 discount factor | PASS / FROZEN — `gamma=0.90` |
| F3 epsilon start | PASS / FROZEN — `epsilon_0=0.30` |
| F4 epsilon minimum | PASS / FROZEN — `epsilon_min=0.03` |
| F5 epsilon decay | PASS / FROZEN — multiplicative `0.995` |
| F6 authority + RO2 + AHBN boundary | PASS |
| F7 numerical sanity | PASS |
| F8 closure | PASS / COMPLETE / FROZEN |

**S02-F LEARNING PARAMETERS = PASS / COMPLETE / FROZEN.**

No parameter sweep is authorized by this freeze. Performance tuning alone is not grounds to reopen S02-F.

### 02.7.8 Next documented gate

The next unresolved Section-15 requirement is:

```text
G — Q-Learning Mechanics
    G1 Q-table initialization
    G2 Q-update equation
    G3 exploration/exploitation selection semantics
    G4 tie handling / deterministic RNG semantics where required
    G5 bounded known-answer verification
    G6 closure
```

S02-G must reconcile the historical mechanics against the already-frozen 81-state × 5-action Q-AHBN2 contract and reward contract. It must not reopen S02-F merely for optimization.


---

## 02.8 Q-Learning Mechanics — PASS / COMPLETE / FROZEN

### 02.8.1 Frozen Q-table initialization

Q-AHBN2 uses the frozen 81-state × 5-action logical table. Every state-action entry is initialized to:

$$Q_0(s,a)=0.$$

Lazy materialization is permitted in implementation provided it is exactly equivalent to a fully allocated zero-initialized 81 × 5 table.

### 02.8.2 Frozen one-step Q update

For the completed transition $(s_t,a_t,R_t,s_{t+1})$:

$$
Q(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha_Q\left[R_t+\gamma\max_{a'}Q(s_{t+1},a')-Q(s_t,a_t)\right],
$$

with the S02-F constants:

$$\alpha_Q=0.25,\qquad\gamma=0.90.$$

This is ordinary off-policy one-step tabular Q-learning. No eligibility traces, replay buffer, target network, model-based update, or additional optimizer is introduced.

### 02.8.3 Frozen exploration/exploitation semantics

At each Q-AHBN2 action-selection opportunity:

```text
draw u from the learner's seeded PRNG

if u < epsilon:
    EXPLORE:
        choose uniformly from all 5 frozen Q-AHBN2 actions
else:
    EXPLOIT:
        compute max_a Q(s,a)
        form the set of all actions tied at that maximum
        choose uniformly from that tied set using the same seeded PRNG
```

Random tie handling is mandatory. With zero initialization, this prevents action-order bias at previously unseen states.

### 02.8.4 Deterministic RNG contract

The learner owns a deterministic seeded pseudo-random stream. Given the same frozen logical inputs, initial Q table, seed, and lifecycle, action-selection randomness must be reproducible.

The exact experiment seed mapping and reset/persistence policy are owned by S02-H / the later experiment contract; S02-G freezes only the mechanic that stochastic choices use the controlled learner RNG rather than uncontrolled global randomness.

### 02.8.5 Reward/transition boundary

The update consumes the already-frozen reward $R_t$ from Section 02.6 and the next frozen discrete state $s_{t+1}$ from Sections 02.3–02.4. S02-G does not redefine when an interval begins/ends or when a run resets; those lifecycle semantics are S02-H.

Required ordering at the logical transition level is:

```text
(s_t, a_t)
    ↓
attributed interval outcomes
    ↓
R_t + s_(t+1)
    ↓
one-step Q update for (s_t,a_t)
    ↓
epsilon-greedy selection for the next action
```

### 02.8.6 Source and RO2 reconciliation

The historical ControlSim and GKE learners both use zero initialization, the same one-step Q-learning equation, epsilon-greedy selection, and seeded random tie-breaking. Source comparison is recorded in `docs/00_SOURCE_AUTHORITY_REGISTER.md`, Section 13.

RO2 demonstrates a changing dissemination trade-off across fanout, failures/overload, churn, and heterogeneous conditions. It motivates learning over changing state/action consequences, but does not justify a more complex RL algorithm. Conventional tabular Q-learning is therefore retained as the minimum mechanism required to test the RO4 learning-enhancement question.

Canonical AHBN remains unchanged and is evaluated before this learning layer.

### 02.8.7 Known-answer micro-case

For:

```text
Q(s_t,a_t) = 0
R_t = +0.50
max_a' Q(s_(t+1),a') = 0
alpha_Q = 0.25
gamma = 0.90
```

the frozen update must produce:

$$Q_{new}=0+0.25(0.50+0.90(0)-0)=0.125.$$

A future implementation unit test MUST reproduce this exact value.

### 02.8.8 Gate results

| Subgate | Result |
|---|---|
| G1 Q-table initialization | PASS / FROZEN — zero |
| G2 Q-update | PASS / FROZEN — one-step tabular Q-learning |
| G3 exploration/exploitation | PASS / FROZEN — epsilon-greedy |
| G4 tie/RNG semantics | PASS / FROZEN — seeded uniform random tie handling |
| G5 known-answer verification | PASS — expected update 0.125 |
| G6 closure | PASS / COMPLETE / FROZEN |

**S02-G Q-LEARNING MECHANICS = PASS / COMPLETE / FROZEN.**

### 02.8.9 Next documented gate

```text
H — Learning Lifecycle
    H1 episode definition
    H2 learning trigger / decision interval
    H3 observation interval
    H4 action interval
    H5 transition/reward/update ordering
    H6 epsilon decay placement
    H7 reset/persistence policy
    H8 closure
```

This is the next unresolved Section-15 requirement.


---

## 02.9 Learning Lifecycle — IN PROGRESS

### 02.9.1 H master gate

```text
H1 episode definition
H2 learning trigger / decision interval
H3 observation interval
H4 action interval
H5 transition/reward/update ordering
H6 epsilon decay placement
H7 reset/persistence policy
H8 closure
```

Frozen evidence already requires one Q action for one new-message forwarding decision at one peer, with reward closure only after all direct attempts for that action resolve to NEW, DUPLICATE, or FAILED. Historical next-invocation reward timing is not inherited.

### 02.9.2 Discovered check H-X — overlapping action windows

```text
DISCOVERED CHECK
Origin: reconciliation of per-message reward attribution with one-step Q learning
Reason: another new-message decision may occur before an earlier action closes
Classification: L3
Validity-critical: YES
Scientific decision introduced: YES
Evidence: DOC-02 02.6.1A/02.6.1B and Source Authority Register Section 14
Result: a single historical prev_state/prev_action chain is insufficient when
        multiple per-message attribution windows are simultaneously pending
Impact on frozen decisions: NONE yet
Impact on roadmap: H cannot close until H-X is resolved
```

### 02.9.3 Bounded alternatives

**A — Serialize Q decisions per peer until the current attribution window closes.** This gives a simple sequential chain but changes availability of learned intervention for later new messages.

**B — Permit concurrent per-message attribution records and apply each completed transition to the shared Q table.** Each $(s_t,a_t)$ closes independently. This preserves the frozen one-action-per-new-message contract but requires an explicit next-state rule.

**C — Replace the per-message action unit with a peer-level multi-message control interval.** This would conflict with frozen 02.6.1A and therefore requires reopening that contract.

### 02.9.4 Recommendation at the L3 boundary

**Recommend B.** It preserves the frozen action and reward-attribution contracts without changing canonical AHBN.

If accepted, use this conservative transition rule:

```text
s_t      = frozen state snapshot at action selection
R_t      = reward from that action's closed direct-attempt attribution set
s_(t+1)  = peer's current frozen 81-state representation sampled when that
           action's attribution window closes
update   = frozen one-step Q update on (s_t,a_t,R_t,s_(t+1))
```

This adds no sensor and does not modify AHBN, but it defines causal lifecycle semantics under concurrent message handling and therefore requires explicit L3 approval.

**S02-H = IN PROGRESS — BLOCKED AT H-X L3 DECISION.**
