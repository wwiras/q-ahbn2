# JCC-R1A-C3-D7-SM-REMAINING-P1 — Four-method nonformal smoke preparation (2026-10-17)

## Purpose and decision
Prepare a separately authorized smoke pathway for **Structured, DC-SoC, AHBN and Q-AHBN2**, seed 42 only. **P1 CODE PREPARED / LOCAL VALIDATION PENDING / LIVE RELEASE HOLD**. The earlier Gossip canary remains PASS (1/1) and must not be repeated. Remaining four 0/4 HOLD; D7-F formal 0/25 HOLD; D8 HOLD.

## Frozen design
Each method uses the existing `k5_q_formal.yaml` to derive K7 Exp11 configuration (20 peers, BA m=2, 240 messages separated by 0.4 seconds, four frozen churn offsets 1/26/51/76 s). Five-method scientific design remains unchanged. Results from this gate are **NONFORMAL feasibility only**. Canonical AHBN, bounded Q-AHBN2, and the pinned runtime container are unchanged.

## Implementation (GitHub)
- New separate launcher: `gke/scripts/run_d7_smoke_remaining.sh`; **do not** change or bypass previously verified Gossip-only `run_d7_smoke.sh`.
- Extend `gke/app/k7_exp11_tools.py` contract CLI with `--remaining-four-seed42`. Reuse original common-graph/frozen-input validation with the fixed subset/order. Default full-five formal contract remains unchanged; Gossip-only canary remains unchanged.
- Launcher requires explicit new environment flag `SMOKE_REMAINING_AUTHORIZED=YES` (not the legacy Gossip flag), exact pinned digest, intended GKE context, clean Git tree, exact remote-main revision, all four dedicated namespaces absent. It runs serially and fails closed if any method/validation/cleanup fails; runner retains namespace UID+owner controls; output classified NONFORMAL with full SHA256 manifest and preserved logs.
- **Known residual operational limitation:** Runner may leave a partially created namespace when creation fails before its UID is recorded. Stop and inspect manually if cleanup is unknown. Neither local checks nor source preparation prove a successful GKE deployment.

## Required local no-cloud validation (researcher terminal)
1. `git pull --ff-only origin main`, `git status --porcelain`, `git rev-parse HEAD`.
2. `bash -n gke/scripts/run_d7_smoke_remaining.sh`; `python3 -m py_compile gke/app/k7_exp11_tools.py`; verify existing Gossip launcher unchanged.
3. Verify expected failures without authorization: `env -u SMOKE_REMAINING_AUTHORIZED bash gke/scripts/run_d7_smoke_remaining.sh` should exit nonzero, print HOLD and cause no GKE mutations.
4. Generate four seed-42 configs and topologies in a fresh **temporary** directory using existing `config` and `k7_gen_topology` commands; run `contract --remaining-four-seed42` with the ordered paths. Verify negative tests: wrong method/order, wrong seed, only 3 or 5 topologies, and old Gossip canary contract on the four must all fail. None of these tests deploys pods.
5. For additional safety, perform isolated shell mock regression of launcher/runner admission, interruption and cleanup outcomes on committed exact source; inspect results before live authorization.
6. Record full outputs, code revision, SHA256 and Drive evidence. **No actual smoke launcher invocation with authorization at P1.**

## Release boundary
Proceed to a distinct P2 review only after **exact-source local tests PASS** and archival reconciliation. A successful P1 prepares but does not authorize GKE runs. The researcher controls all GKE actions. D7-F and D8 remain HOLD pending the four smoke results and independent post-run audit.

## Corpus and publication provenance
- Q-AHBN2 GitHub authority: https://github.com/wwiras/q-ahbn2
- Q-AHBN2 canonical experimental Drive: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5
- Prior canary live evidence: https://drive.google.com/drive/folders/1drKb5LsU9CxGAeB34r-TvZrNiu-c5CN_
- Thesis GitHub authority: https://github.com/wwiras/MUM_FIT_ThesisWira
- Thesis Drive corpus: https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR
- Manuscript repository: https://github.com/wwiras/QAHBN2-Manuscript
- Manuscript Drive: https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj
- Manuscript PDF: https://drive.google.com/file/d/1NZKcOHtP4qW0AImbdvQgl8pqINe04qJ4/view
- Q-AHBN paper submitted to *Journal of Cloud Computing*; **under peer review, unpublished, no DOI**. No manuscript claim changes permitted as a consequence of NONFORMAL runs.
