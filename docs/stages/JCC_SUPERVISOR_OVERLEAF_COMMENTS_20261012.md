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
