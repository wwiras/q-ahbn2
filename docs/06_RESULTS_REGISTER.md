# Q-AHBN2 Results Register

**Status:** ACTIVE — FORMAL EVIDENCE IN PROGRESS
**Created:** 2026-09-23 under DOC-SYNC-1

## Registered bounded evidence

### AR-1.4.2 / AR-1.4.3 / AR-1.4.4 — Gamma sensitivity
- Environment: ControlSim Learning Validation
- Candidate gamma: {0.70, 0.80, 0.90}
- Seeds: {42,43,44,45,46}
- Runs: 15/15
- Evidence integrity: PASS
- Scientific comparison: PASS
- Researcher-approved parameter decision: **gamma=0.70 FROZEN**
- Scope limitation: bounded stationary Learning Validation only; not convergence, policy-optimality, or universal-performance evidence.

### Exp10-Q — Failure
- Environment: ControlSim Formal Failure
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Conditions: control and one deterministic non-source peer failure before message 501
- Seeds: {42, 43, 44, 45, 46}
- Methods: AHBN, Q-AHBN2
- Runs: 20/20 completed (0 exclusions, 0 reruns)
- Raw formal directory: `output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal/`
- Analysis directory: `output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal-analysis/`
- Evidence integrity & claim boundary: PASS / CLOSED (S08-CLOSE)
- Scope / claim boundary: condition-specific delivery/delay improvement versus duplicate/forwarding overhead trade-off under one-peer failure; no universal superiority or composite adaptation claims.

### Exp11-Q — Churn
- Environment: ControlSim Formal Churn
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Churn levels: {0.00, 0.20, 0.40} target fractions
- Churn cycles: 4 leave/rejoin cycles (leave before 201, 401, 601, 801; rejoin before 251, 451, 651, 851)
- Seeds: {42, 43, 44, 45, 46}
- Methods: AHBN, Q-AHBN2
- Runs: 30/30 completed (0 exclusions, 0 reruns)
- Raw formal directory: `output/evidence/q-ahbn-28092026203251-exp11q-formal/`
- Closure audit directory: `output/evidence/q-ahbn-28092026212332-exp11q-close-audit/`
- Evidence integrity: PASS / CLOSED (S09-CLOSE)
- Scope limitation: formal evidence completed and frozen under deliberate closure audit; comparative scientific conclusions, statistical aggregation, and inferential claims are deferred beyond this gate.

### Exp12-Q — Heterogeneity
- Environment: ControlSim Formal Heterogeneity
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Resource profiles: balanced, moderate_heterogeneity, weak_heavy
- Seeds: {42, 43, 44, 45, 46}
- Methods: AHBN, Q-AHBN2
- Runs: 30/30 completed (0 exclusions, 0 reruns)
- Frozen formal directory: `output/evidence/Exp12-Q/q-ahbn-28092026215008-exp12q-formal/`
- Evidence integrity: PASS / CLOSED (S10.5)
- Evidence promotion/freeze: PASS / CLOSED (S10.6)
- Scope limitation: formal evidence completed, integrity-verified, promoted and frozen; comparative scientific conclusions and statistical interpretation remain governed by the frozen statistical contract and are not claimed by S10 closure.


### Exp13-Q — Reference Benchmark
- Environment: ControlSim Formal Reference Benchmark
- Topology: BA(100, m=3), source 0, 1,000 sequential messages
- Scenario: churn = 0.40 with four leave/rejoin cycles
- Seeds: {42, 43, 44, 45, 46}
- Methods: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2
- Expected runs: 25
- Raw formal directory: `output/evidence/q-ahbn-29092026081836-exp13q-formal/`
- Producing Q-AHBN2 commit: `2b11b4e95ef98c86458e02c494d6b6ea232a6d7a`
- Evidence integrity/completeness: **PASS / CLOSED (S10A-INTEGRITY)**
- Integrity accounting: 25/25 unique formal cells; 5 Q-AHBN2 trace groups; 410,852 structurally validated decision records; 0 exclusions; 0 reruns
- Evidence freeze/promotion: PENDING
- Interpretation boundary: no comparative scientific conclusions, ranking, aggregation, or publication claim until the verified Exp13-Q evidence is deliberately frozen/promoted and S10A closes.
