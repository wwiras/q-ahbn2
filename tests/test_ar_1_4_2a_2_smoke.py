"""AR-1.4.2A.2 deterministic one-seed end-to-end smoke."""

import unittest

from scripts.run_ar_1_4_2a_2_smoke import run_smoke


class TestAR142A2Smoke(unittest.TestCase):
    def test_seed42_end_to_end(self):
        out = run_smoke()
        self.assertEqual(out["seed"], 42)
        self.assertEqual(out["gamma_fixture"], 0.80)
        self.assertEqual(out["d1_ahbn"], ("gossip", 3))
        self.assertEqual(out["d1_q"], ("gossip", 3))
        self.assertEqual(out["d1_outcomes"], ("NEW", "NEW", "NEW"))
        self.assertEqual(out["d1_reward"], 1.0)
        self.assertTrue(out["d1_updated"])
        self.assertEqual(out["d2_outcomes"], ("NEW", "NEW"))
        self.assertEqual(out["d2_reward"], 1.0)
        self.assertTrue(out["d2_terminal"])
        self.assertTrue(out["d2_updated"])
        self.assertEqual(out["q_updates"], 2)


if __name__ == "__main__":
    unittest.main()
