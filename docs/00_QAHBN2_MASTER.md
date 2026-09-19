# Q-AHBN2 Master Research, Development, Experiment and Publication Contract v1.0

## 1. Purpose

This document is the authoritative operating template for the Q-AHBN2 project from initial reconciliation through development, validation, formal experimentation, statistical analysis, scientific interpretation, manuscript preparation, and submission.

Q-AHBN2 is the redesign/reconciliation of the previous Q-AHBN implementation so that it operates on the latest frozen canonical AHBN.

This document exists to prevent inconsistency across AI conversations, accidental modification of canonical AHBN, uncontrolled experiment expansion, loss of scientific provenance, unnecessary repeated work, post-hoc metric or parameter changes, dependence on AI conversational memory, unnecessary Codex/agent cost, and manuscript claims drifting away from experimental evidence.

The project should remain as simple as possible while preserving scientific validity, reproducibility, traceability, and publication quality.

## 2. Project Objective

Scientific dependency:

```text
RO1 Cloud-native evaluation framework
 ↓
RO2 Characterisation of dissemination trade-offs
 ↓
RO3 Frozen canonical AHBN
 ↓
RO4 Q-AHBN2 learning enhancement
 ↓
Learning validation
 ↓
Controlled evaluation
 ↓
Kubernetes-native realism validation
 ↓
Scientific interpretation
 ↓
Q-AHBN2 manuscript
```

Q-AHBN2 investigates whether a lightweight Q-learning layer can enhance adaptation over the already-frozen canonical AHBN under evaluated dynamic network conditions. Q-AHBN2 does NOT redesign AHBN.

## 3. Absolute Scientific Rule — Canonical AHBN Is Immutable

The latest approved canonical AHBN is a READ-ONLY scientific dependency. Q-AHBN2 MUST follow canonical AHBN exactly, including where applicable: observation definitions, normalization, EWMA formulation and parameters, controller score, sigmoid transformation, mode-selection rule, fanout actuator and thresholds, supported fanout values, eligible-neighbour handling, realized fanout, Gossip semantics, Structured semantics, baseline semantics, and associated metric definitions.

The canonical AHBN implementation and latest approved AHBN Scientific Reports manuscript are the authorities. Previous Q-AHBN is NOT authoritative when it conflicts with canonical AHBN.

Q-AHBN2 may learn over or influence explicitly permitted AHBN operating decisions according to the approved Q-AHBN2 design. It MUST NOT silently change AHBN equations, thresholds, normalization, EWMA, fanout mapping, baseline behaviour, or modify AHBN merely to improve Q-AHBN2 performance. If Q-AHBN2 performs poorly under canonical AHBN, that is a Q-AHBN2 result or design issue. AHBN is not reopened.

## 4. Authority Hierarchy

### Level 1 — Frozen canonical authority
1. Latest approved canonical AHBN repository.
2. Latest revised/frozen AHBN Scientific Reports manuscript.
3. Final AHBN experimental/statistical artifacts where applicable.

### Level 2 — Q-AHBN2 frozen authority
After reconciliation:
4. `00_QAHBN2_MASTER.md`
5. `01_CANONICAL_AHBN_CONTRACT.md`
6. `02_QAHBN2_DESIGN_FREEZE.md`
7. `03_EXPERIMENT_CONTRACT.md`
8. `04_STATISTICAL_CONTRACT.md`

### Level 3 — Historical reference
9. Previous Q-AHBN repository.
10. Previous Q-AHBN manuscript.
11. Previous Q-AHBN experimental outputs.

Historical material may guide Q-AHBN2 but cannot override frozen canonical AHBN.

### Level 4 — Conversational context
ChatGPT memory, previous conversations, Codex narration, researcher recollection, and informal notes are supporting context only. If they conflict with repository evidence or frozen control documents, repository/artifact state wins.

## 5. Human and AI Roles

