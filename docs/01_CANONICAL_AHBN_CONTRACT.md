# Q-AHBN2 Canonical AHBN Contract

**Document ID:** QAHBN2-DOC-01  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/01_CANONICAL_AHBN_CONTRACT.md`  
**Status:** FROZEN CANONICAL AHBN CONTRACT  
**Freeze date:** 2026-09-19  
**Scope:** Normative AHBN boundary inherited by Q-AHBN2. This document defines no Q-learning state, action, reward, hyperparameter, training policy, or implementation.

---

## 1. Purpose

This contract freezes the AHBN mechanism that Q-AHBN2 must treat as immutable. It is derived only from the completed R1/R1-GKE reconciliation and canonical sources registered in `docs/00_SOURCE_AUTHORITY_REGISTER.md`.

Q-AHBN2 may later define a learning layer around this boundary, but it may not silently retune, reinterpret, or replace the AHBN mechanism specified here.

The canonical scientific chain is:

```text
environment-specific local measurements
        ↓
normalization to logical d, l, u, c ∈ [0,1]
        ↓
EWMA state d_hat, l_hat, u_hat, c_hat
        ↓
z = -d_hat + l_hat + u_hat + c_hat
        ↓
w = sigmoid(z)
        ↓
canonical mode + final S5 requested fanout
        ↓
mode-specific eligible-target realization
        ↓
actual forwarding
        ↓
outcomes / subsequent local observations
```

---

## 2. Normative Sources

This contract is bounded by:

| Environment / description | Normative reference |
|---|---|
| ControlSim canonical AHBN | `wwiras/ahbn@936a79480bc1252c79b6ee01f65c88c740af2844` |
| Kubernetes canonical AHBN | `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` |
| Scientific description | Revised AHBN Scientific Reports manuscript, 17 Sep 2026 |
| Reconciliation authority | `docs/00_SOURCE_AUTHORITY_REGISTER.md` |

Historical `wwiras/q-ahbn`, `wwiras/q-ahbn_gke`, and the historical Q-AHBN manuscript are **not** sources for this canonical AHBN contract.

Where implementation provenance is composite, the final reconciled scientific boundary in the source-authority register controls interpretation.

---

## 3. Logical Observation Contract

AHBN has exactly four logical local observations:

| Symbol | Meaning | Range | Direction in score |
|---|---|---:|---:|
| `d` | duplicate pressure | `[0,1]` | negative |
| `l` | local latency pressure | `[0,1]` | positive |
| `u` | local utilization / processing pressure | `[0,1]` | positive |
| `c` | churn / instability pressure | `[0,1]` | positive |

These meanings are common across environments. Raw acquisition, normalization, and observation cadence are environment-specific adapters and are not themselves the environment-independent control law.

### 3.1 ControlSim acquisition

At the pinned ControlSim boundary:

- `d` is the local raw duplicate ratio `duplicates / total_received`, defensively clamped to `[0,1]`;
- `l` is local **one-hop** delay, not end-to-end message age, normalized by the saturating function `x / (x + latency_reference)`;
- the default `latency_reference` is expected normal one-hop delay `base_delay + jitter/2`;
- `u` is average forwarding work per received message, normalized by maximum forwarding budget and scaled by node capacity; explicit overload forces pressure to at least 1 before clamping;
- `c` is the supplied churn/instability proxy clamped to `[0,1]`;
- an omitted optional observation does not manufacture a zero: its corresponding EWMA state is retained.

### 3.2 Kubernetes acquisition

At the pinned Kubernetes boundary, `KubernetesObservationAdapter` closes interval-local windows using `snapshot_and_reset()`:

| Input | GKE normalization |
|---|---|
| `d` | interval duplicates / interval receives; `0` when no receives |
| `l` | mean interval local one-hop latency / fixed 1.0 s reference, clipped to `[0,1]` |
| `u` | `1` when local `overload_ms > 0`, otherwise `0` |
| `c` | interval joins + leaves divided by current neighbour count (minimum denominator 1), clipped to `[0,1]` |

After a snapshot, interval receive, duplicate, latency, join, and leave counters reset.

A zero component in a complete GKE interval snapshot is a legitimate observed interval value. This is different from ControlSim's optional-observation interface and must not be conflated with “missing observation”.

### 3.3 Environment boundary

Cross-platform parity means parity of the **logical controller contract for the same normalized input sequence**, not identity of raw sensor formulas. Q-AHBN2 must preserve this separation.

---

## 4. Canonical EWMA State

The controller maintains:

`d_hat, l_hat, u_hat, c_hat`.

For a supplied logical observation `x_t`:

```text
x_hat(t) = α x_t + (1 - α) x_hat(t-1)
α = 0.30
```

Supplied observations are bounded to `[0,1]`.

Canonical initial state:

- `d_hat = l_hat = u_hat = c_hat = 0`;
- `score = 0`;
- `weight = 0.5`;
- mode = Gossip;
- requested fanout = 3.

The four centres are all zero:

`d0 = l0 = u0 = c0 = 0`.

---

## 5. Canonical Score and Weight

The frozen score is:

```text
z = -d_hat + l_hat + u_hat + c_hat
```

Equivalently, the coefficient vector is:

`(w_d, w_l, w_u, w_c) = (-1,+1,+1,+1)`.

The frozen sigmoid scale is `κ = 1`:

```text
w = sigmoid(z) = 1 / (1 + exp(-z))
```

The weight is a deterministic bounded preference derived from the score. It is **not** a probability used to mix Gossip and Structured forwarding.

---

## 6. Canonical Mode Rule

The frozen mode threshold is `0.50`:

```text
w >= 0.50  ⇔  z >= 0  → Gossip
w <  0.50  ⇔  z <  0  → Structured
```

The implementation label `cluster` denotes the scientific **Structured** mode.

There are exactly two AHBN dissemination modes. No third mode exists in this contract.

---

## 7. Final S5 Requested-Fanout Actuator

The canonical requested forwarding budget is:

`k_request ∈ {2,3,4,5,6}`.

The frozen S5 mapping is:

| Score `z` | `k_request` |
|---|---:|
| `z <= -0.25` | 2 |
| `-0.25 < z < 0.25` | 3 |
| `0.25 <= z < 0.90` | 4 |
| `0.90 <= z < 1.50` | 5 |
| `z >= 1.50` | 6 |

Boundary anchors are normative: `-0.25→2`, `0→3`, `0.25→4`, `0.90→5`, and `1.50→6`.

### 7.1 Kubernetes provenance guard

The pinned GKE repository is composite. Its base `app/ahbn_controller.py` retains the earlier parity-validated S0 2/3/4 actuator, while the frozen final S5 runtime replaces the requested forwarding budget after the canonical controller produces its score/mode/state.

Therefore:

- the GKE base field `canonical_fanout` in the S5 runtime trace is an earlier S0 provenance value;
- it is **not** the final canonical requested fanout;
- `requested_fanout` from the frozen S5 runtime is the final canonical GKE AHBN request;
- Q-AHBN2 must use the final S5 proposal at its AHBN boundary.

---

## 8. Eligible-Target Realization Contract

The controller's `k_request` is a forwarding **budget**, not a guarantee that exactly that many peers will receive the message.

For eligible set `N_e`:

```text
0 <= k_real <= min(k_request, |N_e|)
```

Topology, immediate-sender exclusion, node availability/activity, and mode-specific structural eligibility constrain realization.

### 8.1 Gossip

Eligible candidates exclude the local node, the immediate sender, and unavailable/inactive peers as represented by the environment. Selection is bounded by `k_request`.

### 8.2 Structured

A Structured member forwards only toward its eligible cluster head.

For a Structured cluster head, the canonical policy preserves outward connectivity while remaining within budget: an eligible gateway is prioritized where available, followed by eligible local members, then additional eligible gateways if budget remains.

No canonical realization path may silently append extra targets beyond `k_request`.

### 8.3 Requested versus realized

`k_request` and `k_real` are different scientific quantities and must remain separately interpretable in implementation, traces, analysis, and manuscript claims.

---

## 9. Update and Execution Ordering

The normative logical ordering is:

```text
acquire/derive local observations
        ↓
