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


## JCC-R1A-C3 — Frozen deployment provenance and one-run trace confirmation (2026-10-12)

**Additional verified fact:** Preserved Kubernetes formal evidence `output/evidence/K8s-VAL-Q_Exp13-Q-K8s/q-ahbn-gke-29092026155435-k5q-formal/` has root `git_commit.txt` recording producing Git commit `7ad474c3a249fde58223f2abd5d54918b4bcbb9f` and `image.txt` recording `wwiras/q-ahbn2:k5q-formal-v2-20260929`. The results register pins image digest `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`. Fetching `qahbn2/kubernetes_adapter.py` **at that exact producing Git commit** confirms the same line-72 learner fanout clip `k_q = max(2, min(6, int(k_q)))`; this is not merely a later main-branch regression.

**Selected preserved per-run trace inspected:** `runs/seed42/qahbn2/logs.jsonl` in the frozen evidence family (retrieved as raw file; no edit). The JSONL audit read 3,214 `qahbn2_decision` event rows. Among them, 630 had canonical `k_ahbn=2`; 75 combined `k_ahbn=2` with selected `FANOUT_DOWN`, but logged `k_q=2` instead of contract-derived `k_q=1`. No canonical `k_ahbn=6` decision was observed in this one run, so its upper-bound case cannot be assessed from this run. This demonstrates an **exercised lower-bound contract violation in formal seed 42**, not only a latent bug. Counts are from this one inspected log, not all five formal seeds.

**Impact interpretation:** Affected requested fanout is confirmed; the size or even direction of the *performance impact* cannot be computed from that mismatch alone. Actual realized forwarding depends on eligible targets and decisions in a dynamic run. Original formal outputs and current publication metrics remain preserved and must not be re-labelled as results for a corrected 1–7 implementation. Do not claim corrected K8s implementation/parity, or that K8s proves the frozen Q-AHBN contract, until discrepancy resolved.

**Recommended controlled next gate — JCC-R1A-C3-D1:** audit the other four preserved Q-AHBN Kubernetes run logs for boundary-action frequency and classify original metrics explicitly as deployed clipped-variant evidence; inspect image/build digest provenance. Then prepare, but do **not** execute without approval, a minimal code-and-unit-test correction restoring learned 1–7 requests while leaving canonical AHBN untouched; design controlled validation, and determine whether a new Kubernetes run set and manuscript scope change are required. Existing ControlSim evidence and results are not invalidated by this identified Kubernetes-only clip, but still require ordinary parity/evidence checks.

**Gate status remains JCC-R1A HOLD / scientific modification HOLD / journal submission HOLD.** This is an audit-only stage transaction; no algorithm, test, frozen evidence, manuscript or data was modified.


## JCC-R1A-C3-D1 — Five-seed Kubernetes trace-impact assessment (2026-10-12)

**Gate:** JCC-R1A-C3-D1. **Execution:** read-only forensic audit of all five formally preserved Q-AHBN Kubernetes `logs.jsonl` objects, production code and contracts. **Decision:** `TRACE-EXTENT PASS / SCIENTIFIC PARITY FAIL / REVALIDATION DECISION: TARGETED CORRECTION AND VALIDATION SCIENTIFICALLY REQUIRED IF K8s IS RETAINED AS CANONICAL Q-AHBN EVIDENCE`. JCC-R1A overall remains HOLD; no new experiment executed or science changed.

### Authority and raw evidence

- Scientific repo `wwiras/q-ahbn2`; immutable science reference `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`. Canonical AHBN contract `docs/01_CANONICAL_AHBN_CONTRACT.md` remains FROZEN; Q design contract `docs/02_QAHBN2_DESIGN_FREEZE.md` expressly forbids the historical Q-layer `2..6` clipping and permits derived requested `1..7`.
- Preserved evidence Drive root `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5` / `output/evidence/K8s-VAL-Q_Exp13-Q-K8s/q-ahbn-gke-29092026155435-k5q-formal/runs/seed{42..46}/qahbn2/logs.jsonl`. Original Drive file IDs: seed 42 `1memXnCGv2l76Wtf9k-jfCktvxtfaT-5n`, 43 `1MGe6Jx6iCnJi3kfDu0M4cuZYSq9hm5Sz`, 44 `1k5Eb-ldT8BTSoa6RbxB2_ZUrF6CP-F_X`, 45 `1K5SW2cG38ooJV336iX14Hw6NFRtaPo8e`, 46 `1x-BTVeJ20eRaHR5MQS62mZBROW_bLcEC`.
- Formal run `git_commit.txt`: `7ad474c3a249fde58223f2abd5d54918b4bcbb9f`. Image `wwiras/q-ahbn2:k5q-formal-v2-20260929`; results-register digest `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`. Checked `qahbn2/kubernetes_adapter.py` at the producing Git SHA; line 72 executes `k_q = max(2, min(6, int(k_q)))`. No image rebuild or registry-digest recomputation was attempted here.
- **Parser note:** formal `logs.jsonl` includes occasional adjacent JSON objects concatenated on a physical line. Read each file in full and parse successive JSON objects with `json.JSONDecoder.raw_decode` instead of trusting one-JSON-record-per-line. The earlier 3,214 seed-42 count was a preliminary undercount: corrected to **3,218** complete decision objects. Four additional objects do not change the previously reported **75** clipped decisions. Parser reported zero malformed remainder lines for all five audited logs.

### All five preserved Q-AHBN run traces: observed clipped requests

| Seed | Parsed `qahbn2_decision` records | `k_AHBN=2` / `FANOUT_DOWN` / logged `k_Q=2`, expected 1 | Of clipped: nonempty eligible/realized targets | Of clipped: empty eligible/realized targets |
| --- | ---: | ---: | ---: | ---: |
| 42 | 3,218 | 75 | 33 | 42 |
| 43 | 1,065 | 28 | 14 | 14 |
| 44 | 2,494 | 81 | 57 | 24 |
| 45 | 4,774 | 201 | 37 | 164 |
| 46 | 5,583 | 338 | 226 | 112 |
| **TOTAL** | **17,134** | **723 (4.22%)** | **367** | **356** |

Every identified mismatch was exactly the *lower* clipping combination `k_AHBN=2`, action `FANOUT_DOWN`, observed `k_Q=2` instead of contract request 1, and all were logged in `mode_q=structured`. No canonical `k_AHBN=6` appeared in these five logs, therefore an **upper-bound action 6→7 is not empirically assessed** by this evidence (although code would clip it). These counts refer to **decision records, not independent delivered messages, and not measured performance impact**.

### Interpretation and impact boundary

1. **Observed request deviation is PROVEN and repeated in all five formal runs.** The producing Git commit includes the clip, and the preserved formal traces show affected decisions. Therefore the frozen 25-run Kubernetes family cannot be characterized as fully implementing the canonical Q-AHBN `1..7` requested-fanout contract.
2. **Transmission/metric effect is NOT measured here.** For 367 affected decisions eligible/realized targets were nonempty; for 356, none were present. Some Structured-mode realizations may be topology/cluster constrained or insensitive to budget. The imported inherited selector must be independently traced with budget 1 versus 2 before inferring any change to actual sends, delivery, duplicates or delay. Never treat 723 decisions as 723 changed transmissions.
3. **Original Kubernetes metrics remain valid observations of the deployed clipped variant**, subject to their existing metric caveats, not confirmatory performance evidence for the canonical 1–7 variant. Their quantitative counterfactual cannot be derived by simply subtracting sends or adjusting aggregates.
4. **ControlSim evidence remains a separate primary family** and is not invalidated by this Kubernetes adapter defect. Maintain existing n=5 scope and overhead limitations. AHBN controller/source/frozen outputs must not change.

### Decision, options and next controlled gate

**Decision D1:** It is scientifically necessary to correct the Q-layer clipping and validate the intended boundary **before claiming full cross-environment implementation parity**. This is not an approval to edit code or rerun GKE yet. If the manuscript retains Kubernetes as implementation evidence for the *canonical* Q-AHBN scheme, recommend an authorized minimal adapter + incorrect-test-assertion fix and formal controlled revalidation. The historical clipped results stay immutable and labelled historical. An alternative editorial choice is to describe the deployed variant explicitly as clipped and limit or remove cross-environment parity/operational generalization claims, but this does not satisfy a claim that the complete frozen Q-AHBN contract was deployed.

**NEXT: JCC-R1A-C3-D2 — Structured target-selector semantic/impact audit and controlled correction/revalidation proposal.** Inspect producing commit's inherited `structured_selector` behavior under budgets 1 vs 2, review actual eligible sets and trace realization, then prepare a narrow source/test patch in a distinct future version and a minimal deterministic/K8s validation contract for researcher execution, including effect on claims and 23 October internal target. No modification, rerun, result promotion or submission authorization has been issued by D1.

**Transaction:** stage-document-only GitHub update. `docs/00_QAHBN2_MASTER.md` §9.5 requires source reconciliation, scope-bounded audit, explicit verdict, minimum file sync, and postwrite readback. Do not edit Master, results/statistics contracts, manuscript or experiment code merely to restate a HOLD. Mac local Google Drive paths are references only; no direct local modification. **JCC-R1A HOLD; SCIENCE CHANGES HOLD; JOURNAL SUBMISSION HOLD.**


## JCC-R1A-C3-D2 — Structured Target-Selector Semantic and Impact Audit (12 October 2026)

**Gate outcome:** SOURCE-SEMANTIC AUDIT PASS; IMPACT IDENTIFIABILITY PARTIAL; SCIENTIFIC PARITY HOLD. This controlled action makes no algorithm, experiment, result, manuscript, or canonical AHBN changes.

### 1. Authority and exact deployed code

- Repository-first audit follows `docs/00_QAHBN2_MASTER.md` §9.5. Scientific reference baseline remains `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`; AHBN stays frozen.
- Formal Kubernetes evidence identifies producing Git revision `7ad474c3a249fde58223f2abd5d54918b4bcbb9f`, image `wwiras/q-ahbn2:k5q-formal-v2-20260929` and registered digest `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`.
- At the producing revision, `qahbn2/kubernetes_adapter.py` lines 68–73 clips `k_q` to 2–6 **before target selection**.
- At that revision, `gke/app/qahbn2_runtime.py` lines 104–110 calls `realize_inherited_targets` and passes `structured_selector=lambda s, budget: self.cluster_targets(s, fanout=budget)`. `qahbn2/kubernetes_integration.py` lines 30–36 invokes that structured selector with `q.k_q`; it does not independently apply a cap.
- At that revision, `gke/app/peer.py` lines 370–398 implements the actual `cluster_targets(sender_id, fanout)` semantics. These exact sources, not a hypothetical generic fanout sampler, govern the frozen Kubernetes observations.

### 2. Deterministic selector semantics: requested budget 2 versus 1

| Sender role and inherited candidate condition | Existing clipped request `k_Q=2` | Contract request `k_Q=1` | Difference |
| --- | --- | --- | --- |
| Cluster head, >=2 ordered eligible candidates | first 2 candidates | first 1 candidate | **One target omitted**; first target unchanged |
| Cluster head, exactly 1 ordered candidate | same 1 candidate | same 1 candidate | No target difference |
| Cluster head, 0 ordered candidates | none | none | No target difference |
| Non-cluster-head with available parent CH other than sender/self | single parent CH | single parent CH | No target difference; branch does not depend on fanout |
| Non-cluster-head with unavailable/ineligible CH | none | none | No target difference |

For cluster heads, `cluster_targets` builds a deterministic ordered list: first available gateway (if any), then available cluster members, then remaining gateways. It returns `selected[:max(1, int(fanout))]`. A 2→1 request can therefore remove **exactly one** target only when at least two such structural candidates exist. Non-CH senders return either their single parent CH or an empty list, regardless of requested fanout. This is a source-semantic counterfactual, *not* a replay of observed propagation or learned Q trajectories.

