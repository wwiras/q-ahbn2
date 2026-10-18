"""P3G offline unit checks; no gRPC network, GKE, or scientific messages."""
import unittest
from types import SimpleNamespace

from recovery_availability import RecoveryAvailability, verify_get_status


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.state = RecoveryAvailability()
        self.assertTrue(self.state.mark_failed(5))

    def confirm(self, ticket, **overrides):
        values = dict(rpc_ok=True, returned_peer_id=5, ready=True,
                      alive=True, topology_permits=True)
        values.update(overrides)
        return self.state.finish_probe(ticket, **values)

    def test_first_and_duplicate_failure(self):
        self.assertFalse(self.state.mark_failed(5))
        self.assertTrue(self.state.is_excluded(5))

    def test_confirmed_recovery_and_idempotency(self):
        ticket = self.state.begin_probe(5)
        self.assertIsNotNone(ticket)
        self.assertIsNone(self.state.begin_probe(5))
        self.assertTrue(self.confirm(ticket))
        self.assertFalse(self.confirm(ticket))
        self.assertFalse(self.state.is_excluded(5))

    def test_wrong_identity(self):
        self.assertFalse(self.confirm(self.state.begin_probe(5), returned_peer_id=4))
        self.assertTrue(self.state.is_excluded(5))

    def test_not_ready(self):
        self.assertFalse(self.confirm(self.state.begin_probe(5), ready=False))

    def test_not_alive(self):
        self.assertFalse(self.confirm(self.state.begin_probe(5), alive=False))

    def test_topology_denied(self):
        self.assertFalse(self.confirm(self.state.begin_probe(5), topology_permits=False))

    def test_transport_failure(self):
        self.assertFalse(self.confirm(self.state.begin_probe(5), rpc_ok=False))

    def test_stale_success_after_new_failure(self):
        ticket = self.state.begin_probe(5)
        self.state.mark_failed(5)
        self.assertFalse(self.confirm(ticket))
        self.assertTrue(self.state.is_excluded(5))

    def test_unexcluded_cannot_probe(self):
        ticket = self.state.begin_probe(5)
        self.assertTrue(self.confirm(ticket))
        self.assertIsNone(self.state.begin_probe(5))

    def test_fake_rpc_success_and_timeout_argument(self):
        ticket = self.state.begin_probe(5)
        seen = []
        def fake(peer_id, timeout):
            seen.append((peer_id, timeout))
            return SimpleNamespace(peer_id=peer_id, ready=True, alive=True)
        result = verify_get_status(ticket, status_call=fake, timeout_s=0.5)
        self.assertEqual(result, (True, 5, True, True))
        self.assertEqual(seen, [(5, 0.5)])

    def test_fake_rpc_failure(self):
        ticket = self.state.begin_probe(5)
        def failure(peer_id, timeout):
            raise TimeoutError()
        self.assertEqual(verify_get_status(ticket, status_call=failure, timeout_s=0.5),
                         (False, None, False, False))

    def test_shared_exclusion_set_and_forward_ack(self):
        legacy = set()
        state = RecoveryAvailability(legacy)
        self.assertTrue(state.mark_failed(7))
        self.assertEqual(legacy, {7})
        self.assertFalse(state.mark_failed(7))
        self.assertTrue(state.mark_recovered(7))
        self.assertEqual(legacy, set())
        self.assertFalse(state.mark_recovered(7))

    def test_ack_invalidates_inflight_probe(self):
        state = RecoveryAvailability()
        state.mark_failed(7)
        ticket = state.begin_probe(7)
        self.assertTrue(state.mark_recovered(7))
        self.assertTrue(state.mark_failed(7))
        self.assertFalse(state.finish_probe(
            ticket, rpc_ok=True, returned_peer_id=7,
            ready=True, alive=True, topology_permits=True,
        ))
        self.assertTrue(state.is_excluded(7))

    def test_failed_probe_preserves_eligibility_exclusion(self):
        ticket = self.state.begin_probe(5)
        self.assertFalse(self.confirm(ticket, rpc_ok=False))
        self.assertTrue(self.state.is_excluded(5))
        self.assertIsNotNone(self.state.begin_probe(5))

    def test_invalid_timeout(self):
        ticket = self.state.begin_probe(5)
        with self.assertRaises(ValueError):
            verify_get_status(ticket, status_call=lambda *_: None, timeout_s=0)


if __name__ == "__main__":
    unittest.main()
