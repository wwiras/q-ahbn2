# P3G-IMG — Exact-source local image preflight, 18 October 2026

**Decision: LOCAL IMAGE PRE-FLIGHT PASS / IMMUTABLE REGISTRY IMAGE NOT ESTABLISHED / CANARY HOLD.**

## Confirmed evidence

- Authoritative source: `wwiras/q-ahbn2`; verified exact image-build Git commit `932034b4d672e9043ee235362e5e7d68db0949f0`.
- GitHub Actions: https://github.com/wwiras/q-ahbn2/actions/runs/39127329941 — **completed SUCCESS**.
- Workflow: `.github/workflows/p3g-image-preflight.yml`.
- Local `linux/amd64` Docker build using `gke/app/Dockerfile.qahbn2`: PASS.
- Build checks include Git commit OCI revision label; imported `recovery_availability`, `peer`, `qahbn2_runtime` and K7 `controller`; generated protobuf `PeerService.NotifyRecoveryRejoin` service descriptor; peer handler and PeerState adapter; K7 churn export. All PASS.
- GitHub Actions archive artifact `p3g-image-preflight-evidence` ID `12136527954`. It includes build log, source hashes, image inspect, import check and SHA256SUMS.
- Local image build output SHA `sha256:1b358dd285e7d9cf2b26c9c61bad1c26ceb279bcd4ae5edc6ff641bbb7bd6514` is a **local image ID/config digest**, **NOT** a pushed registry manifest digest. Never use this ID as a GKE-deployable image reference.
- Separate P3G-V3 offline suite at source SHA `2f3d66ac7fc9ffb3653cc8005f00bd167c3232b5` PASS 61/61, evidence https://github.com/wwiras/q-ahbn2/actions/runs/39126351325.

## Limits and next strict release conditions

1. A Docker image was built and inspected in a temporary CI runner, **not pushed to a registry**. No immutable registry digest exists from this run. Candidate registry release needs distinct authorization, successful push, and read-back of immutable `name@sha256:...` manifest digest.
2. Verify that **both** peer StatefulSet and controller Job use exactly that approved manifest digest, with actual pod `imageID` recorded; no mixed-image deployment.
3. `P3G_RECOVERY_ENABLED` defaults to 0; any canary must explicitly enable and verify it in intended peer pods, with rollback available.
4. The old smoke launcher and D7-P3 verifier still pin historical image `sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`, not established to contain new P3G source. Do not use them unchanged.
5. Fresh **read-only** GKE admission is necessary (context, source revision, node capacity for N=20, namespace absence, privileges, resource quotas and cleanup provenance).
6. One nonformal **AHBN or Q-AHBN2** recovery canary requires separate explicit researcher authorization specifying exact source, registry image and strategy. Earlier Gossip-only authorization is not transferable.
7. No formal D7-F/D8 execution. Do not infer improved delivery from local build/CI results.

**Manuscript:** *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* remains under peer review at *Journal of Cloud Computing*, no DOI, not published.

**GitHub remains authoritative; Drive canonical corpus root reviewed; no Drive files modified during this build gate.**
