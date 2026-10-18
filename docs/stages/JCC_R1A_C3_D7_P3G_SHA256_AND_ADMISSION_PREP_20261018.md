# P3G-ADM — Evidence integrity and read-only admission preparation (18 October 2026)

**Decision: CANONICAL RECEIPT SHA256 VERIFICATION PASS (11/11); DEPLOYMENT TEMPLATE DIGEST PARITY CONDITIONAL PASS; RECOVERY-SPECIFIC ADMISSION PREPARED, NOT EXECUTED; CANARY HOLD.**

## Independently verified Drive corpus

Folder: https://drive.google.com/drive/folders/1ooo2SVnCDwJgfsEjnL7hfg2y9qfv67EI

The complete 12-file folder was fetched through connected Google Drive. Byte-for-byte SHA256 values were recomputed locally on the 11 original evidence files and compared against the Drive `SHA256SUMS` manifest. Result: **11/11 MATCH; zero missing or mismatched files**. Files: `build.log`, `candidate_tag.txt`, `immutable_image.txt`, `immutable_registry_inspect.txt`, `imports.txt`, `local_config_digest.txt`, `push.log`, `registry_inspect.txt`, `release_status.txt`, `source_commit.txt`, `source_sha256.txt`. The manifest `SHA256SUMS` is the comparison authority, not itself an independently signed artifact. This verifies retained evidence integrity, not registry runtime presence or experimental improvement.

Candidate: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`. Image source `884f874c634a2e4a854a8f61b94354a06547c93e`. Local config ID distinct from published manifest digest.

## Read-only admission

New prepared script: `gke/scripts/p3g_recovery_admission_readonly.sh`. Restricts AHBN or Q-AHBN2, uses new immutable manifest digest, local Helm template rendering, N=20, peer-controller identical image, strict `P3G_RECOVERY_ENABLED=1` peer environment assertion, correct GKE context, no existing dedicated namespace, node readiness/amd64, cluster quotas and limit ranges, RBAC read-only queries, and immutable local SHA256 evidence.

**Critical current blocker:** The existing `gke/helm/ahbn/templates/statefulset.yaml` does not inject `P3G_RECOVERY_ENABLED=1`. Therefore the prepared gate deliberately **fails closed on local manifest inspection** before any GKE access or admission PASS claim. Explicit deployment feature flag must be separately reviewed and added, defaulting disabled for other runs. No Helm template or scientific algorithm was modified in this gate.

**Limitations:** The script has been prepared but not executed in the researcher's local authenticated environment; no real cluster access, capacity proof, live pod digest parity, cleanup verification or canary. The existing historical Gossip-only launcher `gke/scripts/run_d7_smoke.sh` remains untouched and must not be used for P3G canary. D7-F/D8 HOLD. Any canary requires separate explicit authorization. No claimed performance improvement.

**Manuscript:** under peer review at Journal of Cloud Computing, no DOI, not published.
