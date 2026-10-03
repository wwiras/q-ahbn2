# S12A — Thesis–Paper Claim Reconciliation

**Status:** PASS / CLOSED — 2026-09-29

## Objective
Convert the frozen S12 interpretation into an explicit claim authorization contract for:
1. PhD thesis Chapter 6 / RO4-RQ4; and
2. the standalone Q-AHBN2 paper.

This gate changes claim authorization only. It does not reopen experiments, parameters, algorithms, statistical procedures, metrics, or evidence.

## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md`
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`
- `docs/01_CANONICAL_AHBN_CONTRACT.md`
- `docs/02_QAHBN2_DESIGN_FREEZE.md`
- `docs/03_EXPERIMENT_CONTRACT.md`
- `docs/04_STATISTICAL_CONTRACT.md`
- `docs/05_REVIEWER_LESSONS.md`
- `docs/06_RESULTS_REGISTER.md`
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`
- `docs/stages/S11_AGGREGATION.md`
- `docs/stages/K6_Q_K8S_EVIDENCE_FREEZE.md`
- `docs/stages/S12_INTERPRETATION.md`

Frozen evidence roles remain:
- Exp10-Q / Exp11-Q / Exp12-Q: primary RO4/RQ4 ControlSim evidence;
- Exp13-Q: bounded external-reference positioning at churn=0.40 only;
- K8s-VAL-Q / Exp13-Q-K8s: operational realization / cloud-native deployment credibility;
- learning traces: mechanism evidence only, not convergence or optimality evidence.

## Claim authorization contract

