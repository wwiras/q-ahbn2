"""Transport-only peer availability and bounded GetStatus recovery (P3G).

Does not select dissemination targets or alter controller/learner contracts.
"""
from __future__ import annotations

import threading
from collections import defaultdict


class RecoveryAvailability:
    def __init__(self, unavailable, observations, *, enabled=False, logger=None):
        self.unavailable = unavailable
        self.observations = observations
        self.enabled = bool(enabled)
        self.logger = logger or (lambda **kwargs: None)
        self.lock = threading.RLock()
        self.epochs = defaultdict(int)
        self.inflight = set()

    def failure(self, target, *, reason="forward_failed"):
        target = int(target)
        with self.lock:
            self.epochs[target] += 1  # invalidate even if already excluded
            changed = target not in self.unavailable
            if changed:
                self.unavailable.add(target)
                self.observations.record_leave()
            self.logger(event="peer_availability", target=target, reason=reason,
                        epoch=self.epochs[target], unavailable=True, changed=changed)
            return changed

    def ack(self, target, *, reason="forward_ack"):
        target = int(target)
        with self.lock:
            changed = target in self.unavailable
            if changed:
                self.unavailable.remove(target)
                self.epochs[target] += 1
                self.observations.record_join()
            self.logger(event="peer_availability", target=target, reason=reason,
                        epoch=self.epochs[target], unavailable=False, changed=changed)
            return changed

    def disable(self):
        with self.lock:
            self.enabled = False
            for target in list(self.inflight):
                self.epochs[target] += 1

    def probe(self, target, *, rpc, permitted, timeout=2.0, trigger="rejoin"):
        """rpc(target, timeout) returns a GetStatus-compatible reply.

        Caller supplies transport; fake RPC makes tests network-free.
        No retry, no Forward RPC, and one in-flight check per target.
        """
        target = int(target)
        with self.lock:
            if not self.enabled or target not in self.unavailable or target in self.inflight:
                return False
            if not permitted(target):
                return False
            epoch = self.epochs[target]
            self.inflight.add(target)
        success = False
        error = None
        try:
            reply = rpc(target, timeout)
            success = (int(reply.peer_id) == target and
                       reply.ready is True and reply.alive is True)
        except Exception as exc:
            error = type(exc).__name__
        finally:
            with self.lock:
                self.inflight.discard(target)
                if (success and self.enabled and self.epochs[target] == epoch
                        and target in self.unavailable and permitted(target)):
                    self.unavailable.remove(target)
                    self.epochs[target] += 1
                    self.observations.record_join()
                    changed = True
                else:
                    changed = False
                self.logger(event="recovery_probe", target=target, trigger=trigger,
                            epoch=epoch, current_epoch=self.epochs[target],
                            positive=success, recovered=changed, error=error)
                return changed
