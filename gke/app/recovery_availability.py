"""P3G experimental transport recovery state; not wired into peer runtime.

No scientific messages are forwarded and no controller/learner is changed.
An explicit lifecycle notification is needed to request a bounded probe.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ProbeTicket:
    peer_id: int
    generation: int


class RecoveryAvailability:
    """Generation-guarded exclusion and single in-flight recovery probes."""

    def __init__(self, excluded: set[int] | None = None) -> None:
        self._lock = threading.RLock()
        self._excluded: set[int] = excluded if excluded is not None else set()
        self._generation: dict[int, int] = {}
        self._inflight: set[int] = set()

    def is_excluded(self, peer_id: int) -> bool:
        with self._lock:
            return peer_id in self._excluded

    def mark_failed(self, peer_id: int) -> bool:
        with self._lock:
            self._generation[peer_id] = self._generation.get(peer_id, 0) + 1
            changed = peer_id not in self._excluded
            self._excluded.add(peer_id)
            return changed

    def mark_recovered(self, peer_id: int) -> bool:
        """Remove exclusion after successful ordinary Forward/duplicate ACK."""
        with self._lock:
            self._generation[peer_id] = self._generation.get(peer_id, 0) + 1
            if peer_id not in self._excluded:
                return False
            self._excluded.remove(peer_id)
            return True

    def begin_probe(self, peer_id: int) -> ProbeTicket | None:
        with self._lock:
            if peer_id not in self._excluded or peer_id in self._inflight:
                return None
            self._inflight.add(peer_id)
            return ProbeTicket(peer_id, self._generation.get(peer_id, 0))

    def finish_probe(
        self,
        ticket: ProbeTicket,
        *,
        rpc_ok: bool,
        returned_peer_id: int | None,
        ready: bool,
        alive: bool,
        topology_permits: bool,
    ) -> bool:
        """Return True only for a verified, current exclusion-to-eligible change."""
        with self._lock:
            # A stale ticket must not cancel a newer probe.
            if ticket.peer_id not in self._inflight:
                return False
            self._inflight.discard(ticket.peer_id)
            if (
                ticket.generation != self._generation.get(ticket.peer_id, 0)
                or ticket.peer_id not in self._excluded
                or not rpc_ok
                or returned_peer_id != ticket.peer_id
                or not ready
                or not alive
                or not topology_permits
            ):
                return False
            self._excluded.remove(ticket.peer_id)
            self._generation[ticket.peer_id] = ticket.generation + 1
            return True


def verify_get_status(
    ticket: ProbeTicket,
    *,
    status_call: Callable[[int, float], object],
    timeout_s: float,
) -> tuple[bool, int | None, bool, bool]:
    """One bounded call, injected for deterministic fake-gRPC testing.

    Caller must supply a timeout-enforcing RPC implementation. No retries here.
    """
    if timeout_s <= 0:
        raise ValueError("timeout_s must be positive")
    try:
        response = status_call(ticket.peer_id, timeout_s)
        return (
            True,
            int(response.peer_id),
            bool(response.ready),
            bool(response.alive),
        )
    except (Exception):
        return (False, None, False, False)
