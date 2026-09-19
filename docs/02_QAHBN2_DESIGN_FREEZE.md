# Q-AHBN2 Design Freeze

**Document ID:** QAHBN2-DOC-02  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/02_QAHBN2_DESIGN_FREEZE.md`  
**Status:** PARTIAL DESIGN FREEZE — Sections 02.1–02.2 FROZEN  
**Freeze date for Sections 02.1–02.2:** 2026-09-19  
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

## 02.3 Next Controlled Decision — State Representation

The next permitted design task is to freeze the Q-AHBN2 logical state representation.

It must begin from the architectural boundary above and must not reopen Sections 02.1–02.2 merely to improve expected performance.
