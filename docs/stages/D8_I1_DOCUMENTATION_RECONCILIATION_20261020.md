# D8-I1 — Documentation reconciliation and scientific transition (2026-10-20)

**Decision: DOCUMENTATION REVIEW RECORDED / FINAL LOCAL AUDIT CONFIRMATION PENDING. D8 scientific validation OPEN (not passed).**

## Sources and authority
- Authoritative code/control repository: https://github.com/wwiras/q-ahbn2
- Canonical RO4 evidence corpus: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5
- Existing D8-I1 records: `D8_I1_INITIAL_DRIVE_INVENTORY_20261020.md`, `D8_I1_ARCHIVED_FILE_INVENTORY_20261020.md`, `D8_I1_SHA256_AUDIT_REPORT_20261020.md`.
- Relevant commits: `dc9c669` (classify Finder metadata), `2456e85` (focused test), `ae0c342` and `8a4a814` (post-hydration audit documentation).

## Reconciliation of recorded observations
1. The formal scope is 5 seeds (42–46) × 5 methods (Gossip, Structured, DC-SoC, AHBN, Q-AHBN2) = 25 runs, with 24 primary artifacts per run (600 files). The archival scan also identified 320 supporting research files. This gives a 920-file scoped research corpus; no older smoke or aborted experiments are included.
2. An initial local SHA256 scan hashed 919/920 files; the seed44/AHBN `pod_readiness_evidence.txt` was a dataless cloud placeholder. This was an access/read issue, not evidence of experimental failure.
3. The documented operator post-hydration rerun (2026-10-20 07:10:44 UTC) hashed all 600 primary and 320 supporting research artifacts with zero missing paths and zero read errors. The earlier script also counted three non-experimental `.DS_Store` Finder files as `EXTRA`, yielding an incomplete classification.
4. Subsequent committed code excludes `.DS_Store` from research evidence counts while reporting those paths separately, and a focused unit test was committed. **There is no confirmed output from running this revised classifier against the operator's local corpus in the evidence reviewed here.** Therefore `CURRENT-STATE BASELINE COMPLETE` is NOT asserted in this record.
5. Three same-day raw-byte Drive fingerprints match local copies, but there is no verified trusted execution-time per-file SHA256 baseline. Even a successful current-state 920/920 fingerprint scan would NOT establish unchanged-since-execution integrity.

## Stash and local-report boundary
- Operator-directed preservation of `stash@{0}` remains mandatory.
- GitHub connector access cannot inspect the operator's local Git stash or uncommitted reports. No stash was applied, dropped, cleared, overwritten, or merged by this documentation record.
- Accordingly, **local stash-to-GitHub reconciliation is pending**, not represented as completed. Compare stash files against the committed reports before any further consolidation; preserve provenance and the stash itself.

## Remaining administrative verification (offline only)
- Run the committed revised SHA256 scanner and focused tests locally, retaining `sha256_summary.json`, execution log, script revision, and output timestamps.
- Expected *conditional* classification if confirmed: 920/920 research files hashed; 3 Finder files ignored and separately reported; 0 missing/read-error/EXTRA research files; trusted historical checksum comparisons unavailable for all 920.
- Compare local stashed reports with their GitHub counterparts; merge only independently verified documentation, without touching `stash@{0}` or original evidence.

## Next scientific stage: D8
Independently verify 25-run manifest/metrics/log reconciliation, exact protocol and timing consistency, and paired seed-level statistical analysis. Preserve all observations; report missingness, uncertainty, paired effects and confidence intervals; separate descriptive from causal claims. These checks are offline. No GKE reruns, algorithm changes, parameter tuning, or scientific-result promotion are authorized by this record.

Manuscript: *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is **under peer review** at *Journal of Cloud Computing*; **no DOI; not accepted or published**.

**Release rule:** D8-I1 final administrative closure requires evidence from the revised local scan and local stash reconciliation. D8 scientific validation requires its own independent protocol/timing/statistical conclusions.