### 3. Five-seed formal trace reconciliation and limits

JCC-R1A-C3-D1 established **723** logged lower-bound mismatches among **17,134** Q decisions over seeds 42–46: 75, 28, 81, 201, 338 respectively (4.22% pooled). All were Structured-mode `k_AHBN=2`, action `FANOUT_DOWN`, recorded `k_Q=2` rather than expected 1; upper 6→7 was not exercised in those formal logs. Of these, 367 had nonempty reported realized targets and 356 none.

**Important correction to impact reasoning:** Nonempty realized targets is **not enough** to prove a transmission would disappear under 1: the non-CH branch ignores the budget, and CH senders with one candidate are unchanged. Precise affected-selection frequency requires correlating decision `peer_id` and point-in-time CH role/topology/availability with the *ordered inherited candidate list* and selected targets. Do **not** call the 367 cases changed transmissions; do not use a speculative number as the outcome.

The formal logs record actual clipped-variant decisions and attempts. They do not contain an independently executed corrected 1–7 learning trajectory. An isolated deterministic selector counterfactual cannot supply corrected delivery, propagation delay, duplicates, rewards, or learning evolution: changing one target can change later peer observations, Q updates, and message histories.

### 4. Decision and narrow correction/validation proposal (NOT authorized execution)

**Scientific finding:** the selector is **budget-sensitive for cluster heads with >=2 candidates**, but budget-insensitive for non-cluster-head senders and CHs with <=1 candidate. Hence the code-level clipping is materially capable of altering network transmissions; it cannot be dismissed as operationally inert, but no quantitative delivery/performance effect is established.

**Recommended proposed code correction**, only following a separately authorized change gate: remove the noncanonical `max(2, min(6, ...))` clip from `qahbn2/kubernetes_adapter.py`, preserving `learner.refine` output; correct `tests/test_k2_kubernetes_adapter.py` boundary expectations to 2→1 and 6→7, add deterministic CH selector cases for >=2, exactly 1, zero candidates and non-CH cases, and verify `k_real <= min(k_Q, |N_e|)` without altering canonical AHBN. No broad learner retuning or ControlSim rewrite.

**Proposed validation sequence:** (1) review producing-image and test provenance; (2) targeted deterministic tests + full relevant K8s regression, including action/transition/reward contracts; (3) explicit independent candidate image/digest; (4) controlled matched Kubernetes formal rerun only if intended canonical Q-AHBN operational/performance claim is retained, preserving the historical clipped 25-run results and comparators unchanged; (5) new statistical/provenance audit and manuscript wording harmonization. A reduced smoke test cannot by itself replace matched formal evidence for a performance claim. Actual execution remains with researcher after scope approval.

**23 October decision:** date remains an internal supervisor-ready *target*, not scientific closure. If the formal rerun cannot be validated by then, either disclose the historical K8s variant and narrow/remove canonical K8s parity claims in the manuscript, or keep the manuscript release on HOLD. Never mask the inconsistency to meet the date.

**Current state:** JCC-R1A-C3-D2 SOURCE AUDIT PASS / PERFORMANCE IMPACT UNDETERMINED / JCC-R1A HOLD / SCIENTIFIC CODE CHANGES HOLD / JOURNAL SUBMISSION HOLD. **Next gate:** JCC-R1A-C3-D3 — point-in-time peer-role and candidate-set evidence reconciliation, followed by explicit scientific change/validation authorization decision. No direct access to the supplied Mac synchronized paths was claimed, and Drive synchronization alone is not evidence promotion.


## JCC-R1A-C3-D3 — Point-in-Time Peer-Role and Candidate-Set Evidence Reconciliation (2026-10-12)

**Gate verdict: POINT-IN-TIME SELECTION-IMPACT RECONCILIATION PASS / PERFORMANCE IMPACT UNDETERMINED. JCC-R1A stays HOLD.** This gate used read-only GitHub/Drive evidence; it has not executed a corrected Q-AHBN run and does not authorize code or result modification.

### Authority and audit method

- Applied `docs/00_QAHBN2_MASTER.md` §9.5: fetch → reconcile controlling gate → audit evidence → adjudicate → update only changed stage → post-write readback. Pinned science reference `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` untouched; AHBN canonical controller frozen.
- Source authority: formal image-producing repository revision `7ad474c3a249fde58223f2abd5d54918b4bcbb9f`, code `gke/app/peer.py` `cluster_targets`, `gke/app/qahbn2_runtime.py` selector delegation, `qahbn2/kubernetes_integration.py`, and `qahbn2/kubernetes_adapter.py`. Image tag `wwiras/q-ahbn2:k5q-formal-v2-20260929`; registered image digest `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`.
- Original Drive evidence per seed: `runs/seed{42..46}/qahbn2/logs.jsonl` and `topology_role_mapping.json`, under `output/evidence/K8s-VAL-Q_Exp13-Q-K8s/q-ahbn-gke-29092026155435-k5q-formal/`. Log file IDs by seed: 42 `1memXnCGv2l76Wtf9k-jfCktvxtfaT-5n`, 43 `1MGe6Jx6iCnJi3kfDu0M4cuZYSq9hm5Sz`, 44 `1k5Eb-ldT8BTSoa6RbxB2_ZUrF6CP-F_X`, 45 `1K5SW2cG38ooJV336iX14Hw6NFRtaPo8e`, 46 `1x-BTVeJ20eRaHR5MQS62mZBROW_bLcEC`. Topology mapping IDs: 42 `1mKhjTlr9HAGtN6ZW4gLWLtsiQzcBVbri`, 43 `1AtsVwv4C8IiuuJAxxxCGgKltma4P2x01`, 44 `16Hln6FiMSrJ4pkY9G5rOY-KlxZehCejI`, 45 `17Zg1fO-6BcXq0SG0WIg3b8uRDAO4XEhz`, 46 `11LPWsbdRYe86B4w62KZKvdF5_PVjNva2`.
- For each affected `qahbn2_decision` (`k_ahbn=2`, `action=FANOUT_DOWN`, logged `k_q=2`, `mode_q=structured`), join `peer_id` to the same-seed topology `nodes[peer_id].is_cluster_head`. Verify every recorded `peer_started` event's `is_cluster_head` agrees with that topology (40 startup/restart events per seed, zero role mismatches in the audit). Then inspect the recorded **point-in-time `realized_targets`** and source selector. The logs' structured `eligible_targets` records are the returned structural target list, **not an independently reconstructed full candidate pool**.
- Read full preserved JSONL data using repeated JSON decoding per physical line to handle adjacent objects. This reconciles the D1 17,134 decision total. No raw evidence was rewritten, reordered, or promoted; analysis was independent of live Kubernetes.

### Audited results: immediate target selection under budget 1 vs logged clipped budget 2

| Seed | Q decisions | Restricted 2→1 requests prevented | CH decisions with exactly two selected targets: **one omitted** under budget 1 | Non-CH decisions: **same targets** under budget 1 |
| --- | ---: | ---: | ---: | ---: |
| 42 | 3,218 | 75 | 13 | 62 |
| 43 | 1,065 | 28 | 4 | 24 |
| 44 | 2,494 | 81 | 33 | 48 |
| 45 | 4,774 | 201 | 11 | 190 |
| 46 | 5,583 | 338 | 90 | 248 |
| **Total** | **17,134** | **723** | **151** | **572** |

- All **151** affected CH records had `len(realized_targets)=2` (and two listed structured `eligible_targets`). In `gke/app/peer.py` the CH selector deterministically orders first available gateway, then members, then remaining gateways, and returns the first `max(1, fanout)` targets. Therefore **the first target remains and exactly the second recorded target is omitted** in a same-instant, otherwise identical 2→1 counterfactual. Example seed 42 CH peer 0 decision `gke:0:m2:2`: recorded targets `[5,2]`; counterfactual budget 1 selects `[5]`.
- The other **572** restricted decisions came from ordinary cluster members. Their selector returns the single eligible parent CH or no target without consulting the `fanout` argument; at the same instant a budget of 1 produces the **same selected-target list**. Across those 572 records, 216 had one parent target and 356 had none.
- No restricted decision was classified as CH with 0 or 1 realized target in these five runs. Per-seed topology had CH IDs `[0,5,10,15]`, and all observed `peer_started` role fields matched role mapping; the frozen Q-AHBN runtime did not emit a role-reassignment/reclustering event in these logs. Cluster-peer availability may change with churn but the **logged selected targets already reflect availability at selection time**, so this classification does not assume all peers stayed available.
- Fractions: 151/723 = **20.9%** of clipped decision records were selection-sensitive; 151/17,134 = **0.88%** of all logged Q decisions. These are **decision-level counterfactual selections**, not 151 guaranteed additional network sends or independent messages. Multiple decisions can pertain to one message; actual send attempts, ACKs, later paths, Q rewards and dynamic feedback require a genuinely corrected run for causal effect.

### Evidence limitations and release decision

**Completed scope:** selected-target counterfactual is identifiable exactly from source selector + preserved role mapping + two-target lists for each recorded lower-bound case. No external full pre-selection candidate list is needed for the first-two-versus-first-one conclusion. Source/trace alignment is established at the role and target-selection level; no executed forward/ACK causal replay, delivery recomputation, code build or corrected GKE deployment occurred.

**Scientific conclusion:** The Kubernetes clip is **operationally material for the forwarding decision mechanism** in 151 observed CH decisions, even though the downstream performance delta is unknown. The other 572 lower-bound violations are logged Q-action violations but have no immediate selection effect in Structured mode. Therefore do not dismiss the clip as universally harmless, nor portray 151 as corrected performance or corrected-send totals. In particular historical cloud results remain evidence of the deployed *clipped variant* only. ControlSim and canonical AHBN remain unchanged.

**Decision:** JCC-R1A-C3-D3 targeted evidence gate **PASS**; overall JCC-R1A **HOLD** pending a separate science-change/validation authorization decision. Recommendation is to prepare a minimal versioned Q-Kubernetes adapter + boundary-test correction, preserve the historical formal run set, and authorize matched revalidation only if the manuscript retains canonical Kubernetes realization claims. If revalidation cannot be completed defensibly by **23 October 2026**, either explicitly identify the historical restricted variant and narrow/remove unsupported parity claims, or hold supervisor release. No retroactive alteration of frozen results, baseline or citations.

**NEXT CONTROLLED GATE: JCC-R1A-C3-D4 — Controlled Correction and Validation Authorization Decision.** Prepare exact diff scope, deterministic tests (CH budget 1/2; non-CH; ±1 at endpoints; F=0/reward lifecycle), producing-image provenance and matched-run comparison plan; request researcher authorization before code writes or cloud execution. JCC-R2 affected scientific prose remains locked; journal submission HOLD. User Mac-synced paths cannot be directly mutated by this connector transaction.



## JCC-R1A-C3-D4 — Controlled Correction and Validation Authorization Decision (2026-10-12)

**GATE VERDICT: PLAN / SCIENTIFIC REMEDIATION NEED ESTABLISHED; IMPLEMENTATION AND EXPERIMENT EXECUTION NOT YET AUTHORIZED.** The D3 evidence has identified 723 lower-bound Q-request discrepancies across five formal Q-AHBN Kubernetes seeds and 151 immediate Structured cluster-head selections that would omit the second target with a true requested fanout of 1. These are decision-level counterfactuals; performance impact, changed completed transmissions, changed rewards and corrected learning trajectory remain unmeasured. We therefore require a narrow, explicitly versioned correction and validation *if* the manuscript will retain a claim that Kubernetes realizes the frozen complete Q-AHBN algorithm. This administrative D4 does not itself approve source edits, a Docker build, GKE spending, a GKE rerun or evidence replacement.

### 1. Authority and frozen boundaries

