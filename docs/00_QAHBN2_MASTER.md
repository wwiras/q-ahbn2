# Q-AHBN2 Master Research, Development, Experiment and Publication Contract v1.0

**Project:** Q-AHBN2  
**Repository:** `wwiras/q-ahbn2`
**Canonical path:** `docs/00_QAHBN2_MASTER.md`  
**Status:** FROZEN MASTER OPERATING CONTRACT  
**Date frozen:** 2026-09-19

---

# 0. Current Project State and Entry Gate

The repository name is frozen as `q-ahbn2`.

The pre-S00 infrastructure workflow has been completed and independently verified:

| Gate | Status |
|---|---|
| Repository name freeze | PASS |
| GitHub repository creation | PASS |
| GitHub workflow smoke test | PASS |
| Google Drive evidence smoke test | PASS |
| Workflow readback verification | PASS |
| Master workflow update/freeze | PASS |
| `00_QAHBN2_MASTER.md` | THIS DOCUMENT |
| S00 entry gate at infrastructure freeze | PASSED / HISTORICAL |

Verified workflow-smoke GitHub commit:

`1c01735b071b33a7bd28afdc60785d551b36489f`

The smoke test proved the operational path:

```text
ChatGPT / bounded operator
        ↓
GitHub source/control record
        ↓
local human/operator execution
        ↓
generated artifact
        ↓
Google Drive evidence storage
        ↓
artifact readback verification
```

This infrastructure smoke test is not scientific Q-AHBN2 evidence and does not constitute S00, development, RL validation, or a formal experiment.

At the time of the pre-S00 infrastructure freeze, the next permitted scientific task was **S00 — Source Audit**. This statement is retained only as historical provenance; current scientific stage/status is governed by the current stage/control document and verified repository state.

---

# 1. Purpose

This document is the authoritative operating template for the Q-AHBN2 project from initial reconciliation through development, validation, formal experimentation, statistical analysis, scientific interpretation, manuscript preparation, and submission.

Q-AHBN2 is the redesign/reconciliation of the previous Q-AHBN implementation so that it operates on the latest frozen canonical AHBN.

This document exists to prevent:

- inconsistency across AI conversations;
- accidental modification of canonical AHBN;
- uncontrolled experiment expansion;
- loss of scientific provenance;
- unnecessary repeated work;
- post-hoc metric or parameter changes;
- dependence on AI conversational memory;
- unnecessary Codex/agent cost;
- manuscript claims drifting away from experimental evidence.

The project should remain as simple as possible while preserving scientific validity, reproducibility, traceability, and publication quality.

---

# 2. Project Objective

The scientific dependency is:

```text
RO1
Cloud-native evaluation framework
        ↓
RO2
Characterisation of dissemination trade-offs
        ↓
RO3
Frozen canonical AHBN
        ↓
RO4
Q-AHBN2 learning enhancement
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

Q-AHBN2 investigates whether a lightweight Q-learning layer can enhance adaptation over the already-frozen canonical AHBN under evaluated dynamic network conditions.

Q-AHBN2 does NOT redesign AHBN.

---

## 2.1 Current Conceptual Architecture — RO2 → Frozen AHBN → Q-AHBN2

This subsection is the compact conceptual map for the current Q-AHBN2 design. It is intended to evolve gradually as S02 decisions are completed. Detailed frozen semantics remain authoritative in `docs/01_CANONICAL_AHBN_CONTRACT.md` and `docs/02_QAHBN2_DESIGN_FREEZE.md`.

The scientific progression is:

```text
RO2 — CHARACTERIZE
What dissemination trade-offs and dynamic-condition effects exist?
        ↓
RO3 — ADAPT
Frozen canonical AHBN responds deterministically to local observations.
        ↓
RO4 — LEARN
Q-AHBN2 learns bounded refinements of the AHBN proposal from experience.
```

In compact form:

```text
RO2 evidence
  • fanout ↔ propagation-delay / duplication trade-off
  • Gossip ↔ robustness with higher redundancy
  • Structured ↔ efficiency with greater dynamic-condition fragility
  • failure / overload / churn change dissemination behaviour
  • heterogeneity reduces efficiency
        ↓
        │ defines the adaptation problem
        ↓
Local canonical observations
  duplication, latency, utilization, churn
        ↓
FROZEN CANONICAL AHBN
  canonical normalization + EWMA
        ↓
  z = -d + l + u + c
        ↓
  canonical mode + S5 fanout proposal
        ↓
  (mode_AHBN, k_AHBN)
        ↓
        │ deterministic proposal; AHBN remains immutable
        ↓
Q-AHBN2 LEARNING LAYER
  construct frozen discrete state from the canonical observations
        ↓
  select one bounded meta-action:
    KEEP
    FANOUT_DOWN
    FANOUT_UP
    SET_GOSSIP
    SET_STRUCTURED
        ↓
  refine the AHBN proposal only
        ↓
  (mode_Q, k_Q)
        ↓
eligible-target realization + forwarding
        ↓
direct attributable outcomes
  NEW | DUPLICATE | FAILED
        ↓
reward evidence
        ↓
learn / update Q(s,a)
        └────────────────────────→ future Q-AHBN2 decisions
```

The conceptual runtime cycle is therefore:

```text
OBSERVE
   ↓
AHBN ADAPT
   ↓
Q-AHBN2 REFINE
   ↓
EXECUTE
   ↓
OUTCOME
   ↓
LEARN
   └──────────────↺
