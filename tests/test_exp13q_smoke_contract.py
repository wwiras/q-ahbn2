import unittest

import qahbn2.formal_exp13q as exp13
from scripts.run_exp13q_smoke import (
    SMOKE_MESSAGES,
    SMOKE_METHODS,
    SMOKE_SEED,
)


class TestExp13QSmokeContract(unittest.TestCase):
    def test_smoke_is_bounded_and_nonformal(self):
        self.assertEqual(SMOKE_SEED, 42)
        self.assertEqual(SMOKE_MESSAGES, 260)
        self.assertEqual(SMOKE_METHODS, exp13.METHODS)
        self.assertLess(SMOKE_MESSAGES, 1000)

    def test_smoke_crosses_exactly_first_frozen_leave_rejoin_pair(self):
        self.assertGreaterEqual(SMOKE_MESSAGES, 251)
        self.assertLess(SMOKE_MESSAGES, 401)
        self.assertEqual(exp13.CYCLE_ONSETS[0], 201)
        self.assertEqual(exp13.REJOIN_BEFORE_MESSAGES[0], 251)


if __name__ == "__main__":
    unittest.main()