- GitHub source of control: wwiras/q-ahbn2. Historical scientific reference pinned at commit \`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68\`. The canonical AHBN controller (observation signals, EWMA, z-score, mode switching and S5 2–6 fanout) is immutable. **Do not modify AHBN, learner reward, action space, Q learning rates, epsilon schedule, topology, churn semantics or statistical contract as a side effect of this fix.**
- Historical K5-Q producing Git commit: \`7ad474c3a249fde58223f2abd5d54918b4bcbb9f\`; image \`wwiras/q-ahbn2:k5q-formal-v2-20260929\`, digest \`sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e\`. These and the original Drive artifacts are **historical clipped-variant evidence**, never revised in place.
- Runtime chain verified: \`qahbn2/learning.py:refine()\` → \`qahbn2/kubernetes_adapter.py:decide()\` → \`qahbn2/kubernetes_integration.py:realize_inherited_targets()\` → \`gke/app/qahbn2_runtime.py\` → inherited \`gke/app/peer.py:cluster_targets()\`. The source-level defect is precisely the extra adapter clip, not the underlying canonical AHBN actuator.
- Relevant published/frozen plans in \`docs/03_EXPERIMENT_CONTRACT.md\`, \`docs/stages/K5_Q_K8S_FORMAL_VALIDATION.md\`, \`gke/app/k5_q_formal_contract.py\`, \`gke/experiments/k5_q_formal.yaml\`, \`gke/scripts/build_k5_q_formal_image.sh\` and \`gke/scripts/run_k5_q_formal.sh\` were rechecked. The historical formal matrix was 5 methods × seeds 42–46 = 25 runs, with N=20, BA(m=2), four prescribed churn cycles, 240 messages at 0.4 s. Retain its frozen identity. The relevant configured AHBN bound shown by generated formal topologies may be 2–4 while the canonical S5 source contract remains 2–6; do not silently conflate them when verifying baseline compatibility.

### 2. Prospective minimal correction specification — no code written at D4

| Path | Precisely permitted candidate change | Prohibited |
| --- | --- | --- |
| \`qahbn2/kubernetes_adapter.py\` | Remove the explanatory comment claiming post-Q fanout support is restricted to 2–6 and the line \`k_q = max(2, min(6, int(k_q)))\`. The immutable \`learner.refine()\` output must flow unmodified into \`KubernetesQDecision.k_q\`. | New learning policies, additional Q cap, changed base S5, changed action semantics. |
| \`tests/test_k2_kubernetes_adapter.py\` | Change only the two boundary oracle expectations: \`FANOUT_DOWN\` from canonical 2 ⇒ requested 1, and \`FANOUT_UP\` from canonical 6 ⇒ requested 7. Extend endpoint tests in both modes if needed. Keep current interior five-action, attribution, F=0, successor, terminal tests. | Deleting failed tests or treating 2 and 6 as compliant learned endpoints. |
| Additional focused tests, only as necessary | Deterministic inherited selector: CH ordered targets with 0, 1 and ≥2 eligible candidates; budget 1/2 target-prefix behavior; non-CH parent-target/no-parent cases; realized target bound; ensure no post-refinement clip in full integration. Include explicit example CH recorded [5,2] → candidate [5], without claiming this reproduces dynamic rewards. | Rewriting the inherited Structured topology/target-selection algorithm, changing comparators or synthetic network workloads. |
| Other files | Only mechanical build/test metadata and an explicit candidate-version/provenance record if needed for reproducibility. | Editing historical logs, K5 published validation, frozen AHBN, ControlSim or baseline results. |

**Implementation verification order:** (i) inspect exact current GitHub HEAD and clean candidate worktree; (ii) create a distinguishable prospective candidate from the latest authoritative source (researcher's preferred main-only workflow is acceptable only with separate immutable candidate Git SHA and image tag, not alteration of a pinned historical ref); (iii) review the exact minimal diff; (iv) run focused tests and regression suites; (v) check source-level action parity against ControlSim while keeping AHBN static; (vi) only after gate-specific approval build/push a fresh linux/amd64 image and verify actual image digest/imports. Unit test changes are *necessary* but not sufficient to claim cloud equivalence.

### 3. Proposed test and validation contract

**TEST / GATE:** JCC-R1A-C3-D5 — Q-Kubernetes fanout-boundary candidate correction and deterministic validation (**proposed, not yet released**).  
**OBJECTIVE:** Restore post-AHBN Q requested-fanout 1–7, verify mode-specific target realization, preserve all canonical and learning contracts.  
**AUTHORITATIVE GITHUB COMMIT:** Candidate commit SHA to be assigned **after explicit researcher approval**, with historical producer \`7ad474c3a249fde58223f2abd5d54918b4bcbb9f\` retained as comparison.  
**AUTHORITATIVE CONTRACT:** \`docs/01_CANONICAL_AHBN_CONTRACT.md\`; \`docs/02_QAHBN2_DESIGN_FREEZE.md\`; \`docs/03_EXPERIMENT_CONTRACT.md\`; this D4 decision and existing K4/K5/K6 Kubernetes freeze boundaries.  
**EXECUTION ENVIRONMENT:** First deterministic Python/CI on clean verified source; next Docker linux/amd64 preflight; finally researcher-managed GKE only after separate release.  
**RUN DIRECTORY:** New timestamped \`output/evidence/JCC-R1A-C3-D5-<timestamp>/\`; never historical \`q-ahbn-gke-29092026155435-k5q-formal/\`.  
**EVENT TYPE:** \`qahbn2_decision\`, structured/gossip eligible and realized target records, direct forwarding outcome, terminal/successor, test/provenance manifests.  
**PARAMETERS:** Entire Q-learning and canonical AHBN scientific parameter set unchanged; only correct the unintended adapter-side requested-fanout clip. Explicit endpoint requests 2→1 and 6→7.  
**SEEDS / REPETITIONS:** Focused deterministic unit/regression tests; existing formal GKE seeds 42–46 only if a prospective new formal run is separately authorized. Never choose subset or seeds in response to favorable outcomes.  
**EXPECTED OUTPUTS:** Test results, exact file diff, candidate Git SHA, lower/upper endpoint traces, selector cases, image tag/digest/preflight, run manifests and per-run raw data only if authorized.  
**USER EXECUTION COMMAND:** At D5 release, derive and read back exact commands from approved candidate SHA; proposed local unit entrypoint \`PYTHONPATH=. python3 -m unittest tests.test_k2_kubernetes_adapter\`; do **not** issue a runnable GKE command or claim a build passed before candidate authorization.  
**EVIDENCE LOCATION:** Candidate-specific local output; preserve to science Drive only after validity/completeness/provenance verification; historical Drive evidence remains untouched.  
**COMPLETENESS CHECK:** All endpoint/selector/ledger cases and every authorized experimental coordinate; no missing seed, metric, manifest, provenance SHA or digest.  
**VALIDITY CHECK:** Requested Q fanout 1–7; unchanged canonical 2–6; \`k_real <= min(k_Q, |N_e|)\` under applicable mode semantics; intact learning lifecycle and no F=0 updates; consistent topology/churn/source/message workload.  
**RESULT:** Not executed.  
**SCIENTIFIC INTERPRETATION:** Deterministic parity alone cannot estimate new deployment delivery/delay/duplicates/forwarding or re-learning path.  
**GITHUB STATUS UPDATE:** D4 proposal record only; D5 remains HOLD pending researcher authorization.  
**NEXT CONTROLLED GATE:** D5 explicit researcher authorization and implementation/test preparation.

### 4. Minimum defensible subsequent GKE validation — conditional plan, not a released experiment

**Option A (preferred if retaining canonical operational validation):** With separately approved candidate and passing lower-risk gates, run a **new five-seed Q-AHBN Kubernetes cell** matching the frozen 20-peer BA(m=2) churn scenario and seeds 42–46, using the same 240-message schedule, defined source, churn offsets, topology generation, metrics and eligibility semantics. It must be independently versioned, fully manifested, validated and preserved. Baseline AHBN comparisons may reference historical identical protocol evidence **only if** matched-run compatibility, image/infra/time conditions and comparator invariance are rigorously established; otherwise re-run the minimal matched AHBN reference cell (5 more runs). For a **new five-method comparison**, repeat the 25-run matched matrix prospectively or explicitly qualify why non-rerun historical comparators remain a legitimate reference—never present old mixed-image runs as one newly executed contemporaneous 25-run study without qualification. Baseline/comparator choice and analytic plan must be frozen **before** inspecting corrected performance outcomes.

**Option B (if no fresh scientific rerun is released):** State that the historical GKE deployment was a restricted Q request 2–6 implementation with 151 same-instant CH decisions potentially changing a forwarding target, and **withdraw or narrow claims of full canonical Q-AHBN operational parity**. The old results may be reported *as deployed-variant observations*, with the discrepancy disclosed and no mislabelling as corrected 1–7 evidence.

The original 25-run evidence is never erased, pooled naively with prospective results or post-hoc “corrected” by subtracting 151 sends. Five seeds remain a small bounded Kubernetes operational validation, not new proof of universal robustness or performance superiority. Use delivery, delay, duplicates, total forwards, churn/recovery and paired statistical intervals wherever estimable; retain null/negative outcomes.

### 5. Approval and release logic

1. **D4 finding — PASS (plan quality / scientific decision):** correction is warranted **if canonical Kubernetes parity is a retained manuscript claim**, because a verified 151 same-instant target-selection sensitivity rules out dismissing the clip as purely cosmetic.
2. **Code-change authorization — HOLD:** user has requested a plan/authorization decision **before any code is changed**, but has not explicitly approved the new science or GKE expenditure. Do not interpret “next controlled action” as blanket permission to execute a candidate correction or full formal rerun.
3. **Scientific experimental release — HOLD:** no new code/test run, image build, GKE formal run, results/register rewrite, or journal submission is approved by D4.
4. **23 October 2026 internal target — CONDITIONAL:** supervisor-ready editorial package only. If candidate and prospective validation cannot meet evidentiary standards, use transparent restricted-deployment wording or move affected release; do not substitute a smoke test for formal paired performance evidence.
5. **Master reconciliation:** \`docs/00_QAHBN2_MASTER.md\` §9.5 says update only records whose authoritative states change. D4 creates a new *stage-local conditional correction plan*, so update this stage only, keeping project-wide Master, experiment/statistical/results/claim registers, manuscript, code, Drive evidence and researcher Mac synced directories unmodified until subsequent authorized decisions.

**Final D4 status:** **PLAN/FINDING PASS; Q-AHBN CODE CORRECTION NOT AUTHORIZED; NEW K8s EVIDENCE NOT AUTHORIZED; JCC-R1A HOLD; JOURNAL SUBMISSION HOLD.** **Next controlled gate: JCC-R1A-C3-D5 — Authorize prospective minimal adapter/test candidate and local deterministic verification, or formally select restricted-variant manuscript treatment.**



## JCC-R1A-C3-D5 — Authorized Minimal Kubernetes Adapter Correction and Local Deterministic Test Release (2026-10-12)

**Decision:** RESEARCHER AUTHORIZATION TO CORRECT Q-KUBERNETES ADAPTER AND BOUNDARY TESTS ACCEPTED; **PATCH READBACK PASS; LOCAL DETERMINISTIC EXECUTION RELEASED / NOT EXECUTED; D5 GATE HOLD PENDING TEST EVIDENCE**. The user explicitly instructed pursuit of the D5 minimal correction and local deterministic tests, while reserving Docker build, GKE deployment and all cloud/formal runs for separate future gates. Nothing in this action reopens immutable canonical AHBN.

### 1. Repository-first reconciliation and exact code change

Controlling workflow: \`docs/00_QAHBN2_MASTER.md\` §9.5 GitHub-first gate process and §9.5.2 test-record grammar. Latest pre-change GitHub main: \`94be77dd45fb95d26b198ab9280772509696ec4f\`; latest GitHub files independently read before edits. Science pinned historical baseline remains \`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68\`, with formal historical GKE producer \`7ad474c3a249fde58223f2abd5d54918b4bcbb9f\`.

Authorized edits implemented on the repository's existing \`main\` branch (researcher preference for minimal branches):

| GitHub change | Minimal diff and purpose | Commit/readback |
| --- | --- | --- |
| \`qahbn2/kubernetes_adapter.py\` | Removed only the incorrect “after refinement remains within 2..6” comment and \`k_q = max(2, min(6, int(k_q)))\`. The existing \`mode_q, k_q = self.learner.refine(...)\` output now propagates directly to \`KubernetesQDecision\`. | \`7343b137fd8b37af3b40331fae16ee36ce861e23\`; exact-content and Git blob SHA readback PASS |
| \`tests/test_k2_kubernetes_adapter.py\` | Corrected exactly two endpoint assertions: AHBN 2 + \`FANOUT_DOWN\` must request 1; AHBN 6 + \`FANOUT_UP\` must request 7. The existing interior action, ACK/new/duplicate/failure, F=0, successor, terminal and selector delegation tests remain intact. | \`e9b4e6eb7e9bd54be55caf4da8e97639fc639da7\`; exact-content and Git blob SHA readback PASS |

**No** code change to \`qahbn2/learning.py\`, \`qahbn2/transition.py\`, ControlSim, \`gke/app/peer.py\`, inherited selector, GKE harness/configuration, frozen canonical AHBN, experiment/statistics/claim/results contracts, manuscript, raw logs or Drive contents. No unapproved Q retuning, action-set changes, extra range caps or scientific result modifications.

The corrected source has **not yet been executed or integration-tested**. Repository readback verifies text and exact diff scope only; it does not establish runtime PASS or prove an image contains this code.

### 2. Released deterministic test contract — researcher executes locally

**TEST / GATE:** JCC-R1A-C3-D5 deterministic correction verification.  
**OBJECTIVE:** Verify Q fanout request 2→1 and 6→7, unchanged interior five-action behavior and learning attribution, and absence of regressions.  
**AUTHORITATIVE GITHUB COMMIT:** \`e9b4e6eb7e9bd54be55caf4da8e97639fc639da7\` (code commit \`7343b137fd8b37af3b40331fae16ee36ce861e23\` is its parent). After the stage bookkeeping commit, local researcher must pull current HEAD and record actual SHA; no unverified hash should be substituted.  
**AUTHORITATIVE CONTRACT:** \`docs/01_CANONICAL_AHBN_CONTRACT.md\`; \`docs/02_QAHBN2_DESIGN_FREEZE.md\`; D1–D4 source/trace findings; this D5 record.  
**EXECUTION ENVIRONMENT:** Researcher's supplied Mac Google Drive-synchronized scientific workspace, local Python and relevant installed dependencies. No GKE or Docker.  
**RUN DIRECTORY:** New \`output/evidence/JCC-R1A-C3-D5-<UTC timestamp>/\` per new local test session; \`output/\` remains ignored/unpromoted until deliberate artifact validity and preservation.  
**EVENT TYPE:** Python unittest deterministic Q-adapter endpoint/ledger and cross-module integration test events; no network workload.  
**PARAMETERS:** Inherited canonical fanout 2–6 (unchanged); Q requested fanout 1–7; unchanged 81 states, five actions, reward/discount/learning/exploration.  
**SEEDS / REPETITIONS:** Deterministic local tests, no extra research seeds or K8s formal runs.  
**EXPECTED OUTPUTS:** Full command transcript, unittest test counts/results, exact Git HEAD and working-tree status, focused endpoint proof, identified test failures/dependency errors if any; preserve exit codes.  
**USER EXECUTION COMMAND:**
\`\`\`bash
cd "/Users/wwiras/Library/CloudStorage/GoogleDrive-samsuddin.samsuddin@monash.edu/My Drive/PhDResearch/myResearch/NewAlgorithm-AHBN/AHBNcode/q-ahbn2"
git pull --ff-only
git rev-parse HEAD
git status --short
mkdir -p "output/evidence/JCC-R1A-C3-D5-$(date -u +%Y%m%dT%H%M%SZ)"
PYTHONPATH=. python3 -m unittest -v tests.test_k2_kubernetes_adapter
PYTHONPATH=. python3 -m unittest discover -s tests -p 'test_*.py'
\`\`\`
Capture real command outputs and exit statuses within the newly made timestamped D5 directory using the researcher's usual local transcript tooling before treating evidence as frozen. A shell command simply printed in GitHub does **not** count as performed.  
**EVIDENCE LOCATION:** Designated timestamped local \`output/evidence/\` directory; promotion to scientific Drive requires later explicit validation, upload/preservation and readback.  
**COMPLETENESS CHECK:** Current SHA must contain both patched files, full test list/result counts and clean expected source status. Inspect endpoints 2→1, 6→7 and existing actions/attribution/F=0/same-peer successor/terminal tests; additional CH selection edge-case tests may be added under separately reconciled scope if focused tests reveal gaps.  
**VALIDITY CHECK:** No canonical AHBN changes; learner output not reclipped; eligible realization constraints preserved; no old assertion accepting 2 and 6 at Q endpoints; no regression test suppression.  
**RESULT:** Source + test-oracle correction COMMITTED/READBACK PASS; tests **NOT RUN / AWAIT RESEARCHER**.  
**SCIENTIFIC INTERPRETATION:** Source correction removes the known invalid cap. It does not establish corrected Kubernetes deployment metrics or downstream performance.  
**GITHUB STATUS UPDATE:** D5 patch prepared; formal D5 PASS withheld until actual local output and evidence verified.  
**NEXT CONTROLLED GATE:** JCC-R1A-C3-D5-T1 — inspect local deterministic regression output and source/trace proof; if PASS, release separate D6 container/image preflight proposal, **not** direct cloud execution.

### 3. Experimental firewall and publication boundary

The prior frozen 25-run (five methods × five seeds) Kubernetes evidence retains its unmodified historical/clipped-variant provenance; it is NOT retrospectively relabelled as corrected fanout 1–7. No Docker build/push, Kubernetes deployment, cloud resource spending, additional training/experiment, fresh performance result, peer-run message, or journal manuscript edit occurred under D5. Reassess matched prospective GKE evidence only after actual D5 local test readback and a separate D6/D7 authorization. Manuscript release and the 23 October 2026 internal target remain conditional, not automatic.

**Final transaction:** code candidate and two test expectations implemented with GitHub readback PASS; D5 deterministic test **OPEN / AWAIT EXECUTION**; JCC-R1A **HOLD**; canonical AHBN **FROZEN**; GKE/Docker/formal runs and journal submission **HOLD**. Only the two explicitly identified files plus this changing stage are authorized to be modified in this transaction.



## JCC-R1A / JCC-R2-to-Submission — Forward Gate Roadmap (planning-only; 2026-10-12)

**Nature:** Project-level planning roadmap, not an authorization, test PASS, science decision, manuscript revision or journal submission. Historical D1–D5 statuses in preceding sections control. All new gate labels below are **PROPOSED** until explicitly reconciled and released under `docs/00_QAHBN2_MASTER.md` §9.5.

**Reconciled on 2026-10-12:** science `wwiras/q-ahbn2@main` = `2d61081da13f44b5b3282bf970c659215b56d814`; manuscript `wwiras/QAHBN2-Manuscript@main` = `57152560860c0b7d0ac0f114b75a8caa9f11a209` with `sn-main.tex`. Historical pinned science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` and historical producing GKE image/commit stay immutable. Google Drive science corpus `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5` exists and contains `output/`, but synced/unreviewed files are not automatically promoted evidence.

