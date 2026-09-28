"""Guarded runner for frozen formal ControlSim Exp10-Q Failure."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from datetime import datetime
from pathlib import Path

from qahbn2.formal_exp10q import (
    CONDITIONS,
    EXPECTED_RUNS,
    METHODS,
    PRIMARY_METRICS,
    Q_METRICS,
    SEEDS,
    run_exp10q_cell,
    validate_matrix,
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
        "--output-dir",
        type=Path,
        default=None,
        help="Optional run directory. Must remain under the gitignored output/ tree.",
    )
    args = parser.parse_args()

    validate_matrix(CONDITIONS, METHODS, SEEDS)
    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    output_root = Path("output")
    output_dir = args.output_dir or (
        output_root / "evidence" / f"q-ahbn-{timestamp}-exp10q-formal"
    )
    try:
        output_dir.resolve().relative_to(output_root.resolve())
    except ValueError as exc:
        raise ValueError("Exp10-Q output directory must be under output/") from exc
    if output_dir.exists():
        raise FileExistsError(
            f"refusing to overwrite existing run directory: {output_dir}"
        )
    output_dir.mkdir(parents=True)

    qahbn2_commit = _git_head()
    rows = []
    traces = []

    for condition, method, seed in EXPECTED_RUNS:
        result = run_exp10q_cell(
            condition=condition, method=method, seed=seed, trace_decisions=True
        )
        missing = [
            metric for metric in PRIMARY_METRICS
            if metric not in result
        ]
        if method == "qahbn2":
            missing.extend(metric for metric in Q_METRICS if metric not in result)
            traces.append({
                "condition": condition,
                "seed": seed,
                "decision_trace": result.pop("decision_trace", []),
            })
        if missing:
            raise RuntimeError(
                f"Exp10-Q {condition}/{method}/seed={seed} missing metrics: {missing}"
            )
        rows.append(result)

    csv_fields = [
        "condition", "method", "seed",
        *PRIMARY_METRICS,
        *Q_METRICS,
        "failed_peer", "failure_before_message",
    ]
    output_csv = output_dir / "exp10q_formal.csv"
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    (output_dir / "decision_trace.json").write_text(
        json.dumps(traces, indent=2) + "\n", encoding="utf-8"
    )

    manifest = {
        "environment": "ControlSim",
        "experiment": "Exp10-Q Failure",
        "event": "formal",
        "timestamp": timestamp,
        "run_directory": str(output_dir),
        "status": "completed",
        "scientific_classification": "formal raw evidence pending validity audit",
        "qahbn2_commit": qahbn2_commit,
        "canonical_ahbn_commit": CANONICAL_AHBN_COMMIT,
        "conditions": list(CONDITIONS),
        "methods": list(METHODS),
        "seeds": list(SEEDS),
        "expected_runs": len(EXPECTED_RUNS),
        "completed_runs": len(rows),
        "frozen_gamma": 0.70,
        "failure_before_message": 501,
        "exclusions": [],
        "reruns": [],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "RUN.md").write_text(
        "# Exp10-Q Formal Failure\n\n"
        f"- Timestamp: {timestamp}\n"
        "- Environment: ControlSim\n"
        "- Event: formal\n"
        f"- Q-AHBN2 commit: {qahbn2_commit}\n"
        f"- Canonical AHBN commit: {CANONICAL_AHBN_COMMIT}\n"
        f"- Expected/completed runs: {len(EXPECTED_RUNS)}/{len(rows)}\n"
        "- Matrix: control + one seeded non-source peer failure; AHBN vs Q-AHBN2; seeds 42-46\n"
        "- Failure onset: after message 500, before message 501; no recovery\n"
        "- Scientific status: raw formal evidence; interpretation prohibited until validity/completeness audit\n",
        encoding="utf-8",
    )
    print(output_dir)


if __name__ == "__main__":
    main()
