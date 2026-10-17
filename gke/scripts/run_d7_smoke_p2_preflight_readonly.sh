#!/usr/bin/env bash
# Read-only P2 technical preflight: no deployment or mutation.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
EXPECTED_CONTEXT="gke_stoked-cosine-415611_us-central1-a_bcgossip-cluster"
EXPECTED_IMAGE="docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"
OUT="${ROOT}/output/evidence/$(date -u +%Y%m%dT%H%M%SZ)-D7-SM-P2-readonly"
mkdir -p "$OUT"
status="HOLD"
finish() {
  rc=$?
  trap - EXIT
  printf '%s\n' "$status" > "$OUT/preflight_status.txt"
  printf '%s\n' "$rc" > "$OUT/preflight_exit_code.txt"
  (cd "$OUT" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 shasum -a 256 > SHA256SUMS)
}
trap finish EXIT
{
  printf 'gate=P2-TECHNICAL-PREFLIGHT\nmode=READ_ONLY\nmethods=structured,dcsoc,ahbn,qahbn2\nseed=42\n'
  for tool in git kubectl helm python3; do
    command -v "$tool" >/dev/null || { echo "HOLD missing $tool"; exit 1; }
  done
  printf 'head=%s\n' "$(git rev-parse HEAD)"
  printf 'remote_main=%s\n' "$(git ls-remote origin refs/heads/main | awk '{print $1}')"
  test -z "$(git status --porcelain)" || { echo "HOLD dirty checkout"; exit 1; }
  test "$(git rev-parse HEAD)" = "$(git ls-remote origin refs/heads/main | awk '{print $1}')" || { echo "HOLD Git mismatch"; exit 1; }
  context="$(kubectl config current-context)"
  printf 'context=%s\n' "$context"
  test "$context" = "$EXPECTED_CONTEXT" || { echo "HOLD context mismatch"; exit 1; }
  kubectl cluster-info >/dev/null || { echo "HOLD cluster unavailable"; exit 1; }
  for method in structured dcsoc ahbn qahbn2; do
    ns="qahbn2-d7-smoke-$method"
    found="$(kubectl get namespace "$ns" --ignore-not-found -o name)"
    printf 'namespace_%s=%s\n' "$method" "${found:-ABSENT}"
    test -z "$found" || { echo "HOLD occupied namespace $ns"; exit 1; }
  done
  printf 'pinned_image=%s\n' "$EXPECTED_IMAGE"
  printf 'launcher_sha256=%s\n' "$(shasum -a 256 gke/scripts/run_d7_smoke_remaining.sh | awk '{print $1}')"
  printf 'runner_sha256=%s\n' "$(shasum -a 256 gke/scripts/run_k7_experiment.sh | awk '{print $1}')"
  printf 'validator_sha256=%s\n' "$(shasum -a 256 gke/app/k7_exp11_tools.py | awk '{print $1}')"
  bash -n gke/scripts/run_d7_smoke_remaining.sh gke/scripts/run_k7_experiment.sh
  python3 -m py_compile gke/app/k7_exp11_tools.py
  status="PASS_READ_ONLY"
  printf 'decision=%s\n' "$status"
} > "$OUT/technical_preflight.txt" 2>&1
cat "$OUT/technical_preflight.txt"
echo "P2 read-only evidence: $OUT"
