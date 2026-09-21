# Q-AHBN2 Accelerated Design Freeze and Execution Plan

**Document ID:** QAHBN2-DOC-02A  
**Repository:** `wwiras/q-ahbn2`  
**Path:** `docs/02A_QAHBN2_ACCELERATED_FREEZE_PLAN.md`  
**Status:** ACTIVE EXECUTION PLAN  
**Created:** 2026-09-21  
**Purpose:** Time-box the remaining Q-AHBN2 design work while preserving scientific validity, reproducibility, traceability, and all previously frozen design assets.

---

# 1. Why this plan exists

The detailed Q-AHBN2 design-freeze process has already produced substantial scientific value. It has clarified:

- the immutable canonical AHBN boundary;
- Q-AHBN2's meta-controller role above canonical AHBN;
- reward-signal admissibility and attribution;
- reward-event semantics;
- reward-component direction;
- reward representation;
- aggregation structure and double-counting concerns;
- local observability and scientific side-effect constraints.

The remaining project risk is now increasingly **time**, not lack of scientific care.

This document therefore introduces an **Accelerated Controlled Freeze** for the remaining design work.

The objective is not to weaken Q-AHBN2.

The objective is to stop spending unlimited time on increasingly small design questions once they are already scientifically defensible.

---

# 2. Non-negotiable preservation rule

## 2.1 Existing design work is preserved

All approved/frozen material in:

- `docs/01_CANONICAL_AHBN_CONTRACT.md`
- `docs/02_QAHBN2_DESIGN_FREEZE.md`

remains authoritative.

In particular:

> **Section 02.6 and all earlier frozen work are scientific assets, not problems to be compressed, rewritten, or reopened.**

The current detailed controlled process continues through the natural completion of **02.6 Reward Construction**.

This accelerated plan begins **after 02.6 is completed/frozen**.

## 2.2 No retrospective simplification

The accelerated process MUST NOT:

- reopen canonical AHBN;
- alter previously frozen Q-AHBN2 decisions merely for speed;
- rewrite 02.5 or 02.6 to make them shorter;
- remove audit evidence already collected;
- tune Q-AHBN2 to force improvement over AHBN;
- redefine formal metrics after seeing formal results.

If a previously frozen decision is later shown to contain an actual implementation defect or scientific-validity defect, the issue must be recorded explicitly and corrected through normal change control.

---

# 3. Governing acceleration principle

After 02.6, the unit of work changes from:

```text
microscopic question
    ↓
audit
    ↓
freeze
    ↓
next microscopic question
```

to:

```text
coherent design block
    ↓
scientific constraint audit
    ↓
minimal deterministic / micro-case test
    ↓
freeze block
    ↓
move on
```

The governing rule is:

> **Freeze to sufficient scientific defensibility, not theoretical perfection.**

A design block is ready to freeze when it is:

1. internally consistent;
2. causally valid;
3. locally observable where required;
4. free from information leakage;
5. compatible with immutable canonical AHBN;
6. reproducible;
7. minimally tested;
8. adequate to answer the research question.

The design does **not** need to be proven theoretically optimal before formal evaluation.

---

# 4. Decision triage rule

Every unresolved design question after 02.6 MUST be classified into one of three categories.

## Category A — Validity-critical

A wrong decision could:

- invalidate causal attribution;
- introduce future-information leakage;
- silently alter canonical AHBN;
- create reward double counting;
- make the comparison unfair;
- make the implementation scientifically ambiguous;
- break reproducibility;
- invalidate cross-platform parity claims.

**Action:** investigate carefully and resolve before freeze.

## Category B — Design-important but conventional

Several scientifically reasonable choices exist, and no single choice must be proven optimal.

Examples may include:

- reasonable discretization boundaries;
- standard Q-learning hyperparameters;
- initialization choices;
- bounded exploration schedules;
- conventional training settings.

**Action:** choose one defensible option, document rationale, test minimally, freeze, and move on.

## Category C — Performance optimization / tuning

The question is primarily:

> "Would another setting make Q-AHBN2 perform better?"

**Action:** do not expand design work merely to improve expected results.

A Category-C question is not permitted to reopen the design unless it exposes a genuine Category-A validity defect.

---

# 5. Four mandatory gates for each accelerated design block

Each post-02.6 block must pass four gates.

| Gate | Question | Required outcome |
|---|---|---|
| G1 Scientific justification | Can the choice be justified from the research objective, architecture, prior evidence, or standard RL practice? | PASS |
| G2 Validity / observability | Is the design causally valid and free of prohibited leakage or attribution ambiguity? | PASS |
| G3 Canonical AHBN protection | Does canonical AHBN remain unchanged and independently traceable? | PASS |
| G4 Minimal executable verification | Does at least one deterministic/micro-case or bounded implementation test confirm intended semantics? | PASS |

If all four gates pass:

> **FREEZE THE BLOCK. DO NOT CONTINUE SEARCHING FOR A BETTER DESIGN.**

---

# 6. Accelerated post-02.6 design blocks

