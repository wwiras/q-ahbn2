# D8-I1 SHA256 audit — detailed execution report

**Result: AUDIT INCOMPLETE.** The audit identified one unreadable Google Drive cloud placeholder. This report preserves the exact partial result; it does not assert integrity verification or baseline completion.

## Execution identity

- Initial execution interval: `2026-10-20T06:26:05.052991+00:00` through `2026-10-20T06:26:05.851925+00:00`.
- Latest execution interval: `2026-10-20T06:28:16.505852+00:00` through `2026-10-20T06:28:17.312322+00:00`.
- Repository HEAD for the latest execution: `57511049a27db0034c5fefa29d5daef1e6207dc5`.
- Audit script: `gke/scripts/audit_d8_i1_sha256.py`.
- Script source SHA256: `d7446e0c5456c9df50f47b7c90182505731e05ddfb2ff114fd485202eaa4841e`.
- Runtime: Python 3.14.6.
- Scope roots: the five entries in `D8_I1_ARCHIVED_FILE_INVENTORY_20261020.md`, and no others.

## Method

The scanner walks the roots in deterministic path order without following symbolic links. It enumerates each expected seed-method coordinate and all 24 expected direct run files, then inventories every other regular file in the five roots. It detects unsupported filesystem objects, duplicate inode/path entries, macOS `SF_DATALESS` cloud placeholders, empty files, read failures, short reads, and files whose metadata changes while hashing. Regular files are opened read-only and streamed to `hashlib.sha256()` in 1 MiB chunks. Size and file identity are checked while reading. An append-only checkpoint journal supports restart; every previously recorded file is read and rehashed before its record is reused.

The audit output directory is outside each evidence root and is Git-ignored by the repository's existing `output/` rule.

## Full inventory counts

| Measure | Result |
|---|---:|
| Formal roots present | 5/5 |
| Seed-method coordinates present | 25/25 |
| Expected primary file paths | 600 |
| Primary files hashed | 599 |
| Supporting artifacts found and hashed | 320/320 |
| All regular files discovered | 920 |
| All files SHA256 hashed | 919 |
| Missing expected paths | 0 |
| Read errors | 1 |
| Unexpected file names | 0 |
| Symbolic links | 0 |
| Duplicate entries | 0 |
| Empty files | 25 |

The 320 additional artifacts comprise 40 root-level files, 125 configuration files, 125 generated files, 5 raw files, and 25 target-selection files. The expected primary total was specified before the scan; no independent expected count was specified for these support families.

## Comparison counts

| Status | Count | Interpretation |
|---|---:|---|
| `MATCH` | 0 | No current hash was compared with a trusted execution-time checksum. |
| `MISMATCH` | 0 | No trusted execution-time checksum comparison failed. |
| `BASELINE_UNAVAILABLE` | 919 | Current hash exists, but a qualifying historical checksum is unavailable. |
| `MISSING` | 0 | Every expected path exists in the local inventory. |
| `READ_ERROR` | 1 | Placeholder detected before file open; no digest produced. |
| `EXTRA` | 0 | No unclassified unexpected file was found. |

Three documented same-day Google Drive raw-byte fingerprints were independently compared as supplemental source references. All three current local digests matched those values. They are not counted as `MATCH`: the prior record explicitly describes these as present-day fingerprints, not evidence that bytes were unchanged from the original experiment execution. Trusted execution-time checksum references found: **0**.

## Blocker and recovery

The expected file `20261020T041621Z-K5Q-formal/runs/seed44/ahbn/pod_readiness_evidence.txt` has a reported size of 21,376 bytes and macOS flags `compressed,dataless`. The audit therefore did not open or hash it. The operator must use Google Drive for desktop/Finder to make this one file available offline and wait for hydration to finish. Then rerun:

```sh
venv/bin/python gke/scripts/audit_d8_i1_sha256.py
```

The resume journal is `output/d8_integrity/sha256_resume.jsonl`. The second scan rehashed and validated all 919 previously completed records, which remained unchanged, but the same file still had the `dataless` flag. No hash was produced for it. Do not copy a different file over the placeholder or modify the archived evidence.

## Output locations

Interim, ignored outputs:

- `output/d8_integrity/sha256_current.csv`
- `output/d8_integrity/sha256_current.json`
- `output/d8_integrity/sha256_comparison.csv`
- `output/d8_integrity/sha256_summary.json`
- `output/d8_integrity/audit_execution.log`
- `output/d8_integrity/baseline_provenance.md`
- `output/d8_integrity/sha256_resume.jsonl`

These files document a partial scan and are not a complete current-state baseline. A later completed scan can create a complete current-state fingerprint baseline, but cannot retrospectively prove unchanged evidence since execution. No thesis or manuscript scientific claims were edited.

## Subsequent hydration and metadata classification (2026-10-20)

Operator-provided rerun at 2026-10-20 07:10:44 UTC: all 600 primary files and 320 previously inventoried supporting files hashed successfully; 0 missing and 0 read errors. Three additional regular files were macOS Finder `.DS_Store` metadata (seed44 archive root, `runs/`, and `runs/seed44/`); the original script hashed 923 files and returned `AUDIT INCOMPLETE` solely because the three Finder files were marked `EXTRA`.

The audit code now excludes regular files named `.DS_Store` from research evidence counts but lists their paths and count under `ignored_non_experimental_metadata` and `ignored_non_experimental_metadata_count`. A unit test covers this case. This report records the operator's earlier run and the code change, **not a claimed execution of the revised script**. Rerun locally and attach the revised `sha256_summary.json` and test output before recording `CURRENT-STATE BASELINE COMPLETE`.

An expected successful rerun would show 920 research evidence files hashed (600 primary, 320 supporting), 3 ignored Finder files, 0 missing, 0 unreadable, 0 EXTRA, and `BASELINE_UNAVAILABLE` for 920 files. No historical SHA256 match is established; all claims of unchanged-since-execution remain unsupported. D8 protocol, timing, and statistics checks are distinct and open.
