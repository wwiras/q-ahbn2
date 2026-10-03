"""Deployable Q-AHBN2 wrapper over the pinned ahbn2_gke peer runtime.

This module is intentionally additive: standalone Gossip, Structured, DC-SoC,
and AHBN behavior remain delegated to the inherited peer runtime. Only
strategy='qahbn2' receives the frozen post-AHBN learning/refinement layer.
"""
from __future__ import annotations

import threading

import peer
import k7_rpc_trace
from k5_final_actuator_policy import requested_fanout
from qahbn2.kubernetes_adapter import KubernetesQAHBN2Adapter
from qahbn2.kubernetes_integration import realize_inherited_targets, register_realized_targets
from qahbn2.learning import QAHBN2Learner


_ORIGINAL_INIT = peer.PeerState.__init__
_ORIGINAL_TARGETS = peer.PeerState.target_peers
_ORIGINAL_FORWARD = peer.PeerState.forward_to_peer
_ORIGINAL_ADAPTIVE = peer.PeerState.adaptive_update


def _init(self):
    _ORIGINAL_INIT(self)
    if self.strategy != "qahbn2":
        return
    # Reuse the inherited AHBN controller/observation path exactly for Q-AHBN2.
    self.ahbn_params = peer.AHBNParams()
    self.default_fanout = self.ahbn_params.default_fanout
    self.mode_threshold = self.ahbn_params.mode_threshold
    self.min_fanout = self.ahbn_params.min_fanout
    self.max_fanout = self.ahbn_params.max_fanout
    self.ahbn_controller = peer.CanonicalAHBNController(self.ahbn_params)
    self.ahbn_state = peer.AHBNState(fanout=self.ahbn_params.default_fanout)
    self.observations = peer.KubernetesObservationAdapter(latency_max_seconds=1.0)
    self.mode = "gossip"
    self.fanout = self.default_fanout
    seed = int(getattr(self, "h2_seed", 42))
    self.qahbn2_adapter = KubernetesQAHBN2Adapter(QAHBN2Learner(seed=seed))
    self.qahbn2_decisions = {}
    self.qahbn2_lock = threading.Lock()


def _adaptive_update(self):
    if self.strategy == "qahbn2":
        # Temporarily present as AHBN only to enter the inherited canonical path.
        strategy = self.strategy
        self.strategy = "ahbn"
        try:
            return _ORIGINAL_ADAPTIVE(self)
        finally:
            self.strategy = strategy
    return _ORIGINAL_ADAPTIVE(self)


def _targets(self, sender_id: int, message_id: str | None = None):
    if self.strategy == "ahbn":
        self.adaptive_update()
        score = self.ahbn_state.score
        budget = requested_fanout("S5", score)
        if self.mode == "cluster":
            eligible = self.diagnostic_cluster_eligible_peers(sender_id)
            targets = self.cluster_targets(sender_id, fanout=budget)
        else:
            eligible = [n for n in self.neighbors if n not in (sender_id, self.peer_id) and n not in self.unavailable_neighbors]
            k = min(budget, len(eligible))
            targets = self.rng.sample(eligible, k) if k > 0 else []
            targets = list(dict.fromkeys(targets))
        canonical_fanout = self.fanout
        self.fanout = budget
        peer.log_event(event="k5_final_actuator_decision", run_id=self.run_id,
            experiment=self.experiment, peer_id=self.peer_id, treatment="S5",
            message_id=message_id, sender=self.peer_id, incoming_sender=sender_id,
            score=score, weight=self.ahbn_state.weight, mode=self.mode,
            eligible_neighbor_count=len(set(eligible)), canonical_fanout=canonical_fanout,
            requested_fanout=budget, actual_fanout=len(targets))
        self.log_ahbn_forwarding_decision(sender_id, message_id, eligible, targets)
        return targets
    if self.strategy != "qahbn2":
        return _ORIGINAL_TARGETS(self, sender_id, message_id)

    self.adaptive_update()
    score = self.ahbn_state.score
    k_ahbn = requested_fanout("S5", score)
    mode_ahbn = "structured" if self.mode == "cluster" else "gossip"
    q = self.qahbn2_adapter.decide(
        peer_id=self.peer_id,
        message_id=str(message_id),
        d_hat=self.ahbn_state.d_hat,
        l_hat=self.ahbn_state.l_hat,
        u_hat=self.ahbn_state.u_hat,
        c_hat=self.ahbn_state.c_hat,
        mode_ahbn=mode_ahbn,
        k_ahbn=k_ahbn,
    )

    gossip_eligible = [
        n for n in self.neighbors
        if n not in (sender_id, self.peer_id)
        and n not in self.unavailable_neighbors
    ]
    realized = realize_inherited_targets(
        q=q,
        sender_id=sender_id,
        gossip_eligible=gossip_eligible,
        structured_selector=lambda s, budget: self.cluster_targets(s, fanout=budget),
        rng_sample=lambda population, k: self.rng.sample(list(population), k),
    )
    register_realized_targets(self.qahbn2_adapter, realized)
    with self.qahbn2_lock:
        self.qahbn2_decisions[str(message_id)] = q.decision_id

    self.mode = "cluster" if q.mode_q == "structured" else "gossip"
    self.fanout = q.k_q
    peer.log_event(
        event="qahbn2_decision",
        run_id=self.run_id,
        experiment=self.experiment,
        peer_id=self.peer_id,
        message_id=message_id,
        decision_id=q.decision_id,
        state=q.state,
        action=q.action,
        d_hat=q.d_hat,
        l_hat=q.l_hat,
        u_hat=q.u_hat,
        c_hat=q.c_hat,
        ahbn_score=self.ahbn_state.score,
        ahbn_weight=self.ahbn_state.weight,
        mode_ahbn=q.mode_ahbn,
        k_ahbn=q.k_ahbn,
        mode_q=q.mode_q,
        k_q=q.k_q,
        eligible_targets=list(realized.eligible_targets),
        realized_targets=list(realized.realized_targets),
    )
    return list(realized.realized_targets)


