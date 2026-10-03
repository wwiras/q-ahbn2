import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "gke/app/qahbn2_runtime.py"
PEER = ROOT / "gke/app/peer.py"


class TestS172ForwardInstrumentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime_text = RUNTIME.read_text()
        cls.peer_text = PEER.read_text()
        cls.runtime_tree = ast.parse(cls.runtime_text)
        cls.peer_tree = ast.parse(cls.peer_text)
        cls.forward_fn = next(
            n for n in cls.runtime_tree.body
            if isinstance(n, ast.FunctionDef) and n.name == "_forward"
        )

    @staticmethod
    def _event_value(call):
        if not isinstance(call, ast.Call):
            return None
        func = call.func
        if not (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "peer"
            and func.attr == "log_event"
        ):
            return None
        for kw in call.keywords:
            if kw.arg == "event" and isinstance(kw.value, ast.Constant):
                return kw.value.value
        return None

    @classmethod
    def _logged_events(cls, node):
        events = []
        nodes = node if isinstance(node, list) else [node]
        for root in nodes:
            for child in ast.walk(root):
                if isinstance(child, ast.Call):
                    value = cls._event_value(child)
                    if value is not None:
                        events.append(value)
        return events

    def _strategy_guard(self):
        return next(
            n for n in self.forward_fn.body
            if isinstance(n, ast.If)
            and isinstance(n.test, ast.Compare)
            and isinstance(n.test.left, ast.Attribute)
            and n.test.left.attr == "strategy"
        )

    def _decision_fallback(self):
        return next(
            n for n in self.forward_fn.body
            if isinstance(n, ast.If)
            and isinstance(n.test, ast.Compare)
            and isinstance(n.test.left, ast.Name)
            and n.test.left.id == "decision_id"
        )

    def _rpc_outcome_if(self):
        for n in ast.walk(self.forward_fn):
            if (
                isinstance(n, ast.If)
                and isinstance(n.test, ast.Attribute)
                and n.test.attr == "ok"
            ):
                return n
        self.fail("resp.ok outcome branch missing")

    def test_new_has_exactly_one_generic_forward_and_traceability(self):
        outcome_if = self._rpc_outcome_if()
        self.assertEqual(self._logged_events(outcome_if.body), ["forward"])
        forward_call = next(
            c for n in outcome_if.body for c in ast.walk(n)
            if isinstance(c, ast.Call) and self._event_value(c) == "forward"
        )
        fields = {kw.arg for kw in forward_call.keywords}
        inherited = {
            "event", "run_id", "experiment", "peer_id", "dst_peer",
            "src_peer", "message_id", "strategy", "mode", "fanout",
            "overload_ms", "bottleneck_active", "bottleneck_delay_ms",
            "is_cluster_head",
        }
        self.assertTrue(inherited.issubset(fields))
        self.assertIn("decision_id", fields)

    def test_duplicate_and_failed_have_no_generic_forward(self):
        outcome_if = self._rpc_outcome_if()
        duplicate_branch = outcome_if.orelse[0]
        self.assertIsInstance(duplicate_branch, ast.If)
        self.assertNotIn("forward", self._logged_events(duplicate_branch.body))
        self.assertNotIn("forward", self._logged_events(duplicate_branch.orelse))

        handlers = [
            n for n in ast.walk(self.forward_fn)
            if isinstance(n, ast.ExceptHandler)
        ]
        self.assertTrue(handlers)
        for handler in handlers:
            self.assertNotIn("forward", self._logged_events(handler))

    def test_success_count_cannot_exceed_attempt_count_by_runtime_structure(self):
        # Every invocation logs one attempt before any delegation/outcome path.
        top_events = []
        for stmt in self.forward_fn.body:
            top_events.extend(self._logged_events(stmt))
            if isinstance(stmt, ast.If):
                break
        self.assertEqual(top_events.count("k7_forward_attempt"), 1)

        outcome_if = self._rpc_outcome_if()
        self.assertEqual(self._logged_events(outcome_if.body).count("forward"), 1)
        self.assertNotIn("forward", self._logged_events(outcome_if.orelse))

        attempt_pos = self.runtime_text.index('event="k7_forward_attempt"')
        success_pos = self.runtime_text.index('event="forward"', attempt_pos)
        self.assertLess(attempt_pos, success_pos)

    def test_qahbn2_fallback_delegates_once_without_local_success_log(self):
        fallback = self._decision_fallback()
        calls = [
            n for n in ast.walk(fallback)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == "_ORIGINAL_FORWARD"
        ]
        self.assertEqual(len(calls), 1)
        self.assertNotIn("forward", self._logged_events(fallback))

    def test_non_qahbn2_path_is_pure_single_delegation(self):
        guard = self._strategy_guard()
        calls = [
            n for n in ast.walk(guard)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name)
            and n.func.id == "_ORIGINAL_FORWARD"
        ]
        self.assertEqual(len(calls), 1)
        self.assertNotIn("forward", self._logged_events(guard))

        # Inherited successful-forward instrumentation remains present.
        self.assertIn('event="forward"', self.peer_text)


if __name__ == "__main__":
    unittest.main()
