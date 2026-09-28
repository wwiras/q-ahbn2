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

## Next permitted task
`S08-PREP-2 — Implement Exp10-Q Formal Harness + Static/Unit Verification`.

No formal experiment is authorized until PREP-2 and the subsequent deterministic smoke/protocol audit pass.
