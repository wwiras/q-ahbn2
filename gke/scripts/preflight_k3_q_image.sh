#!/usr/bin/env bash
set -euo pipefail
IMAGE="${IMAGE:-}"
fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required"

IMAGE="${IMAGE}" bash "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/verify_k3_q_image.sh"

docker run --rm --platform linux/amd64 --entrypoint python "${IMAGE}" -c '
import peer
import gen_topology
import dcsoc_maintenance
import qahbn2_runtime
import controller
print("K3-Q CONTAINER IMPORT PREFLIGHT PASS")
' || fail "container import preflight failed"

echo "K3-Q IMAGE PREFLIGHT PASS"
