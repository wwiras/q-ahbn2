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


## S08-FORMAL-3 — Exp10-Q Frozen Statistical Analysis + Claim-Boundary Audit — 2026-09-28

**Status:** PASS / CLOSED.

### Analysis provenance
The preserved 20-row formal CSV from `q-ahbn-28092026183635-exp10q-formal` was analyzed under the prospectively frozen `docs/04_STATISTICAL_CONTRACT.md`. Control and failure were kept separate; seed was the pairing factor; n=5 per method/condition; method means used sample SD and two-sided 95% Student-t CIs; paired effects used Q-AHBN2 minus AHBN with df=4. No p-value search, composite score, rerun, exclusion, tuning, or new metric was introduced.

Machine-readable local analysis artifact:
`q-ahbn-28092026183635-exp10q-formal-analysis/exp10q_formal_analysis.json`.

### Principal failure-condition result
Under one deterministic non-source peer failure before message 501:
- delivery ratio: AHBN mean 0.733514; Q-AHBN2 mean 0.862580; paired mean difference +0.129066 = +12.907 percentage points; 95% CI [+0.072732,+0.185400]; all five seed differences positive;
- propagation delay: AHBN mean 15.873730; Q-AHBN2 mean 10.041353; paired mean difference -5.832377; 95% CI [-7.476635,-4.188118]; all five seed differences negative;
- duplicates: AHBN mean 110284.2; Q-AHBN2 mean 139082.2; paired mean difference +28798.0; 95% CI [+17548.1,+40047.9]; all five seed differences positive;
- total forwards: AHBN mean 182635.6; Q-AHBN2 mean 224340.2; paired mean difference +41704.6; 95% CI [+24914.1,+58495.1]; all five seed differences positive.

Thus the frozen failure evidence supports a condition-specific trade-off: Q-AHBN2 increased delivery and reduced propagation delay relative to AHBN, while using more duplicate transmissions and forwarding effort. The four predeclared outcomes do not support an omnibus winner/superiority statement.

### Contemporaneous control result
The zero-failure control shows the same directional trade-off:
- delivery paired mean difference +0.133472 (+13.347 percentage points), 95% CI [+0.063137,+0.203807];
- delay paired mean difference -5.977232, 95% CI [-7.978592,-3.975872];
- duplicates paired mean difference +29983.2, 95% CI [+16016.5,+43949.9];
- total forwards paired mean difference +43330.4, 95% CI [+22462.1,+64198.7].

This control is contextual harness evidence and is not substituted for the principal dynamic failure cell.

### Learning/adaptation evidence
For Q-AHBN2 under failure:
- mean reward = -0.262131, 95% CI [-0.276598,-0.247665];
- cumulative reward = -22595.233, 95% CI [-24666.904,-20523.562];
- Q updates mean = 86122.0, 95% CI [82121.964,90122.036];
- state-action coverage mean = 0.077037, 95% CI [0.074472,0.079602];
- intervention count mean = 69245.6; KEEP count mean = 17012.4.

Aggregated failure-condition action proportions were KEEP 0.197227, FANOUT_DOWN 0.199583, FANOUT_UP 0.192921, SET_GOSSIP 0.389511, SET_STRUCTURED 0.020759. These are mechanistic descriptors only. Negative reward does not by itself invalidate the dissemination effects, and the bounded evidence does not establish Q-learning convergence, policy optimality, or a composite Adaptation Efficiency result.

### Claim boundary
Exp10-Q now supports only the following condition-specific statement: under the frozen ControlSim one-peer failure condition and five paired seeds, Q-AHBN2 showed higher delivery and lower propagation delay than frozen AHBN, accompanied by higher duplicate and forwarding overhead, with the reported paired 95% CIs.

Not supported by Exp10-Q alone:
- universal or overall superiority of Q-AHBN2;
- lower communication overhead;
- Q-learning convergence or policy optimality;
- robustness under churn or heterogeneity;
- superiority to Gossip, Structured, DC-SoC, or legacy Q-AHBN;
- Kubernetes/deployment benefit;
- a composite Adaptation Efficiency claim.

## Result

**S08-FORMAL-3 = PASS / CLOSED.**

Exp10-Q is a complete, valid formal dataset with a scientifically interpretable delivery/latency versus communication-overhead trade-off. No corrective rerun or design change is justified by the observed performance.

## Next controlled gate

`S08-CLOSE — Exp10-Q Evidence Freeze / Promotion and Stage Closure`.

This closure gate should preserve the raw formal directory and deterministic analysis artifact, reconcile claim/evidence status, and promote the verified evidence under the existing evidence-management rules before proceeding to S09 Exp11-Q preparation.
