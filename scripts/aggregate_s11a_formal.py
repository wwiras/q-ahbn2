"""Deterministic S11-A aggregation script for primary RO4 evaluation.

Aggregates formal ControlSim evidence across:
- Exp10-Q (Failure)
- Exp11-Q (Churn)
- Exp12-Q (Heterogeneity)

Strictly conforms to docs/04_STATISTICAL_CONTRACT.md.
Exp13-Q is explicitly excluded from S11-A (reserved for S11-B).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

STUDENT_T_95_DF4: float = 2.7764451051977987
FROZEN_SEEDS: Tuple[int, ...] = (42, 43, 44, 45, 46)
METHODS: Tuple[str, ...] = ("ahbn", "qahbn2")

PRIMARY_METRICS: Tuple[str, ...] = (
    "delivery_ratio",
    "propagation_delay",
    "duplicates",
    "total_forwards",
)

LEARNING_NUMERIC_METRICS: Tuple[str, ...] = (
    "mean_reward",
    "cumulative_reward",
    "q_updates",
    "state_action_coverage",
    "intervention_count",
    "keep_count",
)

EXPERIMENT_SPECS: Dict[str, Dict[str, Any]] = {
    "exp10q": {
        "experiment_id": "exp10q",
        "name": "Exp10-Q Failure",
        "condition_key": "condition",
        "conditions": ("control", "failure"),
        "expected_runs": 20,
        "default_csv": Path(
            "output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal/exp10q_formal.csv"
        ),
    },
    "exp11q": {
        "experiment_id": "exp11q",
        "name": "Exp11-Q Churn",
        "condition_key": "churn_level",
        "conditions": ("0.0", "0.2", "0.4"),
        "expected_runs": 30,
        "default_csv": Path(
            "output/evidence/q-ahbn-28092026203251-exp11q-formal/exp11q_formal.csv"
        ),
    },
    "exp12q": {
        "experiment_id": "exp12q",
        "name": "Exp12-Q Heterogeneity",
        "condition_key": "resource_profile",
        "conditions": ("balanced", "moderate_heterogeneity", "weak_heavy"),
        "expected_runs": 30,
        "default_csv": Path(
            "output/evidence/Exp12-Q/q-ahbn-28092026215008-exp12q-formal/exp12q_formal.csv"
        ),
    },
}

CANONICAL_AHBN_COMMIT = "936a79480bc1252c79b6ee01f65c88c740af2844"


def _git_head() -> str:
    """Retrieve current Git HEAD SHA."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.STDOUT
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNAVAILABLE"


