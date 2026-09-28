"""Frozen ControlSim formal Exp12-Q (Heterogeneity) workload.

Implements only the frozen Exp12-Q matrix on the pinned canonical AHBN runtime.

Matrix:
- BA(100,m=3), source 0, 1,000 sequential queue-to-exhaustion messages
- profiles balanced / moderate_heterogeneity / weak_heavy
- seeds 42..46; methods AHBN and Q-AHBN2
- deterministic seeded strong/medium/weak assignment shared by paired methods
- failure and churn disabled
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from statistics import fmean
from typing import Dict, Iterable

from qahbn2.learning import ACTIONS, QAHBN2Learner
from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter
from qahbn2.learning_validation import (
    ALPHA_Q, BA_M, BASE_DELAY, EPSILON_0, EPSILON_DECAY, EPSILON_MIN,
    JITTER, MESSAGE_SOURCE, NUM_CLUSTERS, NUM_MESSAGES, NUM_NODES,
    TOTAL_STATE_ACTION_PAIRS, _AttemptTracker, _DecisionTrace, _load_canonical,
)

GAMMA = 0.70
SEEDS = (42, 43, 44, 45, 46)
METHODS = ("ahbn", "qahbn2")
RESOURCE_PROFILES = ("balanced", "moderate_heterogeneity", "weak_heavy")
RESOURCE_CLASSES = {
    "strong": {"processing_delay": 0.15, "capacity_score": 1.80},
    "medium": {"processing_delay": 0.50, "capacity_score": 1.00},
    "weak": {"processing_delay": 1.00, "capacity_score": 0.55},
}
PROFILE_FRACTIONS = {
    "balanced": {"strong": 0.25, "medium": 0.50, "weak": 0.25},
    "moderate_heterogeneity": {"strong": 0.20, "medium": 0.45, "weak": 0.35},
    "weak_heavy": {"strong": 0.15, "medium": 0.35, "weak": 0.50},
}
EXPECTED_RUNS = tuple(
    (profile, method, seed)
    for profile in RESOURCE_PROFILES
    for seed in SEEDS
    for method in METHODS
)

PRIMARY_METRICS = (
    "delivery_ratio", "propagation_delay", "duplicates", "total_forwards",
)
Q_METRICS = (
    "mean_reward", "cumulative_reward", "q_updates", "state_action_coverage",
    "action_distribution", "intervention_count", "keep_count",
)


def validate_matrix(
    profiles: Iterable[str], methods: Iterable[str], seeds: Iterable[int]
) -> None:
    matrix = tuple(
        (str(profile), str(method), int(seed))
        for profile in profiles for seed in seeds for method in methods
    )
    if matrix != EXPECTED_RUNS:
        raise ValueError(
            "Exp12-Q matrix is frozen: profiles={balanced,moderate_heterogeneity,"
            "weak_heavy}, methods={ahbn,qahbn2}, seeds={42,43,44,45,46}, "
            "exactly 30 runs."
        )


def _resource_config() -> dict:
    return {
        "resources": {
            "classes": {name: dict(values) for name, values in RESOURCE_CLASSES.items()},
            "profiles": {name: dict(values) for name, values in PROFILE_FRACTIONS.items()},
        }
    }


def _controller(AHBNController, AHBNParams):
    return AHBNController(AHBNParams(
        alpha=0.30, d0=0.0, l0=0.0, u0=0.0, c0=0.0,
        w_d=-1.0, w_l=1.0, w_u=1.0, w_c=1.0,
        kappa=1.0, beta=1.0, min_fanout=2, max_fanout=6,
        mode_threshold=0.5,
    ))


def _scenario(seed: int, resource_profile: str):
    if resource_profile not in RESOURCE_PROFILES:
        raise ValueError(f"invalid frozen Exp12-Q resource profile: {resource_profile}")
    (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        assign_static_clusters, build_nodes_from_graph, get_or_build_topology,
    ) = _load_canonical()
    from ahbn.topology import assign_mixed_resources

    graph = get_or_build_topology(
        topology_type="ba", num_nodes=NUM_NODES, seed=int(seed),
        use_cache=False, ba_m=BA_M,
    )
    nodes = build_nodes_from_graph(graph)
    assign_mixed_resources(
        nodes, _resource_config(), seed=int(seed), scenario_name=resource_profile
    )
    cluster_manager = assign_static_clusters(
        nodes, num_clusters=NUM_CLUSTERS, resource_aware_heads=False,
    )
    assignment = tuple(
        (int(node_id), str(nodes[node_id].resource_class))
        for node_id in sorted(nodes)
    )
    assignment_payload = ";".join(f"{node}:{cls}" for node, cls in assignment)
    assignment_sha256 = hashlib.sha256(
        assignment_payload.encode("utf-8")
    ).hexdigest()
    counts = Counter(cls for _, cls in assignment)
    return (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        nodes, cluster_manager, assignment, assignment_sha256, counts,
    )


def resource_assignment_for_seed(seed: int, resource_profile: str) -> tuple:
    scenario = _scenario(int(seed), str(resource_profile))
    return scenario[7]


def _aggregate(sim, message_ids: list[str]) -> Dict[str, object]:
    delivery, delays = [], []
    duplicates = forwards = 0
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


def _resource_provenance(assignment, assignment_sha256, counts) -> dict:
    return {
        "resource_assignment_sha256": assignment_sha256,
        "resource_class_counts": json.dumps(
            {name: int(counts.get(name, 0)) for name in RESOURCE_CLASSES},
            sort_keys=True,
        ),
        "resource_assignment": json.dumps(list(assignment)),
    }


def run_ahbn(*, seed: int, resource_profile: str) -> Dict[str, object]:
    (
        AHBNController, AHBNParams, Simulator, _ClusterStrategy, _GossipStrategy,
        nodes, cluster_manager, assignment, assignment_sha256, counts,
    ) = _scenario(seed, resource_profile)
    from ahbn.strategies.ahbn import AHBNStrategy

    sim = Simulator(
        nodes=nodes,
        strategy=AHBNStrategy(default_fanout=3, adaptive_fanout=True),
        seed=int(seed), base_delay=BASE_DELAY, jitter=JITTER,
        cluster_manager=cluster_manager,
        controller=_controller(AHBNController, AHBNParams),
        ch_overload_factor=1.0, failure_injector=None, churn_manager=None,
        experiment_name="exp12q", strategy_name="ahbn",
        scenario_tag=str(resource_profile), enable_adaptive_trace=False,
        resource_aware_heads=False,
    )
    message_ids = []
    for index in range(1, NUM_MESSAGES + 1):
        message_id = f"exp12q-{index:04d}"
        message_ids.append(message_id)
        sim.inject_message(source_id=MESSAGE_SOURCE, message_id=message_id)
        sim.run(until=float("inf"))
    return {
        **_aggregate(sim, message_ids),
        **_resource_provenance(assignment, assignment_sha256, counts),
    }


def run_qahbn2(
    *, seed: int, resource_profile: str, trace_decisions: bool = True
) -> Dict[str, object]:
    (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        nodes, cluster_manager, assignment, assignment_sha256, counts,
    ) = _scenario(seed, resource_profile)

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
                peer_id=node.node_id, message_id=message.message_id,
                d_hat=node.control.d_hat, l_hat=node.control.l_hat,
                u_hat=node.control.u_hat, c_hat=node.control.c_hat,
                mode_ahbn=str(node.control.mode), k_ahbn=int(node.control.fanout),
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
        nodes=nodes, strategy=QAHBN2Strategy(), seed=int(seed),
        base_delay=BASE_DELAY, jitter=JITTER, cluster_manager=cluster_manager,
        controller=controller, ch_overload_factor=1.0,
        failure_injector=None, churn_manager=None,
        experiment_name="exp12q", strategy_name="qahbn2",
        scenario_tag=str(resource_profile), enable_adaptive_trace=False,
        resource_aware_heads=False,
    )

    message_ids = []
    for index in range(1, NUM_MESSAGES + 1):
        tracker.assert_empty()
        message_id = f"exp12q-{index:04d}"
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
        **_resource_provenance(assignment, assignment_sha256, counts),
        **({"decision_trace": list(trace.records.values())} if trace_decisions else {}),
    }


def run_exp12q_cell(
    *, resource_profile: str, method: str, seed: int, trace_decisions: bool = True
) -> Dict[str, object]:
    profile = str(resource_profile)
    if profile not in RESOURCE_PROFILES:
        raise ValueError(f"invalid frozen Exp12-Q resource profile: {profile}")
    if method not in METHODS:
        raise ValueError(f"invalid frozen Exp12-Q method: {method}")
    if int(seed) not in SEEDS:
        raise ValueError(f"invalid frozen Exp12-Q seed: {seed}")
    if method == "ahbn":
        metrics = run_ahbn(seed=int(seed), resource_profile=profile)
    else:
        metrics = run_qahbn2(
            seed=int(seed), resource_profile=profile, trace_decisions=trace_decisions
        )
    return {
        "resource_profile": profile, "method": method, "seed": int(seed), **metrics,
    }