update canonical EWMA state
        ↓
compute z and w
        ↓
decide canonical mode
        ↓
derive final S5 k_request
        ↓
construct mode-specific eligible set
        ↓
select targets within budget
        ↓
forward to realized targets
        ↓
record forwarding/outcomes
        ↓
feed later local observations
```

A duplicate receipt may update the AHBN observation/controller state but does not trigger another forwarding of that already-seen message.

Environment-specific event scheduling may differ, but it may not change the controller law or bypass the requested-budget realization contract.

Failure/churn events are observations to the canonical path. They do not authorize an unlabelled direct mode/fanout override.

---

## 10. Trace and Observability Contract

A canonical trace must permit reconstruction of the AHBN decision sufficiently to distinguish:

- normalized observations and/or their EWMA state;
- `z` / score;
- `w` / weight;
- mode;
- final S5 `k_request`;
- realized target count where execution-level fanout is being analysed.

ControlSim trace `fanout` denotes controller-requested fanout unless a field explicitly says otherwise.

In final S5 GKE execution:

- `requested_fanout` = final S5 request;
- `actual_fanout` = realized target count;
- `canonical_fanout` = earlier S0 provenance value and must not be reported as final S5 `k_request`.

Any future Q-AHBN2 trace must keep the untouched AHBN base proposal distinguishable from any later learning-layer decision.

---

## 11. Controller Observations versus Evaluation Metrics

Controller inputs and experiment outcomes must not be conflated.

In particular:

- AHBN `l` / `l_hat` is local one-hop latency pressure; experiment propagation delay is an outcome metric;
- AHBN `u` / `u_hat` is local processing/utilization pressure; experiment total forwards is an outcome metric;
- duplicate pressure used by the controller is not automatically identical to any aggregate duplicate-count result;
- local churn/instability pressure is not itself experiment recovery time.

Evaluation metrics may be used later by Q-AHBN2 research only under an explicitly frozen learning/experiment contract. They do not redefine AHBN.

---

## 12. Explicit Non-Features and Prohibitions

The canonical AHBN inherited by Q-AHBN2 has:

- no tau-based suppression actuator;
- no probabilistic Gossip/Structured mixing based on `w`;
- no third dissemination mode;
- no RL/Q-learning state, action, reward, Q-table, exploration schedule, or learning update;
- no historical GKE `fail_pressure` controller;
- no historical rule-based `adaptive_update()` substitute;
- no hard-coded recovery action that may be labelled as learned behavior;
- no target realization that appends peers beyond the requested budget;
- no permission to reinterpret a learning-modified weight as the untouched canonical `sigmoid(z)`;
- no permission to retune `α`, score coefficients, centres, `κ`, mode threshold, or S5 thresholds to accommodate Q-AHBN2.

Any future deterministic safety override, if scientifically approved, must exist outside this AHBN contract and be separately named, justified, logged, and attributed.

---

## 13. Canonical Regression and Parity Anchors

At the ControlSim pinned boundary, `v0.63/scripts/validate_canonical_ahbn_frozen.py` protects:

- `α=0.30`;
- zero centres;
- score signs `(-1,+1,+1,+1)`;
- `κ=1`;
- mode threshold `0.5`;
- fanout range 2–6;
- representative score/mode/fanout anchors;
- exact S5 threshold boundaries.

Representative anchors include:

| EWMA state / score condition | Expected |
|---|---|
| all-zero state | `z=0`, Gossip, `k=3` |
| `d_hat=0.5` only | `z=-0.5`, Structured, `k=2` |
| `l_hat=0.5` only | `z=0.5`, Gossip, `k=4` |
| `u_hat=0.5` only | `z=0.5`, Gossip, `k=4` |
| `z=-0.25` | `k=2` |
| `z=0.25` | `k=4` |
| `z=0.90` | `k=5` |
| `z=1.50` | `k=6` |

The canonical GKE port was reconciled as parity-preserving for the common logical controller, with environment-specific sensing and the final S5 runtime actuator explicitly accounted for.

Future Q-AHBN2 implementation must add its own parity tests against this contract rather than weakening these anchors.

---

## 14. Immutable AHBN Boundary Exposed to Q-AHBN2

The future learning layer may consume or observe only explicitly designed information, but the AHBN base object it receives must remain interpretable as:

```text
AHBN input:
    logical local observations d,l,u,c

