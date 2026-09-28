"""Frozen ControlSim Exp13-Q five-method reference benchmark harness.

Implementation-only integration for S10A-IMPL.
No formal execution is authorized by this module alone.
"""

from __future__ import annotations

import json
from typing import Dict, Iterable

from qahbn2.formal_exp11q import (
    CYCLE_ONSETS,
    REJOIN_BEFORE_MESSAGES,
    PRIMARY_METRICS,
    Q_METRICS,
    _aggregate,
    _apply_churn_boundary,
    _controller,
    churn_schedule_for_seed,
    run_ahbn as run_exp11_ahbn,
    run_qahbn2 as run_exp11_qahbn2,
)
from qahbn2.learning_validation import (
    BA_M,
    BASE_DELAY,
    JITTER,
    MESSAGE_SOURCE,
    NUM_CLUSTERS,
    NUM_MESSAGES,
    NUM_NODES,
    _load_canonical,
)

CHURN_LEVEL = 0.40
SEEDS = (42, 43, 44, 45, 46)
METHODS = ("gossip", "structured", "dcsoc", "ahbn", "qahbn2")
EXPECTED_RUNS = tuple((method, seed) for seed in SEEDS for method in METHODS)

DCSOC_EPS = 2.0
DCSOC_MIN_SAMPLES = 3


def validate_matrix(methods: Iterable[str], seeds: Iterable[int]) -> None:
    matrix = tuple((str(method), int(seed)) for seed in seeds for method in methods)
    if matrix != EXPECTED_RUNS:
        raise ValueError(
            "Exp13-Q matrix is frozen: methods={gossip,structured,dcsoc,ahbn,qahbn2}, "
            "seeds={42,43,44,45,46}, churn=0.40, exactly 25 runs."
        )


def _common_topology(seed: int):
    (
        AHBNController,
        AHBNParams,
        Simulator,
        ClusterStrategy,
        GossipStrategy,
        assign_static_clusters,
        build_nodes_from_graph,
        get_or_build_topology,
    ) = _load_canonical()
    graph = get_or_build_topology(
        topology_type="ba",
        num_nodes=NUM_NODES,
        seed=int(seed),
        use_cache=False,
        ba_m=BA_M,
    )
    nodes = build_nodes_from_graph(graph)
    return (
        AHBNController,
        AHBNParams,
        Simulator,
        ClusterStrategy,
        GossipStrategy,
        assign_static_clusters,
        nodes,
    )


def _run_static_comparator(*, seed: int, method: str) -> Dict[str, object]:
    (
        _AHBNController,
        _AHBNParams,
        Simulator,
        ClusterStrategy,
        GossipStrategy,
        assign_static_clusters,
        nodes,
    ) = _common_topology(seed)

    if method == "gossip":
        strategy = GossipStrategy(fanout=None)
        cluster_manager = assign_static_clusters(
            nodes, num_clusters=NUM_CLUSTERS, resource_aware_heads=False
        )
    elif method == "structured":
        strategy = ClusterStrategy()
        cluster_manager = assign_static_clusters(
            nodes, num_clusters=NUM_CLUSTERS, resource_aware_heads=False
        )
    elif method == "dcsoc":
        from ahbn.strategies.dcsoc import DCSOCStrategy
        from ahbn.topology import assign_dcsoc_clusters

        strategy = DCSOCStrategy()
        cluster_manager = assign_dcsoc_clusters(
            nodes, eps=DCSOC_EPS, min_samples=DCSOC_MIN_SAMPLES
        )
    else:
        raise ValueError(f"invalid static Exp13-Q comparator: {method}")

    sim = Simulator(
        nodes=nodes,
        strategy=strategy,
        seed=int(seed),
        base_delay=BASE_DELAY,
        jitter=JITTER,
        cluster_manager=cluster_manager,
        controller=None,
        ch_overload_factor=1.0,
        failure_injector=None,
        churn_manager=None,
        experiment_name="exp13q",
        strategy_name=method,
        scenario_tag="churn_0.40",
        enable_adaptive_trace=False,
        resource_aware_heads=False,
    )

    schedule = churn_schedule_for_seed(seed, CHURN_LEVEL)
    message_ids = []
    churn_events = []
    for index in range(1, NUM_MESSAGES + 1):
        churn_events.extend(
            _apply_churn_boundary(
                sim,
                index=index,
                churn_level=CHURN_LEVEL,
                schedule=schedule,
            )
        )
        message_id = f"exp13q-{index:04d}"
        message_ids.append(message_id)
        sim.inject_message(source_id=MESSAGE_SOURCE, message_id=message_id)
        sim.run(until=float("inf"))

    return {
        **_aggregate(sim, message_ids),
        "churn_target_count": len(schedule[0]) if schedule else 0,
        "churn_schedule": json.dumps([list(x) for x in schedule]),
        "churn_events": json.dumps(churn_events),
        "dcsoc_eps": DCSOC_EPS if method == "dcsoc" else None,
        "dcsoc_min_samples": DCSOC_MIN_SAMPLES if method == "dcsoc" else None,
    }


def run_exp13q_cell(*, method: str, seed: int, trace_decisions: bool = True) -> Dict[str, object]:
    method = str(method)
    seed = int(seed)
    if method not in METHODS:
        raise ValueError(f"invalid frozen Exp13-Q method: {method}")
    if seed not in SEEDS:
        raise ValueError(f"invalid frozen Exp13-Q seed: {seed}")

    if method in {"gossip", "structured", "dcsoc"}:
        metrics = _run_static_comparator(seed=seed, method=method)
    elif method == "ahbn":
        metrics = run_exp11_ahbn(seed=seed, churn_level=CHURN_LEVEL)
    else:
        metrics = run_exp11_qahbn2(
            seed=seed,
            churn_level=CHURN_LEVEL,
            trace_decisions=trace_decisions,
        )

    return {
        "churn_level": CHURN_LEVEL,
        "method": method,
        "seed": seed,
        **metrics,
    }
