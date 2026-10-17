# JCC-R1A-C3-D7-SM — Operational correction candidate (17 October 2026)

## Authority and scope
GitHub code/control repository: wwiras/q-ahbn2. The thesis repository MUM_FIT_ThesisWira is the thesis text authority. Evidence corpus: Google Drive q-ahbn2/output/evidence. Q-AHBN manuscript is **under peer review** at *Journal of Cloud Computing*, not published and without a DOI.

## Safety-only patch
- Topology validator: explicit Gossip seed-42 single-topology canary switch. Default five-treatment order remains unchanged.
- Smoke launcher: fail closed to canary mode; preserve failure evidence and SHA256 manifest on EXIT.
- Experiment runner: track namespace-create attempt, refuse deletion on missing UID/owner, use correctly quoted label lookup; record experiment and cleanup exit statuses independently. Treat Helm uninstall failure, namespace deletion failure, namespace-query failure, and remaining namespace as HOLD.

## Validation and limitations
Before this candidate commit, a separate **local prototype** runner passed 13 isolated mock cases: wrong context, preexisting namespace, namespace-create failure, failed/empty UID, failed/mismatched owner label, failed owner read, Helm install failure, rollout failure, TERM interruption, Helm uninstall failure, and namespace deletion failure. No GKE access was used. **The 13/13 result is NOT claimed as regression verification of the final committed source**, which still requires read-back, Bash/Python syntax checks and rerunning fault injection against exact GitHub checkout. No formal, scientific, or cloud execution is authorized.

## Controlled status
JCC-R1A-C3-D7-SM: HOLD — exact-commit regression outstanding.
Gossip NONFORMAL canary: HOLD 0/1. Remaining four smoke arms: HOLD 0/4. D7-F HOLD 0/25. D8 HOLD.

## Scientific freeze
D7-P2 experimental design, canonical AHBN controller and bounded Q-AHBN2 formulation not reopened. Do not count local mocks as GKE evidence. SIGKILL, connectivity loss, and namespace creation races still require manual post-failure verification.


## D7-SM-V1 exact-commit local verification (2026-10-17)

**Evidence source revision:** `fb264810a545ce26114bbd4608f24bef93deb89e` (read-back from GitHub main before this documentation update).

- `run_k7_experiment.sh`: exact Git blob `c58af41e551ca138bd3cf234d95f4f8bc1c248b4`; `bash -n` PASS; 16/16 isolated mock cases PASS, including namespace-create before/after mutation, UID/owner checks, Helm install, rollout, SIGTERM, Helm uninstall, delete, post-delete query and successful mock completion. Simulated failure outcomes can deliberately retain a namespace with a HOLD decision; no guarantee of automatic cleanup in unknown-ownership cases.
- `run_d7_smoke.sh`: exact Git blob `5e9d7611f6118bf4b6484db919b0dce44ea2f891`; `bash -n` PASS; 4/4 early-rejection checks PASS (missing approval, five-method request with/without extra flag, unsupported mode).
- The test evidence is available in the assistant-produced local evidence bundle `D7-SM-V1-exact-commit` as `regression.json`, `launcher_negative_tests.json`, `verification_summary.json` and `SHA256SUMS`; `sha256sum -c SHA256SUMS` PASS. This evidence has **not been independently confirmed in the Google Drive corpus**.
- **Outstanding:** full Python `gke/app/k7_exp11_tools.py` syntax and exact-commit canary topology-contract integration have not been executed. Original repository `gke/scripts/test_d7_p4_cleanup.py` remains the older five-case suite; these 16 cases were executed in a separate local test harness, not through that repository test script.
- **Gate decision: PARTIAL VERIFICATION / HOLD**, not PASS. Do not authorize GKE execution until remaining tests, durable evidence registration and reconciliation pass. Gossip 0/1 HOLD; other smoke 0/4 HOLD; D7-F 0/25 HOLD; D8 HOLD. No scientific protocol changes. The manuscript remains under peer review at *Journal of Cloud Computing*, unpublished and without a DOI.


## D7-SM-V1 final local regression adjudication — 2026-10-17 (supersedes partial status above)

**Decision: PASS — exact-commit LOCAL regression only.** **Live Gossip canary remains HOLD**, pending researcher review of archived evidence and point-of-execution safety checks. All tests were local; none contacted GKE.

**Authoritative source commit under test:** `fb264810a545ce26114bbd4608f24bef93deb89e`.
- Exact Git blob read-back matched `gke/scripts/run_k7_experiment.sh` (`c58af41e551ca138bd3cf234d95f4f8bc1c248b4`), `gke/scripts/run_d7_smoke.sh` (`5e9d7611f6118bf4b6484db919b0dce44ea2f891`), and `gke/app/k7_exp11_tools.py` (`cac6cc2d13bdf7430d42c03dec44aaf341e39ea6`).
- `bash -n`: 2/2 PASS. Exact-source Python `py_compile`: PASS for the experiment contract module and its two checked topology generation dependencies; their Git blobs matched the source revision.
- Local fault injection: **16/16** PASS, including namespace create before/after partial mutation, failed/missing UID, label failure/mismatch/read failure, Helm install failure, rollout failure, SIGTERM interruption, Helm uninstall failure, delete failure, post-delete-check failure, wrong context, preexisting namespace and mock success. Cleanup and experiment statuses are separate. In unknown-ownership cases, deletion is deliberately refused and manual review remains necessary.
- Smoke-launcher negative controls: **4/4** PASS, blocking missing approval, forbidden five-treatment mode with/without extra authorization, and invalid mode.
- Topology contract integration: **7/7** PASS; exact single Gossip seed-42 contract succeeds, original five-treatment contract succeeds, default single topology is rejected, canary rejects multiple treatments, wrong seed, wrong algorithm and mutated message count.
- **Total: 27/27 local checks PASS.** SHA256 manifest verified by `sha256sum -c SHA256SUMS`. Generated evidence contains full mock call lists, exit codes, expected local topologies, test harness and source-commit identity.
- Evidence package: `D7-SM-V1-exact-commit-evidence.zip` (SHA256 `561e2a8ba826ce18b2ab8f45bfe83be1865dbf0b668ff45861a380d757521eaa`). Package presently resides in the conversation evidence workspace; **its upload to the canonical Google Drive `output/evidence` has not been verified**. The researcher can archive this unchanged package and independently recompute the checksum.

**Scope limit:** This gate validates deterministic code paths and simulated failures only. It does NOT establish GKE workload completion, resource readiness, reliable live telemetry, or live namespace cleanup. The legacy five-case in-repo D7-P4 suite was not modified; a separate reproducible fault-injection harness is included in the evidence bundle. No scientific algorithm, parameters, experiments, results, manuscript claims or frozen AHBN contract were altered.

**Controlled statuses:** D7-SM-V1 local regression PASS; D7-SM Gossip live canary **HOLD 0/1**; remaining smoke **HOLD 0/4**; D7-F **HOLD 0/25**; D8 **HOLD**. Next decision is an independent package archival/read-back and canary execution-safety release review; the consent already given applies only to one NONFORMAL Gossip seed-42 run. Manuscript remains under peer review at *Journal of Cloud Computing*, not published and without a DOI.