| Claim ID | Scientific claim | Evidence | Scope/condition | Permitted thesis wording | Permitted paper wording | Prohibited wording / overclaim | Status |
|---|---|---|---|---|---|---|---|
| C01 | Q-AHBN2 is a bounded Q-learning meta-controller that operates after, and refines the proposal of, immutable canonical AHBN. | Canonical AHBN contract; Q-AHBN2 design freeze; implementation/parity closure. | Architectural/design claim; both platforms at the logical-contract level. | “Q-AHBN2 extends the frozen AHBN architecture with a bounded post-AHBN learning layer that refines AHBN’s proposed dissemination action.” | “We introduce Q-AHBN2, a bounded Q-learning meta-controller layered above immutable AHBN.” | “Q-AHBN2 replaces/redesigns AHBN”; “AHBN parameters were learned/retuned”; “Q-AHBN2 changes the canonical AHBN controller.” | SUPPORTED |
| C02 | The learning layer is active and outcome-driven: frozen traces contain repeated Q updates, non-zero state-action coverage, interventions, and condition-dependent behavior. | S12 learning-mechanism interpretation; frozen Learning Validation/formal traces. | Mechanistic evidence under tested workloads only. | “The recorded traces demonstrate active outcome-driven refinement, with repeated Q updates, interventions, and condition-dependent state/action use.” | “Learning traces confirm active Q updates and bounded interventions above AHBN.” | “The learner converged”; “the learned policy is optimal”; “negative mean reward proves failure”; “coverage proves convergence.” | SUPPORTED-CONDITIONALLY |
| C03 | Under the frozen Exp10-Q one-peer failure condition, Q-AHBN2 has higher mean delivery and lower mean propagation delay than AHBN, while using more duplicates and forwards. | S11-A/S12: delivery Δ=+0.129066; delay Δ=-5.832377; duplicate Δ=+28,798.0; forward Δ=+41,704.6; n=5 paired seeds; delivery/delay 95% CIs exclude zero. | Exp10-Q failure only. | “Under the tested one-peer failure condition, Q-AHBN2 improved delivery and propagation delay relative to AHBN, at the cost of higher communication overhead.” | “For the predeclared failure condition, Q-AHBN2 increased delivery and reduced propagation delay versus AHBN, with higher duplicate and forwarding overhead.” | “Q-AHBN2 is superior under failures”; “failure robustness is universally solved”; any wording hiding the overhead cost. | SUPPORTED |
| C04 | Across Exp11-Q churn 0.00, 0.20 and 0.40, Q-AHBN2 has higher mean delivery and lower mean propagation delay than AHBN, with effect magnitude decreasing for delivery as churn rises. | S12: delivery Δ +0.133472, +0.062944, +0.023040; delay Δ -5.977232, -3.765746, -1.198793; all delivery/delay paired 95% CIs exclude zero. | Frozen churn levels only; n=5 per condition. | “Across the tested churn levels, Q-AHBN2 improved delivery and delay relative to AHBN; the delivery gain decreased descriptively as churn increased.” | “Q-AHBN2 retained a delivery/latency advantage over AHBN across the three predeclared churn levels, although the delivery effect attenuated with increasing churn.” | “Performance degrades monotonically according to a proven dose-response”; “Q-AHBN2 is churn-proof”; “robust for all churn rates.” | SUPPORTED |
| C05 | Across the three Exp12-Q heterogeneity profiles, Q-AHBN2 has higher mean delivery and lower mean propagation delay than AHBN, with higher duplicates and forwards. | S12: balanced Δdelivery +0.093462, Δdelay -6.875323; moderate +0.057428, -6.541088; weak-heavy +0.058072, -7.813670; all delivery/delay paired 95% CIs exclude zero. | Frozen balanced/moderate/weak-heavy profiles only; n=5 each. | “Under all three tested heterogeneity profiles, Q-AHBN2 improved delivery and propagation delay relative to AHBN, while increasing communication overhead.” | “The learned refinement improved delivery and delay across the predeclared heterogeneity profiles, with an explicit duplicate/forwarding cost.” | “Q-AHBN2 solves heterogeneity”; “heterogeneity-independent superiority”; “lower overhead under heterogeneity.” | SUPPORTED |
| C06 | Across all eight primary ControlSim conditions, Q-AHBN2 consistently shifts AHBN toward higher delivery and lower propagation delay; this is a delivery–latency improvement with communication-overhead trade-off, not across-the-board dominance. | S11-A 80 runs / 40 paired comparisons; S12 eight-condition synthesis; all delivery/delay paired 95% CIs exclude zero; duplicates/forwards means higher in all eight. | Exp10-Q/11-Q/12-Q only; tested conditions; n=5 per cell. | “Across the eight tested ControlSim conditions, Q-AHBN2 consistently improved the delivery–latency trade-off relative to AHBN, while generally increasing duplicate traffic and forwarding effort.” | “Across all eight predeclared ControlSim conditions, Q-AHBN2 produced higher delivery and lower delay than AHBN, with a consistent communication-overhead trade-off.” | “universally superior”; “best”; “dominates AHBN”; “improves all metrics”; pooled overall effect across unlike conditions. | SUPPORTED |
| C07 | Exp13-Q positions Q-AHBN2 relative to Gossip, Structured, DC-SoC and AHBN at one frozen churn=0.40 benchmark; Q-AHBN2 improves AHBN delivery/delay there but does not dominate the external references across all metrics. | S11-B/S12 five-method means at churn=0.40. | One ControlSim benchmark; five seeds; external positioning only. | “The Exp13-Q benchmark places Q-AHBN2 within the established dissemination trade-off at churn=0.40; it improves AHBN delivery/delay but does not dominate all external baselines across the four metrics.” | “At the single predeclared churn=0.40 benchmark, Q-AHBN2 improves over AHBN on delivery and delay but remains a trade-off point rather than an across-metric winner.” | Any omnibus ranking/winner; “Q-AHBN2 outperforms Gossip/Structured/DC-SoC overall”; “Exp13 proves general superiority.” | SUPPORTED-CONDITIONALLY |
| C08 | Kubernetes evidence demonstrates executable distributed realization, Q-AHBN2 observability, and successful operation in the frozen cloud-native protocol. | K6-Q 25/25 validated coordinates; frozen image/digest/provenance; S12 Kubernetes interpretation. | Frozen Kubernetes matrix only. | “Kubernetes validation demonstrates that the frozen Q-AHBN2 learning contract can be realized and observed in a distributed cloud-native deployment.” | “The Kubernetes campaign provides deployment credibility by demonstrating executable distributed realization and traceable learning behavior.” | “Kubernetes independently proves Q-AHBN2 performance superiority”; “Kubernetes replicates the ControlSim gains”; “cloud deployment improves performance.” | SUPPORTED |
| C09 | Kubernetes does not independently establish a consistent Q-AHBN2 performance advantage over AHBN: all five corrected paired 95% CIs cross zero and seed-level directions vary. | S12 Kubernetes paired differences and CIs. | Frozen Kubernetes benchmark; n=5 pairs. | “The Kubernetes results should be interpreted as operational-realization evidence rather than an independent performance-improvement result.” | “Because all five corrected paired intervals cross zero and seed-level effects vary, Kubernetes is used as deployment validation rather than confirmatory performance evidence.” | “Kubernetes validates the same performance improvement”; “the Kubernetes experiment confirms superiority.” | SUPPORTED |
| C10 | ControlSim and Kubernetes are complementary evidence families and must not be pooled or described as literal replication. | Experiment/statistical contracts; K6; S12. | Cross-environment interpretation. | “ControlSim provides the primary controlled performance evidence, while Kubernetes provides complementary operational-realization evidence; the environments are not statistically pooled.” | “The two environments serve complementary evidentiary roles and are not treated as literal replications or pooled samples.” | “replicated exactly on Kubernetes”; “cross-environment equivalence”; pooled CI/effect; direct quantitative equivalence without a frozen equivalence model. | SUPPORTED |
| C11 | RO4/RQ4 contribution: bounded experience-based refinement of frozen AHBN can improve delivery and propagation delay under the tested dynamic ControlSim conditions, but the benefit is condition-dependent and generally incurs higher communication overhead. | C01–C06 plus learning evidence. | Thesis RO4/RQ4; tested failure/churn/heterogeneity conditions. | “RO4 demonstrates that a bounded Q-learning layer can refine AHBN’s adaptive decisions to improve delivery and propagation delay under the evaluated dynamic conditions, while exposing a condition-dependent communication-overhead trade-off.” | n/a except as background framing. | “RO4 proves Q-learning is universally better than AHBN”; “optimal adaptive dissemination”; “all metrics improve.” | SUPPORTED |
| C12 | Paper contribution: Q-AHBN2 is a bounded learning refinement over AHBN, evaluated with primary paired ControlSim experiments, a bounded external benchmark, and complementary Kubernetes realization evidence. | Frozen design + S11/S12 + K6. | Standalone Q-AHBN2 paper contribution framing. | n/a except when summarizing publication contribution. | “The paper contributes a bounded Q-learning refinement of AHBN, evaluates its delivery–latency/overhead trade-off across predeclared dynamic conditions, positions it against established dissemination baselines, and demonstrates cloud-native operational realization.” | “state-of-the-art”; “best method”; “universally superior”; “Kubernetes confirms simulation performance”; “lightweight deployment benefit” unless specifically qualified as architectural/decentralized design rather than measured cost. | SUPPORTED |
| C13 | The study has important limitations: n=5 per cell; effect estimates are condition-specific; no convergence/policy-optimality experiment; no omnibus ranking; no cross-environment pooling/equivalence; Kubernetes performance effects are uncertain; reward/coverage evidence is mechanistic. | Statistical contract; S12 limitations. | Entire study. | “Results are bounded by five seeded repetitions per cell and the tested scenario families; learning traces establish active adaptation rather than convergence or optimality, and Kubernetes is interpreted as operational realization rather than performance replication.” | Same, compacted for manuscript limitations. | Omitting n=5 when presenting CI-based claims; implying inferential breadth beyond tested conditions; hiding Kubernetes uncertainty. | SUPPORTED |
| C14 | A generic “lightweight/low-overhead” performance claim is not supported by the frozen evidence. | S17/S18 corrected Kubernetes accounting: Q-AHBN2 mean F_attempt 2251.0 and successful forwards 1612.2 vs AHBN 1448.0 and 998.6; ControlSim duplicates/forwards generally higher. | Performance/resource-overhead claim. | “The architecture is decentralized and bounded, but the experiments do not establish a generic low-overhead performance benefit.” | “We do not claim generic low communication or forwarding overhead.” | “Q-AHBN2 is lightweight because it sends less”; “lower network overhead”; “resource-efficient” unless a separately measured supported quantity is named and bounded. | NOT SUPPORTED |
| C15 | Q-learning convergence, policy optimality, global hyperparameter optimality, universal superiority, and best-method claims are unsupported. | Design freeze; statistical contract; S12; reviewer lessons. | Entire project. | Explicitly state these are outside the evidence. | Explicitly state these are not claimed. | “converged”, “optimal”, “best”, “state-of-the-art superiority”, “universally superior”, “dominates”. | PROHIBITED |

