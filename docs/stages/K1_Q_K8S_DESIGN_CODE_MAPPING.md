# K1-Q — Q-AHBN2 GKE Design-to-Code Mapping

**Status:** PASS / CLOSED

## Objective
Map the frozen Q-AHBN2 state, action, reward, transition, and AHBN-refinement semantics into the Kubernetes event path.

## Boundary
No learner redesign. Environment-specific observation acquisition is permitted only where already compatible with the canonical AHBN deployment contract.


## Release basis
Released after K0-Q PASS / CLOSED on 2026-09-29.

## Inheritance constraint
K1-Q must start from the pinned `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689` implementation. Gossip, Structured, DC-SoC and canonical AHBN are inherited deployment baselines and are not to be recreated in `q-ahbn2`.

The purpose of K1-Q is to map the frozen Q-AHBN2 learning/refinement contract onto the existing Kubernetes event path and define the smallest safe patch surface in `q-ahbn2`. Historical `q-ahbn_gke` may be consulted for integration context only and cannot override the frozen Q-AHBN2 contract.

## Next permitted task
Perform exact design-to-code mapping only: inherited files/event boundaries, Q-AHBN2 insertion point, state construction, AHBN proposal capture, bounded action refinement, eligible-target realization, attributed NEW/DUPLICATE/FAILED outcomes, reward closure, next-state bookkeeping, learning trace/provenance, and required regression/parity tests. No implementation change until the mapping is complete and accepted.


## K1-Q Read-Only Design-to-Code Mapping — 2026-09-29

### 1. Inherited Kubernetes runtime files and responsibilities

The pinned deployment baseline remains `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`.

| Inherited file/path | K1-Q role | Change policy |
|---|---|---|
| `app/observations.py` | Kubernetes acquisition/normalization of canonical d,l,u,c interval observations | inherit semantics unchanged |
| `app/ahbn_controller.py` | canonical EWMA/controller state, score, sigmoid and mode | immutable |
| `app/peer.py` | gRPC receive/send path; seen-state NEW/DUPLICATE determination; failure observation; Gossip/Structured/DC-SoC eligibility/dispatch | preserve existing comparator semantics; Q-AHBN2 integration may hook only the explicitly mapped qahbn2 path |
| `app/k5_final_actuator_policy.py` | frozen S5 requested-fanout mapping 2..6 | immutable |
| `app/k5_final_actuator_runtime.py` | validated post-controller S5 proposal and existing mode-specific eligibility realization seam | authoritative AHBN proposal boundary for Q-AHBN2 |
| `app/dcsoc_maintenance.py` and established DC-SoC runtime path | DC-SoC comparator behavior | inherit unchanged |
| K6/K7/K8 runtime/controller/harness lineage | established dynamic Kubernetes orchestration, churn/failure handling, provenance and validation patterns | reuse where K4-Q later freezes the exact protocol; do not reinterpret as Q-AHBN2 logic |

Gossip, Structured, DC-SoC and AHBN remain inherited methods. No Q-AHBN2 requirement justifies reimplementation of those algorithms.

### 2. Frozen Q-AHBN2 modules to reuse

The current `q-ahbn2` learning implementation already separates environment-independent learning semantics from ControlSim integration:

| Q-AHBN2 file | Frozen responsibility | Kubernetes decision |
|---|---|---|
| `qahbn2/learning.py` | 81-state discretization, five actions, epsilon-greedy selection/decay, bounded refinement, reward equation, Q update | reuse learning core unchanged |
| `qahbn2/transition.py` | originating-decision ownership, same-peer next-decision successor state, delayed/out-of-order reward closure, F=0 no-update, terminal zero bootstrap | reuse unchanged |
| `qahbn2/controlsim_adapter.py` | ControlSim-specific bridge into the learner | do not reuse as Kubernetes adapter; use as structural reference only |
| `qahbn2/event_bridge.py` | ControlSim-specific direct-attempt bridge | do not reuse simulator target realization; use attribution/closure contract as structural reference |

A Kubernetes adapter/bridge may therefore be added later without duplicating the learner.

### 3. Exact Q-AHBN2 insertion point

For `strategy=qahbn2`, the required logical event order is:

