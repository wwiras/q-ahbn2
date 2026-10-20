#!/usr/bin/env python3
"""Read-only D8-B protocol and timing audit for the archived K5-Q evidence."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
FORMAL_ROOTS = {
    42: "20261020T032934Z-K5Q-formal",
    43: "20261020T035637Z-K5Q-formal",
    44: "20261020T041621Z-K5Q-formal",
    45: "20261020T043745Z-K5Q-formal",
    46: "20261020T045636Z-K5Q-formal",
}
METHODS = ("gossip", "structured", "dcsoc", "ahbn", "qahbn2")
EXPECTED_COMMIT = "6433f7429e0342df44c272b236423c65203a9136"
EXPECTED_IMAGE = (
    "sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228"
    "cd1575dde1c1488f"
)
EXPECTED_TARGETS = [0, 5, 10, 15]
EXPECTED_OFFSETS = [1.0, 26.0, 51.0, 76.0]
MESSAGE_COUNT = 240
MESSAGE_INTERVAL = 0.4


def read_json(path: Path):
    return json.loads(path.read_text())


def read_records(path: Path) -> tuple[list[dict], int]:
    """Read newline or concatenated JSON objects and discard exact duplicates."""
    records = []
    seen = set()
    duplicates = 0
    decoder = json.JSONDecoder()
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        pending = line.strip()
        while pending:
            try:
                record, end = decoder.raw_decode(pending)
            except ValueError as error:
                raise ValueError(f"{path}:{line_number}: malformed JSON") from error
            key = json.dumps(record, sort_keys=True, separators=(",", ":"))
            if key in seen:
                duplicates += 1
            else:
                seen.add(key)
                records.append(record)
            pending = pending[end:].lstrip()
    return records, duplicates


def event_rows(rows: list[dict], name: str) -> list[dict]:
    return [row for row in rows if row.get("event") == name]


def unique_by_event_index(rows: list[dict], name: str) -> list[dict]:
    selected = event_rows(rows, name)
    indexed = {}
    for row in selected:
        index = int(row["event_index"])
        if index in indexed:
            raise ValueError(f"duplicate {name} event_index={index}")
        indexed[index] = row
    if sorted(indexed) != [1, 2, 3, 4]:
        raise ValueError(f"{name} event indices are {sorted(indexed)}, expected 1..4")
    return [indexed[index] for index in range(1, 5)]


def active_peers_at(ts: float, node_count: int, rows: list[dict]) -> set[int]:
    active = set(range(node_count))
    changes = []
    for row in event_rows(rows, "pod_unavailability_observed"):
        changes.append((float(row["ts"]), int(row["target_peer"]), False))
    for row in event_rows(rows, "churn_rejoined"):
        changes.append((float(row["ts"]), int(row["target_peer"]), True))
    for changed_at, peer, available in sorted(changes):
        if changed_at > ts:
            break
        if available:
            active.add(peer)
        else:
            active.discard(peer)
    return active


def recovery_observations(
    rows: list[dict], topology: dict, expected_count: int = MESSAGE_COUNT
) -> list[dict]:
    injections = sorted(
        event_rows(rows, "message_injected"), key=lambda row: float(row["ts"])
    )
    if len(injections) != expected_count:
        raise ValueError(
            f"expected {expected_count} unique source injections, found {len(injections)}"
        )
    arrivals = defaultdict(list)
    for row in event_rows(rows, "received_new"):
        arrivals[str(row["message_id"])].append(row)

    opportunities = []
    for injection in injections:
        message_id = str(injection["message_id"])
        active = active_peers_at(float(injection["ts"]), topology["num_nodes"], rows)
        received = arrivals[message_id]
        received_peers = {int(row["peer_id"]) for row in received}
        eligible = [row for row in received if int(row["peer_id"]) in active]
        complete = active.issubset(received_peers)
        opportunities.append(
            {
                "message_id": message_id,
                "injected_ts": float(injection["ts"]),
                "active_peers": active,
                "full_delivery": complete,
                "completion_ts": max((float(row["ts"]) for row in eligible), default=None)
                if complete
                else None,
            }
        )

    leaves = unique_by_event_index(rows, "churn_leave_scheduled")
    joins = unique_by_event_index(rows, "churn_rejoined")
    output = []
    for join in joins:
        joined_at = float(join["ts"])
        later_opportunities = [
            opportunity
            for opportunity in opportunities
            if opportunity["injected_ts"] >= joined_at
        ]
        candidates = [
            opportunity
            for opportunity in later_opportunities
            if opportunity["full_delivery"]
        ]
        first = candidates[0] if candidates else None
        intervening = [
            leave
            for leave in leaves
            if joined_at < float(leave["ts"])
            and first is not None
            and float(leave["ts"]) <= first["injected_ts"]
        ]
        output.append(
            {
                "event_index": int(join["event_index"]),
                "target_peer": int(join["target_peer"]),
                "join_ts": joined_at,
                "recovered": first is not None,
                "recovery_time_s": (
                    float(first["completion_ts"]) - joined_at if first is not None else None
                ),
                "recovery_message_id": first["message_id"] if first is not None else None,
                "recovery_injection_ts": first["injected_ts"] if first is not None else None,
                "censored": first is None,
                "censored_at_s": topology["settle_time"] if first is None else None,
                "last_injection_ts": opportunities[-1]["injected_ts"],
                "later_injection_opportunity_span_s": opportunities[-1]["injected_ts"] - joined_at,
                "post_join_injection_opportunity_count": len(later_opportunities),
                "censor_value_basis": (
                    "run-level post-workload settle_time; not elapsed time from this rejoin"
                ),
                "intervening_leave_event_indices": [
                    int(leave["event_index"]) for leave in intervening
                ],
                "search_is_bounded_by_censor_value": False,
            }
        )
    anchor_counts = Counter(
        row["recovery_message_id"] for row in output if row["recovered"]
    )
    for row in output:
        row["anchor_reused_within_run"] = bool(
            row["recovery_message_id"]
            and anchor_counts[row["recovery_message_id"]] > 1
        )
    return output


def close(left: float, right: float, tolerance: float = 1e-9) -> bool:
    return abs(float(left) - float(right)) <= tolerance


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_hash(value: dict) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def audit_run(evidence: Path, seed: int, method: str, validator_passes: int):
    root = evidence / FORMAL_ROOTS[seed]
    run = root / "runs" / f"seed{seed}" / method
    manifest = read_json(run / "run_manifest.json")
    topology = read_json(run / "topology.json")
    metrics = read_json(run / "metrics.json")
    rows, duplicate_records = read_records(run / "logs.jsonl")
    controller_rows, _ = read_records(run / "controller.log")
    all_events = Counter(row.get("event") for row in rows)
    issues = []

    def require(condition: bool, message: str):
        if not condition:
            issues.append(message)

    epoch = float(manifest["experiment_epoch"])
    epoch_rows = event_rows(rows, "k7_experiment_epoch")
    require(len(epoch_rows) == 1, "one common epoch record")
    if len(epoch_rows) == 1:
        require(close(epoch_rows[0]["experiment_epoch"], epoch), "manifest/log epoch parity")

    injections = sorted(
        event_rows(rows, "k7_message_injection"),
        key=lambda row: int(str(row["msg_id"])[1:]),
    )
    require(len(injections) == MESSAGE_COUNT, "240 controller injection records")
    injection_ids = [
        int(str(row["msg_id"])[1:])
        for row in injections
        if str(row.get("msg_id", "")).startswith("m")
        and str(row.get("msg_id", ""))[1:].isdigit()
    ]
    require(injection_ids == list(range(1, MESSAGE_COUNT + 1)),
            "controller message identifiers m1..m240 exactly once")
    injection_grid_errors = []
    injection_lateness = []
    injection_ack = True
    injection_schedule = []
    for index, injection in enumerate(injections, 1):
        planned = epoch + (index - 1) * MESSAGE_INTERVAL
        grid_error = float(injection["planned_injection_ts"]) - planned
        injection_grid_errors.append(abs(grid_error))
        computed_lateness = max(
            0.0,
            (float(injection["actual_injection_start_ts"]) - float(injection["planned_injection_ts"]))
            * 1000.0,
        )
        injection_lateness.append(computed_lateness)
        injection_schedule.append(
            {
                "seed": seed,
                "method": method,
                "run_id": metrics["run_id"],
                "message_id": injection["msg_id"],
                "planned_offset_s": planned - epoch,
                "planned_injection_ts": float(injection["planned_injection_ts"]),
                "actual_start_offset_s": float(injection["actual_injection_start_ts"]) - epoch,
                "actual_injection_start_ts": float(injection["actual_injection_start_ts"]),
                "actual_injection_end_ts": float(injection["actual_injection_end_ts"]),
                "planned_grid_error_s": grid_error,
                "actual_start_lateness_ms": computed_lateness,
                "start_run_elapsed_ms": float(injection["start_run_elapsed_ms"]),
                "injection_status": injection["injection_status"],
            }
        )
        injection_ack &= injection.get("injection_status") == "ACK"
        require(
            close(computed_lateness, injection["injection_lateness_ms"], 1e-6),
            f"{injection.get('msg_id')} recorded lateness matches actual-start minus planned",
        )
        require(
            close(
                float(injection["actual_injection_end_ts"])
                - float(injection["actual_injection_start_ts"]),
                float(injection["start_run_elapsed_ms"]) / 1000.0,
                1e-5,
            ),
            f"{injection.get('msg_id')} StartRun elapsed duration parity",
        )

    schedule = topology["k7_exp11"]["planned_churn_schedule"]
    targets = [int(row["target_peer"]) for row in schedule]
    offsets = [float(row["planned_leave_offset_s"]) for row in schedule]
    require(int(manifest["seed"]) == seed and manifest["algorithm"] == method, "manifest seed/method")
    require(metrics.get("seed") == seed and metrics.get("algorithm") == method,
            "metrics seed/method")
    require(metrics.get("run_id") == f"k7_exp11_{method}_seed{seed}", "metrics run identity")
    require(topology["num_nodes"] == 20, "N=20")
    require(topology["topology_type"] == "ba" and topology["ba_m"] == 2, "BA(m=2)")
    require(topology["seed"] == seed, "topology seed")
    require(manifest["message_count"] == MESSAGE_COUNT, "240-message manifest")
    require(close(manifest["message_interval"], MESSAGE_INTERVAL), "0.4-second manifest interval")
    require(topology["workload"] == {"message_count": MESSAGE_COUNT, "message_interval": MESSAGE_INTERVAL},
            "topology workload")
    require(offsets == EXPECTED_OFFSETS, "frozen leave offsets")
    require(targets == EXPECTED_TARGETS, "frozen target schedule")
    require(manifest["frozen_targets"] == EXPECTED_TARGETS, "frozen target manifest")
    target_artifact = read_json(root / "target-selection" / f"seed{seed}.json")
    computed_target_hash = canonical_hash(
        {key: value for key, value in target_artifact.items() if key != "selection_hash"}
    )
    require(target_artifact.get("seed") == seed, "target-selection seed")
    require(target_artifact.get("frozen_targets") == EXPECTED_TARGETS, "target-selection targets")
    require(target_artifact.get("selection_hash") == computed_target_hash,
            "target-selection artifact hash")
    require(manifest.get("target_selection_hash") == computed_target_hash,
            "manifest target-selection hash")
    require(topology.get("message_source") not in EXPECTED_TARGETS, "source is not a churn target")
    expected_strategy = "cluster" if method == "structured" else method
    require(topology.get("strategy") == expected_strategy, "method strategy")
    require(topology["k7_exp11"].get("algorithm") == method, "topology method identity")
    require(bool(topology["dcsoc"].get("dynamic_maintenance")) == (method == "dcsoc"),
            "DC-SoC maintenance isolation")

    leaves = unique_by_event_index(rows, "churn_leave_scheduled")
    downs = unique_by_event_index(rows, "pod_unavailability_observed")
    joins = unique_by_event_index(rows, "churn_rejoined")
    churn_lateness_ms = []
    churn_abs_dispatch_error_ms = []
    churn_rows = []
    for index, (plan, leave, down, join) in enumerate(zip(schedule, leaves, downs, joins), 1):
        planned = epoch + offsets[index - 1]
        actual_start = float(leave["actual_churn_start_ts"])
        signed_dispatch_error = (actual_start - planned) * 1000.0
        lateness = max(0.0, (actual_start - planned) * 1000.0)
        churn_lateness_ms.append(lateness)
        churn_abs_dispatch_error_ms.append(abs(signed_dispatch_error))
        require(
            close(lateness, leave.get("churn_lateness_ms", lateness), 1e-5),
            f"event {index} logged churn lateness",
        )
        require(abs(signed_dispatch_error) <= 500.0, f"event {index} within 0.5s dispatch tolerance")
        require(int(leave["target_peer"]) == targets[index - 1], f"event {index} leave target")
        require(int(down["target_peer"]) == targets[index - 1], f"event {index} unavailable target")
        require(int(join["target_peer"]) == targets[index - 1], f"event {index} rejoin target")
        require(close(float(leave["planned_leave_time"]), planned), f"event {index} planned leave epoch")
        require(close(float(leave["planned_churn_ts"]), planned), f"event {index} planned churn epoch")
        require(
            float(leave["ts"]) <= float(down["ts"]) <= float(join["recovery_ready_time"])
            <= float(join["grpc_alive_time"]) <= float(join["ts"]),
            f"event {index} leave/down/Ready/gRPC/rejoin ordering",
        )
        require(join.get("event_status") == "COMPLETE", f"event {index} rejoin completion")
        replacement_uid = next(
            (
                row
                for row in event_rows(rows, "replacement_uid_observed")
                if int(row.get("event_index", -1)) == index
            ),
            None,
        )
        require(replacement_uid is not None, f"event {index} replacement UID observed")
        if replacement_uid is not None:
            require(
                replacement_uid.get("replacement_pod_uid") == join.get("replacement_pod_uid"),
                f"event {index} replacement UID identity",
            )
        churn_rows.append(
            {
                "event_index": index,
                "target_peer": targets[index - 1],
                "planned_leave_ts": planned,
                "actual_leave_dispatch_ts": actual_start,
                "dispatch_lateness_ms": lateness,
                "signed_dispatch_error_ms": signed_dispatch_error,
                "previous_event_still_unavailable_at_dispatch": (
                    index > 1 and float(joins[index - 2]["ts"]) > actual_start
                ),
                "pod_unavailable_ts": float(down["ts"]),
                "replacement_uid_observed_ts": next(
                    (
                        float(row["ts"])
                        for row in event_rows(rows, "replacement_uid_observed")
                        if int(row.get("event_index", -1)) == index
                    ),
                    None,
                ),
                "pod_ready_ts": float(join["ready_ts"]),
                "grpc_alive_ts": float(join["grpc_alive_time"]),
                "rejoin_event_ts": float(join["ts"]),
                "ready_latency_from_unavailable_s": float(join["ready_ts"])
                - float(down["ts"]),
                "grpc_latency_from_unavailable_s": float(join["grpc_alive_time"])
                - float(down["ts"]),
            }
        )

    source_commit = (root / "git_commit.txt").read_text().strip()
    expected_image = (root / "expected_image_digest.txt").read_text().strip()
    pods = read_json(run / "pods.json").get("items", [])
    runtime_ids = sorted(
        {
            container.get("imageID")
            for pod in pods
            for container in pod.get("status", {}).get("containerStatuses", [])
            if container.get("imageID")
        }
    )
    require(source_commit == EXPECTED_COMMIT, "recorded source commit")
    require(expected_image == EXPECTED_IMAGE, "recorded expected image digest")
    require(len(pods) == 20, "20 peer pod snapshots")
    require(
        len(runtime_ids) == 1
        and runtime_ids[0].endswith(EXPECTED_IMAGE)
        and len(
            [
                container.get("imageID")
                for pod in pods
                for container in pod.get("status", {}).get("containerStatuses", [])
                if container.get("imageID")
            ]
        )
        == 20,
        "runtime imageID matches immutable expected digest",
    )
    require(
        all(
            container.get("ready") is True
            for pod in pods
            for container in pod.get("status", {}).get("containerStatuses", [])
        ),
        "final snapshot containers Ready",
    )
    status_names = (
        "experiment_exit_status.txt",
        "cleanup_exit_status.txt",
        "namespace_cleanup_exit_status.txt",
        "helm_cleanup_exit_status.txt",
        "cleanup_status.txt",
    )
    statuses = {name: (run / name).read_text().strip() for name in status_names}
    require(statuses["experiment_exit_status.txt"] == "0", "experiment exit status 0")
    require(statuses["cleanup_exit_status.txt"] == "0", "cleanup exit status 0")
    require(statuses["namespace_cleanup_exit_status.txt"] == "0", "namespace cleanup exit 0")
    require(statuses["helm_cleanup_exit_status.txt"] == "0", "Helm cleanup exit 0")
    require(statuses["cleanup_status.txt"] == "PASS", "cleanup PASS")
    controller_pods = read_json(run / "controller_pods.json").get("items", [])
    require(
        [pod.get("status", {}).get("phase") for pod in controller_pods] == ["Succeeded"],
        "controller pod Succeeded",
    )
    require(validator_passes == 5, "five method validator PASS records at seed level")

    recovery = recovery_observations(rows, topology)
    observed_recovery = metrics["recovery_events"]
    require(len(observed_recovery) == 4, "four recovery metric rows")
    for computed, recorded in zip(recovery, observed_recovery):
        require(
            computed["event_index"] == recorded["event_index"]
            and computed["recovery_message_id"] == recorded["recovery_message_id"]
            and computed["recovered"] == recorded["recovered"]
            and computed["censored"] == recorded["censored"]
            and computed["censored_at_s"] == recorded["censored_at_s"]
            and (
                computed["recovery_time_s"] is None
                and recorded["recovery_time_s"] is None
                or computed["recovery_time_s"] is not None
                and close(computed["recovery_time_s"], recorded["recovery_time_s"])
            ),
            f"recovery event {computed['event_index']} independently matches metrics",
        )

    run_finished = event_rows(rows, "run_finished")
    require(len(run_finished) == 1, "one run_finished record")
    last_actual_end = max(float(row["actual_injection_end_ts"]) for row in injections)
    if run_finished:
        require(float(run_finished[-1]["ts"]) >= last_actual_end, "run finished after final injection")
    log_end = max((float(row["ts"]) for row in rows if "ts" in row), default=None)
    return {
        "seed": seed,
        "method": method,
        "run_id": metrics["run_id"],
        "evidence_path": run.relative_to(evidence).as_posix(),
        "topology": "Barabasi-Albert",
        "network_size": topology["num_nodes"],
        "ba_m": topology["ba_m"],
        "message_count": manifest["message_count"],
        "planned_interval_s": manifest["message_interval"],
        "common_epoch": epoch,
        "planned_grid_max_abs_error_s": max(injection_grid_errors, default=None),
        "planned_grid_max_gap_error_s": max(
            (
                abs(
                    float(b["planned_injection_ts"])
                    - float(a["planned_injection_ts"])
                    - MESSAGE_INTERVAL
                )
                for a, b in zip(injections, injections[1:])
            ),
            default=None,
        ),
        "max_actual_injection_lateness_ms": max(injection_lateness, default=None),
        "injection_lateness_definition": "max(0, actual StartRun call start - planned grid point)",
        "injections_acknowledged": injection_ack,
        "planned_churn_offsets_s": offsets,
        "churn_targets": targets,
        "max_churn_dispatch_lateness_ms": max(churn_lateness_ms, default=None),
        "max_abs_churn_dispatch_error_ms": max(churn_abs_dispatch_error_ms, default=None),
        "churn_events": churn_rows,
        "runtime_recovery_probe_event_count": sum(
            1 for row in rows if row.get("event") == "recovery_probe"
        ),
        "recovery_observations": recovery,
        "_injection_schedule": injection_schedule,
        "last_actual_injection_end_ts": last_actual_end,
        "run_finished_ts": float(run_finished[-1]["ts"]) if run_finished else None,
        "configured_settle_time_s": float(topology["settle_time"]),
        "post_workload_settle_observed_s": (
            float(run_finished[-1]["ts"]) - last_actual_end if run_finished else None
        ),
        "last_log_event_ts": log_end,
        "delivery_ratio": metrics["delivery_ratio"],
        "propagation_delay": metrics["propagation_delay"],
        "duplicates": metrics["duplicates"],
        "total_forwards": metrics["total_forwards"],
        "F_attempt": metrics["F_attempt"],
        "F_success": metrics["F_success"],
        "message_source": topology["message_source"],
        "target_selection_hash": manifest["target_selection_hash"],
        "target_selection_hash_valid": target_artifact.get("selection_hash") == computed_target_hash,
        "method_strategy": topology["strategy"],
        "dcsoc_dynamic_maintenance": topology["dcsoc"]["dynamic_maintenance"],
        "source_commit": source_commit,
        "expected_image_digest": expected_image,
        "runtime_image_ids": runtime_ids,
        "validator_passes_for_seed": validator_passes,
        "exit_and_cleanup_status": statuses,
        "controller_pod_phases": [
            pod.get("status", {}).get("phase") for pod in controller_pods
        ],
        "exact_duplicate_records_removed": duplicate_records,
        "protocol_check": "PASS" if not issues else "REVIEW",
        "protocol_issues": issues,
        "_rows": rows,
        "_controller_rows": controller_rows,
        "_topology": topology,
    }


def forwarding_summary(run: dict) -> dict:
    rows = run["_rows"]
    topology = run["_topology"]
    leaves = unique_by_event_index(rows, "churn_leave_scheduled")
    joins = unique_by_event_index(rows, "churn_rejoined")
    outcome_events = (
        "forward",
        "forward_failed",
        "forward_duplicate_ack",
    )
    outcomes = defaultdict(list)
    for event_name in outcome_events:
        for row in event_rows(rows, event_name):
            key = (
                str(row.get("message_id", row.get("msg_id", ""))),
                int(row.get("peer_id", -1)),
                int(row.get("dst_peer", -1)),
            )
            outcomes[key].append(row)
    summaries = []
    representative_timelines = []
    for leave, join in zip(leaves, joins):
        target = int(join["target_peer"])
        joined_at = float(join["ts"])
        peer_availability = [
            row
            for row in event_rows(rows, "peer_availability")
            if int(row.get("target", -1)) == target and float(row["ts"]) >= joined_at
        ]
        attempts = [
            row
            for row in event_rows(rows, "k7_forward_attempt")
            if float(row["ts"]) >= joined_at
            and (
                int(row.get("sender", -1)) == target
                or int(row.get("destination_peer", -1)) == target
            )
        ]
        receipts = [
            row
            for row in event_rows(rows, "received_new")
            if int(row.get("peer_id", -1)) == target and float(row["ts"]) >= joined_at
        ]
        attempt_records = []
        for attempt in sorted(attempts, key=lambda row: float(row["ts"])):
            key = (
                str(attempt.get("message_id", attempt.get("msg_id", ""))),
                int(attempt.get("sender", -1)),
                int(attempt.get("destination_peer", -1)),
            )
            matching = sorted(
                (
                    result
                    for result in outcomes.get(key, [])
                    if float(result["ts"]) >= float(attempt["ts"])
                ),
                key=lambda row: float(row["ts"]),
            )
            result = matching[0] if matching else None
            attempt_records.append(
                {
                    "event": "k7_forward_attempt",
                    "ts": float(attempt["ts"]),
                    "message_id": key[0],
                    "sender": key[1],
                    "destination_peer": key[2],
                    "outcome": result.get("event") if result else "no_matching_outcome_record",
                    "outcome_ts": float(result["ts"]) if result else None,
                }
            )
        availability_records = [
            {
                "event": "peer_availability",
                "ts": float(row["ts"]),
                "reporting_peer_id": int(row.get("peer_id", -1)),
                "target_peer": target,
                "unavailable": row.get("unavailable"),
                "changed": row.get("changed"),
                "reason": row.get("reason"),
            }
            for row in peer_availability
        ]
        lifecycle = [
            {
                "event": "churn_leave_scheduled",
                "ts": float(leave["actual_churn_start_ts"]),
                "planned_ts": float(leave["planned_leave_time"]),
            },
            {
                "event": "pod_unavailability_observed",
                "ts": float(
                    next(
                        row["ts"]
                        for row in event_rows(rows, "pod_unavailability_observed")
                        if int(row["event_index"]) == int(join["event_index"])
                    )
                ),
            },
            {
                "event": "replacement_pod_ready",
                "ts": float(join["ready_ts"]),
                "replacement_pod_uid": join.get("replacement_pod_uid"),
            },
            {
                "event": "controller_grpc_alive",
                "ts": float(join["grpc_alive_time"]),
            },
            {
                "event": "churn_rejoined",
                "ts": float(join["ts"]),
            },
        ]
        timeline = lifecycle + availability_records + attempt_records
        timeline.extend(
            {
                "event": "received_new",
                "ts": float(row["ts"]),
                "message_id": row["message_id"],
                "peer_id": target,
                "source_peer": row.get("src_peer"),
            }
            for row in receipts
        )
        representative_timelines.append(
            {
                "event_index": int(join["event_index"]),
                "target_peer": target,
                "events": sorted(timeline, key=lambda row: row["ts"]),
            }
        )
        summaries.append(
            {
                "event_index": int(join["event_index"]),
                "target_peer": target,
                "leave_dispatch_ts": float(leave["actual_churn_start_ts"]),
                "unavailable_ts": float(
                    next(
                        row["ts"]
                        for row in event_rows(rows, "pod_unavailability_observed")
                        if int(row["event_index"]) == int(join["event_index"])
                    )
                ),
                "replacement_ready_ts": float(join["ready_ts"]),
                "controller_grpc_alive_ts": float(join["grpc_alive_time"]),
                "rejoin_log_ts": joined_at,
                "local_peer_availability_updates_after_rejoin": len(peer_availability),
                "first_local_availability_update_ts": min(
                    (float(row["ts"]) for row in peer_availability), default=None
                ),
                "local_availability_changed_true": sum(
                    bool(row.get("changed")) for row in peer_availability
                ),
                "local_availability_states": sorted(
                    {
                        bool(row["unavailable"])
                        for row in peer_availability
                        if "unavailable" in row
                    }
                ),
                "forward_attempts_to_or_from_target_after_rejoin": len(attempts),
                "first_forward_attempt_ts": min(
                    (float(row["ts"]) for row in attempts), default=None
                ),
                "last_forward_attempt_ts": max(
                    (float(row["ts"]) for row in attempts), default=None
                ),
                "new_message_deliveries_to_target_after_rejoin": len(receipts),
                "first_new_delivery_ts": min(
                    (float(row["ts"]) for row in receipts), default=None
                ),
                "forward_attempt_outcome_counts": dict(
                    Counter(row["outcome"] for row in attempt_records)
                ),
            }
        )
    m77_injections = [
        row
        for row in event_rows(rows, "message_injected")
        if row.get("message_id") == "m77"
    ]
    message_77 = None
    if m77_injections:
        injection = m77_injections[0]
        active = active_peers_at(
            float(injection["ts"]), topology["num_nodes"], rows
        )
        receipts = [
            row
            for row in event_rows(rows, "received_new")
            if row.get("message_id") == "m77"
        ]
        delivered = {
            int(row["peer_id"]) for row in receipts if int(row["peer_id"]) in active
        }
        message_77 = {
            "message_id": "m77",
            "injection_ts": float(injection["ts"]),
            "active_peer_count_at_injection": len(active),
            "active_peers_receiving_new_message": len(delivered),
            "full_delivery_to_active_peers": active.issubset(delivered),
            "last_eligible_receipt_ts": max(
                (
                    float(row["ts"])
                    for row in receipts
                    if int(row["peer_id"]) in active
                ),
                default=None,
            ),
            "recovery_event_anchors": [
                recovery
                for recovery in run["recovery_observations"]
                if recovery["recovery_message_id"] == "m77"
            ],
        }
    return {
        "seed": run["seed"],
        "method": run["method"],
        "delivery_ratio": run["delivery_ratio"],
        "event_summaries": summaries,
        "timestamped_event_sequences": representative_timelines,
        "message_77_recovery_anchor_check": message_77,
        "explicit_neighbour_membership_transition_events": sum(
            1
            for row in rows
            if any(token in str(row.get("event", "")).lower() for token in ("neighbor_add", "neighbor_remove", "neighbour"))
        ),
        "initial_neighbour_topology_available": bool(topology.get("nodes")),
        "limitations": [
            "peer_availability is a local per-peer unavailable-cache observation, not a cluster-wide neighbour-membership acknowledgement",
            "controller gRPC GetStatus success is not a proof that every peer can route to the replacement",
            "forward attempts are opportunities; only separate outcomes or received_new records show success",
            "no recorded clock-synchronization error bounds cross-pod timestamp ordering",
        ],
    }


def write_csv(path: Path, rows: list[dict], fields: list[str] | None = None):
    if fields is None:
        fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-dir", type=Path, default=REPO / "output/evidence")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    evidence = args.evidence_dir.resolve()
    output = args.output_dir.resolve()
    if output == evidence or evidence in output.parents:
        parser.error("output directory must be outside the original evidence tree")
    output.mkdir(parents=True, exist_ok=True)

    runs = []
    for seed, root_name in FORMAL_ROOTS.items():
        terminal = (evidence / root_name / "terminal.log").read_text()
        validator_passes = terminal.count("K7 RESULT VALIDATION PASS")
        for method in METHODS:
            runs.append(audit_run(evidence, seed, method, validator_passes))

    for seed in FORMAL_ROOTS:
        same_seed = [run for run in runs if run["seed"] == seed]
        topology_identity = {
            json.dumps(
                {
                    "source": run["_topology"]["message_source"],
                    "adjacency": {
                        peer: value.get("neighbors")
                        for peer, value in run["_topology"]["nodes"].items()
                    },
                    "target_selection_hash": run["target_selection_hash"],
                    "targets": run["churn_targets"],
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            for run in same_seed
        }
        if len(topology_identity) != 1:
            for run in same_seed:
                run["protocol_issues"].append(
                    "within-seed methods do not share topology, source, or target selection"
                )
                run["protocol_check"] = "REVIEW"

    matrix = []
    recoveries = []
    for run in runs:
        matrix.append(
            {
                key: value
                for key, value in run.items()
                if not key.startswith("_") and key != "recovery_observations"
            }
        )
        for recovery in run["recovery_observations"]:
            recoveries.append(
                {
                    "seed": run["seed"],
                    "method": run["method"],
                    "run_id": run["run_id"],
                    "evidence_path": run["evidence_path"],
                    **recovery,
                }
            )

    anchor_counts = Counter(
        (row["seed"], row["method"], row["recovery_message_id"])
        for row in recoveries
        if row["recovered"]
    )
    for row in recoveries:
        row["anchor_reuse_count_in_run"] = (
            anchor_counts[(row["seed"], row["method"], row["recovery_message_id"])]
            if row["recovery_message_id"]
            else 0
        )
    forwarding = [
        forwarding_summary(run)
        for run in runs
    ]
    forwarding_by_method = []
    for method in METHODS:
        events = [
            event
            for item in forwarding
            if item["method"] == method
            for event in item["event_summaries"]
        ]
        method_runs = [run for run in runs if run["method"] == method]
        forwarding_by_method.append(
            {
                "method": method,
                "mean_observed_delivery_ratio": sum(
                    run["delivery_ratio"] for run in method_runs
                )
                / len(method_runs),
                "rejoins_with_local_peer_availability_updates": sum(
                    bool(event["local_peer_availability_updates_after_rejoin"])
                    for event in events
                ),
                "rejoins_with_forward_attempts": sum(
                    bool(event["forward_attempts_to_or_from_target_after_rejoin"])
                    for event in events
                ),
                "rejoins_with_new_delivery_to_target": sum(
                    bool(event["new_message_deliveries_to_target_after_rejoin"])
                    for event in events
                ),
            }
        )
    representative = [
        item for item in forwarding
        if item["seed"] == 44 and item["method"] in {"gossip", "structured"}
    ]
    issue_register = [
        {
            "id": "D8B-001",
            "classification": "Measurement-definition inconsistency",
            "scope": "100 recovery-event observations",
            "finding": (
                "The code searches all later full-delivery opportunities without an 18-second "
                "cutoff and assigns 18 seconds only when no opportunity is found."
            ),
            "evidence": [
                "gke/app/k7_exp11_tools.py:373-376",
                "gke/app/controller_shared.py:794",
                "gke/experiments/k5_q_formal.yaml: recovery_definition and settleTime",
                "all formal runs: metrics.json and logs.jsonl",
            ],
            "protocol_effect": (
                    "The 18-second value is the run-level post-workload settle delay, not a per-rejoin "
                    "censor time. The 100 secondary recovery records use a fixed label despite "
                    "different remaining injection opportunities; primary metrics and run coordinates "
                    "are unaffected."
            ),
        },
        {
            "id": "D8B-002",
            "classification": "Event-anchor ambiguity",
            "scope": "Seed44/Gossip recovery events 1 and 2",
            "finding": (
                "The same m77 full-delivery observation is assigned to both event 1 "
                "(27.438531 s) and event 2 (2.982053 s); event 2 leave occurs before event 1 "
                "is attributed recovery."
            ),
            "evidence": [
                "20261020T041621Z-K5Q-formal/runs/seed44/gossip/metrics.json",
                "20261020T041621Z-K5Q-formal/runs/seed44/gossip/logs.jsonl",
                "neighbour_forwarding_analysis.json",
            ],
            "protocol_effect": (
                "This is consistent with the implemented unrestricted search, but the value "
                "cannot be interpreted as an isolated event-1 recovery latency."
            ),
        },
        {
            "id": "D8B-003",
            "classification": "Insufficient archived evidence",
            "scope": "Neighbour-state causal explanation",
            "finding": (
                "Logs contain local peer_availability observations and forwarding attempts, "
                "but no cluster-wide membership convergence acknowledgement or clock-skew bound."
            ),
            "evidence": [
                "gke/app/recovery_availability.py: failure and ack",
                "gke/app/qahbn2_runtime.py: _forward",
                "formal run logs.jsonl: peer_availability, k7_forward_attempt and outcomes",
            ],
            "protocol_effect": (
                "The archive supports separation of Ready, controller gRPC health, local cache "
                "state and observed delivery, but cannot establish neighbour convergence caused delivery."
            ),
        },
        {
            "id": "D8B-004",
            "classification": "Insufficient archived evidence",
            "scope": "Historical archive integrity and remote comparison",
            "finding": (
                "No trusted execution-time per-file checksum baseline exists; this audit is "
                "offline and does not refresh GitHub or Google Drive."
            ),
            "evidence": [
                "docs/stages/D8_A_INDEPENDENT_OFFLINE_RECONCILIATION_20261020.md",
                "docs/stages/d8_a_20261020/i1_sha256_summary.json",
            ],
            "protocol_effect": (
                "Current local files can be read and fingerprinted, but unchanged-since-execution "
                "and remote freshness are not established."
            ),
        },
    ]
    summary = {
        "audit_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "evidence_dir": str(evidence),
        "audit_script_sha256": sha256(Path(__file__)),
        "run_count": len(runs),
        "recovery_observation_count": len(recoveries),
        "protocol_pass_count": sum(run["protocol_check"] == "PASS" for run in runs),
        "protocol_review_count": sum(run["protocol_check"] != "PASS" for run in runs),
        "issue_count": len(issue_register),
        "planned_grid_max_abs_error_s": max(
            run["planned_grid_max_abs_error_s"] for run in runs
        ),
        "maximum_injection_lateness_ms": max(
            run["max_actual_injection_lateness_ms"] for run in runs
        ),
        "recovered_event_count": sum(row["recovered"] for row in recoveries),
        "recovered_after_18s_count": sum(
            row["recovered"] and row["recovery_time_s"] > 18.0 for row in recoveries
        ),
        "reused_recovery_anchor_event_count": sum(
            row["anchor_reused_within_run"] for row in recoveries
        ),
        "unrecovered_events_with_less_than_18s_of_later_injection_opportunities": sum(
            not row["recovered"]
            and row["later_injection_opportunity_span_s"] < 18.0
            for row in recoveries
        ),
        "later_injection_opportunity_span_s_range": [
            min(row["later_injection_opportunity_span_s"] for row in recoveries),
            max(row["later_injection_opportunity_span_s"] for row in recoveries),
        ],
        "post_workload_settle_observed_s_range": [
            min(run["post_workload_settle_observed_s"] for run in runs),
            max(run["post_workload_settle_observed_s"] for run in runs),
        ],
        "event_observability_across_100_rejoins": {
            "with_local_peer_availability_updates": sum(
                bool(event["local_peer_availability_updates_after_rejoin"])
                for item in forwarding
                for event in item["event_summaries"]
            ),
            "with_forward_attempts_to_or_from_target": sum(
                bool(event["forward_attempts_to_or_from_target_after_rejoin"])
                for item in forwarding
                for event in item["event_summaries"]
            ),
            "with_new_delivery_to_rejoined_target": sum(
                bool(event["new_message_deliveries_to_target_after_rejoin"])
                for item in forwarding
                for event in item["event_summaries"]
            ),
            "explicit_neighbour_membership_transition_records": sum(
                item["explicit_neighbour_membership_transition_events"]
                for item in forwarding
            ),
        },
        "event_observability_by_method": forwarding_by_method,
        "recommendation": "PARTIAL",
    }

    (output / "protocol_timing_matrix.json").write_text(
        json.dumps(matrix, indent=2) + "\n"
    )
    matrix_csv = [
        {
            **{
                key: value
                for key, value in row.items()
                if key != "churn_events"
            },
            "churn_event_timing_json": json.dumps(
                row["churn_events"], separators=(",", ":")
            ),
        }
        for row in matrix
    ]
    write_csv(
        output / "protocol_timing_matrix.csv",
        matrix_csv,
        [
            key
            for key in matrix_csv[0]
        ],
    )
    injection_schedule = [
        injection
        for run in runs
        for injection in run["_injection_schedule"]
    ]
    write_csv(
        output / "message_injection_schedule.csv",
        injection_schedule,
    )
    (output / "recovery_event_verification.json").write_text(
        json.dumps(recoveries, indent=2) + "\n"
    )
    write_csv(output / "recovery_event_verification.csv", recoveries)
    (output / "neighbour_forwarding_analysis.json").write_text(
        json.dumps(
            {
                "all_run_summaries": forwarding,
                "representative_seed44_runs": representative,
            },
            indent=2,
        )
        + "\n"
    )
    (output / "discrepancy_register.json").write_text(
        json.dumps(issue_register, indent=2) + "\n"
    )
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return 0 if summary["protocol_review_count"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