The human researcher remains the scientific authority and approves research objectives, Q-AHBN2 design, experimental matrix, formal parameters, seeds, repetitions, baselines, metrics, statistical methodology, formal experiment status, exclusions/reruns, scientific interpretation, and changes to frozen methodology. AI execution does not constitute scientific authorization.

ChatGPT is the first-priority AI assistant for scientific reasoning, repository inspection, canonical reconciliation, methodology, code review, test planning, experiment design, statistical planning, result verification/analysis, interpretation, manuscript drafting, claim auditing, authorized GitHub/Drive operations, exact human-execution commands, and bounded Codex prompts. ChatGPT should independently verify artifacts wherever practical.

Human execution is the default for straightforward execution:

```text
ChatGPT → exact command → Human executes → artifact produced → ChatGPT verifies
```

Codex / Antigravity / Copilot are secondary operators for bounded local tasks such as small code changes, repetitive edits, regression/smoke execution, terminal operations, and mechanical checks. Delegated tasks must specify repository/path, objective, allowed/prohibited operations, expected outputs, and stopping condition. Agents must not independently redesign the science.

## 6. External Memory Rule

AI conversational memory is NOT the project source of truth. The repository is the external project memory.

At the beginning of every significant new AI session:
1. read `docs/00_QAHBN2_MASTER.md`;
2. read `docs/01_CANONICAL_AHBN_CONTRACT.md`;
3. read the current stage file;
4. verify current repository state;
5. continue only from the documented next permitted task.

If chat history conflicts with these files, follow the files and report the conflict.

## 7. Control-Document Structure

```text
docs/
├── 00_SOURCE_AUTHORITY_REGISTER.md
├── 00_QAHBN2_MASTER.md
├── 01_CANONICAL_AHBN_CONTRACT.md
├── 02_QAHBN2_DESIGN_FREEZE.md
├── 03_EXPERIMENT_CONTRACT.md
├── 04_STATISTICAL_CONTRACT.md
├── 05_REVIEWER_LESSONS.md
├── 06_RESULTS_REGISTER.md
├── 07_CLAIM_EVIDENCE_MATRIX.md
└── stages/
    ├── S00_SOURCE_AUDIT.md
    ├── S01_RECONCILIATION.md
    ├── S02_DESIGN_FREEZE.md
    ├── S03_DEVELOPMENT.md
    ├── S04_REGRESSION_PARITY.md
    ├── S05_RL_VALIDATION.md
    ├── S06_SMOKE.md
    ├── S07_COMPLETENESS_GATE.md
    ├── S08_FORMAL_EXP10Q.md
    ├── S09_FORMAL_EXP11Q.md
    ├── S10_FORMAL_EXP12Q.md
    ├── S11_AGGREGATION.md
    ├── S12_INTERPRETATION.md
    ├── S13_MANUSCRIPT.md
    └── S14_SUBMISSION_AUDIT.md
```

Do not create unnecessary documentation beyond this unless needed.

## 8. Standard Stage Record

Every stage uses:
```markdown
# Stage
## Objective
## Authoritative inputs
## Frozen parameters
## Actions performed
## Commands executed
## Evidence produced
## Verification
## Result
## Scientific decision
## Issues / limitations
## Next permitted task
## Status
PENDING / PASS / FAIL / FROZEN
```

Update the stage record before moving to the next stage.

## 9. Source Code vs Experimental Evidence

GitHub is the versioned executable scientific record: source code, experiment definitions/configuration, scripts, tests, analysis code, documentation/control contracts, and reproducibility material.

Google Drive is the complete experimental evidence/workspace: raw results, logs, manifests, Kubernetes evidence, figures/tables, intermediate analyses, run records, large artifacts, and manuscript working evidence. Large generated experiment outputs normally remain outside Git.

## 10. Artifact Verification Principle

Assistant narration is not evidence. Artifact state is evidence. Important claims must ultimately be traceable to artifacts. Verify actual logs/outputs/source/manifests and the raw→aggregation→statistics chain rather than accepting AI/script narration.

## 11. Immutable Experiment Outputs

Every execution receives a new timestamped directory.

