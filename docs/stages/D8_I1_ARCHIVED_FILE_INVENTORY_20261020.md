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

## Raw-byte SHA256 follow-up (20 October 2026)
- Retrieved raw Google Drive bytes for the seed42/Q-AHBN2 `run_manifest.json`, `metrics.json`, and `cleanup_status.txt` by their actual Drive file IDs. Local SHA256 hashes calculated with `sha256sum` and byte lengths agreed with Drive's supplied lengths:
  - `runs/seed42/qahbn2/run_manifest.json` (757 bytes): `e87f76a684a8a6ef9c2a85f09dee0b98c91de40bad6c507dda765af64dadf179`
  - `runs/seed42/qahbn2/metrics.json` (1742 bytes): `0a825eddcc440ab2a7022a4726306b300c308540b5cc1200f37f45bd1f61dc51`
  - `runs/seed42/qahbn2/cleanup_status.txt` (5 bytes): `c26de83abdc9496cd1301470918ec39ecca1cf389ef0ae1c6504da1800d1c431`
- Enumerated method folders and Drive IDs for all 25 `run_manifest.json` and `metrics.json` files, in addition to the earlier 600-file inventory. Attempted a 25-manifest raw-download/hash batch; the connector imposed a maximum-tool-call failure before returning validated results. Do not credit or reproduce any unreturned digest from that batch.
- Searched connected Google Drive for filenames/metadata relating to SHA256/checksum registers and examined a sample formal seed root's `raw/` folder. No original, authenticated, comprehensive 600-file SHA256 reference register was established. A present-day SHA256 fingerprint alone cannot establish 'unchanged since execution'.
- **Bounded result: 3 independently calculated raw-byte SHA256 fingerprints; zero original-to-current independent checksum matches demonstrated. Full check 1 remains HOLD.** Retain all 25 experimental observations; this is not a finding that the runs are defective. No GKE or algorithm modification.
