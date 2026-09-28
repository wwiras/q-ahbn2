# S10 — Formal Exp12-Q: Heterogeneity

**Status:** S10.3 PASS / CLOSED; S10.4 NEXT; FORMAL EXECUTION RELEASED

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

The focused suite verified:
- exact 30-run matrix;
- exact frozen resource-class parameters and profile fractions;
- deterministic resource assignment for the same profile/seed;
- expected class counts for balanced, moderate_heterogeneity, and weak_heavy;
- rejection of unauthorized profile/method/seed expansion.

The complete regression suite additionally confirmed that the existing Q-AHBN2 learning, transition bookkeeping, reward/update path, provenance trace, Exp10-Q contract, Exp11-Q contract, and canonical topology integration remained intact.

No scientific parameter, implementation contract, or frozen protocol was changed during S10.3. No formal Exp12-Q result was generated or interpreted.

## S10.4 release boundary

S10.4 is the next permitted gate and the frozen 30-run formal Exp12-Q matrix is released for execution.

During formal execution:
- no tuning or parameter modification;
- no selective rerun based on observed performance;
- no comparator/profile/seed expansion;
- no interpretation or aggregation before S10.5 validity/integrity audit;
- any interruption must first be classified as a runtime/validity issue.

## Boundary
Exp12-Q remains part of the primary AHBN-versus-Q-AHBN2 RO4/RQ4 causal evaluation. No redesign, parameter change, comparator expansion, extra severity, or result-driven protocol change is authorized here.

Exact matrix, run count, outcomes, exclusions/reruns, and analysis remain governed by the frozen experiment/statistical contracts.
