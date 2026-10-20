#!/usr/bin/env python3
"""Read-only SHA256 inventory for the five formal D8-I1 evidence roots."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_ROOT = ROOT / "output" / "evidence"
OUTPUT_ROOT = ROOT / "output" / "d8_integrity"
FORMAL_ROOT_SEEDS = {
    "20261020T032934Z-K5Q-formal": 42,
    "20261020T035637Z-K5Q-formal": 43,
    "20261020T041621Z-K5Q-formal": 44,
    "20261020T043745Z-K5Q-formal": 45,
    "20261020T045636Z-K5Q-formal": 46,
}
METHODS = ("gossip", "structured", "dcsoc", "ahbn", "qahbn2")
EXPECTED_RUN_FILES = (
    "churn_events.json",
    "metrics.json",
    "run_manifest.json",
    "topology_role_mapping.json",
    "cleanup_exit_status.txt",
    "cleanup_status.txt",
    "namespace_check_error.txt",
    "namespace_cleanup_exit_status.txt",
    "helm_cleanup_exit_status.txt",
    "namespace_cleanup.txt",
    "helm_cleanup.txt",
    "logs.jsonl",
    "final_snapshot.jsonl",
    "controller.log",
    "controller_pods.json",
    "pod_readiness_evidence.txt",
    "pods.json",
    "experiment_exit_status.txt",
    "peer_stream.jsonl",
    "controller_job.json",
    "peer_stream.err",
    "statefulset.json",
    "generated_config.yaml",
    "topology.json",
)
ROOT_SUPPORT_FILES = {
    "K4_Q_K8S_VALIDATION_FREEZE.md",
    "expected_image_digest.txt",
    "git_commit.txt",
    "git_status.txt",
    "image.txt",
    "k5_q_formal_contract.py",
    "started_utc.txt",
    "terminal.log",
}
SUPPORT_DIRECTORIES = {"configs", "generated", "raw", "target-selection"}
CHUNK_SIZE = 1024 * 1024
DATALESS_FLAG = getattr(stat, "SF_DATALESS", 0x40000000)
JOURNAL_NAME = "sha256_resume.jsonl"
CSV_FIELDS = (
    "relative_path",
    "seed",
    "method",
    "artifact_category",
    "size_bytes",
    "sha256",
    "audit_outcome",
    "comparison_status",
    "same_day_source_comparison",
    "reference_sha256",
    "is_expected_primary",
    "is_empty",
    "duplicate_of",
    "error",
)

# These three digests are documented as same-day raw-byte fingerprints obtained
# from Drive, not as checksums created by the experiment at execution time.
SAME_DAY_DRIVE_FINGERPRINTS: dict[str, dict[str, Any]] = {
    "20261020T032934Z-K5Q-formal/runs/seed42/qahbn2/run_manifest.json": {
        "size_bytes": 757,
        "sha256": "e87f76a684a8a6ef9c2a85f09dee0b98c91de40bad6c507dda765af64dadf179",
        "source": "Drive raw-byte retrieval by file ID, documented 2026-10-20",
        "source_record": "docs/stages/D8_I1_ARCHIVED_FILE_INVENTORY_20261020.md",
    },
    "20261020T032934Z-K5Q-formal/runs/seed42/qahbn2/metrics.json": {
        "size_bytes": 1742,
        "sha256": "0a825eddcc440ab2a7022a4726306b300c308540b5cc1200f37f45bd1f61dc51",
        "source": "Drive raw-byte retrieval by file ID, documented 2026-10-20",
        "source_record": "docs/stages/D8_I1_ARCHIVED_FILE_INVENTORY_20261020.md",
    },
    "20261020T032934Z-K5Q-formal/runs/seed42/qahbn2/cleanup_status.txt": {
        "size_bytes": 5,
        "sha256": "c26de83abdc9496cd1301470918ec39ecca1cf389ef0ae1c6504da1800d1c431",
        "source": "Drive raw-byte retrieval by file ID, documented 2026-10-20",
        "source_record": "docs/stages/D8_I1_ARCHIVED_FILE_INVENTORY_20261020.md",
    },
}


class AuditInterrupted(Exception):
    """Test-only interruption after a durable file checkpoint."""


def sha256_stream(path: Path, chunk_size: int = CHUNK_SIZE) -> tuple[str, int, os.stat_result]:
    """Hash a regular file without following a final-component symbolic link."""
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise OSError(f"not a regular file: {path}")
    if DATALESS_FLAG and before.st_flags & DATALESS_FLAG:
        raise OSError(f"macOS dataless cloud placeholder: {path}")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        if not stat.S_ISREG(opened.st_mode):
            raise OSError(f"opened object is not a regular file: {path}")
        if (opened.st_dev, opened.st_ino) != (before.st_dev, before.st_ino):
            raise OSError(f"file identity changed before read: {path}")
        if DATALESS_FLAG and opened.st_flags & DATALESS_FLAG:
            raise OSError(f"macOS dataless cloud placeholder: {path}")
        digest = hashlib.sha256()
        bytes_read = 0
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            while block := stream.read(chunk_size):
                digest.update(block)
                bytes_read += len(block)
        after = os.fstat(descriptor)
        if (opened.st_dev, opened.st_ino, opened.st_size, opened.st_mtime_ns) != (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
        ):
            raise OSError(f"file changed while being hashed: {path}")
        if bytes_read != after.st_size:
            raise OSError(
                f"short read: read {bytes_read} bytes, stat reports {after.st_size}"
            )
        return digest.hexdigest(), bytes_read, after
    finally:
        os.close(descriptor)


def load_resume_journal(path: Path) -> dict[str, dict[str, Any]]:
    """Read the last complete checkpoint for each file; reject corrupt records."""
    records: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return records
    data = path.read_bytes()
    lines = data.splitlines(keepends=True)
    for index, raw_line in enumerate(lines):
        try:
            item = json.loads(raw_line)
        except json.JSONDecodeError:
            if index == len(lines) - 1 and not raw_line.endswith((b"\n", b"\r")):
                break
            raise ValueError(f"invalid completed resume journal row {index + 1}")
        if not isinstance(item, dict) or not isinstance(item.get("relative_path"), str):
            raise ValueError(f"invalid resume journal row {index + 1}")
        records[item["relative_path"]] = item
    return records


def expected_relative_paths(
    roots: Mapping[str, int],
    methods: Sequence[str],
    required_files: Sequence[str],
) -> dict[str, tuple[int, str, str]]:
    expected: dict[str, tuple[int, str, str]] = {}
    for root_name, seed in roots.items():
        for method in methods:
            for file_name in required_files:
                relative = f"{root_name}/runs/seed{seed}/{method}/{file_name}"
                expected[relative] = (seed, method, file_name)
    return expected


def identify_path(relative_path: str, root_name: str, seed: int) -> tuple[str | None, str]:
    parts = Path(relative_path).parts
    if len(parts) >= 4 and parts[0:2] == ("runs", f"seed{seed}"):
        method = parts[2]
        return (method if method in METHODS else None), "primary_run"
    if len(parts) == 1 and parts[0] in ROOT_SUPPORT_FILES:
        return None, "root_support"
    if len(parts) > 1 and parts[0] in SUPPORT_DIRECTORIES:
        return None, parts[0]
    return None, "unclassified"


def discover_files(root: Path, root_name: str) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    """Walk without following links and retain explicit records for unsafe entries/errors."""
    entries: list[dict[str, Any]] = []
    scan_errors: list[dict[str, str]] = []
    if not root.exists():
        scan_errors.append({"path": root_name, "error": "evidence root is missing"})
        return entries, scan_errors
    if root.is_symlink():
        scan_errors.append({"path": root_name, "error": "evidence root is a symbolic link"})
        return entries, scan_errors

    pending = [root]
    while pending:
        directory = pending.pop()
        try:
            children = sorted(os.scandir(directory), key=lambda item: item.name)
        except OSError as error:
            rel = directory.relative_to(root).as_posix()
            scan_errors.append(
                {"path": f"{root_name}/{rel}" if rel != "." else root_name, "error": str(error)}
            )
            continue
        for child in children:
            path = Path(child.path)
            relative = path.relative_to(root).as_posix()
            try:
                metadata = child.stat(follow_symlinks=False)
            except OSError as error:
                entries.append(
                    {
                        "relative_path": f"{root_name}/{relative}",
                        "kind": "stat_error",
                        "error": str(error),
                    }
                )
                continue
            if stat.S_ISDIR(metadata.st_mode):
                pending.append(path)
            elif stat.S_ISREG(metadata.st_mode):
                entries.append(
                    {
                        "relative_path": f"{root_name}/{relative}",
                        "kind": "regular_file",
                        "size_bytes": metadata.st_size,
                        "st_dev": metadata.st_dev,
                        "st_ino": metadata.st_ino,
                    }
                )
            elif stat.S_ISLNK(metadata.st_mode):
                entries.append(
                    {
                        "relative_path": f"{root_name}/{relative}",
                        "kind": "symlink",
                        "error": "symbolic link not followed or hashed",
                    }
                )
            else:
                entries.append(
                    {
                        "relative_path": f"{root_name}/{relative}",
                        "kind": "special_file",
                        "error": "non-regular filesystem object not opened or hashed",
                    }
                )
    entries.sort(key=lambda entry: entry["relative_path"])
    scan_errors.sort(key=lambda entry: entry["path"])
    return entries, scan_errors


def comparison_for(
    relative_path: str,
    sha256: str | None,
    audit_outcome: str,
    expected: bool,
    historical_references: Mapping[str, str],
    same_day_references: Mapping[str, dict[str, Any]],
) -> tuple[str, str, str | None]:
    if audit_outcome != "HASHED":
        return audit_outcome, "NOT_COMPARED", None
    if not expected:
        return "EXTRA", "NOT_COMPARED", None
    original = historical_references.get(relative_path)
    if original:
        status = "MATCH" if sha256 == original else "MISMATCH"
        return status, "NOT_COMPARED", original
    reference = same_day_references.get(relative_path)
    if reference:
        same_day_status = (
            "MATCH"
            if sha256 == reference["sha256"]
            else "MISMATCH"
        )
        return "BASELINE_UNAVAILABLE", same_day_status, reference["sha256"]
    return "BASELINE_UNAVAILABLE", "NOT_AVAILABLE", None


def write_csv(path: Path, records: Sequence[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow(record)


def atomic_write_text(path: Path, text: str) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def audit_campaign(
    evidence_roots: Mapping[str, tuple[Path, int]],
    output_dir: Path,
    *,
    methods: Sequence[str] = METHODS,
    required_files: Sequence[str] = EXPECTED_RUN_FILES,
    historical_references: Mapping[str, str] | None = None,
    same_day_references: Mapping[str, dict[str, Any]] | None = None,
    stop_after: int | None = None,
) -> dict[str, Any]:
    """Inventory and hash a campaign; output must be outside every evidence root."""
    audit_started_utc = dt.datetime.now(dt.timezone.utc).isoformat()
    historical_references = historical_references or {}
    same_day_references = same_day_references or {}
    resolved_roots = {
        name: (Path(os.path.abspath(path)), seed)
        for name, (path, seed) in evidence_roots.items()
    }
    resolved_output = Path(os.path.abspath(output_dir))
    for name, (root, _) in resolved_roots.items():
        if resolved_output == root or root in resolved_output.parents:
            raise ValueError(f"audit output must not be inside evidence root {name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    journal_path = output_dir / JOURNAL_NAME
    resume_records = load_resume_journal(journal_path)
    expected = expected_relative_paths(
        {name: seed for name, (_, seed) in resolved_roots.items()},
        methods,
        required_files,
    )
    records: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    inode_paths: dict[tuple[int, int], str] = {}
    folded_paths: dict[str, str] = {}
    scan_errors: list[dict[str, str]] = []
    blocked_prefixes: list[str] = []
    hashed_count = 0

    with journal_path.open("a", encoding="utf-8") as journal:
        for root_name, (root, seed) in sorted(resolved_roots.items()):
            discovered, root_errors = discover_files(root, root_name)
            scan_errors.extend(root_errors)
            blocked_prefixes.extend(
                error["path"] for error in root_errors
                if error["error"] != "evidence root is missing"
                and error["error"] != "evidence root is a symbolic link"
            )
            if any(error["path"] == root_name for error in root_errors):
                records.append(
                    {
                        "relative_path": root_name,
                        "seed": seed,
                        "method": "",
                        "artifact_category": "root",
                        "size_bytes": "",
                        "sha256": "",
                        "audit_outcome": "READ_ERROR",
                        "comparison_status": "READ_ERROR",
                        "same_day_source_comparison": "NOT_COMPARED",
                        "reference_sha256": "",
                        "is_expected_primary": False,
                        "is_empty": False,
                        "duplicate_of": "",
                        "error": root_errors[0]["error"],
                    }
                )

            for entry in discovered:
                relative_path = entry["relative_path"]
                seen_paths.add(relative_path)
                method, category = identify_path(
                    relative_path.removeprefix(f"{root_name}/"), root_name, seed
                )
                is_expected = relative_path in expected
                is_known_support = category in (
                    "root_support",
                    *SUPPORT_DIRECTORIES,
                )
                record: dict[str, Any] = {
                    "relative_path": relative_path,
                    "seed": seed if method is not None else "",
                    "method": method or "",
                    "artifact_category": category,
                    "size_bytes": entry.get("size_bytes", ""),
                    "sha256": "",
                    "audit_outcome": "",
                    "comparison_status": "",
                    "same_day_source_comparison": "NOT_COMPARED",
                    "reference_sha256": "",
                    "is_expected_primary": is_expected,
                    "is_empty": False,
                    "duplicate_of": "",
                    "error": entry.get("error", ""),
                }

                if entry["kind"] != "regular_file":
                    record["audit_outcome"] = "READ_ERROR"
                    record["comparison_status"] = "READ_ERROR"
                    records.append(record)
                    continue

                identity = (entry["st_dev"], entry["st_ino"])
                duplicate_of = inode_paths.get(identity)
                if duplicate_of:
                    record["duplicate_of"] = duplicate_of
                else:
                    inode_paths[identity] = relative_path
                folded = relative_path.casefold()
                if folded in folded_paths and folded_paths[folded] != relative_path:
                    record["duplicate_of"] = folded_paths[folded]
                else:
                    folded_paths[folded] = relative_path

                path = root / relative_path.removeprefix(f"{root_name}/")
                try:
                    digest, size, current_stat = sha256_stream(path)
                    record["size_bytes"] = size
                    record["sha256"] = digest
                    record["is_empty"] = size == 0
                    record["audit_outcome"] = "HASHED"
                    old = resume_records.get(relative_path)
                    record["resume_revalidated"] = bool(
                        old
                        and old.get("sha256") == digest
                        and old.get("size_bytes") == size
                        and old.get("st_dev") == current_stat.st_dev
                        and old.get("st_ino") == current_stat.st_ino
                        and old.get("st_mtime_ns") == current_stat.st_mtime_ns
                    )
                    journal_row = {
                        "relative_path": relative_path,
                        "size_bytes": size,
                        "sha256": digest,
                        "st_dev": current_stat.st_dev,
                        "st_ino": current_stat.st_ino,
                        "st_mtime_ns": current_stat.st_mtime_ns,
                    }
                    journal.write(json.dumps(journal_row, sort_keys=True) + "\n")
                    journal.flush()
                    os.fsync(journal.fileno())
                    hashed_count += 1
                    if stop_after is not None and hashed_count >= stop_after:
                        raise AuditInterrupted("intentional test interruption")
                except OSError as error:
                    record["audit_outcome"] = "READ_ERROR"
                    record["error"] = str(error)

                comparison, source_comparison, reference_hash = comparison_for(
                    relative_path,
                    record["sha256"] or None,
                    record["audit_outcome"],
                    is_expected or is_known_support,
                    historical_references,
                    same_day_references,
                )
                record["comparison_status"] = comparison
                record["same_day_source_comparison"] = source_comparison
                record["reference_sha256"] = reference_hash or ""
                records.append(record)

        for relative_path, (seed, method, _) in sorted(expected.items()):
            if relative_path in seen_paths:
                continue
            blocked = any(
                relative_path == prefix or relative_path.startswith(prefix + "/")
                for prefix in blocked_prefixes
            )
            missing_status = "READ_ERROR" if blocked else "MISSING"
            records.append(
                {
                    "relative_path": relative_path,
                    "seed": seed,
                    "method": method,
                    "artifact_category": "primary_run",
                    "size_bytes": "",
                    "sha256": "",
                    "audit_outcome": missing_status,
                    "comparison_status": missing_status,
                    "same_day_source_comparison": "NOT_COMPARED",
                    "reference_sha256": "",
                    "is_expected_primary": True,
                    "is_empty": False,
                    "duplicate_of": "",
                    "error": "expected file is absent" if not blocked else "parent directory unreadable",
                }
            )

    records.sort(key=lambda record: record["relative_path"])
    counts = {
        status: sum(record["comparison_status"] == status for record in records)
        for status in ("MATCH", "MISMATCH", "BASELINE_UNAVAILABLE", "MISSING", "READ_ERROR", "EXTRA")
    }
    outcome_counts = {
        status: sum(record["audit_outcome"] == status for record in records)
        for status in ("HASHED", "MISSING", "READ_ERROR")
    }
    primary_records = [record for record in records if record["is_expected_primary"]]
    support_records = [record for record in records if not record["is_expected_primary"]]
    successful_primary = sum(record["audit_outcome"] == "HASHED" for record in primary_records)
    additional_hashed = sum(record["audit_outcome"] == "HASHED" for record in support_records)
    source_comparison_counts = {
        status: sum(
            record["same_day_source_comparison"] == status for record in records
        )
        for status in ("MATCH", "MISMATCH", "NOT_AVAILABLE", "NOT_COMPARED")
    }
    missing_roots = sum(
        not root.exists() or root.is_symlink() for root, _ in resolved_roots.values()
    )
    duplicate_records = [record for record in records if record["duplicate_of"]]
    summary: dict[str, Any] = {
        "audit_started_utc": audit_started_utc,
        "evidence_roots": sorted(resolved_roots),
        "root_count": len(resolved_roots),
        "expected_seeds": sorted(seed for _, seed in resolved_roots.values()),
        "methods": list(methods),
        "expected_primary_files": len(expected),
        "files_discovered": len(discovered_paths := [
            record for record in records
            if record["audit_outcome"] in ("HASHED", "READ_ERROR", "EXTRA")
            and record["artifact_category"] != "root"
        ]),
        "primary_files_hashed": successful_primary,
        "additional_files_hashed": additional_hashed,
        "files_hashed": outcome_counts["HASHED"],
        "files_attempted": len(discovered_paths),
        "comparison_status_counts": counts,
        "audit_outcome_counts": outcome_counts,
        "same_day_source_comparison_counts": source_comparison_counts,
        "same_day_drive_reference_count": len(same_day_references),
        "trusted_execution_time_reference_count": len(historical_references),
        "empty_files": [
            record["relative_path"] for record in records
            if record["is_empty"] and record["audit_outcome"] == "HASHED"
        ],
        "duplicate_entries": duplicate_records,
        "scan_errors": scan_errors,
        "missing_roots": missing_roots,
        "decision": "",
    }
    if (
        counts["MISMATCH"]
        or counts["EXTRA"]
        or duplicate_records
        or scan_errors
        or missing_roots
        or counts["MISSING"]
        or counts["READ_ERROR"]
        or successful_primary != len(expected)
        or additional_hashed + successful_primary != outcome_counts["HASHED"]
    ):
        summary["decision"] = "AUDIT INCOMPLETE" if not counts["MISMATCH"] else "INTEGRITY DISCREPANCY"
    elif historical_references and counts["BASELINE_UNAVAILABLE"] == 0:
        summary["decision"] = "INTEGRITY VERIFIED"
    else:
        summary["decision"] = "CURRENT-STATE BASELINE COMPLETE"

    summary["audit_finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    summary["scan_error_count"] = len(scan_errors)
    summary["empty_file_count"] = len(summary["empty_files"])
    summary["additional_artifact_categories"] = {
        category: sum(
            record["artifact_category"] == category
            and record["audit_outcome"] == "HASHED"
            for record in support_records
        )
        for category in ("root_support", *sorted(SUPPORT_DIRECTORIES), "unclassified")
    }

    atomic_write_text(
        output_dir / "sha256_current.json",
        json.dumps({"summary": summary, "files": records}, indent=2, sort_keys=True) + "\n",
    )
    write_csv(output_dir / "sha256_current.csv", records)
    write_csv(output_dir / "sha256_comparison.csv", records)
    atomic_write_text(output_dir / "sha256_summary.json", json.dumps(summary, indent=2) + "\n")
    log_lines = [
        f"Audit started UTC: {summary['audit_started_utc']}",
        f"Audit finished UTC: {summary['audit_finished_utc']}",
        f"Formal roots: {', '.join(summary['evidence_roots'])}",
        f"Files discovered: {summary['files_discovered']}",
        f"Files hashed: {summary['files_hashed']}",
        f"Comparison counts: {json.dumps(counts, sort_keys=True)}",
        f"Decision: {summary['decision']}",
    ]
    atomic_write_text(output_dir / "audit_execution.log", "\n".join(log_lines) + "\n")
    return summary


def baseline_provenance_text(summary: Mapping[str, Any], repo_revision: str, script_sha256: str) -> str:
    return f"""# D8-I1 SHA256 baseline provenance

