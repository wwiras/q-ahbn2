# K0-Q — Kubernetes Scope Reconciliation

**Status:** NEXT / RELEASED — READ-ONLY RECONCILIATION

## Objective
Reconcile the authoritative canonical AHBN-GKE lineage, historical Q-AHBN-GKE implementation history, frozen Q-AHBN2 logical design, current Kubernetes environment, and the prospective Exp13-Q-K8s matched reference-benchmark requirement before any new deployment implementation.

## Prospective scope authority
Kubernetes now has two distinct scientific roles:

1. **K8s-VAL-Q deployment validation:** frozen AHBN versus frozen Q-AHBN2.
2. **Exp13-Q-K8s matched reference benchmark:** Gossip, Structured, DC-SoC, AHBN and Q-AHBN2, corresponding to the frozen Exp13-Q-Sim comparator family in support of RO1 cross-environment evaluation.

The Exp13-Q-K8s arm must be established independently of observed ControlSim performance and must not be used to reopen Exp10-Q, Exp11-Q, Exp12-Q or Exp13-Q-Sim.

## Boundary
Read-only audit first. Freeze only the logical invariants and comparator semantics that must survive deployment. No ControlSim result may be used to redesign Q-AHBN2, alter a comparator, or select a favorable Kubernetes outcome. No K8s formal outcome is authorized by K0-Q.


## Release basis
Released after S11-A and S11-B aggregation closure on 2026-09-29. The frozen Master stage map places K0-Q immediately after S11 and before S12 interpretation.

## Next permitted task
Perform read-only reconciliation of the authoritative canonical AHBN-GKE lineage, historical Q-AHBN-GKE implementation history, frozen Q-AHBN2 logical contract, current Kubernetes implementation/environment, and prospective Exp13-Q-K8s matched five-method benchmark requirement. No implementation change, deployment execution, parameter change, or interpretation is authorized in K0-Q.


## K0-Q Reconciliation Findings — 2026-09-29

### 1. Authoritative deployment lineage
- Canonical Kubernetes/GKE authority is `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`, as already frozen in `docs/00_SOURCE_AUTHORITY_REGISTER.md`.
- Historical Kubernetes Q-learning authority is `wwiras/q-ahbn_gke@a9af5ccb9b564d5f2c2daaeeb9a04b191780cdbe` and remains historical context only.
- Current Q-AHBN2 code/control authority remains `wwiras/q-ahbn2`.

### 2. Comparator inheritance decision
The existing `ahbn2_gke` implementation is to be reused rather than recreated for:
- Gossip;
- Structured (runtime label `cluster`);
- DC-SoC;
- canonical AHBN, including the later frozen S5 requested-fanout runtime layer.

These four deployment methods are inherited as the established AHBN Scientific Reports comparator/runtime lineage. K1-Q must not reimplement them from scratch or alter their scientific semantics merely to integrate Q-AHBN2.

### 3. Q-AHBN2 patch boundary
Only the new Q-AHBN2 learning/refinement layer is to be patched into the inherited `ahbn2_gke` event path for current work. The patch must preserve:
- canonical AHBN observations and environment-specific Kubernetes acquisition semantics;
- AHBN-first proposal generation;
- frozen Q-AHBN2 81-state representation;
- five actions: KEEP, FANOUT_DOWN, FANOUT_UP, SET_GOSSIP, SET_STRUCTURED;
- frozen reward attribution over NEW/DUPLICATE/FAILED with F=0 => no update;
- frozen learning parameters alpha_Q=0.25, gamma=0.70, epsilon_0=0.30, epsilon_min=0.03, lambda=0.995;
- canonical requested-versus-realized fanout distinction and eligible-neighbour constraints;
- no controller bypass or historical hard-coded failure reaction.

Historical `q-ahbn_gke` code may inform integration mechanics only. Its historical state, action effects, reward, hard-coded recovery behavior, and non-canonical realization path must not be inherited when they conflict with the frozen Q-AHBN2 contract.

### 4. Established ahbn2_gke evidence relevant to reuse
Read-only audit confirms the pinned repository already contains isolated deployment paths and prior verification records for:
- standalone Gossip with no AHBN/Structured/DC-SoC decision leakage;
- native Structured cluster-head/member/gateway forwarding;
- DC-SoC static structural forwarding and dynamic maintenance;
- canonical AHBN observations, controller dispatch, and later S5 runtime realization;
- multi-method churn harness lineage over Gossip, Structured, DC-SoC and AHBN.

Accordingly, the scientific and engineering baseline for K1-Q is inheritance plus bounded integration, not greenfield Kubernetes implementation.

### 5. Prospective two-part Kubernetes scope
The already-frozen future Kubernetes scope remains:
1. **K8s-VAL-Q:** AHBN versus Q-AHBN2 deployment validation.
2. **Exp13-Q-K8s:** one matched five-method reference arm using Gossip, Structured, DC-SoC, AHBN and Q-AHBN2.

K0-Q does not freeze the exact Kubernetes run/repetition structure or implementation-required scenario deviations. Those remain owned by K4-Q after K1-Q through K3-Q establish implementation readiness.

### 6. No-change confirmation
K0-Q performed read-only reconciliation only:
- no comparator implementation changed;
- no Q-AHBN2 code patched yet;
- no parameter changed;
- no deployment or Docker action executed;
- no formal Kubernetes result inspected or produced;
- no ControlSim result used to redesign or retune the Kubernetes protocol.

## Result
$$\boxed{\textbf{K0-Q = PASS / CLOSED}}$$

The authoritative deployment baseline is `ahbn2_gke`; current Q-AHBN2 work must patch only the frozen Q-AHBN2 learning layer onto that established runtime while preserving the four existing method implementations.

## Next permitted action
$$\boxed{\textbf{K1-Q — Q-AHBN2 GKE Design-to-Code Mapping}}$$

K1-Q is mapping/audit first. It must identify the exact inherited `ahbn2_gke` files/event boundaries and the minimum `q-ahbn2` patch surface for Q-AHBN2 integration before any code modification.
