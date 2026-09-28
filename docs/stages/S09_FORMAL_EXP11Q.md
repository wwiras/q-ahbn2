# S09 — Formal Exp11-Q: Churn

**Status:** PASS / CLOSED — FORMAL EVIDENCE FROZEN AND PROMOTED

## Objective
Execute the frozen Exp11-Q Churn matrix from `docs/03_EXPERIMENT_CONTRACT.md` under the frozen statistical/provenance rules after bounded preparation verification.

## Authoritative inputs
- `docs/03_EXPERIMENT_CONTRACT.md`
- `docs/04_STATISTICAL_CONTRACT.md`
- `docs/02_QAHBN2_DESIGN_FREEZE.md`
- `docs/01_CANONICAL_AHBN_CONTRACT.md`
- `docs/stages/S08_FORMAL_EXP10Q.md` — S08-CLOSE PASS / CLOSED
- pinned canonical AHBN: `wwiras/ahbn@936a79480bc1252c79b6ee01f65c88c740af2844`

## Frozen matrix
- topology: BA(100,m=3)
- source: 0
- workload: 1,000 sequential messages per run
- churn levels: 0.00, 0.20, 0.40 target fraction
- churn cycles: 4
- leave boundaries: before messages 201, 401, 601, 801
- rejoin: after 50 subsequent messages, implemented as before messages 251, 451, 651, 851
- target selection: deterministic from seed; identical schedule for paired AHBN/Q-AHBN2
- cluster heads: eligible
- seeds: 42–46
- methods: AHBN, Q-AHBN2
- expected formal runs: 30
- frozen Q-AHBN2 learning contract: 81 states; five frozen actions; reward `(NEW-DUPLICATE-FAILED)/F`; alpha_Q=0.25; gamma=0.70; epsilon 0.30→0.03 with decay 0.995
- canonical AHBN remains immutable

## S09-PREP-1 — Frozen Contract-to-Harness Reconciliation — 2026-09-28

### Gate
Read-only reconciliation of the frozen Exp11-Q experiment/statistical contracts against the latest repository and pinned canonical AHBN churn runtime.

### Why
S08 is fully closed and promoted. Exp11-Q may therefore enter preparation, but formal execution must not begin until the frozen churn schedule is represented exactly in executable code and bounded regression/smoke verification passes.

### Audit findings
1. The formal experiment contract already freezes the complete 30-cell matrix and message-index churn schedule.
2. The statistical contract already freezes per-level analysis at 0.00, 0.20 and 0.40 with paired AHBN/Q-AHBN2 seed comparisons.
3. The pinned canonical AHBN runtime already provides `handle_churn_leave` and `handle_churn_join`, including canonical topology repair, churn-event accounting and churn-feedback updates.
4. The Q-AHBN2 repository had no dedicated Exp11-Q formal harness or runner before this gate.
5. Reusing the Exp10-Q failure runner unchanged would violate the Exp11-Q contract because it does not implement repeated leave/rejoin membership instability.

### Scientific reasoning
The safest implementation is integration-only: reuse the already validated Exp10-Q/Q-AHBN2 execution path and the canonical AHBN churn handlers, while driving churn at the prospectively frozen message-index boundaries. This preserves AHBN semantics and changes only the scenario event schedule required by Exp11-Q.

For a leave before message 201, “rejoin after 50 subsequent messages” means messages 201–250 execute while the selected peers are unavailable, followed by rejoin before message 251; the same mapping applies to cycles beginning before 401, 601 and 801. This interpretation is deterministic and directly implements the frozen contract without introducing a wall-clock parameter.

## Result
**S09-PREP-1 = PASS / CLOSED.**

## OUTPUT-STD-1 — Gitignored Generated-Output Root Standardization — 2026-09-28

**Status:** PASS / CLOSED.

### Gate
Standardize all Q-AHBN2 generated test, experiment, formal-run, analysis, trace and log artifacts under the repository-local `output/` tree before S09-PREP-3.

### Why
Large formal traces and logs must remain outside Git history. A single gitignored output root also removes ambiguity between historical root-level `q-ahbn-*`, `outputs/`, and `output/` conventions.

### Frozen operational rule
- repository-local generated-output root: `output/`;
- normal evidence-working subroot: `output/evidence/`;
- formal example: `output/evidence/q-ahbn-<DDMMYYYYHHmmss>-exp11q-formal/`;
- analysis example: `output/evidence/q-ahbn-<DDMMYYYYHHmmss>-exp11q-formal-analysis/`;
- no generated experiment directory may be created at repository root;
- custom `--output-dir` values must remain inside `output/`;
- `output/` is excluded by `.gitignore`;
- Google Drive synchronization of `output/` is working storage only; deliberate evidence promotion/readback remains required for authoritative evidence.