Simulation: `q-ahbn-<DDMMYYYYHHmmss>-<experiment>-<event>/`

GKE: `q-ahbn-gke-<DDMMYYYYHHmmss>-<experiment>-<event>/`

Never overwrite previous experiment directories. Preserve successful, failed, diagnostic, smoke, regression, formal, excluded, and rerun evidence. Scientific admissibility is documented, not implemented by deletion.

## 12. Run Metadata

Every run should contain `RUN.md` and `manifest.json`. At minimum record environment, experiment, event, timestamp, run directory, status, and scientific classification. Formal experiments additionally record where applicable Git commit SHA, software version/tag, configuration, seeds, repetitions, expected/completed runs, exclusions, failure information, and environment details.

## 13. Event Vocabulary

Approved vocabulary: `regression`, `parity`, `rl-validation`, `smoke`, `diagnostic`, `pilot`, `formal`, `rerun`, `analysis`. “Formal” means formally executed, not automatically scientifically admissible.

## 14. Q-AHBN2 Reconciliation Stage

Before code modification compare previous Q-AHBN against canonical AHBN. Audit observations, normalization, EWMA, controller score, sigmoid, mode rule, actuator, fanout values/thresholds, realized fanout, eligible neighbours, Gossip, Structured, dynamic-event handling, metrics, logging, configurations, seeds, baselines, aggregation, and statistics.

Classify components: `MATCH`, `DIFFERENT-BUT-VALID`, `MUST-UPDATE`, `INVALIDATES-OLD-RESULTS`, `NEEDS-VERIFICATION`.

Record Component, Previous Q-AHBN, Canonical AHBN, Difference, Scientific impact, Code impact, Result impact, Required action, Evidence location. No code changes before reconciliation approval.

## 15. Q-AHBN2 Design Freeze

Audit exact state representation/discretization/count, action space/semantics, reward equation/coefficients/penalties, learning rate, discount factor, epsilon/decay, Q-table initialization/update, episode definition, exploration/exploitation, learning trigger, observation/action intervals, reset/persistence.

Classify `UNCHANGED`, `ADAPT`, `INVALIDATED`, `UNRESOLVED`. Use the minimum scientifically justified adaptation necessary for compatibility; do not redesign merely to seek better performance. Once approved: **Q-AHBN2 DESIGN FREEZE.**

## 16. Metric Contract

Two classes:
- Dissemination/AHBN-comparison metrics: final AHBN Scientific Reports definitions authoritative where applicable; only verified implemented metrics such as propagation delay, duplicates, total forwards, delivery/reachability where relevant, recovery time, and resource/utilization measures where relevant.
- Learning-validation metrics: only what is necessary to establish learning behaviour, potentially reward trajectory, Q updates/value evolution, exploration/exploitation, action distribution, and state-action behaviour.

Do not claim convergence from visual flattening alone. Do not introduce a composite “Adaptation Efficiency” metric unless rigorously approved and necessary.

## 17. Manuscript Metric Hierarchy

Tier A Primary: directly answers the research question. Tier B Supporting: mechanism/boundary interpretation. Tier C Audit/evidence: preserved for integrity/reproducibility. Placement must not change merely because a result is unattractive. Material interpretation-changing evidence must be disclosed appropriately.

## 18. Statistical Contract

Follow final AHBN Scientific Reports statistical methodology wherever scientifically applicable. Before formal execution freeze independent runs, seeds, repetitions, aggregation hierarchy, summaries, variability, 95% confidence interval (95% CI), exact CI calculation, paired/unpaired structure, and effect-size/significance procedures where applicable. Never change statistical method after seeing results merely to improve presentation. Report magnitude and uncertainty.

## 19. Scientific Presentation Rule

Communicate: strongest supported finding → mechanism → quantitative evidence → uncertainty → boundary conditions → limitations.

This never permits cherry-picking seeds, excluding valid inconvenient results, redefining metrics, changing baselines/AHBN, manipulating statistics, or hiding materially interpretation-changing evidence. All evidence remains preserved.