### Phase A: implementation validity (existing gate D5-T1 and proposed D6–D8)

| Gate | Work / exact evidence-based release condition | Current control state |
| --- | --- | --- |
| **JCC-R1A-C3-D5-T1** | Researcher runs targeted `tests.test_k2_kubernetes_adapter` and full local deterministic regression. Inspect producing SHA, exit status, test list/counts, 2→1/6→7 endpoint behavior, target selection, F=0, same-peer successor, reward and terminal lifecycle. Fix new defects only via newly authorized scope; verify exact outputs and GitHub readback. | **NEXT / OPEN — outputs not yet evidenced** |
| **JCC-R1A-C3-D6 (proposed)** | After D5-T1 PASS, verify immutable candidate SHA, clean local source, prospective unique image tag, linux/amd64 digest, runtime/controller import and container preflight. No performance inference or historical image overwrite. | HOLD / not authorized |
| **JCC-R1A-C3-D7 (proposed)** | Before cloud use, freeze corrected Q arm, exact 5-seed matched protocol, needed AHBN/comparator rerun criterion, validity/exclusion/statistical plans and cloud approval. Execute only with researcher authorization; preserve all raw artifacts under a fresh run directory and validate manifests. If only 5 corrected Q runs, prove benchmark compatibility or label results separately; if five-method contemporaneous claim requires it, run a separately authorized 25-run matrix. | HOLD / conditional |
| **JCC-R1A-C3-D8 (proposed)** | Independently audit corrected raw → metrics → seed pairs → confidence intervals, action traces, manuscript parity, original-versus-corrected variant distinction, unexpected or null results, immutable evidence preservation and readback. No claim of benefit without paired support. | HOLD / conditional |

**Fallback at D7 decision:** If corrected Kubernetes formal work is not authorized or cannot pass, retain the original deployed-clipped variant explicitly as a limited operational observation, remove/narrow 1–7 K8s parity claims, and do not treat a deterministic smoke test as corrected performance validation.

### Phase B: JCC-R1A science closure (proposed C1/C2/C4/C5, after D8 or fallback)

| Gate | Decision scope | Required acceptance |
| --- | --- | --- |
| **JCC-R1A-C1 — Parameter adequacy** | Justify fixed 81-state/5-action Q learner, \(\alpha_Q=.25\), \(\gamma=.70\) with bounded gamma sensitivity, epsilon schedule and NEW/DUP/FAIL reward; separate design choice from empirically optimized parameter. | No unsupported optimum/generalization; additional sensitivity only if a necessary retained claim requires it. |
| **JCC-R1A-C2 — Experimental sufficiency** | Determine what 80-run primary ControlSim, 25-run Exp13-Q-Sim and bounded 20-peer GKE do and do not support. | Precisely stated BA/topology/churn and seed scope; no uncontrolled extra experiments. |
| **JCC-R1A-C4 — External comparator and literature adequacy** | Verify current published state-of-the-art papers, DC-SoC reference, canonical AHBN predecessor provenance/status, novelty and correct citations. | No claim that AHBN Scientific Reports is published if still under review; compare like-for-like evidence. |
| **JCC-R1A-C5 — Claims/statistics parity** | Reconcile every manuscript table/figure and claim with frozen raw/aggregation/paired statistics; distinguish stronger/weaker metrics and overhead. | Zero unsupported claims; negative/null cases retained; no data fabrication or post-hoc metric substitution. |
| **JCC-R1A-CLOSE** | Independent scientific-adequacy signoff, open finding ledger disposition, code/evidence/manuscript revision release contract. | PASS required to unlock substantive JCC-R2 scientific text updates; scientific HOLD until completed. |

### Phase C: manuscript rewrite (proposed JCC-R2 stages; manuscript repo authority)

**Sequence is evidence-first, not page-order:** `wwiras/QAHBN2-Manuscript/sn-main.tex` remains original authoritative manuscript until its own change/review gates. Proposed steps:

