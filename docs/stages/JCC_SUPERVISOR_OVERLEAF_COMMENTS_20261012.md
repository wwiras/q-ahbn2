# JCC Supervisor Overleaf Comments — Controlled Reconciliation (2026-10-12)

**Status:** COMMENT INVENTORY RECONCILED / EDITORIAL REVISION HOLD
**Scientific repo:** `wwiras/q-ahbn2`
**Manuscript repo:** `wwiras/QAHBN2-Manuscript`
**Pinned science baseline:** `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`
**Prior stage:** `docs/stages/JCC_SUPERVISOR_REPOSITIONING_20261012.md`
**Authority:** `docs/00_QAHBN2_MASTER.md`, `docs/01_CANONICAL_AHBN_CONTRACT.md`, `docs/02_QAHBN2_DESIGN_FREEZE.md`
**Input:** Three supervisor Overleaf comments provided verbatim by researcher on 2026-10-12; supervisor WhatsApp guidance on repositioning, parameter justification, subsection consolidation, and desired revision by 2026-10-23.

## Received reviewer comments (supervisor, not external journal review)
1. `sn-main.tex`, Method, canonical proposal, line 327: “Why k is these numbers?” Target: `k_AHBN in {2,3,4,5,6}`.
2. `sn-main.tex`, Method, bounded action space, line 384: “how these numbers affected by k_AHBN?” Target: `k_Q in {1,2,3,4,5,6,7}`.
3. `sn-main.tex`, Method, bounded action space, lines 365–368: “need explanation why you have these action selection.” Target: `KEEP, FANOUT_DOWN, FANOUT_UP, SET_GOSSIP, SET_STRUCTURED`.

## Audited conclusions and bounded editorial change map

| ID | Scientific answer | Manuscript revision | Verification gate |
|---|---|---|---|
| OC-01 | The deterministic canonical controller produces one of five requested fanouts 2–6; it uses frozen score boundaries −0.25, 0.25, 0.90, 1.50. These are inherited design levels, not five independently optimized RL choices. Prior RO2 fanout characterization informs latency–duplication rationale; distinguish evidence for a bounded control range from proof of optimal endpoints. | Replace unexplained set with compact rationale and provenance, preferably a design-choice table; avoid asserting optimality. | Check AHBN contract, RO2 evidence, latest approved AHBN paper before citing a numerical selection study. |
| OC-02 | Exactly one Q action modifies the canonical proposal. FANOUT_DOWN yields k_AHBN−1; FANOUT_UP yields k_AHBN+1; KEEP and mode-setting actions preserve k_AHBN. Therefore k_Q 1–7 is a derived range, not independently tuned bounds. Realized targets satisfy 0 ≤ k_real ≤ min(k_Q, |N_e|). The historical learner-side upper clip of six was explicitly removed. | Add succinct transformation equation and worked boundary examples 2→1 and 6→7; distinguish requested vs realized. | Verify design freeze and implementation parity; no Q-layer cap of six. |
| OC-03 | Five actions separate (i) preserve baseline, (ii) ±1 changes to forwarding intensity, and (iii) selecting either available mode while retaining fanout. They restrict learning to interpretable, single-dimension changes of the two existing control actuators. Action selection is an architectural design decision, not an exhaustive or experimentally optimized action-set search. Mode-setting may be a proposal-level no-op. | Add reasons for each action family, acknowledge no action-set sensitivity study, preserve frozen policy and logging. | Verify frozen design, current method and implemented transformations. |

## Supervisor-agreed journal positioning

Explain the complete deterministic hybrid controller in a self-contained way, avoid presenting unpublished AHBN as an established published third-party method, and reduce AHBN branding/thesis chronology in title/abstract/introduction/method narrative. **Do not conceal scientific provenance or mislabel the factual AHBN baseline.** Preserve an accurate method distinction between deterministic baseline proposal, learned intervention and actual realization. Center novelty on the bounded Q-learning mechanism and its attributable outcomes; justify fixed hyperparameters separately from sensitivity-supported gamma; consolidate overly fragmented Results and Discussion subsections while preserving experiment distinctions and statistical caveats.