- Audit start (UTC): {summary['audit_started_utc']}
- Audit completion (UTC): {summary['audit_finished_utc']}
- Audited repository revision before audit: `{repo_revision}`
- Audit script SHA256: `{script_sha256}`
- Scope: five named formal evidence roots, seeds 42–46, methods Gossip, Structured, DC-SoC, AHBN, and Q-AHBN2.
- Current-state outputs: `output/d8_integrity/sha256_current.csv`, `sha256_current.json`, `sha256_comparison.csv`, and `sha256_summary.json`.
- Current regular files discovered / hashed: {summary['files_discovered']} / {summary['files_hashed']}.
- Trusted experiment-time SHA256 references: {summary['trusted_execution_time_reference_count']}.

## Historical checksum search

The requested GitHub D8 inventory, protocol decision, and preliminary reconciliation records were read before the audit. Repository code search and local evidence-name searches found no complete contemporaneous per-file checksum register for this 25-run campaign. The three hashes noted in the dated D8 inventory are same-day raw Drive-byte fingerprints, not authenticated checksums created by the experiment at execution time; they are therefore reported separately and do not count as `MATCH`.

For those three documented Drive fingerprints, the audit records equality or difference from the current local bytes as a separate same-day source comparison. This comparison does not establish that bytes have remained unchanged since execution.

