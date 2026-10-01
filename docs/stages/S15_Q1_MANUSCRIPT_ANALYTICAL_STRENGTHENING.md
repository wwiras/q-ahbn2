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


## S15-1 — Current Q-AHBN Analytical Gap Matrix

**Status:** PASS / CLOSED — 2026-10-01

### Audit conclusion
The active manuscript is scientifically complete but analytically under-expressed relative to the AHBN Scientific Reports benchmark. The dominant gaps are presentation/mechanism gaps, not missing experiment gaps.

| Manuscript area | Current gap | Frozen evidence source | Recommended action | Scientific value | Claim risk | Existing evidence sufficient? |
|---|---|---|---|---|---|---|
| Method / architecture | No mechanism figure | Design freeze; canonical AHBN contract | Add Q-AHBN closed-loop architecture/process figure | HIGH | LOW | YES |
| Learning mechanism | Learning evidence mainly prose | Formal traces; S12 C02 | Add bounded learning-mechanism summary figure/table | HIGH | MEDIUM | YES |
| Primary results | 8 conditions compressed into one table | S11-A / S12 | Add paired-difference trade-off figure | HIGH | LOW | YES |
| Dynamic stress | Churn attenuation and heterogeneity patterns not visually synthesized | S11-A / S12 | Add condition-wise trend/small-multiple plot | HIGH | LOW | YES |
| Exp13 | Five-method positioning only tabular | S11-B / S12 | Add four-metric bounded comparator figure | MEDIUM-HIGH | MEDIUM | YES |
| Kubernetes | Unusual total_forwards/F_attempt accounting easy to misread | K6 / S12 | Add explicit accounting caveat/table or figure | HIGH | HIGH | YES |
| Sensitivity | Gamma evidence not publication-visible | AR-1.4.2–1.4.4 / S05 | Add bounded gamma-sensitivity summary | MEDIUM-HIGH | MEDIUM | YES |
| Discussion | Result→mechanism→limitation links can be stronger | S12/S12A | Revise synthesis around evidence roles | HIGH | LOW | YES |
| Reproducibility | Provenance is strong but mostly external to manuscript | S14/PROVENANCE | Add compact reproducibility statement/table if journal format allows | MEDIUM | LOW | YES |
| Reviewer defence | Likely challenges are not explicitly pre-empted | S12A/S14/AHBN reviewer lessons | Add reviewer-challenge audit and targeted revisions | HIGH | LOW | YES |

### Autonomous decision
No new experiment is scientifically necessary at S15-1. Proceed to evidence inventory.

## S15-2 — Existing-Evidence Analysis Inventory

**Status:** PASS / CLOSED — 2026-10-01

### Reusable frozen evidence
1. Primary S11-A aggregation: 80/80 runs, 40/40 same-seed pairs, eight condition-specific paired outcomes.
2. Learning/adaptation summaries: mean/cumulative reward, q_updates, state_action_coverage, intervention_count, keep_count, action distributions with per-seed retention.
3. Exp13-Q: 25/25 runs, five methods, one frozen churn=0.40 benchmark.
4. Kubernetes: 25/25 validated coordinates, five-method means plus paired AHBN–Q-AHBN intervals and runtime-accounting diagnostics.
5. Gamma sensitivity: 15/15 runs over gamma={0.70,0.80,0.90}, seeds 42–46, integrity PASS; gamma=0.70 selected from the predeclared candidate set.
6. Full design/provenance chain: experiment contracts, statistical contract, manifests, hashes, code SHAs, frozen image digest.

### Evidence sufficiency decision
The preserved evidence is sufficient for all planned S15 analytical strengthening without extending the statistical contract. Any added quantitative artifact must remain descriptive or reproduce already-authorized paired uncertainty.

## S15-3 — Learning-Mechanism Analysis

**Status:** PASS / CLOSED — 2026-10-01

### Authorized synthesis
Q-AHBN should be explained as the cycle:
AHBN proposal → discretized 81-state representation → one of five bounded meta-actions → realized forwarding → direct NEW/DUPLICATE/FAILED attribution → reward closure → next-same-peer Q update.

Mechanism evidence supports:
- repeated Q updates;
- non-zero state-action coverage;
- repeated interventions;
- condition-dependent action/state use;
- active outcome-driven refinement.

Mechanism evidence does not support:
- convergence;
- learned-policy optimality;
- reward maximization across environments;
- universal performance benefit.

### Recommended publication artifact
One architecture/process figure plus one compact descriptive learning table/plot. Use existing aggregate learning fields only; no new inferential test.

## S15-4 — Effect and Trade-off Analysis

**Status:** PASS / CLOSED — 2026-10-01

