"""Real ControlSim Learning Validation workload for AR-1.4.2.

This module integrates the frozen Q-AHBN2 learner with the pinned canonical
AHBN v0.63 ControlSim runtime.  It does not copy or modify canonical AHBN.
The canonical runtime must be supplied via AHBN_V063_ROOT or a sibling
../ahbn/v0.63 checkout.

Learning Validation is deliberately stationary: BA(100, m=3), source 0,
base delay 1.0, jitter 0.2, four static clusters, no failure/churn/resource
disturbance, and 1,000 messages disseminated sequentially to queue exhaustion.
The learner and AHBN state persist within one run and reset between runs.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path
from statistics import fmean
from typing import Dict

from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter
from qahbn2.learning import ACTIONS, QAHBN2Learner


NUM_MESSAGES = 1000
NUM_NODES = 100
BA_M = 3
MESSAGE_SOURCE = 0
BASE_DELAY = 1.0
JITTER = 0.2
NUM_CLUSTERS = 4

ALPHA_Q = 0.25
EPSILON_0 = 0.30
EPSILON_MIN = 0.03
EPSILON_DECAY = 0.995

STABILIZATION_WINDOW = 50
STABILIZATION_DELTA = 0.05
STABILIZATION_CONSECUTIVE = 3
TOTAL_STATE_ACTION_PAIRS = 81 * len(ACTIONS)
CANONICAL_AHBN_COMMIT = "936a79480bc1252c79b6ee01f65c88c740af2844"


def _canonical_root() -> Path:
    explicit = os.environ.get("AHBN_V063_ROOT")
    candidates = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    candidates.append(Path(__file__).resolve().parents[2] / "ahbn" / "v0.63")
    for root in candidates:
        if (root / "ahbn" / "simulator.py").is_file():
            resolved = root.resolve()
            repo_root = resolved.parent
            try:
                head = subprocess.check_output(
                    ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
                    text=True, stderr=subprocess.STDOUT,
                ).strip()
            except (OSError, subprocess.CalledProcessError) as exc:
                raise RuntimeError(
                    "Canonical AHBN execution requires a Git checkout so the "
                    "pinned authority commit can be verified."
                ) from exc
            if head != CANONICAL_AHBN_COMMIT:
                raise RuntimeError(
                    "Canonical AHBN checkout mismatch: expected "
                    f"{CANONICAL_AHBN_COMMIT}, found {head}. "
                    "Do not execute sensitivity on an unpinned AHBN revision."
                )
            return resolved
    raise RuntimeError(
        "Canonical AHBN v0.63 checkout not found. Set AHBN_V063_ROOT to the "
        "pinned wwiras/ahbn checkout's v0.63 directory "
        "(authority commit 936a79480bc1252c79b6ee01f65c88c740af2844)."
    )


def _load_canonical():
    root = _canonical_root()
    root_text = str(root)
    if root_text not in sys.path:
        sys.path.insert(0, root_text)

    from ahbn.control import AHBNController, AHBNParams
    from ahbn.simulator import Simulator
    from ahbn.strategies.cluster import ClusterStrategy
    from ahbn.strategies.gossip import GossipStrategy
    from ahbn.topology import (
        assign_static_clusters,
        build_nodes_from_graph,
        get_or_build_topology,
    )
    return (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        assign_static_clusters, build_nodes_from_graph, get_or_build_topology,
    )


def stabilization_point(rewards: list[float]) -> int | str:
    """Frozen B.3A reward-stability diagnostic."""
    w = STABILIZATION_WINDOW
    means = [
        fmean(rewards[start:start + w])
        for start in range(0, len(rewards) - w + 1, w)
    ]
    deltas = [abs(means[i] - means[i - 1]) for i in range(1, len(means))]
    needed = STABILIZATION_CONSECUTIVE
    for start in range(0, len(deltas) - needed + 1):
        if all(delta <= STABILIZATION_DELTA for delta in deltas[start:start + needed]):
            # deltas[start] compares windows j-1 and j, with one-based j=start+2.
            return w * (start + 2)
    return "NOT_STABILIZED"


class _AttemptTracker:
    def __init__(self, adapter: ControlSimQAHBN2Adapter) -> None:
        self.adapter = adapter
        self.pending: Dict[str, dict] = {}
        self.by_attempt: Dict[tuple[int, int, str], str] = {}

    def register(self, decision_id: str, src_id: int, message_id: str,
                 targets: list[int]) -> None:
        if not targets:
            self.adapter.close(decision_id, new=0, duplicate=0, failed=0)
            return
        self.pending[decision_id] = {
            "remaining": len(targets), "NEW": 0, "DUPLICATE": 0, "FAILED": 0
        }
        for dst_id in targets:
            key = (int(src_id), int(dst_id), str(message_id))
            if key in self.by_attempt:
                raise RuntimeError(f"duplicate direct-attempt key: {key}")
            self.by_attempt[key] = decision_id

    def resolve(self, src_id: int, dst_id: int, message_id: str, outcome: str) -> None:
        key = (int(src_id), int(dst_id), str(message_id))
        decision_id = self.by_attempt.pop(key, None)
        if decision_id is None:
            return
        rec = self.pending[decision_id]
        rec[outcome] += 1
        rec["remaining"] -= 1
        if rec["remaining"] == 0:
            self.adapter.close(
                decision_id,
                new=rec["NEW"], duplicate=rec["DUPLICATE"], failed=rec["FAILED"],
            )
            del self.pending[decision_id]

    def assert_empty(self) -> None:
        if self.pending or self.by_attempt:
            raise RuntimeError("unresolved direct-attempt attribution at queue exhaustion")


def run_learning_validation(*, gamma: float, seed: int) -> Dict[str, object]:
    (
        AHBNController, AHBNParams, Simulator, ClusterStrategy, GossipStrategy,
        assign_static_clusters, build_nodes_from_graph, get_or_build_topology,
    ) = _load_canonical()

    graph = get_or_build_topology(
        topology_type="ba", num_nodes=NUM_NODES, seed=seed,
        use_cache=False, ba_m=BA_M,
    )
    nodes = build_nodes_from_graph(graph)
    cluster_manager = assign_static_clusters(
        nodes, num_clusters=NUM_CLUSTERS, resource_aware_heads=False,
    )
    controller = AHBNController(AHBNParams(
        alpha=0.30, d0=0.0, l0=0.0, u0=0.0, c0=0.0,
        w_d=-1.0, w_l=1.0, w_u=1.0, w_c=1.0,
        kappa=1.0, beta=1.0, min_fanout=2, max_fanout=6,
        mode_threshold=0.5,
    ))

    learner = QAHBN2Learner(
        alpha=ALPHA_Q, gamma=float(gamma), epsilon=EPSILON_0,
        epsilon_min=EPSILON_MIN, epsilon_decay=EPSILON_DECAY, seed=seed,
    )
    adapter = ControlSimQAHBN2Adapter(learner)
    tracker = _AttemptTracker(adapter)

    gossip = GossipStrategy(fanout=3)
    cluster = ClusterStrategy()

    class QAHBN2Strategy:
        def select_targets(self, node, message, simulator, sender_id=None):
            mode_ahbn = str(node.control.mode)
            k_ahbn = int(node.control.fanout)
            q = adapter.decide(
                peer_id=node.node_id, message_id=message.message_id,
                d_hat=node.control.d_hat, l_hat=node.control.l_hat,
                u_hat=node.control.u_hat, c_hat=node.control.c_hat,
                mode_ahbn=mode_ahbn, k_ahbn=k_ahbn,
            )
            mode_q = q.mode_q
            if mode_q == "gossip":
                gossip.fanout = int(q.k_q)
                targets = gossip.select_targets(
                    node, message, simulator, exclude_target_id=sender_id,
                )
            elif mode_q in {"cluster", "structured"}:
                cluster.fanout = int(q.k_q)
                targets = cluster.select_targets(
                    node, message, simulator, exclude_target_id=sender_id,
                )
            else:
                raise ValueError(f"unknown Q-AHBN2 dissemination mode: {mode_q}")

            realized = [
                target for target in dict.fromkeys(targets)
                if target != node.node_id
            ]
            tracker.register(q.decision_id, node.node_id, message.message_id, realized)
            return realized

    class QAHBN2Simulator(Simulator):
        def handle_receive(self, now, dst_id, src_id, message, sent_at=None):
            # Resolve the originating direct attempt before canonical receive
            # processing changes seen-state. Source injection has no registered
            # direct-attempt key and is therefore excluded automatically.
            if src_id != dst_id:
                dst = self.nodes[dst_id]
                outcome = "DUPLICATE" if dst.has_seen(message.message_id) else "NEW"
                tracker.resolve(src_id, dst_id, message.message_id, outcome)
            return super().handle_receive(now, dst_id, src_id, message, sent_at)

    sim = QAHBN2Simulator(
        nodes=nodes,
        strategy=QAHBN2Strategy(),
        seed=seed,
        base_delay=BASE_DELAY,
        jitter=JITTER,
        cluster_manager=cluster_manager,
        controller=controller,
        ch_overload_factor=1.0,
        failure_injector=None,
        churn_manager=None,
        experiment_name="learning_validation",
        strategy_name="qahbn2",
        scenario_tag=f"gamma={float(gamma):.2f}",
        enable_adaptive_trace=False,
        resource_aware_heads=False,
    )

    delivery: list[float] = []
    delays: list[float] = []
    duplicates = 0
    total_forwards = 0

    for index in range(NUM_MESSAGES):
        message_id = f"lv-{index + 1:04d}"
        sim.inject_message(source_id=MESSAGE_SOURCE, message_id=message_id)
        sim.run(until=float("inf"))
        tracker.assert_empty()
        summary = sim.metrics.summarize_message(message_id, total_nodes=NUM_NODES)
        delivery.append(float(summary["delivery_ratio"]))
        if summary["propagation_delay"] is not None:
            delays.append(float(summary["propagation_delay"]))
        duplicates += int(summary["duplicates"])
        total_forwards += int(summary["total_forwards"])

    # The final same-peer decisions have no later decision opportunity.
    # Close only those latest records as terminal; rewarded records then update
    # with zero bootstrap, while F=0 records remain non-reward-bearing.
    for decision_id in tuple(learner.transitions.latest_decision_by_peer.values()):
        learner.terminal(decision_id)

    rewards = list(learner.reward_history)
    action_counts = Counter(action for _, action in learner.action_history)
    action_distribution = {action: action_counts.get(action, 0) for action in ACTIONS}
    unique_state_actions = len(set(learner.action_history))

    return {
        "mean_reward": fmean(rewards) if rewards else 0.0,
        "cumulative_reward": sum(rewards),
        "stabilization": stabilization_point(rewards),
        "q_updates": learner.update_count,
        "state_action_coverage": unique_state_actions / TOTAL_STATE_ACTION_PAIRS,
        "action_distribution": json.dumps(action_distribution, sort_keys=True),
        "delivery_ratio": fmean(delivery) if delivery else 0.0,
        "propagation_delay": fmean(delays) if delays else 0.0,
        "duplicates": duplicates,
        "total_forwards": total_forwards,
    }
