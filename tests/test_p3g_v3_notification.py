"""P3G-V3 controller-to-peer fake-gRPC verification. No cluster access."""
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import controller_shared as controller
from peer import PeerService, PeerState
from recovery_availability import RecoveryAvailability


class Sink:
    def __init__(self):
        self.joins = 0
        self.leaves = 0
    def record_join(self):
        self.joins += 1
    def record_leave(self):
        self.leaves += 1


class Channel:
    def __init__(self, address, endpoints):
        self.address = address
        self.endpoints = endpoints
    def __enter__(self):
        return self
    def __exit__(self, *_):
        return False


class EndToEndNotification(unittest.TestCase):
    def setUp(self):
        self.sink = Sink()
        p = PeerState.__new__(PeerState)
        p.peer_id = 1
        p.neighbors = [4]
        p.strategy = "ahbn"
        p.unavailable_neighbors = set()
        p.dcsoc_maintenance = None
        p.run_id = "p3g-v3"
        p.experiment = "p3g-v3"
        p.namespace = "ns"
        p.peer_service_name = "svc"
        p.grpc_port = 50051
        p.forward_count = p.recv_count = p.duplicate_count = 0
        p.recovery = RecoveryAvailability(p.unavailable_neighbors, self.sink, enabled=True)
        self.peer = p
        self.sink = self.sink
        self.peer.recovery.failure(4)
        self.topology = {"strategy": "ahbn", "nodes": {
            "0": {"neighbors": [4]},
            "1": {"neighbors": [4]},
            "2": {"neighbors": [3]},
            "4": {"neighbors": [0, 1]},
        }}
        self.called = []
        self.status = SimpleNamespace(peer_id=4, ready=True, alive=True)
        self.down = set()
        self.endpoints = {}
        self.endpoints["peer-1.svc.ns.svc.cluster.local:50051"] = self.peer
        self.endpoints["peer-0.svc.ns.svc.cluster.local:50051"] = "survivor"

    def channel(self, address):
        return Channel(address, self.endpoints)

    def stub(self, channel):
        t = self
        class Stub:
            def NotifyRecoveryRejoin(self, request, timeout):
                t.called.append(("NotifyRecoveryRejoin", channel.address, timeout))
                if channel.address in t.down:
                    raise TimeoutError("notification unavailable")
                owner = t.endpoints[channel.address]
                if owner == "survivor":
                    return SimpleNamespace(ok=True, message="recovery disabled")
                return PeerService(owner).NotifyRecoveryRejoin(request, None)
            def GetStatus(self, request, timeout):
                t.called.append(("GetStatus", channel.address, timeout))
                if channel.address in t.down:
                    raise TimeoutError("status unavailable")
                return t.status
            def Forward(self, request, timeout):
                raise AssertionError("recovery must not forward")
        return Stub()

    def dispatch(self):
        with patch.object(controller.grpc, "insecure_channel", side_effect=self.channel), \
             patch.object(controller.peer_pb2_grpc, "PeerServiceStub", side_effect=self.stub), \
             patch("peer.grpc.insecure_channel", side_effect=self.channel), \
             patch("peer.peer_pb2_grpc.PeerServiceStub", side_effect=self.stub), \
             patch.object(controller, "log_event"):
            return controller.notify_recovery_rejoin(
                self.topology, 4, "svc", "ns", 50051)

    def test_ahbn_full_path(self):
        result = self.dispatch()
        self.assertEqual((result["attempted"], result["acknowledged"]), (2, 2))
        self.assertNotIn(4, self.peer.unavailable_neighbors)
        self.assertEqual((self.sink.leaves, self.sink.joins), (1, 1))
        self.assertEqual(len([x for x in self.called if x[0] == "GetStatus"]), 1)
        self.assertEqual((self.peer.forward_count, self.peer.recv_count,
                          self.peer.duplicate_count), (0, 0, 0))

    def test_qahbn2_full_path(self):
        self.topology["strategy"] = "qahbn2"
        self.peer.strategy = "qahbn2"
        result = self.dispatch()
        self.assertEqual(result["acknowledged"], 2)
        self.assertEqual(self.sink.joins, 1)

    def test_failed_getstatus_does_not_clear(self):
        self.status = SimpleNamespace(peer_id=4, ready=False, alive=True)
        result = self.dispatch()
        self.assertEqual(result["acknowledged"], 2)
        self.assertIn(4, self.peer.unavailable_neighbors)
        self.assertEqual(self.sink.joins, 0)

    def test_notification_delivery_failure_is_recorded(self):
        self.down.add("peer-1.svc.ns.svc.cluster.local:50051")
        result = self.dispatch()
        self.assertEqual(result["acknowledged"], 1)
        self.assertEqual(result["errors"], [{"peer_id": 1, "error": "TimeoutError"}])
        self.assertIn(4, self.peer.unavailable_neighbors)

    def test_duplicate_notification_no_second_join(self):
        self.dispatch()
        self.dispatch()
        self.assertEqual(self.sink.joins, 1)

    def test_rollback_enabled_false(self):
        self.peer.recovery.disable()
        self.dispatch()
        self.assertIn(4, self.peer.unavailable_neighbors)
        self.assertEqual(self.sink.joins, 0)
        self.assertFalse(any(x[0] == "GetStatus" for x in self.called))

    def test_non_neighbors_not_notified(self):
        self.dispatch()
        endpoints = [x[1] for x in self.called if x[0] == "NotifyRecoveryRejoin"]
        self.assertEqual(endpoints, [
            "peer-0.svc.ns.svc.cluster.local:50051",
            "peer-1.svc.ns.svc.cluster.local:50051",
        ])

    def test_unrelated_strategy_not_notified(self):
        self.topology["strategy"] = "dcsoc"
        result = self.dispatch()
        self.assertEqual(result["attempted"], 0)
        self.assertEqual(self.called, [])

    def test_new_failure_invalidates_late_status(self):
        original = self.stub
        def delayed_stub(channel):
            obj = original(channel)
            original_get = obj.GetStatus
            def delayed(request, timeout):
                self.peer.recovery.failure(4)
                return original_get(request, timeout)
            obj.GetStatus = delayed
            return obj
        with patch.object(controller.grpc, "insecure_channel", side_effect=self.channel), \
             patch.object(controller.peer_pb2_grpc, "PeerServiceStub", side_effect=delayed_stub), \
             patch("peer.grpc.insecure_channel", side_effect=self.channel), \
             patch("peer.peer_pb2_grpc.PeerServiceStub", side_effect=delayed_stub), \
             patch.object(controller, "log_event"):
            controller.notify_recovery_rejoin(self.topology, 4, "svc", "ns", 50051)
        self.assertIn(4, self.peer.unavailable_neighbors)
        self.assertEqual(self.sink.joins, 0)


if __name__ == "__main__":
    unittest.main()
