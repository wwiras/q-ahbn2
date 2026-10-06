# JCC Final Controlled Submission Audit

**Target journal:** Journal of Cloud Computing: Advances, Systems and Applications  
**Audit date:** 2026-10-06  
**Scientific repository:** `wwiras/q-ahbn2`  
**Manuscript repository:** `wwiras/QAHBN2-Manuscript`  
**Pinned science baseline:** `6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`  
**Scope:** submission readiness only. No experiment, algorithm, parameter, result, evidence family, or scientific claim authorization is reopened.

## Reconciliation

- latest scientific `main` reconciled;
- latest manuscript `main` reconciled;
- `docs/00_QAHBN2_MASTER.md`, source-authority records, S16/S20 submission-production records, manuscript master/provenance, root `sn-main.tex`, and root `references.bib` reviewed;
- scientific Drive root `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5` and manuscript Drive root `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj` reconciled as synchronized work/evidence locations under the existing authority model;
- registered pre-audit JoCC proof remains `main05Oct2026_2329.pdf`; because JCC-4 changed submission-format/source metadata, a fresh clean compile is required before upload.

## JCC-0 — Journal requirements and scope audit

**Status: PASS / CLOSED**

The current journal scope explicitly includes cloud-computing research across the software/hardware stack and permits cloud systems to be considered alongside peer-to-peer, cluster, and grid systems. Research Article requirements checked include title/author metadata, 150–250-word abstract, 3–10 keywords, abbreviation handling, declarations, editable source files, line/page numbering, double spacing, data availability, formal dataset citation, and a cover letter.

No scope-driven scientific rewrite is required.

## JCC-1 — Manuscript-to-journal fit audit

**Status: PASS / CLOSED**

Fit is supported by the manuscript's:
- adaptive P2P/distributed-systems problem;
- cloud-native/Kubernetes realization and observability evidence;
- reinforcement-learning control layer;
- explicit treatment of controlled simulation and Kubernetes as complementary evidence families.

The paper does not rely on a superficial cloud keyword insertion; the Kubernetes evaluation and prior cloud-native framework establish a substantive journal bridge.

## JCC-2 — Title / abstract / keywords / editorial-positioning audit

**Status: PASS / CLOSED**

- title retained unchanged;
- abstract already within the journal's 150–250-word range following S20-4;
- seven keywords satisfy the journal's 3–10 keyword guidance;
- title/abstract/Introduction/Conclusion preserve the same bounded narrative:
  latency–duplication trade-off -> deterministic AHBN -> bounded Q-AHBN refinement -> condition-specific delivery/delay improvement -> communication-overhead cost -> bounded benchmark positioning -> Kubernetes operational realization;
- no novelty or superiority inflation introduced.

## JCC-3 — Scientific and claim-boundary final audit

**Status: PASS / CLOSED**

No scientific reopening is warranted.

The manuscript retains the frozen prohibitions on:
- universal superiority;
- omnibus method ranking;
- generic lightweight/low-overhead performance;
- Q-table convergence or policy optimality;
- global hyperparameter optimality;
- cross-environment pooling/equivalence;
- Kubernetes confirmation of a consistent Q-AHBN performance advantage;
- network-size scalability beyond the evaluated sizes.

No experiment, parameter, algorithm, statistic, evidence family, or numerical result was changed.

## JCC-4 — Formatting / declarations / references / data-availability audit

**Status: PASS / CLOSED WITH ADMINISTRATIVE FOLLOW-UP**

Submission-compliance corrections applied:
1. root `sn-main.tex` switched to Springer submission mode using `referee` and `lineno` options for double spacing and line numbering;
2. Zenodo dataset DOI `10.5281/zenodo.23165652` is now cited from the Availability of data and materials statement;
3. root `references.bib` now contains a BibTeX-compatible formal Zenodo dataset reference;
4. a bounded AI-assisted manuscript-preparation disclosure was added, recording ChatGPT use for language/structure/consistency/formatting/compliance support while explicitly preserving human scientific responsibility and stating that AI was not used to generate experimental data or replace final scientific decisions.

Verified current source:
- active manuscript: root `sn-main.tex`;
- shared bibliography: root `references.bib`;
- figures/tables are native LaTeX/TikZ/PGFPlots; no external `includegraphics` dependencies were found.

