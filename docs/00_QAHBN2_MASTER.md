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
docs/
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
    ├── DOC_SYNC_2_STAGE_MAP_RECONCILIATION.md
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
    ├── S10A_FORMAL_EXP13Q_REFERENCE_BENCHMARK.md
    ├── S11_AGGREGATION.md
    ├── K0_Q_K8S_SCOPE_RECONCILIATION.md
    ├── K1_Q_K8S_DESIGN_CODE_MAPPING.md
    ├── K2_Q_K8S_INTEGRATION_PARITY.md
    ├── K3_Q_K8S_SMOKE.md
    ├── K4_Q_K8S_VALIDATION_FREEZE.md
    ├── K5_Q_K8S_FORMAL_VALIDATION.md
    ├── K6_Q_K8S_EVIDENCE_FREEZE.md
    ├── S12_INTERPRETATION.md
    ├── S12A_CLAIM_RECONCILIATION.md
    ├── S13_MANUSCRIPT.md
    ├── S13_T_CHAPTER6_MAPPING.md
    └── S14_SUBMISSION_AUDIT.md
```

This is the frozen downstream stage map after S07-D. Exp13-Q-Sim is a separate publication-positioning benchmark and does not alter Exp10-Q/Exp11-Q/Exp12-Q. K0-Q through K6-Q remain the bounded Kubernetes deployment-validation chain, but their prospective scope now includes a matched Exp13-Q-K8s five-method reference-benchmark arm so that the RO1 cloud-native evaluation framework can support the same bounded comparator family in both ControlSim and Kubernetes. This amendment does not reopen Exp10-Q/Exp11-Q/Exp12-Q or the frozen Exp13-Q-Sim matrix. S12A reconciles thesis/paper claims before manuscript finalization, and S13-T maps verified RO4 evidence into thesis Chapter 6.

Do not create unnecessary documentation beyond this unless a later controlled gate establishes that it is scientifically or operationally required.

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

The current local repository may reside inside a Google Drive Desktop synchronized path. Therefore Drive may automatically synchronize repository files, `.git/`, the ignored `output/` tree, and other working files.

**Strict generated-output standard:** every experiment, smoke, regression, diagnostic, pilot, formal run, analysis artifact, trace, log, manifest, figure, generated table, and preserved scientific evidence directory must reside under repository-local `output/`. The normal evidence path is `output/evidence/<timestamped-run-directory>/`. Generated artifacts and evidence must not exist as new root-level `evidence/`, `outputs/`, or `q-ahbn-*/` directories and must not be committed to Git.

The only data-directory exception is root-level `topology/`, reserved exclusively for topology data/cache material. Topology data must not be stored under `output/`, and experiment/log/evidence artifacts must not be stored under `topology/`.

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

## 9.5 GitHub-First Controlled Gate Workflow — Project-Wide Standard

From S02-CLOSE onward, every controlled gate and every test type uses the following workflow:

```text
FETCH GITHUB
    ↓
RECONCILE CURRENT AUTHORITY / VERIFY CURRENT GATE
    ↓
PREPARE CODE / CONFIGURATION / TEST CONTRACT
    ↓
EXECUTE OR AUDIT ONLY THE AUTHORIZED SCOPE
    ↓
DECIDE: PASS / HOLD / FAIL
    ↓
SYNC ONLY FILES WHOSE AUTHORITATIVE STATE CHANGED
    ↓
VERIFY OUTPUT / EVIDENCE WHERE APPLICABLE
    ↓
POST-WRITE GITHUB READBACK
    ↓
DECLARE CURRENT STATUS + NEXT CONTROLLED GATE
```

For executable tests, the researcher performs the run from the designated local synchronized workspace. Generated output is written to the prescribed timestamped run directory and is promoted to authoritative Google Drive evidence only after the applicable validity/completeness checks and deliberate preservation/readback.

The synchronization rule is:

> **Audit every gate; edit only files whose authoritative state actually changed.**

Accordingly:

- the detailed stage/audit record is updated for every completed controlled gate;
- the Master, status, experiment, statistical, results, claim/evidence, source-authority, code, or other files are updated only when the gate changes the authoritative state represented by that file;
- a valid no-change audit must not create artificial edits;
- historical evidence is preserved and locally marked historical/superseded where necessary rather than silently rewritten;
- a successful write operation is not sufficient to declare a transition complete.

### 9.5.1 No-status-declaration-before-readback rule

No PASS/CLOSED/FROZEN/NEXT status created by a repository write is authoritative until the affected files have been re-fetched from GitHub and reconciled against the intended state.

The required sequence is:

```text
edit
  ↓
commit
  ↓
re-fetch
  ↓
reconcile
  ↓
declare status
```

If readback exposes a contradiction, stale status, incomplete write, or unexpected change, the gate remains HOLD until reconciled.

### 9.5.2 Standard test record grammar

The following grammar is the project-wide standard for unit, deterministic, smoke, regression, parity, Learning Validation, diagnostic, pilot, ControlSim formal, and Kubernetes formal tests. Fields that genuinely do not apply may be recorded as `N/A`; applicable fields must not be silently omitted.

```text
TEST / GATE:
OBJECTIVE:
AUTHORITATIVE GITHUB COMMIT:
AUTHORITATIVE CONTRACT:
EXECUTION ENVIRONMENT:
RUN DIRECTORY:
EVENT TYPE:
PARAMETERS:
SEEDS / REPETITIONS:
EXPECTED OUTPUTS:
USER EXECUTION COMMAND:
EVIDENCE LOCATION:
COMPLETENESS CHECK:
VALIDITY CHECK:
RESULT:
SCIENTIFIC INTERPRETATION:
GITHUB STATUS UPDATE:
NEXT CONTROLLED GATE:
```

**Execution responsibility:** ChatGPT prepares and verifies the code, configuration, test contract, expected outputs, and exact run command from the latest authoritative GitHub state. The researcher executes the test from the designated local Google Drive workspace. Generated outputs are written to the prescribed timestamped output directory and deliberately preserved in the designated Google Drive evidence area after the applicable checks. ChatGPT then verifies the returned artifacts before any scientific PASS/FAIL decision or GitHub status transition is recorded.

This workflow does not transfer scientific decision authority from the researcher and does not authorize a test merely because the grammar exists.


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


## S07 Closure — 2026-09-28

The completeness gate is now **PASS / CLOSED** after prospectively freezing the formal experiment matrix in `docs/03_EXPERIMENT_CONTRACT.md` (S07-A) and the formal statistical contract in `docs/04_STATISTICAL_CONTRACT.md` (S07-B), followed by the read-only S07-C completeness re-audit. Formal ControlSim execution is released beginning with S08 Exp10-Q Failure. Canonical AHBN and the frozen Q-AHBN2 learning contract remain unchanged.

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

> **HISTORICAL / SUPERSEDED STATUS:** At this earlier AR-1.4.2B preparation point, no gamma had yet been selected and no sensitivity result yet existed. This statement is preserved only as chronological provenance. Subsequent AR-1.4.3 evidence-integrity verification and AR-1.4.4 researcher adjudication completed the bounded selection; the current authoritative value is `gamma=0.70` **FROZEN**.

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

**Historical registration status (SUPERSEDED):** `S02-CLOSE = NEXT / NOT YET EXECUTED`. This records the gate state at registration and is not the current S02 status.

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

**Historical completion status:** **PASS / COMPLETE — SUPERSEDED BY C3/C4/C5 CLOSURE PROGRESSION.**

> **Historical record:** The C2 registration text below is preserved for provenance. It no longer represents the current S02 gate or next action.

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

---

## S02-CLOSE-C5 — Master C2 Status Supersession — 2026-09-28

**Status:** **PASS / COMPLETE — FINAL STATIC S02-CLOSE RE-AUDIT NEXT.**

**Scope:** administrative Master-status reconciliation only. No simulation, test execution, parameter tuning, redesign, scientific decision, implementation change, Google Drive evidence work, deletion of historical evidence, or canonical-AHBN modification was authorized or performed.

### Correction completed

The preserved S02-CLOSE-C2 registration block is now explicitly labelled historical and completed. Its original purpose, checks, closure rule, and provenance remain intact, but it can no longer be interpreted as the current gate or next action.

### Boundary

C5 does **not** itself close S02. Only a clean mandatory GitHub readback and final static S02-CLOSE re-audit may authorize:

```text
S02 = PASS / CLOSED / FROZEN
S03 = NEXT
```

# 25. S07-D Prospective Thesis–Paper Scope Amendment — 2026-09-28

S07-D closed prospectively before inspection of any formal Exp10-Q / Exp11-Q / Exp12-Q result.

The frozen evidence architecture is:

```text
Learning Validation
    -> stationary learning-mechanics / bounded parameter evidence

Exp10-Q Failure
Exp11-Q Churn
Exp12-Q Heterogeneity
    -> primary thesis RO4/RQ4 AHBN-versus-Q-AHBN2 causal evaluation
    -> 80 formal ControlSim runs total

Exp13-Q Reference Benchmark
    -> publication positioning only
    -> Gossip / Structured / DC-SoC / AHBN / Q-AHBN2
    -> churn=0.40, BA(100,m=3), source 0, 1,000 sequential messages
    -> four Exp11-Q-compatible churn cycles
    -> seeds 42--46
    -> 25 formal ControlSim runs

K8s-VAL-Q
    -> later bounded deployment validation
```

Total frozen formal ControlSim scope after S07-D is **105 runs**. Exp10-Q / Exp11-Q / Exp12-Q remain scientifically unchanged.

The control-document structure now additionally includes:

```text
docs/stages/S10A_FORMAL_EXP13Q_REFERENCE_BENCHMARK.md
```

Exp13-Q must not be used to redesign Q-AHBN2, retune parameters, select a favorable scenario post hoc, or create an omnibus algorithm ranking. Its role is bounded external reference positioning under one prospectively selected high-churn condition.

After S07-D closure, the immediate operational next task remains **S08-PREP-3 — Local Regression + Bounded Exp10-Q Smoke**.


## Current-stage reconciliation — 2026-09-29
S12A — Thesis–Paper Claim Reconciliation is **PASS / CLOSED**. The final claim authorization contract is frozen in `docs/stages/S12A_CLAIM_RECONCILIATION.md` and `docs/07_CLAIM_EVIDENCE_MATRIX.md`.

The next permitted paper gate is **S13 — Q-AHBN2 Manuscript**. S13 must draft only within the S12A claim boundaries and must not reopen experimental design, parameters, algorithms, metrics, evidence, or statistical procedures. The separate thesis evidence-mapping gate remains **S13-T — Chapter 6 Mapping** according to the frozen downstream stage map.


---

## S13 Publication-Workspace Reconciliation — 2026-09-30

S13-1 manuscript structure/evidence mapping and S13-2 manuscript drafting-plan/source-pack reconciliation are **PASS / CLOSED**.

The publication architecture is now frozen as a dual-repository model within the Google Drive-synchronized local workspace:

```text
q-ahbn2/
  Git-tracked scientific/code/control record
  output/ = Git-ignored, Drive-synchronized generated/working evidence

QAHBN2-Manuscript/
  separate Git-tracked publication repository
  output/ = Git-ignored, Drive-synchronized manuscript working/evidence area
```

This preserves the existing project-wide generated-output standard: new scientific/generated artifacts remain under repository-local `output/`; no competing root-level `evidence/` or `outputs/` hierarchy is introduced.

Repository authority remains separated:
- `wwiras/q-ahbn2` is the scientific/code/control authority;
- the future `wwiras/QAHBN2-Manuscript` repository is the publication-source authority;
- the designated Q-AHBN2 Google Drive evidence hierarchy remains the experimental evidence authority;
- automatic Drive synchronization does not itself constitute evidence promotion.

The repositories must be linked by explicit provenance using the Q-AHBN2 science commit SHA, Drive folder ID, manifest/hash where available, S12A claim ID, and manuscript section/figure/table identity. Overleaf is to connect only to the manuscript repository.

**Current paper gate:** S13-2 = PASS / CLOSED.  
**Next permitted paper action:** S13-3 — Manuscript Repository Bootstrap / Provenance Initialization.  
**Separate thesis path:** S13-T remains unopened.


### S13-3 manuscript-repository bootstrap status — 2026-09-30

The separate private publication repository now exists at `wwiras/QAHBN2-Manuscript` and has been initialized with a lean publication skeleton, manuscript `.gitignore`, `docs/MANUSCRIPT_MASTER.md`, and `docs/PROVENANCE.md`.

Pinned Q-AHBN2 manuscript science baseline: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

The manuscript repository is cloned by the researcher inside the Google Drive-synchronized local path:
`/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myPaper/ClusterComputing/QAHBN2-Manuscript`.

The manuscript repository points back to this scientific repository and the registered frozen evidence families. This scientific repository now recognizes `wwiras/QAHBN2-Manuscript` as the publication-source repository.

Manuscript-side Google Drive folder ID: `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`.

**S13-3 = PASS / CLOSED** after manuscript Drive identity registration and cross-repository provenance initialization.

**Next permitted paper action:** S13-4 — Section 3 Q-AHBN2 Method Drafting, bounded by the S13-2 source pack and frozen S12A claim contract.


### S13-4 Section 3 Method drafting — 2026-09-30

Section 3 has been drafted in the publication repository at `sections/03_method.tex` using the pinned science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` and S12A claims C01/C02 only. Controlled readback passed.

**S13-4 = PASS / CLOSED.**

**Next permitted paper action:** S13-5 — Section 4 Experimental Methodology Drafting.


### S13 manuscript architecture refinement — 2026-09-30

The publication-source repository `wwiras/QAHBN2-Manuscript` now uses a versioned single-file manuscript model.

Current active source:
`versions/v0.0/main.tex`

Publication-source rules:
- no root `main.tex`;
- no `sections/`, `figures/`, `tables/`, or dedicated `bibliography/` directories;
- all manuscript sections, LaTeX/TikZ figures/diagrams, and tables live directly in the active versioned `main.tex`;
- Zotero/BibTeX bibliography files are researcher-managed and added manually inside the applicable version directory;
- new `versions/vX.Y/` directories require explicit controlled version transition.

This administrative refinement preserves the pinned scientific baseline and S13-4 content.

**S13-4 remains PASS / CLOSED.**
**Next permitted paper action remains S13-5 — Section 4 Experimental Methodology Drafting.**


### S13-5 Experimental Methodology closure — 2026-09-30