def compute_file_sha256(path: Path | str) -> str:
    """Compute SHA-256 hash of a file deterministically."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def load_csv_rows(csv_path: Path | str) -> List[Dict[str, str]]:
    """Load rows from a CSV file in read-only mode without mutating the file."""
    path = Path(csv_path)
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def compute_metric_summary(
    values_by_seed: Dict[int, float],
    seeds: Sequence[int] = FROZEN_SEEDS,
) -> Dict[str, Any]:
    """Compute n, mean, sample SD (ddof=1), and 95% Student-t CI.

    Formula from docs/04_STATISTICAL_CONTRACT.md:
      mean +/- t_(0.975, n-1) * s / sqrt(n)
    For n=5, df=4:
      t_(0.975, 4) = 2.7764451051977987
    """
    if len(seeds) != 5:
        raise ValueError(f"S11-A requires strictly 5 seeds, got {len(seeds)}")
    if set(values_by_seed.keys()) != set(seeds):
        missing = set(seeds) - set(values_by_seed.keys())
        extra = set(values_by_seed.keys()) - set(seeds)
        raise ValueError(
            f"Seed mismatch: missing={sorted(missing)}, extra={sorted(extra)}"
        )

    ordered_values: List[float] = []
    for s in seeds:
        val = float(values_by_seed[s])
        if not math.isfinite(val):
            raise ValueError(f"Non-finite value for seed {s}: {val}")
        ordered_values.append(val)

    n = len(ordered_values)
    mean_val = statistics.mean(ordered_values)
    sd_val = statistics.stdev(ordered_values)  # ddof=1 sample standard deviation
    margin = STUDENT_T_95_DF4 * sd_val / math.sqrt(n)

    seed_values_dict = {str(s): values_by_seed[s] for s in seeds}

    return {
        "n": n,
        "mean": mean_val,
        "sd": sd_val,
        "ci95_low": mean_val - margin,
        "ci95_high": mean_val + margin,
        "seed_values": seed_values_dict,
    }


def compute_paired_effects(
    qahbn2_by_seed: Dict[int, float],
    ahbn_by_seed: Dict[int, float],
    metric: str,
    mean_ahbn: float,
    mean_q: float,
    seeds: Sequence[int] = FROZEN_SEEDS,
) -> Dict[str, Any]:
    """Compute paired differences Delta_i = QAHBN2_i - AHBN_i across same seeds.

    Formula from docs/04_STATISTICAL_CONTRACT.md:
      Delta_i = QAHBN2_i - AHBN_i
      mean(Delta), sample SD, two-sided 95% Student-t CI.
      relative_change_percent = 100 * (mean_QAHBN2 - mean_AHBN) / mean_AHBN
      percentage_point_difference = mean(Delta) * 100 (for delivery_ratio)
    """
    if len(seeds) != 5:
        raise ValueError(f"S11-A requires strictly 5 seeds, got {len(seeds)}")
    if set(qahbn2_by_seed.keys()) != set(seeds) or set(ahbn_by_seed.keys()) != set(seeds):
        raise ValueError("Seed mismatch between AHBN and Q-AHBN2 pairing keys")

    diffs: List[float] = []
    seed_diffs_dict: Dict[str, float] = {}
    for s in seeds:
        q_val = float(qahbn2_by_seed[s])
        a_val = float(ahbn_by_seed[s])
        if not math.isfinite(q_val) or not math.isfinite(a_val):
            raise ValueError(f"Non-finite paired value at seed {s}: q={q_val}, a={a_val}")
        delta = q_val - a_val
        diffs.append(delta)
        seed_diffs_dict[str(s)] = delta

    n = len(diffs)
    mean_diff = statistics.mean(diffs)
    sd_diff = statistics.stdev(diffs)
    margin = STUDENT_T_95_DF4 * sd_diff / math.sqrt(n)

    result: Dict[str, Any] = {
        "n": n,
        "mean": mean_diff,
        "sd": sd_diff,
        "ci95_low": mean_diff - margin,
        "ci95_high": mean_diff + margin,
        "seed_differences_Q_minus_A": seed_diffs_dict,
    }

    if mean_ahbn != 0.0:
        result["relative_change_percent"] = 100.0 * (mean_q - mean_ahbn) / mean_ahbn
    else:
        result["relative_change_percent"] = None

    if metric == "delivery_ratio":
        result["percentage_point_difference"] = mean_diff * 100.0

    return result


def compute_action_distribution(
    q_rows_by_seed: Dict[int, Dict[str, str]],
    seeds: Sequence[int] = FROZEN_SEEDS,
) -> Dict[str, Any]:
    """Aggregate action distribution counts and proportions across seeds."""
    per_seed: Dict[str, Dict[str, int]] = {}
    aggregate_counts: Dict[str, int] = {}
    total_actions = 0

    for s in seeds:
        row = q_rows_by_seed[s]
        raw_dist = row.get("action_distribution", "")
        if not raw_dist:
            raise ValueError(f"Missing action_distribution for seed {s}")
        dist = json.loads(raw_dist)
        per_seed[str(s)] = dist
        for action, count in dist.items():
            aggregate_counts[action] = aggregate_counts.get(action, 0) + int(count)
            total_actions += int(count)

    if total_actions > 0:
        aggregate_proportions = {
            action: count / total_actions for action, count in aggregate_counts.items()
        }
    else:
        aggregate_proportions = {action: 0.0 for action in aggregate_counts}

    return {
        "aggregate_counts": aggregate_counts,
        "aggregate_proportions": aggregate_proportions,
        "per_seed": per_seed,
    }


def compute_qahbn2_learning(
    q_rows_by_seed: Dict[int, Dict[str, str]],
    seeds: Sequence[int] = FROZEN_SEEDS,
) -> Dict[str, Any]:
    """Compute descriptive learning and adaptation summaries for Q-AHBN2."""
    learning_summary: Dict[str, Any] = {}

    for metric in LEARNING_NUMERIC_METRICS:
        vals: Dict[int, float] = {}
        for s in seeds:
            row = q_rows_by_seed[s]
            raw_val = row.get(metric, "")
            if raw_val is None or raw_val == "":
                raise ValueError(f"Missing Q-learning metric '{metric}' for seed {s}")
            vals[s] = float(raw_val)
        learning_summary[metric] = compute_metric_summary(vals, seeds=seeds)

    learning_summary["action_distribution"] = compute_action_distribution(
        q_rows_by_seed, seeds=seeds
    )
    return learning_summary


def validate_experiment_rows(
    rows: List[Dict[str, str]],
    condition_key: str,
    conditions: Tuple[str, ...],
    seeds: Tuple[int, ...] = FROZEN_SEEDS,
    expected_runs: Optional[int] = None,
) -> None:
    """Validate completeness, uniqueness, and metric integrity of experiment rows."""
    expected_total = len(conditions) * len(METHODS) * len(seeds)
    if expected_runs is not None and expected_total != expected_runs:
        raise ValueError(
            f"Configured expected_runs ({expected_runs}) does not match matrix size ({expected_total})"
        )

    if len(rows) != expected_total:
        raise ValueError(
            f"Expected {expected_total} rows, but received {len(rows)} rows."
        )

    seen_cells = set()
    for idx, row in enumerate(rows):
        if condition_key not in row:
            raise KeyError(f"Row {idx} missing condition key '{condition_key}'")
        cond_val = str(row[condition_key])
        if cond_val not in conditions:
            raise ValueError(
                f"Row {idx} has unexpected condition '{cond_val}', expected one of {conditions}"
            )

        method = row.get("method")
        if method not in METHODS:
            raise ValueError(
                f"Row {idx} has unexpected method '{method}', expected one of {METHODS}"
            )

        try:
            seed = int(row.get("seed", -1))
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Row {idx} has invalid seed: {row.get('seed')}") from exc

        if seed not in seeds:
            raise ValueError(
                f"Row {idx} has unexpected seed {seed}, expected one of {seeds}"
            )

        cell_key = (cond_val, method, seed)
        if cell_key in seen_cells:
            raise ValueError(f"Duplicate cell found: {cell_key}")
        seen_cells.add(cell_key)

        for pm in PRIMARY_METRICS:
            if pm not in row or row[pm] == "":
                raise ValueError(f"Row {idx} missing primary metric '{pm}'")
            val = float(row[pm])
            if not math.isfinite(val):
                raise ValueError(f"Row {idx} has non-finite '{pm}': {val}")
            if pm == "delivery_ratio" and not (0.0 <= val <= 1.0):
                raise ValueError(f"delivery_ratio out of [0, 1] at row {idx}: {val}")
            if pm == "propagation_delay" and val <= 0.0:
                raise ValueError(f"propagation_delay <= 0 at row {idx}: {val}")
            if pm in ("duplicates", "total_forwards") and val < 0.0:
                raise ValueError(f"{pm} < 0 at row {idx}: {val}")

        if method == "qahbn2":
            for lm in LEARNING_NUMERIC_METRICS:
                if lm not in row or row[lm] == "":
                    raise ValueError(f"Q-AHBN2 row {idx} missing learning metric '{lm}'")
                lval = float(row[lm])
                if not math.isfinite(lval):
                    raise ValueError(f"Non-finite learning metric '{lm}' at row {idx}: {lval}")
            if "action_distribution" not in row or not row["action_distribution"]:
                raise ValueError(f"Q-AHBN2 row {idx} missing 'action_distribution'")

    for cond in conditions:
        for method in METHODS:
            for s in seeds:
                if (cond, method, s) not in seen_cells:
                    raise ValueError(f"Missing required cell: {(cond, method, s)}")


def aggregate_experiment_data(
    rows: List[Dict[str, str]],
    condition_key: str,
    conditions: Tuple[str, ...],
    seeds: Tuple[int, ...] = FROZEN_SEEDS,
    expected_runs: Optional[int] = None,
) -> Dict[str, Any]:
    """Compute full statistical aggregation for one experiment."""
    validate_experiment_rows(
        rows,
        condition_key=condition_key,
        conditions=conditions,
        seeds=seeds,
        expected_runs=expected_runs,
    )

    cell_summaries: Dict[str, Dict[str, Dict[str, Any]]] = {}
    paired_effects: Dict[str, Dict[str, Any]] = {}
    qahbn2_learning: Dict[str, Any] = {}

    rows_by_condition: Dict[str, List[Dict[str, str]]] = {c: [] for c in conditions}
    for row in rows:
        cond_val = str(row[condition_key])
        rows_by_condition[cond_val].append(row)

    for cond in conditions:
        cond_rows = rows_by_condition[cond]
        cell_summaries[cond] = {}
        paired_effects[cond] = {}

        method_rows: Dict[str, Dict[int, Dict[str, str]]] = {
            m: {} for m in METHODS
        }
        for r in cond_rows:
            m = r["method"]
            s = int(r["seed"])
            method_rows[m][s] = r

        for method in METHODS:
            cell_summaries[cond][method] = {}
            for metric in PRIMARY_METRICS:
                vals_by_seed = {
                    s: float(method_rows[method][s][metric]) for s in seeds
                }
                cell_summaries[cond][method][metric] = compute_metric_summary(
                    vals_by_seed, seeds=seeds
                )

        for metric in PRIMARY_METRICS:
            q_vals = {s: float(method_rows["qahbn2"][s][metric]) for s in seeds}
            a_vals = {s: float(method_rows["ahbn"][s][metric]) for s in seeds}
            mean_ahbn = cell_summaries[cond]["ahbn"][metric]["mean"]
            mean_q = cell_summaries[cond]["qahbn2"][metric]["mean"]
            paired_effects[cond][metric] = compute_paired_effects(
                qahbn2_by_seed=q_vals,
                ahbn_by_seed=a_vals,
                metric=metric,
                mean_ahbn=mean_ahbn,
                mean_q=mean_q,
                seeds=seeds,
            )

        qahbn2_learning[cond] = compute_qahbn2_learning(
            method_rows["qahbn2"], seeds=seeds
        )

    return {
        "cell_summaries": cell_summaries,
        "paired_effects": paired_effects,
        "qahbn2_learning": qahbn2_learning,
    }


def aggregate_experiment_from_csv(
    csv_path: Path | str,
    experiment_id: str,
) -> Dict[str, Any]:
    """Aggregate a single formal experiment CSV by experiment ID."""
    if experiment_id not in EXPERIMENT_SPECS:
        raise ValueError(
            f"Unknown experiment_id '{experiment_id}', expected one of {list(EXPERIMENT_SPECS.keys())}"
        )
    spec = EXPERIMENT_SPECS[experiment_id]
    rows = load_csv_rows(csv_path)
    result = aggregate_experiment_data(
        rows=rows,
        condition_key=spec["condition_key"],
        conditions=spec["conditions"],
        seeds=FROZEN_SEEDS,
        expected_runs=spec["expected_runs"],
    )
    return {
        "experiment_id": experiment_id,
        "name": spec["name"],
        "condition_key": spec["condition_key"],
        "conditions": list(spec["conditions"]),
        "source_csv": str(csv_path),
        "source_sha256": compute_file_sha256(csv_path),
        "total_rows": len(rows),
        **result,
    }


def aggregate_s11a(
    exp10_csv: Path | str,
    exp11_csv: Path | str,
    exp12_csv: Path | str,
) -> Dict[str, Any]:
    """Aggregate full frozen S11-A scope (Exp10-Q, Exp11-Q, Exp12-Q).

    Exp13-Q is explicitly excluded from S11-A.
    """
    exp10_agg = aggregate_experiment_from_csv(exp10_csv, "exp10q")
    exp11_agg = aggregate_experiment_from_csv(exp11_csv, "exp11q")
    exp12_agg = aggregate_experiment_from_csv(exp12_csv, "exp12q")

    total_runs = exp10_agg["total_rows"] + exp11_agg["total_rows"] + exp12_agg["total_rows"]
    if total_runs != 80:
        raise ValueError(f"S11-A requires strictly 80 runs, got {total_runs}")

    return {
        "schema_version": "1.0.0",
        "analysis_contract": "docs/04_STATISTICAL_CONTRACT.md",
        "scope": "S11-A (Exp10-Q Failure, Exp11-Q Churn, Exp12-Q Heterogeneity)",
        "student_t_multiplier_95_df4": STUDENT_T_95_DF4,
        "frozen_seeds": list(FROZEN_SEEDS),
        "primary_metrics": list(PRIMARY_METRICS),
        "total_runs": total_runs,
        "total_paired_comparisons": 40,
        "experiments": {
            "exp10q": exp10_agg,
            "exp11q": exp11_agg,
            "exp12q": exp12_agg,
        },
    }


def generate_summary_csv_rows(s11a_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate flattened rows for the auditable summary CSV table."""
    summary_rows: List[Dict[str, Any]] = []

    experiments = s11a_data.get("experiments", {})
    for exp_id in ("exp10q", "exp11q", "exp12q"):
        exp_data = experiments[exp_id]
        exp_name = exp_data["name"]
        cond_key = exp_data["condition_key"]
        conditions = exp_data["conditions"]

        for cond in conditions:
            for metric in PRIMARY_METRICS:
                ahbn_cell = exp_data["cell_summaries"][cond]["ahbn"][metric]
                q_cell = exp_data["cell_summaries"][cond]["qahbn2"][metric]
                pair = exp_data["paired_effects"][cond][metric]

                row = {
                    "experiment": exp_name,
                    "condition_key": cond_key,
                    "condition": cond,
                    "metric": metric,
                    "ahbn_mean": ahbn_cell["mean"],
                    "ahbn_sd": ahbn_cell["sd"],
                    "ahbn_ci95_low": ahbn_cell["ci95_low"],
                    "ahbn_ci95_high": ahbn_cell["ci95_high"],
                    "qahbn2_mean": q_cell["mean"],
                    "qahbn2_sd": q_cell["sd"],
                    "qahbn2_ci95_low": q_cell["ci95_low"],
                    "qahbn2_ci95_high": q_cell["ci95_high"],
                    "paired_diff_mean": pair["mean"],
                    "paired_diff_sd": pair["sd"],
                    "paired_diff_ci95_low": pair["ci95_low"],
                    "paired_diff_ci95_high": pair["ci95_high"],
                    "relative_change_percent": pair.get("relative_change_percent"),
                    "percentage_point_difference": pair.get("percentage_point_difference", ""),
                }
                summary_rows.append(row)

    return summary_rows


