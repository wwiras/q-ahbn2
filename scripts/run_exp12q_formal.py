"""Guarded runner for frozen formal ControlSim Exp12-Q Heterogeneity."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from datetime import datetime
from pathlib import Path

from qahbn2.formal_exp12q import (
    EXPECTED_RUNS, METHODS, PRIMARY_METRICS, PROFILE_FRACTIONS, Q_METRICS,
    RESOURCE_CLASSES, RESOURCE_PROFILES, SEEDS, run_exp12q_cell, validate_matrix,
)

CANONICAL_AHBN_COMMIT = "936a79480bc1252c79b6ee01f65c88c740af2844"


def _git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.STDOUT
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNAVAILABLE"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir", type=Path, default=None,
        help="Optional run directory. Must remain under the gitignored output/ tree.",
    )
    args = parser.parse_args()

    validate_matrix(RESOURCE_PROFILES, METHODS, SEEDS)
    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    output_root = Path("output")
    output_dir = args.output_dir or (
        output_root / "evidence" / f"q-ahbn-{timestamp}-exp12q-formal"
    )
    try:
        output_dir.resolve().relative_to(output_root.resolve())
    except ValueError as exc:
        raise ValueError("Exp12-Q output directory must be under output/") from exc
    if output_dir.exists():
        raise FileExistsError(
            f"refusing to overwrite existing run directory: {output_dir}"
        )
    output_dir.mkdir(parents=True)

    qahbn2_commit = _git_head()
    rows, traces = [], []
    paired_assignments = {}

    for resource_profile, method, seed in EXPECTED_RUNS:
        result = run_exp12q_cell(
            resource_profile=resource_profile, method=method, seed=seed,
            trace_decisions=True,
        )
        missing = [metric for metric in PRIMARY_METRICS if metric not in result]
        if method == "qahbn2":
            missing.extend(metric for metric in Q_METRICS if metric not in result)
            traces.append({
                "resource_profile": resource_profile,
                "seed": seed,
                "decision_trace": result.pop("decision_trace", []),
            })
        if missing:
            raise RuntimeError(
                f"Exp12-Q {resource_profile}/{method}/seed={seed} "
                f"missing metrics: {missing}"
            )

        pair_key = (resource_profile, seed)
        assignment_sha = result["resource_assignment_sha256"]
        previous = paired_assignments.setdefault(pair_key, assignment_sha)
        if previous != assignment_sha:
            raise RuntimeError(
                f"Exp12-Q paired resource assignment mismatch for "
                f"{resource_profile}/seed={seed}"
            )
        rows.append(result)

    csv_fields = [
        "resource_profile", "method", "seed",
        *PRIMARY_METRICS, *Q_METRICS,
        "resource_assignment_sha256", "resource_class_counts", "resource_assignment",
    ]
    output_csv = output_dir / "exp12q_formal.csv"
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    (output_dir / "decision_trace.json").write_text(
        json.dumps(traces, indent=2) + "\n", encoding="utf-8"
    )
    manifest = {
        "environment": "ControlSim",
        "experiment": "Exp12-Q Heterogeneity",
        "event": "formal",
        "timestamp": timestamp,
        "run_directory": str(output_dir),
        "status": "completed",
        "scientific_classification": "formal raw evidence pending validity audit",
        "qahbn2_commit": qahbn2_commit,
        "canonical_ahbn_commit": CANONICAL_AHBN_COMMIT,
        "topology": "BA(100,m=3)",
        "message_source": 0,
        "messages_per_run": 1000,
        "resource_profiles": list(RESOURCE_PROFILES),
        "resource_classes": RESOURCE_CLASSES,
        "profile_fractions": PROFILE_FRACTIONS,
        "methods": list(METHODS),
        "seeds": list(SEEDS),
        "expected_runs": len(EXPECTED_RUNS),
        "completed_runs": len(rows),
        "frozen_gamma": 0.70,
        "failure_enabled": False,
        "churn_enabled": False,
        "exclusions": [],
        "reruns": [],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "RUN.md").write_text(
        "# Exp12-Q Formal Heterogeneity\n\n"
        f"- Timestamp: {timestamp}\n"
        "- Environment: ControlSim\n"
        "- Event: formal\n"
        f"- Q-AHBN2 commit: {qahbn2_commit}\n"
        f"- Canonical AHBN commit: {CANONICAL_AHBN_COMMIT}\n"
        f"- Expected/completed runs: {len(EXPECTED_RUNS)}/{len(rows)}\n"
        "- Matrix: balanced/moderate_heterogeneity/weak_heavy; "
        "AHBN vs Q-AHBN2; seeds 42-46\n"
        "- Topology/workload: BA(100,m=3), source 0, 1,000 sequential "
        "queue-to-exhaustion messages per run\n"
        "- Failure/churn: disabled\n"
        "- Scientific status: raw formal evidence; interpretation prohibited "
        "until validity/completeness audit\n",
        encoding="utf-8",
    )
    print(output_dir)


if __name__ == "__main__":
    main()
