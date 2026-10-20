# D8-I1 — Archived file inventory and raw-byte integrity (2026-10-20)

**Decision:** INVENTORY PASS (bounded) / SHA256 INTEGRITY HOLD / D8 HOLD.

## Scope
Read-only inspection of canonical Google Drive `q-ahbn2/output/evidence` for formal seed archives:
- seed42: `20261020T032934Z-K5Q-formal`
- seed43: `20261020T035637Z-K5Q-formal`
- seed44: `20261020T041621Z-K5Q-formal`
- seed45: `20261020T043745Z-K5Q-formal`
- seed46: `20261020T045636Z-K5Q-formal`

In each `runs/seedNN` folder, confirmed five method directories: `gossip`, `structured`, `dcsoc`, `ahbn`, `qahbn2`. Listed direct children of **all 25 method directories** individually using the connected Google Drive service.

## Results
- **25/25 run directories present**.
- **24/24 expected direct files present within each method directory**, with the same filename set across all runs.
- **600/600 direct method-run artifact entries present** (25 × 24). This count EXCLUDES seed-root artifacts and separate `raw`, `configs`, `generated`, and `target-selection` subtrees. Those additional archived files have not been exhaustively enumerated.
- Method folder required filenames: `churn_events.json`, `metrics.json`, `run_manifest.json`, `topology_role_mapping.json`, `cleanup_exit_status.txt`, `cleanup_status.txt`, `namespace_check_error.txt`, `namespace_cleanup_exit_status.txt`, `helm_cleanup_exit_status.txt`, `namespace_cleanup.txt`, `helm_cleanup.txt`, `logs.jsonl`, `final_snapshot.jsonl`, `controller.log`, `controller_pods.json`, `pod_readiness_evidence.txt`, `pods.json`, `experiment_exit_status.txt`, `peer_stream.jsonl`, `controller_job.json`, `peer_stream.err`, `statefulset.json`, `generated_config.yaml`, `topology.json`.
- One raw object was downloaded and independently hashed with SHA256: seed42/qahbn2/`run_manifest.json`, 757 bytes, SHA256 `e87f76a684a8a6ef9c2a85f09dee0b98c91de40bad6c507dda765af64dadf179`. No independently authenticated original reference hash was located for that object, so this value is **a present-day fingerprint, not a passed unchanged-from-original comparison**.
- The available dated seed42 audit already described archive checksums as not fully verified; no complete trusted checksum register was established in this inspection.

## Scientific boundaries and remaining integrity checks
1. A matching filename set and provider-reported object size do NOT prove byte integrity or completeness of log content.
2. Download and hash ALL 600 direct run objects plus formally required seed-root/raw/config/generated/target-selection artifacts; obtain contemporaneous archived expected hashes or other independent authoritative reference to claim `UNCHANGED`.
3. Compare actual SHA256 digests against recorded original hashes, preserving mismatches and missing references as distinct states. Without an original digest, label `FINGERPRINTED/BASELINE UNAVAILABLE`, not `PASS`.
4. An absence of archived checksums is an evidence provenance limitation, **not by itself proof of failed execution or invalid experiment**.
5. Preserve all 25 runs and all original observations; no GKE reruns, parameter changes, data exclusions or manuscript promotion.

**Gate decision: D8-I1 PARTIAL. D8 scientific validation HOLD.** Manuscript under peer review at *Journal of Cloud Computing*, no DOI, not published.