```

The central interpretation is:

> **AHBN deterministically adapts dissemination to the observed network condition; Q-AHBN2 learns whether a bounded refinement of that AHBN decision is useful from experience.**

Accordingly, Q-AHBN2 is **not** a replacement controller and does not select a policy before AHBN executes. Canonical AHBN is evaluated first and produces the independently traceable proposal `(mode_AHBN, k_AHBN)`. Q-AHBN2 acts only at the approved post-AHBN intervention boundary.

RO2 is the scientific problem authority for why the adaptation dimensions matter; it does not directly prescribe a Q-AHBN2 action, reward, learning parameter, or numerical hyperparameter. Frozen AHBN supplies the deterministic adaptive baseline. Q-AHBN2 tests whether experience-based bounded refinement can enhance that baseline under the evaluated conditions.

### 2.1.1 Current design boundary

The following conceptual boundaries are already established:

- canonical AHBN sensing, normalization, EWMA, score, sigmoid, mode rule, S5 thresholds, and proposal generation remain immutable;
- Q-AHBN2 uses the canonical local-condition dimensions rather than privileged failure/event labels;
- Q-AHBN2 intervention is post-AHBN and bounded to the frozen Q-AHBN2 action contract;
- forwarding outcomes provide locally attributable learning evidence;
- requested/refined behaviour remains distinct from realized behaviour under eligible-neighbour constraints.

The temporal transition semantics have now been resolved conceptually by AR-1.1–AR-1.2: for a decision at peer $p$, $s_{t+1}$ is the frozen Q-AHBN2 state observed at that same peer's next Q-AHBN2 decision opportunity, while $R_t$ remains owned by the originating action's direct-attempt attribution record even if reward closure is delayed or out of order. Implementation readiness for this concurrent bookkeeping remains pending under AR-1.4.1.

**Historical note (superseded by AR-1.4.4):** future-value bootstrapping was retained while the historical `gamma=0.90` was reopened over the bounded candidate set `{0.70,0.80,0.90}`. That selection process is now complete. The current authoritative Q-AHBN2 discount factor is **`gamma=0.70` FROZEN**.

---

# 3. Absolute Scientific Rule — Canonical AHBN Is Immutable

The latest approved canonical AHBN is a READ-ONLY scientific dependency.

Q-AHBN2 MUST follow canonical AHBN exactly.

This includes, where applicable:

- observation definitions;
- normalization;
- EWMA formulation;
- EWMA parameters;
- controller score;
- sigmoid transformation;
- mode-selection rule;
- fanout actuator;
- fanout thresholds;
- supported fanout values;
- eligible-neighbour handling;
- realized fanout;
- Gossip semantics;
- Structured semantics;
- baseline semantics;
- associated metric definitions.

The canonical AHBN implementation and latest approved AHBN Scientific Reports manuscript are the authorities.

The previous Q-AHBN implementation is NOT authoritative when it conflicts with canonical AHBN.

Q-AHBN2 may learn over or influence explicitly permitted AHBN operating decisions according to the approved Q-AHBN2 design.

Q-AHBN2 MUST NOT silently:

- change AHBN equations;
- change AHBN thresholds;
- change AHBN normalization;
- change AHBN EWMA;
- change AHBN fanout mapping;
- change AHBN baseline behaviour;
- modify AHBN merely to improve Q-AHBN2 performance.

If Q-AHBN2 performs poorly under canonical AHBN, that is a Q-AHBN2 result or design issue.

AHBN is not reopened.

---

# 4. Authority Hierarchy

When sources disagree, use this hierarchy.

## Level 1 — Frozen canonical authority

1. Latest approved canonical AHBN repository.
2. Latest revised/frozen AHBN Scientific Reports manuscript.
3. Final AHBN experimental/statistical artifacts where applicable.

## Level 2 — Q-AHBN2 frozen authority

After reconciliation:

4. `00_QAHBN2_MASTER.md`
5. `01_CANONICAL_AHBN_CONTRACT.md`
6. `02_QAHBN2_DESIGN_FREEZE.md`
7. `03_EXPERIMENT_CONTRACT.md`
8. `04_STATISTICAL_CONTRACT.md`

## Level 3 — Historical reference

9. Previous Q-AHBN repository.
10. Previous Q-AHBN manuscript.
11. Previous Q-AHBN experimental outputs.

Historical material may guide Q-AHBN2 but cannot override frozen canonical AHBN.

## Level 4 — Conversational context

ChatGPT memory, previous conversations, Codex narration, researcher recollection, and informal notes are supporting context only.

If they conflict with repository evidence or frozen control documents:

> Repository/artifact state wins.

---

# 5. Human and AI Roles

## 5.1 Human Researcher

The researcher remains the scientific authority.

The researcher approves:

- research objectives;
- Q-AHBN2 design;
- experimental matrix;
- formal parameters;
- seeds;
- repetitions;
- baselines;
- metrics;
- statistical methodology;
- formal experiment status;
- exclusions/reruns;
- scientific interpretation;
- changes to frozen methodology.

AI execution does not constitute scientific authorization.

## 5.2 ChatGPT — Primary AI Assistant

ChatGPT is the first-priority AI assistant.

Use ChatGPT first for:

- scientific reasoning;
- repository inspection;
- canonical reconciliation;
- methodology;
- code review;
- test planning;
- experiment design;
- statistical planning;
- result verification;
- result analysis;
- interpretation;
- manuscript drafting;
- claim auditing;
- GitHub read/write when authorized;
- Google Drive read/write when authorized;
- exact human-execution commands;
- bounded Codex prompts.

ChatGPT should independently verify artifacts wherever practical.

## 5.3 Human Execution — Default

If execution is straightforward, ChatGPT prepares the exact command and the researcher runs it.

Default:

```text
ChatGPT
   ↓
exact command
   ↓
Human executes
   ↓
artifact produced
   ↓
ChatGPT verifies
```

This is the preferred workflow.

## 5.4 Codex / Antigravity / Copilot — Secondary Operators

Use execution agents only when they materially simplify a bounded local task.

Appropriate examples:

- small code changes;
- repetitive edits;
- regression execution;
- smoke execution;
- terminal operations;
- mechanical checks.

Every delegated task should specify:

- repository/path;
- objective;
- allowed operations;
- prohibited operations;
- expected outputs;
- stopping condition.

Execution agents must not independently redesign the science.

---

# 6. External Memory Rule

AI conversational memory is NOT the project source of truth.

The repository is the external project memory.

At the beginning of every significant new AI session:

1. read `00_QAHBN2_MASTER.md`;
2. read `01_CANONICAL_AHBN_CONTRACT.md`;
3. read the current stage file;
4. verify current repository state;
5. continue only from the documented next permitted task.

If chat history conflicts with these files, follow the files and report the conflict.

---

# 7. Control-Document Structure

Maintain:

```text
docs/qahbn2/
│
├── 00_QAHBN2_MASTER.md
├── 01_CANONICAL_AHBN_CONTRACT.md
├── 02_QAHBN2_DESIGN_FREEZE.md
├── 03_EXPERIMENT_CONTRACT.md
├── 04_STATISTICAL_CONTRACT.md
├── 05_REVIEWER_LESSONS.md
├── 06_RESULTS_REGISTER.md
├── 07_CLAIM_EVIDENCE_MATRIX.md
│
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

---

# 8. Standard Stage Record

Every stage uses the same compact format:

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

The stage record should be updated before moving to the next stage.

---

# 9. Source Code vs Experimental Evidence

## 9.1 GitHub — Authoritative Code and Control Record

GitHub is the versioned executable scientific record.

Store:

- source code;
- experiment definitions;
- configuration;
- scripts;
- tests;
- analysis code;
- documentation;
- control contracts;
- reproducibility material.

The authoritative Q-AHBN2 repository is:

`wwiras/q-ahbn2`

Large generated experiment outputs normally remain outside Git.

## 9.2 Local Workspace — Execution Area, Not Evidence Authority

The local working repository is used to:

- edit/pull code;
- execute tests;
- execute experiments;
- generate temporary/working outputs;
- inspect artifacts before preservation.

The current local repository may reside inside a Google Drive Desktop synchronized path. Therefore Drive may automatically synchronize repository files, `.git/`, ignored `output/` directories, and other working files.

Automatic Drive synchronization does **not** make those synchronized working files authoritative experimental evidence.

In particular:

> A synchronized local `output/` directory is working output unless it has passed the required validity checks and is deliberately preserved in the designated authoritative evidence location.

## 9.3 Google Drive — Authoritative Experimental Evidence

Google Drive is the complete experimental evidence store.

Store deliberately preserved evidence such as:

- raw results;
- logs;
- manifests;
- Kubernetes evidence;
- figures;
- tables;
- intermediate analyses;
- run records;
- large artifacts;
- manuscript working evidence.

The Q-AHBN2 Drive root is identified by folder ID:

`1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`

For scientific provenance, the designated evidence hierarchy inside this root—not incidental DriveFS synchronization—determines the authoritative experimental evidence.

