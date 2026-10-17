# JCC-R1A-C3-D7-SM-CANARY — Evidence archival and final safety review (2026-10-17)

## Decision
**EVIDENCE ARCHIVAL PASS; STATIC CODE SAFETY REVIEW PASS WITH RESIDUAL CONDITIONS; LIVE GKE CANARY HOLD.** No cloud mutation performed in this gate. The researcher previously approved possible GKE costs for **one** NONFORMAL Gossip seed-42 canary only, not the remaining smoke methods or any formal runs. This archived-review outcome does not substitute for fresh, point-of-execution admission.

## Authority and provenance
- Code/control authority: `wwiras/q-ahbn2`. Reviewed current `main` at `576bfafa54b0869013f077f6b7c067e3a640ed3c`.
- Test source revision: `fb264810a545ce26114bbd4608f24bef93deb89e`. Reviewed Bash file blobs remain unchanged on current `main`: `run_d7_smoke.sh` = `5e9d7611f6118bf4b6484db919b0dce44ea2f891`; `run_k7_experiment.sh` = `c58af41e551ca138bd3cf234d95f4f8bc1c248b4`.
- Canonical Drive evidence folder: https://drive.google.com/drive/folders/1hN6CCIR0qB0eEP9uBmB4UO9gPS3nXKED within `q-ahbn2/output/evidence`.
- Compared all **19/19** Drive artifacts (including SHA256SUMS, the 16-case test harness, run logs, contract tests, and topology/configuration inputs) byte-for-byte against their local original files: **PASS**. Local `sha256sum -c SHA256SUMS`: PASS. Archive ZIP `D7-SM-V1-exact-commit-evidence.zip` SHA256 `561e2a8ba826ce18b2ab8f45bfe83be1865dbf0b668ff45861a380d757521eaa` verified locally; the **individual extracted files** are archived in Drive and match. Do not claim that the ZIP itself is present in Drive.
- D7-SM-V1 exact-source local tests: **27/27 PASS**. They demonstrate local code behavior, not live GKE runtime.

## Frozen canary scope
Exactly one **Gossip**, seed `42`, NONFORMAL; BA(m=2), `N=20`, 240 messages at 0.4 s intervals; planned churn leave offsets 1, 26, 51 and 76 seconds; namespace `qahbn2-d7-smoke-gossip`, Kubernetes context `gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster`; container `docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`. Frozen design and AHBN/Q-AHBN2 controllers are unchanged.

## Static execution safety review
- Launcher rejects missing approval and all non-canary modes; one Gossip topology uses explicit canary validation, default five-method contract unchanged.
- Runner checks Kubernetes context, empty dedicated namespace, exact image digest, namespace UID and owner label before cleanup; logs experiment/cleanup statuses separately; preserves failure evidence and refuses unsafe deletion when namespace ownership cannot be proven.
- **Residual operational risk:** namespace-create may partially succeed before an error or UID retrieval failure, in which case manual namespace reconciliation is necessary. `SIGKILL`, disconnection, scheduling failure and cluster-side resource changes are not controlled by local mocks. Do not treat a local cleanup PASS as live cleanup proof.
- The read-only GKE admission from 2026-10-17 is point-in-time, not valid proof of the state immediately before execution. The current admission script considers at least **one** node Ready; that is not sufficient assurance that twenty pods can be scheduled simultaneously.
- `run_d7_smoke.sh` demands clean worktree but does not itself enforce a particular approved remote `main` revision. Require explicit revision parity check with GitHub `main` immediately before execution, alongside intended context and namespace absence.
- Live execution must be researcher-performed, one nonformal canary only. It requires a **fresh** read-only admission, confirmation of adequate cluster capacity and quota/cost exposure, validated exact source revision/worktree, user-controlled interruption/cleanup plan, and independent post-run review of namespace absence, run logs, metrics, image IDs, run marker and SHA256 checksums.

## Gate and next decision
- **Evidence archival: PASS.**
- **Static safety review: PASS, CONDITIONAL** (the guardrails are present; dynamic cluster conditions unknown).
- **LIVE CANARY RELEASE: HOLD** until those fresh checks are independently examined. No live command released here.
- Gossip canary **0/1 HOLD**, other four smoke **0/4 HOLD**, D7-F **0/25 HOLD**, D8 **HOLD**.
- Next controlled gate: `JCC-R1A-C3-D7-SM-CANARY-PREEXEC` — fresh read-only cluster admission, exact checkout/capacity/cost confirmation and explicit one-canary execution release review. After a researcher run, audit evidence and cleanup before declaring canary PASS.
- Manuscript is under peer review at *Journal of Cloud Computing*, unpublished, no DOI.