The remaining design should be handled as a small number of coherent blocks rather than many isolated micro-decisions.

## Block A — State Representation Freeze

**Scope:**

- final logical RL state;
- permitted state inputs;
- discretization / encoding;
- state cardinality;
- local observability;
- cross-platform logical parity;
- missing/edge-case handling.

**Must verify:**

- no future information;
- no hidden global knowledge;
- canonical AHBN observations are not redefined;
- the same logical state contract can be represented in ControlSim and Kubernetes.

**Exit condition:**

```text
STATE REPRESENTATION = PASS / FROZEN
```

---

## Block B — Action Architecture Freeze

**Scope:**

- final Q-AHBN2 action set;
- exact action semantics;
- how each action refines the AHBN proposal;
- requested fanout/mode behavior;
- no-op/base behavior;
- topology/eligibility realization;
- safety/physical constraints;
- complete action logging.

**Must verify:**

- AHBN proposal is recorded before Q intervention;
- Q actions do not retroactively modify canonical AHBN;
- every retained action has a real, distinguishable effect where physically possible;
- no hidden deterministic rule is mislabeled as a learned action.

**Exit condition:**

```text
ACTION ARCHITECTURE = PASS / FROZEN
```

---

## Block C — Learning Configuration Freeze

**Scope:**

- Q-learning update equation;
- learning rate;
- discount factor;
- exploration strategy;
- epsilon start/end/decay or equivalent;
- Q initialization;
- tie handling;
- update timing;
- episode/update mechanics;
- any required deterministic seed handling.

**Acceleration rule:**

These parameters do not require proof of global optimality.

They require:

- clear rationale;
- bounded sanity checking;
- reproducibility;
- compatibility with the frozen architecture.

**Exit condition:**

```text
LEARNING CONFIGURATION = PASS / FROZEN
```

---

## Block D — Training and Evaluation Protocol Freeze

**Scope:**

- training versus evaluation separation;
- learning-validation procedure;
- seed policy;
- episode/run structure;
- stopping/stabilization rule;
- adaptation-efficiency measurement;
- formal comparison against frozen AHBN;
- ControlSim and Kubernetes role separation;
- output/logging requirements;
- pilot versus formal-run boundary;
- rerun/exclusion rules.

**Must preserve existing experiment families:**

- Exp10-Q — Failure;
- Exp11-Q — Churn;
- Exp12-Q — Heterogeneity;
- corresponding Kubernetes validation where already planned.

**Exit condition:**

```text
TRAINING / EVALUATION PROTOCOL = PASS / FROZEN
```

---

## Block E — Final End-to-End Design Audit

This is the final design gate before implementation/formal execution.

Audit the full chain:

```text
local observations
    ↓
canonical AHBN
    ↓
AHBN proposal
    ↓
Q-AHBN2 state
    ↓
Q action
    ↓
Q-AHBN2 requested decision
    ↓
eligible realization
    ↓
attributed outcomes
    ↓
reward
    ↓
Q update
    ↓
next state
```

Required checks:

- canonical AHBN unchanged;
- state/action/reward boundaries align;
- reward attribution aligns with the acting decision interval;
- no double counting beyond what the frozen reward contract explicitly permits;
- Q update receives the intended state/action/reward/next-state tuple;
- deterministic trace is interpretable;
- ControlSim contract is implementable;
- Kubernetes contract is logically compatible.

**Exit condition:**

```text
Q-AHBN2 COMPLETE DESIGN FREEZE = PASS / FROZEN
```

---

# 7. Hard stopping rule

For any post-02.6 question, ask:

> **Could leaving this unresolved invalidate the experiment or make Q-AHBN2 irreproducible?**

If **YES**:

- continue investigation until validity is established.

If **NO** and a conventional defensible choice exists:

- choose;
- document;
- minimally test;
- freeze;
- move on.

If the remaining question is essentially whether another parameter might produce better performance:

- classify as optimization;
- do not expand the design freeze.

---

# 8. Pilot rule

Pilots are permitted only when needed to establish that the design or implementation functions as intended.

Permitted pilot purposes include:

- confirming Q values actually update;
- verifying state transitions;
- confirming actions are executable;
- verifying reward computation;
- detecting dead actions;
- detecting impossible states;
- checking numerical stability;
- confirming logging completeness;
- detecting implementation defects;
- estimating whether the formal run configuration is operationally feasible.

Pilots MUST NOT be used as an open-ended search for settings that maximize superiority over AHBN.

A pilot result may trigger redesign only when it reveals:

1. a correctness defect;
2. a scientific-validity defect;
3. an unusable or non-executable design;
4. a contradiction with the frozen contract.

An unattractive performance result alone is not sufficient reason to redesign.

---

# 9. Formal-run lock

Once the final Q-AHBN2 design and experiment protocol are frozen and formal runs begin:

> **No post-hoc redesign is permitted because the results are weak, mixed, or below expectation.**

Formal results may show:

