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


## JCC-R1 / R1A — Initial Evidence-Backed Audit and Conditional Decision (2026-10-12)

**Gate verdict: CONDITIONAL PASS for repository/manuscript mapping and bounded evidence screening; HOLD for full scientific adequacy closure.** The initial paper-to-contract-to-registered-evidence audit is completed below. This is *not* approval to change Q-AHBN science, an independent rerun of statistics, exhaustive code-level verification, a completed SOTA literature review, or supervisor sign-off. JCC-R1A remains OPEN for the stated C cases and source/code checks.

### 1. Inputs actually inspected and authority reconciliation

| Source | Verified use |
| --- | --- |
| Scientific `docs/00_QAHBN2_MASTER.md` §9.5 | GitHub fetch → reconcile → bounded audit → recorded decision → update only changed stage → GitHub post-write readback. |
| Scientific `docs/01_CANONICAL_AHBN_CONTRACT.md`, `docs/02_QAHBN2_DESIGN_FREEZE.md`, `docs/03_EXPERIMENT_CONTRACT.md`, `docs/04_STATISTICAL_CONTRACT.md`, `docs/06_RESULTS_REGISTER.md`, `docs/07_CLAIM_EVIDENCE_MATRIX.md` | Checked normative AHBN boundary, Q design/provenance, run matrix, analysis role, reported claims and restrictions. |
| Manuscript `wwiras/QAHBN2-Manuscript/sn-main.tex` on current `main` | Inspected exact method lines ~312–437, experimental protocol ~594–666, Results ~670–1245, Discussion ~1246–1300, Limitations ~1302–1319; headings enumerated. |
| Scientific Drive `output/evidence/` | Located preserved AR-1.4.2 gamma CSV, S11-A primary aggregation CSV and S11-B Exp13-Q CSV; opened and spot-checked their reported content and provenance; did not reaggregate raw data, audit every underlying run, or independently recompute hashes. |
| AHBN Scientific Reports PDF, Drive `1_C3fJpukQ-RJWLjU5Krx5lSwCio9TSQh` | Fetched readable paper text for background/provenance, not treated as a published or peer-reviewed method reference. |

**Current manuscript structural audit:** 7 Results subsections (learning, failure, churn, heterogeneity, cross-condition, benchmark, Kubernetes); 6 Discussion subsections (primary evidence, learning mechanism, overhead, external positioning, Kubernetes, contribution/scope). Targeted condensation is justified editorially; no table deletion or result alteration authorized.

### 2. JCC-R1A parameter/evidence adequacy matrix — preliminary classification

**Interpretation:** A means retained/adequately supported within the stated scope; B means retained as a disclosed fixed or inherited design choice without claiming optimization; C is a specific follow-up audit question that may merit targeted testing depending on how strong a claim the paper seeks to make; D means demonstrated scientific error. **No D is established by this screening.** All Q-AHBN values remain the historical frozen *reference implementation* pending controlled decision; A/B are provisional adequacy assessments, not retrospective parameter retuning.