## 9.4 Evidence Promotion Rule

The conceptual flow is:

```text
GitHub exact code/config
        ↓
local execution
        ↓
working output
        ↓
validity/completeness verification
        ↓
deliberate preservation in designated Drive evidence area
        ↓
readback verification
        ↓
authoritative experimental evidence
```

For formal experiments, the preserved evidence must be traceable back to the exact Git commit/configuration that produced it.

If a synchronized working copy and a deliberately preserved evidence copy both exist, the deliberately preserved evidence location is authoritative.

---

# 10. Artifact Verification Principle

Assistant narration is not evidence.

Artifact state is evidence.

Examples:

```text
Codex: "test passed"
        ↓
inspect actual output/log

ChatGPT: "repository uses formula X"
        ↓
inspect source

Script: "formal run completed"
        ↓
verify manifest + expected runs + raw files

Analysis: "Q-AHBN2 improved metric X"
        ↓
verify raw → aggregation → statistics
```

Every important scientific claim should ultimately be traceable to an artifact.

---

# 11. Immutable Experiment Outputs

Every execution receives a new timestamped directory.

Simulation:

```text
q-ahbn-<DDMMYYYYHHmmss>-<experiment>-<event>/
```

GKE:

```text
q-ahbn-gke-<DDMMYYYYHHmmss>-<experiment>-<event>/
```

Never overwrite previous experiment directories.

Preserve successful runs, failed runs, diagnostics, smoke tests, regression runs, formal runs, excluded runs, and reruns.

Scientific admissibility is documented, not implemented by deletion.

---

# 12. Run Metadata

Every run should contain:

```text
RUN.md
manifest.json
```

At minimum record:

- environment;
- experiment;
- event;
- timestamp;
- run directory;
- status;
- scientific classification.

Formal experiments should additionally record where applicable:

- Git commit SHA;
- software version/tag;
- configuration;
- seeds;
- repetitions;
- expected runs;
- completed runs;
- exclusions;
- failure information;
- environment details.

---

# 13. Event Vocabulary

Approved vocabulary includes:

```text
regression
parity
rl-validation
smoke
diagnostic
pilot
formal
rerun
analysis
```

`formal` means formally executed.

It does not automatically mean scientifically admissible.

---

# 14. Q-AHBN2 Reconciliation Stage

Before code modification, compare previous Q-AHBN against canonical AHBN.

Audit at minimum:

- observations;
- normalization;
- EWMA;
- controller score;
- sigmoid;
- mode rule;
- actuator;
- fanout values;
- thresholds;
- realized fanout;
- eligible neighbours;
- Gossip;
- Structured;
- dynamic-event handling;
- metrics;
- logging;
- configurations;
- seeds;
- baselines;
- aggregation;
- statistics.

Classify every component:

```text
MATCH
DIFFERENT-BUT-VALID
MUST-UPDATE
INVALIDATES-OLD-RESULTS
NEEDS-VERIFICATION
```

Record:

```text
Component
Previous Q-AHBN
Canonical AHBN
Difference
Scientific impact
Code impact
Result impact
Required action
Evidence location
```

No code changes before this reconciliation is approved.

---

# 15. Q-AHBN2 Design Freeze

Audit the existing learning mechanism.

Verify exact:

- state representation;
- state discretization;
- state count;
- action space;
- action semantics;
- reward equation;
- reward coefficients;
- penalty conditions;
- learning rate;
- discount factor;
- epsilon;
- epsilon decay;
- Q-table initialization;
- Q-update;
- episode definition;
- exploration/exploitation;
- learning trigger;
- observation interval;
- action interval;
- reset/persistence.

Classify:

```text
UNCHANGED
ADAPT
INVALIDATED
UNRESOLVED
```

Use the minimum scientifically justified adaptation necessary to make previous Q-AHBN compatible with canonical AHBN.

Do not redesign merely to seek better performance.

Once approved:

> Q-AHBN2 DESIGN FREEZE.

---


## 15.1 S02 Design Freeze Master Completion Checklist

This checklist is the authoritative completion map for **S02 — Q-AHBN2 Design Freeze**. It is derived directly from the exact verification requirements in Section 15 and must be reconciled against repository evidence rather than conversational memory.

A row marked **PASS / FROZEN** means the corresponding Section 15 requirement is already explicitly resolved by a frozen Q-AHBN2 design contract. **VERIFY / RECONCILE** means evidence may exist but has not yet been reconciled into the S02 master completion status. **PENDING** means a design decision remains to be completed.

| ID | S02 requirement | Section 15 coverage | Verified repository evidence | Status |
|---|---|---|---|---|
| A | Architecture / AHBN intervention boundary | prerequisite to exact learning mechanism | DOC-02 Sections 02.1--02.2 | **PASS / FROZEN** |
| B | State representation | state representation | DOC-02 Section 02.3 | **PASS / FROZEN** |
| C | State discretization + state count | state discretization; state count | DOC-02 Section 02.4: 3 bins x 4 dimensions = 81 states | **PASS / FROZEN** |
| D | Action space + action semantics | action space; action semantics | DOC-02 Section 02.5: 5 actions; 81 x 5 = 405 Q cells | **PASS / FROZEN** |
| E | Reward contract | reward equation; reward coefficients/magnitudes; penalty/zero-evidence conditions | DOC-02 Section 02.6 | **PASS / COMPLETE / FROZEN** |
| F | Learning parameters | learning rate; discount factor; epsilon; epsilon decay | DOC-02 Section 02.7 + Source Authority Register Section 12 | **PASS / COMPLETE / FROZEN** |
| G | Q-learning mechanics | Q-table initialization; Q-update; exploration/exploitation | DOC-02 Section 02.8 + Source Authority Register Section 13 | **PASS / COMPLETE / FROZEN** |
| H | Learning lifecycle | episode definition; learning trigger; observation interval; action interval; reset/persistence | DOC-02 02.9 + later AR transition/lifecycle closures | **PASS / COMPLETE / FROZEN** |
| I | Cross-platform / AHBN-boundary audit | design-level compatibility of the complete learning mechanism with immutable AHBN and one logical ControlSim/Kubernetes learning contract | S02-CLOSE-C1 reconciliation; implementation/regression parity remains later-stage work | **PASS / DESIGN-LEVEL RECONCILED** |
| J | Final S02 closure audit | all Section 15 requirements resolved; no hidden design choice remains | S02-CLOSE audit held for C1 corrections | **READY FOR RE-AUDIT AFTER C1** |

### 15.1.1 Historical S02 position before later lifecycle / C1 closures — SUPERSEDED

> **Historical status only — SUPERSEDED.** The block below records the earlier S02 position before the later lifecycle/transition closures and S02-CLOSE-C1 reconciliation. It is preserved for provenance and is not the current project status.

```text
HISTORICAL / SUPERSEDED:
S02 — Q-AHBN2 DESIGN FREEZE = IN PROGRESS

A Architecture                         PASS / FROZEN
B State representation                PASS / FROZEN
C State discretization + count        PASS / FROZEN
D Action space + semantics            PASS / FROZEN
E Reward                              PASS / COMPLETE / FROZEN
F Learning parameters                 PASS / COMPLETE / FROZEN
G Q-learning mechanics                PASS / COMPLETE / FROZEN
H Learning lifecycle                  HISTORICAL — later PASS / COMPLETE / FROZEN
I Cross-platform / AHBN-boundary      HISTORICAL — later PASS / DESIGN-LEVEL RECONCILED
J Final S02 closure audit             HISTORICAL — later advanced to C1/C2 re-audit
```

