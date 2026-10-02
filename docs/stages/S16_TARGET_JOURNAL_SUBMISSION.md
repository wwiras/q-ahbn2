# S16 — Publication Artifact Engineering

**Programme status:** ACTIVE  
**Opened:** 2026-10-01  
**Entry condition:** S15 PASS / CLOSED  
**Scientific baseline:** `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`


## Authorized sources and reconciliation contract

S16 inherits the project-wide authority model from `docs/00_QAHBN2_MASTER.md` and `docs/00_SOURCE_AUTHORITY_REGISTER.md`. Every S16 gate must reconcile the latest authoritative state before artifact construction or manuscript modification.

### Scientific/code/control authority

- Repository: `wwiras/q-ahbn2`
- Pinned manuscript science baseline: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`
- Designated local synchronized scientific workspace:  
  `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`
- Authoritative preserved scientific/evidence Drive root: folder ID `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`

Operational model:

```text
GitHub science/control
        ↓
local execution / working area
        ↓
validity + completeness checks
        ↓
deliberate evidence promotion / preservation
        ↓
verified Drive evidence
```

Automatic Drive synchronization alone is not evidence promotion.

### Manuscript/publication-source authority

- Repository: `wwiras/QAHBN2-Manuscript`
- Active manuscript source: `versions/v0.0/main.tex`
- Manuscript-side Drive folder ID: `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`
- Designated local synchronized manuscript workspace:  
  `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myPaper/ClusterComputing/QAHBN2-Manuscript`

Operational model:

```text
QAHBN2-Manuscript GitHub
        ↕
local manuscript workspace
        ↕
manuscript Drive synchronization
```

The manuscript repository is the publication-source authority. Drive synchronization does not override Git-tracked manuscript provenance.

### Historical source authority used during S16

- `Q_AHBN_FirstDraft.pdf` — Drive file ID `1NahEY5sZPdwhpg2uduBxIxqyS3ikMGqj` — **Authority Level 6 historical source only**.
- Permitted during S16 for historical design lineage and prior figure/table/algorithm/presentation ideas.
- It is not current scientific authority for state/action/reward semantics, hyperparameters, convergence/optimality, quantitative results, or claim wording.
- Any conflict is resolved in favour of the current frozen Q-AHBN2 contracts, promoted evidence, S12/S12A, and the pinned science baseline.

### Mandatory gate reconciliation

Before each S16 gate:
1. fetch and reconcile latest `main` for `wwiras/q-ahbn2`;
2. reconcile `docs/00_QAHBN2_MASTER.md` and `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
3. reconcile the applicable S16 stage record and frozen S12/S12A/S15 constraints;
4. reconcile the latest `wwiras/QAHBN2-Manuscript` publication source and manuscript provenance before any manuscript artifact edit;
5. use Drive only for preserved evidence/source material according to its registered role;
6. after every GitHub write, re-fetch the affected file(s) and verify readback before declaring the transition authoritative.

Conversation memory is not authority.

## Programme-control amendment

The earlier target-journal-selection branch is **SUPERSEDED by researcher decision on 2026-10-01**. Venue selection will be made manually by the researcher and is removed from the S16 critical path.

The existing neutral LaTeX format remains authoritative during S16. No journal-template migration is authorized.

S16 is now restricted to publication-artifact engineering from frozen evidence:
- figures;
- analytical tables;
- formal algorithm/pseudocode;
- artifact/text consistency and visual production.

Frozen throughout S16:
- canonical AHBN and Q-AHBN science;
- parameters, reward, state/action space and transition semantics;
- experiment matrices and run counts;
- S12/S12A claim boundaries;
- S15 statistical/evidence-role contract.

No new experiment or new inferential family is authorized by S16.

# S16-0 — Figure, Table and Algorithm Architecture Audit

**Status:** PASS / CLOSED — 2026-10-01

## Audit question

Determine exactly which final publication artifacts are scientifically necessary, which question each artifact answers, the frozen evidence source, and whether it replaces, complements, or absorbs an existing manuscript artifact.

## Current manuscript artifact inventory

The active manuscript currently contains:
- Figure `fig:qahbn-cycle`: boxed textual Q-AHBN intervention/learning cycle.
- Table `tab:learning-mechanism`: bounded learning-trace evidence.
- Table `tab:primary-paired-results`: primary paired ControlSim results including uncertainty.
- Table `tab:primary-tradeoff-synthesis`: eight-condition effect/trade-off synthesis.
- Table `tab:exp13-results`: five-method churn=0.40 benchmark.
- Table `tab:kubernetes-accounting`: total_forwards versus F_attempt accounting caveat.
- Table `tab:kubernetes-results`: frozen Kubernetes five-method means.

No formal publication pseudocode/algorithm environment is currently present.

## Artifact architecture decision

| ID | Final artifact | Scientific question answered | Frozen evidence / contract | Relationship to current manuscript | Priority |
|---|---|---|---|---|---|
| F1 | Q-AHBN architecture and learning-cycle figure | Where does Q-AHBN act relative to immutable AHBN, and how does information/reward flow? | Frozen AHBN boundary; Q-AHBN state/action/reward/transition contract; S12 C01-C02 | **REPLACE/UPGRADE** current boxed `fig:qahbn-cycle` | ESSENTIAL |
| A1 | Formal Q-AHBN bounded-refinement pseudocode | What exact ordered procedure is executed at each decision and update? | 81-state, five-action, epsilon-greedy, direct-attempt reward closure, next-same-peer update, frozen Q update | **NEW; COMPLEMENTS F1**. Must not duplicate explanatory prose line-for-line | ESSENTIAL |
| F2 | Primary eight-condition paired trade-off figure | Are delivery/delay improvements accompanied by communication cost across the primary conditions? | S11-A 40 paired comparisons; authorized paired CIs; S12 C03-C06 | **COMPLEMENTS/ABSORBS visual role of** `tab:primary-tradeoff-synthesis`; exact uncertainty remains in `tab:primary-paired-results` | ESSENTIAL |
| F3 | Dynamic-stress response figure | How does the AHBN→Q-AHBN effect vary across failure, churn and heterogeneity conditions? | Same S11-A frozen effects; descriptive churn attenuation; S12/S15 | **COMPLEMENTS F2**, not a second copy of all four metrics. Focus on stress-family interpretation | HIGH |
| F4 | Exp13 bounded comparator figure | Where does Q-AHBN sit relative to Gossip, Structured, DC-SoC and AHBN at the single frozen churn=0.40 benchmark? | S11-B / Exp13-Q 25 runs; S12 C07 | **COMPLEMENTS** `tab:exp13-results`; must remain metric-wise, descriptive, non-ranking | HIGH |
| F5 | Gamma sensitivity figure | What bounded evidence supported selection of gamma=0.70 among the predeclared values {0.70,0.80,0.90}? | Frozen 15-run gamma sensitivity; seeds 42-46; AR-1.4.2-AR-1.4.4 | **NEW** publication figure; must show bounded parameter-selection provenance only, not broad robustness/global optimality | HIGH |
| T1 | Learning-mechanism evidence table | Is learning demonstrably active without claiming convergence? | Frozen learning traces; q_updates, coverage, interventions/action use; S12 C02/C13/C15 | **RETAIN AND RATIONALIZE** `tab:learning-mechanism` | HIGH |
| T2 | Primary paired statistical table | What are the exact primary paired estimates/uncertainty supporting the main claims? | S11-A paired contract | **RETAIN** `tab:primary-paired-results` as numerical/statistical authority | ESSENTIAL |
| T3 | Kubernetes evidence + accounting table | What does Kubernetes establish, and why must total_forwards be interpreted with F_attempt? | 25/25 Kubernetes coordinates; paired intervals; runtime accounting; S12 C08-C10/C14-C15 | **MERGE/RATIONALIZE** `tab:kubernetes-accounting` with the relevant AHBN/Q-AHBN portion of `tab:kubernetes-results` where clarity permits; five-method operational context may remain separately if needed | HIGH |
| T4 | Gamma sensitivity table/callout | Why was gamma=0.70 selected, and what is the bounded scope of that evidence? | 15-run gamma sensitivity, gamma={0.70,0.80,0.90}, seeds 42-46 | **NEW compact artifact** only if exact frozen values are publication-ready; otherwise concise methods text is sufficient | MEDIUM |
| T5 | Exp13 exact-values table | What exact five-method values underlie F4? | Frozen Exp13 means | **RETAIN** `tab:exp13-results`, potentially compacted after F4 | HIGH |

## Redundancy decisions

1. **F1 versus A1:** both are required but answer different questions. F1 is architecture/information flow; A1 is executable logical sequence.
2. **F2 versus primary tables:** F2 carries the pattern/trade-off message. T2 remains the exact statistical authority. The current `tab:primary-tradeoff-synthesis` becomes redundant once F2 exists unless it contains exact values unavailable in T2; default disposition is **ABSORB/REMOVE after verification**.
3. **F2 versus F3:** F2 gives the complete eight-condition four-metric overview; F3 must therefore emphasize stress-family response, especially churn attenuation and heterogeneity/failure context, rather than redraw the same four panels.
4. **F4 versus T5:** F4 supports visual comparison; T5 preserves exact benchmark values. Neither may imply an omnibus score, ranking or winner.
5. **Kubernetes:** do **not** create a superiority figure. A table/callout is scientifically safer because the key message is evidence role and accounting semantics, not a stable performance direction.
6. **Gamma:** create **F5 as a compact bounded sensitivity figure**, restricted to the three predeclared values gamma={0.70,0.80,0.90}. It must explain parameter-selection provenance only and must not imply broad robustness, global optimality, convergence, or exhaustive hyperparameter search. T4 remains an optional exact-value companion if needed.

## Minimum final artifact set

The researcher-approved publication-artifact package is therefore:
- **5 figures:** F1 architecture, F2 primary trade-off, F3 dynamic stress, F4 Exp13 positioning, F5 bounded gamma sensitivity;
- **1 formal algorithm:** A1 Q-AHBN bounded-refinement pseudocode;
- **5 tables:** T1 learning evidence, T2 paired statistical results, T3 Kubernetes/accounting, T4 compact gamma-sensitivity exact-value table/callout, and T5 Exp13 exact values.

**T4 is optional at final publication layout**, so the final manuscript may contain 4 core tables if F5 and surrounding Methods text provide sufficient exact-value clarity. F5 itself is now part of the approved figure architecture.

This architecture is deliberately selective: each artifact must answer a distinct reviewer/scientific question. It does not authorize artifact-count inflation or new evidence.

## Construction principles

- Every artifact must answer one explicit scientific/reviewer question.
- Exact numerical values must originate from frozen registered evidence or existing authorized manuscript values.
- No chart may imply ranking, convergence, universal superiority, global optimality, generic low overhead or cross-environment equivalence.
- ControlSim and Kubernetes remain visually and statistically separate.
- Use consistent condition/method naming across figure, table and prose.
- Captions must state evidence scope and interpretation boundaries where misreading is plausible.
- Publication artifacts should be source-controlled and reproducible; no decorative graphics are authorized.
- Existing neutral LaTeX format remains unchanged.

## Gate decision

The current evidence is sufficient to construct the artifact package. No new experiment, rerun, parameter change or new inferential test is required.

**S16-0 = PASS / CLOSED.**

## Revised controlled programme — researcher-approved stage architecture

This programme revision is an administrative/control amendment made after S16-0 closure and before any further scientific/publication-artifact gate is executed. It does not reopen S16-0, S12/S12A/S15, the pinned science baseline, experiments, statistics, parameters, or manuscript claims.

### S16-0A — Historical Q-AHBN Manuscript Artifact Refinement Audit — NEXT

Systematically inspect the Authority-Level-6 historical `Q_AHBN_FirstDraft.pdf` before new artifact design. Produce a controlled mapping:

`historical artifact -> useful presentation idea -> current scientific conflict (if any) -> permitted reuse -> prohibited inheritance -> proposed S16 destination`.

This gate may recover presentation concepts, architecture organization, algorithm/workflow presentation, result-figure structures, table organization, caption patterns, and explanatory sequencing only. It must not inherit historical six-action semantics, superseded state/reward definitions or parameters, convergence/optimality claims, historical numerical results, or historical simulation/Kubernetes conclusions as current Q-AHBN evidence.

### S16-1 — Q-AHBN Architecture Figure Specification

Freeze the scientific and visual specification for F1 only: canonical observations -> immutable AHBN proposal -> bounded Q-AHBN refinement -> eligible-target realization/forwarding -> directly attributable outcomes -> reward/learning feedback. S16-0A presentation lessons may inform layout only.

### S16-2 — Formal Q-AHBN Algorithm Specification

Freeze A1 against the current 81-state x 5-action design, AHBN-first intervention boundary, epsilon-greedy selection, bounded proposal transformation, requested-versus-realized forwarding distinction, direct-attempt reward closure, F=0 no-update boundary, same-peer successor-state semantics, delayed attribution, and frozen Q update. Exact lifecycle ordering must be reconciled with current implementation/contracts before publication.

### S16-3 — Mechanism Figure + Algorithm Consistency Audit

Perform a strict semantic reconciliation across F1, A1, manuscript Section 3, `docs/02_QAHBN2_DESIGN_FREEZE.md`, canonical AHBN authority, implementation semantics, and source-authority rules. Neither artifact is publication-ready until this audit passes.

### S16-4 — Mechanism Artifact Manuscript Integration

Replace/upgrade the current boxed `fig:qahbn-cycle`, integrate A1, and update only directly affected explanatory prose, captions and cross-references. Preserve the neutral LaTeX architecture and frozen science.

### S16-5 — Primary Paired Trade-off Figure Specification

Specify F2 from the frozen 40 same-seed AHBN--Q-AHBN pairs across eight primary ControlSim conditions. Delivery and propagation delay use only authorized paired uncertainty; duplicates and forwards expose the communication-cost direction without inventing a new inferential family.

### S16-6 — Primary Trade-off Figure Construction + Verification

Construct F2 and independently reconcile every plotted quantity, uncertainty statement, label and caption against S11-A/S12/S12A and registered provenance. No new interpretation is authorized.

### S16-7 — Dynamic-Stress Response Figure Specification

Specify F3 so it adds information beyond F2, emphasizing the failure contrast, descriptive churn attenuation, and heterogeneity response. No fitted trend, dose-response model, or extrapolation is authorized.

### S16-8 — Dynamic-Stress Figure Construction + Verification

Construct F3 and verify all values, visual encodings, captions and evidence boundaries against frozen primary evidence.

### S16-9 — Exp13 Bounded Positioning Figure Specification

Specify F4 for Gossip, Structured, DC-SoC, AHBN and Q-AHBN at the single frozen churn=0.40 Exp13-Q reference benchmark. The artifact must remain metric-wise, descriptive and non-ranking; no composite score or winner framing is permitted.

### S16-10 — Exp13 Figure Construction + Verification

Construct F4 and reconcile every plotted value and caption with frozen Exp13-Q evidence and the exact-values table.

### S16-11 — Learning-Evidence Table Rationalization

Review `tab:learning-mechanism`. Retain only evidence establishing active learning/refinement, including Q updates, state-action coverage and intervention/action use where authorized. Remove redundancy with F1/A1 and preserve the no-convergence/no-policy-optimality boundary.

### S16-12 — Primary Statistical Table Rationalization

Audit `tab:primary-paired-results` and `tab:primary-tradeoff-synthesis`. Preserve the paired statistical table as the exact numerical/uncertainty authority. After F2 verification, absorb/remove the synthesis table if it is redundant and contains no uniquely required exact value.

### S16-13 — Kubernetes Evidence and Accounting Table Rationalization

Reconcile `tab:kubernetes-results` and `tab:kubernetes-accounting`. Preserve Kubernetes as operational-realization evidence, all paired-CI uncertainty, seed-direction limits where relevant, and the `total_forwards` versus `F_attempt` accounting distinction. No Kubernetes superiority visualization is authorized.

### S16-14 — Gamma Sensitivity Figure Specification

Specify F5 from the frozen 15-run gamma sensitivity evidence over gamma={0.70,0.80,0.90}, seeds 42--46. Freeze the visual encoding, exact evidence fields, caption scope and non-claims. The figure must support only bounded parameter-selection provenance for gamma=0.70 and must not imply broad robustness, global optimality, convergence, or exhaustive hyperparameter search.

### S16-14A — Gamma Sensitivity Figure Construction + Verification

Construct F5 and independently reconcile every plotted quantity, label and caption against the frozen gamma-sensitivity evidence and AR-1.4.2--AR-1.4.4. Verify that the visual does not overstate the evidence scope.

### S16-14B — Gamma Sensitivity Table/Callout Decision

Evaluate whether T4 materially improves exact-value auditability beyond F5 and concise Methods text. Retain T4 only if it adds nonredundant publication value. If retained, it must remain compact and exact-value oriented; if omitted, record the redundancy decision explicitly.

### S16-15 — Whole Artifact Package Integration

Integrate verified F1--F5, A1 and the rationalized table set into `wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`. Update cross-references, captions, placement and immediately surrounding prose only as needed. No new science is authorized.

### S16-16 — Artifact-to-Evidence Provenance Audit

For every final figure (F1--F5), table (T1--T5, with T4 optional at final layout) and algorithm (A1), register and verify:

`artifact ID -> manuscript label -> source evidence/contract -> claim IDs -> exact numerical provenance where applicable -> permitted interpretation -> prohibited interpretation`.

Synchronize the manuscript-side provenance record only after verification.

### S16-17 — Figure/Table/Algorithm Visual + LaTeX Production Audit

Audit rendering, legibility, typography, line/marker distinction, legends, table width, figure scale, caption completeness, cross-references, float placement, page flow, grayscale readability and LaTeX/source integrity. This is a production audit, not a scientific reopening.

### S16-18 — Reviewer-Challenge Artifact Audit

Test whether the finished artifact package directly answers foreseeable reviewer questions about the intervention boundary, immutable AHBN, exact algorithm procedure, evidence of active learning, communication cost, dynamic-stress response, bounded comparator positioning, Kubernetes evidence role/accounting, and gamma selection. No new reviewer-driven experiment is implied by this gate.

### S16-19 — Whole-Manuscript Artifact/Text Consistency Audit

Reconcile Abstract, Introduction, Methods, Experimental Methodology, Results, Discussion, Limitations and Conclusion against every final artifact. Reconfirm prohibitions on convergence/policy optimality, global hyperparameter optimality, universal superiority/ranking, generic lightweight/low-overhead performance, cross-environment pooling/equivalence, and Kubernetes performance confirmation.

### S16-20 — Final Historical-to-Current Manuscript Refinement Audit

Return once to Authority-Level-6 `Q_AHBN_FirstDraft.pdf` after the current artifact package is mature. Check whether any useful historical presentation/explanatory element was missed. Permitted changes are limited to presentation, explanatory sequencing, visual organization, captions and bounded contextual clarity. Historical science, results and superseded claims remain prohibited.

### S16-21 — Publication Artifact Engineering Closure

Close S16 only after the approved 5-figure + 1-algorithm + 5-table architecture has been resolved, all retained artifacts are integrated and verified, the optional T4 redundancy decision is recorded, artifact provenance is complete, visual/LaTeX and reviewer-challenge audits pass, whole-manuscript artifact/text consistency passes, and no unauthorized scientific change has occurred.

## Controlled state after programme revision

- **S16-0:** PASS / CLOSED.
- **S16-0A:** PASS / CLOSED.
- **Researcher-approved artifact architecture amendment (2026-10-02):** **5 figures + 1 formal algorithm + 5 tables**, with T4 optional at final manuscript layout.
- **S16-1:** NEXT / RELEASED.
- **S16-2 through S16-14, S16-14A, S16-14B, and S16-15 through S16-21:** PENDING; each is released only by closure of its required predecessor.
- Venue selection remains researcher-controlled and outside the S16 critical path.
- A later venue-specific submission-production programme may be opened only after researcher venue selection and S16 closure.

## Next controlled gate

**S16-1 — Q-AHBN Architecture Figure Specification.**

---

# S16-0A — Historical Q-AHBN Manuscript Artifact Refinement Audit

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Audit Authority-Level-6 historical manuscript `Q_AHBN_FirstDraft.pdf` only for reusable publication-presentation ideas. Historical science, numerical results, state/action/reward semantics, hyperparameters, convergence/optimality claims, and simulation-to-Kubernetes conclusions remain non-authoritative.

