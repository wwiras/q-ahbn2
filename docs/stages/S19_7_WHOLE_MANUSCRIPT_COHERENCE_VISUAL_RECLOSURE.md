# S19-7 — Whole-Manuscript Coherence / Consistency Harmonization

**Status:** IN PROGRESS — narrative harmonization completed; compile/visual proof pending.

## Objective
Harmonize the active manuscript with the revised abstract so that the paper reads as one coherent scientific argument:
1. latency--duplication trade-off characterization;
2. deterministic AHBN runtime balancing;
3. bounded Q-AHBN experience-driven refinement;
4. percentage-based primary-result framing;
5. explicit communication-overhead trade-off;
6. separated evidence roles for ControlSim, external positioning, and Kubernetes.

## Reconciliation
- latest science master reconciled;
- latest active manuscript source reconciled;
- science Drive root and manuscript Drive root rechecked;
- pinned science baseline unchanged: `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`.

## Manuscript harmonization
Active source:
`versions/v0.0/main.tex`

Commit:
`451d86ffc29d6c8ee273258e92df282f77b46b05`

### Introduction
Reframed the opening around the latency--duplication trade-off, then made the progression explicit:
fixed dissemination characterization -> deterministic AHBN adaptation -> bounded Q-AHBN learning refinement.
Clarified that AHBN rebalances the current local condition but its fixed mapping does not learn from prior forwarding outcomes.

### Related Work
Strengthened the final positioning paragraph so the literature gap matches the abstract: Q-AHBN is not a replacement dissemination family, but an experience-driven refinement above an already adaptive AHBN baseline.

### Methodology
Clarified the dual-loop interpretation:
- AHBN remains the deterministic local control loop;
- Q-AHBN adds a bounded learning loop from attributable outcomes.
No state, action, reward, parameter, threshold, or Algorithm 1 semantic changed.
Also corrected the prose typo “compact architectural” -> “compact architectural view”.

### Results
Narrative reporting now mirrors the abstract's percentage framing while leaving frozen tables, figures, absolute paired effects, and confidence intervals unchanged.
Verified relative effects from frozen S11-A:
- one-peer failure: delivery +17.60%, delay -36.74%;
- churn 0.00/0.20/0.40: delivery +18.23/+8.08/+2.88%; delay -37.27/-27.69/-11.91%;
- balanced/moderate/weak-heavy: delivery +11.86/+6.92/+6.95%; delay -32.09/-30.43/-33.63%;
- overall tested-condition ranges: delivery +2.88% to +18.23%; delay reduction 11.91% to 37.27%.

The registered paired Student-t intervals remain attached to the absolute paired effects; relative percentages are descriptive re-expression of the same frozen means and are not a new inferential family.

### Discussion
Reframed the opening and primary interpretation around the same three-step progression as the abstract and Introduction. Added the verified relative effect ranges to the synthesis while preserving the communication-overhead, non-dominance, condition-specific, and non-pooled evidence boundaries.

## Evidence authority for percentages
Frozen S11-A Drive folder:
`1XMWn5FWKwJV78YeTGakJb1bVJ6XKfrLH`

Summary CSV:
`1D6Z1DZa5CLnXBX6Z0Adljb260Er7S1_M`

Registered SHA-256:
`9b2d21a103c9cd115acc56a003eb8bab60a49db92bc82af3a8da004d03b33833`

## Scientific-boundary audit
- no experiments reopened;
- no parameters changed;
- no AHBN or Q-AHBN logic changed;
- no new statistical computation introduced;
- no figures or quantitative tables changed;
- no confidence intervals changed;
- no evidence families pooled;
- no convergence, optimality, universal-superiority, ranking, or generic-low-overhead claim introduced.

## Remaining S19-7 requirement
Compile and visual/proof inspection of the complete manuscript remains pending. S19-7 must not be declared PASS/CLOSED until the latest PDF is compiled and checked for:
- abstract/section consistency;
- Figure 1 layout;
- table/figure references;
- LaTeX errors/warnings affecting content;
- percentage wording and mathematical typography;
- overall page-flow/readability.

**Current status: S19-7 = IN PROGRESS.**


## Citation-support correction — Gossip and DC-SoC — 2026-10-03
Researcher review identified that several publication-facing mentions of Gossip and DC-SoC appeared without nearby literature support.

A bounded citation pass was applied to the active manuscript using already-vetted published bibliography entries:
- Gossip-related support: `berendea_fair_2020` and `baniata_dons_2022` where the prose makes general Gossip/comparator statements;
- introductory Gossip trade-off support additionally uses `li_ls_gossip_2022`;
- DC-SoC support: `dong_dc-soc_2024` at comparator-introduction and later positioning/scope statements.

The Related Work section already contained direct DC-SoC and Gossip citations and was retained. No citation was added to purely numerical table rows, labels, or figure axis text where the values originate from this study's frozen experiment rather than from the cited papers.

Active manuscript citation commit:
`61a49da97641a3be3761f06553549a1ba1c8c571`.

No bibliography entry was added or changed; all cited keys already existed in the active published/eligible 26-reference bibliography. No experiment, result, statistic, parameter, figure value, table value, or claim boundary changed.

S19-7 remains IN PROGRESS pending compile/visual proof.


## Citation-key synchronization with Chapter 2 bibliography — 2026-10-03
Researcher supplied `ahbnLR26Sept2026chap2_92.bib` as the citation-key authority for overlapping references.

A title/DOI reconciliation was performed against the active manuscript bibliography. Citation keys were changed only where the same publication could be matched unambiguously. The active manuscript source was synchronized as follows:
- `shahsavari_block_2022` -> `shahsavari_theoretical_2022`
- `perigee_2020` -> `mao_perigee_2020`
- `tang_latency_2023` -> `tang_strategic_2023`
- `li_ls_gossip_2022` -> `li_ls-gossip_2022`
- `fortino_tons_2023` -> `fortino_using_2023`
- `mohamed_bnsf_2024` -> `mohamed_efficient_2024`
- `tran_nval_2022` -> `tran_framework_2022`
- `diperna_topologies_2025` -> `di_perna_impact_2025`
- `koshikawa_overlay_2026` -> `koshikawa_impacts_2026`

Entries whose keys already matched the Chapter 2 bibliography were left unchanged.

Several active manuscript references do not have a verified matching entry in the supplied 92-entry bibliography and were therefore not renamed: `qiu_geography_2023`, `wira_cloudnative_2025`, `wira_kubernetes_2025`, `decker_q8s_2025`, `albert_barabasi_2002`, and `erdos_renyi_1960`.

Manuscript source commit:
`a7d7aa9155345f9620296b4215c460f72349bcdc`.

No scientific claim, evidence, result, parameter, figure, or table value changed. S19-7 remains IN PROGRESS pending bibliography-entry synchronization/readback and final compile/visual proof.
