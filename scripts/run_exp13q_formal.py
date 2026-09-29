"""Guarded runner for frozen formal ControlSim Exp13-Q reference benchmark."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from datetime import datetime
from pathlib import Path

from qahbn2.formal_exp13q import (
    CHURN_LEVEL,
    CYCLE_ONSETS,
    DCSOC_EPS,
    DCSOC_MIN_SAMPLES,
    EXPECTED_RUNS,
    METHODS,
    PRIMARY_METRICS,
    Q_METRICS,
    REJOIN_BEFORE_MESSAGES,
    SEEDS,
    run_exp13q_cell,
    validate_matrix,
)
from qahbn2.learning_validation import MESSAGE_SOURCE, NUM_MESSAGES, NUM_NODES

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

    validate_matrix(METHODS, SEEDS)

    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    output_root = Path("output")
    output_dir = args.output_dir or (
        output_root / "evidence" / f"q-ahbn-{timestamp}-exp13q-formal"
    )
    try:
        output_dir.resolve().relative_to(output_root.resolve())
    except ValueError as exc:
        raise ValueError("Exp13-Q output directory must be under output/") from exc
    if output_dir.exists():
        raise FileExistsError(
            f"refusing to overwrite existing run directory: {output_dir}"
        )
    output_dir.mkdir(parents=True)

    qahbn2_commit = _git_head()
    rows = []
    traces = []
    schedule_by_seed = {}

    for method, seed in EXPECTED_RUNS:
        result = run_exp13q_cell(
            method=method,
            seed=seed,
            trace_decisions=True,
        )
        missing = [metric for metric in PRIMARY_METRICS if metric not in result]
        if method == "qahbn2":
            missing.extend(metric for metric in Q_METRICS if metric not in result)
            traces.append(
                {
                    "churn_level": CHURN_LEVEL,
                    "seed": seed,
                    "decision_trace": result.pop("decision_trace", []),
                }
            )
        if missing:
            raise RuntimeError(
                f"Exp13-Q {method}/seed={seed} missing metrics: {missing}"
            )

        schedule = result.get("churn_schedule")
        previous = schedule_by_seed.setdefault(seed, schedule)
        if previous != schedule:
            raise RuntimeError(
                f"Exp13-Q common churn schedule mismatch for seed={seed}"
            )
        rows.append(result)

    csv_fields = [
        "churn_level",
        "method",
        "seed",
        *PRIMARY_METRICS,
        *Q_METRICS,
        "churn_target_count",
        "churn_schedule",
        "churn_events",
        "dcsoc_eps",
        "dcsoc_min_samples",
    ]
    output_csv = output_dir / "exp13q_formal.csv"
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    (output_dir / "decision_trace.json").write_text(
        json.dumps(traces, indent=2) + "\n", encoding="utf-8"
    )

    manifest = {
        "environment": "ControlSim",
        "experiment": "Exp13-Q Reference Benchmark",
        "event": "formal",
        "timestamp": timestamp,
        "run_directory": str(output_dir),
        "status": "completed",
        "scientific_classification": "formal raw evidence pending validity audit",
        "qahbn2_commit": qahbn2_commit,
        "canonical_ahbn_commit": CANONICAL_AHBN_COMMIT,
        "topology": f"BA({NUM_NODES},m=3)",
        "message_source": MESSAGE_SOURCE,
        "messages_per_run": NUM_MESSAGES,
        "churn_level": CHURN_LEVEL,
        "cycle_onsets_before_message": list(CYCLE_ONSETS),
        "rejoin_before_message": list(REJOIN_BEFORE_MESSAGES),
        "methods": list(METHODS),
        "seeds": list(SEEDS),
        "expected_runs": len(EXPECTED_RUNS),
        "completed_runs": len(rows),
        "dcsoc_eps": DCSOC_EPS,
        "dcsoc_min_samples": DCSOC_MIN_SAMPLES,
        "frozen_gamma": 0.70,
        "exclusions": [],
        "reruns": [],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    (output_dir / "RUN.md").write_text(
        "# Exp13-Q Formal Reference Benchmark\n\n"
        f"- Timestamp: {timestamp}\n"
        "- Environment: ControlSim\n"
        "- Event: formal\n"
        f"- Q-AHBN2 commit: {qahbn2_commit}\n"
        f"- Canonical AHBN commit: {CANONICAL_AHBN_COMMIT}\n"
        f"- Expected/completed runs: {len(EXPECTED_RUNS)}/{len(rows)}\n"
        "- Matrix: Gossip, Structured, DC-SoC, AHBN, Q-AHBN2; seeds 42-46\n"
        "- Scenario: churn=0.40; BA(100,m=3); source 0; 1,000 sequential "
        "queue-to-exhaustion messages per run\n"
        "- Churn cycles: leave before 201/401/601/801; "
        "rejoin before 251/451/651/851\n"
        "- Scientific status: raw formal reference-benchmark evidence; "
        "interpretation prohibited until validity/completeness audit\n",
        encoding="utf-8",
    )

    print(output_dir)


if __name__ == "__main__":
    main()