### Primary effect structure
Across all eight ControlSim conditions, Q-AHBN has positive paired mean delivery differences and negative paired mean delay differences versus AHBN; all paired 95% Student-t CIs for those two outcomes exclude zero. Duplicate and forward means are higher in all eight conditions.

Recommended main analytical figure: four aligned panels over the eight conditions showing paired mean differences for:
- delivery (percentage points);
- propagation delay;
- duplicates;
- total forwards;
with zero reference line and existing paired 95% CIs where available.

Interpretation remains a delivery/latency improvement with communication-overhead trade-off, not dominance.

## S15-5 — Dynamic-Stress Response Analysis

**Status:** PASS / CLOSED — 2026-10-01

### Stress-specific findings
- Failure: tested one-peer failure retains higher delivery/lower delay with higher communication cost.
- Churn: delivery gain contracts descriptively from +13.347 pp at 0.00 to +6.294 pp at 0.20 to +2.304 pp at 0.40; no dose-response model is authorized.
- Heterogeneity: all three frozen profiles retain higher delivery/lower delay with higher duplicates/forwards; delay reduction remains substantial across profiles.

Recommended artifact: stress-family small multiples or grouped paired-difference figure. Do not fit trend models or extrapolate.

## S15-6 — Exp13 Comparative Positioning Analysis

**Status:** PASS / CLOSED — 2026-10-01

Exp13 remains one bounded five-method ControlSim benchmark at churn=0.40. Q-AHBN improves AHBN delivery/delay there but does not dominate Gossip, Structured, or DC-SoC across the four metrics.

Recommended artifact: metric-wise point/bar panels for delivery, delay, duplicates, forwards with a caption explicitly stating that panels are descriptive positioning, not an omnibus score or ranking.

## S15-7 — Kubernetes Cross-Environment Analysis

**Status:** PASS / CLOSED — 2026-10-01

### Evidence-role decision
ControlSim and Kubernetes remain complementary and non-pooled.

Kubernetes supports:
- executable distributed realization;
- observability of the frozen learning contract;
- exposure of deployment/runtime accounting constraints.

Kubernetes does not support:
- independent consistent Q-AHBN performance improvement over AHBN;
- literal replication of ControlSim;
- pooled cross-environment effects.

### Critical accounting interpretation
The low Kubernetes Q-AHBN total_forwards mean (10.0 vs 998.6 for AHBN) must be presented together with mean F_attempt (2345.4 vs 1448.0). Therefore total_forwards cannot be used as a generic low-overhead claim.

Recommended artifact: compact runtime-accounting callout/table, not a superiority graph.

## S15-8 — Robustness / Sensitivity Evidence Review

**Status:** PASS / CLOSED — 2026-10-01

Reusable sensitivity evidence exists for gamma only within the frozen bounded candidate set {0.70,0.80,0.90} in ControlSim Learning Validation, 15/15 runs. gamma=0.70 remains the selected frozen value.

Permitted interpretation:
- the selected gamma was not arbitrary;
- the bounded predeclared comparison supplied parameter-selection evidence;
- all candidates exhibited nonzero state-action coverage and broad action use.

Prohibited interpretation:
- global gamma optimality;
- convergence;
- universal robustness;
- sensitivity coverage for alpha_Q, epsilon schedule, reward design, or action-space design.

No new sensitivity experiment is scientifically required.

## S15-9 — Figures and Analytical Tables Package

**Status:** PASS / CLOSED — 2026-10-01

Approved manuscript analytical package:
1. Figure A — Q-AHBN bounded learning architecture/process.
2. Figure B — Eight-condition paired trade-off synthesis.
3. Figure C — Dynamic-stress response synthesis (failure/churn/heterogeneity).
4. Figure D — Exp13 bounded five-method positioning.
5. Table/Callout E — Kubernetes runtime-accounting interpretation.
6. Table/Callout F — Bounded gamma-sensitivity evidence.

Decision: these artifacts can be authored directly in LaTeX/TikZ/PGFPlots from already frozen registered values and descriptive summaries. No raw-evidence recomputation or new experiment is required.

## S15-10 — Reviewer-Challenge Audit

**Status:** PASS / CLOSED — 2026-10-01

Likely reviewer challenges and required manuscript defence:
1. “Did the learner converge?” → explicitly no convergence claim; show active-learning evidence only.
2. “Why gamma=0.70?” → bounded predeclared sensitivity evidence, not global optimality.
3. “Are the gains free?” → no; primary gains generally incur duplicate/forwarding cost.
4. “Does performance survive stronger churn?” → tested gains attenuate descriptively; no extrapolation.
5. “Is Q-AHBN better than all baselines?” → Exp13 is positioning only; no winner/ranking.
6. “Does Kubernetes confirm simulation?” → no; operational realization only and paired CIs cross zero.
7. “Why is Kubernetes total_forwards so low?” → runtime accounting differs; present F_attempt caveat.
8. “Is n=5 enough for broad claims?” → claims are condition-specific and paired; no universal generalization.
9. “Is Q-AHBN lightweight?” → architecture is bounded/tabular, but generic low-overhead performance is not supported.
10. “Was AHBN retuned?” → no; canonical AHBN remains immutable.