- improvement;
- small improvement;
- condition-dependent improvement;
- trade-offs;
- no material improvement;
- degradation.

All are scientifically admissible.

Changes after formal-run start require an explicit documented validity/correctness reason and must not be disguised as routine tuning.

---

# 10. Time box

**Plan start:** 2026-09-21

## Internal design-freeze target

Target complete Q-AHBN2 design freeze:

> **2026-09-25 to 2026-09-27**

This is a planning time box, not permission to accept a known invalid design.

Validity-critical defects remain blocking.

Ordinary design choices do not receive unlimited investigation time.

## Intended project trajectory

```text
21–27 Sep
Finish 02.6 + accelerated remaining design freeze
        ↓
late Sep / early Oct
Implementation + unit/regression/parity checks
        ↓
early Oct
Bounded learning-validation / diagnostic pilots
        ↓
early–mid Oct
Formal ControlSim Exp10-Q / Exp11-Q / Exp12-Q
        ↓
mid Oct
Kubernetes validation / formal experiments
        ↓
mid–late Oct
Analysis + figures + tables + interpretation
        ↓
25 Oct
Q-AHBN2 manuscript target
        ↓
31 Oct
Thesis first-draft target
```

The dates after design freeze are planning targets and may move if a genuine correctness issue is discovered, but fundamental architecture discussion should not continue indefinitely into October.

---

# 11. Progress tracker

This table is the operational progress reference for the accelerated plan.

| ID | Design / execution block | Status | Evidence / notes |
|---|---|---|---|
| P0 | Canonical AHBN contract | PASS / FROZEN | Existing authority; immutable |
| P1 | 02.1–02.4 Q-AHBN2 design | PASS / FROZEN | Existing detailed design assets |
| P2 | 02.5 Reward Signal Admissibility | PASS / FROZEN | Existing detailed design assets |
| P3 | 02.6 Reward Construction | IN PROGRESS | Continue current detailed process; do not compress or reopen |
| A | State Representation Freeze | BLOCKED BY P3 | Accelerated block begins after 02.6 |
| B | Action Architecture Freeze | BLOCKED | Accelerated block |
| C | Learning Configuration Freeze | BLOCKED | Accelerated block |
| D | Training / Evaluation Protocol Freeze | BLOCKED | Accelerated block |
| E | Final End-to-End Design Audit | BLOCKED | Final design gate |
| F | Complete Q-AHBN2 Design Freeze | BLOCKED | Target 2026-09-25 to 2026-09-27 |
| G | Implementation Verification | BLOCKED | Unit/regression/parity |
| H | Bounded Pilot / Learning Validation | BLOCKED | Correctness and feasibility only |
| I | Formal ControlSim Experiments | BLOCKED | Exp10-Q / Exp11-Q / Exp12-Q |
| J | Formal Kubernetes Validation | BLOCKED | Frozen protocol |
| K | Analysis / Interpretation | BLOCKED | Evidence-driven |
| L | Manuscript Completion | BLOCKED | Target 2026-10-25 |

---

# 12. Status vocabulary

Use only the following operational states unless a specific detailed design section requires additional scientific notation:

- `BLOCKED`
- `READY`
- `IN PROGRESS`
- `PASS / FROZEN`
- `FAIL — VALIDITY DEFECT`
- `SUPERSEDED BY EXPLICIT CHANGE CONTROL`

Do not use `PASS` for a design block until all mandatory gates have been satisfied.

---

# 13. Required update discipline

When a block is completed:

1. update its detailed authoritative section in `docs/02_QAHBN2_DESIGN_FREEZE.md` or the appropriate later contract;
2. update the corresponding row in this progress tracker;
3. record the supporting test/evidence reference where applicable;
4. do not reopen previous frozen blocks without an explicit defect/change-control reason;
5. continue immediately to the next READY block.

This file is a **control and progress document**.

It does not replace the detailed scientific design record.

---

# 14. Scientific interpretation rule

The research hypothesis may be that learning can improve adaptation over frozen AHBN.

The implementation and experiment process MUST remain outcome-neutral.

The design must not be tuned merely to manufacture a positive result.

The scientific contribution may ultimately be:

- improved adaptation;
- reduced overhead under particular conditions;
- faster stabilization;
- condition-dependent gains;
- evidence of limits of lightweight Q-learning over AHBN;
- or a combination of benefits and trade-offs.

The formal evidence determines the conclusion.

---

# 15. Current controlled action

As of 2026-09-21:

```text
CURRENT ACTIVE SCIENTIFIC TASK:
02.6 Reward Construction

PROCESS:
Continue the existing detailed controlled freeze.

DO NOT:
- compress 02.6;
- rewrite already frozen 02.5/02.6 assets;
- jump ahead into accelerated Block A prematurely.

NEXT PROCESS CHANGE:
After 02.6 = PASS / FROZEN,
activate Accelerated Block A — State Representation Freeze.
```

---

# 16. One-line operating rule

> **Protect validity aggressively; treat conventional choices efficiently; stop optimizing during design; freeze and execute.**
