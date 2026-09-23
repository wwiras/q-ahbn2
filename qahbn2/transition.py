"""Per-decision transition bookkeeping for Q-AHBN2.

This module implements the AR-1.1/AR-1.2 temporal contract only.  It deliberately
contains no AHBN controller logic, state discretisation, action transformation,
reward calculation, exploration policy, or simulator event logic.

Contract:
* s_t is captured when a peer makes a Q-AHBN2 decision.
* s_(t+1) is the state at that same peer's next Q-AHBN2 decision opportunity.
* R_t belongs to the originating decision and may arrive before or after s_(t+1).
* A non-terminal transition becomes update-ready only when both are available.
* A terminal transition needs a numerical reward but has no successor state.
* A zero-forwarding-evidence decision closes without a numerical reward and is
  never reward-bearing/update-ready.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Hashable, Optional, Tuple


StateKey = Tuple[str, str, str, str]
ActionName = str
DecisionId = Hashable
PeerId = Hashable


@dataclass
class TransitionRecord:
    """One Q-AHBN2 decision and the evidence needed for one Q update."""

    decision_id: DecisionId
    peer_id: PeerId
    message_id: Hashable
    state_t: StateKey
    action_t: ActionName
    reward_t: Optional[float] = None
    next_state: Optional[StateKey] = None
    reward_ready: bool = False
    next_ready: bool = False
    terminal: bool = False
    no_forwarding_evidence: bool = False
    update_consumed: bool = False

    @property
    def update_ready(self) -> bool:
        """Whether this record contains exactly the evidence needed for an update."""
        if self.update_consumed or self.no_forwarding_evidence or not self.reward_ready:
            return False
        if self.terminal:
            return True
        return self.next_ready

    @property
    def bootstrap_state(self) -> Optional[StateKey]:
        """Successor state for bootstrapping; None means terminal/zero bootstrap."""
        if self.terminal:
            return None
        return self.next_state


class TransitionBookkeeper:
    """Own pending transitions without coupling reward order to decision order."""

    def __init__(self) -> None:
        self.records: Dict[DecisionId, TransitionRecord] = {}
        self.latest_decision_by_peer: Dict[PeerId, DecisionId] = {}

    def begin_decision(
        self,
        *,
        decision_id: DecisionId,
        peer_id: PeerId,
        message_id: Hashable,
        state_t: StateKey,
        action_t: ActionName,
    ) -> TransitionRecord:
        """Register a decision and link the previous same-peer decision to state_t."""
        if decision_id in self.records:
            raise ValueError(f"duplicate decision_id: {decision_id!r}")

        previous_id = self.latest_decision_by_peer.get(peer_id)
        if previous_id is not None:
            previous = self.records[previous_id]
            if not previous.terminal and not previous.next_ready:
                previous.next_state = state_t
                previous.next_ready = True

        record = TransitionRecord(
            decision_id=decision_id,
            peer_id=peer_id,
            message_id=message_id,
            state_t=state_t,
            action_t=action_t,
        )
        self.records[decision_id] = record
        self.latest_decision_by_peer[peer_id] = decision_id
        return record

    def attach_reward(self, decision_id: DecisionId, reward: float) -> TransitionRecord:
        """Attach the numerical reward to its originating decision."""
        record = self._record(decision_id)
        if record.no_forwarding_evidence:
            raise ValueError("cannot attach reward after no-forwarding-evidence closure")
        if record.reward_ready:
            raise ValueError(f"reward already attached: {decision_id!r}")
        record.reward_t = float(reward)
        record.reward_ready = True
        return record

    def close_no_forwarding_evidence(self, decision_id: DecisionId) -> TransitionRecord:
        """Close F=0 without manufacturing a numerical reward or Q update."""
        record = self._record(decision_id)
        if record.reward_ready:
            raise ValueError("cannot mark no-forwarding-evidence after reward attachment")
        record.no_forwarding_evidence = True
        return record

    def mark_terminal(self, decision_id: DecisionId) -> TransitionRecord:
        """Mark the final decision at a peer as terminal (zero bootstrap)."""
        record = self._record(decision_id)
        record.terminal = True
        record.next_state = None
        record.next_ready = False
        return record

    def consume_update(self, decision_id: DecisionId) -> TransitionRecord:
        """Mark one ready transition as consumed; prevents duplicate Q updates."""
        record = self._record(decision_id)
        if not record.update_ready:
            raise ValueError(f"transition is not update-ready: {decision_id!r}")
        record.update_consumed = True
        return record

    def get(self, decision_id: DecisionId) -> TransitionRecord:
        return self._record(decision_id)

    def _record(self, decision_id: DecisionId) -> TransitionRecord:
        try:
            return self.records[decision_id]
        except KeyError as exc:
            raise KeyError(f"unknown decision_id: {decision_id!r}") from exc