## Historical artifact inventory and classification

| Historical artifact / pattern | Useful presentation idea | Current scientific conflict | Classification | Permitted reuse | Prohibited inheritance | Proposed S16 destination |
|---|---|---|---|---|---|---|
| Fig. 1 — overall Q-AHBN architecture | Layered visual hierarchy from observations through learning/control to dissemination, with explicit feedback | Historical figure places Q-learning before AHBN and treats learned policy as feeding the AHBN controller; current design requires immutable AHBN first, then bounded post-AHBN refinement | **ADAPT** | Reuse layered structure, compact labels, directional flow and feedback-loop concept | No historical ordering, six-action semantics, adaptive-weight wording, or implication that Q-learning retunes AHBN internals | **F1** |
| Fig. 2 — Q-learning decision workflow | Simple top-to-bottom lifecycle with a visible cycle return | Historical workflow assumes generic immediate reward/update and omits direct-attempt closure, F=0 no-update, delayed attribution and next-same-peer semantics | **ADAPT** | Reuse lifecycle readability and explicit cycle arrow | No “AHBN executes selected policy” semantics, immediate generic reward ownership, or same-step successor assumption | **F1 + A1** |
| Fig. 3 — AHBN/Q-learning interaction | Separating baseline proposal, meta-refinement, final policy and execution is reviewer-friendly | Historical action names and parameter-adjustment semantics differ materially from the frozen five-action design | **REUSE CONCEPT** | Reuse the visual distinction among baseline proposal, bounded refinement and final/realized behaviour | No six named legacy actions, weight/tau manipulation, or superseded AHBN controller details | **F1**, with exact lifecycle deferred to **A1** |
| Fig. 4 — overall experimental framework | Compact environment/evidence pipeline helps readers understand study structure | Historical simulation-training -> learned-Q-table -> Kubernetes transfer/generalization narrative conflicts with current separate evidence-family contract | **REPLACE** | At most reuse the idea of visually separating environments and evidence flow | No trained-policy transfer, convergence-before-deployment, identical-metric/generalization, replication or cross-environment confirmation framing | No new S16 artifact; presentation lesson only for **T3/captions** |
| Figs. 5–7 — reward/state/action learning plots | Learning activity is easier to review when mechanism evidence is visible | Historical plots explicitly support convergence, state-space saturation and six-action distributions; values and semantics are obsolete | **DO NOT REUSE** | Presentation lesson only: keep current learning evidence concise and interpretable | No historical curves, values, convergence/saturation claims, six-action frequencies or old episode counts | **T1** only |
| Failure result figures | Pair dissemination benefit with communication cost rather than present one metric | Historical values/claims differ from current paired evidence and include lower-overhead conclusions | **REPLACE** | Reuse multi-metric pairing and condition-specific captioning | No old numbers, run counts, comparator matrix or lower-overhead interpretation | **F2/F3** |
| Churn result figures | Small multiples with common stress axis improve pattern recognition | Historical churn grid, recovery/adaptation-efficiency metrics and numerical trends are not current evidence | **ADAPT** | Reuse small-multiple stress-family layout and consistent condition axis | No old churn levels, recovery/adaptation-efficiency metric, monotonic/dose-response interpretation or values | **F3** |
| Heterogeneity result figures | Metric-specific panels make the trade-off immediately visible | Historical evidence often shows lower duplicates/forwards and resource-aware six-action explanations, conflicting with current evidence | **ADAPT** | Reuse aligned metric panels and direct AHBN/Q-AHBN comparison style | No historical lower-overhead claim, values, scenario semantics or action-frequency interpretation | **F2/F3** |
| Kubernetes result figures/tables | Deployment-specific presentation should expose operational metrics and accounting explicitly | Historical manuscript treats Kubernetes as policy-transfer/generalization/performance confirmation and reports obsolete values | **REPLACE** | Reuse compact operational table organization and explanatory captions | No performance-confirmation, generalization, adaptation-efficiency or old numerical claims | **T3** |
| Tables 1–5 — objectives/framework/scenario/metric mapping | Tables can compress methodology and map questions to evidence | Historical RO numbering, metrics, experiment descriptions and adaptation-efficiency formulation are superseded | **NOT RELEVANT TO CURRENT S16** | General navigation lesson only | No restoration of old experiment matrix, convergence objective, adaptation-efficiency metric or run descriptions | Existing Methods prose; no new S16 artifact |
| Tables 6+ — learning/results/action-frequency tables | Exact values beside figures can support auditability | Historical values, six-action frequencies, state counts, rewards and run counts are not Q-AHBN2 evidence | **DO NOT REUSE** | Only the principle that exact numerical authority belongs in tables | No historical statistics, action labels or values | **T1/T2/T5** with current evidence only |
| Algorithm/pseudocode | No formal algorithm/pseudocode environment was found in the historical draft | There is therefore no historical algorithm authority to reuse | **NOT RELEVANT TO CURRENT S16** | None beyond confirming the need for a formal current algorithm | Do not reconstruct the current algorithm from historical prose | **A1 remains NEW** |
| Captions | Self-contained captions can explain the scientific message and scope | Several historical captions embed unsupported convergence, generalization, lower-overhead or superiority claims | **ADAPT** | Reuse descriptive, self-contained caption style with explicit condition/scope | No stronger interpretation than S12/S12A permits | All **F1–F4/T1–T5** |
| Section-to-figure sequencing | Architecture -> workflow -> interaction -> experimental framework -> results creates a progressive mental model | Historical mechanism figures are partially redundant and science ordering is obsolete | **REUSE CONCEPT** | Keep progressive reviewer comprehension: mechanism first, exact procedure second, evidence/trade-offs next, bounded deployment evidence later | Do not retain three overlapping mechanism diagrams or obsolete experiment progression | **S16-1 onward** |

## Reusable presentation lessons

1. Use a **layered visual hierarchy** with short labels and clear arrows; this is more readable than prose-only boxes.
2. Keep **architecture and executable procedure separate**: F1 explains where information flows; A1 defines exact lifecycle semantics.
3. Show the **closed-loop feedback path explicitly**, but label it with current attributable outcomes/reward ownership rather than generic dissemination feedback.
4. Prefer **small multiples/aligned metric panels** for dynamic-stress interpretation; do not collapse delivery, delay and communication cost into a composite score.
5. Keep **exact numerical authority in tables** while figures communicate pattern and evidence role.
6. Make captions **self-contained and scope-bounded**, especially where a reviewer could misread an artifact as convergence, superiority, low overhead, or cross-environment confirmation.
7. Preserve **visual separation between ControlSim and Kubernetes**; the historical sequential-transfer narrative is rejected.
8. Avoid redundancy: the historical manuscript shows that three overlapping mechanism diagrams are unnecessary; current **F1 + A1** is sufficient.

## Scientific conflicts that remain blocked

The audit reconfirmed that the historical manuscript contains presentation-adjacent scientific statements incompatible with the frozen design/evidence:
- six-action policy semantics and obsolete action names;
- superseded state/reward/controller descriptions;
- convergence/stable-policy and state-space-saturation interpretations;
- historical adaptation-efficiency formulation;
- old experiment matrices, churn levels, run counts and numerical results;
- lower-overhead/resource-efficiency conclusions that conflict with the current communication-cost trade-off;
- simulation-training -> learned-Q-table -> Kubernetes-transfer/generalization framing;
- Kubernetes performance-confirmation language.

None may migrate into S16.

## Mapping into frozen S16 artifact architecture

- **F1:** strongly benefits from the historical layered architecture, feedback-loop clarity and baseline/refinement/final-action separation, but current ordering must be **observations -> immutable AHBN proposal -> bounded Q-AHBN refinement -> eligible-target realization/forwarding -> directly attributable outcomes -> reward/learning feedback**.
- **A1:** remains entirely current-specification work. Historical workflow contributes only the idea of a readable ordered lifecycle.
- **F2:** reuse the multi-metric comparison principle only; all values, uncertainty and trade-off direction come from S11-A/S12.
- **F3:** reuse the small-multiple stress-response presentation pattern, especially shared axes and family-specific panels; use only current failure/churn/heterogeneity evidence and no trend fitting.
- **F4:** no direct historical five-method analogue is suitable for reuse; current Exp13 purpose remains unchanged. Historical lesson: keep metrics visually separate.
- **T1:** expose active learning compactly, but no historical reward/convergence/state/action statistic is reusable.
- **T2:** remains exact current paired-statistical authority; historical result tables have no evidentiary role.
- **T3:** historical Kubernetes presentation reinforces the value of explicit runtime accounting, but current table must emphasize operational realization and the `total_forwards`/`F_attempt` distinction.
- **T4:** no useful historical gamma artifact; retain the current bounded sensitivity decision.
- **T5:** current Exp13 exact-values table remains unchanged; historical numerical tables provide no reusable data.

## Concrete recommendations for S16-1 onward

1. In **S16-1**, use one reviewer-oriented F1 with roughly 5–6 clear layers rather than multiple overlapping mechanism figures.
2. F1 should visually distinguish **AHBN proposal**, **Q-AHBN requested refinement**, and **realized forwarding**; this is the strongest reusable idea from historical Fig. 3.
3. Draw the learning return path from **directly attributable NEW/DUPLICATE/FAILED outcomes / reward closure** back to the learning layer; do not use a generic immediate Bellman loop that hides delayed closure and same-peer succession.
4. Reserve exact temporal/update semantics for **A1** so F1 remains conceptually readable.
5. Build **F2/F3** as aligned panels with consistent condition naming and a visible zero/reference baseline where appropriate; do not add adaptation-efficiency or recovery-time panels.
6. Keep **Kubernetes tabular**, not a performance-superiority plot.
7. Use captions to state scope and non-claims explicitly where misinterpretation risk is high.
8. Consolidate rather than inflate: current **F1 + A1** is sufficient for mechanism exposition.

## Administrative-adjustment decision

**No adjustment to the frozen S16 artifact architecture is required.**

The historical audit refines presentation strategy only. F1, A1, F2, F3, F4 and T1–T5 retain their S16-0 scientific purposes and evidence roles. No new artifact, experiment, statistic, metric, algorithm change, parameter change, claim authorization or manuscript-source edit is required.

## Gate decision

**S16-0A = PASS / CLOSED.**

The historical manuscript yielded useful presentation concepts but no current scientific authority. The audit therefore closes without scientific redesign and without modification of `versions/v0.0/main.tex`.

## Next controlled gate

**S16-1 — Q-AHBN Architecture Figure Specification.**


---

# S16 Programme Architecture Amendment — Researcher Approval, 2026-10-02

**Status:** PASS / FROZEN ADMINISTRATIVE AMENDMENT

Following S16-0 and S16-0A closure, the researcher explicitly approved the final working publication-artifact architecture:

| ID | Approved artifact | Purpose / reviewer question | Highlight rationale |
|---|---|---|---|
| F1 | Q-AHBN Architecture and Learning-Cycle Figure | Explain canonical observations -> immutable AHBN proposal -> bounded Q-AHBN refinement -> realized forwarding -> attributable outcomes -> learning feedback. | Main conceptual figure; makes the post-AHBN bounded-refinement novelty and immutable-AHBN boundary immediately visible. |
| F2 | Primary Eight-Condition Paired Trade-off Figure | Visualize the main AHBN vs Q-AHBN evidence across the eight primary ControlSim conditions, including benefit and communication-cost directions. | Main quantitative result figure; communicates the central paired trade-off without hiding duplicates/forwarding cost. |
| F3 | Dynamic-Stress Response Figure | Show how the AHBN->Q-AHBN effect varies across failure, churn and heterogeneity stress families. | Shows where refinement helps and how the effect changes under the dynamic conditions the method targets. |
| F4 | Exp13 Bounded Five-Method Comparator Figure | Position Gossip, Structured, DC-SoC, AHBN and Q-AHBN at the single frozen churn=0.40 benchmark. | Provides bounded external methodological positioning without converting Exp13 into primary causal evidence or a winner ranking. |
| F5 | Gamma Sensitivity Figure | Show the bounded gamma={0.70,0.80,0.90} evidence supporting selection of gamma=0.70. | Demonstrates that the discount factor was examined rather than arbitrarily chosen, while remaining explicitly bounded and non-optimality seeking. |
| A1 | Formal Q-AHBN Bounded-Refinement Algorithm / Pseudocode | Specify the exact executable lifecycle including AHBN-first proposal, five Q-actions, realization, outcome attribution, reward closure, F=0 no-update, next-same-peer semantics and Q update. | Reproducibility bridge between conceptual architecture and implementation semantics. |
| T1 | Learning-Mechanism Evidence Table | Summarize evidence that learning/refinement was active without convergence or policy-optimality claims. | Gives compact mechanism evidence and replaces historical convergence-style diagnostics. |
| T2 | Primary Paired Statistical Results Table | Preserve exact primary AHBN vs Q-AHBN paired estimates and authorized uncertainty. | Numerical/statistical authority behind F2/F3. |
| T3 | Kubernetes Evidence and Accounting Table | Present Kubernetes operational-realization evidence and the total_forwards versus F_attempt accounting distinction. | Keeps deployment evidence bounded and avoids misleading performance-confirmation visualization. |
| T4 | Compact Gamma-Sensitivity Table / Callout | Provide exact gamma-sensitivity values when they materially improve auditability. | Optional companion to F5; retained only if nonredundant. |
| T5 | Exp13 Exact-Values Table | Preserve the exact five-method values underlying F4. | Numerical authority for the bounded Exp13 comparison. |

Approved hierarchy:
- **Mechanism:** F1 -> A1 -> T1
- **Primary scientific evidence:** F2 -> F3 -> T2
- **Broader comparator positioning:** F4 -> T5
- **Parameter justification:** F5 -> T4 (optional)
- **Cloud-native validation:** T3 only; no Kubernetes superiority figure

Administrative consequences:
1. F5 is now an approved core figure rather than an optional/omitted large gamma artifact.
2. S16-14 is converted from an artifact-decision gate into **F5 specification**.
3. New **S16-14A** constructs/verifies F5.
4. New **S16-14B** decides whether optional T4 adds nonredundant exact-value utility.
5. S16-15 integration scope becomes **F1--F5 + A1 + rationalized T1--T5**.
6. No new experiment, rerun, parameter search, statistical family, claim authorization, or manuscript-source edit is introduced by this amendment.
7. The pinned science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

**Next released gate remains S16-1 — Q-AHBN Architecture Figure Specification.**


---

# S16-1 — Q-AHBN Architecture Figure Specification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Freeze the scientific content and visual specification for **F1 — Q-AHBN Architecture and Learning-Cycle Figure** only. This gate specifies the figure; it does not construct the final TikZ/LaTeX artifact and does not modify `versions/v0.0/main.tex`.

## Reconciliation

S16-1 was reconciled against:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/02_QAHBN2_DESIGN_FREEZE.md`;
- S12/S12A claim boundaries;
- S16-0 and S16-0A;
- manuscript `docs/MANUSCRIPT_MASTER.md`, `docs/PROVENANCE.md`, and current `versions/v0.0/main.tex`;
- pinned science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

No scientific conflict requiring reopening was found.

## F1 reviewer question

> **Where does Q-AHBN act relative to immutable canonical AHBN, what is requested versus realized, and how do directly attributable forwarding outcomes return learning evidence to the bounded refinement layer?**

F1 is conceptual architecture/information-flow authority. A1 will remain the exact executable lifecycle authority.

## Frozen F1 scientific flow

The figure MUST communicate this ordering:

```text
[1] LOCAL CANONICAL OBSERVATIONS
    normalized local d, l, u, c
              ↓
    canonical EWMA state
    (d_hat, l_hat, u_hat, c_hat)
              │
              ├─────────────────────────────┐
              ↓                             ↓
[2] IMMUTABLE CANONICAL AHBN          [3a] Q STATE KEY
    z = -d_hat+l_hat+u_hat+c_hat           discretize same EWMA state
    w = sigmoid(z)                          L/M/H per dimension
    canonical mode + S5 fanout              3^4 = 81 states
              ↓                             │
    p_AHBN=(mode_AHBN,k_AHBN)              │
              └──────────────┬──────────────┘
                             ↓
[3] BOUNDED Q-AHBN REFINEMENT
    epsilon-greedy selection from five actions:
    KEEP | FANOUT_DOWN | FANOUT_UP |
    SET_GOSSIP | SET_STRUCTURED
    action is applied relative to preserved AHBN proposal
                             ↓
    requested p_Q=(mode_Q,k_Q)
                             ↓
[4] ELIGIBLE-TARGET REALIZATION + FORWARDING
    mode-specific eligible set N_e
    realized target count 0 <= k_real <= min(k_Q,|N_e|)
    requested decision remains distinct from realized forwarding
                             ↓
[5] DIRECT ATTRIBUTABLE OUTCOMES
    each initiated direct attempt terminates as exactly one:
    NEW | DUPLICATE | FAILED
    F=NEW+DUPLICATE+FAILED
                             ↓
[6] REWARD / LEARNING FEEDBACK
    reward-bearing closure only when F>0
    R=(NEW-DUPLICATE-FAILED)/F
    F=0 => no numerical reward / no reward-bearing Q update
    learning update uses the originating decision and
    next-same-peer successor-state contract
                             └──────────────↺ future Q-AHBN decisions
```

## Required semantic distinctions

F1 MUST visually preserve these distinctions:

1. **Continuous canonical AHBN state vs discrete Q state.** AHBN operates on continuous EWMA values; the L/M/H discretization is only the Q-table key.
2. **AHBN proposal vs Q-AHBN refinement.** `(mode_AHBN,k_AHBN)` is complete and traceable before Q-AHBN acts.
3. **Selected Q action vs refined requested proposal.** The action transforms the preserved AHBN proposal; it does not retune AHBN internals.
4. **Requested fanout vs realized forwarding.** `k_Q` is a request; `0 <= k_real <= min(k_Q,|N_e|)` is constrained by the eligible set.
5. **Realized targets vs initiated attempts/outcomes.** Unrealized target slots do not create synthetic FAILED outcomes.
6. **Outcome evidence vs environmental state.** NEW/DUPLICATE/FAILED and reward information feed learning; they are not additional environmental state dimensions.
7. **Reward closure vs successor-state timing.** The figure must not imply that reward and `s_(t+1)` necessarily become available simultaneously.
8. **Current decision vs future learning.** Reward ownership remains with the originating decision; transition order follows the same peer's next Q-AHBN decision opportunity.

## Visual architecture

F1 is frozen as **one landscape-oriented conceptual figure with six numbered visual layers**.

### Layer 1 — Observe
Short heading: **Canonical local observations**

Show:
- `d, l, u, c`;
- canonical normalization/EWMA;
- `(d_hat,l_hat,u_hat,c_hat)`.

Do not show environment-specific raw sensor implementation details.

### Layer 2 — AHBN Adapt
Short heading: **Immutable canonical AHBN**

Show:
- `z=-d_hat+l_hat+u_hat+c_hat`;
- mode rule at conceptual level;
- S5 fanout proposal;
- output `(mode_AHBN,k_AHBN)`.

The word **IMMUTABLE** or an equivalent explicit visual label is mandatory.

### Layer 3 — Q-AHBN Refine
Short heading: **Bounded Q-AHBN refinement**

Show two converging inputs:
- discrete 81-state key from the same canonical EWMA state;
- preserved AHBN proposal.

Inside the layer show:
- epsilon-greedy Q-action selection;
- the five frozen actions;
- transformation of the AHBN proposal only;
- output `(mode_Q,k_Q)`.

Do not show historical six-action names, adaptive weights, tau, direct modification of z/w/EWMA, or a learned replacement controller.

### Layer 4 — Realize / Execute
Short heading: **Eligible-target realization and forwarding**

Show:
- eligible-neighbour set `N_e`;
- `0 <= k_real <= min(k_Q,|N_e|)`;
- forwarding attempts.

This layer is the visual boundary between **requested refinement** and **realized execution**.

### Layer 5 — Outcome
Short heading: **Direct attributable outcomes**

Show:
- NEW;
- DUPLICATE;
- FAILED;
- `F=NEW+DUPLICATE+FAILED`.

The three outcomes must be presented as mutually exclusive terminal outcomes of initiated direct attempts.

### Layer 6 — Learn
Short heading: **Reward closure and learning feedback**

Show:
- `R=(NEW-DUPLICATE-FAILED)/F` for `F>0`;
- compact note: `F=0 -> no reward-bearing update`;
- compact note: `s_(t+1) = same peer's next Q-AHBN decision state`;
- return arrow to the Q-AHBN learning layer/future decision.

