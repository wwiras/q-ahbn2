"""Frozen ControlSim formal Exp11-Q (Churn) workload.

Implements only the S07-A frozen Exp11-Q matrix on the pinned canonical AHBN
runtime. Churn is applied at frozen message-index boundaries, not wall-clock
simulation times.

Matrix:
- BA(100,m=3), source 0, 1,000 sequential queue-to-exhaustion messages
- seeds 42..46; methods AHBN and Q-AHBN2
- churn levels 0.00, 0.20, 0.40
- four leave/rejoin cycles
- leave before messages 201, 401, 601, 801
- rejoin after 50 subsequent messages: before 251, 451, 651, 851
- deterministic seeded target schedule shared by paired methods
"""

from __future__ import annotations

import json
import random
from collections import Counter
from statistics import fmean
from typing import Dict, Iterable

from qahbn2.learning import ACTIONS, QAHBN2Learner
from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter
from qahbn2.learning_validation import (
    ALPHA_Q,
    BA_M,
    BASE_DELAY,
    EPSILON_0,
    EPSILON_DECAY,
    EPSILON_MIN,
    JITTER,
    MESSAGE_SOURCE,
    NUM_CLUSTERS,
    NUM_MESSAGES,
    NUM_NODES,
    TOTAL_STATE_ACTION_PAIRS,
    _AttemptTracker,
    _DecisionTrace,
    _load_canonical,
)

GAMMA = 0.70
SEEDS = (42, 43, 44, 45, 46)
METHODS = ("ahbn", "qahbn2")
CHURN_LEVELS = (0.00, 0.20, 0.40)
CYCLE_ONSETS = (201, 401, 601, 801)
REJOIN_BEFORE_MESSAGES = tuple(value + 50 for value in CYCLE_ONSETS)
EXPECTED_RUNS = tuple(
    (level, method, seed)
    for level in CHURN_LEVELS
    for seed in SEEDS
    for method in METHODS
)

PRIMARY_METRICS = (
    "delivery_ratio",
    "propagation_delay",
    "duplicates",
    "total_forwards",
)
Q_METRICS = (
    "mean_reward",
    "cumulative_reward",
    "q_updates",
    "state_action_coverage",
    "action_distribution",
    "intervention_count",
    "keep_count",
)


def validate_matrix(
    churn_levels: Iterable[float], methods: Iterable[str], seeds: Iterable[int]
) -> None:
    matrix = tuple(
        (float(level), str(method), int(seed))
        for level in churn_levels
        for seed in seeds
        for method in methods
    )
    if matrix != EXPECTED_RUNS:
        raise ValueError(
            "Exp11-Q matrix is frozen: churn={0.00,0.20,0.40}, "
            "methods={ahbn,qahbn2}, seeds={42,43,44,45,46}, exactly 30 runs."
        )


def churn_schedule_for_seed(seed: int, churn_level: float) -> tuple[tuple[int, ...], ...]:
    level = float(churn_level)
    if level not in CHURN_LEVELS:
        raise ValueError(f"invalid frozen Exp11-Q churn level: {level}")
    if level == 0.0:
        return tuple(() for _ in CYCLE_ONSETS)

    candidates = [node_id for node_id in range(NUM_NODES) if node_id != MESSAGE_SOURCE]
    target_count = max(1, int(round(level * len(candidates))))
    target_count = min(target_count, len(candidates))
    rng = random.Random(int(seed))
    return tuple(
        tuple(sorted(rng.sample(candidates, target_count)))
        for _ in CYCLE_ONSETS
    )


def _controller(AHBNController, AHBNParams):
    return AHBNController(AHBNParams(
        alpha=0.30, d0=0.0, l0=0.0, u0=0.0, c0=0.0,
        w_d=-1.0, w_l=1.0, w_u=1.0, w_c=1.0,
        kappa=1.0, beta=1.0, min_fanout=2, max_fanout=6,
        mode_threshold=0.5,
    ))


def _scenario(seed: int):
    (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        assign_static_clusters, build_nodes_from_graph, get_or_build_topology,
    ) = _load_canonical()
    graph = get_or_build_topology(
        topology_type="ba", num_nodes=NUM_NODES, seed=int(seed),
        use_cache=False, ba_m=BA_M,
    )
    nodes = build_nodes_from_graph(graph)
    cluster_manager = assign_static_clusters(
        nodes, num_clusters=NUM_CLUSTERS, resource_aware_heads=False,
    )
    return (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        nodes, cluster_manager,
    )


