"""P3G-V1: integration checks against the actual PeerState class.

Run from repository root:
    PYTHONPATH=gke/app python -m unittest tests.test_p3g_peerstate_integration -v

These tests bypass pod startup only; the forwarding, recovery and target methods
are the production PeerState implementation. No GKE or real gRPC is used.
"""
import random
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from peer import PeerState
from recovery_availability import RecoveryAvailability


class CountingObservations:
    def __init__(self):
        self.joins = 0
        self.leaves = 0

    def record_join(self):
        self.joins += 1

    def record_leave(self):
        self.leaves += 1


class FakeChannel:
    def __init__(self, stub):
        self.stub = stub

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


class P3GPeerStateIntegration(unittest.TestCase):
    def setUp(self):
        self.observations = CountingObservations()
        self.state = PeerState.__new__(PeerState)
        s = self.state
        s.peer_id = 1
        s.run_id = "p3g-offline"
        s.experiment = "p3g-offline"
        s.strategy = "gossip"
        s.neighbors = [4]
        s.default_fanout = None
        s.rng = random.Random(42)
        s.failed = False
        s.namespace = "default"
        s.peer_service_name = "ahbn-peer"
        s.grpc_port = 50051
        s.forward_count = 0
        s.recv_count = 0
        s.duplicate_count = 0
        s.mode = "gossip"
        s.fanout = 3
        s.overload_ms = 0
        s.bottleneck_active = False
        s.bottleneck_delay_ms = 0
        s.is_cluster_head = False
        s.dcsoc_maintenance = None
        s.unavailable_neighbors = set()
        s.observations = self.observations
        s.recovery = RecoveryAvailability(
            s.unavailable_neighbors, self.observations, enabled=True)
        self.status_reply = SimpleNamespace(peer_id=4, ready=True, alive=True)
        self.forward_reply = SimpleNamespace(ok=True, message="ok")
        self.calls = []

    def stub(self, _):
        outer = self
        class Stub:
            def GetStatus(self, request, timeout):
                outer.calls.append(("GetStatus", timeout))
                return outer.status_reply

            def Forward(self, request, timeout):
                outer.calls.append(("Forward", timeout))
                return outer.forward_reply
        return Stub()

    def rpc(self):
        return (
            patch("peer.grpc.insecure_channel",
                  side_effect=lambda *_: FakeChannel(None)),
            patch("peer.peer_pb2_grpc.PeerServiceStub",
                  side_effect=self.stub),
        )

    def exclude(self):
        self.state.recovery.failure(4)

    def test_churn_rejoin_notification_calls_production_peerstate(self):
        self.exclude()
        a, b = self.rpc()
        with a, b:
            self.assertTrue(self.state.notify_recovery_rejoin(4))
        self.assertEqual(self.state.target_peers(sender_id=0), [4])
        self.assertEqual(self.calls, [("GetStatus", 2.0)])

    def test_churn_rejoin_notification_rejects_non_neighbor(self):
        self.state.recovery.failure(7)
        a, b = self.rpc()
        with a, b:
            self.assertFalse(self.state.notify_recovery_rejoin(7))
        self.assertEqual(self.calls, [])

    def test_churn_rejoin_notification_noop_when_disabled(self):
        self.exclude()
        self.state.recovery.disable()
        a, b = self.rpc()
        with a, b:
            self.assertFalse(self.state.notify_recovery_rejoin(4))
        self.assertIn(4, self.state.unavailable_neighbors)
        self.assertEqual(self.calls, [])

    def test_service_rejoin_rpc_invokes_real_recovery(self):
        from peer import PeerService
        from peer import peer_pb2
        self.exclude()
        request = peer_pb2.DCSOCMaintenanceRequest(
            node_id=4, available=True, reason="k7_churn_rejoin"
        )
        a, b = self.rpc()
        with a, b:
            reply = PeerService(self.state).NotifyRecoveryRejoin(request, None)
        self.assertTrue(reply.ok)
        self.assertEqual(reply.message, "recovered")
        self.assertEqual(self.observations.joins, 1)

    def test_real_target_excluded_then_restored_after_verified_status(self):
        self.assertEqual(self.state.target_peers(sender_id=0), [4])
        self.exclude()
        self.assertEqual(self.state.target_peers(sender_id=0), [])
        a, b = self.rpc()
        with a, b:
            self.assertTrue(self.state.probe_recovery(4))
        self.assertEqual(self.state.target_peers(sender_id=0), [4])
        self.assertEqual((self.observations.leaves, self.observations.joins),
                         (1, 1))
        self.assertEqual(self.calls, [("GetStatus", 2.0)])

    def test_real_peerstate_status_probe_does_not_forward_or_change_metrics(self):
        self.exclude()
        before = (self.state.forward_count, self.state.recv_count,
                  self.state.duplicate_count)
        a, b = self.rpc()
        with a, b:
            self.assertTrue(self.state.probe_recovery(4))
        self.assertEqual(
            (self.state.forward_count, self.state.recv_count,
             self.state.duplicate_count), before)
        self.assertTrue(all(name != "Forward" for name, _ in self.calls))

    def test_wrong_status_identity_keeps_real_target_excluded(self):
        self.exclude()
        self.status_reply = SimpleNamespace(peer_id=7, ready=True, alive=True)
        a, b = self.rpc()
        with a, b:
            self.assertFalse(self.state.probe_recovery(4))
        self.assertEqual(self.state.target_peers(sender_id=0), [])

    def test_real_forward_ack_transitions_exactly_once(self):
        self.exclude()
        request = SimpleNamespace(sender_id=1, message_id="m1")
        a, b = self.rpc()
        with a, b, patch("peer.log_event"):
            self.state.forward_to_peer(4, request)
            self.state.forward_to_peer(4, request)
        self.assertEqual(self.observations.joins, 1)
        self.assertEqual(self.state.forward_count, 2)

    def test_real_forward_failure_records_one_leave(self):
        self.forward_reply = SimpleNamespace(ok=False, message="rejected")
        request = SimpleNamespace(sender_id=1, message_id="m1")
        a, b = self.rpc()
        with a, b, patch("peer.log_event"):
            self.state.forward_to_peer(4, request)
            self.state.forward_to_peer(4, request)
        self.assertEqual(self.observations.leaves, 1)
        self.assertEqual(self.state.target_peers(sender_id=0), [])

    def test_disabled_recovery_preserves_exclusion(self):
        self.exclude()
        self.state.recovery.disable()
        a, b = self.rpc()
        with a, b:
            self.assertFalse(self.state.probe_recovery(4))
        self.assertEqual(self.calls, [])
        self.assertEqual(self.state.target_peers(sender_id=0), [])

    def test_non_neighbour_cannot_be_recovered(self):
        self.state.recovery.failure(7)
        a, b = self.rpc()
        with a, b:
            self.assertFalse(self.state.probe_recovery(7))
        self.assertEqual(self.calls, [])

    def test_stale_positive_response_cannot_override_new_failure(self):
        self.exclude()
        def stub(_):
            outer = self
            class Stub:
                def GetStatus(self, request, timeout):
                    outer.state.recovery.failure(4)
                    return outer.status_reply
            return Stub()
        with (patch("peer.grpc.insecure_channel",
                    side_effect=lambda *_: FakeChannel(None)),
              patch("peer.peer_pb2_grpc.PeerServiceStub", side_effect=stub)):
            self.assertFalse(self.state.probe_recovery(4))
        self.assertIn(4, self.state.unavailable_neighbors)
        self.assertEqual(self.observations.joins, 0)


if __name__ == "__main__":
    unittest.main()