## 20. Reviewer-Lessons Contract

Proactively distinguish controlled simulation from Kubernetes-native evidence; state exactly what CIs represent; distinguish latency among received messages from network-wide dissemination; distinguish observation from generalization. Avoid unsupported “universally superior”, “optimal”, “robust”, “reliable”, “production-ready”, “guaranteed”, “outperforming”.

Requested and realized behaviour must be distinguished. Limitations should address evaluated scale/topology, local observations, Q-table/state-space constraints, training/warm-up, parameter/deployment scope, simulation-vs-Kubernetes differences, and untested conditions. Preserve code version, configuration, seeds, repetitions, raw results, exclusions, and analysis code.

## 21. Experimental Scope Rule

Use the minimum matrix required for RO4/Q-AHBN2. Candidate dynamic scenarios from previous Q-AHBN are Failure, Churn, Heterogeneity, but each must be re-verified under canonical AHBN.

For each experiment specify research question, baseline, treatment, topology, N, seeds, repetitions, event/parameters, metrics, outputs, aggregation, and validity criteria. Principal comparison is expected to be Frozen AHBN vs Q-AHBN2. Additional baselines require a specific purpose.

## 22. Test Pipeline

```text
Development
 ↓
Regression
 ↓
Canonical AHBN parity
 ↓
Q-learning logic tests
 ↓
Deterministic RL sanity validation
 ↓
Smoke tests
 ↓
Completeness Gate
 ↓
Formal experiments
 ↓
Aggregation validation
 ↓
Statistical validation
 ↓
Scientific interpretation
```

Do not skip directly to formal experiments. Distinguish implementation failure, experimental failure, and scientifically valid negative result.

## 23. Completeness Gate — Last Point for Experiment Design

After smoke and before formal experiments ask whether the frozen matrix will provide all evidence needed to answer Q-AHBN2 and prepare the manuscript. Check scenarios, baselines, metrics/logging, seeds/repetitions, statistics, learning evidence, Kubernetes evidence, and metadata.

If YES: **EXPERIMENT CONTRACT FROZEN.** After this: no new scenarios/metrics/baselines/hyperparameter exploration/AHBN changes/Q-AHBN2 redesign/scope expansion. Additional execution only corrects a documented validity problem.

## 24. Formal Experiment Rule

Formal experiments execute only the frozen contract. Never rerun merely because results are disappointing. Valid rerun reasons: implementation defect, configuration error, corrupted/incomplete output, methodological inconsistency, or infrastructure failure affecting validity. Document every rerun/exclusion. After completion: **FORMAL DATASET FREEZE.**

## 25. Aggregation Rule

```text
Raw evidence → validated runs → aggregation script → summary statistics → 95% CI → tables → figures
```

Never manually copy numbers where reproducible automation is available. Validate expected run counts before interpretation.

## 26. Scientific Interpretation Rule

Do not begin with “Did Q-AHBN2 win?” Ask what happened, magnitude, uncertainty, consistency, conditions, plausible mechanism, supported/unsupported conclusions, and exposed limitations. Legitimate outcomes include clear/modest/metric-specific/condition-dependent improvement, trade-off, approximate equivalence, no improvement, or degradation.

## 27. Claim–Evidence Register

Before manuscript finalization every major claim maps to Claim, Experiment, Metric, Numerical result, 95% CI/statistical evidence, Figure/Table, Boundary, Limitation. Store in `07_CLAIM_EVIDENCE_MATRIX.md`.

## 28. Q-AHBN2 Paper Identity

This is not Paper 1/RO1. Previously published work already established cloud-native simulation framework, Kubernetes deployment, Gossip implementation, observability, resource utilization, and scalability. Do not substantially re-explain Kubernetes/GKE/Pods/YAML/generic cloud-native concepts/Gossip fundamentals/previous observability architecture.

Position concisely: “Building upon the cloud-native simulator introduced by Wira et al. (2025), this work proposes and evaluates a reinforcement-learning-enhanced dissemination control mechanism.”

## 29. Target Manuscript Structure

