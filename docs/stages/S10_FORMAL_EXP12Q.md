# S10 — Formal Exp12-Q: Heterogeneity

**Status:** S10.4 PASS / CLOSED; S10.5 NEXT; RAW FORMAL EVIDENCE PENDING INTEGRITY AUDIT

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

## S10.5 release boundary

S10.5 is the next permitted gate. It must audit raw evidence validity/completeness, including exact 30-cell matrix uniqueness, paired AHBN/Q-AHBN2 resource-assignment identity, required metric-field completeness, finite/structurally valid outputs, Q-only learning evidence, and decision-trace structural completeness. The large trace should be audited locally without copying it into GitHub.

S10.6 evidence freeze/promotion remains blocked until S10.5 passes.

## Boundary
Exp12-Q remains part of the primary AHBN-versus-Q-AHBN2 RO4/RQ4 causal evaluation. No redesign, parameter change, comparator expansion, extra severity, or result-driven protocol change is authorized here.

Exact matrix, run count, outcomes, exclusions/reruns, and analysis remain governed by the frozen experiment/statistical contracts.