This is an operational/provenance change only. No experiment matrix, parameter, metric, result, statistical rule, or claim is changed.

## Result
**OUTPUT-STD-1 = PASS / CLOSED.**

## OUTPUT-STD-2 — Root Layout Correction and Enforcement — 2026-09-28

**Status:** PASS / CLOSED.

### Gate
Supersede OUTPUT-STD-1 where necessary so that every generated log/evidence/result/analysis directory is under `output/`, with `topology/` as the sole separate root-level data directory.

### Why
Local Explorer inspection showed historical generated material still present at repository root: `evidence/Exp10-Q`, root-level `q-ahbn-*` gamma-sensitivity directories, and `outputs/topologies`. The prior standard therefore did not fully express the intended physical repository layout.

### Corrected standard
```text
q-ahbn2/
├── docs/
├── output/
│   └── evidence/    # all generated logs/evidence/results/analysis
├── topology/        # topology data/cache only
├── qahbn2/
├── scripts/
└── tests/
```

Prohibited for new work:
- root-level `evidence/`;
- root-level `outputs/`;
- root-level generated `q-ahbn-*/`;
- logs/evidence under `topology/`.

The historical AR-1.4.2 gamma-sensitivity runner is also corrected to default to `output/evidence/` and reject custom paths outside `output/`. A tracked `topology/README.md` establishes the root topology directory without treating topology data as experiment evidence.

### Scientific boundary
This is filesystem/provenance governance only. Historical artifact contents, Exp10-Q evidence identity, scientific results, matrices, parameters, statistics, and claims are unchanged. Moving a local directory changes its location, not its scientific content.

## Result
**OUTPUT-STD-2 = PASS / CLOSED for authoritative repository controls.**

### Local readback closure
Researcher local readback on 2026-09-28 confirmed:
- root directories include `output/`, `output/evidence/`, and root-level `topology/`;
- no root-level `evidence/`, `outputs/`, or generated `q-ahbn-*/` directories remain within the inspected depth;
- `git status --short` returned empty, confirming a clean Git working tree after relocation.

Therefore the physical local workspace now matches the frozen OUTPUT-STD-2 layout.

## S09-PREP-2 — Implement Exp11-Q Formal Harness + Static Verification — 2026-09-28

**Status:** IMPLEMENTATION COMPLETE / LOCAL EXECUTION VERIFICATION REQUIRED.

### Implemented
- `qahbn2/formal_exp11q.py`
- `scripts/run_exp11q_formal.py`
- `tests/test_formal_exp11q_contract.py`

### Static contract guards
The implementation:
- enforces exactly churn levels `0.00, 0.20, 0.40`;
- enforces methods `AHBN, Q-AHBN2`;
- enforces seeds 42–46 and exactly 30 formal cells;
- generates four deterministic per-seed target sets using non-source peers only;
- produces 20 targets per cycle at churn=0.20 and 40 targets per cycle at churn=0.40 from the 99 eligible non-source peers;
- uses the same target schedule for the paired AHBN/Q-AHBN2 runs;
- applies leave before 201/401/601/801 and rejoin before 251/451/651/851;
- uses the pinned canonical AHBN churn handlers rather than redefining leave/rejoin semantics;
- preserves queue-to-exhaustion between messages;
- preserves the frozen Q-AHBN2 learner and direct-attempt reward attribution path;
- emits the four primary dissemination metrics, frozen Q-AHBN2 learning/adaptation fields, churn target schedule/event provenance, `RUN.md`, `manifest.json`, CSV and Q-decision trace;
- writes the formal directory by default to `output/evidence/q-ahbn-<timestamp>-exp11q-formal/` and rejects custom output paths outside `output/`;
- refuses matrix expansion;
- introduces no new metric, parameter, baseline or scientific claim.

### Verification boundary
GitHub/static inspection cannot execute the researcher’s local pinned ControlSim checkout. Runtime behavior, canonical import compatibility, tracker closure across churn transitions, topology repair, and the bounded churn smoke must therefore be verified locally before formal execution is released.

## Result
**S09-PREP-2 = PASS / CLOSED.**

## S09-PREP-3 — Local Regression + Bounded Exp11-Q Churn Smoke — 2026-09-28

**Status:** PASS / CLOSED.

### Commands executed
- Full local regression suite:
  `PATH=/Users/wwiras/Documents/src/AHBNProj/venv0.6/bin:$PATH PYTHONPATH=. python -m unittest discover -s tests -v`
