# S13 — Q-AHBN2 Manuscript

**Status:** ACTIVE — S13-1 PASS / CLOSED; S13-2 NEXT — 2026-09-29

## Objective
Draft the standalone Q-AHBN2 manuscript only from verified claims and registered evidence.

## Authoritative claim boundary
All manuscript statements must remain within the frozen S12A authorization in:
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`.

S13 does not reopen experiments, parameters, algorithms, metrics, statistical procedures, evidence, or scientific interpretation.

## S13-1 — Manuscript Structure / Evidence-to-Section Mapping

**Result:** PASS / CLOSED — 2026-09-29

### Working paper scope
A standalone paper on Q-AHBN2 as a bounded Q-learning meta-controller that refines immutable canonical AHBN, evaluated using primary paired ControlSim experiments under failure, churn and heterogeneity, one bounded five-method external-reference benchmark, and complementary Kubernetes operational-realization evidence.

### Working title boundary
The title must describe bounded learning/adaptive dissemination without implying optimality, universal superiority, convergence, or Kubernetes performance replication.

**Working title:**  
**Q-AHBN2: Bounded Q-Learning Refinement of Adaptive Hybrid Blockchain Dissemination under Dynamic Network Conditions**

This is a working manuscript title, not a scientific claim expansion.

## Frozen manuscript architecture

| Section | Scientific purpose | Authorized S12A claims | Primary evidence / authority | Required boundary |
|---|---|---|---|---|
| Abstract | Compact problem, method, primary result, trade-off, external positioning and deployment-realization summary | C01, C06, C07, C08, C10, C12, C13 | Design freeze; S11-A; S11-B; K6; S12 | Must state communication-overhead trade-off; no convergence/optimality/universal-superiority wording |
| 1. Introduction | Motivate dynamic dissemination problem; position AHBN as frozen adaptive baseline; state Q-AHBN2 gap and paper contributions | C01, C12, C13, C15 | Canonical AHBN contract; design freeze; reviewer lessons; S12A | Contribution language must use refinement, not replacement/redesign; no “best/state-of-the-art superiority” |
| 2. Related Work | Situate Gossip, Structured, hybrid/adaptive dissemination and RL-based adaptation; identify the bounded gap addressed by Q-AHBN2 | C01, C12, C15 as boundaries | Existing literature to be cited during drafting; canonical AHBN lineage | Literature synthesis must not manufacture empirical claims about Q-AHBN2 |
| 3. Q-AHBN2 Method | Define immutable AHBN proposal, state abstraction, bounded actions, reward attribution, Q update and post-AHBN refinement architecture | C01, C02 | Canonical AHBN contract; Q-AHBN2 design freeze; frozen learning contract | Mechanism description may show active learning design; must not imply convergence or optimality |
| 4. Experimental Methodology | Define ControlSim primary experiments, paired design, metrics/statistics, Exp13-Q bounded reference role and Kubernetes protocol/evidence role | C03–C10, C13 | Experiment contract; statistical contract; S11; K6 | Preserve n=5; same-seed pairing; Exp13 separate; K8s non-pooled and non-replication |
| 5. Results | Report learning evidence, Exp10-Q, Exp11-Q, Exp12-Q, cross-condition synthesis, Exp13-Q and Kubernetes results without changing evidence roles | C02–C10, C13, C14 | S11-A; S11-B; K6; S12 | Report delivery/delay gains together with duplicate/forwarding cost; K8s uncertainty explicit |
| 5.1 Learning behaviour | Demonstrate active Q updates, interventions and condition-dependent state/action behaviour | C02 | Frozen learning traces; S12 | Active refinement only; no convergence/policy-optimality claim |
| 5.2 Failure — Exp10-Q | Report AHBN vs Q-AHBN2 under frozen one-peer failure condition | C03 | S11-A/S12 Exp10-Q | Higher delivery/lower delay with higher duplicates/forwards; condition-specific |
| 5.3 Churn — Exp11-Q | Report three frozen churn levels and attenuation of delivery gain | C04 | S11-A/S12 Exp11-Q | Descriptive attenuation only; no dose-response proof or “churn-proof” claim |
| 5.4 Heterogeneity — Exp12-Q | Report balanced/moderate/weak-heavy profiles | C05 | S11-A/S12 Exp12-Q | Improvement under tested profiles with overhead trade-off; no general solution claim |
| 5.5 Cross-condition ControlSim synthesis | Synthesize the eight primary conditions | C06 | S11-A/S12 | No pooled overall effect; improvement is delivery–latency with communication-overhead trade-off |
| 5.6 Exp13-Q external-reference benchmark | Position Q-AHBN2 against Gossip, Structured, DC-SoC and AHBN at churn=0.40 | C07 | S11-B/S12 | Bounded external positioning only; no omnibus ranking/winner |
| 5.7 Kubernetes operational realization | Report executable cloud-native realization and paired uncertainty | C08, C09 | K6/S12 | Deployment credibility, not independent performance confirmation |
| 6. Discussion | Explain what bounded learning refinement changes, condition dependence, overhead trade-off, relation of primary/external/deployment evidence | C01, C02, C06–C10, C12–C15 | S12 interpretation + S12A contract | ControlSim and K8s complementary, not pooled/equivalent; no generic lightweight claim |
| 7. Limitations | Make evidentiary and generalization limits explicit | C13, C14, C15 | Statistical contract; S12; S12A | n=5; condition-specific; no convergence/optimality; no omnibus ranking; no cross-environment equivalence |
| 8. Conclusion | Answer paper objective with strongest evidence-bounded synthesis | C01, C06–C10, C12–C15 | Entire frozen evidence chain | Conclude refinement and tested trade-off improvement only; retain overhead and scope qualification |

## Claim-placement rules

### Paper-level contribution authority
C12 is the authoritative paper contribution synthesis. C11 is thesis RO4/RQ4 wording and is reserved for S13-T / Chapter 6 mapping; it must not be presented as an additional standalone-paper empirical claim.

### Manuscript-wide safeguards
C13–C15 apply across the complete manuscript, not only Section 7:
- C13 requires visible scope and uncertainty limitations wherever quantitative claims are summarized.
- C14 prohibits converting “bounded” architecture into a generic low-overhead/lightweight performance claim.
- C15 prohibits convergence, policy optimality, best-method, dominance and universal-superiority wording.

### Evidence-role separation
- Primary performance evidence: Exp10-Q / Exp11-Q / Exp12-Q only.
- Learning/mechanistic evidence: learning traces only.
- External positioning: Exp13-Q at churn=0.40 only.
- Operational realization: Kubernetes only.
- Cross-environment interpretation: complementary evidence; no statistical pooling, equivalence claim or literal replication.

## Planned manuscript result flow
1. Learning behaviour / mechanism evidence.
2. Exp10-Q failure.
3. Exp11-Q churn.
4. Exp12-Q heterogeneity.
5. Eight-condition ControlSim synthesis.
6. Exp13-Q bounded external positioning.
7. Kubernetes operational realization.
8. Discussion integrating the evidence roles without pooling them.

This ordering prevents the external benchmark or Kubernetes evidence from being mistaken for the primary RO4 causal evidence.

## S13-1 verification
The structure covers the requested Abstract, Introduction, Related Work, Q-AHBN2 Method, Experimental Methodology, Results, Discussion, Limitations and Conclusion. Every empirical/synthesis section is mapped to frozen S12A claim IDs and evidence roles. No new experiment, metric, statistical test, hypothesis, parameter or scientific interpretation has been introduced.

**S13-1 = PASS / CLOSED.**

## Next permitted action
**S13-2 — Manuscript Drafting Plan / Source-and-Evidence Pack**

S13-2 should establish the exact drafting sequence and authoritative source/evidence pack for each manuscript section before substantive prose is committed. Literature citations may be reconciled for Introduction/Related Work, but no scientific claim may exceed the S12A contract.

## Evidence organization
The manuscript organizes verified evidence as: learning validation; failure; churn; heterogeneity; Exp13-Q reference benchmark; bounded Kubernetes deployment validation; and cross-experiment discussion.

## Boundary
Claim wording must remain traceable through `docs/07_CLAIM_EVIDENCE_MATRIX.md`. Exp13-Q is bounded external positioning, not a universal algorithm ranking. Kubernetes is operational-realization evidence, not independent confirmation of ControlSim performance. Unfinished or unverified evidence must not be promoted into manuscript claims.