def _aggregate(sim, message_ids: list[str]) -> Dict[str, object]:
    delivery = []
    delays = []
    duplicates = 0
    forwards = 0
    for message_id in message_ids:
        summary = sim.metrics.summarize_message(message_id, total_nodes=NUM_NODES)
        delivery.append(float(summary["delivery_ratio"]))
        if summary["propagation_delay"] is not None:
            delays.append(float(summary["propagation_delay"]))
        duplicates += int(summary["duplicates"])
        forwards += int(summary["total_forwards"])
    return {
        "delivery_ratio": fmean(delivery) if delivery else 0.0,
        "propagation_delay": fmean(delays) if delays else 0.0,
        "duplicates": duplicates,
        "total_forwards": forwards,
    }


def _apply_churn_boundary(
    sim,
    *,
    index: int,
    churn_level: float,
    schedule: tuple[tuple[int, ...], ...],
) -> list[dict]:
    events = []
    if churn_level == 0.0:
        return events

    for cycle, rejoin_index in enumerate(REJOIN_BEFORE_MESSAGES):
        if index == rejoin_index:
            for node_id in schedule[cycle]:
                sim.handle_churn_join(
                    now=float(sim.clock), node_id=node_id, churn_rate=float(churn_level)
                )
            events.append({
                "cycle": cycle + 1,
                "event": "join",
                "before_message": index,
                "targets": list(schedule[cycle]),
            })

    for cycle, onset_index in enumerate(CYCLE_ONSETS):
        if index == onset_index:
            for node_id in schedule[cycle]:
                if node_id == MESSAGE_SOURCE:
                    raise AssertionError("formal Exp11-Q must never churn the source")
                sim.handle_churn_leave(
                    now=float(sim.clock), node_id=node_id, churn_rate=float(churn_level)
                )
            events.append({
                "cycle": cycle + 1,
                "event": "leave",
                "before_message": index,
                "targets": list(schedule[cycle]),
            })
    return events


def run_ahbn(*, seed: int, churn_level: float) -> Dict[str, object]:
    (
        AHBNController, AHBNParams, Simulator, _ClusterStrategy, _GossipStrategy,
        nodes, cluster_manager,
    ) = _scenario(seed)
    from ahbn.strategies.ahbn import AHBNStrategy

    controller = _controller(AHBNController, AHBNParams)
    sim = Simulator(
        nodes=nodes,
        strategy=AHBNStrategy(default_fanout=3, adaptive_fanout=True),
        seed=int(seed),
        base_delay=BASE_DELAY,
        jitter=JITTER,
        cluster_manager=cluster_manager,
        controller=controller,
        ch_overload_factor=1.0,
        failure_injector=None,
        churn_manager=None,
        experiment_name="exp11q",
        strategy_name="ahbn",
        scenario_tag=f"churn_{float(churn_level):.2f}",
        enable_adaptive_trace=False,
        resource_aware_heads=False,
    )

    schedule = churn_schedule_for_seed(seed, churn_level)
    message_ids = []
    churn_events = []
    for index in range(1, NUM_MESSAGES + 1):
        churn_events.extend(_apply_churn_boundary(
            sim, index=index, churn_level=float(churn_level), schedule=schedule
        ))
        message_id = f"exp11q-{index:04d}"
        message_ids.append(message_id)
        sim.inject_message(source_id=MESSAGE_SOURCE, message_id=message_id)
        sim.run(until=float("inf"))

    return {
        **_aggregate(sim, message_ids),
        "churn_target_count": len(schedule[0]) if schedule else 0,
        "churn_schedule": json.dumps([list(x) for x in schedule]),
        "churn_events": json.dumps(churn_events),
    }