SUMMARY_CSV_COLUMNS = [
    "experiment",
    "condition_key",
    "condition",
    "metric",
    "ahbn_mean",
    "ahbn_sd",
    "ahbn_ci95_low",
    "ahbn_ci95_high",
    "qahbn2_mean",
    "qahbn2_sd",
    "qahbn2_ci95_low",
    "qahbn2_ci95_high",
    "paired_diff_mean",
    "paired_diff_sd",
    "paired_diff_ci95_low",
    "paired_diff_ci95_high",
    "relative_change_percent",
    "percentage_point_difference",
]


def write_summary_csv(summary_rows: List[Dict[str, Any]], out_path: Path | str) -> None:
    """Write summary table to CSV file."""
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(summary_rows)


def run_s11a_pipeline(
    output_dir: Path | str,
    exp10_csv: Optional[Path | str] = None,
    exp11_csv: Optional[Path | str] = None,
    exp12_csv: Optional[Path | str] = None,
) -> Path:
    """Execute S11-A aggregation pipeline and write release artifacts.

    Note: This is intended for gate S11-A-1, NOT S11-A-PREP.
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    csv10 = Path(exp10_csv) if exp10_csv else EXPERIMENT_SPECS["exp10q"]["default_csv"]
    csv11 = Path(exp11_csv) if exp11_csv else EXPERIMENT_SPECS["exp11q"]["default_csv"]
    csv12 = Path(exp12_csv) if exp12_csv else EXPERIMENT_SPECS["exp12q"]["default_csv"]

    s11a_data = aggregate_s11a(exp10_csv=csv10, exp11_csv=csv11, exp12_csv=csv12)

    # 1. Machine-readable JSON
    json_path = out_dir / "s11a_primary_ro4_aggregation.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(s11a_data, f, indent=2)

    # 2. Publication-auditable CSV
    summary_rows = generate_summary_csv_rows(s11a_data)
    csv_path = out_dir / "s11a_primary_ro4_summary.csv"
    write_summary_csv(summary_rows, csv_path)

    # 3. RUN.md and manifest.json provenance
    timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
    git_sha = _git_head()

    manifest = {
        "environment": "ControlSim",
        "stage": "S11-A",
        "event": "formal_aggregation",
        "timestamp": timestamp,
        "git_commit": git_sha,
        "canonical_ahbn_commit": CANONICAL_AHBN_COMMIT,
        "statistical_contract": "docs/04_STATISTICAL_CONTRACT.md",
        "total_runs_ingested": 80,
        "total_paired_comparisons": 40,
        "input_files": {
            "exp10q": {"path": str(csv10), "sha256": compute_file_sha256(csv10)},
            "exp11q": {"path": str(csv11), "sha256": compute_file_sha256(csv11)},
            "exp12q": {"path": str(csv12), "sha256": compute_file_sha256(csv12)},
        },
        "output_files": {
            "aggregation_json": {"path": str(json_path.name), "sha256": compute_file_sha256(json_path)},
            "summary_csv": {"path": str(csv_path.name), "sha256": compute_file_sha256(csv_path)},
        },
    }
    with open(out_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    run_md_content = f"""# S11-A Primary RO4 Formal Aggregation Run