Do **not** draw a simple immediate `s_t,a_t,R_t,s_(t+1)` loop that visually asserts simultaneous reward closure and successor-state availability.

## Visual grammar

- Use **solid forward arrows** for runtime observation/proposal/refinement/execution/outcome flow.
- Use a **visually distinct return arrow** for learning feedback. Distinction must remain understandable in grayscale; line style/arrow form, not color alone, must carry meaning.
- AHBN and Q-AHBN must occupy separate bounded regions.
- The preserved AHBN proposal must cross an explicit post-AHBN intervention boundary before entering the Q-AHBN refinement block.
- Requested and realized quantities must use different labels and boxes; they must never share one ambiguous “final action” label.
- Keep formulas minimal. F1 is not the algorithm listing.
- Use short labels suitable for one-column or two-column publication scaling; no prose paragraph inside the figure.
- No decorative network topology graphic is required unless it directly clarifies eligible-target realization.
- The figure must remain legible in grayscale and when reduced to normal manuscript width.

## Information deliberately deferred to A1

F1 MUST NOT become a pseudocode substitute. A1 remains authoritative for:
- exact per-decision bookkeeping;
- action application ordering;
- epsilon decay/parameter mechanics;
- delayed reward attachment;
- next-state-first versus reward-first arrival;
- overlapping/out-of-order closures;
- Q-update readiness condition;
- terminal rewarded transition zero bootstrap;
- exact Q-update equation and frozen alpha_Q/gamma values.

F1 may name these boundaries only where necessary to avoid a false lifecycle interpretation.

## Caption specification

Working caption:

> **Q-AHBN bounded-refinement architecture and learning cycle.** Canonical AHBN first processes the local normalized observations and produces an independently traceable mode/fanout proposal. Q-AHBN discretizes the same canonical EWMA state, selects one of five bounded meta-actions, and refines only the completed AHBN proposal before eligible-target realization. Learning evidence is derived from directly attributable NEW, DUPLICATE, and FAILED forwarding outcomes. Requested and realized forwarding remain distinct, and the learning return path follows the frozen reward-closure and next-same-peer transition contract. The figure describes architecture and information flow; exact update ordering is specified by Algorithm A1.

Final wording may be tightened during S16-4 integration without changing these semantics.

## Required figure labels / terminology

Publication-facing terminology:
- **Q-AHBN**, not Q-AHBN2, inside the manuscript figure;
- **canonical AHBN**;
- **immutable AHBN proposal** or equivalent;
- **bounded refinement**;
- **requested proposal**;
- **eligible-target realization**;
- **realized forwarding**;
- **direct attributable outcomes**;
- **reward closure / learning feedback**.

Repository/control documentation may continue to use Q-AHBN2 where referring to the project/repository identity.

## Prohibited visual implications

F1 MUST NOT imply:
- Q-learning executes before AHBN;
- Q-AHBN replaces AHBN;
- Q-AHBN modifies AHBN normalization, EWMA, z, sigmoid, mode rule or S5 thresholds;
- historical six-action semantics, weight adjustment or tau control;
- a hard Q-layer fanout cap of 6;
- failure/event labels as privileged Q-state inputs;
- immediate reward closure for every decision;
- `F=0` as numerical zero reward;
- unrealized target slots as FAILED attempts;
- convergence, stable/optimal policy, or global hyperparameter optimality;
- generic low-overhead/resource-efficiency performance;
- simulation-to-Kubernetes policy transfer or cross-environment confirmation;
- any experimental result or superiority claim.

## Relationship to current manuscript artifact

Current `fig:qahbn-cycle` is a useful semantic placeholder but is not the final F1. At S16-4 it will be **REPLACED/UPGRADED**, preserving its valid scientific ordering while adding:
- explicit continuous-state/discrete-state branching;
- explicit AHBN proposal preservation;
- requested-versus-realized distinction;
- eligible-target realization;
- precise reward/no-reward boundary;
- non-immediate next-same-peer learning feedback.

No `versions/v0.0/main.tex` edit is authorized in S16-1.

## Verification checklist

S16-1 specification passes only if:
- canonical AHBN is visibly first and immutable — **PASS**;
- Q-AHBN acts only post-AHBN — **PASS**;
- 81-state/five-action contract is correct — **PASS**;
- requested and realized forwarding are distinct — **PASS**;
- NEW/DUPLICATE/FAILED attribution is correct — **PASS**;
- `F=0` no-update boundary is preserved — **PASS**;
- next-same-peer/delayed attribution is not misrepresented — **PASS**;
- historical six-action/convergence/transfer semantics are absent — **PASS**;
- F1 remains conceptual and A1 retains executable-detail authority — **PASS**;
- no new science/evidence/claim is introduced — **PASS**.

## Gate decision

**S16-1 = PASS / CLOSED.**

F1's scientific and visual specification is frozen. No figure was constructed, no experiment/evidence was changed, and no manuscript source was modified.

## Next controlled gate

**S16-2 — Formal Q-AHBN Algorithm Specification.**


---

# S16-2 — Formal Q-AHBN Algorithm Specification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Freeze **A1 — Formal Q-AHBN Bounded-Refinement Algorithm / Pseudocode** as the publication-facing executable-semantics bridge between F1 and the frozen implementation. This gate specifies A1 only. It does not insert the algorithm into `versions/v0.0/main.tex`, construct F1, alter source code, rerun experiments, or change frozen science.

## Authority reconciliation

A1 was reconciled against the current authority chain, especially:
- canonical-AHBN-first architecture;
- frozen four-dimensional canonical EWMA state and 81-state discretization;
- final five-action contract;
- requested-versus-realized forwarding distinction;
- direct-attempt NEW/DUPLICATE/FAILED attribution;
- reward and F=0 semantics;
- concurrent per-decision transition bookkeeping;
- next-same-peer successor-state semantics;
- terminal zero-bootstrap semantics;
- one-step tabular Q-learning;
- current learning constants after S02 closure.

Historical `gamma=0.90` worked examples in earlier chronological design text are explicitly superseded and MUST NOT appear as current A1 authority.

## A1 reviewer question

> **Exactly how does one Q-AHBN decision refine a completed AHBN proposal, how are its forwarding outcomes attributed, and under what conditions is the corresponding Q-value updated?**

## Publication role

A1 is the executable-semantics authority for the manuscript. It complements:
- **F1:** conceptual architecture/information flow;
- **T1:** evidence that the learning mechanism was active.

A1 is not implementation source code and must not expose environment-specific plumbing that is irrelevant to the logical cross-platform algorithm.

## Frozen algorithm title

**Algorithm A1 — Q-AHBN bounded post-AHBN refinement with attributable delayed Q-learning**

A shorter typeset title may be used at integration if the semantic meaning is unchanged.

## Frozen inputs and state

A1 MUST declare or make unambiguous:

- canonical local observations supplied through the existing AHBN adapter;
- canonical AHBN controller, immutable;
- shared Q table initialized to zero;
- action set
  `A={KEEP,FANOUT_DOWN,FANOUT_UP,SET_GOSSIP,SET_STRUCTURED}`;
- `alpha_Q=0.25`;
- `gamma=0.70`;
- `epsilon_0=0.30`;
- `epsilon_min=0.03`;
- `lambda_epsilon=0.995`;
- seeded learner RNG / uniform random tie handling;
- per-peer/per-decision transition records required for overlapping decisions.

The logical Q table contains at most `81 x 5 = 405` state-action entries.

## Frozen A1 pseudocode specification

The publication algorithm MUST be semantically equivalent to the following:

```text
Algorithm A1: Q-AHBN bounded post-AHBN refinement with attributable delayed Q-learning

Initialize Q[S,A] <- 0 for 81 states x 5 actions
Initialize epsilon <- epsilon_0 = 0.30
Initialize empty per-decision transition records
Set alpha_Q <- 0.25, gamma <- 0.70
Set epsilon_min <- 0.03, lambda_epsilon <- 0.995

ON each new-message Q-AHBN decision opportunity for message m at peer p:

  1. Update canonical AHBN observations and canonical EWMA state
       x_t <- (d_hat_t, l_hat_t, u_hat_t, c_hat_t)

  2. Execute immutable canonical AHBN first
       p_AHBN <- (mode_AHBN, k_AHBN)
     Preserve/log p_AHBN before any Q intervention

  3. Form the Q state from the same canonical EWMA snapshot
       s_t <- (B(d_hat_t), B(l_hat_t), B(u_hat_t), B(c_hat_t))
     where B maps [0,1] to L/M/H using fixed 1/3 and 2/3 boundaries

  4. Before selecting the current action, register s_t as the successor
     state for the immediately preceding Q-AHBN decision at the SAME PEER,
     if such a predecessor is awaiting its next-state component.
     If that predecessor's reward is already closed, it may now become
     update-ready.

  5. Select a_t by seeded epsilon-greedy policy over Q(s_t, .):
       with probability epsilon:
           choose uniformly from the five actions
       otherwise:
           choose uniformly among actions attaining max_a Q(s_t,a)

  6. Apply exactly one bounded action relative to preserved p_AHBN:
       KEEP            -> (mode_AHBN, k_AHBN)
       FANOUT_DOWN     -> (mode_AHBN, k_AHBN - 1)
       FANOUT_UP       -> (mode_AHBN, k_AHBN + 1)
       SET_GOSSIP      -> (Gossip, k_AHBN)
       SET_STRUCTURED  -> (Structured, k_AHBN)
     Denote the requested refined proposal p_Q=(mode_Q,k_Q).

  7. Apply the existing mode-specific eligible-target realization:
       choose eligible set N_e according to canonical execution semantics
       0 <= k_real <= min(k_Q, |N_e|)
     Initiate forwarding only to the realized targets.
     Requested fanout and realized forwarding remain distinct.

  8. Create a transition/attribution record owned by this decision
       D_t=(peer p, message m, s_t, a_t, p_AHBN, p_Q, ...)
     and attach every initiated direct attempt to D_t.

  9. For each initiated direct attempt, record exactly one terminal outcome:
       NEW | DUPLICATE | FAILED
     Do not create FAILED outcomes for target slots that were not realized.

 10. When all direct attempts owned by D_t have terminated:
       F_t <- NEW_t + DUPLICATE_t + FAILED_t

       if F_t = 0:
           mark NO_FORWARDING_EVIDENCE
           assign no numerical reward
           perform no reward-bearing Q update for D_t
       else:
           R_t <- (NEW_t - DUPLICATE_t - FAILED_t) / F_t
           attach R_t to D_t

 11. A nonterminal D_t is update-ready only when BOTH are available:
       (a) its own closed numerical reward R_t, and
       (b) s_(t+1), captured at peer p's next Q-AHBN decision opportunity.
     Reward closure and successor-state arrival may occur in either order.
     Closure order MUST NOT redefine transition order.

 12. For each update-ready nonterminal record:
       Q(s_t,a_t) <-
         Q(s_t,a_t)
         + alpha_Q * [ R_t
                       + gamma * max_a' Q(s_(t+1),a')
                       - Q(s_t,a_t) ]

 13. For each terminal rewarded record:
       use zero bootstrap:
       Q(s_t,a_t) <-
         Q(s_t,a_t)
         + alpha_Q * [ R_t - Q(s_t,a_t) ]

 14. Decay exploration once per learner decision:
       epsilon <- max(epsilon_min, lambda_epsilon * epsilon)

 15. Continue; multiple attribution records may coexist and close
     independently against the shared Q table.
```

## Temporal-order clarification

For publication readability, A1 may visually group the runtime decision path and the asynchronous learning-completion path into two labelled parts:

**A. Decision and forwarding path**
- observe/update canonical AHBN;
- execute AHBN first;
- discretize state;
- capture same-peer successor linkage;
- epsilon-greedy action;
- bounded proposal transform;
- eligible-target realization;
- direct attempts.

**B. Attribution and learning-completion path**
- close NEW/DUPLICATE/FAILED attribution;
- compute reward only for `F>0`;
- wait until both reward and successor state exist;
- update shared Q table;
- terminal zero bootstrap;
- no reward-bearing update for `F=0`.

This two-part presentation is preferred if a single linear listing would falsely imply synchronous reward closure.

## Action boundary details

A1 MUST preserve:
- canonical AHBN proposal fanout `k_AHBN in {2,3,4,5,6}`;
- one-step Q fanout refinement, permitting requested `k_Q in {1,...,7}`;
- **no historical Q-layer clipping back to 6**;
- physical/topological realization by the eligible set;
- mode and fanout primitive actions remain independently attributable.

A1 MUST NOT invent a new fanout bound or safety override.

## Reward and attribution details

A1 MUST preserve:
- one Q action for one new-message forwarding decision at one peer;
- direct-attempt attribution ownership by the originating decision;
- mutually exclusive NEW/DUPLICATE/FAILED outcomes;
- `F=NEW+DUPLICATE+FAILED`;
- `R=(NEW-DUPLICATE-FAILED)/F` only when `F>0`;
- numerical `R=0` with `F>0` is a valid observed reward and is NOT equivalent to `F=0`;
- `F=0` produces no numerical reward and no reward-bearing Q update.

## Transition and concurrency details

A1 MUST preserve:
- concurrent per-message attribution records;
- same-peer next-decision state as `s_(t+1)`;
- reward ownership by the originating decision even if closure is delayed/out of order;
- reward and successor state may arrive in either order;
- update occurs only when both are available;
- terminal rewarded transition uses zero bootstrap;
- shared Q table receives each independently completed transition.

A1 MUST NOT revert to a single historical `prev_state/prev_action` chain.

## Exploration mechanics

Publication A1 MUST use the current frozen exploration mechanics:
- epsilon-greedy;
- seeded controlled RNG;
- uniform random exploration over all five actions;
- uniform random tie-breaking among maximizing actions;
- `epsilon_0=0.30`;
- `epsilon_min=0.03`;
- multiplicative `lambda_epsilon=0.995`;
- decay once per learner decision.

No exploration parameter is claimed optimal.

## Q-update authority

For a nonterminal rewarded transition:

[
Q(s_t,a_t) leftarrow Q(s_t,a_t)
+alpha_Qleft[
R_t+gammamax_{a'}Q(s_{t+1},a')-Q(s_t,a_t)
ight],
]

with current frozen values:

[
alpha_Q=0.25,qquad gamma=0.70.
]

For a terminal rewarded transition the bootstrap term is zero.

Historical chronological text using `gamma=0.90` is provenance only and is prohibited from the current algorithm artifact.

## Publication abstraction boundary

A1 SHOULD omit:
- ControlSim event-queue implementation details;
- Kubernetes/gRPC implementation details;
- file/log field names unless required for scientific meaning;
- experiment-specific disturbance values;
- Exp10/Exp11/Exp12/Exp13 conditions;
- statistical analysis;
- gamma-sensitivity results;
- learning-curve or convergence diagnostics.

A1 SHOULD retain only algorithmically necessary logical semantics common to the validated implementations.

## Relationship to F1

F1 and A1 must agree on:
1. canonical AHBN executes first;
2. Q state comes from the same canonical EWMA snapshot;
3. five bounded actions;
4. preserved AHBN proposal;
5. requested refined proposal;
6. eligible-target realization;
7. direct attributable NEW/DUPLICATE/FAILED outcomes;
8. F=0 no-reward-bearing-update boundary;
9. learning feedback to future decisions.

A1 adds the temporal/concurrency precision deliberately omitted from F1.

## Working algorithm note/caption

Working note:

> **Algorithm A1 formalizes the bounded post-AHBN refinement lifecycle.** Canonical AHBN produces and preserves its complete proposal before Q-AHBN selects one of five primitive refinements. Requested decisions are then subject to existing eligible-target realization. Each decision owns the terminal outcomes of its initiated direct forwarding attempts; a numerical reward exists only when at least one attempt is made. Because reward closure and the same peer's next decision state may arrive asynchronously, a nonterminal Q update is executed only after both components are available. Terminal rewarded transitions use zero bootstrap.

## Prohibited implications

A1 MUST NOT imply:
- AHBN is learned, replaced or retuned;
- Q-AHBN selects before AHBN;
- historical six-action/weight/tau semantics;
- privileged failure/recovery labels in the Q state;
- Q-requested fanout is capped at canonical AHBN's maximum 6;
- unrealized targets count as FAILED;
- F=0 is numerical zero reward;
- reward closure determines successor-state order;
- updates are necessarily synchronous;
- convergence, stable policy, policy optimality or global hyperparameter optimality;
- ControlSim-trained policy transfer to Kubernetes;
- performance superiority.

## Verification

Specification audit:
- AHBN-first ordering — **PASS**;
- current 81 x 5 state/action contract — **PASS**;
- five action transforms — **PASS**;
- no Q-layer cap at 6 — **PASS**;
- requested-versus-realized distinction — **PASS**;
- direct-attempt outcome ownership — **PASS**;
- F=0 semantics — **PASS**;
- next-same-peer transition — **PASS**;
- asynchronous reward/successor readiness — **PASS**;
- terminal zero bootstrap — **PASS**;
- current alpha_Q=0.25 and gamma=0.70 — **PASS**;
- current epsilon schedule — **PASS**;
- historical gamma=0.90 excluded as current authority — **PASS**;
- no new science or evidence — **PASS**.

## Gate decision

**S16-2 = PASS / CLOSED.**

A1's publication-level executable semantics are frozen. No algorithm was inserted into the manuscript and no scientific implementation was changed.

## Next controlled gate

**S16-3 — Mechanism Figure + Algorithm Consistency Audit.**


---

# S16-3 — Mechanism Figure + Algorithm Consistency Audit

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Perform a strict semantic reconciliation across the frozen F1 specification, frozen A1 specification, current manuscript Section 3, `docs/02_QAHBN2_DESIGN_FREEZE.md`, canonical AHBN authority, validated implementation semantics, and source-authority rules.

This gate is an audit/correction gate only. It does not construct F1/A1 and does not edit `versions/v0.0/main.tex`.

## Reconciliation result

One specification-level overstatement was found and corrected before closure:

### C1 — realized-fanout equality overstatement

**Finding:** S16-1/S16-2 used `k_real=min(k_Q,|N_e|)` / assignment-equivalent wording in the draft F1/A1 specifications.

**Higher-authority contract:** the frozen design requires:

[
0 le k_{mathrm{real}} le min(k_Q,|N_e|).
]

The eligible-target realization stage may realize fewer targets than the requested budget. Therefore equality is not guaranteed by the frozen contract.

**Correction:** all S16 F1/A1 specification occurrences that asserted equality/assignment were corrected to the bounded relation. This is a documentation-semantic correction to match already-frozen science; it does not change the algorithm, implementation, experiments, evidence, or claims.

**Manuscript status:** current Section 3 already uses the correct bounded relation and therefore requires no scientific correction for this item.

## F1 ↔ A1 ↔ Section 3 consistency matrix