AHBN internal state:
    d_hat,l_hat,u_hat,c_hat

AHBN deterministic proposal:
    z
    w = sigmoid(z)
    mode ∈ {Gossip, Structured}
    k_request ∈ {2,3,4,5,6}

Execution boundary:
    canonical mode-specific eligible-target realization
    k_real <= min(k_request, |N_e|)
```

If Q-AHBN2 later modifies a mode or forwarding budget, the canonical AHBN proposal must first exist unchanged and remain separately observable. The modified result is a **Q-AHBN2 decision**, not a retroactive redefinition of AHBN.

---

## 15. Freeze Gate

Verification checklist:

- [x] ControlSim canonical source pinned and reconciled.
- [x] Kubernetes canonical source pinned and reconciled.
- [x] Four logical observation semantics fixed.
- [x] Environment-specific observation adapters distinguished.
- [x] EWMA fixed at `α=0.30`.
- [x] Score and sigmoid fixed.
- [x] two-mode rule fixed.
- [x] final S5 requested-fanout mapping fixed.
- [x] requested-versus-realized semantics fixed.
- [x] mode-specific eligibility/realization boundary fixed.
- [x] trace interpretation guards fixed.
- [x] controller observations separated from experiment outcomes.
- [x] legacy Q-AHBN semantics excluded.
- [x] no Q-AHBN2 state/action/reward/hyperparameter values introduced.

**CANONICAL AHBN CONTRACT GATE: PASS / FROZEN.**

Any change to this document requires reopening the canonical source-reconciliation gate with stronger source evidence. Q-AHBN2 design convenience is not sufficient justification for changing AHBN.

---

## 16. Next Permitted Artifact

With this contract frozen, the next controlled artifact is:

`docs/02_QAHBN2_DESIGN_FREEZE.md`

That artifact may design the Q-AHBN2 learning layer, but it must reference and preserve this canonical AHBN contract. Implementation remains unauthorized until the design-freeze gate passes.
