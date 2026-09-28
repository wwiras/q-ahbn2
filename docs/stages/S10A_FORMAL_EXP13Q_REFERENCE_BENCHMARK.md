# S10A — Formal Exp13-Q: Reference Benchmark

**Status:** FROZEN DESIGN / EXECUTION NOT YET RELEASED

## Objective
Provide one bounded external reference benchmark for standalone Q-AHBN2 publication positioning without replacing or expanding the primary thesis RO4 causal matrix.

## Scientific role
- Exp10-Q / Exp11-Q / Exp12-Q remain the primary AHBN-versus-Q-AHBN2 RO4/RQ4 evidence.
- Exp13-Q is external reference positioning only.
- K8s-VAL-Q remains separate deployment validation.

## Frozen matrix
- scenario: churn = 0.40;
- topology: BA(100,m=3);
- source: peer 0;
- workload: 1,000 sequential messages, queue-to-exhaustion;
- churn cycles: before messages 201, 401, 601, 801;
- rejoin: after 50 subsequent messages per cycle;
- seeds: 42--46;
- methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2;
- expected runs: 25.

## Comparator provenance
Gossip, Structured, DC-SoC and AHBN are inherited from the established pinned canonical AHBN/RO2 comparator lineage. Q-AHBN2 uses the frozen S02 learning contract above canonical AHBN.

## Execution boundary
No formal execution is authorized by this file alone. Before Exp13-Q formal execution, create and verify the minimum dedicated five-method churn harness under a bounded preparation gate. The harness must preserve comparator semantics, exact schedule, common seeded scenario generation, output provenance and the frozen Q-AHBN2 design.

No comparator, severity, seed, topology, reward or learning-parameter change is permitted in response to future formal results.

## Statistical boundary
Use the Exp13-Q amendment in `docs/04_STATISTICAL_CONTRACT.md`. No omnibus winner score, post-hoc test shopping, or universal-superiority claim.

## Next permitted task
The immediate project task after S07-D is still `S08-PREP-3 — Local Regression + Bounded Exp10-Q Smoke`. This Exp13-Q stage remains frozen/pending until the primary formal sequence reaches it.