| Semantic item | F1 | A1 | Current Section 3 | Frozen authority | Audit |
|---|---|---|---|---|---|
| canonical observations / EWMA | continuous canonical state shown | canonical state updated first | explicit | canonical AHBN | PASS |
| AHBN executes first | explicit immutable AHBN layer | Step 2 before Q action | explicit | architectural invariant | PASS |
| AHBN proposal preserved | explicit `p_AHBN` | preserved/logged before Q intervention | explicit | proposal/intervention boundary | PASS |
| Q state source | same canonical EWMA snapshot | same canonical EWMA snapshot | same variables | state contract | PASS |
| discretization | L/M/H, 81 states | fixed 1/3 and 2/3 bins | explicit | 81-state contract | PASS |
| action set | five actions | same five transforms | same five transforms | action contract | PASS |
| Q fanout boundary | bounded one-step refinement | `k_Q in {1,...,7}` | same | action contract | PASS |
| historical cap at 6 | prohibited | explicitly prohibited | values 1 and 7 explicit | action invariant A12/A13 | PASS |
| requested vs realized | distinct | distinct | distinct | architecture/observability | PASS |
| realized-fanout relation | corrected to bounded relation | corrected to bounded relation | bounded relation | `0<=k_real<=min(...)` | **PASS after C1** |
| direct attempt outcomes | NEW/DUPLICATE/FAILED | exact terminal outcomes | explicit | reward contract | PASS |
| unrealized slots | not FAILED | not FAILED | explicit | reward attribution | PASS |
| `F=0` | no numerical reward/update | explicit | explicit | reward contract | PASS |
| numerical `R=0,F>0` | deferred to A1 | explicit | explicit | reward contract | PASS |
| same-peer successor | named | exact capture rule | explicit | transition contract | PASS |
| overlapping records | deferred to A1 | concurrent records | explicit | transition contract | PASS |
| reward/next-state arrival order | non-synchronous visual requirement | either order | either order | transition contract | PASS |
| nonterminal update readiness | deferred to A1 | both components required | explicit | transition contract | PASS |
| terminal zero bootstrap | deferred to A1 | explicit | explicit | transition contract | PASS |
| Q update | deferred to A1 | alpha=0.25, gamma=0.70 | same | current learning contract | PASS |
| epsilon mechanics | deferred to A1 | 0.30→floor 0.03, decay 0.995 | same | lifecycle contract | PASS |
| convergence/optimality | prohibited | prohibited | explicitly disclaimed | claim contract | PASS |

## Notation reconciliation

The audit identified a presentation ambiguity, not a scientific conflict:

- manuscript Section 3 currently uses `s_t` once for the continuous four-variable learning-state description and `S_t` for the discrete Q-table key;
- A1 uses `x_t` for the continuous canonical EWMA snapshot and `s_t` for the discrete Q state;
- F1 conceptually distinguishes the continuous canonical state from the discrete Q key.

For F1/A1 integration, the publication notation is frozen as:

[
x_t=(hat d_t,hatell_t,hat u_t,hat c_t)
]

for the **continuous canonical EWMA snapshot**, and

[
s_t=(B(hat d_t),B(hatell_t),B(hat u_t),B(hat c_t))
]

for the **discrete 81-state Q-table key**.

At S16-4, Section 3 may receive this notation-only harmonization so F1, A1 and prose use one unambiguous convention. This does not alter state semantics.

## Temporal consistency audit

F1 intentionally compresses the asynchronous lifecycle. It remains consistent with A1 only under these frozen reading rules:

1. the feedback arrow represents learning evidence returning to **future Q-AHBN decisions**, not an immediate same-step update;
2. `s_(t+1)` is the same peer's next Q-AHBN decision state;
3. reward belongs to the originating decision and may close before or after that successor state is observed;
4. A1, not F1, is authoritative for per-decision records, readiness and update ordering;
5. terminal rewarded transitions use zero bootstrap;
6. `F=0` never enters the numerical reward/Q-update path.

No temporal contradiction remains under these rules.

## Action/realization consistency audit

The mechanism artifacts must retain the following exact separation:

```text
canonical AHBN proposal:
  k_AHBN in {2,3,4,5,6}

one selected Q action:
  delta fanout in {-1,0,+1} OR mode-set primitive

Q-requested proposal:
  k_Q in {1,2,3,4,5,6,7}

canonical mode-specific realization:
  0 <= k_real <= min(k_Q, |N_e|)
```

The phrase **realized target count** must not be typeset as if it were necessarily equal to the requested eligible budget.

## F1/A1 division of responsibility — frozen after audit

**F1 must answer:** where the learning layer sits, what it receives, what it may refine, what is requested versus realized, what outcomes return as evidence, and where the feedback loop goes.

**A1 must answer:** exactly how state/action selection, proposal transformation, per-decision attribution, reward closure, successor linkage, update readiness, terminal handling, Q update and epsilon decay operate.

F1 must not duplicate A1's concurrency machinery. A1 must not become an environment-specific implementation listing.

## Current manuscript Section 3 disposition

Section 3 is scientifically consistent with the audited F1/A1 contracts on:
- immutable AHBN;
- state dimensions and bins;
- five actions;
- `k_Q in {1,...,7}`;
- bounded eligible-target realization;
- direct-attempt reward;
- `F=0`;
- alpha/gamma;
- epsilon schedule;
- same-peer successor state;
- asynchronous reward/successor ordering;
- terminal zero bootstrap;
- no convergence/optimality implication.

Two publication-engineering changes are therefore authorized for **S16-4 only**:
1. replace/upgrade the placeholder `fig:qahbn-cycle` with audited F1;
2. harmonize continuous/discrete state notation and integrate audited A1 with only directly necessary prose/cross-reference changes.

No broader Section 3 rewrite is justified by S16-3.

## Prohibited semantic drift reconfirmed

Neither F1 nor A1 may imply:
- Q-before-AHBN execution;
- replacement or retuning of canonical AHBN;
- six historical actions, tau or adaptive-weight manipulation;
- privileged disturbance labels as Q state;
- Q-layer clipping to 6;
- equality between requested eligible budget and realized target count;
- synthetic FAILED outcomes for unrealized targets;
- `F=0` as numerical zero reward;
- reward-closure order as transition order;
- synchronous-only updates;
- convergence/policy optimality/global parameter optimality;
- performance superiority;
- ControlSim-to-Kubernetes learned-policy transfer.

## Verification

- mandatory authority reconciliation — **PASS**;
- F1 versus A1 semantic audit — **PASS after C1 correction**;
- F1/A1 versus current Section 3 — **PASS**;
- F1/A1 versus design freeze — **PASS after C1 correction**;
- AHBN-first boundary — **PASS**;
- state/discretization — **PASS**;
- five-action transforms — **PASS**;
- requested/realized distinction — **PASS**;
- reward attribution and F=0 — **PASS**;
- transition/concurrency semantics — **PASS**;
- terminal handling — **PASS**;
- learning constants/exploration — **PASS**;
- claim/non-claim boundaries — **PASS**;
- no experiment/evidence/science change — **PASS**.

## Gate decision

**S16-3 = PASS / CLOSED.**

The F1 and A1 specifications are now mutually consistent with the frozen design authority and current manuscript science. The only defect found was the realized-fanout equality overstatement, corrected to the authoritative bounded relation. No final artifact was constructed or integrated.

## Next controlled gate

**S16-4 — Mechanism Artifact Manuscript Integration.**


---

# S16-4 — Mechanism Artifact Manuscript Integration

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Integrate the audited mechanism artifacts into the active manuscript without reopening science:
1. replace/upgrade the placeholder `fig:qahbn-cycle` with the audited F1 mechanism figure;
2. integrate formal Algorithm A1;
3. harmonize continuous/discrete state notation;
4. update only directly affected prose, captions and cross-references.

## Authority reconciliation

S16-4 was executed after reconciling:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- S16-1, S16-2 and S16-3;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`;
- researcher-supplied Drive roots for the scientific and manuscript workspaces.

No new scientific evidence was required because F1/A1 are mechanism artifacts derived from already-frozen design authority rather than quantitative experimental results.

## Manuscript changes performed

File:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

### F1 integration

The previous boxed textual placeholder was replaced by a publication-oriented TikZ mechanism figure with six layers:

1. canonical local observations;
2. immutable canonical AHBN;
3. bounded Q-AHBN refinement;
4. eligible-target realization;
5. direct attributable outcomes;
6. reward closure and learning feedback.

The figure preserves:
- AHBN-first ordering;
- continuous canonical state versus discrete Q-state key;
- five-action Q-AHBN refinement;
- preserved AHBN proposal;
- requested proposal versus realized forwarding;
- bounded realization `0 <= k_real <= min(k_Q,|N_e|)`;
- NEW/DUPLICATE/FAILED outcomes;
- `F=0` no-reward-bearing-update boundary;
- same-peer future-state learning feedback;
- non-immediate feedback-loop visual grammar.

The retained manuscript label is:
`fig:qahbn-cycle`.

### A1 integration

Algorithm A1 was integrated using `algorithm` + `algpseudocode` and labelled:
`alg:qahbn`.

The integrated algorithm includes:
- zero Q-table initialization for 81 x 5 entries;
- current constants `alpha_Q=0.25`, `gamma=0.70`, `epsilon_0=0.30`, `epsilon_min=0.03`, `lambda_epsilon=0.995`;
- immutable AHBN execution first;
- discrete state construction from the same canonical EWMA snapshot;
- same-peer successor linkage;
- seeded epsilon-greedy action selection;
- five exact bounded transforms;
- bounded eligible-target realization;
- decision-owned direct-attempt attribution;
- NEW/DUPLICATE/FAILED closure;
- `F=0` no numerical reward/no reward-bearing update;
- reward-bearing update only when required information is available;
- terminal zero bootstrap;
- one epsilon decay per learner decision;
- note that multiple decision records may coexist and close independently.

A compact manuscript paragraph now explicitly ties Algorithm A1 to Fig. F1 and states that environment-specific ControlSim/Kubernetes plumbing is intentionally omitted.

### Notation harmonization

The continuous canonical EWMA snapshot is now written:

[
x_t=(hat d_t,hatell_t,hat u_t,hat c_t),
]

while the discrete Q-table key is:

[
s_t=(B(hat d_t),B(hatell_t),B(hat u_t),B(hat c_t)).
]

This is a notation-only harmonization frozen by S16-3. No state semantics changed.

## LaTeX support changes

Added:
- `tikz` with `arrows.meta,positioning,fit,calc`;
- `algorithm`;
- `algpseudocode`;
- small local `\When` / `\EndWhen` commands for readable asynchronous reward-closure pseudocode.

A source-level audit corrected an initial command-escaping issue in the Q-update display before gate closure.

## Scientific non-changes

S16-4 did not:
- alter the pinned science baseline;
- change AHBN or Q-AHBN implementation;
- alter parameters/actions/reward/transition semantics;
- rerun any experiment;
- create new evidence;
- change result values or claims;
- introduce convergence/optimality/superiority language;
- change Kubernetes evidence role;
- change Exp13 positioning.

## Verification

Source audit after integration:
- placeholder F1 removed/replaced — **PASS**;
- `fig:qahbn-cycle` retained — **PASS**;
- six F1 layers present — **PASS**;
- AHBN-first semantics — **PASS**;
- bounded realization relation — **PASS**;
- five actions present — **PASS**;
- direct-attempt outcomes/reward boundary — **PASS**;
- same-peer future state shown — **PASS**;
- A1 label/cross-reference present — **PASS**;
- current alpha/gamma/epsilon constants — **PASS**;
- terminal zero bootstrap — **PASS**;
- notation x_t versus s_t harmonized — **PASS**;
- no scientific result section modified by this gate — **PASS**.

## Gate decision

**S16-4 = PASS / CLOSED.**

The audited mechanism figure and formal algorithm are now integrated into the active manuscript source. Later visual-production audit remains responsible for final rendered typography, float placement, scaling and page-flow judgement.

## Next controlled gate

**S16-5 — Primary Paired Trade-off Figure Specification.**


---

# S16-5 — Primary Paired Trade-off Figure Specification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Freeze the scientific, numerical and visual specification for **F2 — Primary Eight-Condition Paired Trade-off Figure** from the already-frozen S11-A primary RO4 aggregation. This gate specifies F2 only. It does not construct the figure and does not edit `versions/v0.0/main.tex`.

## Authority reconciliation

S16-5 was reconciled against:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- S12/S12A interpretation and claim boundaries;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- current S16 control state through S16-4;
- manuscript `docs/MANUSCRIPT_MASTER.md`, `docs/PROVENANCE.md`, and active `versions/v0.0/main.tex`;
- registered S11-A Drive evidence folder `1XMWn5FWKwJV78YeTGakJb1bVJ6XKfrLH`.

The authoritative numerical source for F2 is:
`s11a_primary_ro4_summary.csv`
Drive file ID: `1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`.

Supporting aggregation/provenance:
- `s11a_primary_ro4_aggregation.json` — Drive ID `1pnw4Bj4USG2ZhqTyUgqW78Y9OggOg0WB`;
- `manifest.json` — Drive ID `1GNXUE5erbj0-diF4DL60nlIJu48awiB7`;
- S11-A comprises 80 formal runs and 40 same-seed AHBN--Q-AHBN pairs.

No new calculation, experiment, statistical family or evidence source is authorized by S16-5.

## F2 scientific question

F2 must answer:

> **Across each of the eight predeclared primary ControlSim conditions, how does Q-AHBN shift the frozen AHBN operating point in delivery, propagation delay, duplicate traffic and forwarding effort, while preserving the paired design and the communication-overhead trade-off?**

F2 is the main visual representation of claim family C03--C06. It is not an omnibus performance score and must not answer “which method wins?”

## Unit of comparison

Every plotted quantity is a condition-specific same-seed paired difference:

[
Delta_i = Q	ext{-}AHBN_i-AHBN_i.
]

F2 plots the **mean paired difference across the five frozen seeds** for each condition.

No cross-condition pooling is permitted.

## Frozen condition order

The x-axis order is fixed by experiment family and protocol:

1. Exp10 control;
2. Exp10 failure;
3. Exp11 churn 0.00;
4. Exp11 churn 0.20;
5. Exp11 churn 0.40;
6. Exp12 balanced;
7. Exp12 moderate heterogeneity;
8. Exp12 weak-heavy.

The Exp10 control and Exp11 churn 0.00 rows have identical frozen numerical values because they instantiate the same undisturbed baseline configuration in their respective experiment families. **Both must remain visible** because F2 represents the eight predeclared experimental conditions rather than deduplicating them post hoc.

Visual grouping should make the three families apparent:
- Failure: 2 conditions;
- Churn: 3 conditions;
- Heterogeneity: 3 conditions.

No visual joining line may imply that all eight conditions form one continuous ordered dose axis.

## Frozen F2 architecture

F2 is a **2 x 2 aligned small-multiple figure** sharing the same eight condition positions:

### Panel (a) — Delivery

Quantity:
[
100	imesDelta	ext{delivery ratio}
]
reported as **percentage-point difference**.

Encoding:
- point estimate = paired mean difference converted to percentage points;
- horizontal/vertical error bar = paired 95% Student-t CI, also converted to percentage points;
- zero reference line mandatory.

Interpretation:
- positive = higher Q-AHBN delivery;
- negative = lower Q-AHBN delivery.

### Panel (b) — Propagation delay

Quantity:
[
Delta	ext{propagation delay}.
]

Encoding:
- point estimate = paired mean difference;
- error bar = paired 95% Student-t CI;
- zero reference line mandatory.

Interpretation:
- negative = lower Q-AHBN delay;
- positive = higher Q-AHBN delay.

Do not invert the sign merely to make “improvement” positive; the plotted quantity must remain the registered Q-AHBN-minus-AHBN difference.

### Panel (c) — Duplicate transmissions

Quantity:
[
Delta	ext{duplicates}.
]

Encoding:
- paired mean difference only;
- zero reference line mandatory;
- **no inferential error bar in F2**.

Interpretation:
- positive = more duplicate transmissions under Q-AHBN;
- negative = fewer duplicates.

The registered S11-A file contains paired uncertainty fields for duplicates, but F2 deliberately uses overhead as the descriptive communication-cost dimension. This avoids visually elevating overhead uncertainty into a new headline inferential family beyond the frozen S12/S12A framing. Exact uncertainty remains available in the registered aggregation and may remain in T2 if retained by S16-12.

### Panel (d) — Total forwards

Quantity:
[
Delta	ext{total forwards}.
]

Encoding:
- paired mean difference only;
- zero reference line mandatory;
- **no inferential error bar in F2**.

Interpretation:
- positive = more forwarding effort under Q-AHBN;
- negative = less forwarding effort.

As with duplicates, F2 uses the overhead metric descriptively; it does not create a new statistical claim family.

## Frozen numerical plotting table

All values below are copied from the registered S11-A summary; no recomputation is required at construction time except delivery-ratio-to-percentage-point scaling.

| Condition | Delivery Δ (pp) | Delivery paired 95% CI (pp) | Delay Δ | Delay paired 95% CI | Duplicate Δ | Forward Δ |
|---|---:|---:|---:|---:|---:|---:|
| Exp10 control | +13.3472 | [+6.3137, +20.3807] | -5.977232 | [-7.978592, -3.975872] | +29,983.2 | +43,330.4 |
| Exp10 failure | +12.9066 | [+7.2732, +18.5400] | -5.832377 | [-7.476635, -4.188118] | +28,798.0 | +41,704.6 |
| Exp11 churn 0.00 | +13.3472 | [+6.3137, +20.3807] | -5.977232 | [-7.978592, -3.975872] | +29,983.2 | +43,330.4 |
| Exp11 churn 0.20 | +6.2944 | [+4.8314, +7.7574] | -3.765746 | [-4.779881, -2.751610] | +16,345.0 | +22,639.4 |
| Exp11 churn 0.40 | +2.3040 | [+0.4980, +4.1100] | -1.198793 | [-2.018132, -0.379453] | +2,944.8 | +5,248.8 |
| Exp12 balanced | +9.3462 | [+3.8045, +14.8879] | -6.875323 | [-8.041421, -5.709225] | +23,313.0 | +32,659.2 |
| Exp12 moderate | +5.7428 | [+1.4762, +10.0094] | -6.541088 | [-8.072779, -5.009396] | +16,042.4 | +21,785.2 |
| Exp12 weak-heavy | +5.8072 | [+2.0600, +9.5544] | -7.813670 | [-11.239517, -4.387823] | +18,496.4 | +24,303.6 |

Construction must use the full registered precision from `s11a_primary_ro4_summary.csv`; the table above is the human-readable specification.

## Visual grammar

F2 must be readable without relying on color.

Required:
- four aligned panels;
- same condition order in all panels;
- clear panel labels (a)--(d);
- explicit zero reference line in every panel;
- family grouping by spacing, separators, brackets or facet-strip-like labels;
- points/markers for paired mean differences;
- error bars only in delivery and delay panels;
- compact condition labels suitable for publication width;
- axis labels containing units/meaning;
- caption explicitly defining `Delta = Q-AHBN - AHBN`.

Preferred publication labels:
- Exp10: Control, Failure;
- Exp11: Churn 0.00, Churn 0.20, Churn 0.40;
- Exp12: Balanced, Moderate, Weak-heavy.

The experiment-family identity must remain visible even if labels are shortened.

## Why paired differences rather than raw method means

F2 is designed around the predeclared paired experiment. Plotting the paired effect:
- directly represents the scientific AHBN--Q-AHBN comparison;
- preserves seed as the blocking factor;
- exposes the zero-effect reference naturally;
- makes favorable direction explicit per metric;
- avoids visually overstating differences through separate raw-mean scales;
- complements rather than duplicates exact method means and tables.

F2 must not use message-level observations or within-run trace points as independent samples.

## Uncertainty authority

For delivery and delay:
- use only the registered paired two-sided 95% Student-t confidence intervals with `df=4`;
- do not substitute method-wise CIs, standard deviations, standard errors, bootstrap intervals, Bayesian intervals or newly computed uncertainty;
- do not pool seeds across conditions.

For duplicates and forwards:
- F2 shows paired mean differences descriptively;
- no F2 error bars;
- do not attach significance markers, stars, p-values or categorical “significant/not significant” labels.

This specification does not deny the registered overhead CIs; it controls their visual role in F2.

## Scientific reading rules

The figure supports the following bounded reading:

1. delivery differences are positive in all eight plotted conditions;
2. delay differences are negative in all eight;
3. registered paired 95% CIs for delivery and delay exclude zero in all eight;
4. duplicate and forward mean differences are positive in all eight;
5. therefore the tested conditions show a repeated shift toward higher delivery/lower delay accompanied by higher mean communication activity;
6. the magnitude is condition-dependent;
7. the churn delivery effect contracts descriptively from churn 0.00 to 0.40.

The figure does **not** establish:
- one pooled primary effect;
- universal superiority;
- improvement in all metrics;
- a composite winner;
- formal monotonic dose-response;
- extrapolation outside the frozen conditions;
- lower communication overhead;
- statistical certainty for overhead merely because its plotted mean is positive;
- convergence or policy optimality.

## F2 versus F3 separation

F2 is the **complete primary trade-off overview** across all eight rows and four primary metrics.

F3, specified later, must not duplicate F2. Its role is to expose **within-family dynamic-stress response and effect variation**, especially:
- control versus one-peer failure;
- descriptive churn attenuation;
- heterogeneity-profile response.

F3 may reorganize frozen primary evidence to answer the stress-response question but may not introduce fitted trends, pooled effects or extrapolation.

## Relationship to current manuscript tables

F2 complements the exact-value authority currently represented by:
- `tab:primary-paired-results`;
- `tab:primary-tradeoff-synthesis`.

S16-5 does **not** remove or edit either table. S16-12 will decide redundancy after F2 exists and is verified.

The intended hierarchy is:
- F2 = visual trade-off pattern and condition-wise effect direction;
- T2 = exact paired numerical/statistical authority;
- any redundant synthesis table = candidate for removal only at S16-12.

## Frozen working caption

> **Primary paired ControlSim trade-off across the eight predeclared conditions.** Points show condition-specific mean paired differences, `Delta = Q-AHBN - AHBN`, across the five matched seeds. Delivery is expressed as percentage-point difference; delivery and propagation-delay error bars are the registered paired 95% Student-t confidence intervals (`df=4`). Duplicate and total-forward panels show paired mean differences descriptively to expose communication-cost direction. Positive delivery and negative delay indicate the Q-AHBN shift toward higher delivery and lower delay, whereas positive duplicate and forward differences indicate greater communication activity. Conditions remain separated by failure, churn and heterogeneity families and are not pooled into an overall effect.

Caption wording may be tightened at S16-6/S16-15 without changing these semantics.

## Construction contract for S16-6

S16-6 must:
1. construct F2 from the registered S11-A summary;
2. independently verify every plotted value against `s11a_primary_ro4_summary.csv`;
3. verify delivery percentage-point conversion;
4. verify delivery/delay CI endpoints;
5. verify condition order/family grouping;
6. verify zero lines and favorable-direction explanations;
7. verify grayscale readability and manuscript-width legibility;
8. record the generated-artifact provenance;
9. avoid editing scientific interpretation beyond directly necessary figure references/caption preparation unless explicitly released by the gate.

## Gate decision

**S16-5 = PASS / CLOSED.**

F2's scientific question, evidence source, condition order, four-panel architecture, uncertainty use, visual grammar, caption scope, permitted interpretation and prohibited interpretation are frozen.

No figure was constructed and `versions/v0.0/main.tex` was not modified under S16-5.

## Next controlled gate

**S16-6 — Primary Trade-off Figure Construction + Verification.**


---

# S16-6 — Primary Trade-off Figure Construction + Verification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Construct and verify **F2 — Primary Eight-Condition Paired Trade-off Figure** exactly from the frozen S16-5 specification and registered S11-A aggregation, without introducing new evidence, new statistics, pooling, or broader manuscript interpretation.

## Construction authority

Primary numerical source:
- `s11a_primary_ro4_summary.csv`
- Drive file ID: `1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`
- registered SHA-256: `9b2d21a103c9cd115acc56a003eb8bab60a49db92bc82af3a8da004d03b33833`

Supporting provenance:
- S11-A aggregation commit: `59ef254099fb3edb617f323dd864324c320d9a85`
- canonical AHBN commit: `936a79480bc1252c79b6ee01f65c88c740af2844`
- 80 formal runs
- 40 same-seed paired comparisons
- frozen seeds 42--46
- Student-t multiplier for paired 95% CI, df=4: `2.7764451051977987`

## Constructed artifact

Working publication outputs:
- `F2_primary_paired_tradeoff.png`
- `F2_primary_paired_tradeoff.pdf`
- `F2_primary_paired_tradeoff_verification.csv`

Working artifact SHA-256 values:
- PNG: `cd8dff98854cc6b3c574c29eb3e16458fdaca1014b0f09915ec6c049968686b3`
- PDF: `8e2113a4c2df3f7234f8d1c05e1cfa9d56ab8da06ad5361c23db43d164b2db3a`
- verification CSV: `add7e31ffa71decfb5fba01bab1350769570481b364c5e55d9710b0f26946c4f`

These are publication working artifacts, not new scientific evidence.

## Visual construction

F2 was constructed as the frozen 2 x 2 aligned small-multiple architecture:

1. **(a) Delivery** — paired mean difference in percentage points with registered paired 95% Student-t CI;
2. **(b) Propagation delay** — paired mean difference with registered paired 95% Student-t CI;
3. **(c) Duplicates** — paired mean difference only;
4. **(d) Total forwards** — paired mean difference only.

All panels:
- use `Delta = Q-AHBN - AHBN`;
- preserve the same eight-condition order;
- contain a zero reference line;
- use family separators between Exp10 / Exp11 / Exp12;
- avoid connecting all conditions as one continuous dose axis;
- remain readable without dependence on color.

## Verified plotted values

| Condition | Delivery Δ (pp) | Delivery 95% CI (pp) | Delay Δ | Delay 95% CI | Duplicate Δ | Forward Δ |
|---|---:|---:|---:|---:|---:|---:|
| Exp10 control | 13.3472 | [6.313727, 20.380673] | -5.977232 | [-7.978592, -3.975872] | 29,983.2 | 43,330.4 |
| Exp10 failure | 12.9066 | [7.273178, 18.540022] | -5.832377 | [-7.476635, -4.188118] | 28,798.0 | 41,704.6 |
| Exp11 churn 0.00 | 13.3472 | [6.313727, 20.380673] | -5.977232 | [-7.978592, -3.975872] | 29,983.2 | 43,330.4 |
| Exp11 churn 0.20 | 6.2944 | [4.831447, 7.757353] | -3.765746 | [-4.779881, -2.751610] | 16,345.0 | 22,639.4 |
| Exp11 churn 0.40 | 2.3040 | [0.497956, 4.110044] | -1.198793 | [-2.018132, -0.379453] | 2,944.8 | 5,248.8 |
| Exp12 balanced | 9.3462 | [3.804499, 14.887901] | -6.875323 | [-8.041421, -5.709225] | 23,313.0 | 32,659.2 |
| Exp12 moderate | 5.7428 | [1.476160, 10.009440] | -6.541088 | [-8.072779, -5.009396] | 16,042.4 | 21,785.2 |
| Exp12 weak-heavy | 5.8072 | [2.059961, 9.554439] | -7.813670 | [-11.239517, -4.387823] | 18,496.4 | 24,303.6 |

The verification export preserves these values directly from the registered summary after only the authorized delivery-ratio-to-percentage-point conversion.

## Verification results

- authoritative S11-A source reconciliation — **PASS**;
- registered source hash/provenance reconciliation — **PASS**;
- eight-condition order — **PASS**;
- Exp10 control retained — **PASS**;
- Exp11 churn 0.00 retained separately — **PASS**;
- delivery percentage-point conversion — **PASS**;
- delivery paired CI endpoints — **PASS**;
- delay paired CI endpoints — **PASS**;
- duplicate paired means — **PASS**;
- total-forward paired means — **PASS**;
- no overhead inferential error bars — **PASS**;
- zero-effect reference in all panels — **PASS**;
- family separators — **PASS**;
- no cross-condition pooling — **PASS**;
- no composite score/ranking — **PASS**;
- no new statistical family — **PASS**;
- grayscale-independent visual encoding — **PASS**;
- working PNG/PDF/CSV hashes recorded — **PASS**.

## Scientific reading audit

The constructed F2 supports only the frozen bounded reading:
- delivery paired means are positive in all eight tested conditions;
- delay paired means are negative in all eight;
- delivery/delay paired 95% CIs exclude zero in all eight;
- duplicate and forward paired means are positive in all eight;
- the resulting pattern is a delivery--latency shift with higher mean communication activity;
- effect magnitude remains condition-dependent.

F2 does not support or imply universal superiority, improvement in all metrics, pooled overall effect, formal dose-response, lower communication overhead, convergence, policy optimality, or extrapolation outside tested conditions.

## Manuscript integration status

S16-6 is construction + verification only. The current active manuscript source is not broadly rewritten at this gate. Final package integration and table rationalization remain controlled by later S16 gates.

## Gate decision

**S16-6 = PASS / CLOSED.**

F2 is constructed and numerically verified against the registered S11-A source. The working figure is publication-ready for later controlled integration, subject to the later whole-package visual/LaTeX production audit.

## Next controlled gate

**S16-7 — Dynamic-Stress Response Figure Specification.**


---

# S16-6A — F2 Native TikZ/PGFPlots Manuscript Integration Amendment

**Status:** PASS / CLOSED — 2026-10-02

## Researcher direction

The researcher explicitly preferred a native TikZ figure in the manuscript rather than retaining PNG/PDF as the publication representation of F2.

This amendment does not reopen S16-5 scientific specification or S16-6 numerical verification. It changes only the manuscript representation of the already-verified F2 artifact.

## Reconciliation

Before editing, the current authoritative state was re-read from:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- S16-5/S16-6 control records;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`.

The pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Manuscript implementation

F2 is now authored directly in:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

using:
- TikZ;
- PGFPlots;
- PGFPlots `groupplots` library.

The manuscript preamble now includes:
- `\usepackage{pgfplots}`;
- `\usepgfplotslibrary{groupplots}`;
- `\pgfplotsset{compat=1.18}`.

The final manuscript figure label is:
`fig:primary-paired-tradeoff`.

## Scientific content retained exactly

The native figure retains the frozen S16-5/S16-6 architecture:
1. delivery paired mean difference in percentage points with registered paired 95% CI;
2. propagation-delay paired mean difference with registered paired 95% CI;
3. duplicate paired mean difference only;
4. total-forward paired mean difference only.

It preserves:
- `Delta = Q-AHBN - AHBN`;
- all eight condition positions;
- Exp10/Exp11/Exp12 family separation;
- paired CI only for delivery/delay;
- descriptive overhead panels without significance markers;
- no pooling or composite score;
- no fitted trend/dose-response implication.

The TikZ/PGFPlots coordinates were transcribed from the already-verified S16-6 values. No new statistic or data transformation was introduced beyond the already-frozen delivery percentage-point conversion.

## Manuscript prose integration

The cross-condition synthesis now references:
`Figure~\ref{fig:primary-paired-tradeoff}`

as the visual trade-off overview.

The existing exact-value tables are intentionally retained pending S16-12 table rationalization.

## Status of prior PNG/PDF outputs

The earlier PNG/PDF remain historical S16-6 construction/verification working artifacts only.

They are no longer the preferred manuscript representation of F2.

The authoritative publication representation is now the native TikZ/PGFPlots source embedded in `versions/v0.0/main.tex`.

## Verification

- native PGFPlots package/library present — **PASS**;
- four-panel groupplot present — **PASS**;
- all eight delivery coordinates present — **PASS**;
- all eight delay coordinates present — **PASS**;
- delivery/delay error bars present — **PASS**;
- overhead panels contain no error bars — **PASS**;
- Exp10/Exp11/Exp12 separators present — **PASS**;
- manuscript label/cross-reference present — **PASS**;
- existing tables retained — **PASS**;
- no science/evidence/claim change — **PASS**.

Final rendered typography and float/page-flow judgment remain assigned to S16-17.

## Gate decision

**S16-6A = PASS / CLOSED.**

S16-6 remains PASS/CLOSED. F2 is now integrated natively in the manuscript as TikZ/PGFPlots.

## Next controlled gate

**S16-7 — Dynamic-Stress Response Figure Specification.**


---

# S16-7 — Dynamic-Stress Response Figure Specification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Freeze the scientific and visual specification for **F3 — Dynamic-Stress Response Figure** using only the already-frozen S11-A primary ControlSim evidence.

F3 must add analytical value beyond F2 by exposing **within-family variation in the Q-AHBN-minus-AHBN delivery and propagation-delay effects** under:
1. failure status;
2. increasing churn;
3. heterogeneous resource profiles.

This gate specifies F3 only. It does not construct the figure and does not edit `versions/v0.0/main.tex`.

## Authority reconciliation

S16-7 was reconciled against:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- S12/S12A interpretation and claim boundaries;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- S16-5/S16-6/S16-6A;
- manuscript `docs/MANUSCRIPT_MASTER.md`, `docs/PROVENANCE.md`, and active `versions/v0.0/main.tex`;
- registered S11-A Drive summary `s11a_primary_ro4_summary.csv`, file ID `1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`.

The pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

No new experiment, aggregation, statistical test, uncertainty family, fitted model or scientific claim is introduced by S16-7.

## F3 reviewer question

F3 must answer:

> **How does the condition-specific Q-AHBN refinement effect on delivery and propagation delay vary within the predeclared failure, churn and heterogeneity stress families?**

This is intentionally different from F2:
- F2 asks for the complete eight-condition **delivery/latency/communication-cost trade-off overview**;
- F3 asks how the two primary effectiveness effects **respond within each dynamic-stress family**.

F3 is therefore an effect-response figure, not a second omnibus trade-off figure.

## Scope of metrics

F3 includes only:
1. delivery paired difference, expressed in percentage points;
2. propagation-delay paired difference, retaining the registered sign.

Duplicates and total forwards are excluded from F3 because:
- their communication-cost direction is already visible in F2;
- exact values remain in T2 pending S16-12 rationalization;
- including all four metrics would substantially duplicate F2 rather than answer the stress-response question.

The F3 caption must explicitly direct the reader to F2/T2 for communication-overhead context.

## Frozen family structure

F3 consists of **three horizontally arranged family panels**:

### Panel (a) — Failure response

Conditions:
- Control;
- One-peer failure.

Purpose:
- show whether the Q-AHBN-minus-AHBN delivery and delay effects materially change between the undisturbed Exp10 control and the predeclared one-peer failure condition.

This is a two-condition contrast only.

No claim of general failure robustness or failure-rate response is permitted.

### Panel (b) — Churn response

Conditions:
- churn 0.00;
- churn 0.20;
- churn 0.40.

Purpose:
- expose the registered descriptive attenuation of the delivery effect as churn rises;
- show the corresponding condition-specific delay effects.

The three observed points may be connected by a thin line **only as a visual guide through the ordered predeclared churn levels**.

Such a line is not a fitted regression, interpolation or dose-response model.

No trend line, regression coefficient, correlation, slope test or extrapolation is permitted.

### Panel (c) — Heterogeneity response

Conditions:
- Balanced;
- Moderate heterogeneity;
- Weak-heavy.

Purpose:
- show how delivery and delay effects differ across the three named resource profiles.

These resource profiles are categorical scenarios, not a validated continuous heterogeneity scale.

Therefore:
- points must **not** be connected by a line;
- no monotonic ordering or dose-response implication is permitted.

## Dual-metric visual architecture

Each family panel uses two vertically aligned sub-axes sharing the family-specific x positions:

**Upper sub-axis — Delivery**
- quantity: `100 x paired_diff_mean(delivery_ratio)`;
- unit: percentage points;
- registered paired 95% Student-t CI;
- zero reference line.

**Lower sub-axis — Propagation delay**
- quantity: paired `Q-AHBN - AHBN` delay difference;
- registered paired 95% Student-t CI;
- zero reference line.

This yields a conceptual **3 columns x 2 metric rows** figure while preserving the reviewer-facing three-family organization.

A six-small-axis implementation is preferred over dual y-axes. Dual y-axes are prohibited because they can obscure the sign and scale distinction between delivery and delay.

## Frozen numerical authority

All plotted values come directly from the registered S11-A summary.

| Family | Condition | Delivery Δ (pp) | Delivery paired 95% CI (pp) | Delay Δ | Delay paired 95% CI |
|---|---|---:|---:|---:|---:|
| Failure | Control | +13.3472 | [+6.313727, +20.380673] | -5.977232 | [-7.978592, -3.975872] |
| Failure | One-peer failure | +12.9066 | [+7.273178, +18.540022] | -5.832377 | [-7.476635, -4.188118] |
| Churn | 0.00 | +13.3472 | [+6.313727, +20.380673] | -5.977232 | [-7.978592, -3.975872] |
| Churn | 0.20 | +6.2944 | [+4.831447, +7.757353] | -3.765746 | [-4.779881, -2.751610] |
| Churn | 0.40 | +2.3040 | [+0.497956, +4.110044] | -1.198793 | [-2.018132, -0.379453] |
| Heterogeneity | Balanced | +9.3462 | [+3.804499, +14.887901] | -6.875323 | [-8.041421, -5.709225] |
| Heterogeneity | Moderate | +5.7428 | [+1.476160, +10.009440] | -6.541088 | [-8.072779, -5.009396] |
| Heterogeneity | Weak-heavy | +5.8072 | [+2.059961, +9.554439] | -7.813670 | [-11.239517, -4.387823] |

Construction must use the full registered precision in `s11a_primary_ro4_summary.csv`.

## Scale policy

Within each metric row, use a **common y-scale across all three family panels**:
- all delivery sub-axes share one delivery scale;
- all delay sub-axes share one delay scale.

This allows condition-to-condition magnitude comparison without panel-specific visual magnification.

The delivery and delay rows do not share a numeric scale with each other.

The zero line must remain visible on every sub-axis.

## Uncertainty policy

F3 uses only the already-registered paired 95% Student-t confidence intervals for delivery and delay.

Required:
- paired CIs only;
- `df=4`;
- five matched seeds per condition;
- no method-wise CI substitution;
- no new bootstrap/SE/SD interval;
- no significance stars;
- no p-values;
- no pooled CI;
- no family-level omnibus test.

All registered delivery/delay CIs exclude zero, but F3 must not convert that observation into a universal or cross-family statistical claim.

## Visual grammar

F3 must be grayscale-safe and native TikZ/PGFPlots when constructed.

Required:
- three family columns labelled **Failure**, **Churn**, **Heterogeneity**;
- delivery row above delay row;
- point estimates with paired 95% CI error bars;
- zero line in every sub-axis;
- shared delivery scale across columns;
- shared delay scale across columns;
- compact condition labels;
- no color-dependent meaning;
- no background decoration or topology graphic;
- no communication-overhead series.

For churn only:
- a thin solid/dashed line may join the three point estimates within each metric row as an ordering guide;
- the caption must state that it is a visual guide and not a fitted trend.

For failure and heterogeneity:
- use unconnected points/error bars.

## F2/F3 non-redundancy contract

F2 and F3 have different publication jobs.

**F2 — trade-off overview**
- eight rows on one common condition axis;
- delivery + delay + duplicates + forwards;
- emphasizes effectiveness versus communication cost;
- answers “what operating-point shift occurs?”

**F3 — stress-response view**
- organized by experimental family;
- delivery + delay only;
- emphasizes within-family effect variation;
- answers “how does the effectiveness shift vary with the tested dynamic condition?”

F3 must not repeat duplicate/forward panels, recreate the F2 eight-condition axis, or introduce an aggregate effectiveness score.

## Permitted scientific reading

F3 may support the following bounded observations:

1. **Failure:** the delivery and delay paired effects are similar in magnitude between the Exp10 control and one-peer failure rows.
2. **Churn:** the delivery effect decreases descriptively from +13.3472 pp at churn 0.00 to +6.2944 pp at 0.20 and +2.3040 pp at 0.40.
3. **Churn:** the magnitude of the negative delay difference also narrows across the three frozen churn levels.
4. **Heterogeneity:** all three profiles retain positive delivery and negative delay effects, but effect magnitudes vary by profile.
5. **Heterogeneity:** the weak-heavy profile has the largest-magnitude negative mean delay difference among the three tested profiles, while its delivery effect is similar to the moderate profile.
6. All statements remain condition-specific and descriptive unless already authorized by the registered paired CIs.

## Prohibited readings

F3 must not claim or visually imply:
- Q-AHBN is failure-proof or universally robust;
- a formal failure-response curve;
- a statistically established monotonic churn dose-response;
- linear/nonlinear churn trend;
- interpolation between churn 0.00, 0.20 and 0.40;
- extrapolation beyond churn 0.40;
- that the three heterogeneity profiles form a continuous severity scale;
- monotonic heterogeneity response;
- cross-family pooling;
- a family-level winner;
- universal superiority;
- convergence or policy optimality;
- communication-cost improvement.

## Working caption

> **Dynamic-stress response of the primary paired ControlSim effects.** Each column isolates one predeclared experiment family: one-peer failure relative to its control, churn at 0.00/0.20/0.40, and the balanced/moderate/weak-heavy resource profiles. The upper row shows Q-AHBN-minus-AHBN delivery differences in percentage points and the lower row shows propagation-delay differences; error bars are the registered paired 95% Student-$t$ confidence intervals across the five matched seeds ($df=4$). The joined churn points are an ordering guide through the three tested churn levels, not a fitted trend or dose-response model. Heterogeneity profiles are categorical and are therefore shown as unconnected effects. Communication-overhead effects are reported separately in Figure F2 and the primary paired-results table.

