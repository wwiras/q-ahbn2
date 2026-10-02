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
6. **Gamma:** do **not** create a large robustness figure. The evidence covers gamma only over three predeclared values and does not justify broad sensitivity/robustness presentation.

## Minimum final artifact set

The minimum publication-complete package is therefore:
- **4 figures:** F1 architecture, F2 primary trade-off, F3 dynamic stress, F4 Exp13 positioning;
- **1 formal algorithm:** A1 Q-AHBN pseudocode;
- **4 core tables:** T1 learning evidence, T2 paired statistical results, T3 Kubernetes/accounting, T5 Exp13 exact values;
- **optional compact T4 gamma table/callout**, subject to exact-value/provenance readback.

This is a maximum useful architecture, not a requirement to inflate artifact count. During implementation, an artifact may be merged only when the scientific question remains immediately readable.

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

### S16-14 — Gamma Sensitivity Publication Artifact Decision

Inspect the frozen 15-run gamma sensitivity evidence over gamma={0.70,0.80,0.90}, seeds 42--46. Add a compact table/callout only if exact frozen values materially improve publication clarity. Otherwise retain concise Methods prose. No broad robustness, global-optimality or convergence interpretation is permitted.

### S16-15 — Whole Artifact Package Integration

Integrate verified F1--F4, A1 and the rationalized table set into `wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`. Update cross-references, captions, placement and immediately surrounding prose only as needed. No new science is authorized.

### S16-16 — Artifact-to-Evidence Provenance Audit

For every final figure, table and algorithm, register and verify:

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

Close S16 only after all essential artifacts are integrated and verified, table redundancy is resolved, artifact provenance is complete, visual/LaTeX and reviewer-challenge audits pass, whole-manuscript artifact/text consistency passes, and no unauthorized scientific change has occurred.

## Controlled state after programme revision

- **S16-0:** PASS / CLOSED.
- **S16-0A:** NEXT / RELEASED.
- **S16-1 through S16-21:** PENDING; each is released only by closure of its required predecessor.
- Venue selection remains researcher-controlled and outside the S16 critical path.
- A later venue-specific submission-production programme may be opened only after researcher venue selection and S16 closure.

## Next controlled gate

**S16-0A — Historical Q-AHBN Manuscript Artifact Refinement Audit.**

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
