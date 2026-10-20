# D8 — Archived integrity and protocol audit decision (2026-10-20)

**Decision: HOLD scientific validation.** D7-F execution 25/25 is reported, but file-by-file integrity and protocol conformance are NOT independently closed. This is a fail-closed evidence decision, not an assertion that the experiments are defective.

## Inspected live sources
- Read `docs/stages/D8_A_B_PRELIMINARY_RECONCILIATION_20261020.md` in `wwiras/q-ahbn2`. Its status is PARTIAL/provisional and its seed44 recovery discrepancy and seed43 negative paired delivery result remain unresolved.
- Listed canonical Drive `q-ahbn2/output/evidence` and identified five formal roots dated 2026-10-20: `032934Z` seed42; `035637Z` seed43; `041621Z` seed44; `043745Z` seed45; `045636Z` seed46.
- Listed `runs/seed42` through `runs/seed46`: each contains five method directories (gossip, structured, dcsoc, ahbn, qahbn2): **25 folder coordinates present**.
- Listed all 23 direct file names under `runs/seed46/qahbn2`, `ahbn`, `dcsoc`, `structured`, and `gossip`. They include `metrics.json`, `run_manifest.json`, `churn_events.json`, controller/pod logs, namespace and Helm cleanup files, exit status, and topology/configuration artifacts.
- Read seed46 Q-AHBN2 `cleanup_exit_status.txt` = `0`, `cleanup_status.txt` = `PASS`; the namespace check error file was empty.
- Retrieved raw-file references for selected seed46 JSON manifest/metric objects, but no independent all-file raw-byte SHA256 comparison was completed.

## Boundaries and blockers
1. Folder/file presence **does not** verify raw-byte integrity. A complete manifest of all 25 runs and per-file archived checksums must be checked against source bytes; no SHA256 PASS is asserted here.
2. No complete inspection of the 25 run manifests, per-pod runtime digests, deployed configuration, experiment exit, cleanup and namespace-absence records, or workload/churn event traces has been completed.
3. The seed44 Gossip recovery event (27.44 s vs 18 s censoring threshold, repeated m77) still requires timestamp-level adjudication. Preserve raw data; no post-hoc exclusion.
4. Seed43 Q-AHBN2-versus-AHBN delivery was negative; preserve it. No universal superiority claim.
5. The previously reported paired +21.09 percentage-point delivery difference and CI are **provisional**. Full four-metric summary, dispersion, paired effects, and protocol/validity checks are required before science closure.
6. The absence of full verification is an **audit-completeness limitation**, not proof that a given GKE run failed.

## Next evidence-only checks
Read/checksum the 25 `run_manifest.json` and `metrics.json` objects; verify all run exit and cleanup outcomes; reconcile exact source/image and per-pod imageID, topology, seeds, traffic/churn schedules and target IDs; inspect raw recovery traces; compute reproducible per-method and paired four-metric tables. Keep all methods and all seeds, and leave original evidence and algorithms unchanged.

**Status: D8 HOLD. No GKE, no algorithm modification, no scientific closure.** Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* remains **under peer review** at *Journal of Cloud Computing*; not published; no DOI.

## Follow-up offline readback (2026-10-20)
- Re-read canonical Drive `output/evidence/` inventory: all five dated formal seed roots remain discoverable; the older `20261020T023432Z-K5Q-formal` root is separate and must not be silently incorporated into the formal 25-coordinate matrix.
- Re-read the pre-existing `D8_A_B_PRELIMINARY_RECONCILIATION_20261020.md` and this decision record against GitHub. Preliminary delivery figures and outstanding protocol issues remain as previously documented.
- Attempted comprehensive nested 25-folder inventory through the connector, but that request was interrupted by the connector's per-call limit. No complete run-by-run readback, SHA256 comparison, full four-metric statistical analysis or timestamp-level seed44 adjudication resulted from this follow-up.
- Existing sampled seed46 archives show `k7-exp11-v2`, 240 messages at planned 0.4-second intervals, churn offsets +1/+26/+51/+76 s, targets 0/5/10/15, and contract hash `5b26ed302abc57ce2816511f5257da7aca488ba7f3d6686e52483cd3f5675a7d`. This is sampled configuration evidence, not a finding that all 25 runs conformed.
- **Decision unchanged: D8 HOLD.** Missing verification must not be confused with demonstrated experimental invalidity. No algorithm change, new GKE run, exclusion, or manuscript result update was performed.