def run_qahbn2(
    *, seed: int, churn_level: float, trace_decisions: bool = True
) -> Dict[str, object]:
    (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        nodes, cluster_manager,
    ) = _scenario(seed)

    controller = _controller(AHBNController, AHBNParams)
    learner = QAHBN2Learner(
        alpha=ALPHA_Q, gamma=GAMMA, epsilon=EPSILON_0,
        epsilon_min=EPSILON_MIN, epsilon_decay=EPSILON_DECAY, seed=int(seed),
    )
    adapter = ControlSimQAHBN2Adapter(learner)
    trace = _DecisionTrace(enabled=trace_decisions)
    tracker = _AttemptTracker(adapter, trace=trace)
    gossip = GossipStrategy(fanout=3)
    cluster = ClusterStrategy()

    class QAHBN2Strategy:
        def select_targets(self, node, message, simulator, sender_id=None):
            q = adapter.decide(
                peer_id=node.node_id,
                message_id=message.message_id,
                d_hat=node.control.d_hat,
                l_hat=node.control.l_hat,
                u_hat=node.control.u_hat,
                c_hat=node.control.c_hat,
                mode_ahbn=str(node.control.mode),
                k_ahbn=int(node.control.fanout),
            )
            if q.mode_q == "gossip":
                gossip.fanout = int(q.k_q)
                targets = gossip.select_targets(
                    node, message, simulator, exclude_target_id=sender_id,
                )
            elif q.mode_q in {"cluster", "structured"}:
                cluster.fanout = int(q.k_q)
                targets = cluster.select_targets(
                    node, message, simulator, exclude_target_id=sender_id,
                )
            else:
                raise ValueError(f"unknown Q-AHBN2 dissemination mode: {q.mode_q}")
            realized = [
                target for target in dict.fromkeys(targets)
                if target != node.node_id
            ]
            trace.register(q, realized)
            tracker.register(q.decision_id, node.node_id, message.message_id, realized)
            return realized

    class QAHBN2Simulator(Simulator):
        def handle_receive(self, now, dst_id, src_id, message, sent_at=None):
            if src_id != dst_id:
                dst = self.nodes[dst_id]
                outcome = "DUPLICATE" if dst.has_seen(message.message_id) else "NEW"
                tracker.resolve(src_id, dst_id, message.message_id, outcome)
            return super().handle_receive(now, dst_id, src_id, message, sent_at)

    sim = QAHBN2Simulator(
        nodes=nodes,
        strategy=QAHBN2Strategy(),
        seed=int(seed),
        base_delay=BASE_DELAY,
        jitter=JITTER,
        cluster_manager=cluster_manager,
        controller=controller,
        ch_overload_factor=1.0,
        failure_injector=None,
        churn_manager=None,
        experiment_name="exp11q",
        strategy_name="qahbn2",
        scenario_tag=f"churn_{float(churn_level):.2f}",
        enable_adaptive_trace=False,
        resource_aware_heads=False,
    )

    schedule = churn_schedule_for_seed(seed, churn_level)
    message_ids = []
    churn_events = []
    for index in range(1, NUM_MESSAGES + 1):
        tracker.assert_empty()
        churn_events.extend(_apply_churn_boundary(
            sim, index=index, churn_level=float(churn_level), schedule=schedule
        ))
        message_id = f"exp11q-{index:04d}"
        message_ids.append(message_id)
        sim.inject_message(source_id=MESSAGE_SOURCE, message_id=message_id)
        sim.run(until=float("inf"))
        tracker.assert_empty()

    for decision_id in tuple(learner.transitions.latest_decision_by_peer.values()):
        learner.terminal(decision_id)

    rewards = list(learner.reward_history)
    action_counts = Counter(action for _, action in learner.action_history)
    unique_state_actions = len(set(learner.action_history))
    keep_count = action_counts.get("KEEP", 0)
    intervention_count = len(learner.action_history) - keep_count

    return {
        **_aggregate(sim, message_ids),
        "mean_reward": fmean(rewards) if rewards else 0.0,
        "cumulative_reward": sum(rewards),
        "q_updates": learner.update_count,
        "state_action_coverage": unique_state_actions / TOTAL_STATE_ACTION_PAIRS,
        "action_distribution": json.dumps(
            {action: action_counts.get(action, 0) for action in ACTIONS},
            sort_keys=True,
        ),
        "intervention_count": intervention_count,
        "keep_count": keep_count,
        "churn_target_count": len(schedule[0]) if schedule else 0,
        "churn_schedule": json.dumps([list(x) for x in schedule]),
        "churn_events": json.dumps(churn_events),
        **({"decision_trace": list(trace.records.values())} if trace_decisions else {}),
    }


def run_exp11q_cell(
    *, churn_level: float, method: str, seed: int, trace_decisions: bool = True
) -> Dict[str, object]:
    level = float(churn_level)
    if level not in CHURN_LEVELS:
        raise ValueError(f"invalid frozen Exp11-Q churn level: {level}")
    if method not in METHODS:
        raise ValueError(f"invalid frozen Exp11-Q method: {method}")
    if int(seed) not in SEEDS:
        raise ValueError(f"invalid frozen Exp11-Q seed: {seed}")
    if method == "ahbn":
        metrics = run_ahbn(seed=int(seed), churn_level=level)
    else:
        metrics = run_qahbn2(
            seed=int(seed), churn_level=level, trace_decisions=trace_decisions
        )
    return {
        "churn_level": level,
        "method": method,
        "seed": int(seed),
        **metrics,
    }