```text
existing Kubernetes observations
        ↓
canonical AHBN snapshot/update
        ↓
canonical AHBN EWMA state (d_hat,l_hat,u_hat,c_hat)
        ↓
frozen S5 AHBN proposal (mode_AHBN,k_AHBN)
        ↓
Q-AHBN2 discretize same canonical EWMA state
        ↓
choose one frozen Q action
        ↓
bounded refine(mode_AHBN,k_AHBN)
        ↓
existing Gossip/Structured eligible-target semantics
        ↓
realized targets constrained by eligibility
        ↓
direct send attempts
        ↓
NEW | DUPLICATE | FAILED attribution to originating decision
        ↓
reward closure
        ↓
same peer's next Q decision supplies s_(t+1)
        ↓
Q update when reward + successor evidence are both ready
```

The Q-AHBN2 state MUST use the post-update canonical AHBN EWMA components, not the raw interval snapshot. The Q-AHBN2 AHBN proposal MUST use the final frozen S5 requested fanout, not the historical base-controller `canonical_fanout` diagnostic.

### 4. State construction mapping

At each Q-AHBN2 decision opportunity:
1. preserve `KubernetesObservationAdapter.snapshot_and_reset(...)` and canonical `CanonicalAHBNController.update(...)`;
2. after that update, read the canonical AHBN EWMA state components;
3. pass those four normalized EWMA values to the existing `QAHBN2Learner.discretize()`;
4. preserve the exact L/M/H boundaries already frozen in the learner, yielding 3^4 = 81 states.

No Kubernetes-only state component, failure phase, topology role, privileged event label or historical Q-AHBN-GKE state is permitted.

### 5. AHBN proposal capture and Q refinement

The AHBN proposal exposed to Q-AHBN2 is:
- `mode_AHBN`: canonical post-update Gossip/Structured mode;
- `k_AHBN`: final S5 requested fanout from the frozen S5 policy.

Then call the unchanged frozen learner action/refinement semantics:
- KEEP;
- FANOUT_DOWN;
- FANOUT_UP;
- SET_GOSSIP;
- SET_STRUCTURED.

Any refined requested fanout remains subject to the frozen Q-AHBN2 action bounds and then to actual eligible-neighbour realization. Q-AHBN2 must not alter AHBN EWMA, score, sigmoid, thresholds, S5 mapping, or the comparator implementations.

### 6. Eligible-target realization mapping

After Q refinement:
- Gossip mode reuses the established Gossip eligible set: exclude self, immediate sender and unavailable neighbours, then select only within the requested budget;
- Structured mode reuses the established cluster-head/member/gateway semantics and budget-aware structural selection;
- realized fanout remains distinct from requested/refined fanout;
- DC-SoC is never entered as a Q-AHBN2 action and remains a standalone comparator.

The ControlSim bridge's simple prefix realization is not portable Kubernetes behavior and MUST NOT replace the inherited GKE selection semantics.

### 7. Direct-attempt outcome attribution

The frozen reward requires each direct attempt owned by a Q-AHBN2 decision to close as exactly one of:
- `NEW`: the receiver accepted the message as first-seen;
- `DUPLICATE`: the receiver already had the message;
- `FAILED`: the originating sender's direct attempt failed to complete successfully.

The existing receiver `seen_messages` path already distinguishes first reception from duplicate reception. The existing sender path already distinguishes successful gRPC completion from send failure. K1-Q therefore maps a minimal Q-AHBN2-only acknowledgement/outcome bridge so the sender can attribute receiver NEW versus DUPLICATE to the originating decision. Source injection is excluded exactly as in the frozen reward-admissibility contract.

This bridge must not change dissemination decisions or standalone comparator semantics.

### 8. Reward closure and F=0

For each originating decision, aggregate only its direct-attempt outcomes:
`F = NEW + DUPLICATE + FAILED`.

Reuse `QAHBN2Learner.close_outcomes()` unchanged:
- F>0 -> reward = (NEW - DUPLICATE - FAILED)/F;
- F=0 -> no numerical reward and no Q update.

Concurrency may allow outcomes to close after a later decision; ownership remains by unique decision ID.

### 9. Next-state bookkeeping

Reuse `TransitionBookkeeper` unchanged:
- s_t is captured at a peer's Q-AHBN2 decision;
- the next Q-AHBN2 decision at that same peer supplies s_(t+1) to the preceding pending transition;
- reward may arrive before or after s_(t+1);
- update occurs once both required pieces are available;
- final reward-bearing pending decisions are terminal with zero bootstrap;
- F=0 decisions never become reward-bearing/update-ready.