| Item | Evidence and manuscript location | Initial class | Decision / unresolved issue |
| --- | --- | --- | --- |
| Canonical AHBN observations, EWMA 0.30, score/mode and `k_AHBN` 2–6 | Immutable `01_CANONICAL_AHBN_CONTRACT.md`; manuscript ~315–335; OC-01 | A (inherited freeze) | Retain AHBN unchanged; explain RO2-informed bounded fanout, do not pretend its endpoints were independently tuned by Q-learning. AHBN numerical provenance may require RO2 paper/source cross-check. |
| Q state: 3 bins per each of four signals, 81 states | `02_QAHBN2_DESIGN_FREEZE.md`; manuscript ~340–359 and ~1319 | B; C only if stronger robustness claim requested | Compact architectural representation; bins at 1/3 and 2/3 not evaluated against alternatives. Keep limitation; no optimization claim. An alternative-bin sensitivity test is optional unless claimed robustness becomes essential. |
| Five meta-actions / 405 Q values | Design freeze; manuscript ~361–380 and ~412–437; OC-03 | B | Five interpretable single-axis actions, KEEP, ±1 fanout, either mode. No action-set ablation reported; justify architecture without claiming minimal/optimal action set. |
| Derived Q fanout `k_Q` 1–7 and eligible realization | Design freeze; manuscript ~382–390; OC-02 | A (algebraic contract) | Bounds follow canonical 2–6 plus at most ±1; distinguish request from realized targets. Confirm no historical upper Q cap leaks into current code at targeted parity check. |
| Attribution reward `(NEW−DUPLICATE−FAILED)/F` with F=0 no update | Design freeze and manuscript ~392–407 | B | Decision-owned outcome semantics documented; no alternative reward-weight sensitivity claimed. Do not assert universally optimal reward shaping. |
| Q learning rate `alpha_Q=0.25` | Design freeze, manuscript ~416–429 | B; C if sensitivity is needed for a stronger parameter-robustness claim | Fixed not gamma-tuned; distinguish from frozen AHBN EWMA alpha=0.30. Explain rationale/limitation; test only if material to review conclusions. |
| Q discount `gamma=0.70` | Results register 15/15 gamma validation, seeds 42–46, candidates .70/.80/.90; Drive gamma CSV; manuscript ~482–582 | A (bounded selection) | Selected within predeclared stationary sensitivity; retain lower-forward trade-off at gamma=.90. Neither global optimum nor convergence demonstrated. |
| Exploration epsilon 0.30→floor 0.03, decay 0.995 | Design freeze and manuscript ~431–437 | B; C if robustness-to-exploration is claimed | Fixed schedule with no recorded parameter sweep; be explicit and avoid global optimality. |
| Primary Exp10-Q/11-Q/12-Q, 80 runs / 40 paired seeds | Results register, predeclared experiment/statistical contracts, Drive S11-A CSV, manuscript ~599–637, ~719–1078 | A within tested scenario; C for external generalization | Predeclared 8 condition cells and five seeds, Student-t paired CI; no pseudo-replication, no pooled condition-wide causal effect, no general robustness/universal winner claim. |
| Exp13-Q five-method comparison | Results register / S11-B CSV; manuscript ~639–644 and ~1079–1209 | A (bounded comparison) | One predeclared high-churn condition and five methods; do not claim overall SOTA superiority. |
| Kubernetes 20-peer operational realization | Claim matrix / experimental contract; manuscript ~646–657 and ~1210–1245 | A (implementation); C for confirmatory improvement | Current manuscript correctly states paired performance CIs cross zero; Kubernetes supports execution/observability, not consistent performance gains or simulator replication. |
| Statistical claims and overhead | `04_STATISTICAL_CONTRACT.md`, `07_CLAIM_EVIDENCE_MATRIX.md`, S11-A CSV, manuscript ~1249–1319 | A for bounded claims | Delivery/delay gains in tested ControlSim conditions coexist with higher duplicates/forwards; five seeded runs per cell, not proof of broad statistical robustness. |

### 3. Material follow-up questions (not decisions to rerun)

**R1A-C1 — Selection robustness:** Do the paper's *actual* novelty claims require sensitivity for state-bin count/thresholds, action set, Q learning rate, exploration schedule or reward choice, beyond honest architectural justification and limitations? **No such sweeps were present in the inspected evidence.** If claims remain bounded, B may suffice; otherwise design a *prospective* minimal controlled sensitivity before changing science.

**R1A-C2 — Generality and scope:** Existing primary evidence uses BA(100,m=3), five seeds, fixed workloads; Kubernetes uses 20 peers and materially different pacing. Decide if current bounded scope is sufficient for Journal of Cloud Computing positioning without claims of topology-size robustness, realistic network latency or independent deployment superiority. Any new scalability/topology stress test requires a separate hypothesis/experiment gate.

**R1A-C3 — Implementation/parity spot checks:** Before R2 method closure, trace five action transformations, reward F=0 and next-decision transition, derived k=7 possibility, gamma/exploration constants and realized-neighbour constraint against active code and at least representative stored traces. The normative documents and prose are internally aligned, but full implementation readback was not performed in this initial pass.

**R1A-C4 — Comparator framing:** Related Work should explicitly compare verified published hybrid algorithms such as DC-SoC, yet must not substitute them for the actual AHBN controller underneath Q-AHBN. Check primary reference accuracy and discuss novelty as bounded outcome-attributed refinement rather than saying AHBN is already published.

