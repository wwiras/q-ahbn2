# P3G-REG — Registry image release boundary (2026-10-18)

**Decision: REGISTRY PUBLICATION NOT AUTHORIZED / HOLD.** This is a controlled preparation gate, not an image push, GKE deployment, canary or formal experiment.

## Verified starting point

- Authoritative `wwiras/q-ahbn2` default branch `main`, reviewed at `07cd7064d171d8c9b77bb9ef200defc7db3ca3a2`.
- P3G-IMG local container build/import preflight: PASS, workflow https://github.com/wwiras/q-ahbn2/actions/runs/39127329941 at source `932034b4d672e9043ee235362e5e7d68db0949f0`.
- P3G-V3 61 offline regression assertions PASS at source `2f3d66ac7fc9ffb3653cc8005f00bd167c3232b5`.
- Local image ID is **not** a registry digest. Existing `docker.io/wwiras/q-ahbn2@sha256:8a47cedb...` is a historical smoke image and must not be reused as proof of new P3G code.
- Canonical experiment Google Drive `output/evidence` folder reviewed read-only. No P3G registry receipt is present.

## Registry release requirements (one immutable version)

1. Specify the registry and repository destination, credentials and publish authority. Use the existing Docker Hub repository only if expressly approved. Do not disclose credentials in logs or Git commits.
2. Pin exact source commit (must contain the tested recovery correction) and clean checkout. Build `linux/amd64` from `gke/app/Dockerfile.qahbn2`, preserving OCI revision and input SHA256 provenance.
3. Verify **inside the image** the peer, Q-AHBN2 runtime, controller entrypoint and generated `NotifyRecoveryRejoin` protocol. Preserve build/import logs and SHA256 manifest.
4. Publish a unique, nonmoving candidate tag only after explicit image-push authorization. Read back registry's canonical immutable `repository@sha256:<manifest_digest>`. Record manifest digest separate from local image/config digest.
5. Inspect digest mapping used by peer StatefulSet **and** controller Job in the chart/rendered manifests. **Do not assert actual pod imageID parity until live pod inspection.**
6. Preserve provenance receipt (source SHA, image repository, tag, manifest digest, platform, build workflow URL, UTC, checksums and release scope) in authoritative GitHub record and canonical Drive evidence folder when uploaded.
7. Newly published image is only a **candidate**. Fresh read-only GKE admission, explicit recovery flag and a separately approved ONE nonformal AHBN or Q-AHBN2 canary are later gates.

No frozen AHBN/Q-AHBN2 algorithm change; no performance claims. D7-F/D8 remain HOLD. The Journal of Cloud Computing manuscript is under peer review, no DOI and not published.

**Blocker:** The user's message repeats the intended separate release action but does not explicitly authorize a registry push, select a registry destination or identify credentials usable by this connected GitHub tool. GitHub connector supports repository/Actions reading and source updates; it does not itself expose a direct container registry push action. Do not attempt a push via unapproved secret-bearing workflow.
