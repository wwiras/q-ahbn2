"""Narrow ControlSim-facing adapter for the frozen Q-AHBN2 learning core.

The simulator remains responsible for canonical AHBN observation/decision,
eligible-target selection, sends, and direct NEW/DUPLICATE/FAILED attribution.
This adapter only bridges those already-frozen values into the learner.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from qahbn2.learning import QAHBN2Learner


@dataclass(frozen=True)
class QDecision:
    decision_id: str
    peer_id: int
    message_id: str
    state: tuple[str, str, str, str]
    action: str
    mode_ahbn: str
    k_ahbn: int
    mode_q: str
    k_q: int


class ControlSimQAHBN2Adapter:
    def __init__(self, learner: QAHBN2Learner) -> None:
        self.learner = learner
        self._serial = 0

    def decide(self, *, peer_id: int, message_id: str, d_hat: float, l_hat: float,
               u_hat: float, c_hat: float, mode_ahbn: str, k_ahbn: int) -> QDecision:
        state = self.learner.discretize(d_hat, l_hat, u_hat, c_hat)
        action = self.learner.choose_action(state)
        mode_q, k_q = self.learner.refine(mode_ahbn, int(k_ahbn), action)
        self._serial += 1
        decision_id = f"{peer_id}:{message_id}:{self._serial}"
        self.learner.begin(
            decision_id=decision_id, peer_id=peer_id, message_id=message_id,
            state=state, action=action,
        )
        return QDecision(
            decision_id=decision_id, peer_id=peer_id, message_id=message_id,
            state=state, action=action, mode_ahbn=mode_ahbn, k_ahbn=int(k_ahbn),
            mode_q=mode_q, k_q=k_q,
        )

    def close(self, decision_id: str, *, new: int, duplicate: int, failed: int) -> None:
        self.learner.close_outcomes(
            decision_id, new=new, duplicate=duplicate, failed=failed
        )

    def terminal(self, decision_id: str) -> None:
        self.learner.terminal(decision_id)