**R1A-C5 — Scope-risk observation:** The inspected S11-B CSV indicates that some standalone benchmark methods can outperform Q-AHBN on specific outcomes at churn 0.40; current manuscript recognizes this and does not claim an omnibus ranking. Verify exact table/CSV parity when drafting. Do not defend weaker benchmark rankings with exaggerated novelty or altered baselines.

### 4. Section-level supervisor comment-to-change inventory

| Manuscript section / current lines | Supervisor controls | Required revision | Audit/acceptance check |
| --- | --- | --- | --- |
| Title, Abstract, Introduction ~202–221 | WA-01, WA-02 | Journal question, testable learning contribution, no thesis chronology, less repeated unpublished AHBN branding | Scientific dependency still accurately disclosed; no generic performance/scalability claims. |
| Related Work ~222–258 | WA-01, WA-02, WA-07 | Verify SOTA hybrid/learning mechanisms and explicit comparison gap; distinguish citations from actual experimental comparators | Credible primary citations; no literature method falsely described as Q-AHBN's base controller. |
| Q-AHBN Method ~259–593 | OC-01–03, WA-01, WA-03, WA-06 | Justify inherited 2–6 range and frozen thresholds, five actions and derived 1–7 range; evidence-grade 81 states, reward and hyperparameters | Frozen canonical-first ordering, traceability and no false parameter sweeps or convergence claims; R1A-C3 verification. |
| Experimental Methodology ~594–669 | WA-03, WA-06 | Make seed/run units, sensitivity versus fixed settings, comparator roles and reproducibility concise | Exact 80 primary runs and 40 pairs; separate Exp13-Q 25 and K8s 25; no pooled evidence or altered baselines. |
| Results ~670–1245 | WA-04, WA-06 | Reduce seven subsection headings where clear; keep individual failure/churn/heterogeneity and benchmark/K8s roles visible | Values/tables/CI and communication overhead unchanged; no removal of weak or null findings. |
| Discussion ~1246–1301 | WA-02, WA-04, WA-06 | Consolidate six headings and explain why bounded attribution learning is novel relative to deterministic baseline | Express condition-dependent advantage and cost, Kubernetes uncertainty and external competitor results. |
| Limitations, Conclusion ~1302–1337 and Declarations | WA-02, WA-05, WA-06 | Tighten scope and journal significance; preserve data DOI as dataset only and manuscript under-review status | No unsupported universal, optimality, lightweight-overhead, convergence or DOI-publication assertions. |

### 5. Decision and release conditions

- **JCC-R1 mapping/inventory: PASS for structural/comment/evidence-source inventory**, based on current GitHub and selected Drive CSVs, not exhaustive numerical/code audit.
- **JCC-R1A scientific adequacy: CONDITIONAL / OPEN**. Several A/B bounded conclusions are provisionally defensible; C1–C5 must be addressed or consciously scoped with explicit evidence before declaring the entire gate PASS. No demonstrated D at this point.
- **Q-AHBN parameter/experiment change decision: NOT MADE**. No new experiment, design change, retune, result rewrite, code action, citation insertion, Overleaf resolution or journal submission authorized.
- **Canonical AHBN:** frozen unchanged. **23 October 2026:** supervisor-ready editorial target only, to be reconsidered if C findings justify new science.
- **Next bounded gate:** JCC-R1A-C3 targeted code/trace parity plus R1A C1–C5 scientific sufficiency resolution, followed by R2 editorial rewrite *only if its dependent claims are evidence-safe*. Record explicit PASS/HOLD outcomes in this stage and read back every authoritative change.

**Git/Drive transaction boundary:** the only planned write in this audit is this controlled stage record in `wwiras/q-ahbn2`; thesis and manuscript repositories unchanged. User-provided Mac-local synced directories cannot be written through the remote connectors. Drive `output/` is storage, not automatic evidence promotion.


## JCC-R1A-C3 — Code-level parity finding and scientific HOLD (2026-10-12)

**Gate decision: FAIL for cross-environment Q-fanout contract parity; JCC-R1A HOLD / NOT CLOSED.** The targeted source audit uncovered a concrete contradiction requiring controlled investigation, rather than another unsupported assurance that existing implementation and manuscript match.

### Confirmed source contradiction