Kubernetes thread completion order must not redefine this temporal contract.

### 10. Minimum implementation patch surface for K2-Q preparation

K1-Q authorizes no implementation yet, but identifies the minimum future patch classes:

1. **Q-AHBN2 Kubernetes adapter/bridge in `q-ahbn2`**
   - instantiate/use the unchanged `QAHBN2Learner`;
   - create unique decision IDs;
   - consume canonical EWMA state + final S5 proposal;
   - expose Q-refined mode/fanout;
   - own pending direct-attempt attribution and closure;
   - expose terminal closure.

2. **Bounded inherited-runtime integration**
   - add `strategy=qahbn2` without changing the behavior of `gossip`, `cluster`, `dcsoc` or `ahbn`;
   - route only Q-AHBN2 through AHBN -> S5 -> Q refinement -> inherited eligibility;
   - return/record enough receiver acknowledgement semantics for NEW/DUPLICATE attribution;
   - attach FAILED to the originating Q decision on direct send failure.

3. **Q-AHBN2 trace/provenance fields**
   - decision_id, peer_id, message_id;
   - state and canonical EWMA components;
   - AHBN score/weight/mode and final S5 k_AHBN;
   - Q action, mode_Q, k_Q;
   - eligible set/count and realized targets/count;
   - NEW/DUPLICATE/FAILED counts, F and reward/no-reward status;
   - successor-state/update identity where an update occurs;
   - epsilon used/current schedule position and Q-update count;
   - producing Git commit/image identity in run provenance.

No new scientific metric is introduced by these traces.

### 11. Required K2-Q regression/parity checks

Before any GKE smoke, K2-Q must deterministically verify at minimum:
1. standalone Gossip unchanged;
2. standalone Structured unchanged;
3. standalone DC-SoC unchanged;
4. standalone AHBN/S5 unchanged;
5. canonical observation/controller trajectory unchanged;
6. Q state = discretization of canonical post-update EWMA state;
7. AHBN proposal captured before Q refinement and uses final S5 fanout;
8. all five Q actions have exact frozen effects and bounds;
9. Gossip/Structured eligible-target semantics remain inherited;
10. requested/refined/realized fanout remain distinguishable;
11. NEW attribution exact and source injection excluded;
12. DUPLICATE attribution exact;
13. FAILED attribution exact;
14. mixed direct attempts close to the exact frozen reward;
15. F=0 causes no Q update;
16. same-peer next-decision state linkage is exact;
17. delayed/out-of-order reward closure remains correct under concurrency;
18. terminal zero-bootstrap behavior exact;
19. epsilon decay and Q-update equation match the frozen learning core;
20. historical Q-AHBN-GKE hard-coded recovery/bypass behavior is absent;
21. Q-AHBN2 does not leak into standalone comparator strategies;
22. deterministic trace/provenance contains enough fields to audit one decision end-to-end.

K2-Q should prefer unit/deterministic integration tests before any Kubernetes resource creation.

### 12. Explicit non-patch files/science

K1-Q does not authorize changes to:
- canonical AHBN equation/normalization/EWMA/sigmoid/mode;
- S5 thresholds or requested-fanout mapping;
- Q-AHBN2 state/action/reward/update/hyperparameters;
- Gossip, Structured or DC-SoC scientific semantics;
- formal Kubernetes topology, run count/repetition count, churn timing or workload pacing;
- ControlSim evidence or interpretation.

Exact K8s experiment protocol remains K4-Q authority.

## K1-Q Result
$$\boxed{\textbf{K1-Q = PASS / CLOSED}}$$

The minimum safe architecture is **inherit the established `ahbn2_gke` runtime, reuse the frozen environment-independent Q-AHBN2 learner/transition core, and add only a Kubernetes-specific adapter plus bounded Q-AHBN2 event-path hooks.**

No implementation, Docker build, deployment, parameter change, experiment or scientific interpretation was performed in K1-Q.

## Next permitted action
$$\boxed{\textbf{K2-Q — GKE Integration / Parity Verification}}$$

K2-Q may now implement the minimum mapped patch and deterministic parity/regression tests. It must remain implementation/parity only: no formal Kubernetes run and no scientific interpretation.