Section 4 Experimental Methodology has been drafted in `versions/v0.0/main.tex` and audited against the pinned science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`, the frozen experiment/statistical contracts, Exp13-Q role definition, K4/K6 Kubernetes records, and S12A boundaries.

No result interpretation or new analysis was introduced.

**S13-5 = PASS / CLOSED.**

**Next permitted paper action:** S13-6 — Section 5 Results Drafting.


### S13-6 Section 5 Results drafting — 2026-09-30

Section 5 has been drafted and audited in the publication repository `versions/v0.0/main.tex`. It reproduces only frozen S11-A/S11-B/K6/S12/S12A results and preserves the required evidence-role and overclaim boundaries.

**S13-6 = PASS / CLOSED.**

**Next permitted paper action:** S13-7 — Section 6 Discussion Drafting.


### S13-7 Section 6 Discussion drafting — 2026-09-30

Section 6 has been drafted and audited in the publication repository `versions/v0.0/main.tex`. It synthesizes only frozen S12/S12A findings and preserves the required trade-off, uncertainty, naming, and overclaim boundaries.

**S13-7 = PASS / CLOSED.**

**Next permitted paper action:** S13-8 — Section 7 Limitations Drafting.


### S13-8 Section 7 Limitations drafting — 2026-09-30

Section 7 has been drafted and audited in the publication repository `versions/v0.0/main.tex` using only frozen C13--C15/statistical limitation authorities.

**S13-8 = PASS / CLOSED.**

**Next permitted paper action:** S13-9 — Section 1 Introduction Drafting.


### S13-9 Section 1 Introduction drafting — 2026-09-30

Section 1 has been drafted and audited in the publication repository `versions/v0.0/main.tex` using the frozen Introduction source pack and S12A C01/C12/C13/C15 boundaries.

**S13-9 = PASS / CLOSED.**

**Next permitted paper action:** S13-10 — Section 2 Related Work Drafting.


### S13-10 Section 2 Related Work drafting — 2026-09-30

Section 2 has been drafted and audited in the publication repository using the frozen thesis Chapter 2 as a literature map and the underlying original Drive papers as claim-verification authority. The retained eight-source paper-scale set covers Gossip, structured/clustered, hybrid/adaptive, and learning-assisted networking while preserving C01/C12/C15 boundaries.

**S13-10 = PASS / CLOSED.**

**Next permitted paper action:** S13-11 — Section 8 Conclusion Drafting.


### S13-11 / S13-12 manuscript closure — 2026-09-30

Section 8 Conclusion and the manuscript Abstract have been drafted and audited in the publication repository `versions/v0.0/main.tex` using only the frozen S12/S12A evidence chain and completed manuscript sections.

**S13-11 = PASS / CLOSED.**  
**S13-12 = PASS / CLOSED.**

No new experiment, parameter, metric, statistic, evidence family, literature claim, convergence/optimality claim, universal-superiority claim, generic low-overhead claim, or cross-environment equivalence claim was introduced.

**Next permitted paper action:** S13-13 — Title and Keywords Finalization.


### S13-13 title/keywords closure — 2026-09-30

The publication title and keywords have been finalized in the manuscript repository within the frozen S12A claim boundary.

**S13-13 = PASS / CLOSED.**

Final title: **Q-AHBN: Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions**

No new evidence, experiment, statistic, metric, literature claim, convergence/optimality claim, universal-superiority claim, generic low-overhead claim, or Kubernetes-confirmation claim was introduced.

**Next permitted paper action:** S13-14 — Whole-Manuscript Consistency and Submission-Readiness Audit.


### S13-14 whole-manuscript audit — 2026-09-30

The whole-manuscript consistency and submission-readiness audit passed for scientific claims, publication naming, numerical traceability, evidence-role boundaries, internal references, LaTeX structure, and S12A claim limits.

**Bibliography authority clarification:** the established contract defines `references.bib` as researcher-managed through Zotero. Its repository presence or absence is not a manuscript-gate criterion and is not a missing scientific artifact, HOLD condition, submission blocker, or assistant-controlled packaging action.

Independent verification against the researcher-authorized Google Drive `supportDocs` corpus confirmed all eight manuscript citation keys in `biblist/ahbnLR25Sept2026chap2_93.bib` (Drive ID `1TXqYfsaInVi_FXOYVZZ_0ljfNSV9MtQe`). This is supplementary source verification only; it does not replace or alter Zotero authority.

**S13-14 = PASS / CLOSED.**

No scientific evidence, experiment, analysis, statistic, metric, or literature source was added or reopened.


### S13 Post-Drafting Gate Reconciliation — 2026-09-30

The completed S13 manuscript sequence was reconciled against the frozen downstream stage map.

Verified:
- S13-1 through S13-14 are PASS / CLOSED;
- pinned manuscript science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A claim authority is unchanged;
- no experiment, parameter, metric, statistic, evidence family, or scientific interpretation was reopened;
- Zotero/`references.bib` remains researcher-managed under the established contract;
- `S13_T_CHAPTER6_MAPPING.md` is a separate thesis path and remains pending/unopened;
- the frozen paper-stage sequence proceeds from `S13_MANUSCRIPT.md` to `S14_SUBMISSION_AUDIT.md`.

**S13 = PASS / CLOSED.**

**Next controlled paper gate:** S14 — Submission / Reproducibility Audit.  
**Separate thesis path:** S13-T — Chapter 6 Evidence Mapping remains unopened.


### S14 Submission / Reproducibility Audit — 2026-09-30

The final standalone-paper submission/reproducibility audit is complete.

Verified against the frozen contracts and registered evidence:
- Exp10-Q 20/20, Exp11-Q 30/30, Exp12-Q 30/30; primary aggregation 80/80 runs / 40/40 pairs;
- Exp13-Q 25/25 separate bounded reference cells;
- Kubernetes 25/25 validated coordinates;
- seeds 42--46 and documented exclusion/rerun rules;
- frozen Q-AHBN2 learning parameters and immutable AHBN boundary;
- quantitative manuscript tables and claim-evidence consistency;
- registered Drive/Git/manifest identifiers;
- publication-facing Q-AHBN terminology and S12A claim limits;
- researcher-managed Zotero/`references.bib` boundary;
- no new supplementary scientific artifact is required under the current contract.

Explicit table-level provenance is registered in `wwiras/QAHBN2-Manuscript/docs/PROVENANCE.md`.

**S14 = PASS / CLOSED.**

The standalone Q-AHBN paper scientific workflow is complete under the current frozen stage map. No new scientific result, experiment, parameter, comparator, claim, literature source, or analysis was introduced.

**Separate thesis path:** S13-T — Chapter 6 Evidence Mapping remains PENDING / unopened.


---

## S17 — Kubernetes Forwarding-Accounting Remediation

### Programme authority

S17 is a bounded post-S16 remediation programme opened after the Kubernetes forwarding-accounting audit identified a method-inconsistent successful-forward event path for decision-bound Q-AHBN2 forwarding.

Governing principle:

> **Fix the measurement, not the scientific result.**

Frozen throughout S17 unless a later gate explicitly authorizes otherwise:

- canonical AHBN equations, normalization, EWMA, score, mode rule, and S5 fanout semantics;
- Q-AHBN2 state/action/reward/transition/lifecycle contracts;
- learning parameters;
- ControlSim experiments/evidence;
- frozen historical Kubernetes evidence and its provenance;
- S12/S12A claim boundaries;
- S16 publication artifacts except where later remediation evidence requires a separately controlled manuscript update.

S18 remains blocked until S17 closes.

### Controlled sequence

1. **S17-0 — Kubernetes Forwarding-Accounting Root-Cause Audit** — PASS / CLOSED.
2. **S17-1 — Minimal Instrumentation Remediation** — PASS / CLOSED.
3. **S17-2 — Deterministic Instrumentation Verification** — PASS / CLOSED.
4. **S17-3 — Kubernetes Smoke Execution** — PASS / CLOSED.
5. **S17-4 — Smoke Aggregation / Acceptance Audit** — PASS / CLOSED.
6. Formal rerun scope may be frozen only after S17-4.

### S17-0 closure finding

The Q-AHBN2 decision-bound forwarding branch increments the internal successful-forward counter and records the Q-AHBN2 NEW outcome, but historically omitted the common generic `event="forward"` emitted by the inherited peer forwarding path. Therefore historical `F_success` / `total_forwards`, defined as the count of generic `forward` events, is method-inconsistent for Q-AHBN2. `F_attempt`, defined from `k7_forward_attempt`, is not affected by this omission.

Classification: **instrumentation/accounting defect; no algorithm defect established**.

### S17-1 implementation — 2026-10-03

Scientific repository implementation commit:

`0dfaf8c5fcbbbad15e6e62844d5f6e7cf4888583`

Changed file only:

`gke/app/qahbn2_runtime.py`

The successful decision-bound Q-AHBN2 `resp.ok` branch now emits the same generic successful-forward event fields as inherited `PeerState.forward_to_peer()`, plus `decision_id` for traceability.

No change was made to:

- destination/target selection;
- AHBN proposal generation;
- Q-AHBN2 action selection;
- requested or realized fanout;
- RPC execution;
- ACK classification;
- reward semantics;
- transition/update lifecycle;
- learning parameters;
- duplicate or failed outcome handling;
- non-Q-AHBN2 forwarding paths;
- ControlSim code/evidence.

The fallback path where no Q decision ID is bound remains delegated to the inherited forwarding function and was not instrumented again, preventing duplicate generic-success logging.

### S17-1 decision

The change is a minimal measurement-semantic repair only. It restores the common meaning:

`event="forward" == successful forwarding RPC`

for the decision-bound Q-AHBN2 path without altering dissemination behavior.

**S17-1 = PASS / CLOSED.**

### Next controlled gate

**S17-2 — Deterministic Instrumentation Verification.**

S17-2 must verify, before any Kubernetes smoke or formal rerun:

- every Q-AHBN2 decision-bound NEW outcome produces exactly one traceable generic `forward` event;
- DUPLICATE and FAILED outcomes do not produce generic successful-forward events;
- `F_success <= F_attempt`;
- the inherited fallback path does not double-log;
- non-Q-AHBN2 forwarding behavior remains unchanged.

No smoke run or formal Kubernetes rerun is authorized until S17-2 passes.


### S17-2 deterministic verification preparation — 2026-10-03

**Status: PREPARED / AWAITING LOCAL EXECUTION**

A bounded deterministic guard suite was added at:

`tests/test_s17_2_forward_instrumentation.py`

Preparation commit:

`185bbbd768478d31bfd56ae47425bb0423201aec`

The suite performs source/AST verification only and does not execute Kubernetes, network RPCs, smoke workloads, simulations, or formal experiments. It contains five tests mapped one-to-one to the S17-2 acceptance invariants:

1. decision-bound Q-AHBN2 NEW path contains exactly one generic `forward` event with inherited common fields plus `decision_id`;
2. DUPLICATE, rejected FAILED, and exception FAILED paths contain no generic successful-forward event;
3. one `k7_forward_attempt` is structurally emitted before delegation/outcome handling and the Q-AHBN2 success path contains only one generic success event, guarding `F_success <= F_attempt`;
4. the Q-AHBN2 no-decision fallback delegates exactly once to `_ORIGINAL_FORWARD` and adds no local generic success event;
5. the non-Q-AHBN2 path delegates exactly once to `_ORIGINAL_FORWARD` and adds no local generic success event; inherited `peer.py` successful-forward instrumentation remains present.

Required local command from the synchronized repository root:

```bash
PYTHONPATH=. python3 -m unittest tests/test_s17_2_forward_instrumentation.py -v
```

Acceptance requires **5/5 PASS** with no test error. Until the researcher executes this deterministic suite and returns the console result for readback, **S17-2 is not closed**.

No GKE smoke, formal rerun, manuscript-result replacement, or S18 work is authorized while this execution is pending.


### S17-2 first local execution — harness error / gate remains open

Researcher local execution on 2026-10-03 ran all five deterministic tests. Results:

- 2 tests reached their assertions and passed:
  - non-Q-AHBN2 path pure single delegation;
  - Q-AHBN2 fallback single delegation/no local success log.
- 3 tests terminated with `AttributeError: 'list' object has no attribute '_fields'` before evaluating their scientific/instrumentation assertions.

Root cause was isolated to the test helper `_logged_events()`: it passed AST statement lists such as `outcome_if.body` directly to `ast.walk()`, which requires an AST node. This is a **test-harness traversal defect**, not evidence that any S17-2 forwarding invariant failed.

The helper was minimally corrected to normalize a list into individual AST roots before walking them.

Harness-fix commit:

`ef9361ee6710ec0bc661cf878388f425def3efbf`

No runtime, algorithm, instrumentation, experiment, metric, or scientific evidence file was changed by this correction.

**S17-2 remains OPEN / AWAITING RERUN.** Acceptance still requires 5/5 deterministic tests to PASS. S17-3, S17-4, formal reruns, manuscript-result replacement, and S18 remain blocked.


### S17-2 deterministic verification rerun — PASS / CLOSED

Researcher local rerun on 2026-10-03 after pulling authoritative `main` completed:

```text
Ran 5 tests in 0.009s
OK
```

All five predeclared S17-2 invariants reached their assertions and passed:

1. decision-bound Q-AHBN2 NEW contains exactly one generic `forward` event with common inherited fields and `decision_id`;
2. DUPLICATE and FAILED paths contain no generic successful-forward event;
3. the runtime structure preserves one attempt event before forwarding handling and at most one Q-AHBN2 generic success event per invocation, satisfying the deterministic accounting guard for `F_success <= F_attempt`;
4. the no-decision Q-AHBN2 fallback delegates exactly once to `_ORIGINAL_FORWARD` and does not add a local success event;
5. non-Q-AHBN2 forwarding delegates exactly once to the unchanged inherited path, whose successful-forward instrumentation remains present.

The prior first-run errors are retained in provenance as a test-harness traversal defect and were corrected only in the test helper. The production runtime remained unchanged between the first and passing S17-2 executions.

**S17-2 = PASS / CLOSED.**

This closes deterministic instrumentation verification only. It does not constitute Kubernetes operational validation and does not replace any historical formal result.

**Next controlled gate: S17-3 — Kubernetes Smoke Execution.**

S17-4, formal rerun-scope selection, formal reruns, manuscript-result replacement, and S18 remain blocked until the required smoke sequence advances through S17-3 and S17-4.


### S17-3 Kubernetes smoke preparation — 2026-10-03

**Status: PREPARED / AWAITING RESEARCHER GKE EXECUTION**

S17-3 reuses the previously validated bounded K3-Q smoke protocol rather than creating a new performance workload:

- Q-AHBN2 only;
- N=4, BA(m=2), seed 42, source 0;
- four messages at 0.2 s interval;
- no induced failure, churn, overload, or bottleneck;
- operational/instrumentation validation only.

The smoke runner was extended only at its post-run validation/summary layer. The topology, workload, Q-AHBN2 algorithm, AHBN controller, learning parameters, forwarding runtime, and formal protocol were not changed.

Preparation commit:

`7a1aa490a0231008b26c58a242b752a1c507c4d5`

The S17-3 runtime acceptance checks now require:

1. decision-bound `qahbn2_attempt_outcome=NEW` keys and generic `event="forward"` keys with `decision_id` to match exactly;
2. no DUPLICATE/FAILED outcome key may overlap a decision-bound generic successful-forward key;
3. `F_success <= F_attempt`;
4. the normal Q-AHBN2 decision/outcome/reward evidence remains present;
5. the generated smoke summary records `F_attempt`, `F_success`, decision-bound NEW count, decision-bound generic-forward count, exact-match status, non-NEW overlap count, and the accounting inequality.

This smoke does not artificially induce FAILED outcomes. Absence of FAILED in this no-failure bounded smoke is not a gate failure; S17-2 already verifies the FAILED instrumentation branch deterministically.

A fresh immutable image must be built from the current post-S17-3-preparation commit and pushed for `linux/amd64`; the existing K3 image predates the S17-1 runtime repair and must not be reused.

**S17-3 remains OPEN pending researcher execution and artifact readback.** S17-4, formal rerun-scope selection, formal reruns, manuscript-result replacement, and S18 remain blocked.


### S17-3 Kubernetes smoke execution — PASS / CLOSED

Researcher-executed bounded GKE smoke on 2026-10-03 used the freshly built immutable image:

`wwiras/q-ahbn2:s17-3-smoke-20261003`

Registry digest:

`sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`

The evidence directory is preserved in the synchronized scientific workspace:

`output/evidence/q-ahbn-gke-03102026111913-k3q-smoke/`

Google Drive synchronized counterpart folder ID:

`1dnNThopXkvIhrit6FOEOIQ-Y90A8oNzN`

Recorded execution Git SHA:

`aa91a86eb571dbd61e52a479ba9271c8ddfdcbbf`

Observed smoke summary:

- status: PASS;
- decision_events: 15;
- attempt_outcome_events: 17;
- reward_closed_events: 11;
- outcomes: NEW and DUPLICATE;
- F_attempt: 17;
- F_success: 11;
- decision_bound_NEW: 11;
- decision_bound_forward: 11;
- new_forward_exact_match: true;
- nonnew_forward_overlap: 0;
- f_success_le_f_attempt: true.

Operational interpretation:

1. all four Kubernetes peer pods reached Ready and the bounded smoke completed;
2. every observed decision-bound NEW outcome had exactly one matching generic successful-forward event;
3. no observed DUPLICATE outcome shared a key with a generic successful-forward event;
4. successful-forward accounting respected `11 <= 17` attempts;
5. normal Q-AHBN2 decision, outcome and reward-closure traces remained present;
6. no FAILED outcome was observed, which is permitted for this frozen no-failure smoke and was already covered deterministically at S17-2;
7. the runner completed with `K3-Q SMOKE PASS` and reported the preserved evidence directory.

This is runtime instrumentation validation only. It does not replace historical formal Kubernetes results, establish corrected formal `total_forwards` values, change the algorithm, or justify a formal rerun scope by itself.

**S17-3 = PASS / CLOSED.**

**Next controlled gate: S17-4 — Smoke Aggregation / Acceptance Audit.**

S17-4 may now determine whether the combined S17-1/S17-2/S17-3 evidence is sufficient to accept the measurement repair and, only then, freeze the scientifically justified formal rerun scope. Formal reruns, manuscript-result replacement, and S18 remain blocked until S17-4 closes.


### S17-4 smoke aggregation / acceptance audit — PASS / CLOSED

S17-4 reconciled the complete remediation chain against the authoritative scientific repository and synchronized Drive evidence.

#### Evidence convergence

**S17-1 — source/runtime repair**

The only production change was in `gke/app/qahbn2_runtime.py`: the decision-bound Q-AHBN2 `resp.ok` branch now emits the common generic `event="forward"` after a successful RPC/ACK, with the inherited forwarding fields plus `decision_id`. No dissemination, target selection, controller, learner, reward, transition, parameter, non-Q method, or ControlSim behavior changed.

Runtime blob after remediation:

`1bc97905f59e7ed701058b08e42a07e30ef934c3`

**S17-2 — deterministic verification**

Five deterministic source/AST guards passed. They establish:
- exactly one generic `forward` for a decision-bound NEW path;
- no generic success on DUPLICATE or FAILED;
- the attempt event precedes forwarding handling and successful-forward count cannot structurally exceed attempt count;
- no double-log on the Q-AHBN2 inherited fallback;
- non-Q-AHBN2 remains a single delegation to the inherited forwarding implementation.

**S17-3 — live Kubernetes verification**

Preserved smoke evidence:

`output/evidence/q-ahbn-gke-03102026111913-k3q-smoke/`

Drive folder ID:

`1dnNThopXkvIhrit6FOEOIQ-Y90A8oNzN`

Execution Git SHA:

`aa91a86eb571dbd61e52a479ba9271c8ddfdcbbf`

Image:

`wwiras/q-ahbn2:s17-3-smoke-20261003`

Digest:

`sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`

Observed accounting:
- F_attempt = 17;
- F_success = 11;
- decision-bound NEW = 11;
- decision-bound generic forward = 11;
- exact NEW/forward key match = true;
- non-NEW/forward overlap = 0;
- F_success <= F_attempt = true;
- observed outcomes = NEW and DUPLICATE;
- decision/outcome/reward traces remained operational.

The no-failure smoke did not produce FAILED outcomes; FAILED logging semantics were already covered deterministically at S17-2.

#### S17-4 acceptance decision

The measurement repair is accepted.

The combined source-level, deterministic, and live-GKE evidence is sufficient to establish that the historical Q-AHBN2 successful-forward accounting defect has been repaired without changing the scientific algorithm or any non-Q comparator execution path.

**S17-4 = PASS / CLOSED.**

#### Minimum scientifically justified formal rerun scope — FROZEN

The formal rerun scope is frozen to:

**Q-AHBN2 only, seeds 42–46, using the already frozen Exp13-Q-K8s protocol coordinates.**

Rationale:

1. the defect is located only in the decision-bound Q-AHBN2 forwarding branch;
2. non-Q-AHBN2 forwarding behavior is unchanged and deterministically verified as inherited single delegation;
3. the original Gossip, Structured, DC-SoC and standalone AHBN formal runs do not depend on the defective Q-AHBN2 logging branch;
4. the affected historical field is Q-AHBN2 `F_success / total_forwards`; re-running unaffected comparator methods would not repair any known defective measurement;
5. delivery ratio, propagation delay, duplicates, and `F_attempt` are not invalidated by this repair;
6. the purpose of the rerun is measurement remediation, not performance optimization or outcome-driven repetition.

Therefore:

- **rerun:** 5 Q-AHBN2 coordinates, seeds 42, 43, 44, 45 and 46;
- **do not rerun:** Gossip, Structured, DC-SoC or AHBN coordinates;
- **preserve:** all historical 25-run evidence and its provenance;
- **do not overwrite:** historical Q-AHBN2 formal artifacts or historical reported values;
- **produce:** a separate post-remediation Q-AHBN2 formal evidence family tied to the repaired runtime/image and the same frozen protocol;
- **later comparison:** unchanged historical comparator evidence may be joined with the post-remediation Q-AHBN2 evidence only under an explicit provenance-aware reconciliation gate.

No manuscript number replacement is authorized yet. No S18 scientific interpretation is authorized yet.

### Next controlled gate

**S17-5 — Q-AHBN2-Only Formal Rerun Preparation / Protocol Reconciliation.**

S17-5 must freeze the post-remediation image, verify the same Exp13-Q-K8s protocol coordinates for seeds 42–46, create a separate evidence namespace, and prepare fail-closed execution/validation. It must not execute formal GKE runs until the preparation gate passes.


### S17-5 Q-AHBN2-only formal rerun preparation / protocol reconciliation — 2026-10-03

**Status: PREPARED / AWAITING LOCAL PREP AUDIT + FORMAL IMAGE FREEZE**

S17-5 implements the S17-4 frozen minimum scope without executing any formal GKE coordinate.

#### Scope freeze

Exactly five post-remediation coordinates are authorized for later execution:

- method: Q-AHBN2 only;
- seeds: 42, 43, 44, 45, 46.

Gossip, Structured, DC-SoC and standalone AHBN are explicitly excluded from the remediation runner.

#### Protocol identity

The remediation runner reuses the frozen K5/Exp13-Q-K8s base:

- N=20;
- BA(m=2);
- inherited K7 common non-structural source policy;
- 240 messages;
- 0.4 s message interval;
- churn offsets +1/+26/+51/+76 s;
- same target-selection helper and topology generator;
- same Q-AHBN2 algorithm/controller/learning contracts;
- same per-coordinate K7 execution and validation path.

No topology, workload, seed, churn, target-selection, controller, learner, reward, transition, or scientific metric rule is altered.

#### Separate evidence namespace

New remediation runner:

`gke/scripts/run_s17_qahbn2_remediation.sh`

Preparation commit:

`cbe17553cbec1f28eea90e35714d5e026f369e33`

Its default evidence root is separately namespaced:

`output/evidence/q-ahbn-gke-<timestamp>-s17-qahbn2-remediation/`

It refuses an existing output root, requires a clean Git worktree, records Git SHA/image/digest, and never writes into the historical K5 formal evidence family.

The runner creates:
- five Q-AHBN2-only configs/topologies;
- a frozen S17 protocol manifest;
- five seed-specific Q-AHBN2 run folders;
- a post-remediation manifest;
- fail-closed validation that `F_success <= F_attempt` for every completed coordinate.

#### Static preparation audit

Added:

`gke/scripts/s17_5_prep_audit.py`

Preparation commit:

`9c0cdcd7aecce2c62a7dc0d31dd208374caa6a98`

The audit verifies:
- Q-AHBN2-only scope;
- exact seed set 42–46;
- absence of multi-method execution selectors;
- reuse of the frozen K5 base;
- N=20, BA(m=2), 240 messages, 0.4 s interval, and +1/+26/+51/+76 s churn offsets;
- separate post-remediation evidence namespace;
- presence of remediation protocol/accounting manifests.

#### Execution boundary

No formal GKE remediation run has started.

Before S17-5 can close and release formal execution, the researcher must:

1. synchronize latest `main`;
2. run the local/static S17-5 prep audit;
3. build a fresh immutable `linux/amd64` formal remediation image from the synchronized post-S17-5-preparation commit;
4. return the image tag and registry digest for readback/freeze.

Until those checks pass:

- the five formal Q-AHBN2 coordinates remain **NOT RELEASED**;
- historical evidence remains untouched;
- manuscript-result replacement is prohibited;
- S18 remains blocked.


### S17-5 closure — local prep audit and formal image freeze

Researcher-executed local/static preparation audit returned:

```text
S17-5 PREP AUDIT PASS
scope=qahbn2-only seeds=42,43,44,45,46
protocol=identical frozen K5 base
namespace=separate post-remediation evidence family
```

A fresh immutable `linux/amd64` formal remediation tag was then built, pushed, registry-verified, and container-import preflighted:

`wwiras/q-ahbn2:s17-remediation-formal-20261003`

Frozen registry digest:

`sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`

The registry digest is identical to the S17-3 smoke-image digest. This is expected and acceptable because the Docker build context/runtime payload is unchanged since the accepted S17-1 repair; the separate immutable tag provides campaign-specific provenance without implying a different runtime binary.

Researcher output confirmed:

- image build/push PASS;
- registry platform verification PASS for `linux/amd64`;
- container import preflight PASS;
- image preflight PASS.

Repository readback at closure confirms:
- remediation runner blob: `fcf8cabac0b15728b39474b153fc5fcfa93e3c71`;
- S17-5 prep-audit blob: `f74b509a054cc57e34fec8959797620db9b62898`;
- repaired runtime blob remains `1bc97905f59e7ed701058b08e42a07e30ef934c3`.

**S17-5 = PASS / CLOSED.**

### Next controlled gate

**S17-6 — Q-AHBN2-Only Formal Remediation Execution (5 runs).**

Released execution scope is exactly:
- method: Q-AHBN2;
- seeds: 42, 43, 44, 45, 46;
- image: `wwiras/q-ahbn2:s17-remediation-formal-20261003`;
- expected digest: `sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`;
- runner: `gke/scripts/run_s17_qahbn2_remediation.sh`;
- separate post-remediation evidence namespace only.

No comparator rerun is authorized. No historical artifact may be overwritten. No manuscript-result replacement or S18 work is authorized. S17-6 execution remains a researcher/manual GKE action.


### S17-6 Q-AHBN2-only formal remediation execution — PASS / CLOSED

Researcher-executed the released five-coordinate remediation campaign on 2026-10-03 using:

- runner: `gke/scripts/run_s17_qahbn2_remediation.sh`;
- image: `wwiras/q-ahbn2:s17-remediation-formal-20261003`;
- expected digest: `sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`;
- execution Git SHA: `352b90091d7c0fec255a9030a5c7d188af2d437b`.

The separate post-remediation evidence root is:

`output/evidence/q-ahbn-gke-03102026113510-s17-qahbn2-remediation/`

Synchronized Google Drive folder ID:

`1cNZ-7ty_PkxeQHoAvvU3JZlI-Y4tewnP`

Completion timestamp recorded in evidence:

`2026-10-03T03:49:59Z`

All five authorized Q-AHBN2 coordinates completed and passed the inherited K7 result validator:

- seed 42: F_attempt=2118, F_success=1539, total_forwards=1539, delivery_ratio=0.37124237965104057, propagation_delay=0.0401592363913854, duplicates=512;
- seed 43: F_attempt=970, F_success=643, total_forwards=643, delivery_ratio=0.18573551263001487, propagation_delay=0.01605471074581146, duplicates=284;
- seed 44: F_attempt=1442, F_success=947, total_forwards=947, delivery_ratio=0.25367012089810015, propagation_delay=0.023390597105026244, duplicates=443;
- seed 45: F_attempt=2951, F_success=2162, total_forwards=2162, delivery_ratio=0.5033726812816189, propagation_delay=0.05044329464435578, duplicates=728;
- seed 46: F_attempt=3774, F_success=2770, total_forwards=2770, delivery_ratio=0.6408662092624356, propagation_delay=0.061876047650973, duplicates=925.

Every coordinate satisfies `F_success <= F_attempt`, and the validator-reported `total_forwards` equals `F_success` for every seed under the repaired instrumentation.

The runner returned:

`S17 Q-AHBN2 FORMAL REMEDIATION 5/5 PASS`

No Gossip, Structured, DC-SoC or standalone AHBN coordinate was rerun. The historical 25-run evidence family remains preserved and untouched.

Drive readback confirms the new evidence family contains:
- `remediation_manifest.json`;
- `s17_protocol_manifest.json`;
- five seed run folders;
- frozen K4/K5 contract copies;
- Git/image/digest provenance;
- start/completion timestamps;
- terminal log.

**S17-6 = PASS / CLOSED.**

This closes execution only. It does not yet authorize replacement of historical manuscript numbers or scientific reinterpretation.

### Next controlled gate

**S17-7 — Post-Remediation Evidence Reconciliation / Acceptance Freeze.**

S17-7 must:
1. read the five post-remediation Q-AHBN2 artifacts;
2. verify protocol/provenance completeness and metric-accounting consistency;
3. reconcile the new Q-AHBN2 measurements against the unchanged historical comparator evidence;
4. determine which Kubernetes table/statistical values are scientifically replaceable and which historical values remain provenance-only;
5. freeze the corrected Kubernetes evidence family before any manuscript update or S18 work.

No manuscript editing or S18 interpretation is authorized until S17-7 closes.


### S17-7 post-remediation evidence reconciliation / acceptance freeze — PASS / CLOSED

S17-7 reconciled the post-remediation Q-AHBN2 evidence against the unchanged historical Kubernetes comparator evidence and froze the corrected authority model.

#### Post-remediation Q-AHBN2 evidence authority

Authoritative corrected Q-AHBN2 Kubernetes evidence family:

`output/evidence/q-ahbn-gke-03102026113510-s17-qahbn2-remediation/`

Synchronized Google Drive folder ID:

`1cNZ-7ty_PkxeQHoAvvU3JZlI-Y4tewnP`

Execution provenance:
- Git SHA: `352b90091d7c0fec255a9030a5c7d188af2d437b`;
- image: `wwiras/q-ahbn2:s17-remediation-formal-20261003`;
- digest: `sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`;
- method: Q-AHBN2 only;
- seeds: 42--46;
- all five coordinates validated.

The frozen per-seed corrected metrics are:

| Seed | Delivery | Delay (s) | Duplicates | F_attempt | F_success / total_forwards |
|---|---:|---:|---:|---:|---:|
| 42 | 0.37124237965104057 | 0.0401592363913854 | 512 | 2118 | 1539 |
| 43 | 0.18573551263001487 | 0.01605471074581146 | 284 | 970 | 643 |
| 44 | 0.25367012089810015 | 0.023390597105026244 | 443 | 1442 | 947 |
| 45 | 0.5033726812816189 | 0.05044329464435578 | 728 | 2951 | 2162 |
| 46 | 0.6408662092624356 | 0.061876047650973 | 925 | 3774 | 2770 |

Corrected Q-AHBN2 means (n=5):
- delivery ratio = **0.3909773807446420**;
- propagation delay = **0.03838477730751038 s**;
- duplicates = **578.4**;
- F_attempt = **2251.0**;
- F_success / total_forwards = **1612.2**.

Sample SDs:
- delivery ratio = **0.184692**;
- propagation delay = **0.018867 s**;
- duplicates = **250.960754**;
- F_attempt = **1131.664703**;
- F_success / total_forwards = **870.341715**.

#### Protocol/provenance acceptance

The five post-remediation coordinates share:
- contract version `k7-exp11-v2`;
- target-selection version `k7-targets-v1`;
- frozen targets 0,5,10,15;
- 240 messages;
- 0.4 s message interval;
- churn offsets 1,26,51,76 s;
- common contract hash `5b26ed302abc57ce2816511f5257da7aca488ba7f3d6686e52483cd3f5675a7d`.

Therefore the post-remediation Q-AHBN2 family is accepted as protocol-consistent and provenance-complete.

#### Corrected Kubernetes authority model

The corrected composite Kubernetes evidence set is now:

1. **Gossip, Structured, DC-SoC, AHBN:** retain their validated historical K5-Q formal coordinates unchanged.
2. **Q-AHBN2:** use the S17 post-remediation five-run family for all publication-facing quantitative values.
3. Historical Q-AHBN2 K5-Q runs remain preserved as provenance/history but are **superseded for quantitative publication use** where the affected execution/accounting semantics could differ.
4. Historical Q-AHBN2 `total_forwards / F_success` values are explicitly non-authoritative.
5. The corrected Q-AHBN2 `F_attempt`, `F_success`, and `total_forwards` are authoritative from S17.
6. For scientific consistency, publication-facing Q-AHBN2 delivery ratio, propagation delay, and duplicates must also come from the same S17 post-remediation coordinates rather than mixing metrics from different executions.
7. Historical comparator metrics remain authoritative because their execution paths were unaffected by the repaired Q-AHBN2 branch.

This preserves seed/method provenance while avoiding a mixed-execution Q-AHBN2 row.

#### Manuscript replacement boundary

Once a dedicated manuscript-update gate is released, T3 / `tab:kubernetes-results` may replace the entire Q-AHBN2 row with the S17-derived Q-AHBN2 statistics while retaining the historical comparator rows.

The previous manuscript explanation that Q-AHBN2 `total_forwards` is instrumentation-noncomparable becomes historical remediation context and should no longer be the publication-facing interpretation after the corrected table is integrated.

Kubernetes remains operational-realization evidence only. This remediation does **not** authorize:
- ControlSim/Kubernetes pooling;
- claims of numerical replication or equivalence;
- Kubernetes confirmation of ControlSim superiority;
- generic low-overhead claims;
- convergence or policy-optimality claims.

**S17-7 = PASS / CLOSED.**

### Next controlled gate

**S17-8 — Corrected Kubernetes Statistical Reconstruction / Manuscript-Update Contract.**

S17-8 should reconstruct the complete publication-facing Kubernetes table/statistics using:
- unchanged historical comparator coordinates;
- S17-remediated Q-AHBN2 coordinates;
- the frozen n=5 mean/SD/95% CI and paired-difference rules.

It must produce the exact corrected values and replacement wording contract before any manuscript source is edited.

S18 remains blocked until the corrected Kubernetes evidence/statistics and manuscript-update contract are frozen.


### S17-8 corrected Kubernetes statistical reconstruction / manuscript-update contract — PASS / CLOSED

S17-8 reconstructed the complete publication-facing Kubernetes statistics from:
- unchanged historical K5-Q formal comparator coordinates for Gossip, Structured, DC-SoC and AHBN;
- S17 post-remediation Q-AHBN2 coordinates for seeds 42--46.

No manuscript source was edited during this gate.

#### Publication-facing method statistics (n=5 each)

All intervals are two-sided 95% Student-t confidence intervals using df=4.

| Method | Delivery mean ± SD [95% CI] | Delay s mean ± SD [95% CI] | Duplicates mean ± SD [95% CI] | F_attempt mean ± SD [95% CI] | Successful forwards / total_forwards mean ± SD [95% CI] |
|---|---|---|---|---|---|
| Gossip | 0.886812 ± 0.017678 [0.864862, 0.908762] | 0.098913 ± 0.052701 [0.033476, 0.164349] | 3485.4 ± 1265.2 [1914.5, 5056.3] | 7489.0 ± 1338.2 [5827.4, 9150.6] | 3959.2 ± 77.5 [3863.0, 4055.4] |
| Structured | 0.081950 ± 0.000747 [0.081023, 0.082878] | 0.003793 ± 0.000542 [0.003120, 0.004466] | 0.0 ± 0.0 [0.0, 0.0] | 153.0 ± 0.0 [153.0, 153.0] | 152.0 ± 0.0 [152.0, 152.0] |
| DC-SoC | 0.409472 ± 0.442103 [-0.139472, 0.958416] | 0.105556 ± 0.135294 [-0.062433, 0.273546] | 3.6 ± 8.0 [-6.4, 13.6] | 1726.0 ± 2101.5 [-883.3, 4335.3] | 1709.2 ± 2099.4 [-897.6, 4316.0] |
| AHBN | 0.260135 ± 0.176009 [0.041590, 0.478679] | 0.025193 ± 0.019750 [0.000670, 0.049715] | 403.6 ± 272.3 [65.6, 741.6] | 1448.0 ± 1089.0 [95.8, 2800.2] | 998.6 ± 828.1 [-29.6, 2026.8] |
| Q-AHBN2 | 0.390977 ± 0.184692 [0.161652, 0.620302] | 0.038385 ± 0.018867 [0.014958, 0.061811] | 578.4 ± 251.0 [266.8, 890.0] | 2251.0 ± 1131.7 [845.9, 3656.1] | 1612.2 ± 870.3 [531.5, 2692.9] |

Negative lower confidence limits for inherently non-negative metrics are retained as untruncated Student-t intervals, not physical predictions.

#### Paired Q-AHBN2 minus AHBN differences by matched seed

| Metric | Mean paired difference | SD | 95% CI |
|---|---:|---:|---:|
| Delivery ratio | +0.130842 | 0.301314 | [-0.243288, +0.504973] |
| Propagation delay (s) | +0.013192 | 0.032827 | [-0.027568, +0.053952] |
| Duplicates | +174.8 | 367.1 | [-281.0, +630.6] |
| F_attempt | +803.0 | 1793.7 | [-1424.2, +3030.2] |
| Successful forwards / total_forwards | +613.6 | 1426.5 | [-1157.7, +2384.9] |

All five paired 95% CIs cross zero.

Therefore the corrected forwarding-accounting repair restores quantitative comparability for Q-AHBN2 successful forwards but does not change the frozen scientific interpretation that the Kubernetes performance contrasts are inconclusive at n=5.

#### Exact manuscript-update contract

For T3 / `tab:kubernetes-results`:

1. retain the historical Gossip, Structured, DC-SoC and AHBN rows;
2. replace the entire Q-AHBN2 row with S17-remediated Q-AHBN2 statistics;
3. replace any Q-AHBN2 successful-forward / `total_forwards` value derived from the historical defective runs with the corrected S17 value;
4. if T3 reports `F_attempt`, use 2251.0 ± 1131.7 [845.9, 3656.1] for Q-AHBN2;
5. if T3 reports successful forwards / `total_forwards`, use 1612.2 ± 870.3 [531.5, 2692.9] for Q-AHBN2;
6. publication-facing paired AHBN--Q-AHBN2 prose must use the corrected paired differences above;
7. remove or rewrite the prior statement that Q-AHBN2 `total_forwards` is instrumentation-noncomparable;
8. replace it with a concise provenance statement that the Q-AHBN2 row was regenerated after correcting a successful-forward logging omission, while comparator rows remain from the unchanged validated historical K5-Q evidence;
9. retain the statement that all paired 95% CIs cross zero and that Kubernetes is operational-realization evidence rather than confirmation of ControlSim superiority;
10. do not claim that the repaired forwarding count implies lower overhead, higher efficiency, superiority, equivalence, transfer, convergence or policy optimality.

#### Evidence provenance to retain in manuscript/supporting records

Historical comparator evidence:
- formal matrix Git SHA: `7ad474c3a249fde58223f2abd5d54918b4bcbb9f`;
- historical image: `wwiras/q-ahbn2:k5q-formal-v2-20260929`;
- digest: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`;
- historical formal Drive folder ID: `15iFp5E2NCKnewFFObLp3xvVQK3IsXjeP`.