- Timestamp: {timestamp}
- Git SHA: `{git_sha}`
- Canonical AHBN Commit: `{CANONICAL_AHBN_COMMIT}`
- Statistical Contract: `docs/04_STATISTICAL_CONTRACT.md`
- Scope: Exp10-Q (Failure), Exp11-Q (Churn), Exp12-Q (Heterogeneity)
- Total Ingested Runs: 80 (20 + 30 + 30)
- Total Paired Comparisons: 40 (10 + 15 + 15)
- Verification Status: PASS
- Output Artifacts:
  - `s11a_primary_ro4_aggregation.json`
  - `s11a_primary_ro4_summary.csv`
  - `manifest.json`
"""
    with open(out_dir / "RUN.md", "w", encoding="utf-8") as f:
        f.write(run_md_content)

    return out_dir


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Deterministic S11-A Formal Aggregator (docs/04_STATISTICAL_CONTRACT.md)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output/evidence/s11-aggregation/s11a-primary-ro4"),
        help="Target output directory for release artifacts",
    )
    parser.add_argument(
        "--exp10-csv",
        type=Path,
        default=None,
        help="Optional path to Exp10-Q formal CSV",
    )
    parser.add_argument(
        "--exp11-csv",
        type=Path,
        default=None,
        help="Optional path to Exp11-Q formal CSV",
    )
    parser.add_argument(
        "--exp12-csv",
        type=Path,
        default=None,
        help="Optional path to Exp12-Q formal CSV",
    )
    args = parser.parse_args()

    run_s11a_pipeline(
        output_dir=args.output_dir,
        exp10_csv=args.exp10_csv,
        exp11_csv=args.exp11_csv,
        exp12_csv=args.exp12_csv,
    )
    print(f"S11-A aggregation complete: {args.output_dir}")


if __name__ == "__main__":
    main()
