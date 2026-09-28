# S08 — Formal Exp10-Q: Failure

**Status:** PREPARATION HOLD — FORMAL HARNESS REQUIRED BEFORE HUMAN EXECUTION

## Objective
Execute the frozen Exp10-Q Failure matrix from `docs/03_EXPERIMENT_CONTRACT.md` under the frozen statistical/provenance rules.

## Authoritative inputs
- `docs/03_EXPERIMENT_CONTRACT.md`
- `docs/04_STATISTICAL_CONTRACT.md`
- `docs/02_QAHBN2_DESIGN_FREEZE.md`
- `docs/01_CANONICAL_AHBN_CONTRACT.md`
- S07 = PASS / CLOSED

## Frozen matrix
- topology: BA(100,m=3)
- source: 0
- workload: 1,000 sequential messages per run
- seeds: 42--46
- methods: AHBN, Q-AHBN2
- failure levels: control and one non-source peer failure
- failure onset: immediately before message 501
- failed peer remains unavailable to end of run
- expected formal runs: 20
- Q-AHBN2 learning contract: frozen S02 contract with gamma=0.70

## S08-PREP-1 — Executable Harness Audit — 2026-09-28

### Actions performed
Read-only audit of the current repository found:
- the real ControlSim Q-AHBN2 Learning Validation adapter exists and is already bound to the pinned canonical AHBN commit;
- direct NEW/DUPLICATE attribution, reward closure, same-peer transition semantics and passive decision provenance already exist;
- the repository does **not** yet contain an Exp10-Q formal runner/harness implementing the newly frozen message-index failure schedule and paired AHBN/Q-AHBN2 matrix.

### Scientific decision
Do not ask the researcher to execute a formal run until the exact frozen Exp10-Q harness exists and is regression/smoke verified. Reusing the stationary gamma-sensitivity runner unchanged would violate the Exp10-Q contract because it has no failure event and only executes Q-AHBN2.

The required implementation is an integration-only extension of the existing validated ControlSim path. It must not redesign the learner or canonical AHBN.

### Minimum implementation requirements
The Exp10-Q harness must:
1. use the pinned canonical AHBN checkout guard;
2. implement both frozen AHBN and Q-AHBN2 methods on the same BA(100,m=3) scenario;
3. preserve 1,000 sequential queue-to-exhaustion messages;
4. select the failed non-source peer deterministically from the seed;
5. apply the one-peer failure exactly before message 501 in the failure condition;
6. keep the failure active through run end;
7. use identical scenario generation for paired methods;
8. emit the four primary dissemination metrics for both methods;
9. emit the frozen learning/adaptation fields and passive decision trace for Q-AHBN2;
10. create RUN.md and manifest.json with exact Git/protocol provenance;
11. refuse any matrix other than the frozen 20-cell Exp10-Q matrix;
12. preserve no-result-based rerun/exclusion behavior.

## Result
**S08-PREP-1 = HOLD / IMPLEMENTATION REQUIRED.**

This is not a scientific-design blocker and does not reopen S07-A/S07-B. It is the minimum executable preparation required to translate the already-frozen protocol into code.

## S08-PREP-2 — Implement Exp10-Q Formal Harness + Static Verification — 2026-09-28

**Status:** IMPLEMENTATION COMPLETE / EXECUTION VERIFICATION REQUIRED.

Implemented and GitHub-readback verified:
- `qahbn2/formal_exp10q.py` — frozen Exp10-Q cell executor for canonical AHBN and Q-AHBN2;
- `scripts/run_exp10q_formal.py` — guarded 20-run formal runner with RUN.md, manifest.json, CSV and decision-trace provenance;
- `tests/test_formal_exp10q_contract.py` — exact matrix/failure-target guards.

Static reconciliation confirms the implementation preserves:
- canonical AHBN S5 controller construction;
- pinned canonical AHBN checkout guard inherited from the validated ControlSim loader;
- BA(100,m=3), source 0, 1,000 sequential messages;
- gamma=0.70 and all frozen learning constants;
- deterministic one-non-source-peer failure after message 500 / before message 501;
- AHBN versus Q-AHBN2 only;
- exact seeds 42--46 and 20-cell matrix guard;
- direct-attempt attribution and passive Q decision provenance;
- no change to canonical AHBN source.

GitHub writes and mandatory readbacks completed.

### Verification boundary
The connector environment cannot execute the researcher's local Python/ControlSim checkout. Therefore runtime correctness of the new integration cannot be declared from static inspection alone.

**S08-PREP-2 = NEEDS MANUAL TEST** for the bounded regression/unit execution and deterministic smoke.

## Next permitted task
`S08-PREP-3 — Local Regression + Bounded Exp10-Q Smoke`.

Formal 20-run Exp10-Q execution remains blocked until PREP-3 passes.


## S08-PREP-3 — Local Regression + Bounded Exp10-Q Smoke — 2026-09-28

**Status:** PASS / CLOSED.

### Local execution evidence
Researcher executed PREP-3 from repository commit `b0c5776672ed814334853d930ff83809af5e9c91` with a clean working tree and branch synchronized to `origin/main`.