Corrected Q-AHBN2 evidence:
- execution Git SHA: `352b90091d7c0fec255a9030a5c7d188af2d437b`;
- image: `wwiras/q-ahbn2:s17-remediation-formal-20261003`;
- digest: `sha256:91eaed37889678b92a6e3fa4338773fcb3d93faa285a3b1bac793610f9aa8666`;
- Drive folder ID: `1cNZ-7ty_PkxeQHoAvvU3JZlI-Y4tewnP`.

The common protocol contract hash remains:
`5b26ed302abc57ce2816511f5257da7aca488ba7f3d6686e52483cd3f5675a7d`.

**S17-8 = PASS / CLOSED.**

### Next controlled gate

**S17-9 — Manuscript-Side Corrected Kubernetes Integration.**

S17-9 may now update the QAHBN2-Manuscript repository using the exact frozen replacement contract above. It must:
- modify only Kubernetes-facing manuscript values/text/provenance affected by the S17 remediation;
- preserve all non-Kubernetes frozen results and claims;
- compile and visually/proof audit the manuscript;
- verify no stale historical Q-AHBN2 forwarding-accounting wording/value remains.

S18 remains blocked until S17-9 manuscript integration and its source/PDF consistency closure are complete.


### S17-9 manuscript-side corrected Kubernetes integration — PASS / CLOSED