The final figure number/reference wording will be synchronized during construction/integration.

## Construction contract for S16-8

S16-8 must:
1. construct F3 natively in TikZ/PGFPlots;
2. use only the registered S11-A summary values;
3. independently verify all delivery percentage-point values and CI endpoints;
4. independently verify all delay values and CI endpoints;
5. preserve common delivery scale across family columns;
6. preserve common delay scale across family columns;
7. connect only the ordered churn points, if a connecting guide is retained;
8. keep heterogeneity and failure effects unconnected;
9. verify grayscale readability and manuscript-width legibility;
10. record artifact/manuscript provenance;
11. avoid adding overhead metrics, fitted trends, pooling or new inference.

## Gate decision

**S16-7 = PASS / CLOSED.**

F3's reviewer question, evidence scope, family organization, metric selection, uncertainty use, common-scale policy, visual grammar, permitted readings and prohibited readings are frozen.

No F3 was constructed and `versions/v0.0/main.tex` was not modified under S16-7.

## Next controlled gate

**S16-8 — Dynamic-Stress Figure Construction + Verification.**


---

# S16-7A — F2 Explanatory-Paragraph Integration Amendment

**Status:** PASS / CLOSED — 2026-10-02

## Trigger

The researcher identified that the native F2 figure, `fig:primary-paired-tradeoff`, had a valid caption and a later cross-condition reference but lacked a dedicated explanatory paragraph immediately after the figure.

## Scope

This amendment is editorial/analytical integration only.

It does not reopen:
- S16-5 figure specification;
- S16-6 numerical verification;
- S16-6A TikZ/PGFPlots representation;
- S12/S12A claim boundaries.

## Manuscript change

A dedicated post-figure paragraph was added immediately after `fig:primary-paired-tradeoff` in:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`.

The paragraph:
- explains panels (a)--(d) together;
- states the sign interpretation for delivery and delay;
- notes that the registered paired 95% CIs for delivery/delay remain on the same side of zero in all eight conditions;
- highlights condition dependence, especially churn attenuation;
- explains that duplicate/forward panels represent communication cost;
- explicitly states that the overhead panels are descriptive and do not create a new inferential claim;
- closes with the bounded interpretation: higher delivery/lower delay at greater mean communication activity, not across-the-board improvement or a pooled effect.

No table values, figure coordinates, confidence intervals, or scientific claims were changed.

## Gate decision

**S16-7A = PASS / CLOSED.**

S16-7 remains PASS/CLOSED and S16-8 remains the next released construction gate.


---

# S16-8 — Dynamic-Stress Figure Construction + Verification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Construct and integrate **F3 — Dynamic-Stress Response Figure** directly in native TikZ/PGFPlots from the frozen S16-7 specification and registered S11-A primary ControlSim evidence.

## Authority reconciliation

Before construction, the current authoritative state was re-read from:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- S12/S12A claim boundaries;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- S16-7 and S16-7A;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`;
- registered S11-A Drive summary `s11a_primary_ro4_summary.csv`, file ID `1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`.

The pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Construction

F3 was integrated directly into:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

as a native TikZ/PGFPlots `groupplot` with:
- group size 3 by 2;
- three experimental-family columns;
- delivery row above delay row;
- common delivery scale `0..22` across all three delivery panels;
- common delay scale `-12..0.5` across all three delay panels;
- paired 95% Student-t confidence intervals for every plotted point;
- zero reference line on every sub-axis;
- connected points only for the ordered churn levels;
- unconnected failure and heterogeneity effects.

Figure label:
`fig:dynamic-stress-response`.

## Verified values

All values were transcribed from the registered S11-A summary.

### Failure
- Control delivery: +13.3472 pp, CI [+6.313727,+20.380673]
- One-peer failure delivery: +12.9066 pp, CI [+7.273178,+18.540022]
- Control delay: -5.977232, CI [-7.978592,-3.975872]
- One-peer failure delay: -5.832377, CI [-7.476635,-4.188118]

### Churn
- 0.00 delivery: +13.3472 pp, CI [+6.313727,+20.380673]
- 0.20 delivery: +6.2944 pp, CI [+4.831447,+7.757353]
- 0.40 delivery: +2.3040 pp, CI [+0.497956,+4.110044]
- 0.00 delay: -5.977232, CI [-7.978592,-3.975872]
- 0.20 delay: -3.765746, CI [-4.779881,-2.751610]
- 0.40 delay: -1.198793, CI [-2.018132,-0.379453]

### Heterogeneity
- Balanced delivery: +9.3462 pp, CI [+3.804499,+14.887901]
- Moderate delivery: +5.7428 pp, CI [+1.476160,+10.009440]
- Weak-heavy delivery: +5.8072 pp, CI [+2.059961,+9.554439]
- Balanced delay: -6.875323, CI [-8.041421,-5.709225]
- Moderate delay: -6.541088, CI [-8.072779,-5.009396]
- Weak-heavy delay: -7.813670, CI [-11.239517,-4.387823]

## Manuscript integration

A dedicated explanatory paragraph was inserted immediately after F3.

It:
- distinguishes F3 from the F2 omnibus trade-off view;
- describes the near-similar failure/control effects;
- states the descriptive churn attenuation;
- identifies heterogeneity-profile variation;
- explicitly denies fitted churn-response and continuous heterogeneity-scale interpretation.

The caption also directs communication-overhead interpretation to:
- Figure `fig:primary-paired-tradeoff`;
- Table `tab:primary-paired-results`.

## Verification

- F3 native TikZ/PGFPlots source present — **PASS**;
- 3 x 2 architecture present — **PASS**;
- all failure coordinates and CI widths present — **PASS**;
- all churn coordinates and CI widths present — **PASS**;
- all heterogeneity coordinates and CI widths present — **PASS**;
- common delivery scale across family panels — **PASS**;
- common delay scale across family panels — **PASS**;
- only churn points connected — **PASS**;
- failure effects unconnected — **PASS**;
- heterogeneity effects unconnected — **PASS**;
- zero reference lines present — **PASS**;
- explanatory paragraph present — **PASS**;
- no overhead series in F3 — **PASS**;
- no fitted model, pooling or new inferential family — **PASS**;
- existing F2 source preserved — **PASS**.

Final rendered typography/spacing remains subject to the later S16-17 visual/LaTeX production audit.

## Gate decision

**S16-8 = PASS / CLOSED.**

F3 is now constructed, numerically verified and integrated directly in the manuscript as native TikZ/PGFPlots.

## Next controlled gate

**S16-9 — Exp13 Bounded Positioning Figure Specification.**


---

# S16-9 — Exp13 Bounded Positioning Figure Specification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Freeze the scientific and visual specification for **F4 — Exp13 Bounded Five-Method Positioning Figure** using only the frozen S11-B Exp13-Q ControlSim benchmark.

F4 must show how Gossip, Structured, DC-SoC, AHBN and Q-AHBN occupy different operating points at the single predeclared churn=0.40 benchmark without converting that benchmark into an overall ranking, winner claim or primary RO4 proof.

This gate specifies F4 only. It does not construct the figure and does not edit `versions/v0.0/main.tex`.

## Authority reconciliation

S16-9 was reconciled against:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/stages/S11_AGGREGATION.md`;
- `docs/stages/S12_INTERPRETATION.md`;
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- S16-0 through S16-8 control records;
- manuscript `docs/MANUSCRIPT_MASTER.md`, `docs/PROVENANCE.md`, and active `versions/v0.0/main.tex`;
- frozen S11-B Drive folder `1frfPsofGtbvpRFCxFMjGi_EZUuv8tNxx`;
- frozen S11-B summary `s11b_exp13q_summary.csv`, Drive file ID `1QGHZCa1tR3G4f0nUGlVcPjWNexGZhf76`.

The pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

No new experiment, aggregation, statistical test or claim is introduced.

## Evidence role

Exp13-Q remains:
- 25/25 frozen ControlSim runs;
- five methods;
- seeds 42--46;
- one churn condition only: 0.40;
- external-reference positioning evidence only;
- separate from the S11-A primary RO4/RQ4 evidence.

F4 therefore must not be presented as:
- the main causal comparison;
- an omnibus benchmark;
- a method leaderboard;
- evidence of general superiority over Gossip, Structured or DC-SoC.

## F4 reviewer question

F4 must answer:

> **At the single frozen churn=0.40 ControlSim benchmark, where do Q-AHBN and AHBN sit relative to Gossip, Structured and DC-SoC across delivery, propagation delay and communication-cost metrics?**

The purpose is **bounded positioning within a multi-metric trade-off**, not selection of a best method.

## Frozen figure architecture

F4 uses a **2 x 2 small-multiple figure**, one panel per metric:

1. **Delivery ratio**
2. **Propagation delay**
3. **Duplicate transmissions**
4. **Total forwards**

Each panel shows the same five methods in the same fixed order:

1. Gossip
2. Structured
3. DC-SoC
4. AHBN
5. Q-AHBN

The order is methodological/reference order and must remain fixed across all panels.

Methods must not be sorted by metric value.

## Plot form

Preferred form: **point-and-interval plot** for each metric.

For each method:
- point = five-seed arithmetic mean;
- error bar = descriptive two-sided 95% Student-t CI for that method mean, `df=4`.

This is preferable to bars because:
- it emphasizes operating-point location rather than magnitude-as-ranking;
- it exposes uncertainty without creating a leaderboard visual;
- it remains compact and grayscale-safe;
- it keeps exact numerical authority in T5.

No paired-difference error bars are used for the external methods.

## Statistical boundary

The F4 intervals are **per-method descriptive 95% confidence intervals**, not a new family of pairwise significance tests.

Required:
- n=5 per method;
- arithmetic mean;
- sample-SD based two-sided 95% Student-t CI;
- `df=4`;
- no p-values;
- no significance stars;
- no pairwise test annotations;
- no multiple-comparison procedure;
- no omnibus test;
- no derived winner labels.

AHBN-vs-Q-AHBN paired Exp13 contrasts may remain part of the S11-B evidence record, but F4 is not designed as a paired-difference inferential figure.

## Frozen numerical authority

All values come directly from `s11b_exp13q_summary.csv`.

### Delivery ratio

| Method | Mean | 95% CI |
|---|---:|---:|
| Gossip | 0.916300 | [0.914036, 0.918564] |
| Structured | 0.920000 | [0.920000, 0.920000] |
| DC-SoC | 0.920000 | [0.920000, 0.920000] |
| AHBN | 0.798664 | [0.766549, 0.830779] |
| Q-AHBN | 0.821704 | [0.786368, 0.857040] |

### Propagation delay

| Method | Mean | 95% CI |
|---|---:|---:|
| Gossip | 3.420314 | [3.296321, 3.544307] |
| Structured | 4.489333 | [4.486088, 4.492579] |
| DC-SoC | 1.505306 | [0.939534, 2.071077] |
| AHBN | 10.063965 | [9.287946, 10.839983] |
| Q-AHBN | 8.865172 | [8.505423, 9.224921] |

### Duplicate transmissions

| Method | Mean | 95% CI |
|---|---:|---:|
| Gossip | 327220.0 | [324606.010, 329833.990] |
| Structured | 0.0 | [0.0, 0.0] |
| DC-SoC | 0.0 | [0.0, 0.0] |
| AHBN | 140033.8 | [131495.870, 148571.730] |
| Q-AHBN | 142978.6 | [132197.983, 153759.217] |

### Total forwards

| Method | Mean | 95% CI |
|---|---:|---:|
| Gossip | 417850.0 | [415057.291, 420642.709] |
| Structured | 91000.0 | [91000.0, 91000.0] |
| DC-SoC | 91000.0 | [91000.0, 91000.0] |
| AHBN | 218900.2 | [207457.526, 230342.874] |
| Q-AHBN | 224149.0 | [209942.837, 238355.163] |

Construction must use the full registered precision from the frozen CSV.

## Scale and axis policy

Each metric has its own scientifically natural scale.

Required:
- delivery axis remains in raw ratio units, not percentage points;
- delay remains in the ControlSim propagation-delay units used by the manuscript;
- duplicates and forwards remain absolute counts;
- no metric is sign-inverted;
- no z-score, normalization, min-max scaling or composite score;
- zero baseline should remain visible for duplicates and forwards;
- delivery/delay axes should be chosen to preserve legibility without implying a shared cross-metric scale.

Axes across panels are not numerically comparable to one another.

## Visual grammar

F4 must be grayscale-safe and, when constructed, native TikZ/PGFPlots.

Required:
- 2 x 2 aligned panels;
- same fixed method order in every panel;
- point estimates plus descriptive 95% CI;
- clear metric units;
- compact method labels;
- no color-dependent meaning;
- no arrows saying “better” or “worse”;
- no gold/bold “winner” method;
- no ranking numerals;
- no method reordered by performance;
- no shaded dominance region;
- no radar chart;
- no spider chart;
- no parallel-coordinate aggregate;
- no composite efficiency score.

A subtle typographic distinction may identify AHBN and Q-AHBN as the study methods, but it must not imply superiority. If used, that distinction must remain grayscale-safe and symmetric between the two.

## Scientific reading rules

F4 may support these bounded descriptive statements:

1. At churn=0.40, Q-AHBN has higher mean delivery and lower mean propagation delay than AHBN.
2. Q-AHBN and AHBN occupy similar intermediate communication-cost regions relative to the zero-duplicate Structured/DC-SoC references and the much higher-cost Gossip reference.
3. Gossip, Structured, DC-SoC, AHBN and Q-AHBN occupy different metric-specific operating points rather than a single common ordering.
4. Structured and DC-SoC have the same mean delivery, duplicate count and forward count in this benchmark but differ in propagation delay.
5. Gossip has higher mean delivery than AHBN/Q-AHBN but also markedly higher duplicate and forward counts.
6. The benchmark illustrates trade-off positioning at one fixed high-churn condition.

F4 does not by itself establish pairwise statistical superiority among all five methods.

## Prohibited readings

F4 must not claim or visually imply:
- Q-AHBN is the best method;
- AHBN or Q-AHBN wins overall;
- any global ranking of the five methods;
- dominance across all four metrics;
- state-of-the-art superiority;
- general external-baseline superiority;
- general churn robustness;
- results beyond churn=0.40;
- Exp13 as primary RO4 causal evidence;
- pooled effect with S11-A;
- statistical significance between arbitrary external-method pairs;
- a composite performance/efficiency score.

## Relationship to T5

F4 and T5 have complementary roles.

**F4**
- visual operating-point positioning;
- metric-by-metric comparison;
- descriptive uncertainty;
- no ranking.

**T5**
- exact five-method numerical authority;
- exact means and, after S16-11/S16-12 rationalization if retained, exact interval values as appropriate.

The existing `tab:exp13-results` is the current precursor to T5 and is not removed or restructured during S16-9.

## Relationship to F2/F3

F4 is scientifically separate from F2/F3.

- F2 = primary eight-condition AHBN-vs-Q-AHBN trade-off.
- F3 = within-family response of that primary paired effect.
- F4 = one-condition, five-method external positioning.

F4 must never be visually blended with F2/F3 in a way that suggests a single pooled evidence family.

## Working caption

> **Bounded five-method ControlSim positioning at churn 0.40.** Points show five-seed method means and error bars show descriptive 95% Student-$t$ confidence intervals ($df=4$) for delivery ratio, propagation delay, duplicate transmissions and total forwards. The five methods are shown in a fixed reference order rather than ranked by performance. The panels therefore depict metric-specific operating points at one predeclared high-churn benchmark: AHBN and Q-AHBN occupy intermediate communication-cost regions, Gossip operates at substantially higher duplicate/forwarding activity, and Structured/DC-SoC occupy zero-duplicate lower-forward regions while differing in delay. The figure is bounded external positioning only and does not define an overall winner or generalize beyond churn 0.40.

## Construction contract for S16-10

S16-10 must:
1. construct F4 directly as native TikZ/PGFPlots;
2. use only `s11b_exp13q_summary.csv`;
3. independently verify all 20 mean values;
4. independently verify all 20 CI endpoint pairs;
5. preserve fixed method order across all four panels;
6. use point-and-interval representation;
7. keep metric scales separate and natural;
8. avoid sorting/ranking/winner emphasis;
9. keep F4 visually separate from F2/F3 evidence roles;
10. integrate a dedicated figure-specific explanatory paragraph;
11. preserve existing T5 precursor table pending later table rationalization;
12. record provenance and perform repository readback before closure.

## Gate decision

**S16-9 = PASS / CLOSED.**

F4's reviewer question, evidence role, four-panel architecture, fixed method order, descriptive uncertainty, visual grammar, scientific reading rules and anti-ranking boundaries are frozen.

No F4 was constructed and `versions/v0.0/main.tex` was not modified under S16-9.

## Next controlled gate

**S16-10 — Exp13 Figure Construction + Verification.**


---

# S16-10 — Exp13 Figure Construction + Verification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Construct and integrate **F4 — Exp13 Bounded Five-Method Positioning Figure** directly in native TikZ/PGFPlots from the frozen S16-9 specification and registered S11-B Exp13-Q evidence.

## Authority reconciliation

Before construction, the current authoritative state was re-read from:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/stages/S11_AGGREGATION.md`;
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- S16-9;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`;
- frozen S11-B summary `s11b_exp13q_summary.csv`, Drive file ID `1QGHZCa1tR3G4f0nUGlVcPjWNexGZhf76`.

The pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Construction

F4 was integrated directly into:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

as a native TikZ/PGFPlots 2 x 2 point-and-interval figure.

Figure label:
`fig:exp13-bounded-positioning`.

Panels:
1. delivery ratio;
2. propagation delay;
3. duplicate transmissions;
4. total forwards.

Fixed method order in all panels:
1. Gossip;
2. Structured;
3. DC-SoC;
4. AHBN;
5. Q-AHBN.

## Numerical verification

All 20 five-method means were transcribed from `s11b_exp13q_summary.csv`.

The plotted error-bar half widths were calculated only from the frozen registered CI endpoints:
`halfwidth = ci95_high - mean = mean - ci95_low`.

### Delivery
- Gossip 0.916300 +/- 0.002264122
- Structured 0.920000 +/- 0
- DC-SoC 0.920000 +/- 0
- AHBN 0.798664 +/- 0.032115405
- Q-AHBN 0.821704 +/- 0.035336179

### Delay
- Gossip 3.420313942 +/- 0.123992615
- Structured 4.489333441 +/- 0.003245495
- DC-SoC 1.505305601 +/- 0.565771579
- AHBN 10.063964653 +/- 0.776018311
- Q-AHBN 8.865171996 +/- 0.359748174

### Duplicates
- Gossip 327220.0 +/- 2613.990259
- Structured 0 +/- 0
- DC-SoC 0 +/- 0
- AHBN 140033.8 +/- 8537.930459
- Q-AHBN 142978.6 +/- 10780.616708

### Total forwards
- Gossip 417850.0 +/- 2792.709084
- Structured 91000.0 +/- 0
- DC-SoC 91000.0 +/- 0
- AHBN 218900.2 +/- 11442.673780
- Q-AHBN 224149.0 +/- 14206.163256

No new statistical interval was computed. The PGFPlots half-width representation is a transcription of the already-registered two-sided S11-B confidence intervals.

## Manuscript integration

F4 was placed inside the Exp13 results subsection before the existing exact-value table.

A dedicated explanatory paragraph now follows F4 and states:
- Q-AHBN has higher mean delivery and lower mean delay than AHBN at this one benchmark;
- AHBN/Q-AHBN occupy intermediate communication-cost regions;
- Gossip occupies a higher duplicate/forward operating point;
- Structured/DC-SoC share delivery, duplicate and forward means here but differ in delay;
- the figure is descriptive external positioning only;
- it does not define a best method, add arbitrary pairwise significance tests, or generalize beyond churn=0.40.

The existing `tab:exp13-results` was preserved unchanged as the exact-value precursor to T5.

## Verification

- F4 native TikZ/PGFPlots source present — **PASS**;
- 2 x 2 architecture present — **PASS**;
- fixed five-method order preserved in all panels — **PASS**;
- 20 means verified against frozen S11-B CSV — **PASS**;
- 20 registered CI pairs represented through corresponding explicit half widths — **PASS**;
- no method sorting — **PASS**;
- no winner/ranking annotation — **PASS**;
- no composite normalization or score — **PASS**;
- natural metric scales retained — **PASS**;
- duplicate/forward zero baselines visible — **PASS**;
- dedicated explanatory paragraph present — **PASS**;
- existing Exp13 exact-value table retained — **PASS**;
- no pooling with S11-A or F2/F3 — **PASS**;
- no new inference — **PASS**.

Final rendered typography/spacing remains assigned to the later S16-17 visual/LaTeX production audit.

## Gate decision

**S16-10 = PASS / CLOSED.**

F4 is now constructed, numerically verified, integrated and bounded to its registered one-condition external-positioning role.

## Next controlled gate

**S16-11 — Learning-Evidence Table Rationalization.**


---

# S16-11 — Learning-Evidence Table Rationalization

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Rationalize **T1 — Learning-Mechanism Evidence Table** so it carries distinct evidential value beyond F1/A1 and the surrounding learning-behaviour prose, while remaining strictly inside the frozen S12/S12A learning-mechanism claim boundary.

## Authority reconciliation

Before editing, the current authoritative state was re-read from:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/stages/S12_INTERPRETATION.md`;
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- `docs/stages/S11_AGGREGATION.md`;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`.

The pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Audit of pre-rationalization T1

The previous table was scientifically safe but publication-weak because it:
- repeated nearby prose almost verbatim;
- mixed qualitative observations, exact anchors and claim boundaries in one two-column list;
- did not distinguish evidence class from scientific interpretation;
- did not show why each trace feature matters;
- risked reading as a checklist rather than a mechanism-evidence table.

No numerical defect was found.

## Rationalization decision

T1 is retained, but its role is changed from a generic evidence checklist to a structured:

**evidence class -> frozen observation -> scientific role / claim boundary**

table.

This makes T1 complementary to:
- F1: conceptual architecture/information flow;
- A1: executable bounded-learning semantics;
- surrounding prose: narrative interpretation.

T1 now answers:
> What concrete trace evidence shows that the learning layer was active, and what claim does each observation legitimately support?

## Frozen evidence retained

T1 retains only evidence already frozen by S12/S12A:
- repeated reward-bearing Q updates;
- non-zero state-action use;
- coverage anchor 0.142 at churn 0.40;
- heterogeneity coverage range 0.106--0.111;
- repeated bounded interventions above preserved AHBN proposals;
- coexistence of KEEP decisions with interventions;
- negative mean reward under the frozen reward definition;
- trace retention of AHBN proposal, selected Q action, requested Q proposal, realized forwarding and attributable outcomes.

No new exact update count, intervention count, action-frequency count or reward statistic was introduced because those exact values are not part of the presently frozen publication-facing claim record being rationalized here.

## New T1 structure

The table is now a `table*` with three columns:
1. Evidence class
2. Frozen observation
3. Scientific role / claim boundary

Rows:
- Reward-bearing updates
- State--action use
- Bounded interventions
- Reward behaviour
- Traceability
- Overall inference

## Claim discipline

T1 explicitly supports:
- active learning;
- outcome-driven updating;
- bounded interventions above AHBN;
- condition-dependent state/action use;
- reconstructable decision/outcome traceability.

T1 explicitly does **not** support:
- Q-table convergence;
- policy optimality;
- universal performance benefit;
- method superiority;
- reward-sign-as-success/failure classification.

## Manuscript change

Updated:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

Table label remains:
`tab:learning-mechanism`.

The label is preserved to avoid unnecessary reference churn.

## Gate decision

**S16-11 = PASS / CLOSED.**

T1 is now rationalized as a reviewer-facing mechanism-evidence table with explicit observation-to-claim mapping and no new scientific evidence.

## Next controlled gate

**S16-12 — Primary Statistical Table Rationalization.**


---

# S16-12 — Primary Statistical Table Rationalization

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Rationalize **T2 — Primary Paired Statistical Results Table** so it serves as the single exact numerical companion to F2/F3 without retaining two near-duplicate eight-condition tables.

## Authority reconciliation

Before editing, the current authoritative state was re-read from:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/stages/S11_AGGREGATION.md`;
- `docs/stages/S12_INTERPRETATION.md`;
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/04_STATISTICAL_CONTRACT.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- S16-5 through S16-8;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`;
- registered S11-A Drive summary `s11a_primary_ro4_summary.csv`, file ID `1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`.

Pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Audit finding

Two tables were redundant:
- `tab:primary-paired-results`;
- `tab:primary-tradeoff-synthesis`.

Both contained the same eight conditions and the same four paired effects, differing mainly in delivery scaling/rounding and caption wording.

Keeping both created:
- numerical duplication;
- excess manuscript length;
- risk of inconsistent rounding;
- unnecessary reviewer navigation burden.

## Rationalization decision

The two tables are consolidated into one authoritative T2 under the preserved label:
`tab:primary-paired-results`.

The old `tab:primary-tradeoff-synthesis` table is removed.

T2 now retains:
1. condition;
2. delivery paired mean difference in percentage points;
3. registered delivery paired 95% Student-t CI;
4. propagation-delay paired mean difference;
5. registered delay paired 95% Student-t CI;
6. duplicate paired mean difference;
7. total-forward paired mean difference.

This preserves the full trade-off while assigning inference only to the two metrics for which F2/F3 already use the registered paired intervals.

## Statistical boundary

T2 uses the frozen S11-A same-seed paired design:
- five matched seeds per condition;
- `Delta = Q-AHBN - AHBN`;
- delivery reported in percentage points;
- two-sided paired 95% Student-t CIs for delivery and delay;
- `df=4`.

Duplicate and total-forward columns remain paired mean differences only in T2.

No duplicate/forward CIs, p-values, significance stars, pooled estimate or new inferential family were added during rationalization.

## Numerical authority

All T2 values were reconciled against:
`s11a_primary_ro4_summary.csv`.

The eight frozen rows remain:
- Exp10 control;
- Exp10 failure;
- Exp11 churn 0.00;
- Exp11 churn 0.20;
- Exp11 churn 0.40;
- Exp12 balanced;
- Exp12 moderate;
- Exp12 weak-heavy.

## Manuscript integration

Updated:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`.

