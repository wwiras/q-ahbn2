# Q-AHBN2 Statistical Contract

**Status:** S07-B PASS / FORMAL ANALYSIS CONTRACT FROZEN
**Created:** 2026-09-23 under DOC-SYNC-1
**Formal statistical freeze:** 2026-09-28

## Purpose
Authoritative predeclared aggregation, uncertainty, comparison, exclusion, rerun, and interpretation rules for formal Q-AHBN2 Exp10-Q / Exp11-Q / Exp12-Q.

The AR-1.4.2 gamma sensitivity remains governed by its separately frozen bounded analysis and is not retroactively redefined here.

## 1. Unit of analysis and pairing

The formal experimental unit is one complete method x condition x seed run defined by `docs/03_EXPERIMENT_CONTRACT.md`.

For every condition, AHBN and Q-AHBN2 runs with the same seed form a paired comparison. The seed is the blocking/pairing factor because it controls the stochastic topology/event/resource assignment path. The five frozen seeds are:

```text
42, 43, 44, 45, 46
```

No run may be split into message-level pseudo-replicates for inferential comparison. Message-level/per-decision records are diagnostic/trace evidence within a run, not independent experimental replicates.

## 2. Required validation before aggregation

Before any scientific aggregation:

1. verify expected run count for the experiment;
2. verify every frozen method x condition x seed cell is present exactly once, except documented excluded/rerun provenance;
3. verify method labels, conditions, seeds, Git SHA/configuration and frozen learner parameters match the experiment contract;
4. verify required metrics are finite and within their logical domains;
5. verify no incomplete or corrupted run is silently included;
6. verify paired cells remain pairable after any validity exclusion/rerun;
7. retain original invalid/excluded evidence and its reason.

A dataset that fails completeness/validity is not interpreted until the defect is resolved under the frozen rerun rules.

## 3. Primary formal outcomes

The four primary dissemination outcomes are:

- delivery_ratio;
- propagation_delay;
- duplicates;
- total_forwards.

These outcomes jointly describe effectiveness, latency and communication overhead. No single metric is designated as an omnibus winner criterion.

For Q-AHBN2, required learning/adaptation evidence is descriptive/mechanistic rather than an additional family of superiority endpoints:

- reward-bearing Q-update count;
- mean reward;
- cumulative reward;
- state-action coverage;
- action distribution;
- AHBN proposal versus selected Q action;
- requested/refined versus realized fanout where available;
- mode/intervention traces.

No composite Adaptation Efficiency score is calculated.

## 4. Per-cell descriptive aggregation

For each experiment x condition x method x metric, report at minimum:

- n valid runs;
- arithmetic mean;
- sample standard deviation;
- 95% confidence interval for the mean.

Because n=5 is small, the 95% confidence interval for a method/condition mean uses the Student-t interval:

```text
mean +/- t_(0.975, n-1) * s / sqrt(n)
```

Do not substitute normal z=1.96 intervals for these five-run cell means.

For count outcomes (duplicates, total_forwards), the same across-seed summary is used. No Poisson assumption is imposed because the experimental replicate is the complete seeded run rather than an independent event count.

## 5. Paired AHBN versus Q-AHBN2 comparison

For each experiment x condition x primary metric:

1. compute the paired seed difference
   `Delta_i = QAHBN2_i - AHBN_i`;
2. report mean paired difference `mean(Delta)`;
3. report its sample standard deviation;
4. report a two-sided 95% Student-t confidence interval for the mean paired difference using df=n-1;
5. report the five individual paired differences or an equivalent machine-readable table so consistency across seeds is auditable.

Direction must be interpreted by metric:

- delivery_ratio: positive Delta means higher Q-AHBN2 delivery;
- propagation_delay: negative Delta means lower Q-AHBN2 delay;
- duplicates: negative Delta means fewer Q-AHBN2 duplicates;
- total_forwards: negative Delta means fewer Q-AHBN2 forwards.

The sign convention must remain explicit; do not transform all outcomes into a hidden normalized score.

## 6. Relative effect reporting

Where the AHBN reference mean is non-zero and the ratio is scientifically meaningful, a relative change may be reported as a secondary descriptive effect:

```text
100 * (mean_QAHBN2 - mean_AHBN) / mean_AHBN
```

Relative change never replaces the absolute paired difference/CI and must not be used when the denominator is zero or near-zero in a way that makes the ratio unstable or misleading.

Delivery ratio should additionally be expressed in absolute percentage-point difference where useful.

## 7. Hypothesis-test boundary

The primary formal evidence is effect magnitude plus uncertainty from the paired design. Null-hypothesis significance testing is not required to answer the Q-AHBN2 research question and is not the primary decision rule.

Accordingly:

- no binary `p < 0.05 => success` rule is used;
- no formal experiment PASS/FAIL is determined by statistical significance;
- no post-hoc search across alternative tests is permitted;
- confidence intervals that include zero are reported as uncertainty compatible with no mean difference under the tested condition, not as proof of equivalence;
- confidence intervals that exclude zero may be described as a directionally consistent estimated mean effect under the frozen five-seed design, without claiming universal superiority.

If a manuscript later reports an inferential p-value for a paired comparison, it must be generated reproducibly from the frozen paired differences using a two-sided paired t-test and must be treated as supplementary to effect size/CI, not as the scientific selection rule.

