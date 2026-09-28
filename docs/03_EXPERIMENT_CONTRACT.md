# Q-AHBN2 Experiment Contract

**Status:** S07-A PASS / FORMAL CONTROLSIM MATRICES FROZEN
**Created:** 2026-09-23 under DOC-SYNC-1
**Formal matrix freeze:** 2026-09-28

## Purpose
Authoritative home for the controlled experimental protocols that follow design/development/validation closure.

## 1. Formal comparison boundary

The principal formal comparison is:

```text
Frozen canonical AHBN
        vs
Q-AHBN2
```

No Gossip, Structured, DC-SoC, legacy Q-AHBN, or other additional comparator is required in the Q-AHBN2 formal matrix. Their role is already established in RO2/AHBN evidence; adding them here would expand workload without being necessary to answer whether learning-based bounded refinement improves or changes the frozen AHBN baseline.

Canonical AHBN is immutable. Q-AHBN2 uses the frozen learning contract:

- tabular Q-learning;
- 81 states;
- actions: KEEP, FANOUT_DOWN, FANOUT_UP, SET_GOSSIP, SET_STRUCTURED;
- reward: R = (NEW - DUPLICATE - FAILED) / F;
- F = 0 -> no Q update;
- alpha_Q = 0.25;
- gamma = 0.70;
- epsilon_0 = 0.30;
- epsilon_min = 0.03;
- epsilon_decay = 0.995;
- same-peer next-decision transition semantics.

Each formal run starts from a fresh learner/Q-table/controller state and preserves learner state within that run. AHBN baseline runs execute the same scenario without Q-learning.

## 2. Shared ControlSim protocol

Unless an experiment section overrides a field, all three formal ControlSim families use:

| Field | Frozen value |
|---|---|
| topology | BA preferential-attachment graph |
| N | 100 peers |
| BA parameter | m=3 |
| source | peer 0 |
| base one-hop delay | 1.0 |
| jitter | 0.2 |
| structured partition | four static clusters |
| seeds | 42, 43, 44, 45, 46 |
| repetitions | one run per seed/method/condition |
| methods | AHBN, Q-AHBN2 |
| workload | 1,000 sequential messages per run, queue-to-exhaustion between injections |
| reset rule | fresh topology/runtime/learner state for every run; no cross-run learning |
| common-randomness rule | the same seed is paired across AHBN and Q-AHBN2 for the same condition |
| execution order | by seed: AHBN then Q-AHBN2 for each condition; each run is process/reset independent |
| canonical AHBN | frozen S5 controller and realization semantics |
| output event | formal |

### Scientific basis

BA(100,m=3), source 0, base_delay=1.0, jitter=0.2, four static clusters, seeds 42--46, and sequential 1,000-message execution reuse the already frozen Q-AHBN2 Learning Validation / canonical RO2-AHBN ControlSim reference rather than adding new topology or arrival-rate degrees of freedom. Five paired seeds retain the established bounded replication design while avoiding unnecessary within-seed duplicate repetitions.

The dynamic families are deliberately limited to failure, churn, and heterogeneity because RO2 identified these as distinct threats to static dissemination and the Q-AHBN2 master contract identifies them as the minimum expected RO4 dynamic scope.

## 3. Required formal outputs and metrics

Every formal run must preserve raw per-message/per-decision data sufficient to reconstruct the aggregate result and Q-AHBN2 intervention history.

Required dissemination outcomes:

- delivery_ratio;
- propagation_delay;
- duplicates;
- total_forwards.

Required learning/adaptation evidence for Q-AHBN2:

- reward-bearing Q-update count;
- mean reward;
- cumulative reward;
- state-action coverage;
- action distribution;
- AHBN proposal versus Q-AHBN2 selected action;
- requested/refined fanout versus realized fanout where applicable;
- mode/intervention trace over the run.

Where the scenario has an explicit disturbance onset/recovery event, the run must also preserve event timing and enough message-index/time information to describe post-event response without inventing a new composite score.

### Adaptation-efficiency boundary

