#!/usr/bin/env bash
set -euo pipefail
IMAGE="${IMAGE:-}"
EXPECTED_ARCH="${EXPECTED_ARCH:-amd64}"
fail(){ echo "ERROR: $*" >&2; exit 1; }
[ -n "${IMAGE}" ] || fail "IMAGE is required"
command -v docker >/dev/null || fail "docker is required"

RAW="$(docker buildx imagetools inspect --raw "${IMAGE}" 2>/dev/null)" || fail "cannot inspect pushed image: ${IMAGE}"

ARCH="$(printf '%s' "${RAW}" | python3 -c '
import json,sys
x=json.load(sys.stdin)
if "architecture" in x:
    print(x["architecture"])
elif "manifests" in x:
    vals=[m.get("platform",{}).get("architecture") for m in x["manifests"]]
    vals=[v for v in vals if v and v != "unknown"]
    print(",".join(sorted(set(vals))))
else:
    print("")
')"

[ -n "${ARCH}" ] || fail "image architecture could not be determined"
case ",${ARCH}," in
  *,"${EXPECTED_ARCH},"*) ;;
  *) fail "image architecture is ${ARCH}; expected ${EXPECTED_ARCH}" ;;
esac

echo "K3-Q IMAGE VERIFY PASS: ${IMAGE} includes linux/${EXPECTED_ARCH}"