### Authorship metadata follow-up
Three `\equalcont{These authors contributed equally to this work.}` markers remain for Chee Keong Tan, Wai Peng Wong, and Ian K.T. Tan. They were not changed because equal-contribution status is an authorship declaration requiring researcher/co-author confirmation. This is the only unresolved factual metadata item.

## JCC-5 — Cover letter

**Status: PASS / CLOSED**

Created manuscript-repository file:
`docs/JCC_COVER_LETTER.md`

The letter includes:
- why the manuscript fits Journal of Cloud Computing;
- bounded contribution and evidence framing;
- data availability DOI;
- competing-interests declaration;
- author approval statement;
- originality / not-under-consideration statement;
- no special-issue claim.

## JCC-6 — Submission package audit

**Status: CONDITIONAL PASS**

Required upload package:
- freshly compiled final manuscript PDF from current root `sn-main.tex`;
- root `sn-main.tex`;
- root `references.bib`;
- `sn-jnl.cls`;
- `sn-mathphys-num.bst` and any other template support files required by the portal/compiler;
- cover-letter text from `docs/JCC_COVER_LETTER.md`;
- author/affiliation/corresponding-author metadata entered in the portal;
- Zenodo DOI already embedded/cited in the manuscript.

Do not duplicate the Zenodo ZIP as a supplementary upload unless the submission portal/editor specifically requests it.

A clean recompile is required because JCC-4 changed the manuscript source after the registered `main05Oct2026_2329.pdf` proof.

## JCC-7 — Submission decision

**Current decision: HOLD — one administrative release check only.**

No scientific defect remains.

Equal-contribution metadata has now been resolved by explicit researcher authorization: all three `\\equalcont` declarations were removed, while the approved Author contributions paragraph was retained unchanged.

Release to **GO FOR SUBMISSION** after:
1. a fresh clean compile of the current source is visually/build verified and used as the upload PDF.

These are administrative/proof checks only and do not reopen manuscript science.

## Status

`JCC-0 PASS`  
`JCC-1 PASS`  
`JCC-2 PASS`  
`JCC-3 PASS`  
`JCC-4 PASS`  
`JCC-5 PASS`  
`JCC-6 CONDITIONAL PASS`  
`JCC-7 HOLD — fresh compile / visual proof only`


## JCC-7A — Equal-contribution metadata resolution — 2026-10-06

**Status: PASS / CLOSED**

Researcher explicitly authorized removal of all three `\\equalcont{These authors contributed equally to this work.}` declarations after reconciling them against the approved differentiated Author contributions statement.

Manuscript action:
- removed all three `\\equalcont` declarations from root `sn-main.tex`;
- retained the approved Author contributions paragraph unchanged;
- manuscript commit: `a46f8696db6585eab788a22ef5604a07c07cb4b7`.

Verification:
- remaining `\\equalcont` occurrences in active manuscript: **0**;
- approved Samsuddin Samsuddin Wira contribution wording remains present;
- no author order, affiliation, corresponding-author designation, scientific content, result, parameter, evidence family, or claim boundary changed.

**JCC-7 remaining release check:** fresh clean compile and visual/build verification of the current source only.


## JCC-7B — Table 2 referee-layout overlap correction — 2026-10-06

**Status: PASS / CLOSED (source correction); visual proof pending under JCC-7 final release**

Trigger:
- researcher supplied compiled-page evidence showing Table 2 overlapping the right-side line-number column in the Springer referee/lineno layout.

Scope:
- formatting-only correction in root `sn-main.tex`;
- no wording, evidence value, scientific interpretation, claim boundary, table row content, algorithm parameter, experiment, or result was changed.

Applied correction:
- `\tabcolsep`: 5pt -> 4pt
- Table 2 column widths: `p{2.7cm} p{5.45cm} p{5.45cm}` -> `p{2.5cm} p{5.0cm} p{5.0cm}`

Manuscript commit:
- `7066493d1cb282d784a24e2ee2f1753f07d74980`

Verification:
- active source contains the narrowed Table 2 geometry;
- Table 2 wording/content is unchanged;
- JCC-7 remains **HOLD — fresh clean compile and visual/build verification only**.

Required release action:
1. researcher performs a fresh clean compile of the current manuscript source;
2. page containing Table 2 is visually checked to confirm no overlap with `lineno`;
3. final PDF/build is checked for submission integrity;
4. if clean, close JCC-7 as **GO FOR SUBMISSION**.
