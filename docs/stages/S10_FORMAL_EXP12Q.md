# S10 — Formal Exp12-Q: Heterogeneity

**Status:** S10 PASS / CLOSED; EXP12-Q FORMAL EVIDENCE VERIFIED / PROMOTED / FROZEN

## Objective
Execute the frozen Exp12-Q heterogeneity matrix from `docs/03_EXPERIMENT_CONTRACT.md` under the frozen statistical/provenance rules.

## Controlled sequence
`S10.1 harness mapping -> S10.2 implementation -> S10.3 regression/smoke -> S10.4 formal execution -> S10.5 integrity -> S10.6 evidence freeze`.

## S10.1 — Frozen contract-to-harness mapping

**Result:** PASS / CLOSED.

Read-only reconciliation established that no new simulator semantics or scientific redesign is required. Exp12-Q reuses:
- the validated sequential-message formal Q-AHBN2 execution path from Exp10-Q/Exp11-Q;
- the pinned canonical AHBN S5 controller and dissemination implementation;
- canonical `assign_mixed_resources(...)` semantics for deterministic seeded resource assignment.

The historical canonical Exp12 configuration is mechanism precedent only; the authoritative Q-AHBN2 matrix remains `docs/03_EXPERIMENT_CONTRACT.md`.

## S10.2 — Formal harness implementation

**Result:** PASS / CLOSED.

Implementation-only changes:
- `qahbn2/formal_exp12q.py` — exact frozen 30-run matrix, resource classes/profiles, deterministic canonical resource assignment, AHBN and unchanged Q-AHBN2 paths, sequential 1,000-message queue-to-exhaustion workload, and resource-assignment provenance.
- `scripts/run_exp12q_formal.py` — guarded formal runner restricted to `output/`, with manifest/RUN metadata, decision trace, exact matrix validation, and mandatory paired AHBN/Q-AHBN2 resource-assignment identity check.
- `tests/test_formal_exp12q_contract.py` — exact matrix/resource contract guards and deterministic assignment/count checks.

No simulation, smoke run, formal run, parameter change, AHBN modification, Q-AHBN2 redesign, statistical change, or result inspection was performed in S10.2.

## S10.3 — Regression / deterministic smoke and pairing validation

**Result:** PASS / CLOSED.

Local execution at Q-AHBN2 commit `c185b6ee4225e8eda348a76d4da30cacea4f3244` produced:
- focused Exp12-Q frozen-contract suite: **5/5 PASS**;
- complete project regression suite: **32/32 PASS**.

The focused suite verified the exact matrix/resource contract, deterministic resource assignment, expected profile class counts, and rejection of unauthorized expansion. The complete regression suite confirmed that the existing Q-AHBN2 learning/reward/transition/provenance path and prior formal-contract integrations remained intact.

## S10.4 — Frozen 30-run formal execution

**Result:** PASS / CLOSED for execution completeness; raw evidence proceeds to S10.5 integrity audit.

Formal directory:
`output/evidence/q-ahbn-28092026215008-exp12q-formal`

Read-only post-execution verification established:
- manifest status: `completed`;
- expected/completed runs: **30/30**;
- CSV data rows: **30**;
- Q-AHBN2 producing commit: `a47ca0171d8af74a4b24f64a18b5d9edb5a58270`;
- canonical AHBN commit: `936a79480bc1252c79b6ee01f65c88c740af2844`;
- topology/workload: BA(100,m=3), source 0, 1,000 sequential queue-to-exhaustion messages/run;
- profiles: balanced, moderate_heterogeneity, weak_heavy;
- methods: AHBN, Q-AHBN2;
- seeds: 42--46;
- failure/churn disabled;
- exclusions: none;
- reruns: none.

Preserved artifacts include `RUN.md`, `manifest.json`, `exp12q_formal.csv`, and `decision_trace.json`. The decision trace is approximately 539 MB and therefore remains a local/Drive-synced artifact for bounded local integrity checking rather than remote ingestion.

No result interpretation, performance-based rerun, tuning, matrix change, or aggregation was performed in S10.4.

## S10.5 — Formal evidence integrity / completeness audit

**Result:** PASS / CLOSED.

A read-only local programmatic audit was performed over the preserved formal directory, including the approximately 539 MB decision trace. No scientific performance interpretation was performed.

The audit established:
- all four required artifacts present and readable;
- manifest/provenance consistent with the frozen Exp12-Q contract;
- exact **30-cell** matrix with no duplicate, missing, or unauthorized cells;
- paired AHBN/Q-AHBN2 resource-assignment identity for all **15 profile/seed pairs**;
- valid 100-peer assignments and exact frozen resource-class counts for all profiles;
- structurally valid required dissemination fields across all 30 rows;
- structurally valid Q-learning fields for all 15 Q-AHBN2 rows and empty Q-only fields for AHBN as designed;
- valid frozen five-action distributions with internal count reconciliation;
- valid, untruncated decision-trace JSON containing exactly **15 Q-AHBN2 run groups** and no AHBN trace groups;
- **1,331,081** individual decision records structurally validated, with per-group record counts matching CSV action totals;
- cross-artifact identity/provenance consistency;
- exclusions: none;
- reruns: none.

**Defects found:** none.

The audit outcome establishes evidence integrity/completeness only. It does not constitute scientific interpretation or comparative performance analysis.

## S10.6 — Evidence freeze / promotion and stage closure

**Result:** PASS / CLOSED.

The S10.5-verified formal evidence was deliberately promoted in the designated Google Drive-synced evidence hierarchy without rewriting raw evidence.

Promoted hierarchy:
`output/evidence/Exp12-Q/q-ahbn-28092026215008-exp12q-formal/`

Promotion verification:
- dedicated `Exp12-Q` evidence container created under `output/evidence/`;
- existing verified formal folder moved into that container;
- the same Google Drive formal-folder ID was preserved, confirming organizational promotion rather than copy/recreation;
- promoted folder verified by Drive readback;
- no raw formal artifact modified;
- no rerun, exclusion, tuning, aggregation, or scientific interpretation performed.

S10.1 through S10.6 are complete. Exp12-Q formal evidence is frozen for later statistical analysis/interpretation under the governing statistical contract.

## Boundary
Exp12-Q remains part of the primary AHBN-versus-Q-AHBN2 RO4/RQ4 causal evaluation. No redesign, parameter change, comparator expansion, extra severity, or result-driven protocol change is authorized here.

Exact matrix, run count, outcomes, exclusions/reruns, and analysis remain governed by the frozen experiment/statistical contracts.