**Current authority:** H is PASS / COMPLETE / FROZEN; I is PASS / DESIGN-LEVEL RECONCILED; J is awaiting the post-C2 static S02-CLOSE re-audit. No scientific decision in H or I is currently unresolved.

### 15.1.1A S02-F closure record

S02-F was reconciled as one bounded work package on 2026-09-21. **Historical S02-F initially carried `gamma=0.90`; AR-1.4.4 later superseded that numerical value.** Current frozen values are `alpha_Q=0.25`, `gamma=0.70`, `epsilon_0=0.30`, `epsilon_min=0.03`, and multiplicative `epsilon_decay=0.995`. Historical ControlSim and GKE sources were compared explicitly; RO2 was used to constrain the scientific rationale without claiming hyperparameter optimality; canonical AHBN `alpha_AHBN=0.30` remains immutable and distinct.

### 15.1.1B Current blocking decision

S02-H exposed a validity-critical concurrency issue when the frozen per-new-message action/reward contract is combined with one-step Q-learning: multiple message-attribution windows may overlap at a peer. DOC-02 Section 02.9 records alternatives and recommends concurrent per-message transition records with $s_{t+1}$ sampled at that action's closure. This is an L3 lifecycle decision and is the current stopping boundary.

### 15.1.2 S02 completion contract

The remaining work SHALL be executed as coherent bounded work packages, not as an automatically expanding sequence of microscopic gates:

```text
F — Learning Parameters
    alpha
    gamma
    epsilon
    epsilon decay
        ↓
G — Q-Learning Mechanics
    Q-table initialization
    Q-update
    exploration/exploitation
        ↓
H — Learning Lifecycle
    episode definition
    learning trigger
    observation interval
    action interval
    reset/persistence
        ↓
I — Cross-Platform / AHBN-Boundary Audit
        ↓
J — Final S02 Closure Audit
        ↓
Q-AHBN2 DESIGN FREEZE = PASS / COMPLETE / FROZEN
```

Where scientifically efficient, F and G may be executed together as the accelerated **Learning Configuration** block, provided every individual Section 15 requirement remains explicitly checked and recorded. H may be reconciled with the relevant training/evaluation contract only where doing so does not leave an unstated design choice in S02.

No completed A--E item may be reopened merely for optimization. Reopening requires a documented validity defect or higher-authority contradiction.

### 15.1.3 Delegated execution rule for S02

For each remaining item F--J:

1. read the latest master, source-authority register, canonical AHBN contract, and current design contract;
2. execute bounded L1 verification directly where the decision is already implied by frozen evidence;
3. for conventional L2 choices, analyze and recommend a scientifically defensible setting without searching for global optimum;
4. stop for explicit researcher decision if an L3 scientific assumption or validity-changing choice is encountered;
5. log unexpected validity-critical checks with provenance and result;
6. update this checklist and the detailed design record when the work package closes;
7. proceed to the next documented unresolved item.

The S02 exit condition is:

```text
Q-AHBN2 DESIGN FREEZE = PASS / COMPLETE / FROZEN
```

Only after that closure may the project advance to the remaining metric/statistical/experiment-contract freeze and then S03 Development.

# 16. Metric Contract

Use two metric classes.

## A. Dissemination / AHBN-comparison metrics

The final AHBN Scientific Reports definitions are authoritative wherever applicable.

Candidate metrics include only verified implemented metrics such as:

- propagation delay;
- duplicates;
- total forwards;
- delivery/reachability measure where scientifically relevant;
- recovery time;
- resource/utilization measures where relevant.

Exact definitions must be frozen before formal experiments.

## B. Learning-validation metrics

Use only what is necessary to establish learning behaviour, potentially:

- reward trajectory;
- Q updates;
- Q-value evolution;
- exploration/exploitation;
- action distribution;
- state-action behaviour.

Do not claim convergence from visual flattening alone.

Do not introduce a new composite metric such as "Adaptation Efficiency" unless it already has a rigorous, approved mathematical definition and provides necessary information not adequately represented by existing metrics.

---

# 17. Manuscript Metric Hierarchy

Before formal results are known, classify metrics:

## Tier A — Primary

Directly answer the Q-AHBN2 research question.

Expected main-text figures/tables.

## Tier B — Supporting

Help interpret the mechanism or boundary conditions.

May appear in main text, supplementary material, or concise tables.

## Tier C — Audit / evidence

Preserved for scientific integrity and reproducibility but not necessarily shown prominently.

Metric placement must not be changed merely because a result is unattractive.

A result that materially changes the interpretation of Q-AHBN2 must be disclosed appropriately even if it is unfavorable.

---

# 18. Statistical Contract

Follow the final AHBN Scientific Reports statistical methodology wherever scientifically applicable.

Before formal execution freeze:

- number of independent runs;
- seeds;
- repetitions;
- aggregation hierarchy;
- mean/other summaries;
- variability measure;
- 95% confidence interval;
- exact CI calculation;
- paired/unpaired structure;
- effect-size/significance procedures where applicable.

The phrase is:

> 95% confidence interval (95% CI)

Never invent or change the statistical method after seeing results merely to improve presentation.

Report magnitude and uncertainty.

---

# 19. Scientific Presentation Rule

The manuscript should communicate the strongest scientifically supported contribution.

Use:

```text
strongest supported finding
        ↓
mechanism
        ↓
quantitative evidence
        ↓
uncertainty
        ↓
boundary conditions
        ↓
limitations
```

This is strategic scientific communication.

It is NOT permission to cherry-pick seeds, exclude valid inconvenient results, redefine metrics after results, change baselines, alter AHBN, manipulate statistics, or hide evidence that materially changes interpretation.

All evidence remains preserved.

---

# 20. Reviewer-Lessons Contract

Use lessons from the AHBN Scientific Reports review proactively.

`05_REVIEWER_LESSONS.md` should include at minimum:

## Accurate reporting

- distinguish controlled simulation from Kubernetes-native evidence;
- state exactly what confidence intervals represent;
- distinguish latency among received messages from network-wide dissemination;
- distinguish experimental observation from generalization.

## Claim control

Avoid unsupported:

- universally superior;
- optimal;
- robust;
- reliable;
- production-ready;
- guaranteed;
- outperforming.

## Requested vs realized behaviour

If Q-AHBN2 requests an action that topology or resource conditions constrain:

```text
requested action ≠ realized action
```

Report the distinction.

## Limitations

Proactively address evaluated scale, topology, local observations, Q-table/state-space constraints, training/warm-up, parameter scope, deployment scope, simulation-vs-Kubernetes differences, and untested conditions.

## Reproducibility

Preserve code version, configuration, seeds, repetitions, raw results, exclusions, and analysis code.

---

# 21. Experimental Scope Rule

The experimental matrix must be the minimum required to answer RO4/Q-AHBN2.

Expected dynamic scenarios from previous Q-AHBN are:

```text
Failure
Churn
Heterogeneity
```

