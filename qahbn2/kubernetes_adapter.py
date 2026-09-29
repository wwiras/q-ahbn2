"""Kubernetes/GKE bridge for the frozen Q-AHBN2 learner.

This module contains no canonical AHBN logic and no comparator implementation.
It consumes already-produced canonical EWMA state and final S5 AHBN proposal,
then performs only the frozen Q-AHBN2 refinement/attribution lifecycle.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Sequence

from qahbn2.learning import QAHBN2Learner


@dataclass(frozen=True)
class KubernetesQDecision:
    decision_id: str
    peer_id: int
    message_id: str
    state: tuple[str, str, str, str]
    action: str
    mode_ahbn: str
    k_ahbn: int
    mode_q: str
    k_q: int
    d_hat: float
    l_hat: float
    u_hat: float
    c_hat: float


@dataclass
class AttemptLedger:
    expected_targets: tuple[int, ...]
    outcomes: Dict[int, str] = field(default_factory=dict)

    def record(self, target_peer: int, outcome: str) -> None:
        if target_peer not in self.expected_targets:
            raise ValueError(f"target {target_peer} not owned by this decision")
        if outcome not in {"NEW", "DUPLICATE", "FAILED"}:
            raise ValueError(f"invalid direct-attempt outcome: {outcome}")
        if target_peer in self.outcomes:
            raise ValueError(f"duplicate outcome for target {target_peer}")
        self.outcomes[target_peer] = outcome

    @property
    def complete(self) -> bool:
        return len(self.outcomes) == len(self.expected_targets)

    def counts(self) -> tuple[int, int, int]:
        vals = tuple(self.outcomes.values())
        return vals.count("NEW"), vals.count("DUPLICATE"), vals.count("FAILED")


class KubernetesQAHBN2Adapter:
    """Environment bridge; canonical AHBN and target selection stay external."""

    def __init__(self, learner: QAHBN2Learner) -> None:
        self.learner = learner
        self._serial = 0
        self._ledgers: Dict[str, AttemptLedger] = {}

    def decide(
        self, *, peer_id: int, message_id: str,
        d_hat: float, l_hat: float, u_hat: float, c_hat: float,
        mode_ahbn: str, k_ahbn: int,
    ) -> KubernetesQDecision:
        state = self.learner.discretize(d_hat, l_hat, u_hat, c_hat)
        action = self.learner.choose_action(state)
        mode_q, k_q = self.learner.refine(mode_ahbn, int(k_ahbn), action)
        # Frozen actuator support after refinement remains within 2..6.
        k_q = max(2, min(6, int(k_q)))
        self._serial += 1
        decision_id = f"gke:{peer_id}:{message_id}:{self._serial}"
        self.learner.begin(
            decision_id=decision_id, peer_id=peer_id, message_id=message_id,
            state=state, action=action,
        )
        return KubernetesQDecision(
            decision_id=decision_id, peer_id=peer_id, message_id=message_id,
            state=state, action=action, mode_ahbn=mode_ahbn, k_ahbn=int(k_ahbn),
            mode_q=mode_q, k_q=k_q, d_hat=float(d_hat), l_hat=float(l_hat),
            u_hat=float(u_hat), c_hat=float(c_hat),
        )

    def register_targets(self, decision_id: str, targets: Sequence[int]) -> None:
        if decision_id in self._ledgers:
            raise ValueError(f"targets already registered: {decision_id}")
        uniq = tuple(dict.fromkeys(int(t) for t in targets))
        self._ledgers[decision_id] = AttemptLedger(expected_targets=uniq)
        if not uniq:
            self.learner.close_outcomes(decision_id, new=0, duplicate=0, failed=0)

    def record_ack(self, decision_id: str, target_peer: int, *, ack_ok: bool) -> None:
        # Existing ahbn2_gke PeerService.Forward returns Ack.ok == is_new.
        self._record(decision_id, target_peer, "NEW" if ack_ok else "DUPLICATE")

    def record_failure(self, decision_id: str, target_peer: int) -> None:
        self._record(decision_id, target_peer, "FAILED")

    def _record(self, decision_id: str, target_peer: int, outcome: str) -> None:
        ledger = self._ledger(decision_id)
        ledger.record(int(target_peer), outcome)
        if ledger.complete:
            new, duplicate, failed = ledger.counts()
            self.learner.close_outcomes(
                decision_id, new=new, duplicate=duplicate, failed=failed
            )

    def terminal(self, decision_id: str) -> None:
        self.learner.terminal(decision_id)

    def ledger(self, decision_id: str) -> AttemptLedger:
        return self._ledger(decision_id)

    def _ledger(self, decision_id: str) -> AttemptLedger:
        try:
            return self._ledgers[decision_id]
        except KeyError as exc:
            raise KeyError(f"unknown decision ledger: {decision_id}") from exc
