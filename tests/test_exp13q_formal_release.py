import ast
import unittest
from pathlib import Path

import qahbn2.formal_exp13q as exp13
from scripts import run_exp13q_formal as runner


class TestExp13QFormalRelease(unittest.TestCase):
    def test_runner_pins_expected_provenance_and_matrix(self):
        self.assertEqual(
            runner.CANONICAL_AHBN_COMMIT,
            "936a79480bc1252c79b6ee01f65c88c740af2844",
        )
        self.assertEqual(len(exp13.EXPECTED_RUNS), 25)
        self.assertEqual(
            exp13.METHODS,
            ("gossip", "structured", "dcsoc", "ahbn", "qahbn2"),
        )
        self.assertEqual(exp13.SEEDS, (42, 43, 44, 45, 46))
        self.assertEqual(exp13.CHURN_LEVEL, 0.40)

    def test_runner_preserves_formal_workload_and_output_guard(self):
        self.assertEqual(runner.NUM_MESSAGES, 1000)
        source = Path("scripts/run_exp13q_formal.py").read_text(encoding="utf-8")
        self.assertIn('output_root = Path("output")', source)
        self.assertIn('"evidence"', source)
        self.assertIn("relative_to(output_root.resolve())", source)
        self.assertIn('"expected_runs": len(EXPECTED_RUNS)', source)
        self.assertIn('"completed_runs": len(rows)', source)
        self.assertIn('"exclusions": []', source)
        self.assertIn('"reruns": []', source)

    def test_runner_calls_only_frozen_cell_executor(self):
        tree = ast.parse(
            Path("scripts/run_exp13q_formal.py").read_text(encoding="utf-8")
        )
        calls = [
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ]
        self.assertIn("run_exp13q_cell", calls)
        self.assertNotIn("run_exp11q_cell", calls)
        self.assertNotIn("run_exp12q_cell", calls)


if __name__ == "__main__":
    unittest.main()