- Frozen contract `docs/02_QAHBN2_DESIGN_FREEZE.md` and manuscript `wwiras/QAHBN2-Manuscript/sn-main.tex` lines approximately 382–390 permit post-controller requested `k_Q` in {1,...,7}, derived from canonical AHBN {2,...,6} and one unit `FANOUT_DOWN`/`FANOUT_UP`. Historical Q-layer clipping to 6 is explicitly prohibited. Keep canonical AHBN unchanged.
- `qahbn2/learning.py`, lines 74–86, implements the correct five actions and permits 2→1 / 6→7. `qahbn2/controlsim_adapter.py`, lines 34–49, retains this output; `qahbn2/event_bridge.py`, lines 35–48, bounds realized forwarding by eligible targets, not an artificial learner cap.
- **Contradiction:** `qahbn2/kubernetes_adapter.py` lines **68–73** calls the same learner but then executes `k_q = max(2, min(6, int(k_q)))`. Thus learned `FANOUT_DOWN` on canonical 2 is reported as 2 instead of 1, and `FANOUT_UP` on canonical 6 is reported as 6 instead of 7, before eligible-target realization. This violates Q-layer action semantics independent of topology.
- `tests/test_k2_kubernetes_adapter.py`, lines approximately 37–48, currently *asserts* those clipped boundary outputs as expected, and therefore guards the noncanonical behavior rather than catching it. The same test checks only interior action cases at canonical k=3.
- Other inspected learner semantics appear aligned at source level: `learning.py` lines 17–25 action names/alpha/gamma/epsilon values, lines 45–55 3-bin state, lines 57–72 epsilon schedule, lines 97–111 reward and F=0 closure, lines 122–133 Q update; `transition.py` lines 70–99 same-peer successor, lines 112–118 F=0, lines 120–133 terminal/update consumption. These observations do not constitute an executed test pass.

### Scientific significance and required next action

**This is a verified implementation inconsistency, not evidence that the observed Kubernetes results must be recalculated or that a particular result is false.** Determine which code revision and image actually produced frozen Kubernetes formal data; inspect corresponding source/image provenance and representative trace boundary cases; identify how often k=1 or 7 was selected versus clipped, and whether observed results/claims were affected. Do not silently edit historical evidence or equate current GitHub main with an already-deployed image.

**Required controlled resolution:** (1) retrieve K8s producing commit/image digest and its adapter version; (2) audit method/decision/eligibility traces for boundary actions; (3) assess materiality and scope of any correction; (4) propose minimal future fix/test changes, including changing incorrect boundary assertions, only after scientific approval; (5) if evidence was affected, re-evaluate or rerun only under explicit protocol and preserve original outputs. No changes to frozen AHBN.

### C1/C2/C4/C5 disposition at this checkpoint

| Question | Decision | Rationale |
| --- | --- | --- |
| C1 parameter robustness | B / CONDITIONAL | Existing gamma sweep is direct bounded selection evidence; 81-state binning, action set, alpha, reward and epsilon are declared fixed designs, with untested alternatives disclosed in manuscript. No necessity for a sweep is established merely by absence; the supervisor's parameter rationale concern remains an editorial obligation. |
| C2 generality | B / CONDITIONAL | Existing 80-run ControlSim, one-condition Exp13-Q, and 20-peer Kubernetes support explicitly bounded claims; they do not justify network-size or cross-platform improvement claims. Additional scenario tests contingent on any intended stronger claim. |
| C3 source parity | **FAIL / BLOCKER** | Hard learner-side fanout clipping in Kubernetes adapter contradicts frozen Q-AHBN request boundary; deployment impact remains unknown. |
| C4 SOTA framing | OPEN / R3 dependency | DC-SoC exists in registered Exp13-Q reference comparator and manuscript citations, but a verified full SOTA literature comparison is not completed in this code audit. |
| C5 external benchmark | B / CONDITIONAL | S11-B registered evidence and manuscript distinguish one-condition benchmark from primary pairs and do not claim omnibus superiority; table-by-table final publication parity is still a release check. |

**Overall decision:** JCC-R1A remains **HOLD**, and science-change authorization remains **HOLD** pending deployment provenance/impact. Do not mark R2 Method or the manuscript's cross-platform algorithm-parity statement scientifically reconciled yet. Reassess the 23 October supervisor-ready date if evidence revalidation is needed. The pinned scientific baseline is a retained historical reference, not carte blanche to overwrite it. The present transaction is an audit/control-record update only.