- Dedicated Exp11-Q contract tests:
  `PATH=/Users/wwiras/Documents/src/AHBNProj/venv0.6/bin:$PATH PYTHONPATH=. python -m unittest tests.test_formal_exp11q_contract -v`
- Bounded Exp11-Q churn smoke:
  `PATH=/Users/wwiras/Documents/src/AHBNProj/venv0.6/bin:$PATH PYTHONPATH=. python -c "<bounded paired smoke execution>"`

### Regression result
- Full test suite: 27 tests executed, 27 PASS, 0 failures, 0 errors.
- Dedicated Exp11-Q contract suite: 4 tests executed, 4 PASS, 0 failures, 0 errors.
  - `test_exact_frozen_matrix`: PASS
  - `test_matrix_expansion_is_rejected`: PASS
  - `test_schedule_is_deterministic_paired_and_excludes_source`: PASS
  - `test_canonical_topology_cache_dir_redirected_to_root_topology`: PASS

### Bounded smoke configuration
- Scenario: BA(100, m=3), source 0, 1,000 sequential queue-to-exhaustion messages.
- Methods: paired AHBN and Q-AHBN2.
- Seed: 42.
- Churn level: 0.20 (20 non-source targets per cycle).
- Cycles: 4 leave/rejoin cycles.
  - Leave onsets: before messages 201, 401, 601, 801.
  - Rejoin onsets: before messages 251, 451, 651, 851 (after 50 subsequent messages).
- Churn targets: deterministic seeded non-source node IDs shared identically between paired AHBN and Q-AHBN2.
- Q-AHBN2 learning contract: frozen 81-state / 5-action space, alpha_Q=0.25, gamma=0.70, epsilon=0.30->0.03 (decay=0.995).

### Smoke output directory
- Directory: `output/evidence/q-ahbn-28092026202033-exp11q-smoke/`
- Artifacts generated:
  - `RUN.md` (smoke provenance, parameters, and explicit non-evaluative classification)
  - `manifest.json` (machine-readable run metadata, git commits, configuration, status)
  - `exp11q_smoke.csv` (diagnostic results, churn target counts, churn schedule, churn events)
  - `decision_trace.json` (passive Q-AHBN2 decision trace with 82,021 decision records)

### Runtime verification findings
1. Canonical imports / runtime compatibility: successfully loaded canonical AHBN v0.63 (`936a79480bc1252c79b6ee01f65c88c740af2844`) controllers, simulators, and topology generators without modifying canonical AHBN source.
2. Defect fix and contract enforcement: canonical `ahbn.topology` originally defaulted `TOPOLOGY_CACHE_DIR` to `Path("outputs/topologies")`, which violated `OUTPUT-STD-2`. A minimal integration compatibility fix was applied in `qahbn2/learning_validation.py` (`_load_canonical`) setting `ahbn_topology.TOPOLOGY_CACHE_DIR = Path("topology")`, accompanied by regression test `test_canonical_topology_cache_dir_redirected_to_root_topology`. Verified that root-level `outputs/` is not created.
3. Deterministic churn schedule: 20 targets generated per cycle from the 99 non-source candidates; identical schedules assigned to paired AHBN and Q-AHBN2 runs; node 0 (source) was never targeted.
4. Churn leave events: 4 leave events executed exactly at message boundaries 201, 401, 601, 801; target nodes marked inactive; canonical topology and cluster overlay repairs triggered successfully.
5. Inactive peer dissemination: messages 201–250, 401–450, 601–650, 801–850 were disseminated while target peers were unavailable.
6. Churn rejoin events: 4 rejoin events executed exactly at message boundaries 251, 451, 651, 851; target nodes restored active status; canonical topology and cluster overlay repairs triggered successfully.
7. Post-rejoin dissemination: dissemination continued normally after each rejoin through queue exhaustion.
8. Q-AHBN2 forwarding and outcome attribution: direct-attempt outcomes (NEW, DUPLICATE) were resolved cleanly without runtime exceptions.
9. Tracker and reward closure: `tracker.assert_empty()` was verified at every sequential message boundary (no unresolved pending attempts); terminal decisions were cleanly resolved at run termination; cumulative reward and Q-updates (81,291 updates) completed as expected.
10. Artifact audit: all output artifacts reside strictly under `output/evidence/`; no root-level `evidence/`, `outputs/`, or generated `q-ahbn-*` directories were created.

