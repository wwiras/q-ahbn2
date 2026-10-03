# S12 — Scientific Interpretation

**Status:** PASS / CLOSED — 2026-09-29

## Objective
Interpret only verified frozen evidence while preserving trade-offs, limitations, condition dependence and prohibited-overclaim boundaries.

## Evidence roles
1. Learning mechanics: frozen Learning Validation.
2. Primary RO4/RQ4 causal evidence: Exp10-Q / Exp11-Q / Exp12-Q.
3. External positioning: Exp13-Q only.
4. Operational realization: frozen K8s-VAL-Q / Exp13-Q-K8s.

## Primary ControlSim interpretation
S11-A contains 80 runs and 40 same-seed AHBN/Q-AHBN2 pairs. Across all eight frozen conditions, Q-AHBN2 minus AHBN has positive mean delivery difference and negative mean propagation-delay difference. All eight paired 95% Student-t CIs exclude zero for delivery and delay.

Paired mean differences (Q-AHBN2 minus AHBN):

| Condition | Delivery | Delay | Duplicates | Forwards |
|---|---:|---:|---:|---:|
| Exp10 control | +0.133472 | -5.977232 | +29,983.2 | +43,330.4 |
| Exp10 failure | +0.129066 | -5.832377 | +28,798.0 | +41,704.6 |
| Exp11 churn 0.00 | +0.133472 | -5.977232 | +29,983.2 | +43,330.4 |
| Exp11 churn 0.20 | +0.062944 | -3.765746 | +16,345.0 | +22,639.4 |
| Exp11 churn 0.40 | +0.023040 | -1.198793 | +2,944.8 | +5,248.8 |
| Exp12 balanced | +0.093462 | -6.875323 | +23,313.0 | +32,659.2 |
| Exp12 moderate heterogeneity | +0.057428 | -6.541088 | +16,042.4 | +21,785.2 |
| Exp12 weak-heavy | +0.058072 | -7.813670 | +18,496.4 | +24,303.6 |

Interpretation: Q-AHBN2 consistently shifts frozen AHBN toward higher delivery and lower delay in the tested ControlSim conditions, but generally at substantially higher duplicate and forwarding overhead. It is a trade-off refinement, not across-the-board dominance. At churn=0.40, overhead-difference CIs cross zero and are more uncertain.

The delivery gain contracts descriptively as churn rises: +13.347 pp at 0.00, +6.294 pp at 0.20, +2.304 pp at 0.40. No dose-response model is claimed.

## Learning-mechanism interpretation
Frozen traces show extensive Q updates, non-zero state-action coverage and repeated interventions above AHBN. Coverage rises to 0.142 at churn=0.40 and from 0.106 to 0.111 across the three heterogeneity profiles. Mean reward remains negative under the frozen reward definition. Evidence supports active outcome-driven refinement, not convergence, policy optimality or universal benefit.

## Exp13-Q positioning
Five-seed means at the single frozen ControlSim churn=0.40 benchmark:

| Method | Delivery | Delay | Duplicates | Forwards |
|---|---:|---:|---:|---:|
| Gossip | 0.916300 | 3.420314 | 327,220.0 | 417,850.0 |
| Structured | 0.920000 | 4.489333 | 0.0 | 91,000.0 |
| DC-SoC | 0.920000 | 1.505306 | 0.0 | 91,000.0 |
| AHBN | 0.798664 | 10.063965 | 140,033.8 | 218,900.2 |
| Q-AHBN2 | 0.821704 | 8.865172 | 142,978.6 | 224,149.0 |

Q-AHBN2 improves AHBN delivery/delay in this bounded benchmark but does not dominate the external references across all outcomes. Exp13-Q therefore positions the learned refinement within the dissemination trade-off; it is not universal-superiority evidence.

## Kubernetes interpretation — S18 post-remediation reconciliation
S17 supersedes only the historical Q-AHBN2 Kubernetes measurement row and associated paired statistics; the four historical comparator families remain authoritative and unchanged.

Corrected five-seed means:

| Method | Delivery | Delay (s) | Duplicates | F_attempt | F_success / total_forwards |
|---|---:|---:|---:|---:|---:|
| AHBN | 0.260135 | 0.025193 | 403.6 | 1448.0 | 998.6 |
| Q-AHBN2 | 0.390977 | 0.038385 | 578.4 | 2251.0 | 1612.2 |

Corrected paired Q-AHBN2-minus-AHBN differences:
- delivery +0.130842, 95% CI [-0.243288,+0.504973];
- delay +0.013192 s, 95% CI [-0.027568,+0.053952];
- duplicates +174.8, 95% CI [-281.0,+630.6];
- forwarding attempts +803.0, 95% CI [-1424.2,+3030.2];
- successful forwards +613.6, 95% CI [-1157.7,+2384.9].

All five intervals cross zero and seed-level effects change direction. Kubernetes therefore continues to support executable distributed realization and observability, but not an independent consistent performance-improvement claim over AHBN. The corrected accounting removes the historical logging artifact; it does not establish reduced forwarding or generic low overhead.


## Integrated interpretation
- Q-AHBN2 is a functioning learning meta-controller above immutable AHBN.
- ControlSim provides the primary RO4/RQ4 causal evidence: higher delivery/lower delay under all tested failure, churn and heterogeneity conditions.
- These benefits generally cost more duplicate traffic and forwarding effort.
- Effect magnitude is condition-dependent, especially under increasing churn.
- Exp13-Q provides bounded external positioning only.
- Kubernetes provides bounded deployment credibility, not literal replication or a consistent independent performance advantage.
- ControlSim and Kubernetes are complementary evidence families and must not be pooled.

## Limitations / prohibited overclaims
n=5 per cell; no convergence or policy-optimality experiment; no universal superiority; no global ranking or omnibus winner score; no generic low-overhead claim; no literal ControlSim/Kubernetes replication; no cross-environment pooling. Kubernetes recovery diagnostics remain secondary.

## Result
**S12 = PASS / CLOSED.** Frozen evidence supports a condition-dependent learning refinement with explicit overhead and deployment limitations.

## Next permitted action
**S12A — Thesis–Paper Claim Reconciliation.**
