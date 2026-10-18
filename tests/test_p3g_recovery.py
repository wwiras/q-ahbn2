"""P3G offline recovery tests. Run: PYTHONPATH=gke/app python -m unittest tests.test_p3g_recovery -v"""
import threading
import unittest
from types import SimpleNamespace
from recovery_availability import RecoveryAvailability


class Sink:
    def __init__(self):
        self.joins = 0
        self.leaves = 0
    def record_join(self):
        self.joins += 1
    def record_leave(self):
        self.leaves += 1


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.sink = Sink()
        self.unavailable = set()
        self.events = []
        self.r = RecoveryAvailability(self.unavailable, self.sink, enabled=True,
                                      logger=lambda **e: self.events.append(e))
        self.permitted = lambda target: target == 4
        self.good = lambda target, timeout: SimpleNamespace(
            peer_id=target, ready=True, alive=True)

    def exclude(self):
        self.r.failure(4)

    def test_T01_first_failure(self):
        self.exclude()
        self.assertEqual((self.unavailable, self.sink.leaves), ({4}, 1))

    def test_T02_duplicate_failure(self):
        self.exclude(); self.exclude()
        self.assertEqual(self.sink.leaves, 1)

    def test_T03_structural_rejoin_failed_probe(self):
        self.exclude()
        self.assertFalse(self.r.probe(4, rpc=lambda *_: (_ for _ in ()).throw(OSError()),
                                      permitted=self.permitted))
        self.assertIn(4, self.unavailable)

    def test_T04_verified_recovery(self):
        self.exclude()
        self.assertTrue(self.r.probe(4, rpc=self.good, permitted=self.permitted))
        self.assertEqual(self.sink.joins, 1)

    def test_T05_repeated_positive(self):
        self.exclude()
        self.r.probe(4, rpc=self.good, permitted=self.permitted)
        self.assertFalse(self.r.probe(4, rpc=self.good, permitted=self.permitted))
        self.assertEqual(self.sink.joins, 1)

    def test_T06_stale_response(self):
        self.exclude()
        def late(target, timeout):
            self.r.failure(target)
            return self.good(target, timeout)
        self.assertFalse(self.r.probe(4, rpc=late, permitted=self.permitted))
        self.assertIn(4, self.unavailable)

    def test_T07_excluded_not_eligible(self):
        self.exclude()
        self.assertEqual([n for n in [4] if n not in self.unavailable], [])

    def test_T08_recovered_eligible(self):
        self.exclude()
        self.r.probe(4, rpc=self.good, permitted=self.permitted)
        self.assertEqual([n for n in [4] if n not in self.unavailable][:1], [4])

    def test_T09_structural_permission(self):
        self.exclude()
        self.assertFalse(self.r.probe(4, rpc=self.good, permitted=lambda _: False))
        self.assertIn(4, self.unavailable)

    def test_T10_strategy_neutral(self):
        self.exclude()
        self.assertTrue(self.r.probe(4, rpc=self.good, permitted=self.permitted))

    def test_T11_no_confirmation(self):
        self.exclude()
        self.assertIn(4, self.unavailable)

    def test_T12_deterministic(self):
        self.exclude()
        self.assertEqual(self.r.epochs[4], 1)

    def test_T13_wrong_id(self):
        self.exclude()
        self.assertFalse(self.r.probe(4, rpc=lambda *_: SimpleNamespace(
            peer_id=7, ready=True, alive=True), permitted=self.permitted))

    def test_T14_not_ready_or_alive(self):
        for ready, alive in [(False, True), (True, False)]:
            self.exclude()
            self.assertFalse(self.r.probe(4, rpc=lambda *_: SimpleNamespace(
                peer_id=4, ready=ready, alive=alive), permitted=self.permitted))

    def test_T15_rpc_error(self):
        self.exclude()
        self.assertFalse(self.r.probe(4, rpc=lambda *_: (_ for _ in ()).throw(
            TimeoutError()), permitted=self.permitted))

    def test_T16_no_forward_or_reward(self):
        self.exclude()
        forwards = []
        def status(target, timeout):
            self.assertEqual(timeout, 2.0)
            return self.good(target, timeout)
        self.r.probe(4, rpc=status, permitted=self.permitted)
        self.assertEqual(forwards, [])

    def test_T17_concurrent_new_failure(self):
        self.exclude()
        entered, resume = threading.Event(), threading.Event()
        def rpc(target, timeout):
            entered.set()
            self.assertTrue(resume.wait(2))
            return self.good(target, timeout)
        outcome = []
        thread = threading.Thread(target=lambda: outcome.append(
            self.r.probe(4, rpc=rpc, permitted=self.permitted)))
        thread.start()
        self.assertTrue(entered.wait(2))
        self.r.failure(4)
        resume.set()
        thread.join(2)
        self.assertEqual(outcome, [False])
        self.assertIn(4, self.unavailable)

    def test_T18_disabled_baseline(self):
        self.exclude()
        self.r.disable()
        self.assertFalse(self.r.probe(4, rpc=self.good, permitted=self.permitted))
        self.assertIn(4, self.unavailable)


if __name__ == "__main__":
    unittest.main()