## S15-11 — Manuscript Analytical Revision

**Status:** RELEASED / ACTIVE — 2026-10-01

Autonomous revision scope:
- add publication-quality analytical figures/tables above;
- strengthen Methods/Results/Discussion/Limitations linkage;
- preserve all S12A claim boundaries;
- introduce no new experiment, statistic family, comparator, literature claim, or hyperparameter claim.



## S15-11 — Manuscript Analytical Revision

**Status:** PASS / CLOSED — 2026-10-01

### Changes applied
The active manuscript `wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex` was strengthened using only frozen evidence:
- added a bounded Q-AHBN intervention/learning-cycle figure;
- added a learning-mechanism evidence table;
- added explicit bounded gamma-sensitivity provenance;
- added an eight-condition analytical trade-off synthesis table;
- strengthened descriptive churn attenuation wording without fitting a trend model;
- strengthened Exp13 metric-wise positioning without ranking;
- added a Kubernetes `total_forwards` versus `F_attempt` accounting table;
- strengthened Discussion links between mechanism, results, overhead, sensitivity, and evidence-role boundaries.

Manuscript commit: `70a165f9be1636849e53a70c595aa6ec7aede2ba`.
Provenance registration commit: `fafa4025cd9c9d2be795fdcd16b5049baa98bd94`.

Structural readback:
- 8 sections retained;
- 6 table environments open/close balanced;
- 1 figure environment open/close balanced;
- all new labels occur exactly once.

No new experiment, rerun, statistic family, pooled estimate, comparator, literature claim, parameter value, or scientific evidence was introduced.

## S15-12 — Claim Reconciliation v2

**Status:** PASS / CLOSED — 2026-10-01

### Reconciliation result
The S15 analytical revision does not require any new scientific claim authorization. S12A remains authoritative.

The new artifacts map to existing claims:
- architecture figure → C01/C02;
- learning-mechanism table → C02/C13/C15;
- primary trade-off synthesis → C03-C06/C13-C15;
- Exp13 strengthened interpretation → C07/C12-C15;
- Kubernetes accounting table → C08-C10/C14/C15;
- gamma-sensitivity provenance → C13/C15 and frozen S05 selection evidence.

### Wording boundary retained
Still prohibited:
- convergence or policy optimality;
- global hyperparameter optimality;
- universal superiority / best method / dominance;
- generic lightweight or low-overhead performance;
- literal ControlSim/Kubernetes replication;
- pooled cross-environment effects or equivalence;
- Exp13 omnibus ranking.

No S12A claim ID needs to be reopened or replaced.

## S15-13 — Q1 Submission Readiness Audit

**Status:** PASS / CLOSED — 2026-10-01

### Audit result
The manuscript is now materially stronger than the S14 version in analytical presentation while remaining scientifically bounded.

PASS checks:
1. frozen science baseline unchanged: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
2. canonical AHBN remains immutable;
3. Q-AHBN naming preserved;
4. primary run counts/seeds/evidence roles unchanged;
5. statistical contract unchanged;
6. no unsupported new numerical claim introduced;
7. mechanism evidence is separated from performance evidence;
8. sensitivity provenance is bounded and non-optimality wording is explicit;
9. primary trade-off is visible across all eight conditions;
10. Exp13 remains bounded positioning only;
11. Kubernetes accounting caveat is prominent;
12. ControlSim/Kubernetes remain complementary and non-pooled;
13. limitations/non-claims remain explicit;
14. provenance record updated;
15. no new experiment is scientifically necessary for the present submission-strengthening objective.

### Residual submission tasks outside scientific S15 closure
- journal-specific formatting/template migration;
- final bibliography/Zotero synchronization and compile check;
- final rendered-PDF visual/proof audit;
- journal cover letter / submission metadata if required;
- any journal-specific code/data availability wording.

These are submission-production tasks rather than unresolved S15 science.

## S15 programme closure

**S15 = PASS / CLOSED — 2026-10-01.**

Scientific decision: existing frozen evidence was sufficient to materially strengthen the Q-AHBN manuscript. No new experiment or parameter change was authorized or required.

Next controlled activity is journal-specific submission preparation / final production audit, not additional scientific experimentation.
