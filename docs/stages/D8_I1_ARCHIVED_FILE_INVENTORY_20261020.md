# D8-I1 — Archived file inventory and SHA256 integrity (2026-10-20)

**Decision: AUDIT INCOMPLETE / D8-I1 HOLD.** The five formal roots were inventoried, but one expected file is a macOS dataless Google Drive placeholder and was not opened or hashed. This is an access/completeness limitation, not evidence that an experiment failed or that its bytes differ from an earlier version.

## Scope

The read-only audit covers only these five formal roots in `output/evidence/`:

| Seed | Root |
|---:|---|
| 42 | `20261020T032934Z-K5Q-formal` |
| 43 | `20261020T035637Z-K5Q-formal` |
| 44 | `20261020T041621Z-K5Q-formal` |
| 45 | `20261020T043745Z-K5Q-formal` |
| 46 | `20261020T045636Z-K5Q-formal` |

Methods are Gossip, Structured, DC-SoC, AHBN, and Q-AHBN2. Older smoke tests, aborted attempts, and other evidence roots were excluded. No Kubernetes, GKE, Docker experiments, algorithm changes, reruns, exclusions, or edits to original evidence were performed.

## Inventory and hashing result

- **25/25** seed-method coordinates were present.
- **600** primary run-file paths were expected (25 × 24).
- **920** regular files were discovered: 600 primary run files plus **320 additional supporting artifacts**. The scope did not define a prior expected total for supporting files; all 320 discovered support files were included in the scan.
- Additional artifacts: 40 root-level, 125 `configs/`, 125 `generated/`, 5 `raw/`, and 25 `target-selection/` files.
- **599/600 primary files** and **320/320 additional files** were successfully SHA256 hashed: **919/920 total**.
- Missing files: **0**. Unexpected files: **0**. Symbolic links: **0**. Duplicate entries: **0**.
- One expected primary file could not be read because it is a cloud placeholder:
  `20261020T041621Z-K5Q-formal/runs/seed44/ahbn/pod_readiness_evidence.txt`
  (21,376 bytes reported by metadata; macOS flags include `dataless`). It was not opened or hashed. This must be made available offline and the audit resumed before completeness can be claimed.
- **25 empty files** were detected: each run's `namespace_check_error.txt`. They were hashed as empty files and reported, not silently skipped.

## Checksum provenance and comparison

The pre-existing GitHub D8 inventory, protocol decision, and preliminary reconciliation records were read. Local evidence-name searches, local history, and GitHub repository code searches did not identify a complete contemporaneous per-file SHA256 register.

Three same-day raw-byte Drive fingerprints were recorded in the earlier D8 inventory for seed42/Q-AHBN2 `run_manifest.json`, `metrics.json`, and `cleanup_status.txt`. The current local copies match all three values. These are reported as **3 same-day source-reference matches**, not as proof of unchanged evidence since execution and not as trusted execution-time checksums.

| Comparison status | Count |
|---|---:|
| `MATCH` against trusted execution-time checksum | 0 |
| `MISMATCH` against trusted execution-time checksum | 0 |
| `BASELINE_UNAVAILABLE` | 919 |
| `MISSING` | 0 |
| `READ_ERROR` | 1 |
| `EXTRA` | 0 |

The one `READ_ERROR` has no hash. The 919 `BASELINE_UNAVAILABLE` files have current SHA256 fingerprints, but no qualifying execution-time checksum reference was found. A current-state fingerprint is not a retrospective integrity proof.

## Audit provenance and outputs

- Audited repository revision for the latest scan: `57511049a27db0034c5fefa29d5daef1e6207dc5`.
- Audit script: `gke/scripts/audit_d8_i1_sha256.py`; source SHA256 at execution: `d7446e0c5456c9df50f47b7c90182505731e05ddfb2ff114fd485202eaa4841e`.
- Initial execution: 2026-10-20 06:26:05.052991Z to 06:26:05.851925Z. A second scan after the operator confirmed offline availability ran 2026-10-20 06:28:16.505852Z to 06:28:17.312322Z.
- The second scan re-read and revalidated all 919 prior successful hashes. The remaining file still had the macOS `dataless` flag, so it remained unopened and unhashed.
- Tests: 10 focused `unittest` tests passed, including known vectors, binary/empty and streamed files, mismatch, missing/read-error, interrupted/resumed scanning, extras, and output-path safety.
- Generated machine-readable output and resume journal are in the ignored `output/d8_integrity/` directory, separate from archived evidence:
  `sha256_current.csv`, `sha256_current.json`, `sha256_comparison.csv`, `sha256_summary.json`, `audit_execution.log`, `baseline_provenance.md`, and `sha256_resume.jsonl`.
- The outputs are an **incomplete interim baseline** until the dataless file is downloaded and the scan is rerun. On resume, completed records are re-read and revalidated.

## Decision boundary

**D8-I1 remains AUDIT INCOMPLETE.** No mismatch against a trusted original checksum was found, because no complete execution-time register was available. The single inaccessible placeholder prevents a complete inventory/hash result. Once it is available offline, rerun the audit and update this record with the final totals. The historical checksum limitation remains even if that final scan succeeds.

This integrity audit does not close D8 scientific validation. Protocol, timing, and statistical checks remain separate. All 25 observations remain in scope; no performance-based exclusion is permitted.

The RO4 manuscript remains under peer review at *Journal of Cloud Computing*; it has no DOI and is not described as accepted or published.