No new metric named `Adaptation Efficiency` is introduced. The master/design contracts explicitly prohibit treating the earlier bounded reward-stability diagnostic as a composite adaptation-efficiency score. Formal adaptation behaviour is therefore reported through pre-existing reward, Q-update, coverage/action, controller/intervention, and dissemination traces.

## 4. Exp10-Q — Failure

### Research question
Under node loss, does Q-AHBN2's learned bounded refinement change dissemination effectiveness/overhead relative to frozen AHBN while preserving the canonical controller boundary?

### Frozen matrix

| Field | Value |
|---|---|
| topology/workload | shared protocol |
| failure type | transient peer unavailability during the run |
| failure target | one non-source peer selected deterministically from the run seed |
| cluster-head eligibility | permitted; no protected class other than the source |
| disturbance levels | 0 failed peers (control), 1 failed peer |
| failure onset | immediately before message 501 |
| recovery | no recovery within the 1,000-message run |
| methods | AHBN, Q-AHBN2 |
| seeds | 42--46 |
| total formal runs | 2 levels x 2 methods x 5 seeds = 20 |

### Rationale
RO2/AHBN evidence establishes failure as a separate dynamic stressor and structured-path fragility mechanism. A single-peer failure is the minimum non-zero perturbation and avoids conflating failure count with a new severity sweep. The zero-failure cell supplies an internal contemporaneous control under the identical formal harness; it is not a new scenario family.

## 5. Exp11-Q — Churn

### Research question
Under repeated membership instability, does Q-AHBN2 alter the dissemination trade-off relative to frozen AHBN?

### Frozen matrix

| Field | Value |
|---|---|
| topology/workload | shared protocol |
| churn type | leave/rejoin cycles; temporary unavailability |
| churn levels | 0.00, 0.20, 0.40 target fraction |
| churn events | four cycles |
| cycle onsets | before messages 201, 401, 601, 801 |
| rejoin point | after 50 subsequent messages within each cycle |
| target selection | deterministic from the run seed; same target set schedule for paired methods |
| cluster-head eligibility | permitted |
| methods | AHBN, Q-AHBN2 |
| seeds | 42--46 |
| total formal runs | 3 levels x 2 methods x 5 seeds = 30 |

### Rationale
RO2 already characterized churn over 0--0.40 and showed increasing instability as scientifically relevant. Retaining only 0, 0.20, and 0.40 captures baseline, intermediate, and high evaluated churn without repeating the full historical sweep. Four repeated cycles ensure churn is a sustained within-run condition rather than a one-off failure.

## 6. Exp12-Q — Heterogeneity

### Research question
Under heterogeneous peer processing capacity, does Q-AHBN2 alter dissemination effectiveness/overhead relative to frozen AHBN?

### Frozen matrix

The resource classes reuse the established AHBN ControlSim semantics:

| Class | processing_delay | capacity_score |
|---|---:|---:|
| strong | 0.15 | 1.80 |
| medium | 0.50 | 1.00 |
| weak | 1.00 | 0.55 |

Profiles:

| Profile | strong | medium | weak |
|---|---:|---:|---:|
| balanced | 0.25 | 0.50 | 0.25 |
| moderate_heterogeneity | 0.20 | 0.45 | 0.35 |
| weak_heavy | 0.15 | 0.35 | 0.50 |

Other fields:

| Field | Value |
|---|---|
| topology/workload | shared protocol |
| resource assignment | deterministic from the run seed; identical paired assignment for AHBN/Q-AHBN2 |
| failure/churn | disabled |
| methods | AHBN, Q-AHBN2 |
| seeds | 42--46 |
| total formal runs | 3 profiles x 2 methods x 5 seeds = 30 |

### Rationale
These three profiles are an existing AHBN ControlSim precedent and directly vary forwarding capacity/processing delay without adding a novel heterogeneity model. All three are retained because the balanced profile is the scenario control, while moderate and weak-heavy profiles provide two pre-existing non-zero severity levels.

## 7. Frozen formal ControlSim workload

Expected total formal ControlSim execution:

