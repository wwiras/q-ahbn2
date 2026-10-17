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