These are NOT automatically accepted.

During reconciliation, verify whether each still answers the Q-AHBN2 research question under canonical AHBN.

For every experiment specify:

```text
Research question
Baseline
Treatment
Topology
N
Seed(s)
Repetitions
Dynamic event
Parameters
Metrics
Expected outputs
Statistical aggregation
PASS/FAIL validity criteria
```

The principal comparison is expected to be:

```text
Frozen AHBN
      vs
Q-AHBN2
```

Additional baselines must have a specific scientific purpose.

---

# 22. Test Pipeline

The approved order is:

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

Do not skip directly to formal experiments.

Every stage has explicit PASS/FAIL criteria.

Distinguish:

```text
IMPLEMENTATION FAILURE
EXPERIMENTAL FAILURE
SCIENTIFICALLY VALID NEGATIVE RESULT
```

A scientifically valid negative result is not a software failure.

---

# 23. Completeness Gate — Last Point for Experiment Design

After smoke testing and BEFORE formal experiments ask:

> If the frozen formal experiment matrix completes successfully, will we possess all evidence necessary to answer the Q-AHBN2 research question and prepare the intended manuscript?

Check all necessary scenarios, baselines, metrics, logging, seeds, repetitions, statistics, learning evidence, Kubernetes evidence, and metadata.

If YES:

> EXPERIMENT CONTRACT FROZEN.

After this gate: no additional scenarios, metrics because results look weak, new baselines because they seem interesting, hyperparameter exploration, AHBN changes, Q-AHBN2 redesign, or scope expansion.

Additional execution is permitted only to correct a documented validity problem.

---

# 24. Formal Experiment Rule

Formal experiments execute only the frozen contract.

Never rerun merely because results are disappointing.

Valid rerun reasons include:

- implementation defect;
- configuration error;
- corrupted output;
- incomplete run;
- methodological inconsistency;
- infrastructure failure affecting validity.

Every rerun/exclusion must be documented.

After completion:

> FORMAL DATASET FREEZE.

---

# 25. Aggregation Rule

Aggregation must be reproducible:

```text
Raw evidence
    ↓
validated runs
    ↓
aggregation script
    ↓
summary statistics
    ↓
95% CI
    ↓
tables
    ↓
figures
```

Never manually copy numbers where an automated reproducible path is available.

Validate expected run counts before interpretation.

---

# 26. Scientific Interpretation Rule

Do NOT begin with:

> Did Q-AHBN2 win?

Begin with:

1. What happened?
2. What is the magnitude?
3. What uncertainty surrounds it?
4. Is it consistent across runs/seeds?
5. Under what conditions does it occur?
6. What mechanism plausibly explains it?
7. What can be concluded?
8. What cannot be concluded?
9. What limitation is exposed?

Legitimate outcomes include clear improvement, modest improvement, metric-specific improvement, condition-dependent improvement, trade-off, approximate equivalence, no improvement, and degradation under some conditions.

The scientific contribution is determined from the complete evidence.

---

# 27. Claim–Evidence Register

Before manuscript finalization, every major claim must map to:

```text
Claim
Experiment
Metric
Numerical result
95% CI/statistical evidence
Figure/Table
Boundary
Limitation
```

Store this in:

`07_CLAIM_EVIDENCE_MATRIX.md`

No major quantitative claim should exist without an evidence path.

---

# 28. Q-AHBN2 Paper Identity

This manuscript is NOT Paper 1 / RO1.

The previously published work already established:

- cloud-native simulation framework;
- Kubernetes deployment;
- Gossip implementation;
- observability;
- resource utilization;
- scalability analysis.

Do not spend substantial manuscript space re-explaining Kubernetes basics, GKE basics, Pods, YAML, generic cloud-native concepts, Gossip fundamentals already covered, or previously published observability architecture.

Use concise positioning such as:

> Building upon the cloud-native simulator introduced by Wira et al. (2025), this work proposes and evaluates a reinforcement-learning-enhanced dissemination control mechanism.

The Q-AHBN2 paper must stand independently while citing previous infrastructure contributions rather than reproducing them.

---

# 29. Target Manuscript Structure

Target approximately 28–35 A4 pages.

## 1. Introduction — approximately 3 pages

Focus on dissemination trade-off, limitation of static strategies, AHBN as observation-driven adaptation, the limitation/opportunity motivating learning, Q-AHBN2, and contributions.

## 2. Related Work — approximately 3 pages

Focus only on literature needed to position Gossip/structured/hybrid dissemination, adaptive dissemination, RL in networking/P2P/blockchain, and the gap addressed by Q-AHBN2.

## 3. Q-AHBN2 Design — approximately 6–7 pages

The methodological heart: concise frozen AHBN foundation, Q-AHBN2 architecture, state, action, reward, learning parameters, interaction with AHBN, and pseudocode.

## 4. Experimental Methodology — approximately 3 pages

Reference previous cloud-native framework and include only Q-AHBN2-specific experimental question, environment, scenarios, baselines, parameters, seeds/repetitions, metrics, statistical procedure, 95% CI, and controlled-vs-Kubernetes distinction.

## 5. Learning Validation — approximately 2–3 pages

Establish that the implemented agent exhibits meaningful learning/adaptation behaviour. Do not claim convergence unless rigorously demonstrated.

## 6. Controlled Evaluation — approximately 6–7 pages

Tentative subsections, subject to experiment freeze: Failure, Churn, Heterogeneity.

## 7. Kubernetes-Native Realism Validation — approximately 4–5 pages

Include only experiments required by the frozen contract. Clearly distinguish this evidence from controlled simulation and do not repeat RO1 infrastructure explanation.

## 8. Discussion — approximately 2–3 pages

Cover what learning changes relative to AHBN, cross-scenario trade-offs, practical implications within demonstrated scope, and limitations.

## 9. Conclusion and Future Work — approximately 1–2 pages

Answer the research question using actual evidence. Do not use a predetermined winner table. Future work must emerge from demonstrated limitations.

---

# 30. Manuscript Figure/Table Rule

Figures and tables are provisional until evidence freezes.

The old manuscript structure is a design reference, not a mandatory checklist.

Every final figure/table must answer:

> What scientific claim does this artifact support?

If two figures tell essentially the same story, consolidate them.

The objective is fewer, stronger, evidence-rich figures.

---

# 31. Paper Writing Order

After experimental freeze use:

```text
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
```

This prevents the narrative from predetermining the findings.

---

# 32. Scientific Reports Pre-Review Gate

Before submission, audit Q-AHBN2 as if the AHBN editor/reviewers were reviewing it again.

Check results accuracy, simulation-vs-Kubernetes scope, meaning of every 95% CI, proportional claims, requested-vs-realized actions, explicit limitations, proper acknowledgement of prior RO1/AHBN work without self-plagiarism, and reproducibility from code/config/raw evidence.

If any answer is NO:

> manuscript not submission-ready.

---

# 33. Seven-Day Science/Experiment Sprint

Approximately five morning hours per day.

## Day 1 — Source Audit + Canonical Reconciliation

Deliver repository inventory, authority hierarchy verification, previous Q-AHBN vs canonical AHBN reconciliation, and invalidated old results identified.

Record:

`S00_SOURCE_AUDIT.md`  
`S01_RECONCILIATION.md`