## Results

- Decision: **{summary['decision']}**
- Comparison statuses: `{json.dumps(summary['comparison_status_counts'], sort_keys=True)}`
- Same-day Drive fingerprint comparisons: `{json.dumps(summary['same_day_source_comparison_counts'], sort_keys=True)}`
- Additional artifacts hashed beyond the 600 direct run files: {summary['additional_files_hashed']}
- Empty regular files (listed in the JSON inventory): {summary['empty_file_count']}
- Duplicate entries: {len(summary['duplicate_entries'])}
- Scan errors: {summary['scan_error_count']}

This current-state baseline supports future byte comparisons. It cannot retrospectively prove that all experiment evidence has been unchanged since the runs. No archived evidence was modified.
"""


def get_git_revision() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-dir", type=Path, default=EVIDENCE_ROOT)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_ROOT)
    args = parser.parse_args(argv)

    evidence_roots = {
        name: (args.evidence_dir / name, seed)
        for name, seed in FORMAL_ROOT_SEEDS.items()
    }
    repo_revision = get_git_revision()
    script_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    summary = audit_campaign(
        evidence_roots,
        args.output_dir,
        same_day_references=SAME_DAY_DRIVE_FINGERPRINTS,
    )
    atomic_write_text(
        args.output_dir / "baseline_provenance.md",
        baseline_provenance_text(summary, repo_revision, script_sha256),
    )
    print(json.dumps(summary, indent=2))
    return 0 if summary["decision"] in (
        "INTEGRITY VERIFIED",
        "CURRENT-STATE BASELINE COMPLETE",
    ) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AuditInterrupted, OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"D8-I1 SHA256 audit failed: {error}", file=sys.stderr)
        sys.exit(1)