### Diagnostic values (non-formal evidence)
- AHBN (seed 42, churn 0.20): delivery ratio = 0.745500, propagation delay = 12.855097, duplicates = 122,217, total forwards = 195,767.
- Q-AHBN2 (seed 42, churn 0.20): delivery ratio = 0.820210, propagation delay = 9.403223, duplicates = 139,223, total forwards = 220,244, mean reward = -0.298910, Q-updates = 81,291, state-action coverage = 0.079012.

### Explicit scientific boundary and limitations
The bounded churn smoke values above are purely diagnostic pre-formal integration evidence to verify executable harness mechanics, event timing, and tracker closure. They are **not** formal experimental evidence and must **not** be used for comparative, inferential, or thesis/paper performance claims.

### Result
**S09-PREP-3 = PASS / CLOSED.**

## S09-PREP-4 Reconciliation — Stage Bookkeeping Reconciliation — 2026-09-28

**Status:** FACTUALLY RECONCILED.

The prior planning placeholder `S09-PREP-4 — Exp11-Q Formal Release and Freeze Audit` is reconciled factually against the executed formal run. Full pre-run static and regression verification was achieved under S09-PREP-2 and S09-PREP-3 (clean test suite, contract tests passing, deterministic smoke passing, and root topology redirection verified). Formal execution was performed directly from clean Q-AHBN2 commit `39688467d6bfe33a3281dca65f7c8a85fafc8684` against pinned canonical AHBN commit `936a79480bc1252c79b6ee01f65c88c740af2844`. Rather than retroactively rewriting history, this section records that formal release controls were satisfied and execution proceeded under controlled conditions.

## S09-FORMAL-1 — Execute Frozen 30-Run Exp11-Q Churn Matrix — 2026-09-28

**Status:** EXECUTED / RAW FORMAL EVIDENCE CREATED.

The frozen 30-run Exp11-Q Churn matrix was executed using the guarded formal runner `scripts/run_exp11q_formal.py`:
- Environment: ControlSim;
- Scenario: BA(100, m=3), source 0, 1,000 sequential messages per run;
- Matrix: churn levels {0.00, 0.20, 0.40}, methods {AHBN, Q-AHBN2}, seeds {42, 43, 44, 45, 46};
- Cycles: 4 leave/rejoin cycles per run (leaves before 201, 401, 601, 801; rejoins before 251, 451, 651, 851);
- Q-AHBN2 learner: frozen 81-state / 5-action space, alpha_Q=0.25, gamma=0.70, epsilon 0.30->0.03 (decay 0.995);
- Target selection: deterministic seeded non-source node IDs shared identically between paired AHBN and Q-AHBN2 runs;
- Pinned commits: Q-AHBN2 commit `39688467d6bfe33a3281dca65f7c8a85fafc8684`, canonical AHBN commit `936a79480bc1252c79b6ee01f65c88c740af2844`.

Generated raw formal evidence directory:
`output/evidence/q-ahbn-28092026203251-exp11q-formal/`

All 30 expected runs completed successfully (30/30). No exclusions, selective reruns, parameter adjustments, or matrix expansions occurred.

## S09-FORMAL-2 — Exp11-Q Formal Evidence Integrity, Matrix Completeness, and Large Trace Audit — 2026-09-28

**Status:** PASS / CLOSED.

### Artifact presence and provenance audit
All four required raw formal artifacts are present under `output/evidence/q-ahbn-28092026203251-exp11q-formal/`:
- `RUN.md` (494 bytes)
- `manifest.json` (834 bytes)
- `exp11q_formal.csv` (46,001 bytes)
- `decision_trace.json` (537,124,106 bytes)

Provenance verification confirms:
- Environment: ControlSim;
- Experiment: Exp11-Q Churn;
- Event: formal;
- Timestamp: `28092026203251`;
- Q-AHBN2 commit: `39688467d6bfe33a3281dca65f7c8a85fafc8684`;
- Canonical AHBN commit: `936a79480bc1252c79b6ee01f65c88c740af2844`;
- Expected runs = 30, completed runs = 30;
- Exclusions: 0;
- Reruns: 0.