```text
Exp10-Q: 20 runs
Exp11-Q: 30 runs
Exp12-Q: 30 runs
-------------------
Total:   80 runs
```

This is the complete formal ControlSim matrix. No additional seed, repetition, severity level, baseline, or scenario may be added because observed results appear weak or visually incomplete.

## 8. Execution order and independence

The required execution order is:

```text
Exp10-Q -> Exp11-Q -> Exp12-Q
```

Within each experiment, execute conditions in the order written above. Within each seed/condition pair, execute AHBN then Q-AHBN2.

Execution order is an operational reproducibility rule, not a scientific carry-over rule: every run must initialize independently, and Q-tables, AHBN states, counters, event queues, topology mutation state, and random generators must be initialized from the run configuration/seed. No Q-table is transferred between formal runs or between experiments.

## 9. Provenance and output requirements

Simulation directory:

```text
q-ahbn-<DDMMYYYYHHmmss>-<experiment>-formal/
```

Every preserved experiment directory must include at minimum:

```text
RUN.md
manifest.json
```

and machine-readable raw/summary output containing:

- producing Git commit SHA;
- experiment and condition;
- method;
- seed;
- exact topology/workload/disturbance configuration;
- frozen learning parameters for Q-AHBN2;
- expected/completed run counts;
- execution start/end status;
- metric definitions/fields;
- exclusion/rerun status;
- software/environment identifiers needed for reproducibility.

Formal evidence is promoted to the designated Google Drive evidence hierarchy only after completeness and validity verification. Automatic Drive synchronization is not evidence promotion.

## 10. Protocol exclusions and reruns

A formal run may be excluded/rerun only for a documented validity defect:

- implementation defect;
- configuration mismatch;
- corrupted or unreadable output;
- incomplete/aborted execution;
- methodological inconsistency with this frozen contract;
- infrastructure/runtime failure that invalidates the run.

Poor performance, an unexpected scientific result, low delivery, high duplication, undesirable reward, or disagreement with expectations is not a rerun reason.

If a paired AHBN/Q-AHBN2 run is invalidated by a shared seed/condition defect, the corresponding pair is rerun from the same frozen configuration so paired comparison remains intact. Original failed/excluded artifacts are retained and classified; they are not deleted or overwritten.

## 11. ControlSim versus Kubernetes boundary

S08--S10 formal experiments are the primary controlled-simulation evidence for the Q-AHBN2 research question.

Later Kubernetes work is a deployment-validation layer, not an extension of the ControlSim matrix and not a new parameter-search phase. Kubernetes validation must:

- compare frozen AHBN with frozen Q-AHBN2 only;
- reuse the closest already established AHBN Kubernetes failure/churn/heterogeneity conditions where implementation-compatible;
- preserve environment-specific sensing/normalization while maintaining the same logical Q-AHBN2 state/action/reward contract;
- not retune Q-learning parameters, AHBN, disturbance severity, or metrics based on ControlSim results;
- be frozen in a separate later gate before execution.

ControlSim results therefore cannot be used to choose favourable Kubernetes conditions.

## 12. S07-A freeze decision

`S07-A — Formal Experiment Matrix Freeze = PASS / FROZEN`.

The formal matrices above are prospective. No formal Exp10-Q/Exp11-Q/Exp12-Q result was inspected or used to choose them.

No formal execution is authorized until S07-B freezes the statistical contract and S07-C returns S07 PASS.

## Project-wide test execution and evidence standard

All Q-AHBN2 executable tests inherit the GitHub-first controlled-gate workflow and operational authority frozen in `docs/00_QAHBN2_MASTER.md` and `docs/00_SOURCE_AUTHORITY_REGISTER.md`.

The designated local workspace is:

`/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`

The designated Google Drive evidence root is folder ID:

`1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`

> **Audit every gate; edit only files whose authoritative state actually changed.**

No test PASS, stage transition, or formal evidence claim may be declared solely from assistant narration, command completion, or automatic Drive synchronization. Artifact verification and the required GitHub readback must occur first.