## 8. Multiple outcomes and multiplicity boundary

The four primary metrics are predeclared and represent distinct scientific dimensions of the dissemination trade-off. The three scenario families and their condition levels are also predeclared.

No multiplicity correction is required for the primary descriptive effect-size/95%-CI reporting because the analysis does not use a family of p-values to declare an omnibus winner.

If supplementary p-values are reported, they must not be mined for isolated significance. Any p-value family used for a strong confirmatory claim across multiple metric/condition comparisons must apply Holm correction within the explicitly stated family. Unadjusted exploratory/supplementary p-values must be labelled as such.

## 9. Condition-level versus cross-condition interpretation

Each frozen disturbance/resource level is first interpreted separately.

Cross-condition summaries may be used only to describe patterns such as whether effects strengthen, weaken or change sign with disturbance severity. Do not pool unlike conditions into one overall AHBN-vs-Q-AHBN2 effect unless a later explicitly frozen model justifies that pooling.

No new regression, ANOVA, mixed model, composite score or severity weighting is introduced merely because the observed pattern is complicated.

## 10. Formal scenario interpretation

### Exp10-Q Failure
Report the control and one-failure cells separately. The failure condition is the principal dynamic cell; the zero-failure cell is the contemporaneous harness control.

Where message-index/event traces support it, pre-/post-failure behavior may be shown descriptively. Such within-run segments are not independent replicates and do not change n=5 for the formal paired comparison.

### Exp11-Q Churn
Report 0.00, 0.20 and 0.40 separately. Interpret monotonic/non-monotonic trends descriptively from the frozen levels; do not fit an additional dose-response model unless separately authorized before seeing results.

### Exp12-Q Heterogeneity
Report balanced, moderate_heterogeneity and weak_heavy separately. Resource profile is a fixed scenario condition, not a learned/tuned variable.

## 11. Learning/adaptation evidence

For Q-AHBN2, summarize reward, update, coverage and action/intervention evidence by condition using the same five seeded runs.

Required minimum reporting:

- mean and 95% t-CI for mean_reward and cumulative_reward where defined;
- Q-update count summary;
- state-action coverage summary;
- action distribution aggregated as counts/proportions with per-seed values retained;
- proportion/count of KEEP versus intervention actions;
- fanout-up/down and mode-setting action usage;
- AHBN proposal versus Q decision and realized-action traces sufficient to explain observed dissemination differences.

The previously frozen Learning Validation reward-stability diagnostic is not automatically a required formal endpoint. It may be retained if already emitted unchanged by the harness, but it cannot be relabelled as convergence or Adaptation Efficiency and cannot be tuned or used to terminate runs.

## 12. Missing data, exclusions and reruns

Only validity defects listed in the experiment contract justify exclusion/rerun.

Rules:

- never delete an invalid original run;
- record its status and reason;
- rerun the same frozen method/condition/seed, not a replacement seed;
- if a shared scenario-generation/configuration defect invalidates one member of a pair, rerun the full pair for that seed/condition;
- if only one process/run artifact is invalid and the paired counterpart is demonstrably unaffected, the invalid member may be rerun alone, but pair identity remains the original seed;
- scientific performance is never a validity defect;
- exclusions are reported in the final run-accounting table.

No imputation is permitted for a missing formal run.

## 13. Outliers

No run is excluded solely because a metric is extreme relative to the other seeds.

An extreme value may be excluded only when an independently documented validity defect explains it. Otherwise it remains part of the five-seed evidence and is discussed as observed variability.

No winsorization, trimming or post-hoc robust replacement is permitted.

## 14. Precision and reproducibility

Machine-readable analysis must retain full stored precision. Tables may round:

- delivery ratios to at least 3 decimal places or 0.1 percentage point;
- delay to at least 3 decimal places;
- count means/effects to at least 1 decimal place where averaging creates fractions;
- CI bounds consistently with the corresponding estimate.

Figures/tables must be generated from preserved raw/validated data by reproducible analysis code. Manual transcription is not the authoritative calculation path.

## 15. Scientific decision boundary

Formal experiment execution validity and scientific outcome are separate.

A formal dataset may be:

- complete/valid with improvement;
- complete/valid with trade-offs;
- complete/valid with approximate/no clear difference;
- complete/valid with degradation.

All are scientifically admissible outcomes.

Do not rank conditions or methods by an undisclosed composite. Do not select only favorable metrics, seeds or scenario levels.

Claims must state:

1. condition;
2. metric;
3. absolute effect;
4. 95% CI;
5. consistency/variation across the five paired seeds;
6. relevant learning/intervention evidence;
7. limitation/boundary.

## 16. Dataset freeze

After S08, S09 and S10 each complete their frozen matrices and pass run validity/completeness verification, their raw formal evidence is frozen.

S11 aggregation must consume only the frozen valid datasets plus retained exclusion/rerun provenance. No new formal condition, seed, metric definition, model-selection step or hyperparameter change may be introduced at S11.

## 17. S07-B freeze decision

`S07-B — Formal Statistical Contract Freeze = PASS / FROZEN`.

This statistical contract was frozen before viewing formal Exp10-Q/Exp11-Q/Exp12-Q outcomes.

Next controlled gate: `S07-C — Final Completeness Re-Audit`.
