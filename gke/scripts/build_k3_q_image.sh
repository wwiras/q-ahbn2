#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
IMAGE="${IMAGE:-}"
PLATFORM="${PLATFORM:-linux/amd64}"

fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required, e.g. IMAGE=wwiras/q-ahbn2:k3q-smoke-20260929"
command -v docker >/dev/null || fail "docker is required"

cd "${ROOT_DIR}"
echo "Building Q-AHBN2 K3 smoke image"
echo "  image:    ${IMAGE}"
echo "  platform: ${PLATFORM}"

docker buildx build   --platform "${PLATFORM}"   -f gke/app/Dockerfile.qahbn2   -t "${IMAGE}"   --push   .

echo "Inspecting pushed manifest:"
docker buildx imagetools inspect "${IMAGE}"
IMAGE="${IMAGE}" EXPECTED_ARCH=amd64 bash gke/scripts/verify_k3_q_image.sh
echo "K3-Q IMAGE BUILD/PUSH PASS: linux/amd64 verified"
