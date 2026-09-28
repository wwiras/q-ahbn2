# S09 — Formal Exp11-Q: Churn

**Status:** PREPARATION — IMPLEMENTATION COMPLETE / LOCAL VERIFICATION REQUIRED

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
**S09-PREP-2 = NEEDS MANUAL TEST.**

## Next controlled gate
`S09-PREP-3 — Local Regression + Bounded Exp11-Q Churn Smoke`.

Formal 30-run Exp11-Q execution remains blocked until PREP-3 passes.