1. **JCC-R2.0 — Manuscript architecture/claim map:** supervisor Overleaf OC-01/02/03, WA comments; reduce unnecessary fragmentation without deleting scientific detail; lock section map, figures, table/citation and revision/markup policy.
2. **JCC-R2.1 — Method rewrite:** canonical AHBN→Q boundary, 1–7 request versus realized eligible fanout, five action selection rationale, state/learning/reward/transition lifecycle, fixed parameters versus actual gamma sensitivity and any bounded implementation disclosure.
3. **JCC-R2.2 — Experimental methodology rewrite:** precise ControlSim families, matched seeds, statistical contract, K8s corrected or restricted-variant provenance and exact comparator caveats; avoid claiming equivalence of unrelated environments.
4. **JCC-R2.3 — Results rewrite:** learning + failure + churn + heterogeneity + primary paired comparisons; bounded five-method reference benchmark; accurate Kubernetes operational evidence; all numbers independently checked against frozen evidence, including cost trade-offs and interval crossings.
5. **JCC-R2.4 — Discussion/limitations rewrite:** what learning adds beyond immutable AHBN, communication overhead and worse/null outcomes, small-n and topology limitations, deployed-variant historical correction and SOTA scope.
6. **JCC-R2.5 — Related Work/Introduction/Abstract/Conclusion:** strengthen novelty, contribution and research gap without literature duplication or unsupported publication status. Harmonize all sections after results freeze.
7. **JCC-R2.6 — Internal scientific/style audit:** compile clean, check LaTeX references/abbreviations, figures/tables/TikZ, bibliography and citations, duplicated text, source–claim matrix, reviewer-comment response, change/highlight policy, and word/page count requirements. Each rewrite section needs PASS/approved freeze before overarching closure.
8. **JCC-R2-CLOSE — Supervisor-ready PDF package:** verified `sn-main.tex`, PDF, versioned difference/annotated changes if needed, supervisor comment-resolution register and evidence trace, GitHub postwrite readback.

### Phase D: external review and submission (proposed JCC-R3/R4)

| Gate | Decision | Release criteria |
| --- | --- | --- |
| **JCC-R3.1 — Supervisor consultation/revision** | Send supervisor-ready scientifically audited version; log feedback and reconcile scientifically material changes through new gates. | Supervisor feedback resolved or exceptions explicitly documented. |
| **JCC-R3.2 — Journal of Cloud Computing compliance audit** | Confirm current journal scope, template and submission rules, metadata/author/affiliation/funding, data/code availability, declarations, ethics, figures and cover letter; avoid assuming template/portal requirements without verification. | Full journal checklist PASS. |
| **JCC-R3.3 — Final evidence/PDF freeze** | Freeze submission Git commit, manuscript source, final compiled PDF, references and supplementary/data link checks, checksum/version provenance. | Reproducibility and package completeness PASS. |
| **JCC-R4 — Submission authorization and submission** | Obtain researcher signoff and complete actual target-journal submission through researcher-controlled journal portal. Preserve confirmation/ID and deposited version; update both source controls according to authority. | **SUBMITTED** only after actual journal confirmation; otherwise HOLD. |

**Internal target:** Friday **23 October 2026** for **supervisor-ready** package, not a journal deadline. It is subordinate to scientific and code/evidence integrity. Journal submission remains HOLD until JCC-R4.

**Reconciliation rule:** audit each gate and edit only truly changed authoritative files; source science/evidence decisions stay in the science repo, manuscript content changes in manuscript repo, and scientific Drive output requires deliberate promotion. This planning-only roadmap is recorded solely in the scientific stage. Existing master, test statistics, results and manuscript do not change authority because of this planning note.


## JCC-R1A-C4 / JCC-R2.0 — Researcher-Approved Q-AHBN-First Manuscript Positioning (2026-10-12)

**Type/status:** Researcher-approved narrative/architecture INTENT, recorded for subsequent C4/C2/C5 audits and JCC-R2.0 reconciliation. Not an adequacy PASS, experiment amendment, manuscript-edit authorization or bypass of the current JCC-R1A-C3-D5-T1 gate. The scientific JCC-R1A HOLD remains active.

### A. Principal story and honest technical identity

Present **Q-AHBN** as the self-contained proposed learning-assisted hybrid blockchain dissemination scheme, not chiefly as an extension-paper narrative. Explain its entire deterministic hybrid foundation as an internal controller (local observations, normalization, EWMA, score, mode choice and bounded fanout), followed by the outcome-driven bounded Q-learning refinement (81 states, five actions, attributable NEW/DUP/FAIL outcomes, Q-updates and lifecycle, realized eligible targets). Preserve canonical deterministic controller source and numerical contract without retuning.

The deterministic part is technically the **frozen AHBN controller**. Identify it accurately as AHBN/deterministic hybrid baseline within the learning/no-learning experiment and reproducibility material. Do not incorrectly describe the inherited controller as newly invented in Q-AHBN, suppress disclosure of related submitted research where required, treat the AHBN Scientific Reports manuscript as published, or misattribute the component to another published SOTA scheme. The Q-AHBN paper must define the mechanism fully so readers need not find an unpublished paper; verified published hybrid/learning SOTA establishes external research context and novelty comparison.

### B. Three evaluation questions using pre-existing frozen evidence

| Story block | Registered data | Question, scope and caveat |
| --- | --- | --- |
| **A — Learning contribution (learning-component ablation)** | Exp10-Q failure, Exp11-Q churn, Exp12-Q heterogeneity: **80 primary ControlSim formal runs / 40 paired deterministic AHBN versus Q-AHBN comparisons over eight conditions** | What measurable difference is attributable to enabling the entire bounded learning refinement above the same frozen controller? Report delivery, simulation delay and increased duplicates/forwarding cost. Not evidence that the individual state bins, actions or hyperparameters are optimal. |
| **B — Comparative dissemination performance** | Exp13-Q-Sim: **25 frozen ControlSim runs** across Gossip, Structured, DC-SoC, AHBN and Q-AHBN at churn=0.40 | How does the *complete Q-AHBN scheme* compare against the three established external dissemination methods under one fixed benchmark? Keep the AHBN arm identified in original five-method results; no artificial double counting, arm removal or blanket SOTA-win claim. |
| **C — Cloud-native operational validation** | Historical Exp13-Q-K8s matched five-method Kubernetes/GKE N=20 matrix | What bounded operational behavior is demonstrated? Historical Q implementation clipped 1–7 learning requests back to 2–6 and is a restricted variant. Corrected cloud performance requires separate D5-T1 → proposed D6–D8 validation; do not claim independent reproduction of ControlSim gains. |

These blocks are three evaluation purposes, **not three new experiment families**. The contribution framing is twofold: demonstrate what learning changes relative to the deterministic foundation; characterize the complete proposed scheme relative to established dissemination methods. Cloud-native evaluation is complementary deployment evidence.

### C. Intended manuscript logic — pending JCC-R2.0 section-map audit

1. Introduction — dynamic blockchain dissemination problem, integrated learning-assisted hybrid contribution and research gap.
2. Related Work — Gossip, Structured, hybrid and learning-based dissemination SOTA with verified sources; avoid literature duplication.
3. Q-AHBN Architecture — full deterministic controller plus bounded learner, equations, reward, actions, lifecycle, inherited base 2–6 and derived Q-request 1–7 versus realized fanout.
4. Experimental Methodology — separate ControlSim and GKE environments, baselines, scenarios, seeds, statistics, artifacts and experiment provenance.
5. Learning Contribution Evaluation — frozen Exp10-Q/11-Q/12-Q paired comparison and costs.
6. Comparative Dissemination Performance — bounded Exp13-Q-Sim five-method comparator benchmark.
7. Cloud-Native Validation — verified valid observations with documented Kubernetes restricted-variant/corrected-source distinction.
8. Discussion and Limitations — benefits, overhead, small sample and scope, design choices versus tuned parameters, novelty and validation limits.
9. Conclusion — only scientifically supported Q-AHBN claims.

The nine items form a **logical architecture**, not a command to create nine top-level Springer LaTeX sections. At JCC-R2.0 map onto the existing manuscript template/section hierarchy and Overleaf OC/WA comments. The older Scientific Reports AHBN manuscript is an organizational reference only: do not copy/rename its claims or prose; comply with overlap/related-submission disclosures.

### D. Gate dependencies, evidence and authority

- **C4:** verify hybrid SOTA and genuinely comparable learning-based dissemination sources; decide whether a fair and reproducible additional learning-based numerical comparator is necessary. Preserve Gossip, Structured, DC-SoC and AHBN in the frozen Exp13-Q matrix. New competitors require separately approved prospective experiments.
- **C2:** decide whether the frozen 80-run primary and 25-run reference benchmark are sufficient for the precise intended claims; preserve scenario and sampling limits.
- **C1/C5:** justify design versus optimized learning settings; verify exact paired statistics, overhead and all claims/figures/tables.
- **C3 (unchanged NEXT):** JCC-R1A-C3-D5-T1 targeted and full researcher-run deterministic regression evidence. D6–D8, formal GKE runs and substantive manuscript rewriting remain HOLD.
- **JCC-R1A-CLOSE / JCC-R2.0:** only after scientific release may the manuscript repository map and author the approved text/sections. Manuscript GitHub stays unchanged for this transaction.
- **Immutable firewalls:** pinned science baseline 6ccc94e5df770d588a5ccfa592f603a9a8ab2c68; original experiments, statistical contracts, historical GKE evidence, source files, image records, and Drive output unchanged. Source science repository remains authoritative for this stage.
- **References reconciled:** Science Drive root 1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5 and manuscript cloud folder 1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj listed/read; predecessor Scientific Reports PDF 1_C3fJpukQ-RJWLjU5Krx5lSwCio9TSQh read as reference (**under review, not published**). Local Mac paths are researcher-provided sync locations and were not directly accessed.

**Transaction decision:** Researcher positioning APPROVED/RECORDED; scientific-adequacy C4/C2/C5 PENDING, manuscript substantive edits LOCKED, JCC-R1A-C3-D5-T1 OPEN, JCC-R1A HOLD. Only this stage file changes.


## JCC-R1A — Revision-History and Manuscript-Archive Policy Review (2026-10-12)

**Record type:** Researcher-requested repository organization review and minimal planning decision. This is NOT a new scientific experiment gate, amendment to the frozen design, manuscript rewrite, archival upload, or change to current JCC-R1A-C3-D5-T1 HOLD.

**Reconciled sources:** scientific main at 154b64fc67173e6daad0f8767d208a7d09bef009; manuscript main at 57152560860c0b7d0ac0f114b75a8caa9f11a209; scientific Master section on revision naming and section 9.5; both GitHub root trees; science Drive root 1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5; manuscript Drive root 1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj (contains an existing archives directory). Local researcher paths were not directly accessed.

### Decision: Git history for ordinary revisions; immutable packages for publication milestones

1. **No new general historical version folder** in the science or manuscript GitHub repositories. Avoid reinstating versions/vX.Y or copying the entire source tree on every edit. GitHub source commit SHA and controlled stage/register are authoritative for routine history; preserve all prior commits and pinned science baseline.
2. **Respect existing manuscript convention:** active source is root sn-main.tex; the scientific Master records root-level next-revision source names such as sn-main1.0.tex when a reviewer revision is opened. Do not create or rename a revision-specific source until the relevant manuscript revision gate authorizes it.
3. **Use milestone archives selectively:** at supervisor-ready freeze, journal submission, revision submission and acceptance/final release, register immutable manuscript source reference and exact compiled PDF, bibliography/supplementary package and associated review/response/decision documents as applicable. Archives are frozen records, not alternative live manuscripts. Prefer the existing manuscript Drive archives location after its contents and policy are audited; do not create a duplicate folder by assumption.
4. **Record provenance metadata** for every frozen milestone: milestone type/date, repository, branch, exact commit SHA, source filename, PDF/source artifact filenames, optional checksums, bibliography/assets, reviewer-response references, journal status and manuscript ID if actually issued, archive Drive path/IDs, verification/readback and supersession relation. An optional compact register in existing manuscript docs can point to these snapshots; avoid duplicate registers unless JCC-R2.0 reconciliation demonstrates need.
5. **No false evidence promotion:** Git-ignored output, synchronized Drive copies and generated PDFs remain unverified until deliberately checked, preserved and read back. Existing timestamped research evidence/run folders and immutable experiment outputs remain governed by Master sections 9.5 and 10-12.
6. **Resilience:** GitHub commit history is excellent for text diffs but is not an independent off-site backup or a guarantee against branch-history rewriting; milestone packages in Drive provide an independently recoverable publication record. Any future Git tags should be immutable pointers to verified milestones, not substitutes for verified PDFs/submission records.
7. **Scope:** This stage-note addition is the only present file update. Do not modify the manuscript repository, move its existing archives, create PDF artifacts, retag repositories or amend gitignore under this gate. Decide exact archive content and any optional lightweight register in the later manuscript architecture/freeze gate.

