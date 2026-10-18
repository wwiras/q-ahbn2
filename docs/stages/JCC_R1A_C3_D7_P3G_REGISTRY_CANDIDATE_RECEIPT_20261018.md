# P3G-REG — Docker Hub candidate upload report (18 October 2026)

**Decision: RESEARCHER-REPORTED REGISTRY PUBLICATION PASS; INDEPENDENT IMAGE PARITY / GKE ADMISSION HOLD.**

The researcher ran `gke/scripts/p3g_publish_single_candidate.sh` on the Mac from a clean, fast-forwarded `main` checkout. Terminal output showed successful completion:

- Exact source: `884f874c634a2e4a854a8f61b94354a06547c93e`.
- Reported immutable registry image: `docker.io/wwiras/q-ahbn2@sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f`.
- Local receipt directory: `output/evidence/p3g-dockerhub-candidate-884f874c634a`.
- Script's verification sequence: local linux/amd64 build; peer/recovery/controller import assertions; Docker push; `docker buildx imagetools inspect` of tag and immutable digest; source hashes and evidence SHA256SUMS.
- A host/image architecture warning (Apple Silicon arm64 vs linux/amd64) was displayed, not a reported fatal error.

**Evidence boundary:** This GitHub record is based on the researcher's terminal output and the committed script, **not** an independent registry API read or uploaded receipt contents. Registry digest has been reported and script read-back apparently succeeded; receipt contents, remote platform, and runtime peer/controller pod imageID parity are **not independently audited**.

**Next gates:** Obtain the local receipt (source_sha256.txt, imports.txt, registry_inspect.txt, immutable_registry_inspect.txt, SHA256SUMS); verify the digest from a separate authenticated registry read; confirm peer StatefulSet and controller Job both render this same immutable digest; perform fresh **read-only** GKE admission only with appropriate access. Any nonformal recovery canary requires separate researcher authorization. No GKE deployment, canary or formal D7-F/D8 run authorized.

No frozen AHBN/Q-AHBN2 scientific algorithm change; no claim of improved delivery. Journal of Cloud Computing manuscript remains under peer review, no DOI. Canonical Drive evidence upload is pending; do not claim it was synchronized.
