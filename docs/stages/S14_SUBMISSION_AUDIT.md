# S14 — Submission / Reproducibility Audit

**Status:** PASS / CLOSED — submission/reproducibility audit complete — 2026-09-30

## Objective
Perform the final paper/evidence/reproducibility audit after all evidence and claim-reconciliation gates required for submission are closed.

## Required checks
Audit exact run counts, Git/provenance identifiers, frozen parameter consistency, reproducible figures/tables, claim-to-evidence mapping, exclusions/reruns, seed integrity, terminology, supplementary material, and resolvable evidence locations.

## Boundary
No new scientific result, parameter, experiment, comparator, or claim may be introduced at S14.


## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md`
- `docs/03_EXPERIMENT_CONTRACT.md`
- `docs/04_STATISTICAL_CONTRACT.md`
- `docs/06_RESULTS_REGISTER.md`
- `docs/07_CLAIM_EVIDENCE_MATRIX.md`
- `docs/stages/S13_MANUSCRIPT.md`
- `wwiras/QAHBN2-Manuscript/docs/MANUSCRIPT_MASTER.md`
- `wwiras/QAHBN2-Manuscript/docs/PROVENANCE.md`
- `wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`

Pinned manuscript science baseline:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`

## Audit findings

### 1. Exact run counts and seed integrity — PASS
- Exp10-Q: 20/20 formal runs, seeds 42--46, 0 exclusions, 0 reruns.
- Exp11-Q: 30/30 formal runs, seeds 42--46, 0 exclusions, 0 reruns.
- Exp12-Q: 30/30 formal runs, seeds 42--46, 0 exclusions, 0 reruns.
- Primary S11-A aggregation: 80/80 runs and 40/40 same-seed AHBN--Q-AHBN2 paired comparisons.
- Exp13-Q: 25/25 formal cells, seeds 42--46, 0 exclusions, 0 reruns.
- Kubernetes: 25/25 validated coordinates = 5 methods x seeds 42--46; final reconciliation performed no experiment reruns.

### 2. Frozen parameter consistency — PASS
The manuscript remains consistent with the frozen Q-AHBN2 design contract:
- 81 states;
- actions KEEP, FANOUT_DOWN, FANOUT_UP, SET_GOSSIP, SET_STRUCTURED;
- reward `(NEW - DUPLICATE - FAILED) / F`, with `F=0` giving no Q update;
- `alpha_Q=0.25`, `gamma=0.70`, `epsilon_0=0.30`, `epsilon_min=0.03`, `epsilon_decay=0.995`;
- canonical AHBN remains immutable.

No manuscript text reopens parameter tuning, reward design, action design, or AHBN internals.

### 3. Statistical-contract consistency — PASS
Primary paired claims remain condition-specific, use the frozen same-seed paired design, and do not pool unlike conditions. No post-hoc p-value family, omnibus winner score, global ranking, or cross-environment pooled effect is introduced.

### 4. Quantitative manuscript artifacts — PASS
The active manuscript contains three quantitative tables and no figures.
- `tab:primary-paired-results` reconciles with S11-A primary aggregation.
- `tab:exp13-results` reconciles with S11-B bounded reference aggregation.
- `tab:kubernetes-results` reconciles with K6-Q/S12 Kubernetes evidence.
- No unresolved `\ref` target or duplicate label is present.
- Figure reproducibility is not applicable because the manuscript currently contains no figures.

Explicit table-level provenance has been added to `QAHBN2-Manuscript/docs/PROVENANCE.md`.

### 5. Git / provenance identifiers — PASS
Primary registered identifiers remain resolvable:
- S11-A Drive folder: `1XMWn5FWKwJV78YeTGakJb1bVJ6XKfrLH`;
- S11-A producing aggregation commit: `59ef254099fb3edb617f323dd864324c320d9a85`;
- S11-B Drive folder: `1frfPsofGtbvpRFCxFMjGi_EZUuv8tNxx`;
- Exp13-Q producing commit: `2b11b4e95ef98c86458e02c494d6b6ea232a6d7a`;
- Kubernetes evidence family: `1dq5s83YC9-BH2PTj-VaeP_c1VirfxcFJ`;
- Kubernetes formal folder: `15iFp5E2NCKnewFFObLp3xvVQK3IsXjeP`;
- Kubernetes matrix manifest SHA-256: `d1fbc037ef9da5c253ad0b2d3851a555bdd9165f30d499011d65653aee88d7bf`;
- Kubernetes producing Git SHA: `7ad474c3a249fde58223f2abd5d54918b4bcbb9f`;
- frozen image digest: `sha256:d8ac06197962a6e42cb9e564a9c115c08b9f018df231f61cdbfbb8796422991e`.

### 6. Claim-to-evidence and terminology audit — PASS
Publication-facing algorithm naming remains **Q-AHBN**. S12A boundaries remain intact:
- primary ControlSim evidence for tested-condition delivery/latency improvement with communication-overhead cost;
- Exp13-Q as bounded external positioning only;
- Kubernetes as operational realization / deployment credibility only;
- no convergence, policy optimality, global hyperparameter optimality, universal superiority, best/winner/dominance, generic lightweight/low-overhead, literal replication, or cross-environment pooling claim.

### 7. Bibliography boundary — PASS / researcher-managed
`references.bib` remains researcher-managed through Zotero under the established contract. Its repository presence/absence is not an assistant-controlled S14 criterion. The prior independent Drive check confirmed all eight manuscript citation keys in the researcher-authorized support corpus.

### 8. Supplementary-material boundary — PASS / no new requirement introduced
No new supplementary-material package is scientifically required by S14. Existing registered Git/Drive provenance, manifests, frozen summaries, and source-code/evidence locations provide the reproducibility chain required by the current contract. S14 does not invent extra artifacts merely for completeness.

## Result

**S14 = PASS / CLOSED.**

The standalone Q-AHBN paper has completed the frozen scientific manuscript and submission/reproducibility audit sequence. No new scientific result, parameter, experiment, comparator, claim, literature source, or statistical analysis was introduced.

## Next permitted task
The paper scientific workflow is complete under the current frozen stage map. Any later journal-specific template conversion, author metadata, cover letter, Zotero bibliography insertion, submission portal packaging, or reviewer-response work is researcher/submission administration unless a new controlled gate is explicitly opened.

The separate thesis path `S13-T — Chapter 6 Evidence Mapping` remains PENDING / unopened.