## Scope constraints
- No changes to frozen equations, thresholds, action semantics, code, datasets, experiments, statistics, baselines or results.
- No manufactured justification or retrospective parameter optimization.
- Do not treat manuscript prose revisions as validating performance or scalability.
- Preserve the frozen scientific pipeline and manuscript repository separation.
- Source and evidence authority remains GitHub-first; Drive is supporting evidence. Local Mac sync paths are not directly accessible to this execution environment.

## Evidence/reconciliation inspected
- Current scientific master contract and design freeze fetched from live GitHub `main`.
- Previous `JCC_SUPERVISOR_REPOSITIONING_20261012.md` stage consulted.
- Live manuscript `sn-main.tex` checked; its present method matches all three cited mathematical expressions and the five actions.
- Both user-supplied Drive cloud corpus roots listed successfully; these lists verify corpus access, not content-level evidence revalidation.

## Next bounded gate
Draft a complete supervisor-comment response/change map for author review, then perform controlled manuscript text revisions and a method/provenance audit. After edits: manuscript diff, frozen-science consistency check, build/proof readback, and supervisor sign-off before any journal submission GO. Working deadline **Friday 2026-10-23**, not an automatic approval date.

**Decision:** This stage records comments and reconciled explanations; NO manuscript scientific-method changes and NO frozen design reopening. Status remains **REVISION HOLD** until editorial/verification gates pass.


## WhatsApp follow-up: agreed manuscript revision direction (2026-10-12)

**Provenance:** researcher-supplied WhatsApp excerpts, distinguished from assistant editorial interpretation. Prof Tan agreed that, while AHBN remains unpublished, the article should explain the underlying hybrid mechanism, strengthen parameter justifications, and emphasize Q-learning novelty. Prof Tan additionally requested consolidation of excessive Results and Discussion subsections and a quick rewrite/finalization by the end of the following week while awaiting validation. The researcher acknowledged these instructions. The date **Friday, 23 October 2026** is recorded as an *internal target for a supervisor-ready manuscript*, not a journal submission date or a claim that validation has passed.

### Integrated control requirements

| Control ID | Instruction | Revision acceptance criterion |
| --- | --- | --- |
| WA-01 | Reduce direct emphasis on the unpublished AHBN predecessor. | Explain the deterministic hybrid dissemination controller's observations, score, mode and fanout proposal within the present manuscript; disclose provenance and do not mislabel the AHBN experimental baseline as another method. |
| WA-02 | Change thesis-like progression into a journal-focused argument. | Abstract, Introduction, Related Work, Method, and Conclusion foreground the bounded Q-learning contribution, its gap, comparison, and limits. |
| WA-03 | Justify central parameter and action selections. | Use an evidence-graded parameter rationale (empirical sensitivity, inherited design, or fixed architectural choice). Address the three OC items on k_AHBN, k_Q and five actions. No retrospective optimality or nonexistent sweeps. |
| WA-04 | Consolidate Results and Discussion subsections. | Merge unnecessarily fragmented headings while retaining all condition-specific results, benchmark distinctions, overhead trade-offs, statistical qualifications and Kubernetes scope limits. |
| WA-05 | Rewrite promptly while validation is pending. | Internal supervisor-ready target 2026-10-23; validation, compiled proof, evidence parity, and supervisor sign-off remain independent gates. |
| WA-06 | Preserve scientific integrity. | Only editorial repositioning is authorized: no redesign, rerun, parameter retuning, changed baselines, new results, or unsupported novelty claims. |

### Manuscript-wide audit and change map — next gate

1. **Title/abstract/introduction:** paper-level problem and learning contribution; avoid thesis objective chronology and repeated AHBN emphasis.
2. **Related work:** verify novelty relative to published approaches, avoiding unsupported claims of uniqueness or superiority.
3. **Method, figures, algorithm:** self-contained baseline hybrid controller; exact deterministic-first and post-controller Q boundary; distinguish base proposal, refined request, and eligible-neighbour realization; add OC-01–OC-03 rationales and parameter-evidence table.
4. **Experiment and parameter reporting:** preserve frozen scenarios, statistical comparisons and explicit separation of empirically supported gamma from fixed configuration values.
5. **Results and discussion:** streamline subsection hierarchy without conflating same-seed paired AHBN/Q-AHBN effects, five-method reference results, or Kubernetes operational validation; report overhead honestly.
6. **Release checks:** cross-reference/citation audit, scientific source and claim reconciliation, manuscript diff, clean compilation and proof, supervisor validation/sign-off. A historical JCC submission GO does not automatically carry forward.

