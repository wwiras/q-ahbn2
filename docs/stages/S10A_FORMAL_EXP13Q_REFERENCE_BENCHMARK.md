# S10A — Formal Exp13-Q: Reference Benchmark

**Status:** S10A-VERIFY PASS / CLOSED; S10A-RELEASE PASS / CLOSED; FORMAL EXECUTION RELEASED

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

**Result:** implementation complete.

### S10A-VERIFY-SMOKE — Researcher Runtime Evidence

Researcher executed the released bounded smoke from the synchronized local workspace at GitHub HEAD:

`da2b9e641638b750388afd45ac8e7faa14061cbd`

Preconditions:
- branch `main` synchronized with `origin/main`;
- working tree clean;
- smoke contract tests: 2/2 PASS.

Generated non-formal smoke directory:

`output/evidence/q-ahbn-29092026080825-exp13q-smoke`

Observed runtime integration results:
- Gossip: PASS; leave=201, rejoin=251, churn targets=40;
- Structured: PASS; leave=201, rejoin=251, churn targets=40;
- DC-SoC: PASS; leave=201, rejoin=251, churn targets=40;
- AHBN: PASS; leave=201, rejoin=251, churn targets=40;
- Q-AHBN2: PASS; leave=201, rejoin=251, churn targets=40;
- terminal marker: `EXP13Q_BOUNDED_SMOKE_PASS`.

This is non-formal integration evidence only. No performance comparison, statistical inference, tuning, redesign, or formal result interpretation is permitted from this smoke artifact.

### S10A-VERIFY result

**PASS / CLOSED.**

S10A-VERIFY has now satisfied:
- static contract verification;
- full project regression verification;
- bounded five-method runtime smoke verification.

No scientific parameter, comparator, topology, seed, learning rule, AHBN behavior, or formal workload was changed during verification.

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


## NEXT GATE RECONCILIATION — 2026-09-29

### Authority reconciled
Reconciled against:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/03_EXPERIMENT_CONTRACT.md`;
- `docs/04_STATISTICAL_CONTRACT.md`;
- prior formal-stage execution patterns in S09 and S10;
- current S10A implementation/verification state.

### Finding
No new scientific design, comparator, parameter, seed, scenario, metric, or statistical gate is required. The Exp13-Q scientific contract is already prospectively frozen by S07-D, and S10A static/regression/smoke verification is PASS / CLOSED.

However, formal execution must not begin yet because the project-wide GitHub-first workflow requires the formal execution path and provenance/output guard to be fixed and audited before researcher execution. Unlike Exp11-Q and Exp12-Q, the current repository has no dedicated guarded `scripts/run_exp13q_formal.py` formal runner recorded in S10A.

### Next controlled gate
`S10A-RELEASE — Exp13-Q Formal Runner / Provenance Readiness and Release Audit`.

This is an implementation/readiness gate only. It must:
- add or verify the minimum guarded Exp13-Q formal runner;
- enforce the exact 25-cell matrix;
- preserve the frozen five methods, seeds 42--46, churn=0.40 and 1,000-message workload;
- write only under `output/evidence/`;
- record Q-AHBN2 commit and pinned canonical AHBN commit;
- record expected/completed runs, exclusions and reruns;
- preserve required primary metrics and Q-AHBN2 trace/provenance;
- make no scientific parameter or comparator change;
- perform GitHub readback and local release checks before authorizing formal execution.

Formal execution remains blocked until S10A-RELEASE passes.


## S10A-RELEASE — Exp13-Q Formal Runner / Provenance Readiness and Release Audit

**Mode:** operational/provenance release only. No formal execution, no statistical interpretation, no scientific redesign.

### Implementation completed
Added:
- `scripts/run_exp13q_formal.py`;
- `tests/test_exp13q_formal_release.py`.

The guarded runner:
- validates the exact frozen 25-cell matrix before execution;
- uses only `run_exp13q_cell(...)` from the frozen Exp13-Q harness;
- preserves methods Gossip, Structured, DC-SoC, AHBN and Q-AHBN2;
- preserves seeds 42--46, churn=0.40 and the 1,000-message formal workload;
- writes only beneath `output/`, defaulting to `output/evidence/q-ahbn-<timestamp>-exp13q-formal/`;
- refuses to overwrite an existing run directory;
- records the producing Q-AHBN2 Git commit and pinned canonical AHBN commit;
- records exact methods, seeds, topology/workload, churn boundaries, expected/completed run counts, exclusions and reruns;
- writes `exp13q_formal.csv`, `decision_trace.json`, `manifest.json`, and `RUN.md`;
- enforces same-seed churn-schedule identity across all five methods;
- preserves Q-AHBN2 decision trace/provenance;
- makes no scientific parameter, comparator, topology, learning, reward or statistical change.

Release-contract tests statically guard the pinned canonical commit, exact 25-cell matrix, frozen methods/seeds/churn, 1,000-message workload, output-directory guard, exclusions/reruns fields, and use of the frozen Exp13-Q cell executor only.

### Local release-check evidence

Researcher executed the released checks from the synchronized local workspace at GitHub HEAD:

`f1d66329544230bea67757a61dd9eec71448f070`

Repository preconditions:
- branch `main` synchronized with `origin/main`;
- working tree clean.

Release-specific checks:
- `tests.test_exp13q_formal_release`: **3/3 PASS**;
- combined Exp13 contract/smoke checks: **7/7 PASS**;
- complete project regression suite: **42/42 PASS**.

No test failure, regression, frozen-matrix violation, provenance-guard failure, output-path violation, or unauthorized executor path was observed.

### Current result
**S10A-RELEASE = PASS / CLOSED.**

The guarded formal runner and provenance controls are verified. The exact 25-run Exp13-Q formal matrix is now operationally released for researcher execution under the frozen contract.

No formal result has yet been generated or interpreted at this gate.

### Formal execution release

Formal execution is now authorized only through the guarded runner:

```bash
PYTHONPATH=. python scripts/run_exp13q_formal.py
```

Execution rules:
- no tuning or parameter modification;
- no comparator modification;
- no seed/topology/scenario change;
- no selective rerun based on performance;
- no interpretation or aggregation during execution;
- any interruption or anomaly must be classified first as a runtime/validity issue;
- generated output remains raw formal evidence pending integrity/completeness audit.

## Statistical boundary
Use the Exp13-Q amendment in `docs/04_STATISTICAL_CONTRACT.md`. No omnibus winner score, post-hoc test shopping, or universal-superiority claim.

## Next permitted task
`S10A-FORMAL — Execute Frozen 25-Run Exp13-Q Reference Benchmark Matrix`.

Only the guarded formal runner is authorized. After completion, raw evidence must proceed to integrity/completeness audit before interpretation or aggregation.

**S11 remains blocked until Exp13-Q formal evidence is completed, integrity-verified, and frozen.**
