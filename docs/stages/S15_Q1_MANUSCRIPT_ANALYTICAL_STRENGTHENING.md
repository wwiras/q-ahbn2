# S15 — Q1 Manuscript Analytical Strengthening Programme

**Status:** ACTIVE — S15-0 PASS / CLOSED; S15-1 RELEASED — 2026-10-01

## Governing objective
Strengthen the standalone Q-AHBN manuscript for a serious Q1-journal submission attempt by mining the existing frozen evidence before authorizing any new experiment. S15 does not reopen canonical AHBN, Q-AHBN parameters, algorithms, frozen experiments, or S12A claim boundaries.

Pinned manuscript science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`

Publication-facing name remains **Q-AHBN**.

## S15 sequence
S15-0 AHBN Benchmark Manuscript Decomposition — PASS / CLOSED  
S15-1 Current Q-AHBN Analytical Gap Matrix — RELEASED / NEXT  
S15-2 Existing-Evidence Analysis Inventory  
S15-3 Learning-Mechanism Analysis  
S15-4 Effect and Trade-off Analysis  
S15-5 Dynamic-Stress Response Analysis  
S15-6 Exp13 Comparative Positioning Analysis  
S15-7 Kubernetes Cross-Environment Analysis  
S15-8 Robustness / Sensitivity Evidence Review  
S15-9 Figures and Analytical Tables Package  
S15-10 Reviewer-Challenge Audit  
S15-11 Manuscript Analytical Revision  
S15-12 Claim Reconciliation v2  
S15-13 Q1 Submission Readiness Audit

## S15-0 — AHBN benchmark decomposition

### Benchmark inspected
Latest AHBN Scientific Reports v2.0 clean manuscript, reviewer-markup manuscript, and second-revision response package, reconciled with `wwiras/SRpt` v2.0 source.

### Transferable publication practices
1. Mechanism exposition is visual and traceable: conceptual architecture, process sequence, controller variables, and requested-versus-realized behavior are explicitly separated.
2. Results are multi-metric: latency/efficiency is interpreted together with delivery/reachability and communication activity.
3. Controller behavior is exposed through traces/distributions rather than inferred only from aggregate outcomes.
4. Sensitivity evidence is bounded by provenance: directly tested parameters are distinguished from design choices that were not sensitivity-tested.
5. Counter-intuitive results are explained rather than hidden, including lower communication activity coexisting with lower reachability and narrow controller operating regions.
6. Simulation and Kubernetes are treated as complementary evidence families with distinct roles rather than pooled or presented as literal replication.
7. Comparator fairness is explained at the experimental-contract level without pretending that unlike algorithms have identical tuning semantics.
8. Reviewer responses map each challenge to exact manuscript amendments while explicitly recording what was not changed.
9. Limitations and non-claims are integrated into the scientific interpretation rather than isolated as generic caveats.
10. Reproducibility scope is explicit, including code/archive boundaries and what is or is not sufficient to recreate the original runtime environment.

### Q-AHBN transfer decision
The AHBN practices are transferable as publication strategy, not as scientific evidence. Q-AHBN should preferentially strengthen:
- learning-mechanism visualization and action/state/reward trace exposition;
- condition-wise delivery/latency/communication trade-off visualization;
- dynamic-stress response across failure, churn, and heterogeneity;
- bounded Exp13 comparative positioning;
- explicit ControlSim-versus-Kubernetes evidence-role comparison;
- robustness/sensitivity presentation using already frozen gamma-sensitivity and other existing validation evidence;
- reviewer-facing explanation of unusual runtime accounting, especially Kubernetes `total_forwards` versus `F_attempt`;
- explicit limitation and non-claim linkage.

### Scientific boundary
No new experiment is authorized by S15-0. Existing evidence is sufficient to proceed to an analytical gap audit. Any later proposal for new experimentation must stop for researcher approval.

## S15-1 release contract
S15-1 must audit the active Q-AHBN manuscript section-by-section and claim-by-claim against the frozen evidence inventory. It must check:
- missing mechanism figures and explanatory diagrams;
- missing learning-state/action/reward and trace exposition;
- whether every primary condition has adequate delivery, delay, duplicate, and forwarding trade-off presentation;
- whether effect magnitude can be expressed descriptively without extending the frozen statistical contract;
- dynamic-stress trends across failure, churn, and heterogeneity;
- Exp13 positioning without winner/ranking claims;
- Kubernetes operational-realization analysis, including requested/attempted/realized forwarding distinctions where supported;
- available robustness/sensitivity evidence and its exact provenance boundary;
- unusual or counter-intuitive results needing explicit explanation;
- result-to-discussion linkage;
- limitation-to-evidence linkage;
- reproducibility/provenance presentation;
- likely reviewer challenges and whether current text pre-empts them;
- candidate figures/tables that can be generated entirely from frozen evidence.

For every identified gap, S15-1 must record: manuscript location, evidence source, proposed analytical artifact or prose action, scientific value, claim risk, and whether existing evidence is sufficient.

**Next controlled gate:** S15-1 — Current Q-AHBN Analytical Gap Matrix.