The manuscript repository `wwiras/QAHBN2-Manuscript` has been reconciled against the S17-8 replacement contract.

Manuscript-side closure commit:

`d1c77ebfceca2eb58f2fd42051060afd743f812a`

Active manuscript source:

`versions/v0.0/main.tex`

Active source blob after integration:

`c5248da7237131b5c6681a139d63535e26851361`

S17-9 updated only the authorized Kubernetes-facing manuscript material:
- T3 / `tab:kubernetes-results` Q-AHBN row;
- same-seed AHBN--Q-AHBN Kubernetes paired-difference prose;
- table caption;
- Kubernetes/overhead discussion wording;
- manuscript provenance records.

Publication-facing Q-AHBN Kubernetes means are now:
- delivery 0.390977;
- delay 0.038385 s;
- duplicates 578.4;
- successful forwards / `total_forwards` 1,612.2;
- `F_attempt` 2,251.0.

Corrected paired Q-AHBN-minus-AHBN means / 95% CIs:
- delivery +0.130842 [-0.243288,+0.504973];
- delay +0.013192 s [-0.027568,+0.053952];
- duplicates +174.8 [-281.0,+630.6];
- forwarding attempts +803.0 [-1424.2,+3030.2];
- successful forwards +613.6 [-1157.7,+2384.9].

All five intervals cross zero.

Direct active-source readback confirms removal of stale publication-facing values and defect wording:
- no Q-AHBN Kubernetes `total_forwards=10.0`;
- no `2345.4`;
- no `0.392835 / 0.040161 / 665.8`;
- no publication-facing statement that corrected Q-AHBN `total_forwards` is non-comparable;
- no stale “all four” paired-CI wording.

The historical S16-13A defect description remains only as control/provenance history.

Kubernetes remains operational-realization evidence only. No ControlSim/Kubernetes pooling, confirmation, equivalence, generic low-overhead, convergence, or optimality claim is authorized.

A local LaTeX/PDF compile and visual proof remains a production check in the researcher’s synchronized manuscript workspace; it does not change the scientific S17 evidence freeze.

**S17-9 = PASS / CLOSED.**

### Next controlled gate

**S17-10 — Local Manuscript Compile / PDF Visual-Proof Closure.**

S17-10 is restricted to:
1. synchronize the manuscript repository locally;
2. compile `versions/v0.0/main.tex` in the normal manuscript LaTeX environment;
3. inspect the generated PDF around T3 and the affected Kubernetes prose;
4. confirm no overflow, clipping, broken references, or stale rendered values;
5. record the compiled artifact/proof result.

No scientific number change, new experiment, or reinterpretation is authorized at S17-10.

S18 remains blocked until S17-10 closes.


### S17-10 local manuscript compile / PDF visual-proof closure — PASS / CLOSED

Researcher supplied compiled manuscript PDF `main03Oct2026_1223.pdf`.

The 26-page compiled PDF was inspected directly against the S17-9 manuscript/source freeze.

Rendered Kubernetes section confirms:
- Q-AHBN delivery 0.390977;
- delay 0.038385 s;
- duplicates 578.4;
- successful forwards / `total_forwards` 1,612.2;
- `F_attempt` 2,251.0.

Rendered paired Q-AHBN-minus-AHBN contrasts confirm:
- delivery +0.130842 [-0.243288,+0.504973];
- delay +0.013192 s [-0.027568,+0.053952];
- duplicates +174.8 [-281.0,+630.6];
- forwarding attempts +803.0 [-1424.2,+3030.2];
- successful forwards +613.6 [-1157.7,+2384.9].

All five paired 95% confidence intervals cross zero, preserving the frozen conclusion that Kubernetes is operational-realization evidence rather than confirmatory performance evidence.

Visual proof of page 21 / Table 5 found:
- no clipping;
- no overflow;
- no overlapping cells or rules;
- corrected caption and table values legible;
- surrounding text consistent with S17-8/S17-9 claim boundaries.

Whole-PDF readback confirms 26 pages and no stale publication-facing Q-AHBN Kubernetes values/wording in the corrected section.

Manuscript-side S17-10 closure commit:
`6b73f4156646fcf35c6faa75983ae35cf2ce608b`.

No scientific result, parameter, experiment, algorithm, or evidence role changed.

**S17-10 = PASS / CLOSED.**

### Controlled release

S17-0 through S17-10 are now PASS / CLOSED. The forwarding-accounting remediation, formal Q-AHBN2-only rerun, corrected evidence freeze, statistical reconstruction, manuscript integration, and compiled-PDF proof are complete.

