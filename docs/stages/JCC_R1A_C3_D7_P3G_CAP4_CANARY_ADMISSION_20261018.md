# P3G-CAP4 — Recovery canary preparation and final admission review (2026-10-18)

**Decision: PREPARATION / OFFLINE CHECKS PASS; LIVE CANARY HOLD pending specific researcher authorization.** This is not a report of deployed or confirmed recovery.

## Source of authority and verified changes

- GitHub experiment repo: https://github.com/wwiras/q-ahbn2
- Prior CAP3: `docs/stages/JCC_R1A_C3_D7_P3G_CAP3_LAUNCHER_VERIFICATION_20261018.md`.
- Candidate image approved for a future separately-authorized canary: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`.
- `gke/scripts/p3g_recovery_admission_readonly.sh` corrected to `qahbn2-d7-smoke-p3g-{ahbn,qahbn2}`, matching the recovery launcher. This admission script is READ-ONLY: local Helm rendering, GKE read queries, checksums, no create/apply/delete.
- `gke/scripts/run_k7_experiment.sh`: saves `controller_pods.json` and validates exactly one controller pod's `spec.image` and runtime `imageID` against pinned approved digest after controller Job completes. In recovery mode, validates 20 peers, recovery env `1`, pinned peer image, observed peer runtime IDs, namespace identity and ownership before cleanup.
- `tests/test_p3g_cap3_launcher.py` extended to 12 tests requiring controller runtime digest check. No algorithm/controller/learner source modification.
- Offline CI: https://github.com/wwiras/q-ahbn2/actions/runs/39132019629, **SUCCESS** at `c45de9009dd72e895c25e3cf2bce393a25cbb779`: 39 integrated P3G tests PASS, 12 launcher contract/negative tests PASS, 22 frozen parity/regression tests PASS = **73 tests**, with Bash syntax and compile checks. Later read-only script wording commit `6e7c1177cb12e93708b2851ac7c3b999d8c856cd` does not affect runtime/CI scope.

## Proposed controlled nonformal canary — NOT executed

- One strategy only at a time: **AHBN first**, seed 42, N=20, BA(m=2) graph, 240 messages at 0.4 s intervals, churn schedule retained from `gke/experiments/k5_q_formal.yaml` plus `k7_exp11_tools.py config --algorithm ahbn --seed 42`. This is a **nonformal diagnostic smoke**, never a formal D7-F result.
- Preserve exact configuration/topology, source, target list, failure/rejoin event schedule and peer role mapping. Preserve old and new evidence in separate folders and label the canary as P3G nonformal recovery-enabled.
- Repository source and deployed-image identity are DISTINCT: build source provenance `884f874c...`, running Helm/launcher code commit recorded at execution; immutable candidate digest stays the approved one.
- Controlled launcher `run_k7_experiment.sh` is recovery-enabled only when `P3G_RECOVERY_ENABLED=1` and a dedicated `qahbn2-d7-smoke-p3g-ahbn` namespace is absent. Historic default stays OFF. This generic runner is an execution primitive and does **not** itself provide an external authorization guard. Do NOT run merely because CAP4 has been prepared.
- Planned evidence: git SHA, dirty-worktree check, config/topology hashes, controller and peer spec/runtime digest, actual feature flag, source/target/epoch event logs, observed peer recovery events, per-message forwarding logs and quantitative outcomes, experiment and cleanup exit codes, namespace UID/owner-label receipts, SHA256SUMS, and upload under canonical RO4 Drive `output/evidence`. Check receipt completeness before scientific claims.
- **No automatic favourable outcome inferred**. `p3g_rejoin_notification.acknowledged` means notification RPC accepted, **not** successful transport recovery. `recovery_probe.recovered=true` after peer-local `GetStatus` validates transport recovery; require unique epoch/target event and matching `peer_availability` event. Forwarding must be observed for a later message to the recovered neighbor, with target absent from `unavailable_neighbors`; evaluate delivery ratio and duplicate/forwarding metrics separately.
- Do not treat a controller log `churn_recovered` as proof that all formerly unavailable peers were actually reintroduced. Correlate timelines and identify missing confirmations as inconclusive/failed, not successes.

## Additional admission caveats / safety

1. **Runtime cleanup and live recovery remain unverified.** The generic runner owns namespaces by verified UID/owner label and refuses deletion on mismatch, but actual cleanup proof only follows an authorized run.
2. Runtime controller imageID parity is now instrumented but has not been observed. CI tests assert code presence and early guards; not a Kubernetes simulation.
3. Evaluate the existing runner's `CREATE_ATTEMPTED=1` / `OWN_NAMESPACE=0` failure path if namespace creation succeeds but UID acquisition fails; its protective HOLD avoids unsafe deletion but may leave an orphan namespace needing manual, ownership-verified remediation. Never automatically delete unverified namespace.
4. `p3g_recovery_admission_readonly.sh` is for separate **preflight**, not for canary execution. Refresh read-only preflight immediately before authorized run using the matching P3G namespace.
5. Exact source of `k7_exp11_tools.py` includes historical frozen hashes. If generating config or running its validator fails due to controlled source updates, record as a provenance limitation; do not bypass/rewrite frozen checks silently. Do not infer a validation pass from offline CAP4 alone.
6. Researcher owns capacity and cost decisions; these are not CAP4 scientific blockers.

## Formal release conditions and next decision

- CAP4 **PREPARATION PASS** for source/CI and evidence plan; separate runtime authorization **PENDING**.
- Request an explicit one-run AHBN seed42 P3G diagnostic authorization before any `kubectl create`, `helm install`, or controller workload. If authorized, run exact-commit preflight and preserve all evidence; require runtime cleanup verified before further runs.
- D7-F and D8 remain **HOLD**, no claim that the recovery correction is validated on GKE.
- Manuscript submitted to **Journal of Cloud Computing**, under peer review, unpublished, no DOI. This CAP4 record does not change scientific conclusions.

References:
- Canonical Drive: https://drive.google.com/drive/folders/1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5
- Thesis authority: https://github.com/wwiras/MUM_FIT_ThesisWira