Target approximately 28–35 A4 pages:
1. Introduction (~3 pp): dissemination trade-off, static limitation, AHBN, learning opportunity, Q-AHBN2, contributions.
2. Related Work (~3 pp): only dissemination/adaptation/RL literature needed for positioning.
3. Q-AHBN2 Design (~6–7 pp): concise frozen AHBN foundation, architecture, state/action/reward/parameters/interaction/pseudocode.
4. Experimental Methodology (~3 pp): Q-AHBN2-specific environment/scenarios/baselines/parameters/seeds/repetitions/metrics/statistics and simulation-vs-Kubernetes distinction.
5. Learning Validation (~2–3 pp): meaningful learning/adaptation evidence; no unsupported convergence claim.
6. Controlled Evaluation (~6–7 pp): tentative Failure/Churn/Heterogeneity, subject to experiment freeze.
7. Kubernetes-Native Realism Validation (~4–5 pp): only required frozen-contract experiments.
8. Discussion (~2–3 pp): what learning changes, cross-scenario trade-offs, practical implications, limitations.
9. Conclusion/Future Work (~1–2 pp): answer from actual evidence, not predetermined winners.

Figures/tables are provisional and evidence-driven.

## 30. Manuscript Figure/Table Rule

Every final artifact must support a scientific claim. Consolidate redundant figures. Prefer fewer, stronger, evidence-rich figures.

## 31. Paper Writing Order

After experimental freeze:
1. Results tables/figures
2. Results prose
3. Q-AHBN2 Design
4. Experimental Methodology
5. Discussion + Limitations
6. Introduction
7. Related Work
8. Conclusion
9. Abstract
10. Final claim/reviewer audit

## 32. Scientific Reports Pre-Review Gate

Audit Results, Scope, Statistics, Claims, Mechanism, Limitations, Prior work, and Reproducibility. If any are inadequate, manuscript is not submission-ready.

## 33. Seven-Day Science/Experiment Sprint

Day 1: source audit + canonical reconciliation; record S00/S01; no code modification before approval.
Day 2: scientific freeze; design, metric/statistical contracts, minimum experiment matrix.
Day 3: minimal development + regression + canonical parity.
Day 4: RL validation.
Day 5: smoke + Completeness Gate; after PASS freeze experiment contract.
Days 6–7: formal learning/failure/churn/heterogeneity controlled and required Kubernetes execution; validate, aggregate, compute statistics/95% CI, freeze dataset, begin interpretation.

## 34. Five-Day Manuscript Sprint

Day 8: figures/tables/Results. Day 9: Design/Methodology/Learning Validation. Day 10: Discussion/Limitations/Implications. Day 11: Introduction/Related Work/Conclusion/Abstract. Day 12: claim-evidence, reviewer, citation, figure/table, reproducibility, formatting and compilation audits.

## 35. Scope-Control Rule

Operate under **MINIMUM SCIENTIFICALLY SUFFICIENT WORK**. Add work only if necessary for scientific validity, RO4, manuscript acceptance/reproducibility, or correction of a genuine defect. Otherwise do not add it.

## 36. Automation Rule

Automate repetition, not scientific judgment. Appropriate automation includes directories, manifests, loops, run counts, CI calculations, aggregation, figures/tables, parity and regression checks. Human/ChatGPT judgment remains required for scope, exclusions, interpretation, conclusions, and methodology changes.

## 37. Cost-Control Rule

Priority:
```text
1. ChatGPT directly
2. ChatGPT + human execution
3. ChatGPT + bounded Codex/agent execution
```

Use agents only when they materially save time or reduce mechanical error.

## 38. Failure Handling

```text
STOP → classify failure → record evidence → minimum correction → approve → execute → verify → continue
```

Never casually redesign the project in response to failure.

## 39. Freeze Hierarchy

