"""Frozen Q-AHBN2 learning core for bounded ControlSim integration.

This module contains only the already-approved 81-state/5-action learner,
reward equation, Q update, and post-AHBN refinement.  Canonical AHBN itself is
not implemented or modified here.
"""

from __future__ import annotations

import random
from collections import defaultdict
from typing import DefaultDict, Dict, Iterable, Tuple

from qahbn2.transition import ActionName, DecisionId, StateKey, TransitionBookkeeper


ACTIONS: Tuple[ActionName, ...] = (
    "KEEP", "FANOUT_DOWN", "FANOUT_UP", "SET_GOSSIP", "SET_STRUCTURED"
)


class QAHBN2Learner:
    def __init__(self, *, alpha: float = 0.25, gamma: float = 0.90,
                 epsilon: float = 0.30, seed: int = 42) -> None:
        self.alpha = float(alpha)
        self.gamma = float(gamma)
        self.epsilon = float(epsilon)
        self.rng = random.Random(seed)
        self.transitions = TransitionBookkeeper()
        self.q_table: DefaultDict[StateKey, Dict[ActionName, float]] = defaultdict(
            lambda: {a: 0.0 for a in ACTIONS}
        )
        self.update_count = 0

    @staticmethod
    def bucket3(value: float) -> str:
        if value < 1.0 / 3.0:
            return "L"
        if value < 2.0 / 3.0:
            return "M"
        return "H"

    def discretize(self, d_hat: float, l_hat: float, u_hat: float, c_hat: float) -> StateKey:
        values = (d_hat, l_hat, u_hat, c_hat)
        return tuple(self.bucket3(max(0.0, min(1.0, float(v)))) for v in values)  # type: ignore[return-value]

    def choose_action(self, state: StateKey) -> ActionName:
        if self.rng.random() < self.epsilon:
            return self.rng.choice(ACTIONS)
        qvals = self.q_table[state]
        best = max(qvals.values())
        tied = [a for a in ACTIONS if qvals[a] == best]
        return self.rng.choice(tied)

    @staticmethod
    def refine(mode_ahbn: str, k_ahbn: int, action: ActionName) -> Tuple[str, int]:
        if action == "KEEP":
            return mode_ahbn, k_ahbn
        if action == "FANOUT_DOWN":
            return mode_ahbn, k_ahbn - 1
        if action == "FANOUT_UP":
            return mode_ahbn, k_ahbn + 1
        if action == "SET_GOSSIP":
            return "gossip", k_ahbn
        if action == "SET_STRUCTURED":
            return "structured", k_ahbn
        raise ValueError(f"unknown Q-AHBN2 action: {action}")

    def begin(self, *, decision_id: DecisionId, peer_id: int, message_id: str,
              state: StateKey, action: ActionName) -> None:
        self.transitions.begin_decision(
            decision_id=decision_id, peer_id=peer_id, message_id=message_id,
            state_t=state, action_t=action,
        )
        self._update_ready_for_peer(peer_id)

    @staticmethod
    def reward(new: int, duplicate: int, failed: int) -> float | None:
        fwd = int(new) + int(duplicate) + int(failed)
        if fwd == 0:
            return None
        return (int(new) - int(duplicate) - int(failed)) / fwd

    def close_outcomes(self, decision_id: DecisionId, *, new: int,
                       duplicate: int, failed: int) -> None:
        reward = self.reward(new, duplicate, failed)
        record = self.transitions.get(decision_id)
        if reward is None:
            self.transitions.close_no_forwarding_evidence(decision_id)
        else:
            self.transitions.attach_reward(decision_id, reward)
        self._update_if_ready(record)

    def terminal(self, decision_id: DecisionId) -> None:
        record = self.transitions.mark_terminal(decision_id)
        self._update_if_ready(record)

    def _update_ready_for_peer(self, peer_id: int) -> None:
        for record in self.transitions.records.values():
            if record.peer_id == peer_id:
                self._update_if_ready(record)

    def _update_if_ready(self, record) -> None:
        if not record.update_ready:
            return
        old = self.q_table[record.state_t][record.action_t]
        bootstrap = 0.0
        if record.bootstrap_state is not None:
            bootstrap = max(self.q_table[record.bootstrap_state].values())
        target = float(record.reward_t) + self.gamma * bootstrap
        self.q_table[record.state_t][record.action_t] = old + self.alpha * (target - old)
        self.transitions.consume_update(record.decision_id)
        self.update_count += 1
