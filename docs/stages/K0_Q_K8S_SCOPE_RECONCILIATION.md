# K0-Q — Kubernetes Scope Reconciliation

**Status:** PENDING / NOT RELEASED

## Objective
Reconcile the authoritative canonical AHBN-GKE lineage, historical Q-AHBN-GKE implementation history, frozen Q-AHBN2 logical design, current Kubernetes environment, and the prospective Exp13-Q-K8s matched reference-benchmark requirement before any new deployment implementation.

## Prospective scope authority
Kubernetes now has two distinct scientific roles:

1. **K8s-VAL-Q deployment validation:** frozen AHBN versus frozen Q-AHBN2.
2. **Exp13-Q-K8s matched reference benchmark:** Gossip, Structured, DC-SoC, AHBN and Q-AHBN2, corresponding to the frozen Exp13-Q-Sim comparator family in support of RO1 cross-environment evaluation.

The Exp13-Q-K8s arm must be established independently of observed ControlSim performance and must not be used to reopen Exp10-Q, Exp11-Q, Exp12-Q or Exp13-Q-Sim.

## Boundary
Read-only audit first. Freeze only the logical invariants and comparator semantics that must survive deployment. No ControlSim result may be used to redesign Q-AHBN2, alter a comparator, or select a favorable Kubernetes outcome. No K8s formal outcome is authorized by K0-Q.
