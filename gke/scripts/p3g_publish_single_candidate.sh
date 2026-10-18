#!/usr/bin/env bash
# P3G single-candidate Docker Hub upload. Explicitly approved publication only; no GKE.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
EXPECTED_SHA="${P3G_SOURCE_SHA:?HOLD: exact source SHA required}"
REPO="docker.io/wwiras/q-ahbn2"
[[ "${P3G_DOCKERHUB_UPLOAD_APPROVED:-}" == "YES" ]] || { echo "HOLD: publication approval environment gate missing"; exit 1; }
for bin in docker git sha256sum; do command -v "$bin" >/dev/null || { echo "HOLD: missing $bin"; exit 1; }; done
[[ "$EXPECTED_SHA" =~ ^[0-9a-f]{40}$ ]] || { echo "HOLD: invalid source SHA"; exit 1; }
ACTUAL_SHA="$(git rev-parse HEAD)"
[[ "$ACTUAL_SHA" == "$EXPECTED_SHA" ]] || { echo "HOLD: checkout SHA differs from nominated source; set P3G_SOURCE_SHA only for reviewed exact commit"; exit 1; }
[[ -z "$(git status --porcelain)" ]] || { echo "HOLD: dirty worktree"; exit 1; }
[[ -n "${DOCKERHUB_USERNAME:-}" && "$DOCKERHUB_USERNAME" == "wwiras" ]] || { echo "HOLD: Docker Hub username must be wwiras"; exit 1; }
[[ -n "${DOCKERHUB_TOKEN:-}" ]] || { echo "HOLD: DOCKERHUB_TOKEN must be set securely; do not put token in command history"; exit 1; }
TAG="p3g-recovery-${EXPECTED_SHA}"
IMAGE="${REPO}:${TAG}"
OUT="${P3G_RECEIPT_DIR:-output/evidence/p3g-dockerhub-candidate-${EXPECTED_SHA:0:12}}"
[[ ! -e "$OUT" ]] || { echo "HOLD: receipt folder already exists; do not overwrite"; exit 1; }
mkdir -p "$OUT"
printf "%s\n" "$EXPECTED_SHA" > "$OUT/source_commit.txt"
sha256sum gke/app/Dockerfile.qahbn2 gke/app/peer.proto gke/app/peer.py gke/app/recovery_availability.py gke/app/qahbn2_runtime.py gke/app/controller_shared.py gke/app/k7_controller.py > "$OUT/source_sha256.txt"
printf "%s" "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin >/dev/null
unset DOCKERHUB_TOKEN
docker buildx build --platform linux/amd64 -f gke/app/Dockerfile.qahbn2 --label "org.opencontainers.image.revision=${EXPECTED_SHA}" -t "$IMAGE" --load . > "$OUT/build.log" 2>&1
docker run --rm --entrypoint python "$IMAGE" -c 'import recovery_availability,peer,qahbn2_runtime,controller; assert "NotifyRecoveryRejoin" in peer.peer_pb2.DESCRIPTOR.services_by_name["PeerService"].methods_by_name; assert hasattr(peer.PeerService,"NotifyRecoveryRejoin"); assert hasattr(peer.PeerState,"notify_recovery_rejoin"); assert callable(controller.run_k7_churn); print("P3G_IMAGE_IMPORTS_PASS")' > "$OUT/imports.txt"
docker image inspect "$IMAGE" --format "{{.Id}}" > "$OUT/local_config_digest.txt"
[[ "$(docker image inspect "$IMAGE" --format "{{.Os}}/{{.Architecture}}")" == "linux/amd64" ]] || { echo "HOLD: wrong platform"; exit 1; }
docker push "$IMAGE" > "$OUT/push.log" 2>&1
docker buildx imagetools inspect "$IMAGE" > "$OUT/registry_inspect.txt"
DIGEST="$(sed -n "s/^Digest:[[:space:]]*\(sha256:[[:xdigit:]]\{64\}\).*$/\1/p" "$OUT/registry_inspect.txt" | head -n 1)"
[[ "$DIGEST" =~ ^sha256:[a-f0-9]{64}$ ]] || { echo "HOLD: cannot verify manifest digest"; exit 1; }
IMMUTABLE="${REPO}@${DIGEST}"
docker buildx imagetools inspect "$IMMUTABLE" > "$OUT/immutable_registry_inspect.txt"
grep -F "$DIGEST" "$OUT/immutable_registry_inspect.txt" >/dev/null || { echo "HOLD: immutable digest read-back not verified"; exit 1; }
printf "%s\n" "$IMAGE" > "$OUT/candidate_tag.txt"
printf "%s\n" "$IMMUTABLE" > "$OUT/immutable_image.txt"
printf "%s\n" "REGISTRY CANDIDATE PUBLISHED / GKE HOLD / D7-F HOLD / D8 HOLD" > "$OUT/release_status.txt"
(cd "$OUT" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 -r sha256sum > SHA256SUMS)
echo "P3G REGISTRY RECEIPT: $OUT"
echo "IMMUTABLE IMAGE: $IMMUTABLE"
echo "NO GKE DEPLOYMENT AUTHORIZED"
