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
