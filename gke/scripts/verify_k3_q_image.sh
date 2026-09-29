#!/usr/bin/env bash
set -euo pipefail
IMAGE="${IMAGE:-}"
EXPECTED_PLATFORM="${EXPECTED_PLATFORM:-linux/amd64}"

fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required"
command -v docker >/dev/null || fail "docker is required"

echo "Verifying registry image by platform-specific pull:"
echo "  image:    ${IMAGE}"
echo "  platform: ${EXPECTED_PLATFORM}"

# A successful platform-constrained pull is the authoritative practical check
# needed by K3: Docker must be able to resolve and materialize this tag for
# linux/amd64. This avoids relying on human-readable manifest formatting.
docker pull --platform "${EXPECTED_PLATFORM}" "${IMAGE}" >/dev/null   || fail "registry image cannot be pulled for ${EXPECTED_PLATFORM}"

ACTUAL="$(docker image inspect "${IMAGE}" --format '{{.Os}}/{{.Architecture}}' 2>/dev/null || true)"
[ -n "${ACTUAL}" ] || fail "pulled image configuration could not be inspected"
[ "${ACTUAL}" = "${EXPECTED_PLATFORM}" ]   || fail "pulled image configuration is ${ACTUAL}; expected ${EXPECTED_PLATFORM}"

DIGEST="$(docker image inspect "${IMAGE}" --format '{{join .RepoDigests "\n"}}' 2>/dev/null || true)"
echo "K3-Q IMAGE VERIFY PASS: ${IMAGE} = ${ACTUAL}"
[ -n "${DIGEST}" ] && echo "Repo digest: ${DIGEST}"
