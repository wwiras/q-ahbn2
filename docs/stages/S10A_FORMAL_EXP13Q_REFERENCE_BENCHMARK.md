# S10A — Formal Exp13-Q: Reference Benchmark

**Status:** S10A-PREP PASS / CLOSED; FROZEN DESIGN; IMPLEMENTATION NOT YET RELEASED

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
No formal execution is authorized by this file alone. Before Exp13-Q formal execution, create and verify the minimum dedicated five-method churn harness under bounded preparation, regression, and smoke gates. The harness must preserve comparator semantics, exact schedule, common seeded scenario generation, output provenance and the frozen Q-AHBN2 design.

No comparator, severity, seed, topology, reward or learning-parameter change is permitted in response to formal Exp10-Q / Exp11-Q / Exp12-Q results or future Exp13-Q results.

## S10A-PREP — Frozen Contract-to-Harness Reconciliation

**Mode:** read-only implementation/provenance reconciliation. No code change, no simulation, no smoke run, no formal run, no statistical interpretation.

### Authoritative inputs
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`
- `docs/01_CANONICAL_AHBN_CONTRACT.md`
- `docs/02_QAHBN2_DESIGN_FREEZE.md`
- `docs/03_EXPERIMENT_CONTRACT.md`
- `docs/04_STATISTICAL_CONTRACT.md`
- `docs/stages/S09_FORMAL_EXP11Q.md`
- `qahbn2/formal_exp11q.py`
- pinned canonical ControlSim AHBN: `wwiras/ahbn@936a79480bc1252c79b6ee01f65c88c740af2844`

### Reconciliation findings
1. **Scenario and churn schedule reuse = DIRECT.**
   - Exp13-Q uses the exact frozen Exp11-Q high-churn condition: `churn=0.40`.
   - `qahbn2/formal_exp11q.py` already implements the frozen leave/rejoin boundaries:
     - leave before messages 201, 401, 601, 801;
     - rejoin before messages 251, 451, 651, 851;
     - deterministic seed-specific target schedules;
     - BA(100,m=3), source 0, 1,000 sequential queue-to-exhaustion messages.
   - This schedule should be reused, not re-derived or modified.

2. **AHBN path reuse = DIRECT.**
   - The validated Exp11-Q AHBN execution path uses canonical `AHBNStrategy(default_fanout=3, adaptive_fanout=True)` with the frozen S5 controller.
   - No AHBN controller, normalization, EWMA, mode, fanout, eligible-neighbour or realization behavior may be altered.

3. **Q-AHBN2 path reuse = DIRECT.**
   - The validated Exp11-Q Q-AHBN2 path already provides the frozen learner, adapter, direct-attempt reward attribution, decision trace, action distribution and terminal bookkeeping required by S02/S03.
   - Exp13-Q must reuse this path unchanged for the Q-AHBN2 method.

4. **Gossip comparator mapping = CANONICAL REUSE REQUIRED.**
   - The pinned canonical AHBN repository provides standalone `GossipStrategy` semantics.
   - Standalone Gossip uses no AHBN controller; with `fanout=None` it forwards to all eligible active physical neighbours while excluding the immediate sender.
   - Exp13-Q must reuse the canonical comparator semantics rather than the bounded Gossip helper used internally by Q-AHBN2 action realization.

5. **Structured comparator mapping = CANONICAL REUSE REQUIRED.**
   - The pinned canonical AHBN repository provides standalone `ClusterStrategy` semantics.
   - Standalone Structured uses no AHBN controller and no numeric fanout budget; members forward toward the cluster head and cluster heads preserve their structural local/gateway obligations.
   - Exp13-Q must reuse these standalone comparator semantics, not Q-AHBN2's bounded structured realization.

6. **DC-SoC comparator mapping = CANONICAL REUSE REQUIRED.**
   - No standalone DC-SoC implementation exists in the current q-ahbn2 source tree.
   - The pinned canonical AHBN repository contains `DCSOCStrategy` plus the established DBSCAN-derived cluster/core/master construction and churn lifecycle handling.
   - The canonical simulator handles DC-SoC leave/rejoin through its specific repair/reinstate/recovery path.
   - Therefore the Exp13 harness must integrate/reuse that pinned canonical DC-SoC implementation and must not reimplement or simplify DC-SoC from memory.

7. **Common seeded scenario requirement = REQUIRED.**
   - All five methods must use the same frozen topology seed and the same deterministic churn target schedule for each seed.
   - The harness must record enough provenance to verify this equality across the five methods.

8. **Metrics/provenance = MINIMUM FROZEN SET.**
   - Required primary metrics remain `delivery_ratio`, `propagation_delay`, `duplicates`, and `total_forwards`.
   - Q-AHBN2 retains its frozen learning/action evidence.
   - The formal runner must preserve exact method, seed, churn schedule/targets, producing Q-AHBN2 commit, canonical AHBN commit, exclusions/reruns, and expected/completed run counts.

### Minimum implementation delta
The next implementation gate should add only the minimum dedicated Exp13-Q harness required to:
- instantiate the five frozen methods;
- reuse the Exp11-Q high-churn schedule;
- build identical seeded BA topology/churn schedules per method/seed;
- use canonical standalone Gossip/Structured/DC-SoC semantics;
- reuse validated AHBN and Q-AHBN2 paths;
- validate the exact 25-cell matrix;
- preserve common-scenario provenance;
- produce formal-compatible output under `output/`.

No shared scientific component needs redesign.

### S10A-PREP result
**PASS / CLOSED.**

The frozen Exp13-Q contract maps cleanly onto existing validated components. The only substantive harness addition is integration of the three standalone canonical reference comparators into the existing Exp11-Q high-churn scenario path, with DC-SoC requiring its canonical structural/churn lifecycle support. This is an implementation/integration task, not a scientific redesign.

No code was changed and no experiment was executed during S10A-PREP.

## Statistical boundary
Use the Exp13-Q amendment in `docs/04_STATISTICAL_CONTRACT.md`. No omnibus winner score, post-hoc test shopping, or universal-superiority claim.

## Next permitted task
`S10A-IMPL — Minimal Five-Method Exp13-Q Harness Implementation`.

Implementation must remain bounded to the reconciliation above. After implementation, the harness must pass exact frozen-matrix/static contract tests and bounded regression/smoke verification before formal execution is released.

**S11 remains blocked until Exp13-Q formal evidence is completed, integrity-verified, and frozen.**
