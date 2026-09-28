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
