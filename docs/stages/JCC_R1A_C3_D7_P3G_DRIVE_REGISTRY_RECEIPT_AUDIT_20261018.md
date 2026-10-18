# P3G-REG — Canonical Google Drive receipt audit (18 October 2026)

**Decision: REGISTRY CANDIDATE RECEIPT PASS; DEPLOYMENT IMAGE PARITY AND GKE ADMISSION HOLD.**

Canonical evidence directory (found directly through connected Google Drive): https://drive.google.com/drive/folders/1ooo2SVnCDwJgfsEjnL7hfg2y9qfv67EI under RO4 `output/evidence`.

All 12 files present: `SHA256SUMS`, `release_status.txt`, `candidate_tag.txt`, `immutable_image.txt`, `immutable_registry_inspect.txt`, `registry_inspect.txt`, `push.log`, `local_config_digest.txt`, `imports.txt`, `build.log`, `source_sha256.txt`, `source_commit.txt`.

- Exact build source: `884f874c634a2e4a854a8f61b94354a06547c93e`.
- Candidate tag: `docker.io/wwiras/q-ahbn2:p3g-recovery-884f874c634a2e4a854a8f61b94354a06547c93e`.
- Registry immutable reference: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`.
- `push.log` reports published manifest digest `7e5a3d...` size 4905. Tag and immutable-reference `docker buildx imagetools inspect` receipts both return the identical digest and Docker manifest v2 media type.
- Build log confirms `python:3.11-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce` base and copies peer, recovery adapter, runtime, shared controller, K7 controller; generated proto. `imports.txt`: `P3G_IMAGE_IMPORTS_PASS`.
- Local Docker config image ID `sha256:0366a2fecf516ac56d90f902bbbc94ab1a9b5d29c4972237c0877b054b674127` is **not** the registry manifest digest.
- Drive `SHA256SUMS` contains one entry for each of the other 11 files. It was retrieved. Full independent byte-level recomputation of all 11 Drive file hashes has not been completed; do not describe as cryptographically verified end-to-end.

**Scope:** Receipt consistency and script-recorded registry read-back PASS; no separate fresh registry API fetch was performed in this audit. No GKE pod `imageID` parity verified. Next gate: read-only verify peer StatefulSet/controller Job templates resolve to the same immutable reference, and independently check digest against registry. GKE cluster read-only admission remains separate; canary requires new explicit authorization. D7-F and D8 HOLD.

No changes to frozen algorithms, no performance or delivery claim. Journal of Cloud Computing manuscript under peer review, no DOI. This audit read Drive directly; no new Drive files created.