The cross-condition synthesis now references only:
`Table~\\ref{tab:primary-paired-results}`.

The prose was updated to describe T2 as the consolidated numerical record containing:
- condition-specific paired estimates;
- registered delivery/delay confidence intervals;
- descriptive communication-overhead differences.

## Artifact hierarchy after rationalization

- F2: all-eight-condition visual trade-off overview.
- F3: within-family delivery/delay effect variation.
- T2: exact consolidated numerical authority for the primary paired evidence.

This removes duplication while preserving complementarity.

## Gate decision

**S16-12 = PASS / CLOSED.**

T2 is now a single consolidated primary statistical table; the redundant synthesis table has been removed without loss of frozen evidence.

## Next controlled gate

**S16-13 — Kubernetes Evidence and Accounting Table Rationalization.**


---

# S16-13 — Kubernetes Evidence and Accounting Table Rationalization

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Rationalize **T3 — Kubernetes Evidence and Accounting Table** so the cloud-native evidence is presented as one coherent operational-realization artifact rather than two partially overlapping tables.

## Authority reconciliation

Before editing, the current authoritative state was re-read from:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/stages/S12_INTERPRETATION.md`;
- `docs/stages/S12A_CLAIM_RECONCILIATION.md`;
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`;
- `docs/06_RESULTS_REGISTER.md`;
- S16 control records through S16-12;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`.

Pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Audit finding

The manuscript previously carried two Kubernetes tables:
- `tab:kubernetes-accounting` — AHBN/Q-AHBN `total_forwards` vs `F_attempt`;
- `tab:kubernetes-results` — five-method Kubernetes means.

These tables belong to the same evidentiary package but were separated in a way that:
- duplicated the AHBN/Q-AHBN forwarding values;
- forced the reader to reconcile runtime-accounting context across two tables;
- made the very low Q-AHBN `total_forwards` value visually easier to detach from the higher attributable-attempt count.

## Rationalization decision

The two tables are consolidated into one authoritative T3 under the preserved label:
`tab:kubernetes-results`.

The old `tab:kubernetes-accounting` table is removed.

T3 now contains:
1. Method
2. Delivery mean
3. Delay mean (s)
4. Duplicate mean
5. `total_forwards` mean
6. `F_attempt` mean where applicable

`F_attempt` is populated only for:
- AHBN: 1,448.0
- Q-AHBN: 2,345.4

External methods use “--” because the frozen accounting caveat is specifically an AHBN/Q-AHBN runtime-accounting comparison.

## Evidence-role boundary

T3 remains operational-realization evidence only.

The surrounding manuscript prose retains the same-seed AHBN-vs-Q-AHBN paired differences and registered 95% CIs:
- delivery +0.132700, CI [-0.254409,+0.519810];
- delay +0.014968 s, CI [-0.029801,+0.059737];
- duplicates +262.2, CI [-441.9,+966.3];
- `total_forwards` -988.6, CI [-2022.75,+45.55].

All four intervals cross zero and seed-level directions vary.

Therefore T3 must not be interpreted as:
- independent confirmation of ControlSim performance gains;
- Kubernetes superiority evidence;
- literal replication of ControlSim;
- generic low-overhead evidence.

## Accounting boundary

The table caption explicitly preserves the distinction:
- `total_forwards` = one runtime accounting view;
- `F_attempt` = attributable forwarding-attempt accounting for the AHBN/Q-AHBN contrast.

The very low Q-AHBN `total_forwards` mean of 10.0 is therefore shown adjacent to `F_attempt=2345.4`, preventing an isolated “fewer sends” interpretation.

## Manuscript integration

Updated:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`.

The Kubernetes subsection now states that:
`Table~\\ref{tab:kubernetes-results}`
consolidates the five-method means and AHBN/Q-AHBN forwarding-accounting context.

All references to `tab:kubernetes-accounting` were removed.

## Gate decision

**S16-13 = PASS / CLOSED.**

T3 is now one consolidated Kubernetes operational-realization/accounting table with the accounting caveat structurally embedded.

## Next controlled gate

**S16-14 — Gamma Sensitivity Figure Specification.**


---

# S16-13A — Kubernetes Forwarding-Accounting Semantics Audit

**Status:** PASS / CLOSED — 2026-10-02

**Classification:** read-only implementation/evidence audit; no new experiment, no result recomputation, no algorithm change.

## Trigger

Post-S16-13 reviewer-readability review identified that the frozen Kubernetes Q-AHBN mean `total_forwards=10.0` required exact code-level semantic explanation before proceeding to S16-14.

## Code-level finding

Authoritative Kubernetes validator:
`gke/app/k7_exp11_tools.py`

It defines:
- `attempts = [event == "k7_forward_attempt"]`;
- `fwd = [event == "forward"]`;
- `F_attempt = len(attempts)`;
- `F_success = len(fwd)`;
- `total_forwards = len(fwd)`.

Authoritative Q-AHBN runtime:
`gke/app/qahbn2_runtime.py`

For every call to the forwarding wrapper it first emits:
`event="k7_forward_attempt"`.

For a Q-AHBN decision-bound attempt, the Q-AHBN-specific branch then performs the RPC and records exactly one attributable outcome:
- `NEW`;
- `DUPLICATE`;
- `FAILED`.

On `resp.ok` / `NEW`, the Q-AHBN branch increments `self.forward_count` but does **not** emit the inherited generic `event="forward"`.

The inherited generic forward path is invoked for Q-AHBN only when no Q decision ID is bound for the message (fallback path).

## Meaning of the frozen value 10.0

The frozen Q-AHBN Kubernetes `total_forwards=10.0` is therefore the mean count of generic `forward` log events observed by the validator.

It is **not** a complete or comparable count of successful Q-AHBN forwarding activity, because successful decision-bound Q-AHBN forwards are represented by `qahbn2_attempt_outcome=NEW` and an internal `forward_count` increment rather than a generic `forward` event.

The audit does not infer that all 10 generic events necessarily have one specific causal origin without raw-event classification; the code establishes that the Q-AHBN fallback original-forward path can emit them.

## Meaning of F_attempt

`F_attempt` is directly defined by the validator as the number of `k7_forward_attempt` events.

Frozen means:
- AHBN: 1448.0
- Q-AHBN: 2345.4

Thus `F_attempt` is the trace-comparable initiated-attempt quantity available for the AHBN/Q-AHBN accounting caution.

## Scientific consequence

No frozen raw result is changed.

However, `total_forwards` must no longer be described as a directly comparable successful-forwarding quantity for Q-AHBN in Kubernetes.

Permitted:
- report the frozen value with explicit instrumentation qualification;
- use it as evidence of the runtime accounting mismatch;
- use `F_attempt` to demonstrate that the low `total_forwards` value does not establish low forwarding effort.

Prohibited:
- Q-AHBN sent only 10 messages/forwards;
- Q-AHBN reduced Kubernetes forwarding by ~99%;
- `total_forwards` proves low overhead;
- direct AHBN-vs-Q-AHBN successful-forward comparison using this field.

## Manuscript correction

The T3 caption, Kubernetes results paragraph and communication-overhead discussion were amended to state the exact instrumentation semantics.

This is an explanatory correction only:
- no raw evidence changed;
- no CI changed;
- no experiment rerun;
- no performance claim added.

## Gate decision

**S16-13A = PASS / CLOSED.**

S16-13 remains PASS/CLOSED with the stronger accounting qualification.

## Next controlled gate

**S16-14 — Gamma Sensitivity Figure Specification.**


---

# S16-14 — Gamma Sensitivity Figure Specification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Freeze the scientific and visual specification for **F5 — Gamma Sensitivity Figure** before construction.

No figure is constructed at this gate.

## Authority reconciliation

S16-14 was reconciled after S16-13A against:
- `docs/00_QAHBN2_MASTER.md`;
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`;
- `docs/02_QAHBN2_DESIGN_FREEZE.md`, especially AR-1.4.2--AR-1.4.4;
- `docs/06_RESULTS_REGISTER.md`;
- S12/S12A claim boundaries;
- manuscript `docs/MANUSCRIPT_MASTER.md`;
- manuscript `docs/PROVENANCE.md`;
- active `versions/v0.0/main.tex`.

Pinned science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Frozen evidence

AR-1.4.2 Learning Validation:
- ControlSim;
- stationary 1,000-message workload;
- BA(100,m=3), source 0;
- base delay 1.0, jitter 0.2;
- four static clusters;
- no failure, churn or resource disturbance;
- gamma candidates exactly {0.70,0.80,0.90};
- seeds exactly {42,43,44,45,46};
- 15/15 runs;
- same seed set for every gamma;
- alpha_Q=0.25;
- epsilon_0=0.30;
- epsilon_min=0.03;
- epsilon_decay=0.995.

AR-1.4.3 verified evidence integrity.

AR-1.4.4 selected and researcher-approved gamma=0.70 for subsequent evaluation.

## Reviewer-facing question

F5 must answer:

> Across the three predeclared discount-factor candidates in the bounded stationary Learning Validation workload, what learning/dissemination trade-off supported freezing gamma=0.70 for subsequent Q-AHBN evaluation?

It must **not** answer:
- which gamma is globally optimal;
- which gamma converges best;
- which gamma is universally superior;
- how gamma behaves under the later failure/churn/heterogeneity experiments.

## Figure architecture

F5 shall be one native manuscript figure with a **2 x 2 panel layout**.

Common x-axis in every panel:
- gamma = 0.70, 0.80, 0.90;
- categorical candidate positions in ascending numerical order;
- no fitted trend or extrapolation outside the three tested values.

### Panel (a) — Mean reward
Five-seed descriptive mean:
- gamma 0.70: -0.264444
- gamma 0.80: -0.268304
- gamma 0.90: -0.268232

Role:
- learning-behaviour selection evidence;
- visually expose that differences are small;
- no convergence interpretation.

### Panel (b) — Delivery ratio
Five-seed descriptive mean:
- gamma 0.70: 0.86552
- gamma 0.80: 0.86181
- gamma 0.90: 0.85597

Role:
- productive dissemination component of the selection trade-off.

### Panel (c) — Propagation delay
Five-seed descriptive mean:
- gamma 0.70: 10.05872
- gamma 0.80: 10.07401
- gamma 0.90: 10.16041

Role:
- latency component of the selection trade-off.

### Panel (d) — Total forwards
Five-seed descriptive mean:
- gamma 0.70: 226189.6
- gamma 0.80: 225464.6
- gamma 0.90: 222940.0

Role:
- communication-effort counterweight;
- make explicit that gamma=0.70 was not selected because it minimized every metric.

## Why duplicates are not a fifth panel

Frozen duplicate means:
- gamma 0.70: 140637.4
- gamma 0.80: 140283.4
- gamma 0.90: 138342.6.

They carry the same qualitative trade-off direction as total forwards in this bounded matrix. A fifth panel would add visual density without changing the selection interpretation.

Duplicates remain eligible for:
- T4 if retained at S16-14B;
- exact prose/table reporting;
- the caption's trade-off qualification.

No scientific evidence is discarded.

## Uncertainty/statistical treatment

F5 is **descriptive parameter-selection provenance**, not a new inferential analysis.

Therefore:
- plot the registered five-seed means only;
- do not invent confidence intervals, standard errors, p-values or significance stars;
- do not add post-hoc pairwise tests;
- do not pool this sensitivity matrix with S11-A or Exp13;
- do not construct a composite score.

The existing paired-seed directional evidence may be stated in the accompanying text/caption:
- gamma=0.70 higher mean reward than gamma=0.80 on 4/5 seeds and gamma=0.90 on 4/5;
- gamma=0.70 higher delivery than each alternative on 4/5 seeds;
- gamma=0.70 lower delay than gamma=0.90 on 5/5 seeds;
- gamma=0.90 lower duplicates and forwards than gamma=0.70 on 4/5 seeds.

These are frozen descriptive direction checks, not significance tests.

## Visual semantics

- gamma=0.70 may be identified as the **selected/frozen candidate**, but must not be styled or labelled as “best”, “optimal”, or “winner”.
- All three candidates receive equal candidate status in axes and data marks.
- The figure must make the overhead counter-trade-off visible in panel (d).
- No arrows implying monotonic optimization.
- No convergence curve.
- No stabilization curve.
- No dynamic-condition labels.

## Exact-values authority

F5 is a visual synthesis, not the sole numerical authority.

The exact AR-1.4.4 descriptive means remain authoritative in the frozen design record.

S16-14B will decide whether **T4 — Compact Gamma-Sensitivity Table/Callout** is needed for exact-value retention in the manuscript or whether the figure plus prose is sufficient.

## Frozen caption contract

> **Figure F5. Bounded discount-factor sensitivity used to freeze the Q-AHBN discount factor.** Five-seed descriptive means are shown for the predeclared ControlSim Learning Validation candidates gamma in {0.70,0.80,0.90} under one stationary 1,000-message workload. Panels report (a) mean reward, (b) delivery ratio, (c) propagation delay and (d) total forwarding effort. Gamma=0.70 was subsequently frozen for formal evaluation after the controlled paired-seed review: it retained the strongest mean reward, highest mean delivery and lowest mean delay in this bounded workload, while gamma=0.90 used fewer forwards and duplicates. The figure documents parameter-selection provenance only and does not establish convergence, global hyperparameter optimality or superiority under the later dynamic-condition experiments.

## Claim boundary

Permitted:
- gamma=0.70 was selected from a predeclared bounded three-candidate/five-seed sensitivity matrix;
- the selection reflected a documented reward/delivery/delay versus communication-effort trade-off;
- all candidates showed non-zero state-action coverage and broad action use;
- gamma=0.70 was frozen before the formal dynamic-condition experiments.

Prohibited:
- gamma=0.70 is optimal;
- gamma=0.70 converges fastest/best;
- gamma=0.70 universally outperforms 0.80/0.90;
- the three-candidate matrix exhaustively validates gamma;
- sensitivity results generalize directly to failure, churn, heterogeneity or Kubernetes.

## Relationship to other artifacts

- F5 = visual bounded parameter-selection provenance.
- T4 = optional exact-value compact table/callout, decision deferred to S16-14B.
- T1 = learning-mechanism evidence, not gamma selection.
- F2/F3 = primary S11-A dynamic-condition evidence; scientifically separate.
- F4/T5 = Exp13 bounded external positioning; scientifically separate.
- T3 = Kubernetes operational realization; scientifically separate.

## Gate decision

**S16-14 = PASS / CLOSED.**

No figure was constructed and no manuscript scientific result was changed.

## Next controlled gate

**S16-14A — Gamma Sensitivity Figure Construction + Verification.**


---

# S16-14A — Gamma Sensitivity Figure Construction + Verification

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Construct F5 in the active manuscript exactly from the frozen S16-14 specification and verify numerical, visual-semantic and claim-boundary consistency.

## Construction

F5 was added natively to:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

Figure label:
`fig:gamma-sensitivity`

Architecture:
- native TikZ/PGFPlots;
- 2 x 2 panel layout;
- common candidate x-axis gamma={0.70,0.80,0.90};
- descriptive five-seed means only;
- no confidence intervals, standard errors, significance tests, fitted trend, convergence curve or composite score.

Panels and exact frozen values:
- mean reward: -0.264444, -0.268304, -0.268232;
- delivery ratio: 0.86552, 0.86181, 0.85597;
- propagation delay: 10.05872, 10.07401, 10.16041;
- total forwards: 226189.6, 225464.6, 222940.0.

Frozen duplicate means remain preserved outside the four-panel figure:
140637.4, 140283.4, 138342.6.

## Verification

Readback verification passed:
1. all 12 plotted values exactly match AR-1.4.4;
2. all four specified panels are present;
3. no invented uncertainty or significance layer is present;
4. the caption preserves the bounded parameter-selection interpretation;
5. accompanying prose explicitly presents a trade-off rather than a universal-winner interpretation;
6. gamma=0.70 is identified as the subsequently frozen candidate without “optimal”, “best”, convergence or universal-superiority language;
7. the paired-seed directional checks remain descriptive only;
8. F5 remains scientifically separate from S11-A, Exp13 and Kubernetes evidence.

## Provenance

Manuscript provenance was extended with a dedicated S16-14A F5 record. No separate PNG/PDF is required because the authoritative publication representation is native LaTeX/TikZ/PGFPlots.

## Scientific consequence

No experiment, rerun, parameter, statistic, claim authorization or pinned science baseline changed.

F5 documents only the already-frozen AR-1.4.2--AR-1.4.4 parameter-selection provenance.

## Gate decision

**S16-14A = PASS / CLOSED.**

## Next controlled gate

**S16-14B — Gamma Sensitivity Table/Callout Decision.**


---

# S16-14B — Gamma Sensitivity Table/Callout Decision

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Decide whether the publication package needs T4 in addition to F5, without introducing new analysis.

## Decision

**RETAIN T4 as a compact exact-value companion table.**

F5 remains the visual synthesis. T4 exists only to preserve compact exact values, including the duplicate series that is not plotted in F5.

## Retained T4 scope

Columns:
- gamma=0.70;
- gamma=0.80;
- gamma=0.90.

Rows:
- mean reward;
- delivery ratio;
- propagation delay;
- duplicates;
- total forwards.

Exact values are copied directly from the frozen AR-1.4.4 descriptive comparison.

## Excluded diagnostics

The following remain in the authoritative design record and are intentionally not duplicated in T4:
- cumulative reward;
- stabilization;
- q_updates;
- state_action_coverage;
- action distributions.

These support bounded learning-behaviour consistency rather than the compact publication-facing parameter-selection trade-off.

## Claim boundary

T4:
- does not create a composite score;
- does not rank candidates;
- does not add significance testing or inferential claims;
- does not establish convergence;
- does not establish global hyperparameter optimality;
- does not generalize the stationary sensitivity matrix to later dynamic experiments.

## Manuscript implementation

T4 was integrated into:
`wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