def _forward(self, dst_peer, envelope):
    peer.log_event(
        event="k7_forward_attempt", run_id=self.run_id, experiment=self.experiment,
        msg_id=envelope.message_id, message_id=envelope.message_id,
        sender=self.peer_id, destination_peer=dst_peer, strategy=self.strategy,
        mode=self.mode, fanout=self.fanout,
        sender_role=getattr(self, "dcsoc_role", None) if self.strategy == "dcsoc" else None,
        structured_is_cluster_head=bool(getattr(self, "is_cluster_head", False)) if self.strategy == "cluster" else None,
        structured_cluster_head_id=getattr(self, "cluster_head_id", None) if self.strategy == "cluster" else None,
        structured_gateway_neighbors=list(getattr(self, "gateway_neighbors", [])) if self.strategy == "cluster" else None,
    )
    if self.strategy != "qahbn2":
        return _ORIGINAL_FORWARD(self, dst_peer, envelope)
    decision_id = self.qahbn2_decisions.get(str(envelope.message_id))
    if decision_id is None:
        return _ORIGINAL_FORWARD(self, dst_peer, envelope)

    addr = self.peer_dns(dst_peer)
    try:
        with peer.grpc.insecure_channel(addr) as channel:
            stub = peer.peer_pb2_grpc.PeerServiceStub(channel)
            resp = stub.Forward(envelope, timeout=3)
            if resp.ok:
                self.forward_count += 1
                if dst_peer in self.unavailable_neighbors:
                    self.unavailable_neighbors.remove(dst_peer)
                    self.observations.record_join()
                self.qahbn2_adapter.record_ack(decision_id, dst_peer, ack_ok=True)
                # S17: preserve the inherited successful-forward accounting
                # semantics for decision-bound Q-AHBN2 sends. This event is
                # instrumentation only; forwarding and learning are unchanged.
                peer.log_event(
                    event="forward",
                    run_id=self.run_id,
                    experiment=self.experiment,
                    peer_id=self.peer_id,
                    dst_peer=dst_peer,
                    src_peer=envelope.sender_id,
                    message_id=envelope.message_id,
                    strategy=self.strategy,
                    mode=self.mode,
                    fanout=self.fanout,
                    overload_ms=self.overload_ms,
                    bottleneck_active=self.bottleneck_active,
                    bottleneck_delay_ms=self.bottleneck_delay_ms,
                    is_cluster_head=self.is_cluster_head,
                    decision_id=decision_id,
                )
                outcome = "NEW"
            elif resp.message == "duplicate":
                if dst_peer in self.unavailable_neighbors:
                    self.unavailable_neighbors.remove(dst_peer)
                    self.observations.record_join()
                self.qahbn2_adapter.record_ack(decision_id, dst_peer, ack_ok=False)
                outcome = "DUPLICATE"
            else:
                if dst_peer not in self.unavailable_neighbors:
                    self.unavailable_neighbors.add(dst_peer)
                    self.observations.record_leave()
                self.qahbn2_adapter.record_failure(decision_id, dst_peer)
                outcome = "FAILED"
            peer.log_event(
                event="qahbn2_attempt_outcome", run_id=self.run_id,
                peer_id=self.peer_id, message_id=envelope.message_id,
                decision_id=decision_id, dst_peer=dst_peer, outcome=outcome,
            )
    except Exception as exc:
        if dst_peer not in self.unavailable_neighbors:
            self.unavailable_neighbors.add(dst_peer)
            self.observations.record_leave()
        self.qahbn2_adapter.record_failure(decision_id, dst_peer)
        peer.log_event(
            event="qahbn2_attempt_outcome", run_id=self.run_id,
            peer_id=self.peer_id, message_id=envelope.message_id,
            decision_id=decision_id, dst_peer=dst_peer, outcome="FAILED",
            error=str(exc),
        )

    ledger = self.qahbn2_adapter.ledger(decision_id)
    if ledger.complete:
        rec = self.qahbn2_adapter.learner.transitions.get(decision_id)
        peer.log_event(
            event="qahbn2_reward_closed", run_id=self.run_id,
            peer_id=self.peer_id, message_id=envelope.message_id,
            decision_id=decision_id,
            new=ledger.counts()[0], duplicate=ledger.counts()[1],
            failed=ledger.counts()[2],
            reward=rec.reward_t,
            no_forwarding_evidence=rec.no_forwarding_evidence,
            update_count=self.qahbn2_adapter.learner.update_count,
        )


peer.PeerState.__init__ = _init
peer.PeerState.adaptive_update = _adaptive_update
peer.PeerState.target_peers = _targets
peer.PeerState.forward_to_peer = _forward
k7_rpc_trace.install(peer)

if __name__ == "__main__":
    peer.serve()