### Matrix and CSV audit
Full inspection of `exp11q_formal.csv` confirms:
- Rows: exactly 30 data rows (plus header);
- Unique cells: exactly 30 unique `(churn_level, method, seed)` cells;
- Duplicate cells: 0;
- Missing cells: 0;
- Churn levels: exactly {0.00, 0.20, 0.40};
- Methods: exactly {ahbn, qahbn2};
- Seeds: exactly {42, 43, 44, 45, 46};
- Primary dissemination metrics (`delivery_ratio`, `propagation_delay`, `duplicates`, `total_forwards`): all present, finite, non-negative, and properly typed;
- Churn target counts: 0 for churn 0.00; 20 for churn 0.20; 40 for churn 0.40;
- Churn schedule: 4 cycles per run; target counts match churn level; node 0 (source) is never targeted; paired AHBN and Q-AHBN2 runs share identical deterministic target schedules;
- Churn events: 0 events for churn 0.00; exactly 8 events (4 leave, 4 join) for churn 0.20 and 0.40, with leave events occurring strictly at message boundaries 201, 401, 601, 801 and join events strictly at 251, 451, 651, 851; event targets match schedule targets;
- Q-AHBN2 metrics: `mean_reward`, `cumulative_reward`, `q_updates`, `state_action_coverage`, `intervention_count`, `keep_count`, and `action_distribution` are all finite and valid; AHBN rows correctly maintain empty Q-fields;
- Action distribution sums reconcile exactly: `sum(action_distribution.values()) == intervention_count + keep_count`.

### Large trace audit (>250 MB rule)
In compliance with the project rule mandating local auditing of artifacts >250 MB in the Google Drive-synchronized workspace, `decision_trace.json` (537,124,106 bytes / ~537 MB) was audited locally via incremental group streaming without memory exhaustion:
- Top-level structure: valid JSON array of trace groups;
- Group count: exactly 15 groups, corresponding 1-to-1 with the 15 Q-AHBN2 formal cells (3 churn levels x 5 seeds);
- Unique group mapping: no duplicate or missing groups; each group maps uniquely to a `(churn_level, seed)` cell present in the CSV;
- Individual decision records: exactly 1,264,774 decision records audited across all 15 groups;
- Record schema: every record contains valid `decision_id`, `peer_id` (0..99), `message_id`, `state` (4 elements in {"L","M","H"}), `action` (in the 5 frozen actions), `mode_ahbn`, `k_ahbn`, `mode_q`, `k_q`, `k_real`, `NEW`, `DUPLICATE`, and `FAILED`;
- Record counts: per-cell record count matches `intervention_count + keep_count` in `exp11q_formal.csv` with zero discrepancy;
- Action counts: per-cell action counts in the trace match the serialized `action_distribution` in `exp11q_formal.csv` with 100% agreement;
- Truncation / malformation: 0 malformed records, 0 truncated records.

### Scientific boundary
This gate establishes structural completeness, provenance, determinism, pairing, and protocol validity only. In accordance with controlled closure rules, no comparative performance analysis, inferential statistics, ranking, or result-based design decisions were conducted.

### Result
**S09-FORMAL-2 = PASS / CLOSED.**

## S09-CLOSE — Exp11-Q Evidence Freeze / Promotion and Stage Closure — 2026-09-28

**Status:** PASS / CLOSED.

### Evidence freeze and promotion
The raw formal evidence directory:
`output/evidence/q-ahbn-28092026203251-exp11q-formal/`
is frozen and preserved without modification, renaming, or deletion.

Frozen raw artifact integrity:
- `RUN.md`: 494 bytes, SHA-256 `6da4061efd8c4e77aab03e78bab9961e905df741174739237de0d86997b73cf7`
- `manifest.json`: 834 bytes, SHA-256 `dec009e3cc059e5b303f7ade4a8b877b310cd44c2657bbbf8c1570e6c40aa99a`
- `exp11q_formal.csv`: 46,001 bytes, SHA-256 `d869f4c76cd139b2dd554de5e5a8bf61d8403e8b223106f7809200676347f00c`
- `decision_trace.json`: 537,124,106 bytes, SHA-256 `1dcab26ed6014228e74b1ee7b822cb0e733d1a561ada156f792562402f1dcb2d`

A deterministic closure audit artifact has been created under `output/evidence/`:
`output/evidence/q-ahbn-28092026212332-exp11q-close-audit/`
Containing:
- `RUN.md` (summary of audit and freeze)
- `manifest.json` (machine-readable audit metadata and raw artifact hashes)
- `integrity_report.json` (complete machine-readable verification report)

### Readback verification
Readback confirmed:
- Raw formal directory `output/evidence/q-ahbn-28092026203251-exp11q-formal/` and closure audit directory `output/evidence/q-ahbn-28092026212332-exp11q-close-audit/` reside in the designated Google Drive synchronized hierarchy (`/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2/output/evidence/`);
- The four raw formal artifacts remain unaltered with matching sizes and checksums;
- No duplicate 537 MB trace was copied;
- Working tree remains clean;
- No scientific code or frozen contracts were modified.

### Result
**S09-CLOSE = PASS / CLOSED.**

## Next controlled stage
$$\boxed{\textbf{S10 — Exp12-Q Heterogeneity}}$$
