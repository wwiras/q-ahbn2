#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
IMAGE="${IMAGE:-}"
PLATFORM="${PLATFORM:-linux/amd64}"
fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required; use a fresh immutable formal tag"
cd "${ROOT_DIR}"
python3 gke/scripts/k5_q_prep_audit.py >/dev/null
docker buildx build --platform "${PLATFORM}" -f gke/app/Dockerfile.qahbn2 -t "${IMAGE}" --push .
IMAGE="${IMAGE}" EXPECTED_PLATFORM=linux/amd64 bash gke/scripts/verify_k3_q_image.sh
IMAGE="${IMAGE}" bash gke/scripts/preflight_k3_q_image.sh
echo "K5-Q FORMAL IMAGE PREP PASS"