**S18 — Post-Remediation Scientific Interpretation / Final Manuscript Consistency Re-Closure is now RELEASED.**

S18 is interpretation/control-only. It must not reopen experiments, parameters, controller logic, Q-learning design, or evidence generation.


---

## S18 — Post-Remediation Scientific Interpretation / Final Manuscript Consistency Re-Closure

**Status: PASS / CLOSED — 2026-10-03.**

S18 reconciled the frozen S12/S12A interpretation and claim contract against the corrected S17 Kubernetes forwarding-accounting evidence. The corrected Q-AHBN2 Kubernetes means are delivery 0.390977, delay 0.038385 s, duplicates 578.4, F_attempt 2251.0, and successful forwards/total_forwards 1612.2. All five corrected paired Q-AHBN2-minus-AHBN 95% CIs cross zero.

Scientific interpretation is unchanged: primary ControlSim remains the comparative performance authority; Exp13-Q remains bounded external positioning; Kubernetes remains complementary operational-realization/observability evidence and does not independently establish a consistent performance advantage. No pooling, replication/equivalence, generic low-overhead, convergence, policy-optimality, global hyperparameter-optimality, universal-superiority, or global-ranking claim is authorized.

Detailed closure authority: `docs/stages/S18_POST_REMEDIATION_RECLOSURE.md`.


---

## S19 — Author Manual-Review Manuscript Improvements

**Programme status: ACTIVE — 2026-10-03.**

The researcher released a bounded post-S18 manuscript-communication programme. It does not reopen experiments, parameters, algorithms, statistical methods, evidence generation, or the S18 claim/evidence contract.

### S19-0 — Manuscript Improvement Backlog Freeze and Authority Reconciliation
**PASS / CLOSED — 2026-10-03.**

Frozen backlog:
- MI-01: ControlSim propagation-delay unit → seconds; Kubernetes remains seconds.
- MI-02: strengthen Introduction/Related Work citation density without unnecessary restructuring.
- MI-03: clarify fixed dissemination → RO2 characterization → AHBN runtime adaptation → Q-AHBN experience-driven bounded refinement.
- MI-04: simplify/polish Figure 1 without changing frozen semantics.
- MI-05: remove unnecessary publication-facing S5 terminology.
- MI-06: correct “Adaptive Hybrid Blockchain Networking” to “Adaptive Hybrid Broadcast Network (AHBN)”.

Detailed authority and execution freeze: `docs/stages/S19_0_MANUSCRIPT_IMPROVEMENT_BACKLOG_FREEZE.md`.

**Next and only released gate: S19-1 — Terminology, Nomenclature and Unit Consistency Remediation.**


### S19-1 — Terminology, Nomenclature and Unit Consistency Remediation
**PASS / CLOSED — 2026-10-03.**

Implemented only MI-01, MI-05 and MI-06 in the active manuscript:
- ControlSim propagation delay is publication-facing **seconds**; Kubernetes remains **seconds**;
- publication-facing `S5` jargon is replaced by canonical fanout terminology without changing thresholds/mapping;
- AHBN is correctly expanded as **Adaptive Hybrid Broadcast Network (AHBN)**.

No scientific number, statistic, experiment, parameter, algorithm, evidence role, citation architecture or S18 claim authorization changed.

Detailed closure authority: `docs/stages/S19_1_TERMINOLOGY_NOMENCLATURE_UNIT_REMEDIATION.md`.

**Next and only released gate: S19-2 — RO2 → AHBN → Q-AHBN Progression Clarification.**


### S19-1 MI-01 source-level corrective amendment — 2026-10-03
A narrow source audit against canonical `wwiras/ahbn@936a79480bc1252c79b6ee01f65c88c740af2844` corrected the earlier S19 assumption that ControlSim propagation delay should be labelled rounds. Canonical metrics compute elapsed simulation-clock time (`max(first_seen_times) - created_at`), transport advances the same clock using `base_delay`, `jitter`, and condition-specific delay terms, and the authoritative AHBN Scientific Reports manuscript reports controlled-simulation propagation delay in seconds. Accordingly, MI-01 is frozen as **ControlSim delay = seconds; Kubernetes delay = seconds**. Numeric evidence and S18 claim boundaries are unchanged. S19-1 remains PASS / CLOSED after corrective re-verification.


### S19-1 MI-01 methodological-rationale preservation — 2026-10-03
For future defence/documentation, the project preserves a separate rationale from the source-level unit correction. Blockchain discrete-event simulation may legitimately use a physical-time clock (including millisecond-scale parameterization) for controlled comparative dissemination studies; this does not imply that a nominal `base_delay=1.0` reproduces typical Internet/WAN blockchain latency. The controlled simulator and Kubernetes serve complementary evidence roles, with no absolute-latency prediction, pooling, equivalence, or literal-replication claim.

A specific interpretation such as `base_delay=1.0 ms`, `jitter=0.2 ms` must not be retroactively inferred from the constants alone. It requires a dimensional-consistency audit of all quantities interacting with the simulation clock before being separately frozen. Detailed rationale and audit boundary are recorded in `docs/stages/S19_1_TERMINOLOGY_NOMENCLATURE_UNIT_REMEDIATION.md`.

The current publication decision remains **ControlSim propagation delay = seconds (s)**. Expressing the same consistently defined simulation clock in milliseconds in a future document would be a unit rescaling, not a change to the underlying propagation-delay definition.


### S19-2 — RO2 → AHBN → Q-AHBN Progression Clarification
**PASS / CLOSED — 2026-10-03.**

MI-03 was implemented as a bounded publication-exposition change. The active manuscript now states the progression in reader-facing terms:
- prior systematic characterization of fixed dissemination mechanisms exposes condition-dependent propagation-delay, delivery, and redundant-communication trade-offs;
- canonical AHBN addresses that condition dependence through deterministic decentralized runtime adaptation from local observations;
- Q-AHBN preserves AHBN as the immutable adaptive baseline and adds only bounded experience-driven refinement after the completed AHBN proposal.

The Introduction carries the main clarification; Related Work contains one bounded reinforcement. No citation was added and no manuscript section was restructured. No scientific evidence, number, experiment, parameter, algorithm, learning contract, or S18 claim/evidence role changed.

Detailed closure authority: `docs/stages/S19_2_RO2_AHBN_QAHBN_PROGRESSION_CLARIFICATION.md`.
Manuscript source commit: `e80a2fcf516f0389e5e033bb9f3842cbbc905cc5`.

**Next and only released gate: S19-3 — Introduction / Related Work Citation-Source Audit.**

S19-3 is restricted to MI-02 audit/reconciliation. Citation insertion and prose integration remain reserved for S19-4.


### S19-3 — Introduction / Related Work Citation-Source Audit
**PASS / CLOSED — 2026-10-03.**

MI-02 was audited without changing active manuscript prose or citations. The audit:
- retained the eight S13-verified literature authorities already used in Related Work;
- rechecked original Drive PDFs for key gossip/structured sources;
- identified Shahsavari et al. (2022) and Pei et al. (2024, Matching-Gossip) as additional verified support for currently uncited framing claims;
- distinguished external literature support from internal AHBN/Q-AHBN project-lineage authority;
- froze a claim-to-source matrix for S19-4.

Key audit conclusions:
- Introduction opening claims about condition-dependent dissemination and delay/overhead trade-offs need citation support;
- the S19-2 progression paragraph should be supported by general trade-off literature plus AHBN self/lineage authority, without presenting unrelated external literature as proof of project lineage;
- most Related Work subsection-specific claims are already adequately supported, but a small number of synthesis/transition sentences would benefit from denser citation support;
- `versions/v0.0/references.bib` is currently empty despite citation keys in `main.tex`; this is a bibliography synchronization/production issue, not a source-validity defect, and remains outside S19-3.

Detailed closure authority: `docs/stages/S19_3_INTRO_RELATED_WORK_CITATION_SOURCE_AUDIT.md`.

**Next and only released gate: S19-4 — Citation-Density Integration.**

S19-4 may add only sources released by S19-3 and make minimal local wording adjustments needed for citation fit. It must not restructure Introduction/Related Work or strengthen claims.


### S19-4 — Citation-Density Integration
**PASS / CLOSED — 2026-10-03.**

MI-02 was implemented using only sources released by S19-3. Citation density was strengthened in the Introduction opening, the fixed-dissemination→adaptation progression paragraph, the Related Work taxonomy opening, the gossip redundancy trade-off sentence, and the runtime-adaptive networking transition. No scientific claim was strengthened and no section was restructured.

The active bibliography, previously empty, was synchronized so every citation key currently used in `main.tex` has a matching BibTeX entry. Newly integrated source keys are `shahsavari_block_2022` and `pei_matching-gossip_2024`; all other keys were already part of the S13-verified set.

Manuscript source commit: `7606f73af22ab0e821857094397c493b9f94a1af`.
Bibliography commit: `297fe7fc15bfbfcc7894171506438833b2ba8bd5`.

Detailed closure authority: `docs/stages/S19_4_CITATION_DENSITY_INTEGRATION.md`.

**Next and only released gate: S19-5 — Figure 1 Presentation Redesign Specification.**

S19-5 is specification/parity-control only for MI-04. It must not alter the active Figure 1 implementation.


### S19-4 corrective citation-density expansion — 2026-10-03
Researcher review reopened S19-4 narrowly because the initial ten-reference implementation was insufficient for the manuscript's literature and methodology lineage. The corrective pass expanded citation coverage across Introduction, Related Work and Methodology without altering scientific claims or section structure.

The expanded source architecture now includes over twenty distinct references spanning blockchain gossip, structured/topology-aware dissemination, adaptive/learning-assisted networking, BA/ER topology foundations, cloud-native/Kubernetes evaluation, and the researcher's prior dissemination/framework publications.

Corrective manuscript commit: `84e499a24ff737ab1f3f70f7cb90c6662871c873`.
Corrective bibliography commit: `515a40274d35e3108f5f7564b534b82e334a2351`.
Detailed amendment: `docs/stages/S19_4_CITATION_DENSITY_INTEGRATION.md`.

**S19-4 remains PASS / CLOSED.**
**Next and only released gate remains S19-5 — Figure 1 Presentation Redesign Specification.**


### Unpublished-source removal correction — 2026-10-03
Researcher confirmed that _Characterizing Latency--Duplication Trade-off in Blockchain Dissemination: A Systematic Study of Gossip and Structured Broadcast_ is not yet published. It is therefore excluded as a publication-facing citation and bibliography entry. It may remain an internal source-map/evidence artifact, but it is not counted among manuscript references.

Removal commits:
- manuscript citation removal: `1502b9617fbd3fd7b5ab025d5d8f29d608b65fb5`
- bibliography-entry removal: `c339cd108b3c1dccfa9c88aea8a81fe90c6c2222`

The active manuscript/reference set is now 26 cited entries, subject to post-write key parity verification.


### S19-5 — Figure 1 Presentation Redesign Specification
**PASS / CLOSED — 2026-10-03.**

MI-04 redesign specification is frozen without modifying the active Figure 1. The current six-stage scientific cycle remains authoritative, but S19-6 may simplify its presentation into three visually grouped layers: canonical adaptation, bounded Q-AHBN refinement, and execution/learning evidence.

The S19-5 contract freezes twelve semantic invariants covering AHBN-first ordering, AHBN immutability, preserved proposal identity, bounded post-AHBN intervention, same canonical EWMA state, requested-versus-realized forwarding, attributable outcomes, reward/transition semantics, Algorithm 1 authority, and prohibition of new scientific semantics.

Detailed authority: `docs/stages/S19_5_FIGURE1_PRESENTATION_REDESIGN_SPECIFICATION.md`.

**Next and only released gate: S19-6 — Figure 1 Presentation Implementation and Semantic-Parity Audit.**


### S19-6 — Figure 1 Presentation Implementation and Semantic-Parity Audit
**PASS / CLOSED — 2026-10-03.**

Implemented the researcher-approved compact vertical Figure 1 in the active manuscript. The central flow is now observations -> immutable AHBN -> preserved AHBN proposal -> bounded Q-AHBN refinement -> refined requested proposal -> eligible-target realization -> directly attributable outcomes -> reward/Q update, with learning feedback returning only to future Q-AHBN decisions.

A companion explanatory paragraph preserves technical content removed from the visual, including the 81-state discretization, five bounded refinements, requested-versus-realized distinction, zero-attempt/no-update case, and same-peer future transition. Algorithm 1 remains unchanged and authoritative for exact ordering.

Manuscript implementation commit: `97be74a444b15b143b5e72405040144856acf284`.
S19-5 geometry amendment: `a5f6624cfed59c944f2635c6c100ea40beb809b4`.
Detailed S19-6 audit: `docs/stages/S19_6_FIGURE1_IMPLEMENTATION_SEMANTIC_PARITY_AUDIT.md`.

P1-P12 semantic parity: PASS.

**Next and only released gate: S19-7 — Whole-Manuscript Consistency / Compile / Visual-Proof Re-Closure.**


### S19-6 corrective Figure 1 loop/overlap refinement — 2026-10-03
Researcher visual review of the compiled Figure 1 identified overlap among side annotations. The active figure was therefore corrected without changing scientific evidence or Algorithm 1.

Corrections:
- increased separation around the same-state annotation;
- isolated the right-side learning-loop label;
- added an explicit local control loop from directly attributable outcomes back to future local observations;
- clarified in the caption/prose that the local control loop and Q-AHBN learning loop are distinct.

The local control loop is architectural only and does not add any new observation dimension, reward term, controller signal or metric.

Corrective manuscript commit:
`c74609e45a03ac2f4d5399e6cd0c7a9f6e642004`.

Detailed S19-6 corrective record:
`docs/stages/S19_6_FIGURE1_IMPLEMENTATION_SEMANTIC_PARITY_AUDIT.md`.

**S19-6 remains PASS / CLOSED.**
**Next and only released gate remains S19-7.**


### S19-6 corrective abstract refinement — 2026-10-03
Researcher-approved abstract wording was integrated after direct verification against the frozen S11-A primary RO4 summary CSV.

The revised abstract now makes the scientific progression explicit:
latency--duplication characterization -> deterministic AHBN adaptation -> bounded Q-AHBN learning refinement.

Primary ControlSim results are reported as relative percentage changes rather than raw absolute metric differences. Verified values are taken directly from S11-A:
- one-peer failure: delivery +17.60%; propagation delay -36.74%;
- tested churn/resource conditions: delivery improvement range +2.88% to +18.23%;
- tested churn/resource conditions: propagation-delay reduction range 11.91% to 37.27%.

Evidence authority:
Drive folder `1XMWn5FWKwJV78YeTGakJb1bVJ6XKfrLH`;
summary CSV `1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`;
registered SHA-256 `9b2d21a103c9cd115acc56a003eb8bab60a49db92bc82af3a8da004d03b33833`.

Manuscript commit:
`cd43b1512737c70f5d603926396c8364e9d10c29`.

**S19-6 remains PASS / CLOSED.**
**Next and only released gate remains S19-7.**


### S19-7 whole-manuscript coherence harmonization — 2026-10-03
**IN PROGRESS.**

