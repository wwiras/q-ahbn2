# Q-AHBN2 Claim–Evidence Matrix

**Status:** ACTIVE — S12A CLAIM CONTRACT FROZEN / 2026-09-29
**Created:** 2026-09-23 under DOC-SYNC-1

## Governing rule
Every major thesis/paper claim must remain traceable to frozen evidence, scope, uncertainty and limitations. S12A is the authoritative wording boundary. Stronger wording is not permitted merely because it is rhetorically convenient.

## S12A final claim contract — 2026-09-29

| Claim ID | Scientific claim | Evidence | Scope/condition | Permitted thesis wording | Permitted paper wording | Prohibited wording / overclaim | Status |
|---|---|---|---|---|---|---|---|
| C01 | Q-AHBN2 is a bounded post-AHBN Q-learning meta-controller; canonical AHBN remains immutable. | `01_CANONICAL_AHBN_CONTRACT.md`; `02_QAHBN2_DESIGN_FREEZE.md` | Architecture | Q-AHBN2 extends frozen AHBN with a bounded learning layer that refines the AHBN proposal. | Q-AHBN2 is a bounded Q-learning meta-controller layered above immutable AHBN. | replacement/redesign/retuning of AHBN | SUPPORTED |
| C02 | Frozen traces demonstrate active Q updates, interventions and condition-dependent state/action use. | S12 learning-mechanism interpretation | Mechanism under tested workloads | Active outcome-driven refinement is demonstrated. | Learning traces confirm active bounded refinement. | convergence; policy optimality; coverage-as-convergence | SUPPORTED-CONDITIONALLY |
| C03 | Exp10-Q failure: higher delivery, lower delay, higher duplicates/forwards vs AHBN. | n=5 paired; Δdelivery +0.129066; Δdelay -5.832377; Δduplicates +28798.0; Δforwards +41704.6 | one-peer failure | improvement in delivery/delay at communication-overhead cost | same | universal failure superiority | SUPPORTED |
| C04 | Exp11-Q: delivery/delay advantage at churn 0.00/0.20/0.40; delivery gain attenuates descriptively with churn. | Δdelivery +0.133472/+0.062944/+0.023040; Δdelay -5.977232/-3.765746/-1.198793; delivery/delay CIs exclude zero | tested churn levels | advantage across tested churn levels; decreasing delivery gain | same | churn-proof; proven dose-response; all churn rates | SUPPORTED |
| C05 | Exp12-Q: delivery/delay advantage across balanced/moderate/weak-heavy profiles, with higher overhead. | S12 Exp12 paired results | tested heterogeneity profiles | improvement under all tested profiles with overhead trade-off | same | solves heterogeneity; heterogeneity-independent superiority | SUPPORTED |
| C06 | Across all eight primary ControlSim conditions, Q-AHBN2 improves the delivery–latency trade-off relative to AHBN while generally increasing communication overhead. | S11-A 80 runs / 40 pairs; all eight delivery/delay paired CIs exclude zero; duplicates/forwards means higher | Exp10/11/12 only | consistent tested-condition delivery/latency improvement with overhead trade-off | same | best; dominates; universal superiority; improves all metrics | SUPPORTED |
| C07 | Exp13-Q provides bounded external positioning at churn=0.40; Q-AHBN2 improves AHBN delivery/delay but does not dominate external references across metrics. | S11-B/S12 five-method benchmark | one ControlSim churn benchmark | within dissemination trade-off; not a winner result | same | omnibus winner/ranking; general external superiority | SUPPORTED-CONDITIONALLY |
| C08 | Kubernetes demonstrates executable distributed/cloud-native realization and observability. | K6 25/25 validated coordinates + S12 | frozen K8s matrix | operational realization / deployment credibility | same | Kubernetes proves performance superiority | SUPPORTED |
| C09 | Kubernetes does not independently establish a consistent AHBN-performance advantage. | all four paired 95% CIs cross zero; seed directions vary | frozen K8s matrix | operational evidence, not confirmatory performance evidence | same | confirms/replicates ControlSim gains | SUPPORTED |
| C10 | ControlSim and Kubernetes are complementary evidence families; no pooling or literal replication. | experiment/statistical contracts; K6; S12 | cross-environment | primary controlled performance + complementary deployment evidence | same | pooled cross-environment effect; equivalence; literal replication | SUPPORTED |
| C11 | RO4/RQ4: bounded Q-learning refinement can improve delivery and delay under tested dynamic ControlSim conditions, with condition-dependent communication-overhead cost. | C01–C06 | thesis RO4/RQ4 | authorized RO4 synthesis | n/a | optimal/universal adaptive dissemination | SUPPORTED |
| C12 | Paper contribution combines bounded learning refinement, primary paired evaluation, bounded external positioning and Kubernetes operational realization. | frozen design + S11/S12/K6 | paper scope | publication contribution summary | authorized contribution framing | best/state-of-the-art/universal/K8s confirmation | SUPPORTED |
| C13 | Core limitations must remain explicit: n=5, condition scope, no convergence/optimality proof, no omnibus ranking, no cross-environment pooling/equivalence. | statistical contract; S12 | whole study | explicit limitations | explicit limitations | omission or dilution of these limits | SUPPORTED |
| C14 | Generic low-overhead/lightweight performance benefit is not established. | ControlSim higher duplicate/forward means; K8s F_attempt 2345.4 Q-AHBN2 vs 1448.0 AHBN | performance/resource claim | architecture may be called bounded/decentralized, not generically low-overhead | same | lightweight because fewer sends; reduced network overhead; resource-efficient | NOT SUPPORTED |
| C15 | Convergence, policy optimality, universal superiority, best-method and dominance claims are prohibited. | design/statistical contracts; S12; reviewer lessons | whole project | explicitly outside evidence | explicitly outside evidence | converged/optimal/best/dominates/universally superior | PROHIBITED |

## Mandatory quantitative boundary
For primary Exp10-Q/Exp11-Q/Exp12-Q claims:
- n=5 paired seeded runs per condition;
- same-seed AHBN vs Q-AHBN2 contrasts;
- two-sided 95% Student-t CI for mean paired difference;
- no pooled overall effect across unlike conditions;
- no new p-value family or post-hoc significance selection.

## Evidence-role boundary
- **Primary RO4/RQ4 proof:** Exp10-Q / Exp11-Q / Exp12-Q.
- **Mechanism:** learning traces only.
- **External positioning:** Exp13-Q only; churn=0.40; separate from primary proof.
- **Operational realization:** Kubernetes only; not independent confirmatory superiority.
- **Cross-environment:** complementary, not pooled, not literal replication.

## Authorized synthesis phrases
Preferred:
- “refines AHBN”;
- “bounded post-AHBN learning layer”;
- “improves the delivery–latency trade-off under the tested ControlSim conditions”;
- “with higher communication overhead” / “at a duplicate/forwarding cost”;
- “condition-dependent”;
- “bounded external positioning”;
- “operational realization” / “deployment credibility”.

Avoid:
- “best”;
- “optimal”;
- “converged”;
- “universally superior”;
- “dominates”;
- “replicated on Kubernetes”;
- generic “lightweight/low-overhead” performance language.

## S12A closure
The prior NOT-YET-CLAIMABLE entries are superseded by this final claim contract where S12/K6 evidence has now closed. Historical entries below are retained only through repository history, not as current authority.

**S12A = PASS / CLOSED.**
**Next paper gate: S13 — Q-AHBN2 Manuscript.**