**Gate outcome:** WhatsApp instructions and Overleaf comments are reconciled as a single controlled editorial revision scope. **EDITORIAL AUDIT / REVISION RELEASED; JOURNAL SUBMISSION HOLD.** This update does *not* close the underlying Overleaf reviewer comments or declare the manuscript rewritten. The pinned scientific baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` unchanged. Source of truth remains GitHub `main`; the scientific Drive root `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5` and manuscript Drive root `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj` are supporting synchronized workspaces. Mac-local paths cannot be mutated directly from this connector execution.


## Editorial revision plan and target gates — 12 to 23 October 2026

**Plan status:** PROPOSED / DOCUMENTED; manuscript editing has not begun under this gate. This entry does not override the frozen science or assert the journal review/submission status. The researcher reports the Q-AHBN manuscript as **submitted to Journal of Cloud Computing and under peer review, with no manuscript DOI yet**; independently verify editorial-system status before publication-facing representations. The Zenodo **dataset** DOI recorded in the scientific master is not a paper DOI.

### Date-scoped controlled gate schedule

| Gate | Target | Work | Completion criterion |
|---|---|---|---|
| JCC-R1 Audit & inventory | 12–13 Oct | Compare current `sn-main.tex`, supervisor OC/WA controls, latest manuscript, frozen scientific contracts, latest AHBN Scientific Reports source/PDF, and existing literature; register exact section changes, risks and reference provenance. | Section-by-section change matrix, all OC-01..03 and WA-01..06 mapped, no unsupported evidence claims. |
| JCC-R2 Scientific positioning & method | 14–16 Oct | Reframe contribution/novelty, self-contained deterministic hybrid controller, separate baseline proposal from Q-learning intervention; justify `k_base`, `k_Q`, 5 actions, 81 states, reward, learning coefficients; clearly grade design evidence. | Method matches frozen contracts and code, all major parameter rationales explicit, no AHBN concealment. |
| JCC-R3 Literature/experiment reporting | 17–19 Oct | Explicitly investigate SOTA hybrid blockchain dissemination comparators (e.g., already-studied DC-SoC), verify citation/claim match; streamline Related Work and Experimental Methodology, retain baseline and comparison integrity. | Each external method described as literature or actual comparator according to recorded experiments, no substitution or novelty overclaim. |
| JCC-R4 Results/Discussion restructuring | 20–21 Oct | Consolidate seven Results and six Discussion subsections where editorially coherent; preserve failure/churn/heterogeneity paired results, separate five-method benchmark and K8s observational boundary; rewrite conclusions. | Fewer substantive headings without deleting statistical qualifications, values or overhead limitations. |
| JCC-R5 Proof & internal release | 22–23 Oct | Audit manuscript diff, bibliography, figure/table references, terminology, OC/WA response checklist, compilation, PDF visual proof, controlled GitHub readback and supervisor-ready package. | Supervisor-ready revision by Fri 23 Oct; submission remains hold until proof, pending validation and supervisor approval. |

**Sequencing:** early writing can proceed alongside pending validation; only the factual claims dependent on validation must remain on hold. A gate cannot be declared PASS from a deadline alone. When a blocking audit finding arises, retain the issue openly instead of compromising the frozen science to meet the date.

### Present manuscript structure: verified 12 Oct GitHub main
- `sn-main.tex` has 7 Results subsections: learning behaviour; failure; churn; heterogeneity; cross-condition synthesis; bounded five-method positioning; Kubernetes operational realization.
- Discussion has 6 subsections: primary evidence; learning mechanism; overhead; external positioning; Kubernetes; contribution/scope.
- **Proposed**, not yet approved final layout: Results grouped into (a) learning and paired dynamic-condition effects, (b) five-method reference benchmark, (c) Kubernetes operational evidence; Discussion grouped into (a) mechanism/trade-offs, (b) literature positioning and validation scope. Keep experiment-level subheadings only where vital to reporting clarity.
- This structural proposal must be checked against the long, data-rich heterogeneity and benchmark tables and any supervisor annotations; do not promise a fixed final number of subsections before reflow.

### Source hierarchy and workflow boundaries
- **Science:** `wwiras/q-ahbn2` pinned `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`; current scientific `docs/00_QAHBN2_MASTER.md`, design, experiment, results and claim contracts.
- **Publication text:** `wwiras/QAHBN2-Manuscript/sn-main.tex`, bibliography and manuscript-control records.
- **Thesis:** `wwiras/MUM_FIT_ThesisWira` is authoritative for thesis control/text but *not* for Q-AHBN manuscript algorithm/experiment authority; thesis Drive root `1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR` is supporting reference. Keep thesis and journal prose independent.
- **Source corpora:** RO4 manuscript Drive `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`; Q-AHBN experiment Drive `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`, including `output/`. Google Drive sync or a file existing in `output/` does not alone promote it to authoritative scientific evidence. The AHBN Scientific Reports PDF supplied as Drive file `1_C3fJpukQ-RJWLjU5Krx5lSwCio9TSQh` requires source/version cross-check before numerical-citation reuse.
- Preserve **Q-AHBN** as the manuscript-facing algorithm name; `q-ahbn2` remains repository identifier. Never imply the AHBN paper is published, or conflate a manuscript DOI with the separately registered Zenodo dataset DOI.

### Remaining explicit supervisor item
**WA-07 / SOTA hybrid prior work:** Prof Tan specifically asked whether an existing SOTA hybrid approach can supply a reference. Investigate literature-supported framing and existing SOTA benchmark comparators, but do not claim Q-AHBN runs on another controller or silently relabel the frozen AHBN baseline. Record exact published sources and defensible feature-by-feature distinctions during JCC-R3.

### Proposed next authorized action
**JCC-R1 — manuscript-wide audit/change inventory (not substantive rewrite yet)**. Record section-level change obligations mapped to OC/WA IDs, evidence authority, current claim, proposed revision and verification checks; then perform JCC-R2 through R5 sequentially per `docs/00_QAHBN2_MASTER.md` reconcile/write/readback procedure. No scientific re-opening, no resubmission or journal portal action is authorized by this plan.


## 2026-10-12 reconciliation update — scientific adequacy decision before revision

**Status:** PLAN UPDATED / JCC-R1A OPEN / NO SCIENTIFIC MODIFICATION APPROVED. This supersedes any interpretation of the preceding editorial plan that all Q-AHBN parameters and experiments are permanently frozen or that no new experiments could be justified. The internal target of Friday 23 October 2026 is conditional on scientific adequacy.

### Corrected scientific decision boundary

| Scope | Current decision |
| --- | --- |
| Canonical AHBN | Frozen: retain its observation semantics, normalization/EWMA, score, mode decision, and bounded fanout actuator. Do not redesign AHBN under this revision. |
| Q-AHBN parameters, action space, reward, learning design, and experiments | Keep pinned commit `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` as the unmodified reference baseline **while adequacy is reviewed**. No unconditional freeze-or-modify decision has been made. |
| Potential additional or corrected Q-AHBN science | Decision only after evidence audit, with targeted hypothesis, scope, source parity, controls, comparison, provenance, revalidation, and explicit approval before execution. |
| Editorial manuscript changes | Allowed subject to audit, source accuracy and supervisor review. Not evidence that all design choices have been experimentally optimized. |

**Clarification:** 'Revise the paper, not redesign the algorithm' is the default editorial strategy, not a scientific verdict. The pinned science baseline remains historically immutable as a comparison reference. Any approved scientific candidate must be separately versioned and reconciled rather than silently rewriting the original baseline. No experiment or parameter change is authorized in this stage.

### JCC-R1A — Scientific Adequacy and Additional Experiment Decision Gate

**Target:** During JCC-R1, 12–13 October 2026; **OPEN / NOT YET EXECUTED**.

For every material Q-AHBN parameter, result, experiment and claim, identify: (1) the exact choice and manuscript statement; (2) its frozen contract, code and evidence provenance; (3) whether the existing evidence justifies precisely what is claimed; (4) whether a clear explanation or narrower claim is sufficient; (5) whether a new controlled sensitivity experiment, correction or parameter change would be scientifically necessary.

| Decision | Criteria | Action |
| --- | --- | --- |
| A — RETAIN / EXPLAIN | Existing supporting evidence sufficient | Explain and cite accurately; no rerun. |
| B — RETAIN / QUALIFY | Defensible inherited/fixed design choice, not necessarily optimized | Explain design intent and limitations; narrow overclaims. |
| C — INVESTIGATE | Material unanswered scientific issue | Define targeted experiment/sensitivity test, required controls, metrics and statistical comparison; seek separate approval before execution. |
| D — CORRECT / REVISE | Verified error, invalid assumption, or demonstrated inadequacy | Open controlled scientific correction/change gate, revalidation and evidence/claim reconciliation. |

**Required JCC-R1A artifact:** parameter-and-evidence adequacy matrix containing parameter/experiment, value, source contract/code, linked run or log, evidence class, manuscript location, supported claim, A/B/C/D decision, unresolved risk, required action, authority and schedule effect. Minimum coverage: 81 state bins, five meta-actions, bounded `k_Q` derived from canonical `k_AHBN`, reward and attribution, Q-learning rate, discount gamma and sensitivity evidence, exploration schedule, primary same-seed pairs, Exp13-Q five-method comparisons, Kubernetes scope, statistical analysis and unfavorable outcomes. Record AHBN as frozen reference only.

**Stop/release rule:** R2–R5 editorial work may proceed where facts are settled, but any material unresolved C/D issue blocks affected claim closure. If new experimental work becomes necessary, reassess 23 October rather than weaken the scientific standard. The need for new Q-AHBN science remains **undecided pending R1A**.

### Revised supervisor revision gates (superseding narrower interpretation above)

| Gate | Working target | Deliverable and acceptance |
| --- | --- | --- |
| JCC-R1 plus JCC-R1A | 12–13 Oct | Manuscript-wide section/comment map (OC-01–03; WA-01–07); source/evidence reconciliation; scientific adequacy decisions A/B/C/D before final science scope is declared. |
| JCC-R2 | 14–16 Oct | Journal-oriented Introduction and Method; Q-learning novelty, self-contained frozen deterministic hybrid foundation, accurate parameter and action rationales, subject to R1A conclusions. |
| JCC-R3 | 17–19 Oct | Verifiable SOTA hybrid/learning sources, defensible related-work distinctions, accurately described experimental protocol and baselines. |
| JCC-R4 | 20–21 Oct | Consolidate seven Results and six Discussion subsections as appropriate, retaining identifiable failure/churn/heterogeneity, five-method benchmark, Kubernetes evidence, adverse overhead and limitations. |
| JCC-R5 | 22–23 Oct | Diff, citations, equations, data/provenance, tables/figures, LaTeX compilation, PDF visual proof, controlled readback, supervisor-ready package; NOT automatic publication/submission approval. |

**Observed editorial needs:** sharpen Introduction question/novelty; contextualize existing hybrid and learning SOTA; explain design rationales without fabricating sweeps; preserve actual AHBN/Q-AHBN study lineage; simplify Results and Discussion heading hierarchy without losing distinctions. Proposed grouping: Results (learning plus paired dynamic-condition effects; five-method reference benchmark; Kubernetes operational realization); Discussion (mechanism and trade-offs; external positioning and bounded applicability). Final layout is conditional on detailed content audit.

### Authority and status

- Scientific source: `wwiras/q-ahbn2`; unchanged pinned scientific baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`. Manuscript source: `wwiras/QAHBN2-Manuscript/sn-main.tex`. `wwiras/MUM_FIT_ThesisWira` remains thesis-text authority only.
- Researcher reports Q-AHBN submitted to *Journal of Cloud Computing* and under peer review, **not published and no manuscript DOI**. The existing Zenodo dataset DOI is a different artifact; do not describe it as a journal article DOI. The AHBN Scientific Reports manuscript is also not published.
- Supporting cloud corpora: scientific Drive folder `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`, manuscript Drive `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`; AHBN manuscript PDF `1_C3fJpukQ-RJWLjU5Krx5lSwCio9TSQh`. The scientific Drive root and `output/` folder were located during this administrative review; no individual result log was validated or promoted.
- Researcher-supplied scientific Mac sync path: `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2`. Manuscript sync path: `/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myPaper/ClusterComputing/QAHBN2-Manuscript`. These cannot be directly modified via cloud connector. Repository `output/` is Git-ignored; Drive syncing alone does not certify evidence.

**Transaction outcome:** revision plan and science-decision protocol only; manuscript, Q-AHBN code, AHBN controller, parameters, datasets, numerical results and experimental design remain unchanged. **NEXT: JCC-R1/R1A, OPEN. JOURNAL SUBMISSION HOLD.**