The active manuscript has been harmonized to follow one consistent argument:
latency--duplication characterization -> deterministic AHBN runtime balancing -> bounded Q-AHBN experience-driven refinement -> condition-specific delivery/delay gains with explicit communication-overhead cost.

Narrative updates were applied to Introduction, Related Work, Q-AHBN Method, Results, and Discussion. Primary ControlSim prose now uses verified relative percentage effects consistent with the revised abstract, while all frozen tables, figures, absolute paired effects, confidence intervals, algorithms, parameters, and evidence roles remain unchanged.

Manuscript harmonization commit:
`451d86ffc29d6c8ee273258e92df282f77b46b05`.

Detailed record:
`docs/stages/S19_7_WHOLE_MANUSCRIPT_COHERENCE_VISUAL_RECLOSURE.md`.

S19-7 remains open pending full compile and visual/proof inspection.


### S19-7 citation-support correction — 2026-10-03
Researcher review identified publication-facing mentions of Gossip and DC-SoC without nearby literature support. The active manuscript was corrected using only existing vetted bibliography entries:
- Gossip: `berendea_fair_2020`, `baniata_dons_2022`, and where appropriate `li_ls_gossip_2022`;
- DC-SoC: `dong_dc-soc_2024`.

The correction was limited to narrative statements introducing or positioning these comparator families. Numerical table rows, figure labels and this study's own measured values were not externally cited.

Manuscript commit:
`61a49da97641a3be3761f06553549a1ba1c8c571`.

No bibliography entry, experiment, statistic, parameter, evidence family, or claim boundary changed. S19-7 remains IN PROGRESS pending compile/visual proof.


### S19-7 Chapter 2 citation-key synchronization — 2026-10-03
The researcher supplied `ahbnLR26Sept2026chap2_92.bib` as the citation-key authority for overlapping publications.

A DOI/title reconciliation synchronized nine manuscript/bibliography keys to the Chapter 2 naming convention:
`shahsavari_theoretical_2022`, `mao_perigee_2020`, `tang_strategic_2023`, `li_ls-gossip_2022`, `fortino_using_2023`, `mohamed_efficient_2024`, `tran_framework_2022`, `di_perna_impact_2025`, and `koshikawa_impacts_2026`.

Active manuscript commit:
`a7d7aa9155345f9620296b4215c460f72349bcdc`.

Active bibliography commit:
`4b69e36cb546969339ff06fa036c4924410d0ef9`.

Post-write parity audit:
- distinct cited keys: 26;
- bibliography entries: 26;
- missing cited keys: 0;
- uncited bibliography entries: 0.

References without a verified match in the supplied 92-entry bibliography retained their current keys rather than being guessed.

No scientific evidence, claim, result, parameter, figure, or table value changed. S19-7 remains IN PROGRESS pending final compile/visual proof.


### S19-7 whole-manuscript consistency / compile / visual-proof re-closure — 2026-10-03
**PASS / CLOSED.**

Researcher-supplied compiled artifact `main03Oct2026_1910.pdf` (28 pages) was reviewed for whole-manuscript visual/proof consistency.

Verified:
- revised abstract and percentage-based primary-result framing render correctly;
- Introduction/Related Work citation rendering is coherent;
- Figure 1 renders without overlap, with both local-control and learning feedback paths legible;
- Algorithm 1, Figure 2/Table 1, Table 3, Figures 3--5 and Kubernetes Table 5 render legibly;
- no visible figure/table clipping or broken publication-facing reference presentation was found;
- Results, Discussion, Limitations and Conclusion preserve the intended evidence-role boundaries.

Two bounded proof corrections were applied:
1. abstract downstream consensus/fork implication softened to an evidence-aligned formulation;
2. missing cited bibliography key `qiu_geography_2023` restored from validated manuscript repository history.

Manuscript proof-correction commit:
`5972e40d117580e4d00a83d5b9f6c5fe77d10a03`.

Bibliography repair commit:
`b206a4ffdaeec96bf9aba894b5c03cad3562b1e3`.

Post-write citation audit: 27 distinct cited keys; 0 missing cited bibliography keys.

No experiment, parameter, statistical result, algorithm, figure/table value, evidence family, or S18/S19 claim authorization was reopened.

Detailed record:
`docs/stages/S19_7_WHOLE_MANUSCRIPT_COHERENCE_VISUAL_RECLOSURE.md`.


### S19-7 final post-correction PDF re-closure — 2026-10-03
**PASS / CLOSED — FINAL RE-CLOSURE VERIFIED.**

Researcher-supplied `main03Oct2026_1919.pdf` (28 pages) was reviewed as the post-correction compile artifact.

Verified in the final compiled PDF:
- bounded abstract closing implication is rendered;
- Introduction/Related Work citations resolve, including Qiu;
- Figure 1 remains overlap-free and legible;
- Algorithm 1, Figures 2--5 and Tables 1--5 remain visually intact;
- no visible citation placeholder, clipping, or layout regression was found;
- Results/Discussion/Limitations/Conclusion preserve frozen evidence-role and claim boundaries.

No further source changes were required.

Detailed stage record:
`docs/stages/S19_7_WHOLE_MANUSCRIPT_COHERENCE_VISUAL_RECLOSURE.md`.

S19-7 is now finally re-closed against the 19:19 compiled artifact.


---

# S19-8 — External-Critique Reconciliation and Final Claim-Boundary Audit — 2026-10-04

**Current status: PASS / CLOSED.**

The researcher authorized S19-8 after S19-7. This gate is interpretation/control only and does not reopen experiments, parameters, algorithms, frozen statistics, evidence generation, or Kubernetes execution.

Registered stage record:
`docs/stages/S19_8_EXTERNAL_CRITIQUE_CLAIM_BOUNDARY_AUDIT.md`

The manuscript-side bounded corrections were applied at commit `f51cb4164d12a5dfe304061b3af3757769b32d33`.

Fresh closure artifact: `main04Oct2026_0834.pdf`, Drive ID `1Sa_BKh-tVWP5zkTj2HIgmPdEtW0H7e3o`, 28 pages, 511,544 bytes, local binary SHA-256 `fc542a58f195842e0ec66ca2b2d7f12b851ba2fd7447e9c59749ffcdcc11f4c3`. Source/PDF claim-boundary consistency and whole-document visual proof passed with no scientific or layout regression. S19-8 is PASS / CLOSED; historical S19-7 records remain unchanged.


# S20-0 — Journal-Template Manuscript Architecture Reconciliation — 2026-10-05

**Status:** PASS / CLOSED — administrative publication-architecture reconciliation only.

Researcher-approved manuscript-source convention:
- publication repository: `wwiras/QAHBN2-Manuscript`;
- active journal-template source: root `sn-main.tex`;
- shared bibliography for all manuscript/revision sources: root `references.bib`;
- no `versions/` directory is required prospectively;
- Git history and root-level immutable manuscript snapshots provide source history;
- when a reviewer revision is opened, preserve the submitted source unchanged and create the next root-level source using the `sn-main<revision>.tex` convention (for example, first revision `sn-main1.0.tex`);
- figures, diagrams and manuscript tables are authored natively in LaTeX/TikZ/PGFPlots where practical; no dedicated tracked image/table directory is required for publication artifacts generated natively;
- journal-supplied class/style support files may remain at repository root as required by the target template;
- `output/` remains Git-ignored working/build space; Drive synchronization alone does not promote artifacts to scientific evidence.

The previous `versions/vX.Y/main.tex` convention is superseded prospectively. Historical records that mention it remain historical provenance and must not be rewritten to imply that past gates used the new path.

Current scientific authority remains unchanged:
- pinned manuscript science baseline: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 claim and evidence boundaries remain in force;
- no experiment, parameter, algorithm, statistic, result, evidence family or claim authorization is reopened.

The manuscript repository and its Google Drive counterpart were reconciled before this update. At reconciliation, root `sn-main.tex` and root `references.bib` were present and the journal-template support files were synchronized.

**Next controlled programme:** journal-specific formatting and submission-requirement adaptation may proceed from root `sn-main.tex` without changing the frozen scientific evidence or claim boundaries.


# S20-1 — Overleaf PGFPlots Compatibility Remediation — 2026-10-05

**Status:** PASS / CLOSED — publication-formatting compatibility only.

Trigger:
- Overleaf reported `Package pgfkeys Error: I do not know the key '/pgfplots/line width'` at root manuscript `sn-main.tex` line 514.

Reconciliation:
- manuscript repository `wwiras/QAHBN2-Manuscript` current root `sn-main.tex` was compared with the synchronized Drive counterpart under folder `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`;
- the offending option was confirmed in the shared `groupplot` axis option list as `line width=0.9pt`;
- no Drive/GitHub divergence was identified at the affected block.

Correction:
- removed axis-level `line width=0.9pt`;
- preserved the exact visual intent by moving `line width=0.9pt` into `every axis plot/.append style={...}`, where TikZ drawing options are valid;
- manuscript correction commit: `b0108e0c22587e49acb3f54f4d10145601cb3b02`.

Scientific boundary:
- no experiment, parameter, algorithm, statistic, plotted value, axis limit, marker size, series color, caption, interpretation, evidence family, claim boundary, bibliography, or manuscript prose changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** source-level compatibility defect corrected. Researcher should recompile the synchronized Overleaf project to confirm the provider-side build no longer emits this key error.


# S20-2 — Overleaf algpseudocode Compatibility Remediation — 2026-10-05

**Status:** PASS / CLOSED — publication-formatting compatibility only.

Trigger:
- Overleaf reported `Undefined control sequence` for `\When` at root manuscript `sn-main.tex` line 467 and `\EndWhen` at line 474.

Reconciliation:
- current manuscript repository `wwiras/QAHBN2-Manuscript` and current scientific master were re-fetched before editing;
- the algorithm environment uses `algorithm`, `algorithmicx`, and `algpseudocode`;
- the offending block used `\When...\EndWhen`, commands not defined by the standard `algpseudocode` vocabulary.

Correction:
- replaced `\When{all direct attempts owned by $D_t$ have terminated}` with `\While{not all direct attempts owned by $D_t$ have terminated}`;
- replaced `\EndWhen` with `\EndWhile`;
- manuscript correction commit: `42276cb82a9ac6ea6112ce2b7bae270b6935436e`.

Scientific boundary:
- the change is pseudocode syntax/compatibility only;
- no experiment, parameter, algorithmic state/action/reward/transition semantics, numerical value, result, claim boundary, bibliography, or scientific interpretation was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** unsupported pseudocode commands were removed using standard `algpseudocode` constructs. Researcher should recompile Overleaf to confirm these undefined-control-sequence errors are cleared.


# S20-3 — Overleaf Warning Cleanup — 2026-10-05

**Status:** PASS / CLOSED — preamble compatibility cleanup only.

Trigger:
- Overleaf emitted:
  - `Package caption Warning: Unknown document class (or package), standard defaults will be used`;
  - multiple `Font shape U/rsfs/m/n ... not available` warnings;
  - `Size substitutions with differences`.

Reconciliation and cause:
- root `sn-main.tex` uses Springer Nature class `sn-jnl`;
- the manuscript explicitly loaded `caption` and `subcaption`, while no `subcaption`, `subfigure`, `subfloat`, or `captionof` usage was found;
- the manuscript explicitly loaded `mathrsfs`, while no `\mathscr` usage was found;
- the rsfs font warnings are therefore attributable to an unused package requesting unavailable script-font sizes;
- the caption warning is attributable to loading the generic caption package on top of the custom Springer class despite no manuscript need for that package.

Correction:
- removed unused `\usepackage{caption}`;
- removed unused `\usepackage{subcaption}`;
- removed unused `\usepackage{mathrsfs}`;
- manuscript correction commit: `a3165ca5d26f4c90cceca8c55316353a5c78db6d`.

Scientific boundary:
- no manuscript prose, captions, figure content, data, algorithm, equation semantics, experiment, parameter, result, bibliography, or claim boundary changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** the listed caption and rsfs/font-size substitution warnings should clear on the next clean Overleaf compile. If any size-substitution warning remains, it should be re-evaluated from the fresh log because it may originate from a different font family in the Springer class rather than from rsfs.


# S20-4 — Journal Title-Page / Abstract Compliance Adaptation — 2026-10-05

**Status:** PASS / CLOSED — journal-specific manuscript adaptation only.

Trigger:
- target-journal preparation guidance requires:
  - a title page that identifies the article appropriately, lists full author names/institutional addresses, and indicates the corresponding author;
  - an abstract of 150--250 words with no undefined abbreviations or unspecified references;
  - continuity between title/abstract framing and the full manuscript narrative.

Reconciliation:
- manuscript and scientific repositories were re-fetched at current HEAD before editing;
- the existing title, author list, affiliations and corresponding-author marker already satisfy the supplied title-page requirements;
- no collaboration-group authorship is present;
- the current manuscript contains no LLM author attribution;
- the existing abstract exceeded the requested 150--250-word range.

Decision and correction:
- retained the existing title unchanged because it already identifies Q-AHBN, bounded Q-learning refinement, adaptive blockchain dissemination, and dynamic network conditions;
- retained the existing full author names, institutional addresses and corresponding-author designation unchanged;
- replaced only the abstract with a compressed evidence-faithful version within the required 150--250-word range;
- preserved the existing narrative spine used throughout Introduction, Discussion and Conclusion:
  `latency--duplication trade-off -> deterministic AHBN -> bounded Q-AHBN refinement -> condition-specific delivery/delay gains -> communication-overhead cost -> bounded external positioning -> Kubernetes operational realization`;
- no additional cross-section scientific rewrite was required because the existing Introduction, Discussion and Conclusion already use this same progression;
- manuscript correction commit: `fbb5f699a7c6e4075948d8e4abd66d9e29d160cd`.

Scientific boundary:
- no experiment, parameter, algorithm, numerical result, evidence family, statistical interpretation, claim boundary, bibliography, or title was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** supplied title-page requirements are satisfied by the existing title/author/affiliation structure, and the abstract is now journal-range compliant while remaining synchronized with the manuscript's established scientific narrative.


# S20-5 — Table 3 Landscape Readability Adaptation — 2026-10-05

**Status:** PASS / CLOSED — publication-layout/readability only.

Trigger:
- compiled manuscript review showed Table 3 (`tab:primary-paired-results`) was too small to read comfortably in portrait orientation because it was rendered as a `table*` and then globally shrunk with `\resizebox{\textwidth}{!}{...}`.
- researcher requested Springer-style `sidewaystable` presentation with the table rotated 90 degrees.

Reconciliation:
- current manuscript and scientific master were re-fetched before editing;
- `rotating` is already loaded in the manuscript preamble, so no new package was required;
- all Table 3 values, condition labels, caption meaning, label and surrounding result interpretation were preserved exactly.

Correction:
- replaced `table*` with `sidewaystable`;
- removed global `\resizebox{\textwidth}{!}{...}` shrinkage;
- changed the internal table to `tabular*` over `\textheight`, following the Springer example pattern for rotated wide tables;
- increased readable table typography from `\scriptsize` to `\small` and restored wider column spacing;
- retained `\label{tab:primary-paired-results}` unchanged, preserving all manuscript cross-references;
- manuscript correction commit: `e3cf938edbc677180406de1bc898268220cacd46`.

