# K6-Q — Kubernetes Evidence Integrity / Freeze

**Status:** PENDING / NOT RELEASED

## Objective
Audit completeness, validity and provenance of both K8s-VAL-Q and Exp13-Q-K8s evidence and deliberately preserve verified artifacts.

## Required provenance families
Manifests, image/container provenance, Git commit, topology, source, event/churn schedule, workload timing, metrics, learning traces where applicable, comparator identity, Kubernetes metadata, seed/repetition mapping, exclusions/failures and exact K4-Q protocol version.

## Evidence-role separation
- K8s-VAL-Q evidence supports bounded AHBN-versus-Q-AHBN2 deployment validation.
- Exp13-Q-K8s evidence supports a matched five-method cloud-native reference benchmark corresponding to Exp13-Q-Sim.
- Cross-environment comparison must not be labelled literal replication unless later parity/equivalence evidence supports that stronger description.

## Boundary
Only verified frozen deployment evidence may proceed to interpretation and claim reconciliation. K6-Q does not reopen Exp10-Q, Exp11-Q, Exp12-Q or Exp13-Q-Sim.