## Thesis Chapter 6 / RO4-RQ4 authorized synthesis

The strongest evidence-bounded thesis synthesis is:

> Q-AHBN2 adds a bounded, outcome-driven Q-learning refinement layer above immutable canonical AHBN. Across the eight predeclared ControlSim failure, churn and heterogeneity conditions, the learned refinement produced higher mean delivery and lower mean propagation delay than AHBN, with paired 95% confidence intervals for these two outcomes excluding zero in every condition. These gains were condition-dependent and generally accompanied by higher duplicate traffic and forwarding effort. The external Exp13-Q benchmark positions Q-AHBN2 within, rather than above, the wider dissemination trade-off, while Kubernetes demonstrates operational realization without independently establishing a consistent performance advantage.

This wording is authorized for Chapter 6/RO4-RQ4 subject to exact numerical values and figure/table references being taken from frozen artifacts.

## Q-AHBN2 paper authorized contribution synthesis

The strongest evidence-bounded paper synthesis is:

> Q-AHBN2 is a bounded Q-learning meta-controller that refines, rather than replaces, canonical AHBN. Its primary paired ControlSim evaluation shows a consistent delivery/latency improvement over AHBN across the tested failure, churn and heterogeneity conditions, with an explicit communication-overhead trade-off. A prospectively frozen five-method reference benchmark provides bounded external positioning, and Kubernetes validation demonstrates executable cloud-native realization. The study does not claim convergence, policy optimality, universal superiority, cross-environment equivalence, or generic low-overhead behavior.

