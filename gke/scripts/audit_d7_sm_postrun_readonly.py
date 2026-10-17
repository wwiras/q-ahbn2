#!/usr/bin/env python3
"""Read-only integrity + delivery audit for D7-SM four-method NONFORMAL evidence.

No Kubernetes calls, no file changes, no scientific/controller modifications.
Usage: python3 gke/scripts/audit_d7_sm_postrun_readonly.py \
    output/evidence/20261017T133327Z-D7-SM-remaining
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

METHODS = ("structured", "dcsoc", "ahbn", "qahbn2")
EXPECTED_IMAGE = "docker.io/wwiras/q-ahbn2@sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466"

def audit_manifest(folder: Path) -> dict:
    manifest = folder / "SHA256SUMS"
    if not manifest.is_file() or manifest.is_symlink():
        raise ValueError(f"missing/unsafe manifest: {manifest}")
    lines = manifest.read_text().splitlines()
    pattern = re.compile(r"^([0-9a-f]{64})  \./(.+)$")
    listed = {}
    for line in lines:
        match = pattern.fullmatch(line)
        if not match:
            raise ValueError(f"invalid SHA256SUMS record in {folder}: {line!r}")
        expected, relative = match.groups()
        path = Path(relative)
        if path.is_absolute() or ".." in path.parts or path.name == "SHA256SUMS":
            raise ValueError(f"unsafe SHA256SUMS path: {relative}")
        if relative in listed:
            raise ValueError(f"duplicate checksum path: {relative}")
        listed[relative] = expected
    existing = set()
    for file in folder.rglob("*"):
        if file.is_symlink():
            raise ValueError(f"symlink in evidence tree: {file}")
        if file.is_file() and file.name != "SHA256SUMS":
            existing.add(file.relative_to(folder).as_posix())
    if existing != set(listed):
        raise ValueError(f"evidence manifest mismatch in {folder}: missing={sorted(existing - set(listed))}, stale={sorted(set(listed) - existing)}")
    for relative, expected in listed.items():
        file = folder / relative
        h = hashlib.sha256()
        with file.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                h.update(block)
        if h.hexdigest() != expected:
            raise ValueError(f"SHA256 mismatch: {file}")
    return {"pass": True, "files": len(listed)}

def audit_run(root: Path, method: str) -> dict:
    path = root / "runs" / method
    integrity = audit_manifest(path)
    metrics = json.loads((path / "metrics.json").read_text())
    events = json.loads((path / "churn_events.json").read_text())
    pods = json.loads((path / "pods.json").read_text()).get("items", [])
    opportunities = events["delivery_opportunities"]
    total_expected = sum(int(r["expected_count"]) for r in opportunities)
    total_delivered = sum(int(r["delivered_count"]) for r in opportunities)
    ratio = total_delivered / total_expected
    if len(opportunities) != 240 or metrics["algorithm"] != method or metrics["seed"] != 42:
        raise ValueError(f"invalid coordinate/opportunities: {method}")
    if abs(ratio - float(metrics["delivery_ratio"])) > 1e-12:
        raise ValueError(f"delivery denominator mismatch: {method}")
    if len(pods) != 20 or not all(
        p["spec"]["containers"][0]["image"] == EXPECTED_IMAGE
        and p["status"]["containerStatuses"][0]["imageID"] == EXPECTED_IMAGE
        and p["status"]["containerStatuses"][0].get("ready") is True for p in pods
    ):
        raise ValueError(f"pod/runtime image identity mismatch: {method}")
    if not (path / "validation.txt").read_text().strip().endswith("K7 RESULT VALIDATION PASS") or (path / "cleanup_status.txt").read_text().strip() != "PASS":
        raise ValueError(f"validation/cleanup not PASS: {method}")
    for name in ("experiment_exit_status.txt", "cleanup_exit_status.txt", "namespace_cleanup_exit_status.txt"):
        if (path / name).read_text().strip() != "0":
            raise ValueError(f"nonzero run/cleanup status: {method}/{name}")
    return {
        "method": method, "integrity": integrity, "pods_ready": len(pods),
        "opportunities": len(opportunities), "expected": total_expected, "delivered": total_delivered,
        "delivery_ratio": ratio, "duplicates": metrics["duplicates"],
        "full_delivery_messages": sum(bool(r["full_delivery"]) for r in opportunities),
        "source_only_messages": sum(int(r["delivered_count"]) == 1 for r in opportunities)
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    base = (repo / "output" / "evidence").resolve()
    root = args.evidence_root.resolve()
    if root != base / "20261017T133327Z-D7-SM-remaining":
        raise ValueError("this audit is pinned to the 2026-10-17 four-method NONFORMAL smoke evidence")
    if (root / "smoke_exit_status.txt").read_text().strip() != "0":
        raise ValueError("outer launcher status is not zero")
    if not (root / "status.txt").read_text().startswith("FOUR NONFORMAL METHODS COMPLETED"):
        raise ValueError("outer completion classification missing")
    integrity = audit_manifest(root)
    per_method = [audit_run(root, method) for method in METHODS]
    print(json.dumps({
        "gate": "JCC-R1A-C3-D7-SM-POSTRUN-AUDIT-P1",
        "classification": "NONFORMAL", "seed": 42,
        "outer_manifest": integrity, "runs": per_method,
        "integrity_decision": "PASS",
        "scientific_release": "HOLD — delivery behavior requires causal analysis; this is not formal evidence",
        "formal_D7_F": "HOLD", "D8": "HOLD"
    }, indent=2))
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"POSTRUN AUDIT HOLD: {error}", file=sys.stderr)
        sys.exit(1)