Regression evidence:
- `PYTHONPATH=. python -m unittest discover -s tests -v`
- 23 tests executed;
- 23 PASS;
- 0 failures / 0 errors.

Dedicated Exp10-Q contract evidence:
- `PYTHONPATH=. python -m unittest tests.test_formal_exp10q_contract -v`
- 3 tests executed;
- exact frozen matrix guard PASS;
- deterministic non-source failed-peer guard PASS;
- matrix-expansion rejection guard PASS.

Bounded deterministic integration smoke:
- condition: failure only;
- methods: AHBN and Q-AHBN2;
- seed: 42 only;
- expected/observed failed peer: 82;
- failure boundary: before message 501;
- both methods completed successfully;
- primary dissemination fields present and valid;
- Q-AHBN2 learning/adaptation fields and passive decision trace present;
- terminal assertion: `S08-PREP-3 bounded smoke: PASS`.

Observed smoke outputs are classified strictly as **pre-formal integration evidence**. They are not part of the formal Exp10-Q dataset and must not be used for inferential or comparative thesis/paper claims.

### Scientific interpretation
PREP-3 establishes runtime executability of the new Exp10-Q integration while preserving the frozen contract. The result does not authorize any scientific redesign, parameter adjustment, matrix change, or result-based rerun rule.

The smoke observation that AHBN and Q-AHBN2 produced different dissemination outcomes is not interpreted scientifically at this gate; the purpose was only runtime/provenance verification.

## Result

**S08-PREP-3 = PASS / CLOSED.**

The preparation hold is cleared. The frozen formal 20-run Exp10-Q matrix may now be executed using `scripts/run_exp10q_formal.py` without modification.

## Next permitted task

`S08-FORMAL-1 — Execute Frozen 20-Run Exp10-Q Failure Matrix`.

Formal outputs remain **raw evidence pending validity/completeness audit** after execution. No interpretation or thesis/paper claim is permitted until that post-run audit closes.


## S08-FORMAL-1 — Execute Frozen 20-Run Exp10-Q Failure Matrix — 2026-09-28

**Status:** EXECUTED / RAW FORMAL EVIDENCE CREATED.

Researcher executed the unchanged guarded formal runner from Q-AHBN2 commit `5b4bdaa800fc0afdf238df3b1c7ecf4b65b7db42`:

`PYTHONPATH=. python scripts/run_exp10q_formal.py`

Generated formal evidence directory:
`q-ahbn-28092026183635-exp10q-formal`

No result-based rerun, exclusion, parameter change, or matrix change was reported.

## S08-FORMAL-2 — Exp10-Q Formal Evidence Integrity / Completeness Audit — 2026-09-28

**Status:** PASS / CLOSED.

### Provenance and artifact audit
Required artifacts are present:
- `RUN.md`;
- `manifest.json`;
- `exp10q_formal.csv`;
- `decision_trace.json`.

Manifest reconciliation:
- environment = ControlSim;
- experiment = Exp10-Q Failure;
- event = formal;
- timestamp = 28092026183635;
- Q-AHBN2 commit = `5b4bdaa800fc0afdf238df3b1c7ecf4b65b7db42`;
- canonical AHBN commit = `936a79480bc1252c79b6ee01f65c88c740af2844`;
- expected/completed runs = 20/20;
- gamma = 0.70;
- exclusions = none;
- reruns = none.

### Frozen-matrix integrity
CSV audit confirms:
- rows = 20;
- unique cells = 20;
- duplicate cells = 0;
- conditions exactly `control, failure`;
- methods exactly `ahbn, qahbn2`;
- seeds exactly 42--46.

Failure-condition pairing is preserved for both methods:
- seed 42 -> failed peer 82;
- seed 43 -> failed peer 5;
- seed 44 -> failed peer 53;
- seed 45 -> failed peer 35;
- seed 46 -> failed peer 10.

All failure cells record failure before message 501. Control cells correctly contain no failed peer and no failure boundary.

### Decision-trace integrity
Q-AHBN2 decision trace contains exactly 10 groups: one for each Q-AHBN2 condition/seed cell (2 conditions x 5 seeds). All groups contain non-empty decision records.

### Scientific boundary
This gate establishes structural completeness, pairing, provenance, and frozen-protocol compliance only. It does not evaluate whether AHBN or Q-AHBN2 performed better and does not authorize selective reruns. Numerical scientific interpretation remains a separate controlled gate under the frozen statistical contract.

## Result

**S08-FORMAL-2 = PASS / CLOSED.**

The Exp10-Q formal dataset is structurally complete and eligible for frozen-contract analysis. The raw evidence directory must be preserved unchanged.

## Next permitted task

`S08-FORMAL-3 — Exp10-Q Frozen Statistical Analysis + Claim-Boundary Audit`.

Analysis must use only the predeclared metrics, seed pairing, uncertainty rules, and interpretation boundaries in `docs/04_STATISTICAL_CONTRACT.md`. No parameter tuning, result-based rerun, metric invention, or post-hoc test shopping is permitted.
