# S10 — Formal Exp12-Q: Heterogeneity

**Status:** S10.2 PASS / CLOSED; S10.3 NEXT; FORMAL EXECUTION NOT RELEASED

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

## S10.3 release boundary

S10.3 is the next permitted gate. It must regression-test the implementation and perform only the minimum deterministic smoke/parity work required to establish that the frozen Exp12-Q harness is executable and paired correctly.

S10.4 formal execution remains blocked until S10.3 explicitly passes.

## Boundary
Exp12-Q remains part of the primary AHBN-versus-Q-AHBN2 RO4/RQ4 causal evaluation. No redesign, parameter change, comparator expansion, extra severity, or result-driven protocol change is authorized here.

Exact matrix, run count, outcomes, exclusions/reruns, and analysis remain governed by the frozen experiment/statistical contracts. This stage does not release execution until its preparation gates are satisfied.