Scientific boundary:
- no experiment, parameter, numerical value, statistical result, confidence interval, caption interpretation, evidence role, claim boundary, bibliography, or manuscript prose was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** Table 3 should now occupy a rotated landscape page and be substantially more readable than the previous portrait `resizebox` rendering. A fresh Overleaf compile is required for final visual confirmation.


# S20-6 — Table 3 True-Landscape Page Remediation — 2026-10-05

**Status:** PASS / CLOSED — publication-layout/readability only.

Trigger:
- researcher visually confirmed that the S20-5 `sidewaystable` solution still required the reader to turn their head because it rotated the table content on an otherwise portrait-oriented PDF page;
- researcher requested the same true landscape-page behavior used in the supplied thesis example, where the PDF page itself rotates 90 degrees and the content remains upright to the reader.

Reconciliation:
- current manuscript and scientific master were re-fetched before editing;
- `pdflscape` is already loaded in the manuscript preamble, so `landscape` page rotation is available without adding packages;
- all Table 3 values, caption wording, label, and result interpretation were preserved.

Correction:
- replaced `sidewaystable` with a `landscape` environment containing a normal `table[p]`;
- retained `\small` text and `\tabcolsep=6pt`;
- changed the internal table width from `\textheight` to `\linewidth` so it uses the landscape page text width naturally;
- retained `\label{tab:primary-paired-results}` unchanged;
- manuscript correction commit: `8f4db362034f306b99eac1d39878e8b45648a4aa`.

Scientific boundary:
- no experiment, parameter, numerical value, confidence interval, statistical interpretation, caption meaning, evidence role, claim boundary, bibliography, or manuscript prose was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** the PDF viewer should rotate the Table 3 page itself into landscape orientation, allowing the table to be read normally without the reader turning their head. A fresh Overleaf compile is required for final visual confirmation.


# S20-7 — Table 2 Width / Article-Block Fit Adaptation — 2026-10-05

**Status:** PASS / CLOSED — publication-layout/readability only.

Trigger:
- compiled manuscript review showed Table 2 (`tab:learning-mechanism`) was readable but visually too wide, with its rules and paragraph columns spanning almost the full two-column area and appearing tight against the article block.

Reconciliation:
- current manuscript and scientific master were re-fetched before editing;
- Table 2 used three fixed paragraph columns of `3.0cm + 6.0cm + 6.0cm`, before normal tabular inter-column padding;
- all Table 2 wording, evidence statements, quantitative values, caption, label, and interpretation were preserved.

Correction:
- retained the `table*` environment and `\small` typography;
- reduced the fixed paragraph widths to `2.7cm + 5.45cm + 5.45cm`;
- set `\tabcolsep=5pt` locally for Table 2 to provide a controlled fit inside the article text block;
- no `resizebox`, scaling, landscape rotation, or font-size reduction was introduced;
- manuscript correction commit: `319b63010c2783a5f4ee6e5291074d7070842d54`.

Scientific boundary:
- no manuscript prose, experiment, parameter, numerical value, learning-mechanism evidence, scientific role, claim boundary, bibliography, or interpretation was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** Table 2 should remain readable at the same font size while fitting more comfortably within the two-column article width. Fresh Overleaf compilation is required for final visual confirmation.


# S20-8 — Figure 1 Article-Width Fit Adaptation — 2026-10-05

**Status:** PASS / CLOSED — publication-layout/readability only.

Trigger:
- compiled manuscript review showed Figure 1 (`fig:qahbn-cycle`) extended too broadly across the article width because the left control loop, right learning loop and side-note spacing added substantial horizontal extent around the central Q-AHBN architecture stack.

Reconciliation:
- current manuscript and scientific master were re-fetched before editing;
- Figure 1 is native TikZ and all node text, architecture semantics, arrows, caption, label and surrounding interpretation were preserved.

Correction:
- reduced side-note width from `3.5cm` to `3.0cm`;
- reduced the side-note offset from `1.00cm` to `0.65cm`;
- moved the right learning-loop return path from `xshift=3.1cm` to `xshift=2.25cm`;
- moved the left control-loop return path from `xshift=-4.5cm` to `xshift=-3.35cm`;
- retained the central block dimensions, text sizes, arrow semantics and `figure*` environment unchanged;
- no global scaling or font-size reduction was introduced;
- manuscript correction commit: `d7ef115bd348412f2fe6aa4f79d8cbae0dd1eaad`.

Scientific boundary:
- no architecture meaning, algorithm, parameter, state/action/reward semantics, numerical value, result, caption interpretation, claim boundary, bibliography, or manuscript prose was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** Figure 1 should fit more comfortably inside the two-column article block while retaining readable labels and the same visual hierarchy. Fresh Overleaf compilation is required for final visual confirmation.


# S20-9 — Figure 1 Auxiliary-Label Overlap Remediation — 2026-10-05

**Status:** PASS / CLOSED — publication-layout/readability only.

Trigger:
- fresh compiled review after S20-8 confirmed that Figure 1 now fits the article width, but the auxiliary labels overlapped or visually crowded the dashed feedback paths, especially the left canonical-state note and the two loop labels.

Reconciliation:
- current manuscript and scientific master were re-fetched before editing;
- Figure 1 remains a native TikZ architecture figure;
- no scientific content, architecture relation, node order, arrow direction, caption, label, or surrounding interpretation required change.

Correction:
- reduced auxiliary loop-label font from `\scriptsize` to `\tiny`;
- reduced side-note font from `\scriptsize` to `\tiny`;
- narrowed the side-note text box from `3.0cm` to `2.6cm`;
- moved the canonical-state side note slightly upward and closer to the Q-AHBN block;
- shortened the side-note wording from `same EWMA snapshot / discretized into 3^4=81 Q states` to the equivalent compact form `same EWMA snapshot / 3^4=81 Q states`;
- moved both feedback-loop labels slightly above their dashed horizontal paths and compressed each to two visual lines;
- retained the figure orientation, article-width fit, central block dimensions, and all feedback-arrow coordinates;
- manuscript correction commit: `53d5bbaabddcbda6292da013166ddea442ccc4c4`.

Scientific boundary:
- no architecture semantics, state/action/reward logic, algorithm, parameter, evidence, result, claim boundary, bibliography, or scientific interpretation was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** Figure 1 should remain upright and within article width, with the side note and feedback-loop labels visually separated from the dashed arrows. Fresh Overleaf compilation is required for final visual confirmation.


# S20-10 — Figure 5 X-Axis Label Readability Adaptation — 2026-10-05

**Status:** PASS / CLOSED — publication-layout/readability only.

Trigger:
- compiled manuscript review showed Figure 5 (`fig:exp13-bounded-positioning`) x-axis method labels visually crowding the x-axis baseline in the 2x2 PGFPlots layout.

Reconciliation:
- current manuscript and scientific master were re-fetched before editing;
- Figure 5 data, five-method order, panel dimensions, axes, error bars, caption, label and scientific interpretation were preserved.

Correction:
- changed only the shared Figure 5 x-tick label style from `font=\scriptsize` to `font=\tiny`;
- added `yshift=-1pt` to move the rotated labels slightly farther below the x-axis;
- retained the existing 25-degree rotation and east anchoring;
- manuscript correction commit: `86e9232bc344a5d87e407498807de7468e9d4ea5`.

Scientific boundary:
- no plotted value, error bar, method order, axis scale, benchmark condition, statistical interpretation, caption meaning, evidence role, claim boundary, bibliography, or manuscript prose was changed;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Expected result:** Figure 5 method labels should remain legible while sitting more clearly below the x-axis line. Fresh Overleaf compilation is required for final visual confirmation.


# S20-11 — Target-Journal Literature Integration: Journal of Cloud Computing — 2026-10-05

**Status:** PASS / CLOSED — literature/context integration only.

Trigger:
- researcher requested identification and integration of blockchain-related literature from *Journal of Cloud Computing: Advances, Systems and Applications*, preferably directly relevant to blockchain dissemination.

Search and selection:
- target-journal search identified one directly relevant open-access research article:
  Chunhai Li, Qiyong Chen, Mingfeng Chen, Zhaoyu Su, Yong Ding, Dapeng Lan, and Amir Taherkordi, “Blockchain enabled task offloading based on edge cooperation in the digital twin vehicular edge network,” *Journal of Cloud Computing*, vol. 12, article 120, 2023, DOI `10.1186/s13677-023-00496-6`;
- the paper explicitly models blockchain block broadcast among verifier edge servers and includes broadcast time as part of the consensus-stage communication cost, making it substantively relevant to the manuscript's dissemination/network-latency framing;
- broader Journal of Cloud Computing blockchain/cloud review papers were identified but not forced into the dissemination argument because they are less directly aligned with propagation/broadcast.

Manuscript integration:
- added `li_blockchain_enabled_2023` to the opening Related Work citation set;
- added one bounded sentence stating that recent cloud/edge-oriented blockchain work models block broadcasting as an explicit consensus-stage communication cost among distributed verifier nodes, reinforcing dissemination latency as a system concern beyond cryptocurrency-only settings;
- no literature-wide priority, superiority, novelty or direct comparability claim was introduced;
- manuscript integration commit: `577a6e212abdd8691f7ff08ced6af2e9571a5040`.

Bibliography integration:
- added BibTeX entry `li_blockchain_enabled_2023` to root `references.bib`;
- bibliography commit: `ee7b9ace61aa33925f545fb5b3d3c3ec6f51a209`.

Scientific boundary:
- no experiment, parameter, algorithm, numerical result, statistical interpretation, evidence family, benchmark result, claim boundary, or frozen conclusion was changed;
- literature integration strengthens contextual positioning only;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** one directly relevant target-journal blockchain broadcast/propagation citation is now integrated into the manuscript and bibliography with evidence-bounded wording.


# S20-12 — Zotero Citation-Key / Bibliography Authority Reconciliation — 2026-10-05

**Status:** PASS / CLOSED — bibliographic authority alignment only.

Trigger:
- researcher supplied authoritative Zotero-exported `1item.bib` for the Journal of Cloud Computing paper previously integrated under S20-11 and requested `sn-main.tex` and `references.bib` be aligned, particularly the citation key.

Authoritative attached item:
- citation key: `li_blockchain_2023`;
- title: `Blockchain enabled task offloading based on edge cooperation in the digital twin vehicular edge network`;
- DOI: `10.1186/s13677-023-00496-6`;
- journal field: `J Cloud Comp`;
- year: 2023; volume: 12; number: 1; page/article: 120.

Reconciliation and correction:
- current manuscript and bibliography were re-fetched from `wwiras/QAHBN2-Manuscript` before editing;
- replaced both manuscript citations from provisional key `li_blockchain_enabled_2023` to authoritative Zotero key `li_blockchain_2023`;
- replaced the provisional hand-authored bibliography record with the researcher-supplied Zotero-exported record from `1item.bib`;
- manuscript citation-key commit: `fa5ad6228ee1fe3d03e43ad1e88aa63944766c21`;
- bibliography authority commit: `49c26cf24d270a4dcfafa2fee9336d278ae84d82`.

Scientific boundary:
- no literature interpretation, manuscript prose, experiment, parameter, numerical result, evidence role, claim boundary, or conclusion was changed;
- this gate only aligns citation identity/metadata with the researcher's bibliography authority;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** the Journal of Cloud Computing citation is now consistently keyed as `li_blockchain_2023` in both `sn-main.tex` and `references.bib`, with the bibliography entry sourced directly from the attached Zotero export.


# S20-13 — Source-Bounded Li et al. Claim Tightening — 2026-10-05

**Status:** PASS / CLOSED — literature wording alignment only.

Trigger:
- direct audit of the attached Li et al. (2023) paper showed that the strongest source support is on pp. 8--9, where the blockchain consensus phase is explicitly decomposed into block production, block broadcast, block verification and block confirmation, and block-broadcast time (T_{bb}) contributes to consensus cost (U_{BC});
- the prior manuscript sentence included the broader interpretive phrase `first-class system concern beyond cryptocurrency-only settings`, which was defensible as synthesis but not stated directly by the source.

Correction:
- replaced the broader sentence with:
  `Recent cloud/edge-oriented blockchain work likewise models block broadcasting among verifier edge servers as an explicit component of consensus delay and cost \cite{li_blockchain_2023}.`
- retained citation key `li_blockchain_2023`;
- `references.bib` unchanged because S20-12 already reconciled the Zotero-authoritative record;
- manuscript correction commit: `b4eb16bf74c1abd06a36bc2481aed8f8330aeb54`.

Scientific boundary:
- no experiment, parameter, algorithm, result, evidence family, benchmark interpretation, claim boundary, bibliography metadata, or conclusion changed;
- the change narrows literature wording to match the attached source more directly;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** the Li et al. citation is now phrased at the strongest directly source-supported level for Q1 defensibility.


# S20-14 — Funding / Competing-Interests Declaration Integration — 2026-10-05

**Status:** PASS / CLOSED — administrative manuscript-compliance only.

Trigger:
- researcher supplied the final funding and competing-interests statements for the target journal manuscript;
- researcher also supplied Journal of Cloud Computing example papers for formatting reference.

Example review:
- Journal of Cloud Computing examples use explicit end-matter declaration sections such as `Funding` and `Competing interests`, rather than retaining the Springer template instruction checklist;
- one reviewed example states its funding under a dedicated `Funding` heading and uses the declaration wording `The authors declare no competing interests.`

Correction:
- removed the Springer template placeholder declaration instructions and checklist from root `sn-main.tex`;
- inserted:
  - `\subsection*{Funding}`
  - `This research was supported by the Internal Matching Grant -- Public Service Department (JPA) of Malaysia. The funders had no role in the study design, data collection and analysis, decision to publish, or preparation of the manuscript.`
  - `\subsection*{Competing interests}`
  - `The authors declare that they have no competing interests.`
- manuscript commit: `d33f2f1f3b80daef494b41f0f154f2d8b7b7c298`.

Scientific boundary:
- no experiment, parameter, algorithm, result, evidence family, statistical interpretation, claim boundary, bibliography, conclusion, or scientific prose changed;
- this gate is administrative/compliance only;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** the manuscript now contains explicit journal-style Funding and Competing interests declarations and no longer contains the generic Springer declaration-template checklist.


# S20-15 — Author-Contributions Declaration Integration — 2026-10-05

**Status:** PASS / CLOSED — administrative manuscript-compliance only.

Trigger:
- researcher approved the final author-contributions statement for the target journal manuscript.

Correction:
- added `\subsection*{Author contributions}` to the Declarations section of root `sn-main.tex`;
- inserted the researcher-approved contribution statement for Samsuddin Samsuddin Wira, Chee Keong Tan, Wai Peng Wong, and Ian K.T. Tan;
- retained the existing Funding and Competing interests declarations unchanged;
- manuscript commit: `8aa5f05238960f18afa122307f0a3180d36fbadd`.

Consistency note:
- the manuscript front matter currently still contains `\equalcont{These authors contributed equally to this work.}` markers for Chee Keong Tan, Wai Peng Wong, and Ian K.T. Tan;
- these markers were not changed in this gate because the researcher approved only the Author contributions declaration text;
- they should be reviewed separately if the manuscript is intended to avoid an equal-contribution claim that is not reflected by the approved contribution statement.

