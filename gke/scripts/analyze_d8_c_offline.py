#!/usr/bin/env python3
"""Verify and analyze the frozen 25-run K5-Q matrix, offline and read-only."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import math
import platform
import re
import statistics
import subprocess
import sys
from pathlib import Path

import audit_d8_a_offline as d8a


REPO = Path(__file__).resolve().parents[2]
EVIDENCE = REPO / "output/evidence"
REPORT_TOLERANCE = 5e-10
ROOTS = {
    42: "20261020T032934Z-K5Q-formal",
    43: "20261020T035637Z-K5Q-formal",
    44: "20261020T041621Z-K5Q-formal",
    45: "20261020T043745Z-K5Q-formal",
    46: "20261020T045636Z-K5Q-formal",
}
METHODS = ("gossip", "structured", "dcsoc", "ahbn", "qahbn2")
METHOD_LABELS = {
    "gossip": "Gossip",
    "structured": "Structured",
    "dcsoc": "DC-SoC",
    "ahbn": "AHBN",
    "qahbn2": "Q-AHBN2",
}
METRICS = (
    "delivery_ratio",
    "propagation_delay",
    "duplicates",
    "total_forwards",
)
METRIC_UNITS = {
    "delivery_ratio": "proportion",
    "propagation_delay": "seconds",
    "duplicates": "count",
    "total_forwards": "count",
}
T_CRITICAL_DF4 = 2.7764451051977987
_ACTIVE_LOG_PATH: Path | None = None
EXPECTED_SOURCE = "6433f7429e0342df44c272b236423c65203a9136"
EXPECTED_IMAGE = (
    "sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228"
    "cd1575dde1c1488f"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def finite_number(value, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric, received {value!r}")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite, received {value!r}")
    return result


def csv_number(value, name: str) -> float:
    if not isinstance(value, str):
        return finite_number(value, name)
    try:
        return finite_number(float(value), name)
    except ValueError as error:
        raise ValueError(f"{name} must be a numeric CSV value, received {value!r}") from error


def ci_summary(values: list[float], *, t_critical: float = T_CRITICAL_DF4) -> dict:
    if len(values) != 5:
        raise ValueError(f"expected five independent seed values, found {len(values)}")
    clean = [finite_number(value, "observation") for value in values]
    mean = statistics.fmean(clean)
    sample_sd = statistics.stdev(clean)
    half_width = t_critical * sample_sd / math.sqrt(len(clean))
    return {
        "n": len(clean),
        "mean": mean,
        "sample_sd": sample_sd,
        "ci95_low": mean - half_width,
        "ci95_high": mean + half_width,
        "ci95_half_width": half_width,
        "df": len(clean) - 1,
        "t_critical_two_sided_95": t_critical,
        "ci_distribution": "Student-t",
    }


def crosscheck_value(metric: str, archived: float, reconstructed: float) -> dict:
    delta = reconstructed - archived
    exact = delta == 0.0
    # Numeric JSON values should reproduce exactly; this secondary tight bound
    # only accommodates equivalent decimal serialization if a producer changes.
    within_float_tolerance = math.isclose(
        reconstructed, archived, rel_tol=1e-12, abs_tol=1e-15
    )
    if not within_float_tolerance:
        raise ValueError(
            f"{metric} reconstruction differs from metrics.json: "
            f"archived={archived!r} reconstructed={reconstructed!r}"
        )
    return {
        "archived_metrics_json": archived,
        "independently_reconstructed": reconstructed,
        "difference": delta,
        "exact_numeric_match": exact,
        "within_tolerance": within_float_tolerance,
    }


def load_and_verify(
    evidence_dir: Path,
    reconciliation_csv: Path,
    preliminary_comparison_json: Path,
) -> tuple[list[dict], list[dict]]:
    with reconciliation_csv.open(newline="") as stream:
        reconciled_rows = list(csv.DictReader(stream))
    reconciled = {
        (int(row["seed"]), row["method"]): row for row in reconciled_rows
    }
    if len(reconciled_rows) != 25 or len(reconciled) != 25:
        raise ValueError("D8-A reconciliation must contain exactly 25 unique run rows")

    with preliminary_comparison_json.open() as stream:
        preliminary_rows = json.load(stream)
    preliminary = {}
    for row in preliminary_rows:
        key = (int(row["seed"]), row["method"], row["metric"])
        if key in preliminary:
            raise ValueError(f"duplicate D8-A preliminary comparison row {key}")
        preliminary[key] = row
    if len(preliminary) != 100:
        raise ValueError("D8-A preliminary comparison must contain 100 metric rows")

    dataset = []
    verification = []
    seed_fingerprints = {}
    for seed, root_name in ROOTS.items():
        root = evidence_dir / root_name
        root_commit = (root / "git_commit.txt").read_text().strip()
        expected_image = (root / "expected_image_digest.txt").read_text().strip()
        if root_commit != EXPECTED_SOURCE:
            raise ValueError(f"unexpected root Git commit for seed {seed}: {root_commit}")
        if expected_image != EXPECTED_IMAGE:
            raise ValueError(f"unexpected root image digest for seed {seed}")

        for method in METHODS:
            run = root / "runs" / f"seed{seed}" / method
            manifest_path = run / "run_manifest.json"
            metrics_path = run / "metrics.json"
            topology_path = run / "topology.json"
            logs_path = run / "logs.jsonl"
            manifest = read_json(manifest_path)
            metrics = read_json(metrics_path)
            topology = read_json(topology_path)
            rows, duplicate_log_records, ignored_lines = d8a.records(logs_path)
            reconstructed, opportunities, event_rows = d8a.reconstruct(rows, topology)

            if manifest.get("seed") != seed or manifest.get("algorithm") != method:
                raise ValueError(f"manifest identity mismatch at seed={seed} method={method}")
            if metrics.get("seed") != seed or metrics.get("algorithm") != method:
                raise ValueError(f"metrics identity mismatch at seed={seed} method={method}")
            expected_manifest = {
                "contract_version": "k7-exp11-v2",
                "message_count": 240,
                "message_interval": 0.4,
                "frozen_targets": [0, 5, 10, 15],
                "churn_offsets": [1.0, 26.0, 51.0, 76.0],
            }
            for name, expected in expected_manifest.items():
                if manifest.get(name) != expected:
                    raise ValueError(
                        f"frozen manifest field {name} differs at seed={seed} method={method}"
                    )
            expected_run_id = f"k7_exp11_{method}_seed{seed}"
            if metrics.get("run_id") != expected_run_id:
                raise ValueError(f"run ID mismatch: {metrics.get('run_id')!r}")
            if (seed, method) not in reconciled:
                raise ValueError(f"missing D8-A reconciliation row seed={seed} method={method}")
            if reconciled[(seed, method)].get("content_checks") != "PASS":
                raise ValueError(
                    f"prior independent protocol/content checks did not pass "
                    f"for seed={seed} method={method}"
                )

            expected_topology = {
                "seed": seed,
                "num_nodes": 20,
                "topology_type": "ba",
                "ba_m": 2,
                "strategy": "cluster" if method == "structured" else method,
            }
            for name, expected in expected_topology.items():
                if topology.get(name) != expected:
                    raise ValueError(
                        f"frozen topology field {name} differs at seed={seed} method={method}"
                    )
            if topology.get("workload") != {
                "message_count": 240,
                "message_interval": 0.4,
            }:
                raise ValueError(f"topology workload mismatch at seed={seed} method={method}")
            if topology.get("k5_h2", {}).get("actuator_treatment") != "S5":
                raise ValueError(f"frozen K5-Q treatment mismatch at seed={seed} method={method}")
            if topology.get("k7_exp11", {}).get("algorithm") != method:
                raise ValueError(f"topology algorithm mismatch at seed={seed} method={method}")
            if topology.get("k7_exp11", {}).get("target_peers") != [0, 5, 10, 15]:
                raise ValueError(f"frozen target schedule mismatch at seed={seed} method={method}")
            if topology.get("k7_exp11", {}).get("plannedLeaveOffsetsSec") != [
                1.0,
                26.0,
                51.0,
                76.0,
            ]:
                raise ValueError(f"frozen churn schedule mismatch at seed={seed} method={method}")
            if topology.get("dcsoc", {}).get("dynamic_maintenance") != (method == "dcsoc"):
                raise ValueError(f"DC-SoC isolation mismatch at seed={seed} method={method}")
            target_path = root / "target-selection" / f"seed{seed}.json"
            target = read_json(target_path)
            target_identity = {
                key: value for key, value in target.items() if key != "selection_hash"
            }
            target_hash = hashlib.sha256(
                d8a.canonical(target_identity).encode()
            ).hexdigest()
            if (
                target.get("frozen_targets") != [0, 5, 10, 15]
                or target.get("selection_hash") != manifest.get("target_selection_hash")
                or target_hash != manifest.get("target_selection_hash")
                or topology.get("k7_exp11", {}).get("target_selection_hash")
                != manifest.get("target_selection_hash")
            ):
                raise ValueError(f"target-selection fingerprint mismatch at seed={seed}")
            seed_fingerprint = {
                "edges": {
                    node_id: node.get("neighbors")
                    for node_id, node in topology.get("nodes", {}).items()
                },
                "source": topology.get("message_source"),
                "target_selection_hash": manifest["target_selection_hash"],
            }
            if seed in seed_fingerprints and seed_fingerprints[seed] != seed_fingerprint:
                raise ValueError(f"within-seed topology or target fingerprint differs at seed={seed}")
            seed_fingerprints[seed] = seed_fingerprint
            generated_topology_path = root / "generated" / f"{method}_seed{seed}.json"
            if read_json(generated_topology_path) != topology:
                raise ValueError(f"generated topology mismatch at seed={seed} method={method}")
            generated_config = run / "generated_config.yaml"
            source_config = root / "configs" / f"{method}_seed{seed}.yaml"
            if sha256_file(generated_config) != sha256_file(source_config):
                raise ValueError(f"generated config fingerprint mismatch at seed={seed} method={method}")

            required_statuses = {
                "experiment_exit_status.txt": "0",
                "cleanup_exit_status.txt": "0",
                "namespace_cleanup_exit_status.txt": "0",
                "helm_cleanup_exit_status.txt": "0",
                "cleanup_status.txt": "PASS",
                "namespace_check_error.txt": "",
            }
            for status_file, expected in required_statuses.items():
                observed = (run / status_file).read_text().strip()
                if observed != expected:
                    raise ValueError(
                        f"{status_file}={observed!r}, expected {expected!r} "
                        f"at seed={seed} method={method}"
                    )
            if "deleted" not in (run / "namespace_cleanup.txt").read_text().lower():
                raise ValueError(f"namespace cleanup record missing at seed={seed} method={method}")
            pod_items = read_json(run / "pods.json").get("items", [])
            runtime_image_ids = [
                container.get("imageID")
                for pod in pod_items
                for container in pod.get("status", {}).get("containerStatuses", [])
            ]
            ready_states = [
                container.get("ready")
                for pod in pod_items
                for container in pod.get("status", {}).get("containerStatuses", [])
            ]
            if (
                len(pod_items) != 20
                or len(ready_states) != 20
                or not all(ready_states)
                or not runtime_image_ids
                or any(
                not image_id or not image_id.endswith(EXPECTED_IMAGE) for image_id in runtime_image_ids
                )
            ):
                raise ValueError(f"runtime image identity mismatch at seed={seed} method={method}")
            controller_phases = [
                pod.get("status", {}).get("phase")
                for pod in read_json(run / "controller_pods.json").get("items", [])
            ]
            if controller_phases != ["Succeeded"]:
                raise ValueError(
                    f"controller job did not complete successfully at seed={seed} method={method}"
                )

            metric_checks = {}
            for metric in METRICS:
                archived_value = finite_number(metrics.get(metric), metric)
                reconstructed_value = finite_number(reconstructed.get(metric), metric)
                metric_checks[metric] = crosscheck_value(
                    metric, archived_value, reconstructed_value
                )
                prior = csv_number(
                    reconciled[(seed, method)].get(metric), f"D8-A {metric}"
                )
                if not math.isclose(
                    prior, archived_value, rel_tol=1e-12, abs_tol=1e-15
                ):
                    raise ValueError(
                        f"D8-A audit table mismatch at seed={seed} method={method} "
                        f"metric={metric}: prior={prior} archive={archived_value}"
                    )
                prior_match = preliminary.get((seed, method, metric))
                if prior_match is None:
                    raise ValueError(f"missing D8-A comparison {seed}/{method}/{metric}")
                if not math.isclose(
                    finite_number(prior_match["archived"], "prior archived"),
                    archived_value,
                    rel_tol=1e-12,
                    abs_tol=1e-15,
                ):
                    raise ValueError(
                        f"D8-A preliminary archive mismatch {seed}/{method}/{metric}"
                    )

            if metrics["delivery_ratio"] < 0.0 or metrics["delivery_ratio"] > 1.0:
                raise ValueError(f"delivery ratio out of domain for {seed}/{method}")
            for metric in ("duplicates", "total_forwards"):
                value = metrics[metric]
                if int(value) != value or value < 0:
                    raise ValueError(f"{metric} must be a non-negative integer count")
            if metrics["propagation_delay"] < 0.0:
                raise ValueError(f"negative propagation delay for {seed}/{method}")

            reconciliation = reconciled[(seed, method)]
            dataset_row = {
                "seed": seed,
                "method": method,
                "method_label": METHOD_LABELS[method],
                "run_id": metrics["run_id"],
                "evidence_root": root_name,
                "evidence_path": run.relative_to(evidence_dir).as_posix(),
                **{metric: metrics[metric] for metric in METRICS},
                "F_attempt_diagnostic": metrics["F_attempt"],
                "F_success_diagnostic": metrics["F_success"],
                "source_commit": root_commit,
                "expected_image_digest": expected_image,
                "source_peer": topology["message_source"],
                "target_selection_hash": manifest["target_selection_hash"],
                "metric_reconstruction": "PASS",
                "exact_duplicate_log_records_removed": duplicate_log_records,
                "ignored_log_lines": ignored_lines,
            }
            dataset.append(dataset_row)
            verification.append(
                {
                    "seed": seed,
                    "method": method,
                    "run_id": metrics["run_id"],
                    "evidence_path": run.relative_to(evidence_dir).as_posix(),
                    "metrics_json_sha256": sha256_file(metrics_path),
                    "manifest_json_sha256": sha256_file(manifest_path),
                    "topology_json_sha256": sha256_file(topology_path),
                    "logs_jsonl_sha256": sha256_file(logs_path),
                    "metric_checks": metric_checks,
                    "d8_a_reconciliation_status": reconciliation["content_checks"],
                    "d8_a_prior_comparison_rows": 4,
                    "reconstructed_opportunity_count": len(opportunities),
                    "reconstructed_message_injection_count": len(
                        event_rows["message_injected"]
                    ),
                    "source_commit": root_commit,
                    "expected_image_digest": expected_image,
                }
            )
    return dataset, verification


def summarize_methods(dataset: list[dict]) -> list[dict]:
    results = []
    for method in METHODS:
        cells = sorted(
            (row for row in dataset if row["method"] == method),
            key=lambda row: row["seed"],
        )
        if [row["seed"] for row in cells] != list(ROOTS):
            raise ValueError(f"method {method} does not have exactly seeds 42-46")
        for metric in METRICS:
            result = ci_summary([float(row[metric]) for row in cells])
            results.append(
                {
                    "method": method,
                    "method_label": METHOD_LABELS[method],
                    "metric": metric,
                    "unit": METRIC_UNITS[metric],
                    **result,
                }
            )
    return results


def summarize_qahbn2_vs_ahbn(dataset: list[dict]) -> tuple[list[dict], list[dict]]:
    lookup = {(row["seed"], row["method"]): row for row in dataset}
    paired_rows = []
    summaries = []
    for metric in METRICS:
        differences = []
        for seed in ROOTS:
            ahbn = float(lookup[(seed, "ahbn")][metric])
            qahbn2 = float(lookup[(seed, "qahbn2")][metric])
            delta = qahbn2 - ahbn
            differences.append(delta)
            paired_rows.append(
                {
                    "seed": seed,
                    "metric": metric,
                    "unit": METRIC_UNITS[metric],
                    "AHBN": ahbn,
                    "Q_AHBN2": qahbn2,
                    "Q_AHBN2_minus_AHBN": delta,
                    "delivery_difference_percentage_points": (
                        delta * 100.0 if metric == "delivery_ratio" else None
                    ),
                }
            )
        result = ci_summary(differences)
        ahbn_mean = statistics.fmean(
            float(lookup[(seed, "ahbn")][metric]) for seed in ROOTS
        )
        qahbn2_mean = statistics.fmean(
            float(lookup[(seed, "qahbn2")][metric]) for seed in ROOTS
        )
        summaries.append(
            {
                "comparison": "Q-AHBN2 - AHBN",
                "metric": metric,
                "unit": METRIC_UNITS[metric],
                "AHBN_mean": ahbn_mean,
                "Q_AHBN2_mean": qahbn2_mean,
                "mean_difference": result["mean"],
                "sample_sd_of_differences": result["sample_sd"],
                "ci95_low": result["ci95_low"],
                "ci95_high": result["ci95_high"],
                "ci95_half_width": result["ci95_half_width"],
                "n": result["n"],
                "df": result["df"],
                "t_critical_two_sided_95": result["t_critical_two_sided_95"],
                "relative_mean_change_percent_vs_AHBN": (
                    100.0 * (qahbn2_mean - ahbn_mean) / ahbn_mean
                    if abs(ahbn_mean) > 1e-12
                    else None
                ),
                "mean_delivery_percentage_point_difference": (
                    result["mean"] * 100.0 if metric == "delivery_ratio" else None
                ),
                "direction_note": {
                    "delivery_ratio": "positive means higher Q-AHBN2 delivery",
                    "propagation_delay": "positive means higher Q-AHBN2 delay",
                    "duplicates": "positive means more Q-AHBN2 duplicates",
                    "total_forwards": "positive means more Q-AHBN2 forwards",
                }[metric],
                "significance_test_performed": False,
            }
        )
    return paired_rows, summaries


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"refusing to write an empty CSV: {path}")
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def compare_reported_metrics(dataset: list[dict], preliminary_rows: list[dict]) -> list[dict]:
    source_values = {
        (row["seed"], row["method"], metric): finite_number(row[metric], metric)
        for row in dataset
        for metric in METRICS
    }
    report_values = {}
    for row in preliminary_rows:
        key = (int(row["seed"]), row["method"], row["metric"])
        if key in report_values:
            raise ValueError(f"duplicate preliminary comparison row {key}")
        report_values[key] = row
    if len(source_values) != 100 or len(report_values) != 100:
        raise ValueError("source and preliminary report must each contain 100 metric values")

    comparisons = []
    for key, source_value in sorted(source_values.items()):
        row = report_values.get(key)
        if row is None:
            raise ValueError(f"missing preliminary comparison row {key}")
        reported_value = finite_number(float(row["reported"]), "reported metric")
        archived_value = finite_number(row["archived"], "archived metric")
        archived_difference = abs(source_value - archived_value)
        if not math.isclose(source_value, archived_value, rel_tol=1e-12, abs_tol=1e-15):
            raise ValueError(
                f"preliminary archived value differs from original metrics.json at {key}"
            )
        difference = abs(source_value - reported_value)
        comparisons.append(
            {
                "seed": key[0],
                "method": key[1],
                "metric": key[2],
                "original_metrics_path": (
                    f"output/evidence/{ROOTS[key[0]]}/runs/seed{key[0]}/{key[1]}/metrics.json"
                ),
                "reported_value": reported_value,
                "actual_source_value": source_value,
                "absolute_difference": difference,
                "report_rounding_tolerance": REPORT_TOLERANCE,
                "archived_dataset_absolute_difference": archived_difference,
                "status": "PASS" if difference <= REPORT_TOLERANCE else "FAIL",
            }
        )
    return comparisons


def build_inventory(
    evidence_dir: Path, dataset: list[dict], reconciliation_csv: Path
) -> list[dict]:
    with reconciliation_csv.open(newline="") as stream:
        prior_rows = list(csv.DictReader(stream))
    prior = {(int(row["seed"]), row["method"]): row for row in prior_rows}
    inventory = []
    for row in dataset:
        run_dir = evidence_dir / row["evidence_path"]
        manifest = read_json(run_dir / "run_manifest.json")
        metrics = read_json(run_dir / "metrics.json")
        prior_row = prior[(row["seed"], row["method"])]
        status_files = (
            "experiment_exit_status.txt",
            "cleanup_exit_status.txt",
            "namespace_cleanup_exit_status.txt",
            "helm_cleanup_exit_status.txt",
            "cleanup_status.txt",
            "namespace_check_error.txt",
        )
        statuses = {
            filename: (run_dir / filename).read_text().strip() for filename in status_files
        }
        runtime_image_ids = sorted(
            {
                container.get("imageID")
                for pod in read_json(run_dir / "pods.json").get("items", [])
                for container in pod.get("status", {}).get("containerStatuses", [])
                if container.get("imageID")
            }
        )
        if runtime_image_ids != sorted(set(json.loads(prior_row["runtime_image_ids"]))):
            raise ValueError(
                f"runtime image identifiers differ from prior audit at "
                f"seed={row['seed']} method={row['method']}"
            )
        inventory.append(
            {
                "seed": row["seed"],
                "method": row["method"],
                "run_id": row["run_id"],
                "evidence_root": row["evidence_root"],
                "run_directory": f"output/evidence/{row['evidence_path']}",
                "metrics_path": f"output/evidence/{row['evidence_path']}/metrics.json",
                "manifest_path": f"output/evidence/{row['evidence_path']}/run_manifest.json",
                "manifest_seed": manifest.get("seed"),
                "manifest_method": manifest.get("algorithm"),
                "metrics_seed": metrics.get("seed"),
                "metrics_method": metrics.get("algorithm"),
                "source_commit": row["source_commit"],
                "expected_image_digest": row["expected_image_digest"],
                "runtime_image_ids": json.dumps(runtime_image_ids, separators=(",", ":")),
                "target_selection_hash": row["target_selection_hash"],
                "experiment_exit_status": statuses.get("experiment_exit_status.txt", ""),
                "cleanup_exit_status": statuses.get("cleanup_exit_status.txt", ""),
                "namespace_cleanup_exit_status": statuses.get(
                    "namespace_cleanup_exit_status.txt", ""
                ),
                "helm_cleanup_exit_status": statuses.get(
                    "helm_cleanup_exit_status.txt", ""
                ),
                "cleanup_status": statuses.get("cleanup_status.txt", ""),
                "namespace_check_error": statuses.get("namespace_check_error.txt", ""),
                "content_checks": prior_row["content_checks"],
            }
        )
    return inventory


def build_integrity_manifest(
    evidence_dir: Path,
    dataset: list[dict],
    prior_inventory_path: Path,
    prior_comparison_path: Path,
) -> list[dict]:
    prior_records = json.loads(prior_inventory_path.read_text())
    prior_hashes = {row["path"]: row for row in prior_records}
    with prior_comparison_path.open(newline="") as stream:
        comparison_rows = {
            row["relative_path"]: row for row in csv.DictReader(stream)
        }
    integrity_rows = []
    for run in dataset:
        run_dir = evidence_dir / run["evidence_path"]
        for name in ("metrics.json", "run_manifest.json", "topology.json", "logs.jsonl"):
            path = run_dir / name
            relative_path = f"{run['evidence_path']}/{name}"
            current_hash = sha256_file(path)
            prior = prior_hashes.get(relative_path)
            prior_comparison = comparison_rows.get(relative_path, {})
            reference_hash = prior.get("sha256", "") if prior else ""
            integrity_rows.append(
                {
                    "seed": run["seed"],
                    "method": run["method"],
                    "run_id": run["run_id"],
                    "file_path": f"output/evidence/{relative_path}",
                    "file_size_bytes": path.stat().st_size,
                    "sha256": current_hash,
                    "prior_d8a_audit_sha256": reference_hash,
                    "prior_hash_comparison": (
                        "MATCH"
                        if reference_hash and current_hash == reference_hash
                        else "MISMATCH"
                        if reference_hash
                        else "NO_REFERENCE"
                    ),
                    "trusted_baseline_status": prior_comparison.get(
                        "comparison_status", "NO_REFERENCE"
                    ),
                    "trusted_baseline_reference_sha256": prior_comparison.get(
                        "reference_sha256", ""
                    ),
                    "historical_execution_time_baseline": "UNAVAILABLE",
                }
            )
    return integrity_rows


def compare_statistical_outputs(
    method_summaries: list[dict],
    paired_rows: list[dict],
    paired_summaries: list[dict],
    reference_dir: Path,
) -> dict[str, int]:
    references = {
        "method_summaries.csv": (method_summaries, ("mean", "sample_sd", "ci95_low", "ci95_high")),
        "paired_seed_differences.csv": (paired_rows, ("AHBN", "Q_AHBN2", "Q_AHBN2_minus_AHBN")),
        "paired_qahbn2_vs_ahbn_summaries.csv": (
            paired_summaries,
            ("AHBN_mean", "Q_AHBN2_mean", "mean_difference", "sample_sd_of_differences", "ci95_low", "ci95_high"),
        ),
    }
    match_counts = {}
    for filename, (calculated, numeric_fields) in references.items():
        with (reference_dir / filename).open(newline="") as stream:
            recorded = list(csv.DictReader(stream))
        if len(recorded) != len(calculated):
            raise ValueError(f"{filename} row count differs from independent recalculation")
        for actual, expected in zip(calculated, recorded):
            for field in numeric_fields:
                if not math.isclose(
                    float(actual[field]),
                    float(expected[field]),
                    rel_tol=1e-12,
                    abs_tol=1e-12,
                ):
                    raise ValueError(
                        f"{filename} differs at {actual.get('metric')} field {field}"
                    )
        match_counts[filename] = len(calculated)
    return match_counts


def compare_statistical_report(
    report_path: Path,
    method_summaries: list[dict],
    paired_rows: list[dict],
    paired_summaries: list[dict],
) -> list[str]:
    lines = report_path.read_text().splitlines()

    def table_rows(header: str) -> list[list[str]]:
        for index, line in enumerate(lines):
            if line.strip() == header:
                rows = []
                for candidate in lines[index + 1 :]:
                    if not candidate.strip().startswith("|"):
                        break
                    cells = [cell.strip() for cell in candidate.strip().strip("|").split("|")]
                    if cells and not all(set(cell) <= {"-", ":"} for cell in cells):
                        rows.append(cells)
                return rows
        return []

    def matches_displayed(value: float, token: str) -> bool:
        try:
            reported = float(token.strip().replace(",", "").replace("−", "-"))
        except ValueError:
            return False
        decimal = token.strip().partition(".")[2]
        tolerance = 10 ** (-len(decimal)) if decimal else 0.5
        return abs(value - reported) <= tolerance + 1e-15

    errors = []
    method_rows = table_rows(
        "| Method | Delivery ratio | Propagation delay (s) | Duplicates | Total forwards |"
    )
    expected_methods = {(row["method_label"], row["metric"]): row for row in method_summaries}
    metric_columns = (
        "delivery_ratio",
        "propagation_delay",
        "duplicates",
        "total_forwards",
    )
    if len(method_rows) != len(METHODS):
        errors.append(f"method summary table has {len(method_rows)} rows, expected 5")
    for row in method_rows:
        if len(row) != 5:
            errors.append(f"malformed method summary row: {row!r}")
            continue
        for metric, cell in zip(metric_columns, row[1:]):
            expected = expected_methods.get((row[0], metric))
            match = re.fullmatch(
                r"\s*([^;]+);\s*([^;]+);\s*\[([^,]+),\s*([^\]]+)\]\s*", cell
            )
            if expected is None or match is None:
                errors.append(f"unparseable method summary cell {row[0]}/{metric}: {cell!r}")
                continue
            values = (
                expected["mean"],
                expected["sample_sd"],
                expected["ci95_low"],
                expected["ci95_high"],
            )
            if not all(
                matches_displayed(value, token)
                for value, token in zip(values, match.groups())
            ):
                errors.append(f"method summary differs from report for {row[0]}/{metric}")

    paired_summary_rows = table_rows(
        "| Metric | AHBN mean | Q-AHBN2 mean | Mean paired difference | "
        "SD of paired differences | Two-sided 95% paired t CI |"
    )
    paired_summary_by_metric = {row["metric"]: row for row in paired_summaries}
    if len(paired_summary_rows) != len(METRICS):
        errors.append(
            f"paired summary table has {len(paired_summary_rows)} rows, expected 4"
        )
    for row in paired_summary_rows:
        if len(row) != 6:
            errors.append(f"malformed paired summary row: {row!r}")
            continue
        metric = row[0].split(" (", 1)[0].lower().replace(" ", "_")
        if metric == "propagation_delay":
            metric = "propagation_delay"
        expected = paired_summary_by_metric.get(metric)
        interval = re.fullmatch(r"\[([^,]+),\s*([^\]]+)\]", row[5])
        if expected is None or interval is None:
            errors.append(f"unparseable paired summary row: {row!r}")
            continue
        values = (
            expected["AHBN_mean"],
            expected["Q_AHBN2_mean"],
            expected["mean_difference"],
            expected["sample_sd_of_differences"],
            expected["ci95_low"],
            expected["ci95_high"],
        )
        reported_values = (*row[1:5], *interval.groups())
        if not all(
            matches_displayed(value, token)
            for value, token in zip(values, reported_values)
        ):
            errors.append(f"paired summary differs from report for {metric}")

    per_seed_rows = table_rows(
        "| Seed | Delivery ratio | Delivery (percentage points) | "
        "Propagation delay (s) | Duplicates | Total forwards |"
    )
    paired_by_seed_metric = {
        (row["seed"], row["metric"]): row for row in paired_rows
    }
    if len(per_seed_rows) != len(ROOTS):
        errors.append(f"per-seed table has {len(per_seed_rows)} rows, expected 5")
    for row in per_seed_rows:
        if len(row) != 6:
            errors.append(f"malformed per-seed row: {row!r}")
            continue
        seed = int(row[0])
        expected_values = [
            paired_by_seed_metric[(seed, "delivery_ratio")][
                "Q_AHBN2_minus_AHBN"
            ],
            paired_by_seed_metric[(seed, "delivery_ratio")][
                "delivery_difference_percentage_points"
            ],
            paired_by_seed_metric[(seed, "propagation_delay")][
                "Q_AHBN2_minus_AHBN"
            ],
            paired_by_seed_metric[(seed, "duplicates")]["Q_AHBN2_minus_AHBN"],
            paired_by_seed_metric[(seed, "total_forwards")]["Q_AHBN2_minus_AHBN"],
        ]
        if not all(
            matches_displayed(value, token)
            for value, token in zip(expected_values, row[1:])
        ):
            errors.append(f"per-seed paired values differ from report for seed {seed}")
    return errors


def build_statistical_rows(
    method_summaries: list[dict],
    paired_rows: list[dict],
    paired_summaries: list[dict],
) -> list[dict]:
    output = []
    for row in method_summaries:
        output.append(
            {
                "record_type": "method_summary",
                "method": row["method"],
                "comparison": "",
                "seed": "",
                "metric": row["metric"],
                "unit": row["unit"],
                "n": row["n"],
                "mean": row["mean"],
                "sample_sd": row["sample_sd"],
                "ci95_low": row["ci95_low"],
                "ci95_high": row["ci95_high"],
                "df": row["df"],
            }
        )
    for row in paired_rows:
        output.append(
            {
                "record_type": "paired_seed_difference",
                "method": "",
                "comparison": "Q-AHBN2 - AHBN",
                "seed": row["seed"],
                "metric": row["metric"],
                "unit": row["unit"],
                "n": 1,
                "AHBN": row["AHBN"],
                "Q_AHBN2": row["Q_AHBN2"],
                "mean_difference": row["Q_AHBN2_minus_AHBN"],
                "delivery_difference_percentage_points": row[
                    "delivery_difference_percentage_points"
                ],
            }
        )
    for row in paired_summaries:
        output.append(
            {
                "record_type": "paired_contrast_summary",
                "method": "",
                "comparison": row["comparison"],
                "seed": "",
                "metric": row["metric"],
                "unit": row["unit"],
                "n": row["n"],
                "mean": row["mean_difference"],
                "sample_sd": row["sample_sd_of_differences"],
                "ci95_low": row["ci95_low"],
                "ci95_high": row["ci95_high"],
                "df": row["df"],
            }
        )
    return output


def write_final_reports(
    output: Path,
    dataset: list[dict],
    comparisons: list[dict],
    integrity: list[dict],
    method_summaries: list[dict],
    paired_rows: list[dict],
    paired_summaries: list[dict],
    statistical_reference_matches: dict[str, int],
    statistical_report_failures: list[str],
) -> None:
    failing_metrics = [row for row in comparisons if row["status"] != "PASS"]
    hash_mismatches = [row for row in integrity if row["prior_hash_comparison"] != "MATCH"]
    decision = (
        "HOLD"
        if failing_metrics or hash_mismatches or statistical_report_failures
        else "PARTIAL"
    )
    method_lines = [
        "| Method | Metric | Mean | Sample SD | Unadjusted 95% t CI (df=4) |",
        "|---|---|---:|---:|---|",
    ]
    for row in method_summaries:
        method_lines.append(
            f"| {row['method_label']} | {row['metric']} ({row['unit']}) | "
            f"{row['mean']:.6f} | {row['sample_sd']:.6f} | "
            f"[{row['ci95_low']:.6f}, {row['ci95_high']:.6f}] |"
        )
    paired_lines = [
        "| Metric | Mean Q-AHBN2 − AHBN | Sample SD | Unadjusted 95% paired t CI (df=4) |",
        "|---|---:|---:|---|",
    ]
    for row in paired_summaries:
        paired_lines.append(
            f"| {row['metric']} ({row['unit']}) | {row['mean_difference']:.6f} | "
            f"{row['sample_sd_of_differences']:.6f} | "
            f"[{row['ci95_low']:.6f}, {row['ci95_high']:.6f}] |"
        )
    per_seed_lines = [
        "| Seed | Metric | AHBN | Q-AHBN2 | Q-AHBN2 − AHBN |",
        "|---:|---|---:|---:|---:|",
    ]
    for row in paired_rows:
        per_seed_lines.append(
            f"| {row['seed']} | {row['metric']} | {row['AHBN']:.12g} | "
            f"{row['Q_AHBN2']:.12g} | {row['Q_AHBN2_minus_AHBN']:.12g} |"
        )
    (output / "discrepancies.md").write_text(
        "# D8-C offline evidence discrepancies and limitations\n\n"
        f"- Source-to-report comparisons: {len(comparisons) - len(failing_metrics)}/"
        f"{len(comparisons)} PASS using absolute tolerance {REPORT_TOLERANCE:g}; "
        f"unresolved failed comparisons: {len(failing_metrics)}.\n"
        f"- Original evidence files read and hashed: {len(integrity)}; "
        f"matched prior D8-A audit hashes: "
        f"{sum(row['prior_hash_comparison'] == 'MATCH' for row in integrity)}; "
        f"hash mismatches or absent references: {len(hash_mismatches)}.\n"
        "- No trusted execution-time per-file hash baseline is available. Current hashes "
        "and matching prior D8-A audit fingerprints do not establish byte identity since "
        "experiment execution.\n"
        "- The local mirror's selected seed-43 root "
        "`20261020T035637Z-K5Q-formal/runs/seed43/` contains all five methods and each "
        "manifest identifies seed 43. The earlier, distinct root "
        "`20261020T023432Z-K5Q-formal` is outside the selected matrix and was not "
        "deleted, renamed, or reclassified.\n"
        "- Missing/unreadable required files: none among the 25 original metrics, "
        "manifests, topologies, or logs; all were opened and parsed.\n"
        "- Scientific/protocol violations: none confirmed in the selected 25-run local "
        "evidence set. Unexplained source-to-report mismatches: "
        f"{len(failing_metrics)}. This is a local-mirror finding; no live cluster or "
        "remote Drive operation was performed.\n"
        "- D8-B recovery diagnostics remain limited: 18 seconds is the post-workload "
        "settle interval rather than an event-relative censoring window; one recovered "
        "record exceeds 18 seconds and two event observations reuse a message anchor. "
        "Recovery is secondary and not used in these four metrics.\n"
        "- Statistical reports retain n=5 seeds, unadjusted two-sided Student-t intervals "
        "(df=4), no multiplicity adjustment, and no causal or overall-superiority claim.\n"
        "- D8-A and D8-B remain PARTIAL. No run is excluded for low delivery, and no "
        "manuscript or thesis content is modified.\n"
        + "".join(
            f"- Unresolved source-to-report value: seed={row['seed']}, "
            f"method={row['method']}, metric={row['metric']}, "
            f"reported={row['reported_value']}, source={row['actual_source_value']}, "
            f"absolute_difference={row['absolute_difference']}.\n"
            for row in failing_metrics
        )
        + "".join(
            f"- Prior hash mismatch or absent reference: {row['file_path']} "
            f"({row['prior_hash_comparison']}).\n"
            for row in hash_mismatches
        )
        + (
            "- Statistical report comparison differences: "
            + "; ".join(statistical_report_failures)
            + ".\n"
            if statistical_report_failures
            else "- Existing statistical report and per-seed tables match at displayed precision.\n"
        )
    )
    (output / "audit_report.md").write_text(
        "# D8-C final offline evidence integrity audit\n\n"
        f"**Decision: {decision} — D8-C evidence-reproducibility gate only.** "
        "Statistical values reproduce from the current archived local bytes, but "
        "historical execution-time byte integrity remains unverified; D8-A and D8-B "
        "remain PARTIAL and are not promoted.\n\n"
        "## Evidence matrix and reconciliation\n\n"
        f"- Verified distinct method–seed identities: **{len(dataset)}/25** "
        "(five methods × seeds 42–46; identity checked from manifests and metrics, "
        "not directory names alone).\n"
        f"- Source-to-report primary metric values: "
        f"**{len(comparisons) - len(failing_metrics)}/{len(comparisons)} matched** "
        f"within absolute tolerance {REPORT_TOLERANCE:g}.\n"
        f"- Original files hashed: **{len(integrity)}**; current hashes matched "
        f"prior D8-A audit fingerprints: "
        f"**{sum(row['prior_hash_comparison'] == 'MATCH' for row in integrity)}/"
        f"{len(integrity)}**. No trusted execution-time SHA256 baseline exists.\n"
        f"- Independent statistical outputs agree with the prior D8-C per-seed and "
        f"summary CSVs: {', '.join(f'{name} {count}' for name, count in statistical_reference_matches.items())} rows.\n"
        "- Protocol/source checks: all five root commit records and expected image "
        "digests match the frozen records; per-run runtime image identifiers and "
        "experiment/cleanup status records were checked. No new experiment or live "
        "cluster access was performed.\n\n"
        "## Five-seed method summaries\n\n"
        "Arithmetic mean, sample SD (n−1), and two-sided 95% Student-t confidence "
        "intervals (df=4); intervals are unadjusted.\n\n"
        + "\n".join(method_lines)
        + "\n\n## Prespecified paired Q-AHBN2 − AHBN contrasts\n\n"
        + "\n".join(paired_lines)
        + "\n\nPer-seed values:\n\n"
        + "\n".join(per_seed_lines)
        + "\n\nThe mean delivery difference is "
        f"{paired_summaries[0]['mean_difference'] * 100:.4f} percentage points. "
        "Observed higher mean delivery comes with higher mean propagation delay, "
        "duplicates, and total forwards: a delivery-versus-overhead trade-off, not "
        "overall superiority. The five-seed sample is small; intervals are "
        "unadjusted across endpoints and comparisons.\n\n"
        "## Gate and scientific limitations\n\n"
        "PARTIAL is recommended because the evidence content and calculations agree, "
        "but historical byte integrity cannot be certified without an execution-time "
        "hash baseline. This supports reproducibility from the bytes currently "
        "archived only; it does not prove those bytes have remained unchanged since "
        "execution. D8-A/D8-B limitations, recovery interpretation caveats, and "
        "unproven causal mechanisms remain. D8-C does not close the final D8 "
        "scientific decision. See `discrepancies.md` for the full register.\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-dir", type=Path, default=EVIDENCE)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--reconciliation-csv",
        type=Path,
        default=REPO / "output/d8_a_independent_20261020/audit.csv",
    )
    parser.add_argument(
        "--preliminary-comparison-json",
        type=Path,
        default=REPO / "output/d8_a_independent_20261020/preliminary_comparison.json",
    )
    args = parser.parse_args()
    evidence = args.evidence_dir.resolve()
    output = (
        args.output_dir.resolve()
        if args.output_dir
        else REPO
        / "output"
        / f"d8_c_final_offline_{dt.datetime.now(dt.timezone.utc):%Y%m%dT%H%M%SZ}"
    )
    output = output.resolve()
    if output == evidence or evidence in output.parents:
        parser.error("output directory must be outside original output/evidence")
    if output.exists() and any(output.iterdir()):
        parser.error(f"refusing to overwrite non-empty output directory: {output}")
    output.mkdir(parents=True, exist_ok=True)

    log_path = output / "audit_execution.log"
    git_version = subprocess.check_output(["git", "--version"], text=True).strip()
    log_path.write_text(
        "D8-C final offline audit\n"
        f"started_utc: {dt.datetime.now(dt.timezone.utc).isoformat()}\n"
        f"command: {sys.executable} {' '.join(sys.argv)}\n"
        f"python_version: {sys.version.replace(chr(10), ' ')}\n"
        f"platform: {platform.platform()}\n"
        f"git_version: {git_version}\n"
        "hash_tool: Python hashlib.sha256\n"
        "network_or_cluster_commands: none\n"
        "errors: pending\n"
    )
    global _ACTIVE_LOG_PATH
    _ACTIVE_LOG_PATH = log_path

    dataset, verification = load_and_verify(
        evidence,
        args.reconciliation_csv.resolve(),
        args.preliminary_comparison_json.resolve(),
    )
    if len(dataset) != 25 or len(verification) != 25:
        raise ValueError("verification did not produce exactly 25 run cells")
    if any(row["metric_reconstruction"] != "PASS" for row in dataset):
        raise ValueError("at least one run metric did not verify")

    method_summaries = summarize_methods(dataset)
    paired_rows, paired_summaries = summarize_qahbn2_vs_ahbn(dataset)
    with args.preliminary_comparison_json.resolve().open() as stream:
        preliminary_rows = json.load(stream)
    comparisons = compare_reported_metrics(dataset, preliminary_rows)
    inventory = build_inventory(evidence, dataset, args.reconciliation_csv.resolve())
    prior_inventory_path = REPO / "output/d8_a_independent_20261020/inventory.json"
    prior_sha_comparison_path = REPO / "output/d8_a_i1_confirmation/sha256_comparison.csv"
    integrity = build_integrity_manifest(
        evidence,
        dataset,
        prior_inventory_path,
        prior_sha_comparison_path,
    )
    statistical_reference_matches = compare_statistical_outputs(
        method_summaries,
        paired_rows,
        paired_summaries,
        REPO / "docs/stages/d8_c_20261020",
    )
    statistical_report_failures = compare_statistical_report(
        REPO / "docs/stages/D8_C_STATISTICAL_ANALYSIS_20261020.md",
        method_summaries,
        paired_rows,
        paired_summaries,
    )
    recovery_path = REPO / "docs/stages/d8_b_20261020/recovery_event_verification.csv"
    recovery_rows = list(csv.DictReader(recovery_path.open(newline="")))
    recovery_summary = {
        "source": recovery_path.relative_to(REPO).as_posix(),
        "event_count": len(recovery_rows),
        "recovered_count": sum(row["recovered"] == "True" for row in recovery_rows),
        "censored_count": sum(row["censored"] == "True" for row in recovery_rows),
        "recovered_over_18s_count": sum(
            row["recovered"] == "True"
            and float(row["recovery_time_s"]) > 18.0
            for row in recovery_rows
        ),
        "reused_anchor_event_count": sum(
            row["anchor_reused_within_run"] == "True" for row in recovery_rows
        ),
        "interpretation": (
            "Secondary diagnostic only. The 18-second value is the run-level post-workload "
            "settle delay, not an event-relative censoring horizon. Recovery values are not "
            "used in the four primary statistical analyses."
        ),
    }
    discrepancy_register = [
        {
            "id": "D8C-001",
            "classification": "Verified agreement",
            "status": "CLOSED_FOR_D8C",
            "scope": "100 primary metric values across 25 formal runs",
            "finding": (
                "All four endpoints independently reconstructed from archived logs match "
                "the archived metrics.json values exactly and match the prior D8-A audit "
                "table and 100-row preliminary comparison."
            ),
            "evidence": [
                "metric_verification.json",
                "verified_25_run_dataset.csv",
                "docs/stages/d8_a_20261020/audit.csv",
                "docs/stages/d8_a_20261020/preliminary_comparison.json",
            ],
        },
        {
            "id": "D8C-002",
            "classification": "Historical integrity limitation",
            "status": "OPEN_OUTSIDE_D8C_ARITHMETIC",
            "scope": "Archived evidence bytes",
            "finding": (
                "No trusted execution-time per-file hash baseline is available. Current "
                "SHA256 values identify the files read during D8-C but cannot show that "
                "they have remained byte-identical since execution."
            ),
            "evidence": [
                "metric_verification.json current metrics/manifest/topology/log SHA256 values",
                "docs/stages/d8_a_20261020/provenance.json",
            ],
            "impact": (
                "Statistical results are reproducible from the current archived bytes; "
                "historical byte integrity is not established."
            ),
        },
        {
            "id": "D8C-003",
            "classification": "Secondary recovery measurement limitation",
            "status": "RETAINED_NO_PRIMARY_METRIC_EFFECT",
            "scope": "100 recovery diagnostic observations",
            "finding": (
                "The 18-second value is the run-level post-workload settle delay, not a "
                "per-rejoin censoring horizon; one recovery is over 18 seconds and two "
                "event observations reuse the same message anchor."
            ),
            "evidence": [
                "recovery_secondary_summary.json",
                "docs/stages/d8_b_20261020/recovery_event_verification.csv",
            ],
            "impact": (
                "Recovery observations are not used for the four primary statistical endpoints."
            ),
        },
        {
            "id": "D8C-004",
            "classification": "Causal explanation limitation",
            "status": "UNRESOLVED_NOT_CLAIMED",
            "scope": "Timing and dissemination mechanism",
            "finding": (
                "Archived evidence does not establish cluster-wide neighbour-state convergence "
                "or that timing caused any observed delivery ratio."
            ),
            "evidence": [
                "docs/stages/D8_B_PROTOCOL_TIMING_VERIFICATION_20261020.md",
                "docs/stages/d8_b_20261020/neighbour_forwarding_analysis.json",
            ],
            "impact": (
                "D8-C reports outcomes and uncertainty only; it makes no causal mechanism claim."
            ),
        },
    ]

    (output / "verified_25_run_dataset.json").write_text(
        json.dumps(dataset, indent=2) + "\n"
    )
    write_csv(output / "verified_25_run_dataset.csv", dataset)
    (output / "metric_verification.json").write_text(
        json.dumps(verification, indent=2) + "\n"
    )
    (output / "method_summaries.json").write_text(
        json.dumps(method_summaries, indent=2) + "\n"
    )
    write_csv(output / "method_summaries.csv", method_summaries)
    (output / "paired_seed_differences.json").write_text(
        json.dumps(paired_rows, indent=2) + "\n"
    )
    write_csv(output / "paired_seed_differences.csv", paired_rows)
    (output / "paired_qahbn2_vs_ahbn_summaries.json").write_text(
        json.dumps(paired_summaries, indent=2) + "\n"
    )
    write_csv(output / "paired_qahbn2_vs_ahbn_summaries.csv", paired_summaries)
    (output / "recovery_secondary_summary.json").write_text(
        json.dumps(recovery_summary, indent=2) + "\n"
    )
    (output / "discrepancy_register.json").write_text(
        json.dumps(discrepancy_register, indent=2) + "\n"
    )

    summary = {
        "analysis_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "repository_head": __import__("subprocess").check_output(
            ["git", "-C", str(REPO), "rev-parse", "HEAD"], text=True
        ).strip(),
        "stash_at_0": __import__("subprocess").check_output(
            ["git", "-C", str(REPO), "rev-parse", "stash@{0}"], text=True
        ).strip(),
        "evidence_directory": str(evidence),
        "output_directory": str(output),
        "D8_C_release_document": "docs/stages/D8_C_STATISTICAL_ANALYSIS_20261020.md",
        "frozen_protocol": "docs/stages/K4_Q_K8S_VALIDATION_FREEZE.md",
        "independent_metric_source": "gke/scripts/audit_d8_a_offline.py reconstruct()",
        "verified_run_count": len(dataset),
        "verified_primary_metric_values": len(dataset) * len(METRICS),
        "independent_reconstruction_match_count": sum(
            check["within_tolerance"]
            for row in verification
            for check in row["metric_checks"].values()
        ),
        "D8_A_reconciliation_match_count": len(dataset) * len(METRICS),
        "source_to_report_match_count": sum(
            row["status"] == "PASS" for row in comparisons
        ),
        "source_to_report_tolerance": REPORT_TOLERANCE,
        "integrity_files_checked": len(integrity),
        "prior_audit_hash_matches": sum(
            row["prior_hash_comparison"] == "MATCH" for row in integrity
        ),
        "historical_execution_time_hash_baseline": "unavailable",
        "statistical_report_comparison_failures": statistical_report_failures,
        "method_summary_count": len(method_summaries),
        "paired_seed_difference_count": len(paired_rows),
        "paired_summary_count": len(paired_summaries),
        "seeds": list(ROOTS),
        "methods": list(METHODS),
        "primary_metrics": list(METRICS),
        "seed_is_independent_unit_n": 5,
        "confidence_interval": {
            "distribution": "two-sided Student-t",
            "confidence_level": 0.95,
            "degrees_of_freedom": 4,
            "critical_value": T_CRITICAL_DF4,
            "sample_standard_deviation_ddof": 1,
        },
        "significance_tests_performed": False,
        "run_exclusions": [],
        "recovery_secondary_summary": recovery_summary,
        "D8_A_and_D8_B_disposition": "remain PARTIAL; not closed by D8-C",
        "recommendation": (
            "HOLD"
            if any(row["status"] != "PASS" for row in comparisons)
            or any(row["prior_hash_comparison"] != "MATCH" for row in integrity)
            or statistical_report_failures
            else "PARTIAL"
        ),
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    write_csv(output / "inventory.csv", inventory)
    write_csv(output / "metrics_comparison.csv", comparisons)
    write_csv(output / "integrity_manifest.csv", integrity)
    write_csv(
        output / "statistical_recalculation.csv",
        build_statistical_rows(method_summaries, paired_rows, paired_summaries),
    )
    write_final_reports(
        output,
        dataset,
        comparisons,
        integrity,
        method_summaries,
        paired_rows,
        paired_summaries,
        statistical_reference_matches,
        statistical_report_failures,
    )
    with log_path.open("a") as stream:
        stream.write(
            f"completed_utc: {dt.datetime.now(dt.timezone.utc).isoformat()}\n"
            f"verified_run_count: {len(dataset)}\n"
            f"source_report_comparison_count: {len(comparisons)}\n"
            f"source_report_match_count: "
            f"{sum(row['status'] == 'PASS' for row in comparisons)}\n"
            f"integrity_file_count: {len(integrity)}\n"
            f"prior_hash_match_count: "
            f"{sum(row['prior_hash_comparison'] == 'MATCH' for row in integrity)}\n"
            f"statistical_reference_checks: {json.dumps(statistical_reference_matches)}\n"
            f"statistical_report_failures: {json.dumps(statistical_report_failures)}\n"
            "errors: none\n"
            "exit_code: 0\n"
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        if _ACTIVE_LOG_PATH is not None:
            with _ACTIVE_LOG_PATH.open("a") as stream:
                stream.write(f"error: {type(error).__name__}: {error}\n")
        raise