No code modification before approval.

## Day 2 — Q-AHBN2 Scientific Freeze

Deliver final state/action/reward audit, Q-AHBN2 design contract, metric hierarchy, statistical contract, and minimum experiment matrix.

Record:

`02_QAHBN2_DESIGN_FREEZE.md`  
`03_EXPERIMENT_CONTRACT.md`  
`04_STATISTICAL_CONTRACT.md`

## Day 3 — Development + Regression

Perform only required changes, then regression and canonical AHBN parity.

Record:

`S03_DEVELOPMENT.md`  
`S04_REGRESSION_PARITY.md`

## Day 4 — RL Validation

Test states, actions, reward, Q update, exploration/exploitation, and deterministic sanity.

Record:

`S05_RL_VALIDATION.md`

## Day 5 — Smoke + Completeness Gate

Smoke every intended formal path. Verify logging, outputs, metadata, aggregation compatibility, learning evidence, and GKE path where required.

Then perform the COMPLETENESS GATE.

Record:

`S06_SMOKE.md`  
`S07_COMPLETENESS_GATE.md`

After PASS:

> EXPERIMENT CONTRACT FROZEN.

## Days 6–7 — Formal Execution + Analysis

Execute the frozen learning validation where formal evidence is required, failure, churn, heterogeneity, controlled simulation, and Kubernetes-native experiments required by the contract.

Then validate outputs, aggregate, compute statistics/95% CI, freeze dataset, and begin evidence-first interpretation.

Records:

`S08_FORMAL_EXP10Q.md`  
`S09_FORMAL_EXP11Q.md`  
`S10_FORMAL_EXP12Q.md`  
`S11_AGGREGATION.md`  
`S12_INTERPRETATION.md`

At completion:

> FORMAL EVIDENCE FROZEN.

---

# 34. Five-Day Manuscript Sprint

## Day 8

Freeze figures, tables, and Results.

## Day 9

Write/finalize Q-AHBN2 Design, Experimental Methodology, and Learning Validation.

## Day 10

Write Discussion, Limitations, and Practical implications.

## Day 11

Write Introduction, Related Work, Conclusion, and Abstract.

## Day 12

Perform claim-evidence audit, reviewer-lesson audit, citation audit, figure/table audit, reproducibility audit, formatting, and final compilation.

Record:

`S13_MANUSCRIPT.md`  
`S14_SUBMISSION_AUDIT.md`

---

# 35. Scope-Control Rule

The project operates under:

> MINIMUM SCIENTIFICALLY SUFFICIENT WORK.

Before adding any task ask:

1. Is it necessary for scientific validity?
2. Is it necessary to answer RO4?
3. Is it necessary for manuscript acceptance/reproducibility?
4. Is it necessary because an existing test revealed a genuine defect?

If all answers are NO:

> DO NOT ADD IT.

---

# 36. Automation Rule

Automate repetition, not scientific judgment.

Good automation includes directory creation, manifests, loops, run counts, CI calculations, aggregation, figures, tables, parity checks, and regression checks.

Human/ChatGPT scientific judgment remains required for experimental scope, exclusions, interpretation, conclusions, and methodology changes.

---

# 37. Cost-Control Rule

Priority:

```text
1. ChatGPT directly
2. ChatGPT + human execution
3. ChatGPT + bounded Codex/agent execution
```

Do not use execution agents merely because code is involved.

Use them when they materially save time or reduce mechanical error.

---

# 38. Failure Handling

When something fails:

```text
STOP
 ↓
classify failure
 ↓
record evidence
 ↓
determine minimum correction
 ↓
approve correction
 ↓
execute
 ↓
verify
 ↓
continue
```

Never respond to failure by casually redesigning the project.

---

# 39. Freeze Hierarchy

The project progressively freezes:

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

Later stages must not silently modify earlier frozen stages.

Any required reopening must be explicitly documented and scientifically justified.

---

# 40. Master Workflow

```text
PRE-S00 INFRASTRUCTURE
  │
  ├─ repo freeze
  ├─ GitHub smoke
  ├─ Drive evidence smoke
  └─ workflow PASS
  │
  ▼
Load master/control documents
  │
  ▼
Verify latest repositories
  │
  ▼
S00 Source Audit
  │
  ▼
Audit previous Q-AHBN
  │
  ▼
Compare against canonical AHBN
  │
  ▼
Reconciliation approved
  │
  ▼
Freeze Q-AHBN2 design
  │
  ▼
Freeze metrics/statistics/experiment matrix
  │
  ▼
Minimal development
  │
  ▼
Regression
  │
  ▼
AHBN parity
  │
  ▼
RL validation
  │
  ▼
Smoke
  │
  ▼
COMPLETENESS GATE
  │
  ▼
EXPERIMENT FREEZE
  │
  ▼
Formal experiments
  │
  ▼
Artifact verification
  │
  ▼
DATASET FREEZE
  │
  ▼
Aggregation + 95% CI
  │
  ▼
Evidence-first interpretation
  │
  ▼
CLAIM–EVIDENCE MATRIX
  │
  ▼
Results/figures/tables
  │
  ▼
Manuscript
  │
  ▼
Scientific Reports reviewer-style audit
  │
  ▼
Reproducibility audit
  │
  ▼
MANUSCRIPT FREEZE
  │
  ▼
SUBMIT
```

---

# 41. Master Principles

1. **Canonical AHBN is frozen and immutable.**
2. **Q-AHBN2 learns over AHBN; it does not rewrite AHBN.**
3. **Repository and artifact state outrank AI memory and narration.**
4. **ChatGPT is the primary AI assistant; human execution is the default.**
5. **Codex and other agents are bounded secondary operators.**
6. **The human researcher retains scientific authority.**
7. **Experiment design freezes before formal execution.**
8. **Formal evidence is never rerun merely because it is disappointing.**
9. **All evidence is preserved even when not all evidence appears prominently in the manuscript.**
10. **Present the strongest supported scientific story without overstating or manipulating the evidence.**
11. **Use AHBN Scientific Reports methodology and reviewer lessons wherever applicable.**
12. **Separate controlled simulation from Kubernetes-native evidence.**
13. **Report uncertainty, including 95% CI, with clearly defined scope.**
14. **Automate repetitive work; do not automate scientific judgment.**
15. **Use `.md` control records as persistent external AI/project memory.**
16. **Do not repeat RO1 contributions in the Q-AHBN2 manuscript.**
17. **Use the minimum scientifically sufficient experiments, metrics, figures, and prose.**
18. **Negative, mixed, modest, or condition-dependent results are scientific results—not automatic failures.**
19. **No scope expansion after the Completeness Gate unless scientific validity requires it.**
20. **Finish the research that was designed rather than continuously redesigning it.**
21. **GitHub is authoritative for code/control state; the designated Google Drive evidence hierarchy is authoritative for preserved experimental evidence.**
22. **Incidental DriveFS synchronization of the local workspace is not, by itself, scientific evidence promotion.**

---

# 42. New-Session Bootstrap Prompt

At the beginning of any new ChatGPT/Codex/AI session use:

