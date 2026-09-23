"""Event-path bridge for AR-1.4.2A.1.

The bridge is intentionally simulator-agnostic: ControlSim supplies canonical
AHBN outputs, eligible targets, and direct attempt outcomes.  The bridge never
recomputes or mutates AHBN internals.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from qahbn2.controlsim_adapter import ControlSimQAHBN2Adapter, QDecision


@dataclass(frozen=True)
class DirectAttemptOutcome:
    target_peer: int
    outcome: str  # NEW | DUPLICATE | FAILED


@dataclass(frozen=True)
class ForwardingDecision:
    q: QDecision
    eligible_targets: tuple[int, ...]
    realized_targets: tuple[int, ...]


class ControlSimEventBridge:
    def __init__(self, adapter: ControlSimQAHBN2Adapter) -> None:
        self.adapter = adapter

    def new_message_decision(
        self, *, peer_id: int, message_id: str, d_hat: float, l_hat: float,
        u_hat: float, c_hat: float, mode_ahbn: str, k_ahbn: int,
        eligible_targets: Sequence[int],
    ) -> ForwardingDecision:
        q = self.adapter.decide(
            peer_id=peer_id, message_id=message_id,
            d_hat=d_hat, l_hat=l_hat, u_hat=u_hat, c_hat=c_hat,
            mode_ahbn=mode_ahbn, k_ahbn=k_ahbn,
        )
        # Q-AHBN2 requests k_Q; the simulator realizes only eligible neighbors.
        k_real = min(max(0, q.k_q), len(eligible_targets))
        return ForwardingDecision(
            q=q,
            eligible_targets=tuple(eligible_targets),
            realized_targets=tuple(eligible_targets[:k_real]),
        )

    def close_direct_attempts(
        self, decision_id: str, outcomes: Iterable[DirectAttemptOutcome]
    ) -> None:
        counts = {"NEW": 0, "DUPLICATE": 0, "FAILED": 0}
        for item in outcomes:
            if item.outcome not in counts:
                raise ValueError(f"invalid direct outcome: {item.outcome}")
            counts[item.outcome] += 1
        self.adapter.close(
            decision_id,
            new=counts["NEW"],
            duplicate=counts["DUPLICATE"],
            failed=counts["FAILED"],
        )

    def terminal(self, decision_id: str) -> None:
        self.adapter.terminal(decision_id)