Label:
`tab:gamma-sensitivity`

Its caption explicitly states that it is a compact exact-value companion to F5 and not an omnibus score or optimality test.

## Verification

Readback confirmed:
- all 15 table values match AR-1.4.4 exactly;
- all five intended metrics are present;
- no additional statistic or uncertainty estimate was introduced;
- F5/T4 roles remain distinct;
- provenance is recorded in the manuscript repository.

## Gate decision

**S16-14B = PASS / CLOSED.**

## Next controlled gate

**S16-15 — Whole Artifact Package Integration.**


---

# S16-15 — Whole Artifact Package Integration

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Integrate and cross-check the complete publication artifact package after completion of the individual construction/rationalization gates.

## Integrated package

- F1 — Q-AHBN architecture and learning-cycle figure;
- A1 — formal Q-AHBN bounded-refinement algorithm;
- T1 — learning-mechanism evidence table;
- F2 — primary eight-condition paired trade-off figure;
- F3 — dynamic-stress response figure;
- T2 — primary paired statistical table;
- F4 — Exp13 bounded five-method positioning figure;
- T5 — Exp13 exact-values table;
- F5 — gamma-sensitivity figure;
- T4 — compact gamma exact-value table;
- T3 — Kubernetes evidence/accounting table.

## Integration audit

The active manuscript was audited as one package rather than artifact-by-artifact.

PASS findings:
1. all 11 intended artifacts are present exactly once;
2. no duplicate LaTeX labels are present;
3. no unresolved internal figure/table/algorithm references were found;
4. mechanism, primary ControlSim, Exp13, gamma-sensitivity and Kubernetes evidence roles remain distinct;
5. F1/A1/T1 are complementary rather than duplicative;
6. F2/F3/T2 retain the primary S11-A evidence hierarchy;
7. F4/T5 remain bounded to Exp13 churn=0.40 positioning;
8. F5/T4 remain bounded pre-formal-evaluation parameter-selection provenance;
9. T3 remains operational-realization/accounting evidence only;
10. no cross-environment pooling, omnibus ranking, convergence, optimality or universal-superiority framing was introduced.

## Minor integration correction

T1 existed correctly but had no explicit in-text reference. The learning-behaviour subsection now points reviewers to `tab:learning-mechanism` as the consolidated mechanism-evidence/claim-boundary map.

This correction is editorial/integrative only and changes no scientific content.

## Scientific consequence

No raw evidence, experiment, statistic, parameter, figure value, table value, confidence interval, claim authorization or pinned science baseline changed.

## Gate decision

**S16-15 = PASS / CLOSED.**

## Next controlled gate

**S16-16 — Artifact-to-Evidence Provenance Audit.**


---

# S16-16 — Artifact-to-Evidence Provenance Audit

**Status:** PASS / CLOSED — 2026-10-02

## Objective

Verify that every active publication artifact in the integrated F1--F5 + A1 + T1--T5 package traces to the correct frozen scientific authority and registered evidence family, without dependence on weaker historical or working-output sources.

## Audit result

PASS.

The provenance chain was verified for all active artifacts:
- F1 / A1 / T1 → frozen canonical AHBN + Q-AHBN design/mechanism evidence;
- F2 / F3 / T2 → S11-A primary paired ControlSim aggregation;
- F4 / T5 → S11-B Exp13-Q bounded benchmark aggregation;
- F5 / T4 → AR-1.4.2--AR-1.4.4 bounded gamma-sensitivity/selection evidence;
- T3 → K6-Q frozen Kubernetes evidence plus S16-13A runtime-accounting semantics audit.

## Provenance normalization

The manuscript provenance record still contained historical S15 artifact names:
- `tab:primary-tradeoff-synthesis`;
- `tab:kubernetes-accounting`.

These were not active manuscript labels after S16 rationalization.

The provenance record now explicitly marks:
- `tab:primary-tradeoff-synthesis` as SUPERSEDED/RATIONALIZED into T2 `tab:primary-paired-results`, with F2/F3 carrying visual synthesis;
- `tab:kubernetes-accounting` as SUPERSEDED/MERGED into T3 `tab:kubernetes-results`.

This is documentation normalization only and does not change manuscript scientific content.

## Evidence-authority checks

Confirmed:
1. every active artifact has an identified frozen scientific authority;
2. every quantitative result artifact traces to a registered evidence family;
3. S11-A and S11-B artifacts retain their registered Drive folder/file/hash provenance;
4. Kubernetes T3 retains the frozen evidence-family/folder/manifest/Git/image provenance;
5. F5/T4 use only the frozen AR-1.4.2--AR-1.4.4 sensitivity evidence;
6. no active artifact relies on Authority Level 6 historical Q-AHBN manuscript results or superseded semantics;
7. repository-local `output/` is not treated as authority merely because it is Drive-synchronized;
8. the pinned manuscript science baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`;
9. claim roles remain bounded by S12A and the claim-evidence matrix.

## Gate decision

**S16-16 = PASS / CLOSED.**

No evidence-authority gap or scientific defect was found.

## Next controlled gate

**S16-17 — Figure/Table/Algorithm Visual + LaTeX Production Audit.**


---

# S16-17 — Figure/Table/Algorithm Visual + LaTeX Production Audit

**Status:** HOLD / PARTIAL — 2026-10-02

## Objective

Audit the complete F1--F5 + A1 + T1--T5 package for LaTeX production correctness and page-level visual quality.

## Source-level LaTeX production audit

PASS findings:
1. required packages are loaded: TikZ, PGFPlots, groupplots, algorithm, algpseudocode, booktabs, graphicx and amsmath;
2. all five TikZ figure environments are structurally balanced;
3. all four PGFPlots groupplot environments are structurally balanced;
4. all five table environments are structurally balanced;
5. the single algorithm environment is structurally balanced;
6. no duplicate LaTeX labels were found;
7. no unresolved internal figure/table/algorithm references were found;
8. all 11 intended artifacts remain present exactly once;
9. active publication artifacts are embedded directly in the versioned manuscript source rather than depending on untracked figure files.

## Visual-verification boundary

A full visual PASS cannot be issued from repository source alone.

The manuscript repository currently contains the LaTeX source and bibliography but no tracked compiled PDF and no GitHub build workflow/artifact that renders the current post-S16-14B source. Therefore the following page-level properties remain unverified:
- clipping or overflow of TikZ/PGFPlots figures;
- axis-label/tick-label collisions;
- panel spacing and legibility at rendered size;
- table width/overflow and line wrapping;
- algorithm line wrapping and float placement;
- float ordering/page breaks;
- caption placement and whitespace balance;
- final PDF reference rendering.

Calling these visually verified without a compiled PDF would exceed the available evidence.

## Required closure evidence

Researcher/local execution should compile the current active manuscript source and provide the resulting PDF/log for visual/proof audit. The scientific source must remain unchanged unless the visual audit identifies a production defect.

Suggested local command from the manuscript version directory:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Equivalent latexmk execution is acceptable if available.

## Gate decision

**S16-17 = HOLD / PARTIAL.**

The LaTeX/source production sub-audit passes. The page-level visual sub-audit remains pending compiled-PDF evidence.

S16-18 is not released until S16-17 visual closure is completed.


## S16-17 compiled-PDF visual audit update — 2026-10-02

Compiled PDF audited: `main02Oct2026_1723.pdf` (26 pages).

Observed production defects:
1. Figure 1: connector/annotation text around the AHBN→Q-AHBN and canonical-state paths visually overlaps, reducing legibility.
2. Table 3: the final `Forward Δ` column extends beyond the right page boundary and is clipped in the rendered PDF.

Other inspected artifacts (Algorithm 1, F3, F4, F5, T1, T4, T5, T3) are visually readable with acceptable spacing and no detected clipping/overlap.

Corrective manuscript commit: `da5132a1a84e829ffeb7d49f12b0a9bd2fa51fca`.

Corrections applied:
- Figure 1 connector labels reduced/repositioned for clearer separation.
- Table 3 changed to a width-bounded production form using `\resizebox{\textwidth}{!}{...}` with tighter spacing to prevent right-edge clipping while preserving all exact values.

**Current S16-17 status remains HOLD / PARTIAL pending one recompile of the corrected source and visual confirmation that both defects are resolved.**

S16-18 remains blocked until that recompiled PDF is checked.


### S16-17 Figure 1 visual refinement amendment — 2026-10-02

Researcher supplied recompiled `main02Oct2026_1739.pdf`. Visual readback confirms the earlier Table 3 right-edge clipping defect is resolved: the complete `Forward Δ` column is now contained within the page.

At researcher request, Figure 1 received a presentation-only refinement while preserving the frozen F1 scientific semantics. The revised native TikZ design uses restrained publication-safe stage colors, a clean clockwise six-stage pipeline, a separately routed dashed canonical-EWMA state-reuse path above the pipeline, and a separately routed dashed learning-feedback return path below the pipeline. This removes the crowded crossing/annotation region in the previous rendering and visually distinguishes immutable AHBN, bounded Q-AHBN refinement, forwarding realization, outcomes, and reward closure.

Manuscript source commit: `b2d32b171c16b2e5bb407f0ad662185da6f44b12`.

No scientific content, algorithm semantics, numerical evidence, caption claim boundary, or artifact role changed.

**S16-17 remains HOLD / PARTIAL pending one recompile/readback of the redesigned Figure 1.** Table 3 is visually cleared. S16-18 remains blocked until Figure 1 is confirmed clean in the compiled PDF.


### S16-14A Figure 2 visual-production amendment — 2026-10-02

The researcher explicitly reopened the gamma-sensitivity artifact for visual audit using compiled manuscript PDF `main02Oct2026_1806.pdf`.

Visual finding: Figure 2 is scientifically correct and readable, with all four frozen panels present and no clipping, overlap, or label collision. The plotted trade-off is visible, but the default plot styling is visually light relative to the newly standardized Figure 1 and the other publication figures.

Presentation-only refinement applied in manuscript commit `b3b362446cf527ed157cfec51b5ed8e35fc6027d`:
- all four F5 series use one consistent blue publication color;
- markers are slightly enlarged for manuscript-scale readability;
- line weight is slightly increased;
- panel layout, axes, values, candidate order, captions, and claim boundaries are unchanged.

No scientific value, uncertainty layer, statistic, trend model, or parameter-selection conclusion changed.

S16-14/S16-14A scientific closure remains valid. This amendment is tracked under the current S16-17 visual-production audit and requires one recompile/readback before final visual closure.


### S16-17 Figure 2 production correction — 2026-10-02

Compiled manuscript `main02Oct2026_1836.pdf` confirmed F5 scientific content and the blue styling amendment. One minor production issue remained: the lower-row y-axis labels, especially panel (d) `Total forwards`, were visually tight toward the centre gap. Manuscript commit `91a97d73fe1bb8ed466cf7401469d0b8436c493e` increases the F5 groupplot horizontal separation from 1.35 cm to 1.65 cm. No plotted values, axis ranges, panel dimensions, statistics, caption, scientific interpretation, or S16-14/S16-14A evidence boundary changed. Final S16-17 closure is held pending one researcher recompile/readback.


### S16-17 final compiled-PDF readback — 2026-10-02

Researcher-supplied compiled manuscript `main02Oct2026_1842.pdf` was visually/readback audited after the F5 spacing correction. Figure 2 now has adequate lower-row y-label clearance and a balanced 2x2 layout; no overlap or clipping requiring another production edit was identified. Figure 1 remains visually coherent after its previously approved single-blue styling and standardized box treatment. Figures 3--5, Tables 1--5, and Algorithm 1 are present and legible in the compiled package. No scientific-value, statistical, caption, or claim-boundary change was introduced by the final production correction.

**S16-17 — Figure/Table/Algorithm Visual + LaTeX Production Audit = PASS / CLOSED (2026-10-02).**

Next controlled gate: **S16-18 — Reviewer-Challenge Artifact Audit**.


## S16-18 — Reviewer-Challenge Artifact Audit — 2026-10-02

**Status: PASS / CLOSED**

### Scope
Adversarial reviewer-facing audit of the completed publication artifact package only. No new experiment, statistic, parameter, evidence family, or scientific interpretation was authorized.

Audited package:
F1 `fig:qahbn-cycle`; A1 `alg:qahbn`; T1 `tab:learning-mechanism`; F2 `fig:primary-paired-tradeoff`; F3 `fig:dynamic-stress-response`; T2 `tab:primary-paired-results`; F4 `fig:exp13-bounded-positioning`; T5 `tab:exp13-results`; F5 `fig:gamma-sensitivity`; T4 `tab:gamma-sensitivity`; T3 `tab:kubernetes-results`.

### Reviewer-challenge matrix

| Likely reviewer challenge | Artifact defence | Audit disposition |
|---|---|---|
| Is Q-AHBN replacing or silently retuning AHBN? | F1 + A1 explicitly place immutable canonical AHBN first, preserve its proposal, and permit one bounded post-AHBN refinement before canonical eligible-target realization. | COVERED |
| Are state/action/reward/update semantics reproducible? | A1 plus Section 3 define 81-state discretization, five actions, attributable NEW/DUPLICATE/FAILED reward, F=0 rule, next-same-peer successor, terminal zero bootstrap, and frozen learning constants. | COVERED |
| Is there evidence that learning actually executed rather than behaving as a static wrapper? | T1 records repeated reward-bearing updates, non-zero state-action coverage, bounded interventions, reward behaviour and traceability, with explicit non-convergence boundaries. | COVERED |
| Are the primary performance claims supported by paired evidence and uncertainty? | F2 + T2 expose all eight predeclared same-seed AHBN--Q-AHBN conditions; delivery/delay use registered paired 95% Student-t CIs; duplicates/forwards remain descriptive. | COVERED |
| Are condition effects hidden by pooling? | F3 separates failure, churn and heterogeneity families; T2 retains exact condition-specific estimates; no pooled overall effect is introduced. | COVERED |
| Is the communication-overhead cost obscured? | F2 panels (c,d) + T2 explicitly expose positive duplicate/forward differences; manuscript text frames the result as a delivery-latency/overhead trade-off. | COVERED |
| Does the five-method comparison imply a universal winner? | F4 + T5 show fixed-order metric-specific operating points only at churn=0.40 and explicitly prohibit omnibus ranking/generalization. | COVERED |
| Was gamma chosen post hoc from formal results or presented as globally optimal? | F5 + T4 expose the pre-formal 15-run, three-candidate Learning Validation trade-off and explicitly bound it to parameter-selection provenance, not global optimality/convergence. | COVERED |
| Does Kubernetes independently confirm superiority or low overhead? | T3 plus its caption/text explicitly restrict Kubernetes to operational realization/observability, report CIs crossing zero, and explain the Q-AHBN `total_forwards` instrumentation mismatch using `F_attempt`. | COVERED |
| Are exact values recoverable rather than only graphical? | T2, T4, T5 and T3 provide exact publication-facing numerical companions for the quantitative figures/evidence families. | COVERED |
| Are artifact roles redundant or internally contradictory? | F1/A1/T1 = mechanism; F2/F3/T2 = primary evidence; F4/T5 = bounded comparator positioning; F5/T4 = gamma provenance; T3 = Kubernetes. S16-15/16/17 already verified integration, provenance and production. | COVERED |

### Residual reviewer vulnerabilities

The audit identifies limitations that are already disclosed and do not justify new artifacts:
1. primary inferential cells contain only five paired seeds; uncertainty is therefore bounded to that design;
2. gamma sensitivity covers only three predeclared gamma candidates and one stationary Learning Validation workload;
3. T1 is intentionally mechanism-level and does not expose every raw learning diagnostic or per-action frequency;
4. Exp13-Q covers only the single predeclared churn=0.40 reference condition;
5. Kubernetes is not a numerical replication of ControlSim and its performance contrasts are inconclusive;
6. the Kubernetes `total_forwards` field is instrumentation-noncomparable for Q-AHBN, but T3 now exposes rather than hides that limitation.

These are scope/validity limitations, not missing-artifact defects. Adding new experiments, post-hoc analyses, or extra figures to answer them would violate or unnecessarily expand the frozen evidence contract.

### Decision

The completed artifact package is sufficient to defend the manuscript's authorized claims against the principal foreseeable reviewer challenges. No additional figure, table, algorithm, statistical test, or experiment is required by this gate. Existing artifact redundancy is purposeful figure-to-exact-table pairing rather than duplication without scientific role.

**S16-18 = PASS / CLOSED.**

No manuscript-source edit is required under S16-18.

**Next controlled gate: S16-19 — Whole-Manuscript Artifact/Text Consistency Audit.**