## Explicit prohibited claims

The following wording classes are prohibited unless a future formally authorized evidence gate reopens them:
- “best”, “optimal”, “globally optimal”, “converged”, “state-of-the-art superior”;
- “universally superior”, “dominates”, “improves all metrics”;
- “robust to any failure/churn/heterogeneity” or equivalent extrapolation beyond tested conditions;
- “Kubernetes replicates/confirms the ControlSim performance gains”;
- statistical pooling of ControlSim and Kubernetes;
- an omnibus Exp13-Q winner/ranking claim;
- generic “lightweight”, “low-overhead”, “resource-efficient”, or “reduced forwarding” performance claims unsupported by a specifically named measured quantity;
- any statement that Q-AHBN2 redesigns canonical AHBN or learns/retunes AHBN’s frozen parameters.

## Limitations that must remain visible
- n=5 per condition/cell for the formal paired comparisons;
- Student-t 95% CIs describe uncertainty under the frozen five-seed design and do not imply universality;
- condition-specific effect magnitudes;
- communication-overhead cost in ControlSim;
- no convergence or policy-optimality experiment;
- Exp13-Q is one bounded churn=0.40 benchmark and remains separate from core RO4 causal evidence;
- Kubernetes performance contrasts are uncertain and serve deployment/operational realization rather than independent confirmatory superiority;
- ControlSim and Kubernetes are not pooled and are not literal replications.

## Verification / decision
All required S12A claim classes are traceable to already frozen design, aggregation, statistical, interpretation, and Kubernetes evidence. No new experiment, statistic, metric, hypothesis, ranking or post-hoc analysis is required.

**Result: PASS / CLOSED.**

## Next permitted action
Per the frozen stage map, the next permitted paper gate is:

**S13 — Q-AHBN2 Manuscript**

The separate thesis mapping gate remains **S13-T — Chapter 6 Mapping** at its position in the master sequence. S13 drafting must use this S12A claim contract as an authorization boundary.


## S18 post-remediation reconciliation — 2026-10-03
The S17 forwarding-accounting repair changes the numerical Kubernetes evidence attached to C08/C09/C14, but does not change their scientific authorization status or the overall claim boundary. C09 is now governed by five corrected paired metrics, all with 95% CIs crossing zero. C14 remains NOT SUPPORTED: corrected accounting does not authorize a generic low-overhead or reduced-forwarding claim. All other S12A claims remain unchanged.