> Read `docs/00_QAHBN2_MASTER.md`, `01_CANONICAL_AHBN_CONTRACT.md`, and the current stage `.md` file before doing anything else.
>
> Treat those files and the verified repository state as authoritative.
>
> Verify that you are operating on the latest approved Q-AHBN2 state.
>
> Canonical AHBN is frozen and MUST NOT be altered.
>
> If current code, manuscript text, chat context, AI memory, or previous Q-AHBN assumptions conflict with canonical AHBN or the frozen contracts, STOP and report the conflict.
>
> Perform only the current permitted stage.
>
> Do not expand the experiment, alter frozen parameters, add metrics, modify seeds/repetitions, change statistical procedures, or redesign Q-AHBN2 without explicit researcher approval.
>
> At completion, verify the actual artifacts and update the appropriate stage `.md` record with evidence, result, decision, limitations, status, and next permitted task.

---

# 43. Definition of Done

Q-AHBN2 is complete when:

- canonical AHBN parity is verified;
- Q-AHBN2 design is frozen;
- regression and RL validation pass;
- smoke testing passes;
- Completeness Gate passes;
- formal experiments complete;
- raw evidence is preserved;
- aggregation is reproducible;
- statistical analysis is complete;
- 95% CIs are correctly reported where required;
- scientific interpretation is frozen;
- claim-evidence mapping is complete;
- manuscript is complete;
- reviewer-style audit passes;
- reproducibility audit passes;
- manuscript is submission-ready.

At that point:

> **STOP EXPERIMENTING. SUBMIT THE PAPER.**


## Consolidation note

This canonical file consolidates the former `docs/00_QAHBN2_MASTER.md` and `docs/qahbn2/00_QAHBN2_MASTER.md` authorities. The nested path is retired to eliminate competing master documents. Scientifically relevant operating rules from both versions are retained here; current stage status is governed by the current stage/control document and verified repository state rather than historical entry-gate wording.


---

## 15.1.1C AR-1.4.2 Learning-Validation readiness update — 2026-09-23

The bounded AR-1.4.2B preparation chain has been completed through implementation:

- AR-1.4.2A.1 event-path integration: PASS;
- AR-1.4.2A.2 one-seed deterministic integration smoke: PASS / FROZEN;
- AR-1.4.2B.1 real-workload audit: COMPLETE;
- AR-1.4.2B.2 minimal Learning Validation workload: PASS / FROZEN;
- AR-1.4.2B.3A stabilization diagnostic: PASS / FROZEN;
- AR-1.4.2B.3 implementation: COMPLETE, pending execution verification in the researcher's local canonical-ControlSim environment.

The next permitted execution is the predeclared AR-1.4.2 sensitivity matrix only:

`gamma={0.70,0.80,0.90} x seed={42,43,44,45,46}`, exactly 15 runs.

No gamma has been selected. No sensitivity result exists yet. The human researcher performs the execution and returns the immutable output for verification before any gamma-selection decision is recorded.

The later AR-1 amendment that reopens the exact numerical gamma supersedes the older S02-F wording `gamma=0.90` **for gamma selection only**. Alpha and epsilon schedule values remain frozen as documented. Canonical AHBN remains immutable.


## AR-1.4.2B.4 — Pre-Execution Validity Audit / Blocker Resolution

**Decision date:** 2026-09-23  
**Status:** IMPLEMENTATION/DOCUMENTATION CORRECTED — HUMAN REGRESSION VERIFICATION REQUIRED

Before the first formal gamma-sensitivity run, the pre-execution validity audit resolved three candidate blockers:

- canonical AHBN v0.63 queue-drain behavior: **PASS / no defect**;
- Q-AHBN2 requested fanout range 1..7: **PASS / matches frozen Section 02.5 contract**;
- stabilization timestamp semantics: **researcher-approved correction to detection time**.

The stabilization diagnostic retains `W=50`, `delta=0.05`, and three consecutive comparisons, but reports the first reward-bearing Q-update at which all three comparisons are observable. The constant-reward 200-update micro-case therefore returns 200.

No sensitivity cell was executed and no gamma was selected before this correction.

**Next permitted gate:** human pulls the corrected HEAD, verifies the pinned canonical AHBN checkout, and reruns the full regression suite. Only if the complete suite passes may the frozen 15-run gamma sensitivity begin.


---

## AR-1.4.3 — 15-Run Evidence Integrity / Completeness Audit — 2026-09-23

**Gate result: PASS.** This gate is evidence-integrity/completeness only. It does not select or rank gamma values and does not interpret comparative scientific performance.

### Audited evidence

- run directory: `q-ahbn-23092026115202-ar142-gamma-sensitivity-rl-validation`;
- environment/event: ControlSim / `rl-validation`;
- Q-AHBN2 producing commit: `f689532647dcd167ed4603b1ff3ae3d1b4975528`;
- canonical AHBN authority commit: `936a79480bc1252c79b6ee01f65c88c740af2844`;
- matrix: `gamma={0.70,0.80,0.90} x seed={42,43,44,45,46}`;
- expected/completed: 15/15;
- artifacts present: `RUN.md`, `manifest.json`, `ar_1_4_2_gamma_sensitivity.csv`;
- CSV cardinality: 16 total lines = 1 header + exactly 15 data rows.

### Integrity/completeness findings

1. **Artifact integrity — PASS.** All three required artifacts exist and are non-empty.
2. **Cardinality — PASS.** Exactly 15 data rows are present.
3. **Matrix completeness — PASS.** All 15 predeclared gamma/seed combinations are present: five seeds for each of the three candidate gamma values.
4. **Uniqueness — PASS.** No duplicate `(gamma, seed)` pair is present in the supplied CSV.
5. **Required metrics — PASS.** Every row contains the frozen fields: `mean_reward`, `cumulative_reward`, `stabilization`, `q_updates`, `state_action_coverage`, `action_distribution`, `delivery_ratio`, `propagation_delay`, `duplicates`, and `total_forwards`.
6. **Protocol provenance — PASS.** The producing commit's guarded runner fixes the exact 15-run matrix and required metrics. Its ControlSim Learning Validation adapter fixes the stationary 1,000-message workload (BA(100,m=3), source 0, base delay 1.0, jitter 0.2, four static clusters, no failure/churn/resource disturbance), `alpha_Q=0.25`, `epsilon_0=0.30`, `epsilon_min=0.03`, `epsilon_decay=0.995`, and verifies the pinned canonical AHBN commit before execution.
7. **Structural anomaly audit — PASS.** The supplied rows contain no missing required field, malformed gamma/seed pair, non-finite reported scalar, delivery ratio outside [0,1], negative count, or other obvious indication of partial execution. Action-distribution fields are parseable count mappings over the frozen five actions.
8. **Interpretation boundary — ENFORCED.** No gamma is selected, preferred, ranked, or frozen by AR-1.4.3. The evidence remains raw bounded sensitivity evidence pending the separately controlled scientific comparison/selection gate.

### Scientific decision

`AR-1.4.3 = PASS — EVIDENCE INTEGRITY / COMPLETENESS VERIFIED`.

The 15-run sensitivity dataset is structurally complete and provenance-traceable for the next controlled gate. This PASS is not a convergence claim, policy-optimality claim, or gamma-performance conclusion.


---

## AR-1.4.4 — Gamma Sensitivity Analysis and Selection — APPROVED 2026-09-23

