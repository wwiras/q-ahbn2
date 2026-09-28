# K4-Q — K8s-VAL-Q / Exp13-Q-K8s Protocol Freeze

**Status:** PENDING / NOT RELEASED

## Objective
Prospectively freeze the minimum bounded Kubernetes validation matrix only after K0-Q through K3-Q establish implementation readiness.

## Required two-part scope

### A. K8s-VAL-Q deployment validation
Freeze the minimum AHBN-versus-Q-AHBN2 deployment-validation comparison under one pre-existing dynamic condition.

### B. Exp13-Q-K8s matched reference benchmark
Freeze one five-method Kubernetes reference-benchmark arm using exactly:

- Gossip
- Structured
- DC-SoC
- AHBN
- Q-AHBN2

This arm must be the closest implementation-valid Kubernetes counterpart of the already frozen Exp13-Q-Sim high-churn scenario. Match the frozen scenario semantics, topology intent, source, churn schedule, seeds 42--46 and principal metrics as closely as technically valid. Any Kubernetes-native deviation must be explicit, technically justified and documented before outcomes are inspected.

## Freeze requirements
K4-Q must prospectively fix:

- exact Kubernetes topology realization;
- source;
- churn target/schedule realization;
- workload/message pacing;
- method implementations and comparator provenance;
- Q-AHBN2 frozen parameters;
- seed mapping;
- repetition/run structure;
- metric collection;
- pairing rules where applicable;
- container/image/Git provenance;
- exclusion/rerun rules;
- exact distinction between matched cross-environment benchmarking and literal replication.

## Boundary
No ControlSim-result-driven condition selection, parameter tuning, comparator redesign or post-hoc protocol change. The exact repetition/run structure remains intentionally unfrozen until this gate and must be fixed before any K8s formal outcome is inspected.

Exp10-Q, Exp11-Q, Exp12-Q and Exp13-Q-Sim remain untouched and frozen.