```text
AHBN FREEZE
 ↓
Q-AHBN2 DESIGN FREEZE
 ↓
METRIC FREEZE
 ↓
STATISTICAL FREEZE
 ↓
EXPERIMENT FREEZE
 ↓
CODE/FORMAL-RUN FREEZE
 ↓
DATASET FREEZE
 ↓
INTERPRETATION FREEZE
 ↓
MANUSCRIPT FREEZE
 ↓
SUBMISSION
```

Later stages must not silently modify earlier frozen stages. Reopening requires explicit documentation and scientific justification.

## 40. Master Workflow

```text
START
→ Load master/control documents
→ Verify latest repositories
→ Audit previous Q-AHBN
→ Compare against canonical AHBN
→ Reconciliation approved
→ Freeze Q-AHBN2 design
→ Freeze metrics/statistics/experiment matrix
→ Minimal development
→ Regression
→ AHBN parity
→ RL validation
→ Smoke
→ COMPLETENESS GATE
→ EXPERIMENT FREEZE
→ Formal experiments
→ Artifact verification
→ DATASET FREEZE
→ Aggregation + 95% CI
→ Evidence-first interpretation
→ CLAIM–EVIDENCE MATRIX
→ Results/figures/tables
→ Manuscript
→ Scientific Reports reviewer-style audit
→ Reproducibility audit
→ MANUSCRIPT FREEZE
→ SUBMIT
```

## 41. Master Principles

1. Canonical AHBN is frozen and immutable.
2. Q-AHBN2 learns over AHBN; it does not rewrite AHBN.
3. Repository and artifact state outrank AI memory and narration.
4. ChatGPT is the primary AI assistant; human execution is the default.
5. Codex and other agents are bounded secondary operators.
6. The human researcher retains scientific authority.
7. Experiment design freezes before formal execution.
8. Formal evidence is never rerun merely because it is disappointing.
9. All evidence is preserved even when not all evidence appears prominently in the manuscript.
10. Present the strongest supported scientific story without overstating or manipulating evidence.
11. Use AHBN Scientific Reports methodology/reviewer lessons wherever applicable.
12. Separate controlled simulation from Kubernetes-native evidence.
13. Report uncertainty, including 95% CI, with clearly defined scope.
14. Automate repetitive work; do not automate scientific judgment.
15. Use .md control records as persistent external AI/project memory.
16. Do not repeat RO1 contributions in the Q-AHBN2 manuscript.
17. Use minimum scientifically sufficient experiments, metrics, figures, and prose.
18. Negative, mixed, modest, or condition-dependent results are scientific results—not automatic failures.
19. No scope expansion after Completeness Gate unless scientific validity requires it.
20. Finish the research that was designed rather than continuously redesigning it.

## 42. New-Session Bootstrap Prompt

> Read `docs/00_SOURCE_AUTHORITY_REGISTER.md`, `docs/00_QAHBN2_MASTER.md`, `docs/01_CANONICAL_AHBN_CONTRACT.md`, and the current stage `.md` file before doing anything else.
>
> Treat those files and verified repository state as authoritative. Verify the latest approved Q-AHBN2 state. Canonical AHBN is frozen and MUST NOT be altered.
>
> If code, manuscript text, chat context, AI memory, or previous Q-AHBN assumptions conflict with canonical AHBN or frozen contracts, STOP and report the conflict.
>
> Perform only the current permitted stage. Do not expand experiments, alter frozen parameters, add metrics, modify seeds/repetitions, change statistical procedures, or redesign Q-AHBN2 without explicit researcher approval.
>
> At completion, verify actual artifacts and update the appropriate stage record with evidence, result, decision, limitations, status, and next permitted task.

## 43. Definition of Done

Q-AHBN2 is complete when canonical AHBN parity is verified; Q-AHBN2 design is frozen; regression/RL validation/smoke/Completeness Gate pass; formal experiments complete; raw evidence is preserved; aggregation/statistics and required 95% CIs are complete; scientific interpretation and claim-evidence mapping are frozen; manuscript, reviewer-style audit, and reproducibility audit are complete; and the manuscript is submission-ready.

> **STOP EXPERIMENTING. SUBMIT THE PAPER.**
