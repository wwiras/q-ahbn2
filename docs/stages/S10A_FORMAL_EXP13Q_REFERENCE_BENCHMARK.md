# S10A — Formal Exp13-Q: Reference Benchmark

**Status:** S10A-VERIFY STATIC + REGRESSION PASS; SMOKE IMPLEMENTED / LOCAL EXECUTION PENDING; FORMAL BLOCKED

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

## S10A-IMPL — Minimal Five-Method Exp13-Q Harness Implementation

**Mode:** bounded implementation only. No smoke run, no formal run, no performance interpretation, no parameter change.

### Files added
- `qahbn2/formal_exp13q.py`
- `tests/test_formal_exp13q_contract.py`

### Implemented boundaries
- exact frozen method set: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2;
- exact seeds: 42--46;
- exact churn level: 0.40;
- exact Exp11-Q leave/rejoin boundaries reused;
- exact 25-cell matrix enforced;
- canonical standalone Gossip uses `fanout=None`;
- canonical standalone Structured uses unbounded structural `ClusterStrategy()`;
- canonical DC-SoC uses `DCSOCStrategy` with frozen DBSCAN parameters `eps=2.0`, `min_samples=3`;
- AHBN and Q-AHBN2 directly reuse the validated Exp11-Q high-churn paths;
- all comparator methods reuse the same seeded BA topology and deterministic churn schedule;
- no AHBN/Q-AHBN2 scientific semantics were modified.

### Verification status
Implementation files were written to GitHub and read back. Runtime regression/smoke execution has **not** been performed in this gate.

### S10A-IMPL result
**PASS / CLOSED for code implementation only.**

Formal execution remains blocked.

## S10A-VERIFY — Exp13-Q Static Contract / Regression / Bounded Smoke Verification

### Objective
Verify the exact frozen Exp13-Q matrix, canonical comparator semantics, common seeded topology/churn schedule, project regression safety, and one bounded smoke path before formal execution is released.

### Reconciliation and static verification
Following `docs/00_QAHBN2_MASTER.md`:
1. fetched GitHub authority and current S10A stage;
2. reconciled current gate against Master and experiment contract;
3. inspected the designated Google Drive project root and confirmed the synchronized workspace structure exists;
4. rechecked pinned canonical comparator implementations;
5. strengthened the Exp13-Q contract test with exact Exp11 high-churn schedule parity/determinism checks;
6. performed GitHub post-write readback.

Static findings:
- frozen matrix remains exactly 25 cells;
- churn remains exactly 0.40;
- seeds remain 42--46;
- leave/rejoin boundaries remain 201/251, 401/451, 601/651, 801/851;
- the deterministic churn schedule is imported directly from Exp11-Q;
- source peer 0 is excluded from churn targets;
- expected churn target count is 40 of 99 non-source peers for each cycle;
- Gossip standalone semantics match pinned canonical `GossipStrategy(fanout=None)`;
- Structured standalone semantics match pinned canonical `ClusterStrategy()`;
- DC-SoC uses pinned canonical `DCSOCStrategy` with `eps=2.0`, `min_samples=3`;
- AHBN and Q-AHBN2 remain direct reuse of the validated Exp11-Q high-churn paths.

### Runtime verification boundary
Per Master §5.3 and §9.5, executable regression/smoke tests are researcher-run from the designated local synchronized workspace. No runtime PASS may be declared until the local command output is returned and verified.

### Required local commands
Run from:

`/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`

```bash
git pull
git status
git rev-parse HEAD
PYTHONPATH=. python -m unittest tests.test_formal_exp13q_contract -v
PYTHONPATH=. python -m unittest discover -s tests -v
```

After those pass, the bounded smoke command will be released separately so the smoke remains intentionally small and non-formal.

### Regression verification
Researcher executed the full project regression suite from the designated local synchronized workspace after confirming canonical dependency loading. Result:

```text
Ran 37 tests in 2.523s

OK
```

This includes the complete existing project suite plus the Exp13-Q contract checks. No regression failure, assertion failure, scientific-contract violation, or canonical-AHBN breakage was observed.

The earlier interrupted run is classified as an operational interruption during dependency import, not as a failed test. A bounded canonical-load diagnostic subsequently completed successfully with `CANONICAL_LOAD_PASS`.

### Current S10A-VERIFY result
**STATIC + REGRESSION PASS.**

No formal run is authorized yet. The remaining verification requirement is one bounded, non-formal five-method Exp13-Q smoke execution. No statistical interpretation is authorized.

### S10A-VERIFY-SMOKE-IMPL — Minimal Non-Formal Five-Method Smoke Path

**Mode:** bounded smoke implementation only; local execution remains researcher-run.

Implementation:
- added `scripts/run_exp13q_smoke.py`;
- added `tests/test_exp13q_smoke_contract.py`;
- smoke seed is exactly 42;
- all five frozen methods are exercised;
- workload is bounded to messages 1--260 only;
- this crosses exactly the first frozen leave/rejoin pair: leave before 201 and rejoin before 251;
- the next formal churn onset at 401 is not reached;
- the smoke calls the real Exp13-Q method paths and canonical comparator implementations;
- the 1,000-message formal path/defaults are not modified;
- Q-AHBN2 decision tracing is disabled only for smoke artifact size; learning/runtime behavior is otherwise the real path;
- each method must report the exact first leave/rejoin cycle and 40 churn targets or the smoke fails;
- output is written under `output/evidence/q-ahbn-<timestamp>-exp13q-smoke/`;
- the artifact explicitly records `formal_performance_evidence: false`.

**Result:** implementation complete; executable smoke PASS is not yet claimed.

### Required local smoke command
After pulling the latest GitHub state, run from the repository root:

```bash
git pull
git status
git rev-parse HEAD
PYTHONPATH=. python -m unittest tests.test_exp13q_smoke_contract -v
PYTHONPATH=. python scripts/run_exp13q_smoke.py
```

Return the complete terminal output and generated smoke directory path for verification. Formal Exp13-Q remains blocked until that evidence is checked.

## Statistical boundary
Use the Exp13-Q amendment in `docs/04_STATISTICAL_CONTRACT.md`. No omnibus winner score, post-hoc test shopping, or universal-superiority claim.

## Next permitted task
`S10A-VERIFY-SMOKE — Bounded Five-Method Exp13-Q Smoke`.

The smoke must remain non-formal and intentionally small. It is limited to runtime integration verification of the five frozen methods, common scenario/churn handling, and canonical comparator execution. No tuning, redesign, formal aggregation, or scientific interpretation is permitted.

**S11 remains blocked until Exp13-Q formal evidence is completed, integrity-verified, and frozen.**