Scientific boundary:
- no experiment, parameter, algorithm, result, evidence family, statistical interpretation, claim boundary, bibliography, conclusion, or scientific prose changed;
- this gate is administrative/compliance only;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** the manuscript now contains the approved Author contributions declaration in the target-journal end matter.


# S20-16 — Abbreviation Definition / List Compliance Audit — 2026-10-05

**Status:** PASS / CLOSED — manuscript-compliance and terminology-normalization only.

Trigger:
- target-journal guidance requires abbreviations to be defined at first use and a consolidated List of abbreviations to be provided;
- researcher supplied compiled PDF `main05Oct2026_2217.pdf` for cross-checking against source.

Audit scope:
- reconciled current manuscript repository and scientific master before editing;
- audited root `sn-main.tex` and the 34-page compiled PDF for abbreviations appearing in narrative text, tables, figures, captions, methods, declarations, and front matter;
- excluded bibliography-only journal/conference acronyms and algorithm action tokens that are not manuscript abbreviations requiring glossary treatment.

Controlled first-use corrections:
- `peer-to-peer (P2P)` defined in the abstract;
- `Adaptive Hybrid Broadcast Network (AHBN)` retained at first abstract use;
- `Q-learning Adaptive Hybrid Broadcast Network (Q-AHBN)` defined at first abstract use;
- `Density-Clustering Socially-aware Communication (DC-SoC)` defined at first substantive use;
- `Barabási--Albert (BA)` defined at first methodology use;
- `Google Remote Procedure Call (gRPC)` defined at first deployment-methodology use;
- `confidence interval (CI)` introduced in Table 3 before later abbreviated header reuse;
- `exponentially weighted moving averages (EWMAs)` was already defined at first use;
- JPA is expanded in the Funding declaration and retained in the consolidated list.

List inserted:
- AHBN — Adaptive Hybrid Broadcast Network
- BA — Barabási--Albert
- CI — Confidence interval
- DC-SoC — Density-Clustering Socially-aware Communication
- EWMA — Exponentially weighted moving average
- gRPC — Google Remote Procedure Call
- JPA — Public Service Department of Malaysia (Jabatan Perkhidmatan Awam)
- P2P — Peer-to-peer
- Q-AHBN — Q-learning Adaptive Hybrid Broadcast Network

Placement:
- added `\section*{List of abbreviations}` immediately before `Declarations`, using a compact two-column tabular layout consistent with the supplied journal example.

Exclusions:
- bibliography-only acronyms such as IEEE, ACM, IJACSA, PODC, NIPS, BCCA, ICBC, ISSN, DOI-like identifiers, and journal abbreviations are reference metadata rather than manuscript-defined scientific abbreviations;
- internal control labels such as S11-A, S12A, S17, AR-1.4.4 and action tokens KEEP/FANOUT_UP/FANOUT_DOWN/SET_GOSSIP/SET_STRUCTURED are experiment/control identifiers or algorithm literals and were not added to the abbreviation glossary.

Manuscript commit:
- `be81bc7d7c6526c75f04de40f7ae60384549097b`.

Scientific boundary:
- no experiment, parameter, result, statistical interpretation, evidence family, benchmark conclusion, claim boundary, bibliography entry, or scientific conclusion changed;
- the change is terminology/compliance only;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** the manuscript now defines the substantive abbreviations at first use and contains a consolidated journal-style List of abbreviations.


# S20-16R — Combined Abbreviations + Mathematical Notation Audit — 2026-10-05

**Status:** PASS / CLOSED — supersedes the abbreviation-only scope of S20-16.

Trigger:
- researcher clarified, based on target-journal examples, that the end-matter terminology aid should include not only acronym expansions but also recurring mathematical/algorithmic notation used in the manuscript;
- researcher explicitly requested a full re-audit of root `sn-main.tex` before revision.

Reconciliation and audit:
- current `wwiras/q-ahbn2` and `wwiras/QAHBN2-Manuscript` heads were reconciled before editing;
- the latest manuscript already contained the S20-16 abbreviation list and the researcher's subsequent removal of JPA from that list was preserved;
- recurring notation was re-audited across the Q-AHBN method, Algorithm 1, statistical analysis, Tables 3--5, figures, and Kubernetes results;
- one-off symbols and obvious action literals were excluded to prevent the glossary from becoming a formula dump.

Retained abbreviations:
- AHBN — Adaptive Hybrid Broadcast Network
- BA — Barabási--Albert
- CI — Confidence interval
- DC-SoC — Density-Clustering Socially-aware Communication
- EWMA — Exponentially weighted moving average
- gRPC — Google Remote Procedure Call
- P2P — Peer-to-peer
- Q-AHBN — Q-learning Adaptive Hybrid Broadcast Network

Recurring/interpretation-critical symbols added:
- `d, ell, u, c` — local duplicate, latency, utilization, churn observations;
- `hat d_t, hat ell_t, hat u_t, hat c_t` — canonical EWMA observation state;
- `z_t`, `w_t` — canonical AHBN score and mode-selection weight;
- `k_AHBN`, `p_AHBN`, `p_Q`, `k_Q`, `k_real`, `N_e` — canonical/refined proposal and eligible-target notation;
- `s_t`, `a_t`, `D_t`, `F_t`, `R_t`, `Q(s,a)` — learning/attribution notation;
- `alpha_Q`, `alpha_AHBN`, `gamma`, `epsilon`, `epsilon_min`, `lambda_epsilon` — learning/control parameters;
- `Delta_i`, `Delta`, `n`, `df` — paired-effect/statistical notation used repeatedly in the results.

Exclusions preserved:
- action literals such as KEEP, FANOUT_DOWN, FANOUT_UP, SET_GOSSIP and SET_STRUCTURED remain algorithm vocabulary rather than glossary abbreviations;
- internal workflow/evidence identifiers such as S11-A, S12A, S17, AR-1.4.4 remain provenance labels rather than reader-facing abbreviations;
- bibliography-only acronyms and publisher/reference metadata remain excluded.

Manuscript change:
- renamed the section to `List of abbreviations and symbols`;
- split it into `Abbreviations` and `Mathematical and algorithmic symbols` subsections;
- manuscript commit: `5191dd12ba48ad39d4e431ef460dc18e2b62f1dd`.

Scientific boundary:
- no experiment, parameter value, algorithm semantics, result, confidence interval, evidence family, benchmark conclusion, claim boundary, bibliography, or scientific conclusion changed;
- this revision is terminology/documentation only;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** S20-16 is revised into a combined abbreviation-and-notation compliance record suitable for the target journal, with recurring reader-facing mathematical notation documented alongside acronym expansions.


# S20-16R1 — Abbreviation Coverage Follow-up — 2026-10-05

**Status:** PASS / CLOSED — follow-up correction to S20-16R.

Trigger:
- researcher identified two additional recurring reader-facing terms omitted from the combined abbreviation/symbol audit:
  - `ControlSim`;
  - `Exp*` experiment-identifier convention.

Correction:
- added under the `Abbreviations` subsection:
  - `ControlSim — Controlled simulation environment`;
  - `Exp* — Experiment identifier, where * denotes the experiment ID`;
- preserved the researcher's earlier removal of JPA from the glossary;
- mathematical and algorithmic symbols remain unchanged;
- manuscript commit: `4a5168e53452afdcc97658175a31ede7fc4ea63b`.

Scientific boundary:
- no experiment, parameter, result, statistical interpretation, benchmark claim, algorithm semantics, bibliography, or conclusion changed;
- this is reader-facing terminology documentation only;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- S12A/S18/S19 scientific closures remain unchanged.

**Result:** the combined list now covers the recurring ControlSim environment name and Exp* experiment-ID convention in addition to the previously audited abbreviations and symbols.


# S20-17A--D — Availability of Data and Materials: Curated Publication Package Staging — 2026-10-05

**Status:** S20-17A PASS / CLOSED; S20-17B PASS / CLOSED; S20-17C PASS / CLOSED; S20-17D PASS / CLOSED; S20-17E HOLD FOR RESEARCHER APPROVAL.

Objective:
- satisfy the remaining Journal of Cloud Computing Availability of data and materials requirement using a curated publication-facing data package;
- do not publish the full source-code snapshot as data and do not publish the complete raw execution/log archive;
- preserve all frozen science, evidence boundaries, and S17 Kubernetes accounting remediation.

Reconciliation:
- scientific repository HEAD before this gate: `d2c910155915032452d3d5c2110eb00ab96f9a9f`;
- manuscript repository HEAD: `4a5168e53452afdcc97658175a31ede7fc4ea63b`;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- required Master, source-authority, results, S11, S13 and S16 records were re-read;
- designated Google Drive evidence hierarchy was reconciled before package construction.

S20-17A — scope/provenance freeze:
- include S11-A primary ControlSim summary + machine-readable aggregation;
- include S11-B Exp13-Q summary + machine-readable aggregation;
- include the pre-formal AR-1.4.2 gamma-sensitivity CSV;
- include a corrected publication-facing Kubernetes operational summary and Q-AHBN-minus-AHBN paired-effect summary;
- exclude source code, smoke/diagnostic/pilot runs, terminal logs, complete raw Kubernetes archive, incidental synchronized output, and superseded pre-remediation Q-AHBN Kubernetes accounting;
- code remains separately available through the public scientific repository and is not duplicated into the data archive.

Kubernetes provenance rule:
- Gossip, Structured, DC-SoC and AHBN retain the validated historical K5 evidence;
- Q-AHBN uses the S17 post-remediation five-run family only;
- the curated Kubernetes summary is therefore aligned with the final manuscript rather than copied wholesale from the superseded pre-remediation matrix.

S20-17B — package construction:
- staged package name: `QAHBN2_JoCC_curated_data_v1.0`;
- staged ZIP: `QAHBN2_JoCC_curated_data_v1.0.zip`;
- package contains 11 files including README, data dictionary, package manifest and SHA-256 checksum list;
- compressed size at staging: approximately 30 KB;
- package is local/staged only and has not been publicly archived.

S20-17C — integrity/parity verification:
- all staged JSON files parse successfully;
- CSV data-row counts: S11-A 32; S11-B 20; gamma sensitivity 15; Kubernetes operational summary 5; Kubernetes paired summary 5;
- all staged file SHA-256 checksums verify;
- ZIP integrity test passes;
- publication-facing Kubernetes values match the current authoritative manuscript table/text;
- no new statistic, experiment, result, parameter, algorithm, evidence family or claim was created.

S20-17D — archival staging:
- README explicitly records curated scope and exclusions;
- data dictionary documents field/evidence meaning and claim boundaries;
- package manifest records science baseline and repository HEADs;
- DOI and archive license remain intentionally unset pending researcher approval;
- no Zenodo record has been published and no DOI has been minted.

Scientific boundary:
- no manuscript science, algorithm, parameter, frozen evidence, statistical interpretation, benchmark conclusion, or claim boundary changed;
- ControlSim and Kubernetes evidence remain separate;
- Kubernetes remains operational-realization/observability evidence only.

**Next controlled gate:** S20-17E — public archival release / DOI minting. This is an irreversible public archival action and is **HOLD pending explicit researcher approval**. After a DOI is obtained, S20-17F will integrate the final Availability of data and materials statement and close the requirement.


# S20-17E--F — Public Data Archival Release and Manuscript Integration — 2026-10-05

**Status:** S20-17E PASS / CLOSED; S20-17F PASS / CLOSED.

S20-17E — public archival release:
- researcher explicitly approved the irreversible Zenodo publication under CC BY 4.0;
- Zenodo record is published and public: DOI `10.5281/zenodo.23165652`;
- record title: `Q-AHBN: Curated Data Supporting Experience-Driven Adaptive Blockchain P2P Dissemination`;
- version: `1.0`; resource type: Dataset; publication date: 2026-10-05;
- deposited file: `QAHBN2_JoCC_curated_data_v1.0.zip`, 29,897 bytes, MD5 `821a8ca821afd1931b9cc425b90d5279`;
- public package contains curated publication-facing data only and excludes research source code and the complete raw execution/log archive;
- no public identifier or link to the internal research-code repository is included in the Zenodo metadata.

S20-17F — manuscript integration:
- added a Journal of Cloud Computing `Availability of data and materials` subsection under Declarations;
- statement cites the version-specific Zenodo DOI and accurately describes included publication-facing data and excluded source-code/raw-archive material;
- manuscript commit: `fcb287548e7760efb422be12debf85ce8cde1faa`;
- no manuscript science, algorithm, parameter, result, statistical interpretation, benchmark conclusion, or claim boundary changed.

Authority clarification:
- the earlier S20-17A--D wording that described the scientific repository as public is superseded for publication-facing disclosure purposes;
- the research code repository is treated as internal and is not identified in the Zenodo record or the manuscript data-availability statement.

**Result:** the Journal of Cloud Computing Availability of data and materials requirement is now DOI-backed and closed under S20-17E/F.


# S20-18 — JoCC Final Compiled-Manuscript Proof Registration — 2026-10-05

**Status:** PASS / CLOSED.

Objective:
- register and verify the latest Journal of Cloud Computing compiled manuscript proof supplied by the researcher after S20-17E/F data-availability closure;
- preserve the existing scientific baseline, evidence boundaries, and manuscript claims.

Reconciliation:
- scientific repository HEAD before this gate: `eb78352de24cc4235745827d7f9f2cc3ea1b0ea1`;
- manuscript repository HEAD before this gate: `fcb287548e7760efb422be12debf85ce8cde1faa`;
- pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
- current `docs/00_QAHBN2_MASTER.md`, source-authority register, results register, and manuscript `sn-main.tex` were re-read before closure;
- manuscript-side Google Drive folder ID `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj` was verified as `QAHBN2-Manuscript`;
- latest compiled JoCC proof was verified in Google Drive as `main05Oct2026_2329.pdf`, 522,898 bytes, created 2026-10-05 15:29 UTC.

Compiled-proof verification:
- proof length: 36 pages;
- title and author block render correctly;
- the manuscript retains the bounded Q-AHBN architecture and frozen science;
- primary ControlSim results, Exp13-Q bounded positioning, and corrected Kubernetes operational-realization evidence are present with their established claim boundaries;
- the Declarations section renders the DOI-backed `Availability of data and materials` statement with Zenodo DOI `10.5281/zenodo.23165652`;
- the statement explicitly excludes research source code, smoke/diagnostic runs, superseded runs, terminal logs, and the complete raw Kubernetes execution archive;
- no public code-repository identifier is included in the data-availability statement.

Authority / workspace note:
- researcher-supplied local scientific workspace: `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`;
- researcher-supplied local manuscript workspace: `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myPaper/ClusterComputing/QAHBN2-Manuscript`;
- local paths are recorded as synchronized researcher workspaces only; direct local-filesystem mutation is outside the current connector environment;
- repository-local `output/` remains Git-ignored and Drive synchronization does not itself promote working artifacts to scientific evidence.

Scientific boundary:
- no experiment, parameter, algorithm, result, statistical interpretation, benchmark conclusion, or claim boundary changed;
- this gate registers and verifies the final compiled JoCC proof only.

**Result:** `main05Oct2026_2329.pdf` is the current registered JoCC compiled manuscript proof following S20-17E/F closure.