Researcher approval received after the controlled 15-run gamma-sensitivity analysis.

**Scientific decision:** `gamma=0.70` is **FROZEN** for subsequent Q-AHBN2 development, validation, and controlled evaluation.

Basis: AR-1.4.3 verified the complete 15-run evidence matrix; AR-1.4.4 compared the three predeclared candidates using paired seeds and the frozen learning/dissemination metrics. gamma=0.70 was recommended on the combined evidence, with the efficiency trade-off of gamma=0.90 explicitly retained as a limitation rather than suppressed.

No new run, seed, gamma candidate, reward modification, or post-hoc retuning was introduced. This freeze does not modify canonical AHBN and is not a claim of convergence, policy optimality, global hyperparameter optimality, or universal superiority.

**AR-1.4.4 = PASS / APPROVED / gamma=0.70 FROZEN.**


---

# DOC-SYNC-1 — Repository Control-Structure Reconciliation — 2026-09-23

**Result:** PASS / COMPLETE.

Administrative synchronization only. No scientific redesign, experiment, new parameter, deletion of historical evidence, or movement of existing authoritative files was performed.

The planned control structure has now been instantiated under `docs/`:
- `03_EXPERIMENT_CONTRACT.md`
- `04_STATISTICAL_CONTRACT.md`
- `05_REVIEWER_LESSONS.md`
- `06_RESULTS_REGISTER.md`
- `07_CLAIM_EVIDENCE_MATRIX.md`
- `stages/S00_SOURCE_AUDIT.md` through `stages/S14_SUBMISSION_AUDIT.md`.

Existing authoritative files remain in place. Detailed AR gate history remains authoritative in `02_QAHBN2_DESIGN_FREEZE.md`; stage files are concise navigation/status records and do not duplicate or replace that evidence.

Current stage map after synchronization:

```text
S00  PASS / historical complete
S01  PASS / complete
S02  scientific design complete; final consistency/closure audit next
S03  next after S02 closure
S04-S14  pending
```

The approved AR-1.4.4 decision remains `gamma=0.70` FROZEN. Formal Exp10-Q/Exp11-Q/Exp12-Q execution remains blocked until the intervening stage gates and frozen experiment/statistical contracts permit it.

**Next controlled gate:** `S02-CLOSE — Final Design-Freeze Consistency / Closure Audit`.


---

## S02-CLOSE — Final Design-Freeze Consistency / Closure Audit — REGISTERED 2026-09-23

**Gate type:** Scientific/administrative closure audit only.

**Purpose:** Reconcile the full frozen Q-AHBN2 design, remove stale contradictions, verify that every required parameter and semantic has exactly one authoritative value, and formally close S02 if the audit passes.

**Strict boundary:**
- no simulations;
- no new experiment;
- no parameter tuning;
- no redesign;
- no change to canonical AHBN;
- no reopening of already frozen decisions merely for preference or simplification.

A design change is permitted only if S02-CLOSE discovers a genuine scientific inconsistency that prevents the frozen design from being internally coherent or uniquely interpretable. Any such inconsistency must be documented explicitly before correction.

**Required audit checks:**
1. reconcile the complete frozen design against the authoritative S02 record and source-authority constraints;
2. identify and remove or supersede stale contradictory statements without deleting historical evidence;
3. verify one authoritative value/semantic for every required state, action, reward, transition, learning, lifecycle, and frozen hyperparameter item;
4. verify canonical AHBN remains immutable and Q-AHBN2 remains a bounded post-AHBN meta-controller;
5. verify current frozen learning parameters, including `alpha_Q=0.25` and researcher-approved `gamma=0.70`, are represented consistently;
6. verify no unresolved S02 scientific decision remains hidden behind historical/deferred wording;
7. issue an explicit PASS/FAIL closure decision and, on PASS, mark S02 closed and S03 as the next stage.

**Current status:** `S02-CLOSE = NEXT / NOT YET EXECUTED`.

No simulation or redesign is authorized by registering this gate.


---

## S02-CLOSE-C1 — Consistency Correction & S02-I Reconciliation — 2026-09-23

**Status:** **PASS / COMPLETE — READY FOR S02-CLOSE RE-AUDIT.**

This gate performed documentation/code consistency correction and design-level reconciliation only. No simulation, experiment, parameter tuning, redesign, or canonical-AHBN modification was performed.

### C1 corrections

1. Stale Master statements that presented gamma selection or S02-H/S02-I as currently unresolved are explicitly superseded by the later frozen decisions; historical provenance is retained.
2. The executable learner default is aligned to the already-approved **gamma=0.70**. This is implementation consistency, not parameter selection.
3. **S02-I design-level reconciliation = PASS.** The complete learning mechanism remains outside canonical AHBN: canonical environment adapters produce the logical observations; canonical AHBN alone owns normalization/EWMA, score, sigmoid, mode rule and S5 proposal; Q-AHBN2 consumes the frozen canonical observation state and acts only after `(mode_AHBN,k_AHBN)` exists; eligible-target construction/realization remains the execution boundary. The same logical Q-AHBN2 state/action/reward/transition/learning contract is required in ControlSim and Kubernetes. Raw sensing and execution mechanics may remain environment-specific as already permitted by the canonical contract.

### S02-I scope boundary

This is a **design-level compatibility audit**, not a claim that Kubernetes Q-AHBN2 has already been implemented or empirically parity-tested. Code integration, regression tests and empirical cross-platform parity remain owned by S03/S04 and later validation stages. Therefore S02-I can close without a simulation while preserving those later obligations.

### Canonical-AHBN integrity

No canonical AHBN equation, normalization, EWMA parameter, score coefficient, sigmoid, mode threshold, S5 threshold/mapping, eligible-neighbour semantic, or realized-fanout rule is changed by C1.

**Next permitted gate:** rerun **S02-CLOSE — Final Design-Freeze Consistency / Closure Audit**. S03 remains blocked until that re-audit returns PASS.


---

## S02-CLOSE-C2 — Residual Stale-Status Supersession — REGISTERED 2026-09-23

**Status:** **REGISTERED / NEXT.**

**Purpose:** perform the minimum residual documentation correction required by the S02-CLOSE re-audit. C2 must locally mark or replace stale current-looking statements so repository searches no longer expose an apparently active `gamma=0.90`, unresolved S02-H, pending S02-I, or blocked S02-J when those items have already been superseded by later frozen authority.

**Strict boundary:** documentation-status supersession only. Preserve historical evidence and provenance. No simulation, experiment, parameter tuning, redesign, new scientific decision, or canonical-AHBN modification is authorized. The already-frozen `gamma=0.70` and S02-I design-level PASS are not reopened.

**Required completion checks:**
1. residual `gamma=0.90` occurrences are either unmistakably historical/candidate evidence or removed from current-authority wording;
2. no current Master status presents S02-H as unresolved;
3. no current Master status presents S02-I as pending;
4. no current Master status presents S02-J as blocked by already-resolved F--I work;
5. historical records remain preserved and clearly labelled as historical/superseded;
6. rerun the same static S02-CLOSE repository audit after C2.

**Closure rule:** C2 itself does not close S02. Only a clean subsequent S02-CLOSE static re-audit may authorize `S02 = PASS / CLOSED / FROZEN` and `S03 = NEXT`.