**Next operational gate unchanged:** JCC-R1A-C3-D5-T1 — verify researcher-run deterministic tests. JCC-R1A overall HOLD; proposed D6-D8 and manuscript JCC-R2 remain locked.


## JCC-R1A-C3-D5-T1 — Local Deterministic Evidence Preservation and Readback (2026-10-12)

**Gate outcome: PASS / CLOSED — deterministic local tests only.**

**Reconciliation:** Scientific GitHub main before this evidence transaction: `969d1362355c9bd2b1afbbb04ff76fafebca6441`. Pinned frozen scientific baseline: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` (unchanged). Researcher executed tests on a clean working tree after `git pull --ff-only`. No source changes were authorized or performed under this verification.

**Readback provenance:** The assistant enumerated the specified scientific Google Drive corpus root and directly located `output/evidence/JCC-R1A-C3-D5-20261012T122839Z`, folder ID `1wd2BEZPc2oqBV_K0h6VgV5fdAzP0sAmj`. All three original files were independently fetched from Google Drive (not merely inferred from local sync or terminal narration):

| Artifact | Google Drive file ID | Original readback |
| --- | --- | --- |
| `run_manifest.txt` | `1GXxOV4nXWMMPqzAVbKZRm7oLEwwI_u51` | `UTC=2026-10-12T12:28:41Z`; producing SHA `969d1362355c9bd2b1afbbb04ff76fafebca6441`; empty git status; `targeted_exit=0`; `full_exit=0` |
| `targeted_tests.log` | `1pDp_xy9uWxWPgi0Gsbw32TWe5a7Z01QU` | `Ran 9 tests in 0.001s`; `OK`; each of nine verbose adapter tests reports `ok` |
| `full_regression.log` | `1LcrrynxB02ZeHNK_61EP9k7nBXr0v2VK` | `Ran 103 tests in 0.138s`; `OK (skipped=3)`; zero failures |

**Verification and limitation:** Targeted unit tests cover five learning actions, lower/upper requested fanout endpoints (AHBN 2→Q 1, AHBN 6→Q 7), attribution of NEW/DUPLICATE/FAILED outcomes, F=0 no update, next state on the same peer, delayed reward, terminal update, attempt-ledger guards, inherited gossip target realization/registration and structured selector delegation. Full-regression output is a concise unittest dot transcript: three skips are visible but individual skip reasons are not recorded in this original log; do not claim their specific causes. The original files existed in the designated Google Drive corpus and passed content readback. No checksum was recorded, so do not claim cryptographic artifact attestation.

**Decision:** D5-T1 deterministic-test execution and original-artifact preservation/readback **PASS / CLOSED**. This is a code-level, researcher-run local deterministic result only; it does **not** establish Docker/image parity, corrected GKE operation, performance impact, network reliability, or scientific adequacy of claims. Historical restricted Kubernetes evidence remains frozen and unchanged. ControlSim remains a separate evidence family.

**Forward control:** D5-T1 is closed; **JCC-R1A-C3-D6 — Docker/image validation planning and separately authorized execution** is the next candidate technical gate (RELEASE CANDIDATE / NOT EXECUTED). D7/D8, corrected cloud formal experiments, substantive manuscript rewriting, and journal submission remain HOLD pending their own release criteria. C1/C2/C4/C5 scientific adequacy checks remain PENDING; JCC-R1A overall HOLD. No changes to canonical AHBN, learner settings, datasets, measured results, image records, or `QAHBN2-Manuscript` are authorized by this transaction.


## JCC-R1A-C3-D6 — Docker/Image Configuration and Test-Plan Reconciliation (2026-10-12)

**Status: PRE-BUILD REVIEW / CONDITIONAL HOLD.** D5-T1 was previously closed using independently read-back Google Drive logs; this D6 entry does not assert any Docker build, push, runtime test, registry digest, or GKE deployment has occurred.

**Reconciled authority:** `docs/00_QAHBN2_MASTER.md`; prior D5-T1 stage closure; scientific repo `wwiras/q-ahbn2`; pinned science baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68` unchanged. Manuscript `wwiras/QAHBN2-Manuscript` remains untouched.

### Inspected source paths and risk

- `gke/app/Dockerfile.qahbn2` uses `python:3.11-slim`, installs `gke/app/requirements.txt`, generates gRPC bindings, copies inherited peer/controller files, `gke/app/qahbn2_runtime.py`, and **`COPY qahbn2 qahbn2`**. The corrected adapter is thus included by the recipe when the build context is the current repo root; image contents still require verification.
- `gke/app/qahbn2_runtime.py` imports `KubernetesQAHBN2Adapter` and `QAHBN2Learner`, obtains canonical S5 proposal and records `k_ahbn`, `k_q`, and realized targets. It is a wrapper around inherited runtime; do not conflate requested fanout with actual realized target count.
- `gke/scripts/build_k3_q_image.sh` and `build_k5_q_formal_image.sh` build `linux/amd64` using `docker buildx build ... --push` **before** image verification. Running either is a registry mutation and is not authorized by this pre-build review.
- `gke/scripts/verify_k3_q_image.sh` checks registry pull for `linux/amd64`, image OS/architecture and prints available repo digest. `gke/scripts/preflight_k3_q_image.sh` checks Python module imports, but **does not directly test corrected 2→1 and 6→7 fanout endpoints inside the image**.
- `gke/PROVENANCE.md` pins inherited GKE source `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`. Historical image tags/digests are not evidence for a newly built corrected image.

### D6 proposed researcher-run acceptance sequence (NOT EXECUTED)

1. Record current clean Git SHA, `git status --short`, Docker/Buildx version, target `linux/amd64`, Dockerfile and dependency hashes, exact image reference and whether build is local-only or registry-pushed. Use a **new immutable image tag**; never overwrite historical formal-image references.
2. Prefer an initial **local-only** Buildx build with explicit `--load` and a fresh local tag; do not run existing push scripts as an initial test. Save full stdout/stderr, exit code and image ID.
3. Inspect image OS/architecture and package provenance. Within the container run Python import preflight, then execute an explicit behavioral check that calls the packaged adapter/learner for frozen boundary cases AHBN `k=2` with `FANOUT_DOWN` → Q request `1`, and AHBN `k=6` with `FANOUT_UP` → Q request `7`. Include no hidden learner-side 2–6 clipping and preserve separate realized-neighbor constraints. Test action/mode semantics without altering frozen scientific source.
4. Verify that the container actually uses the intended corrected source, not a stale layer or previously pushed tag. Record SHA-256 file parity for `qahbn2/kubernetes_adapter.py` between repository and container, plus image ID and, only if later pushed, immutable registry digest.
5. Preserve build, architecture, import, behavioral and parity logs with producing SHA and exit codes in a fresh `output/evidence/JCC-R1A-C3-D6-<UTC>` directory; verify original files from the connected scientific Drive corpus before any PASS/CLOSED decision. Record skipped checks as limitations.
6. Only after local D6 evidence passes and researcher explicitly approves registry publication should a new registry image be pushed and independently pulled/verified. Any D7/D8 GKE validation remains a separately released researcher-run gate; D6 is not a performance result.

**Pre-build finding:** Dockerfile appears to package the corrected source from the root build context, but the existing preflight lacks an in-image 1–7 boundary assertion; the existing build scripts publish images before behavioral validation. D6 execution therefore remains **HOLD until a non-pushing test command and evidence contract are accepted**. No source, Dockerfile, image, frozen AHBN controller, experiment, or manuscript modifications in this transaction.


## JCC-R1A-C3-D6-P1 — Researcher-Run Non-Pushing Linux Image Commands (2026-10-12)

**Status: COMMAND PLAN RELEASED / EXECUTION PENDING.** This is a documentation-only command release. No Docker build, container test, image push, GKE action or performance experiment has been performed by the assistant.

**Authority/reconciliation:** Current scientific main before this stage edit: \`cc1693c740f5eb4188baecec4daa53f5fe53fb9e\`; Master \`docs/00_QAHBN2_MASTER.md\`, prior D6 reconciliation, Dockerfile, source adapter/learner, the existing K3 build/push and import scripts, and the Drive corpus root \`1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5\` were inspected. Historical pinned scientific baseline \`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68\` remains immutable. \`QAHBN2-Manuscript\` is untouched.

**Target:** Docker image OS/architecture exactly \`linux/amd64\` (Linux, x86-64), even when the researcher's Mac is Apple Silicon/arm64. Use \`docker buildx build --platform linux/amd64 --load\` from repository root with \`gke/app/Dockerfile.qahbn2\`. Dockerfile packages the \`qahbn2\` source tree and starts \`qahbn2_runtime.py\`.

**Safety:** Do not invoke \`gke/scripts/build_k3_q_image.sh\` or \`build_k5_q_formal_image.sh\` at D6-P1: both contain \`--push\`. No registry tag, cloud project, or Kubernetes resources are changed. The local new-tag naming is SHA/time-based, avoiding historical image names. Require a clean tracked working tree before building to bind source to Git; \`output/\` is ignored evidence.

**Exact gate procedure:** The researcher executes one zsh-compatible Mac script as shared in the D6-P1 assistant turn. That script (1) \`git pull --ff-only\`, \`git status --porcelain\` guard, and prerequisites; (2) logs time, producing HEAD and platform, Docker/Buildx versions and source/Dockerfile/dependency SHA-256 hashes; (3) builds with \`docker buildx build --platform linux/amd64 -f gke/app/Dockerfile.qahbn2 -t <fresh-local-tag> --load .\` (no push); (4) independently checks \`docker image inspect ... '{{.Os}}/{{.Architecture}}'\` equals \`linux/amd64\`; (5) imports \`peer\`, \`gen_topology\`, \`dcsoc_maintenance\`, \`qahbn2_runtime\`, \`controller\`; (6) executes inside the image an inline Python program that instantiates the packaged \`KubernetesQAHBN2Adapter\` and \`QAHBN2Learner\` with forced greedy \`FANOUT_DOWN\` and \`FANOUT_UP\` decisions and asserts both 2→1 and 6→7, checks action/mode behavior and eligible-neighbour realization; (7) compares SHA-256 for \`qahbn2/kubernetes_adapter.py\` inside the image against host source, records image ID and all step exit codes; (8) writes distinct build, inspect, import, parity, source-hash and manifest logs under \`output/evidence/JCC-R1A-C3-D6-<UTC>\`. Use individual exit status checks and stop at first failure. The command must not claim image-level PASS when any check fails.

**Acceptance:** Linux/amd64 architecture PASS, build/loader PASS, container imports PASS, lower and upper bounded requests PASS, realization semantics PASS, exact source-hash parity PASS, clean producing Git SHA documented and original Drive evidence independently readable. Skips, missing Docker Desktop, engine resource/architecture errors or sync delays remain HOLD with actual logs. This establishes only local Linux image packaging and deterministic behavior, not registry immutability, GKE correctness or corrected formal performance.

**Next:** Researcher sends the resulting manifest and test log/evidence directory. Assistant performs original Drive artifact readback, then GitHub closure transaction only if all mandatory conditions pass. The manuscript, frozen AHBN, original experiments and historical restricted image digest are not modified. JCC-R1A overall remains HOLD.


## JCC-R1A-C3-D6-P2 — Linux/AMD64 Local Image Evidence Readback and Closure (2026-10-12)

**Decision: LOCAL D6 PASS / CLOSED.** Researcher executed local, non-pushing Docker build and image/container deterministic validation on 2026-10-12. Assistant independently enumerated the scientific Google Drive corpus \`1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5\`, located the original synchronized evidence at \`output/evidence/JCC-R1A-C3-D6-20261012T125047Z\` (Drive folder ID \`1h5Gh0S-s2KFyHYds5CqAq4TxL40--elt\`), and fetched/read all eight original artifacts.

**Producing scientific source:** \`280855900e89b1db5269ace73b4aabf6c7afae88\`; manifest UTC end \`2026-10-12T12:51:42Z\`; source tree clean at build according to original provenance. Pinned scientific baseline remains \`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68\` (unchanged). Docker \`29.8.1\`; Buildx \`0.37.1\`.

| Original evidence artifact | Drive file ID | Readback finding |
| --- | --- | --- |
| \`run_manifest.txt\` | \`11IziuGoPBl4WpJ8LkJLA9ERjNCVw_GZZ\` | \`local_validation=PASS\`, platform \`linux/amd64\`, all four exit statuses 0, push and GKE NOT_PERFORMED |
| \`source_parity.log\` | \`1dvSaM71SQNrzFekZTHO-yEnLD-U7rSg-\` | host and container adapter SHA-256 identical \`045396d4bd58962852b403aac9f9f8fedd2c43c41636aae85ecb29bc8de9e355\` |
| \`step_results.txt\` | \`1ZUrOAhXckyCxsTfWZkrUz8i89bjg5bzm\` | build/import/parity/source-parity exits all 0 |
| \`fanout_parity.log\` | \`1jLyn6K7T_KZ0-V7INk0813akcXlSKI9S\` | AHBN 2→Q 1, AHBN 6→Q 7, five actions and requested 7/realized 3 all PASS |
| \`import_test.log\` | \`1-ZWCKF-3YMJJTnyWT1-hE2IQEAbcfi6V\` | \`CONTAINER IMPORT PASS\` |
| \`image_inspect.log\` | \`1FgizCKVATJxWa0wopCeCYHI9ZhSZZfBq\` | exact \`linux/amd64\`, local image ID recorded |
| \`build.log\` | \`1mCxRBRepAYeCgKz72oQaMBWxXhYwOENe\` | successful Docker Buildx copy and image export; Python package installation warning regarding root is not a failed step |
| \`provenance.log\` | \`1325lDZJKaMtYBZpqf_2SNhnHv_HCEsQw\` | producing commit SHA, clean checkout, platform, Docker/Buildx versions and source/Dockerfile/dependency hashes |

**Exact built image:** \`qahbn2-d6-local:20261012T125047Z-280855900e89\`. Local image ID: \`sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d\`. This is a LOCAL Docker image ID, not an immutable remote registry digest. The existing historic restricted Kubernetes image digest is not overwritten.

**Interpretation/firewalls:** Evidence supports Linux/AMD64 local packaging, container imports, corrected learner/adaptor bounded fanout action parity, local source parity and eligible-target realization. Does NOT demonstrate cloud deployment, registry publication/pullability, corrected formal GKE results, comparative throughput, delivery, latency, duplication, or a scientific adequacy judgment. Existing ControlSim and historical K8s families remain untouched. No Docker push and no GKE execution occurred.

**Next gate:** D6 local closure is complete. Any registry publication and remote image-digest attestation, then separate D7/D8 GKE validation, require individual researcher authorization and their own evidence gates. JCC-R1A-C1/C2/C4/C5 pending, JCC-R1A overall HOLD; manuscript substantive modifications and journal submission remain locked.


## JCC-R1A-C3-D6-R1 — Linux/AMD64 Registry Publication and Independent Verification Preparation (2026-10-12)

**Gate status: PLAN PREPARED / RESEARCHER PUBLICATION APPROVAL HOLD.** This is a controlled preparation transaction only. No Docker image was uploaded, pulled from the registry, or deployed to GKE by this transaction. JCC-R1A overall HOLD.

**Reconciled current authority:** GitHub science \`wwiras/q-ahbn2\` latest pre-transaction main \`45229d5b8d58a0ba0c38d55e207a2167e6fae7be\`; current Master §9.5/§9.5.2 and its prospective MYT evidence naming update; frozen canonical AHBN contract; D6-P2 stage closure and original Drive evidence folder \`1h5Gh0S-s2KFyHYds5CqAq4TxL40--elt\`; \`gke/app/Dockerfile.qahbn2\`; existing \`gke/scripts/build_k5_q_formal_image.sh\`, \`verify_k3_q_image.sh\`, \`preflight_k3_q_image.sh\`, \`run_k5_q_formal.sh\` and Helm image field. Q-AHBN manuscript repository \`wwiras/QAHBN2-Manuscript\` remained at observed main \`57152560860c0b7d0ac0f114b75a8caa9f11a209\`; no edits. Frozen science baseline \`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68\` remains immutable.

**Proven local image identity:** \`qahbn2-d6-local:20261012T125047Z-280855900e89\`, exact local image ID \`sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d\`, Linux/AMD64 verified. Producing source commit \`280855900e89b1db5269ace73b4aabf6c7afae88\`, clean working state, original logs Drive-read-back; host/container adapter SHA-256 both \`045396d4bd58962852b403aac9f9f8fedd2c43c41636aae85ecb29bc8de9e355\`. **Do not rebuild as a substitute for this already tested image.** A later GitHub documentation commit does not change the producing image source SHA.

**Image publication decision to be approved separately:** choose authenticated registry/repository namespace, access/visibility, and explicitly authorize publishing a fresh immutable candidate tag. Any push potentially exposes program code to viewers of that repository; default to a private registry repository where available. Publication is not implied by approval of this plan. The existing \`build_k3_q_image.sh\` and \`build_k5_q_formal_image.sh\` use \`--push\` and perform a rebuild; **do not use them to publish this pinned local D6 image**.

**Release-gate sequence (human-executed only, once approved):**
1. Before push, run \`git pull --ff-only\`, report \`git rev-parse HEAD\` and clean \`git status --porcelain\`; document the producing source SHA separately, not as the current documentation HEAD. Verify Docker engine, \`docker image inspect\` of the *original* local tag, its OS/architecture exactly \`linux/amd64\` and image ID exactly \`sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d\`. Re-run in-container adapter SHA-256 check against recorded D6 value; fail closed on any mismatch.
2. Use \`docker tag <original-local-image> <approved-registry>/<approved-private-repository>:<new-SHA-and-time-tag>\` to assign a distinct registry reference without a rebuild. A tag alone does not publish. Then, only upon explicit approval, \`docker push <registry-reference>\`. Do not overwrite historical Kubernetes image tags/digests.
3. Capture push transcript and exit code, \`docker buildx imagetools inspect <registry-reference>\` manifest, and exact registry digest (different in role from local image ID). Require \`linux/amd64\` platform and digest \`sha256:<64-hex>\`; do not guess digest. Record the image using \`<registry-repository>@sha256:<manifest-digest>\` for future Kubernetes use, not solely the mutable tag.
4. **Independent pull:** if feasible use a different clean Docker engine or separate machine; otherwise \`docker image rm <registry-reference>\` (only the newly assigned tag), then \`docker pull --platform linux/amd64 <approved-registry-reference>@sha256:<observed-digest>\`, inspecting pulled OS/architecture, digest and in-container source/behavior. Do not remove the pinned D6 local image; record when independence is only a fresh pull in the same engine.
5. Re-run \`peer/gen_topology/dcsoc_maintenance/qahbn2_runtime/controller\` imports and the D6 five-action + 2→1 and 6→7 in-container requested fanout assertions, plus requested 7/realized eligible 3 behavior. Save results and exit codes; verify remote image source hash matches pinned adapter SHA-256. Registry manifest digest and local image ID may differ because they identify different objects; never equate them.
6. Preserve run logs/manifest (source producing SHA, current documentation HEAD, local image ID, approved registry repo/tag, public/private status, observed manifest digest, expected Linux AMD64, push/pull/image/behavior checks, exact time-zone and exit statuses) under a *new unique* \`output/evidence/JCC-R1A-C3-D6-R1-YYYYMMDDHHmmss\` (14-digit MYT time per \`EVID_TIME_20261012_TIMESTAMP_CONTRACT.md\`). Independently read original artifacts from designated Google Drive corpus, then update GitHub stage and perform post-write readback.

**Limits and next gate:** D6-R1 will PASS only after researcher-authorized registry push, immutable digest captured, independent pull and container parity readback. This does not prove cloud operation. D7 planning and later controlled GKE validation require a separate gate/approval after successful registry evidence; D8 and formal runs remain HOLD. Canonical AHBN, frozen experiments, existing result claims, image historical provenance, journal manuscript and publication status untouched.


## JCC-R1A-C3-D6-R1-P1 — Researcher Local Image Presence Check (2026-10-12)

**Status: LOCAL IMAGE PRESENCE / ARCHITECTURE PASS; REGISTRY PUBLICATION HOLD.** Researcher supplied the Mac terminal output after `git pull --ff-only` fast-forwarded local `main` from `2808559` to `ed7c197dfac5bdb11752ef46c5e380f2ae37c0c0`. `docker image inspect` directly reported `OS=linux ARCH=amd64 ID=sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d`. `docker info` reported Docker server `29.8.1`. This matches the previously Drive-read-back D6-P2 local image identity and Linux/AMD64 target. No rebuild was requested or evidenced; image remains the same binary as the D6 validation by ID. Source-producing Git commit remains `280855900e89b1db5269ace73b4aabf6c7afae88`, distinct from current documentation HEAD.

**Limits:** The supplied command output did not include an explicit `git status --porcelain` after pull, Docker registry login, registry destination/visibility, `docker tag`, `docker push`, remotely resolved digest or independent pull. No registry claim or D6-R1 release/closure follows from this check. Await an approved registry repository and visibility; prefer private. Execute tag/push and independent digest/architecture/container parity verification only after that separate authorization. Current `JCC-R1A` overall and D7/D8 Kubernetes gates stay HOLD. Frozen scientific baseline `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`, manuscript and results unchanged.


## JCC-R1A-C3-D6-R1-P2 — Public Docker Hub Destination and Controlled Publication Command Release (2026-10-12)

**Decision: PUBLIC REGISTRY DESTINATION APPROVED BY RESEARCHER; COMMANDS PREPARED / NOT EXECUTED.** The researcher explicitly selected Docker Hub repository \`docker.io/wwiras/q-ahbn2\` with **public** visibility. This means the published image layers can be downloaded and inspected by anyone; public registry exposure is intentional. Repository existence, public setting, Docker Hub credentials and push permissions must be confirmed by the researcher, not assumed. Do not publish if the repository is not explicitly configured public or if the Docker Hub namespace is incorrect.

**Authority:** GitHub science main \`2838d62659f154e3e3b71a6d996cc4ab44e01094\` before this documentation-only transaction; \`docs/00_QAHBN2_MASTER.md\` §9.5 and prospective evidence time rule \`docs/stages/EVID_TIME_20261012_TIMESTAMP_CONTRACT.md\`; D6-P2 and D6-R1-P1 stage evidence. Original local Linux/AMD64 image \`qahbn2-d6-local:20261012T125047Z-280855900e89\`, ID \`sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d\`, source-producing SHA \`280855900e89b1db5269ace73b4aabf6c7afae88\`, adapter SHA-256 \`045396d4bd58962852b403aac9f9f8fedd2c43c41636aae85ecb29bc8de9e355\`. No rebuilding or algorithm edits.

**Researcher execution sequence (prepared in assistant response):** Check current clean Git, Docker daemon, original image ID and \`linux/amd64\`, verify adapter SHA in local container; record UTC/MYT timestamps and exact image provenance; create a new \`output/evidence/JCC-R1A-C3-D6-R1-YYYYMMDDHHmmss\` (MYT) directory; confirm \`docker login\` and that \`wwiras/q-ahbn2\` exists as a **public** Docker Hub repository; tag the exact existing image with a fresh \`d6r1-<MYT14>-<producingSHA12>-amd64\` tag; \`docker push\` only that tag, saving push log and status; inspect registry manifest to get authoritative remote sha256 digest; pull by \`docker.io/wwiras/q-ahbn2@sha256:<remote-manifest-digest>\` with \`--platform linux/amd64\`; verify downloaded OS/architecture, source adapter hash, imports and full D6 five-action + lower/upper boundary + eligible-realization checks. Prefer a separate clean engine for fully independent pull; same-engine digest pull is a limited independent registry retrieval and must be described accurately. Capture all logs and exit codes; never infer a digest from the local image ID. Publish no \`latest\` tag and do not overwrite historical image references.

**Acceptance/closure:** Require recorded Docker Hub public visibility, successful push, remote digest and Linux AMD64, digest-pinned pull, full container behavior and source-hash parity, exact producing source SHA and new MYT evidence path, original Google Drive artifact readback, and post-write GitHub reconciliation. A failure is HOLD. No Kubernetes/GKE action is authorized by this gate; D7/D8 and formal experiments remain HOLD pending separate approval. Manuscript, pinned science baseline, historical results, canonical AHBN and scientific adequacy status unchanged.


## JCC-R1A-C3-D6-R1-P3 — Public Registry Push and Digest-Pinned Pull Evidence Readback (2026-10-12)

**Decision: REGISTRY PUBLICATION PASS; DIGEST-PINNED SAME-ENGINE IMAGE/SOURCE VERIFICATION PASS; D6-R1 FULL CLOSURE HOLD (remaining acceptance controls).** The researcher provided terminal output showing \`D6-R1 REMOTE IMAGE VERIFICATION PASS\`. Assistant independently fetched original files in the scientific Google Drive evidence folder \`output/evidence/JCC-R1A-C3-D6-R1-20261012211222\`, Drive ID \`1pSDVQGRZGmXYw3s6gm9P8fWuoj3o57FT\`. Folder name follows MYT 14-digit prospective convention.

**Provenance:** Producing source \`280855900e89b1db5269ace73b4aabf6c7afae88\`, registry publication documentation HEAD \`48c28755ce74923de1412e79a989c1430add2274\`, tested original local image ID \`sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d\`; Linux/AMD64. Repository destination approved as public \`docker.io/wwiras/q-ahbn2\` by researcher (actual Docker Hub repository visibility setting not independently inspected).

**Published unique tag:** \`docker.io/wwiras/q-ahbn2:d6r1-20261012211222-280855900e89-amd64\`.
**Registry digest:** \`sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466\`.
**Digest-pinned reference:** \`docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466\`.

**Original Drive readback:** \`push.log\` (\`1tpn5-BRI7Z0SFlMYEvWGuNTCzCSe_XOP\`) reports pushed digest; \`step_results.txt\` (\`1b5eRV8dXeiu1PTxlPPhmIonG5gP9F4bp\`) reports \`push_exit=0\`; \`registry_inspect.log\` (\`1Nt5tBqMq483M8DIBeD89oJ-SBPD3bcI-\`) reports Docker v2 manifest and matching digest; \`pull_tag.log\` (\`1LEpFY5EhzylBT6sjsEz5i3fGMeAmjhtv\`) and \`pull_digest.log\` (\`1BIabu7YLOPLOmbQuKvcISWZd2ESvVCF1\`) report successful pull by tag and digest respectively; \`verification_manifest.txt\` (\`19ysUBQ4E2k6vsYadd1G1kiGJULargojJ\`) reports remote \`linux/amd64\`, exact original image ID, source/import PASS and GKE NOT_PERFORMED; \`remote_test.log\` (\`1XOgR7Cr3-dKa-XnzzGNMaCJRF8BFA0Rx\`) reports \`REMOTE CONTAINER IMPORT AND SOURCE PARITY PASS\`; \`provenance.txt\` (\`1iNXAUkp6SPS5vsm0o0ncM9fgeNf_My7t\`) records clean D6 image identity, source and MYT time.

**Boundary of verification:** Pull by digest was on the same Docker engine and log says \`Image is up to date\`, so it is NOT evidence of a fresh independent download on a separate engine. Full D6 five-action and 2→1/6→7 behavioral checks were previously verified for the **same image ID** in D6-P2, but the new remote test directly checked imports and adapter hash only, not a fresh in-container full action-parity run. Docker Hub public visibility is researcher-approved but not independently inspected. Accordingly registry upload and identity/source checks are PASS; full D6-R1 acceptance remains HOLD until independent fresh-engine retrieval or an explicitly approved bounded same-engine limitation, public-visibility confirmation, and a direct remote digest-pinned behavioral parity check (or documented approval to inherit the identical-image-ID D6-P2 evidence).

**Next:** Seek explicit researcher decision on bounded same-engine pull and inherited D6-P2 behavior evidence versus fresh independent verification. Preserve existing evidence; add only new append-only logs to same original evidence folder where appropriate. D7/D8 GKE and JCC-R1A overall remain HOLD; no GKE, canonical science, baseline or manuscript changes.


## JCC-R1A-C3-D6-R1-P4 — Independent engine mismatch diagnostic (2026-10-12)

**STATUS: DIAGNOSTIC COMMANDS RELEASED / D6-R1 HOLD.** Researcher tested public Docker Hub digest `sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466` using a new temporary Docker-in-Docker daemon on the same Mac. Original Drive evidence `output/evidence/JCC-R1A-C3-D6-R1-20261012211222/independent_engine/fresh_pull.log` (Drive ID `1COno1-H6tknGIneaSSFiQri5BIYtkqwN`) was independently read: it records a full fresh layer download and matching registry digest. The script stopped at the strict Step 5 platform/image-ID comparison, before printing the observed values or performing imports. Thus independent fresh-engine download PASS; independent engine identity and source/runtime parity UNKNOWN; do not call this a full PASS. Previous temporary engine was cleaned automatically. Original local D6 image ID `sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d`, original adapter SHA256 `045396d4bd58962852b403aac9f9f8fedd2c43c41636aae85ecb29bc8de9e355` remain the expected immutable references.

**Next diagnostic:** Repeat with a unique temporary Docker-in-Docker engine, new output subdirectory in the same preserved evidence family, and explicit logging of *actual* `.Os`, `.Architecture`, `.Id`, and registry digest before comparing with expected values. If mismatch, preserve the isolated engine for examination; do not change expected values, re-tag, rebuild, republish, run GKE, or relax acceptance. Clean up only after inspection (explicit researcher command). Capture engine daemon metadata and test outcomes. Explain that separate engine on same Mac is not separate physical host. D7/D8 and overall JCC remain HOLD. Manuscript status: Q-AHBN manuscript submitted to Journal of Cloud Computing and under peer review, not published and no DOI; no manuscript/repo scientific changes authorised by this diagnostic.


## JCC-R1A-C3-D6-R1-P5 — Fresh-engine source and import parity (2026-10-12)

**PASS (bounded):** Researcher preserved isolated DinD engine `qahbn2-d6r1-diag-20261012215940` and ran metadata inspection plus digest-pinned Python import/adapter verification. Google Drive evidence independently read back: `independent_engine/diagnostic-20261012215940/image_metadata.log` (Drive ID `1yJWrLOvNje0s5jV_ZWNRWP1l25x9Q4fs`), `identity.log` (`1tqOucmTVf7SMarayAhVJQ-VH49Hgn8Gn`), `source_import_followup.log` (`1CGs_EiiMNkNxK14subzLtOZzp3X2llFd`). Fresh engine `overlayfs`, image `linux/amd64`, registry digest `sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`, imports PASS, adapter hash equals expected `045396d4bd58962852b403aac9f9f8fedd2c43c41636aae85ecb29bc8de9e355`. Its `.Id` reports registry digest `8a47...` rather than original image config ID `d90d...`; image-ID equivalence remains **UNRESOLVED**, not FAIL of source bytes. **D6-R1 overall HOLD** pending inspection of image configuration digest / store semantics; do not infer identity from matching source hash alone. No rebuild, republish, GKE or manuscript changes. Retain temporary engine until explicit cleanup after inspection. D7/D8 HOLD.


## JCC-R1A-C3-D6-R1-P6 — Registry config digest reconciliation (2026-10-12)

**PASS — IMAGE IDENTITY RECONCILED.** Researcher inspected the digest-pinned Docker Hub Schema 2 manifest from the preserved temporary DinD engine (`qahbn2-d6r1-diag-20261012215940`). The registry manifest digest is `sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`, and the `SchemaV2Manifest.config.digest` is `sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d`, exactly matching the original D6-tested local image `.Id`. The isolated engine's `.Id` reported the registry manifest digest because its Docker info `DriverStatus` indicates the containerd snapshotter (`io.containerd.snapshotter.v1`); these are distinct manifest/config identifiers, not evidence of altered image content. Platform linux/amd64, fresh download, Python imports, and adapter SHA256 `045396d4bd58962852b403aac9f9f8fedd2c43c41636aae85ecb29bc8de9e355` all PASS. User-provided complete manifest inspection and original ID comparison are recorded in conversation attachment `Pasted markdown(20261012-140322).md`; preserve a compact `manifest_config_digest.log` in the original Drive evidence folder before archival closure. **D6-R1 fresh-engine image identity and source/import parity PASS; full behavioral parity is inherited only from prior same-image-ID D6-P2 tests, not rerun here.** No GKE, rebuild, republish or manuscript edits. D7/D8 HOLD. Temporary DinD engine awaits safe cleanup. D6-R1 administrative closure pending compact log archive and researcher approval of inherited behavioral evidence.


## JCC-R1A-C3-D6-R1-P7 — Archived manifest-config identity evidence (2026-10-12)

**PASS / VERIFIED DRIVE READBACK.** Researcher ran strict manifest config comparison (`test "$ACTUAL" = "$EXPECTED"`) on retained temporary DinD engine and printed `D6-R1 CONFIGURATION IDENTITY PASS`. Original Google Drive evidence `output/evidence/JCC-R1A-C3-D6-R1-20261012211222/independent_engine/diagnostic-20261012215940/manifest_config_digest.log` was independently read back (Drive file ID `1fa4uqkYn2b22XUpJS2jrF9UfkxNPbFaS`): manifest digest `sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`, platform linux/amd64, config digest `sha256:d90d8ca1439056ba578b6aaa19122548219d80ce6c0b39766a861c2dfdc07d8d` equals original D6-tested image ID. Prior fresh pull, imports and adapter hash verified. **D6-R1 technical verification PASS**, bounded to fresh-engine retrieval, image configuration identity, and source/import parity; behavioral suite not independently rerun in this engine, inherited from original D6-P2 identical-image evidence. Administrative cleanup pending; temporary engine retained until researcher runs targeted `docker rm -f qahbn2-d6r1-diag-20261012215940`. No GKE, rebuild, republish or manuscript modifications. D7/D8 remain HOLD.


## JCC-R1A-C3-D6-R1-P8 — Temporary-engine cleanup and closure (2026-10-12)

**PASS / CLOSED (bounded D6-R1 scope).** Researcher executed `docker rm -f qahbn2-d6r1-diag-20261012215940`; terminal returned the exact container name, confirming successful removal of the isolated Docker-in-Docker verification container. This completes administrative cleanup following verified Google Drive archival/readback of manifest config digest, fresh pull, image metadata, Python imports and adapter SHA-256. Published digest-pinned image configuration matches original tested D6 image ID. Scope: fresh isolated-engine retrieval and source/identity verification, with original D6 behavioral evidence inherited, **not independently rerun**. Independent physical host validation **NOT PERFORMED**; GKE **NOT PERFORMED**; D7/D8 remain HOLD. No rebuild, republish, algorithm or manuscript change. Gate D6-R1 PASS/CLOSED; do not generalize this to subsequent deployment gates.
