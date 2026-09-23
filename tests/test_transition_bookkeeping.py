"""AR-1.4.1B.2 deterministic tests for Q-AHBN2 transition bookkeeping."""

import unittest

from qahbn2.transition import TransitionBookkeeper


S1 = ("L", "L", "L", "L")
S2 = ("M", "L", "L", "L")
S3 = ("H", "M", "L", "L")


class TestTransitionBookkeeping(unittest.TestCase):
    def test_1_sequential_transition(self):
        book = TransitionBookkeeper()
        t1 = book.begin_decision(
            decision_id="d1", peer_id=7, message_id="m1",
            state_t=S1, action_t="KEEP",
        )
        book.attach_reward("d1", 0.5)
        self.assertFalse(t1.update_ready)

        book.begin_decision(
            decision_id="d2", peer_id=7, message_id="m2",
            state_t=S2, action_t="FANOUT_UP",
        )

        self.assertEqual(t1.next_state, S2)
        self.assertEqual(t1.reward_t, 0.5)
        self.assertTrue(t1.update_ready)
        self.assertEqual(t1.bootstrap_state, S2)

    def test_2_next_state_before_reward(self):
        book = TransitionBookkeeper()
        t1 = book.begin_decision(
            decision_id="d1", peer_id=7, message_id="m1",
            state_t=S1, action_t="KEEP",
        )
        book.begin_decision(
            decision_id="d2", peer_id=7, message_id="m2",
            state_t=S2, action_t="SET_GOSSIP",
        )

        self.assertTrue(t1.next_ready)
        self.assertFalse(t1.reward_ready)
        self.assertFalse(t1.update_ready)

        book.attach_reward("d1", 0.25)
        self.assertTrue(t1.update_ready)
        self.assertEqual(t1.next_state, S2)

    def test_3_reward_before_next_state(self):
        book = TransitionBookkeeper()
        t1 = book.begin_decision(
            decision_id="d1", peer_id=7, message_id="m1",
            state_t=S1, action_t="FANOUT_DOWN",
        )
        book.attach_reward("d1", -0.5)

        self.assertTrue(t1.reward_ready)
        self.assertFalse(t1.next_ready)
        self.assertFalse(t1.update_ready)

        book.begin_decision(
            decision_id="d2", peer_id=7, message_id="m2",
            state_t=S2, action_t="KEEP",
        )
        self.assertTrue(t1.update_ready)
        self.assertEqual(t1.next_state, S2)

    def test_4_overlapping_out_of_order_rewards(self):
        book = TransitionBookkeeper()
        t1 = book.begin_decision(
            decision_id="d1", peer_id=7, message_id="m1",
            state_t=S1, action_t="KEEP",
        )
        t2 = book.begin_decision(
            decision_id="d2", peer_id=7, message_id="m2",
            state_t=S2, action_t="FANOUT_UP",
        )
        t3 = book.begin_decision(
            decision_id="d3", peer_id=7, message_id="m3",
            state_t=S3, action_t="SET_STRUCTURED",
        )

        self.assertEqual(t1.next_state, S2)
        self.assertEqual(t2.next_state, S3)
        self.assertFalse(t3.next_ready)

        # Rewards deliberately close out of decision order.
        book.attach_reward("d2", -0.25)
        self.assertTrue(t2.update_ready)
        self.assertFalse(t1.update_ready)

        book.attach_reward("d1", 0.75)
        self.assertTrue(t1.update_ready)
        self.assertEqual(t1.reward_t, 0.75)
        self.assertEqual(t2.reward_t, -0.25)

        # d3 still has no successor despite its reward closing.
        book.attach_reward("d3", 0.10)
        self.assertFalse(t3.update_ready)

        # A fourth same-peer decision supplies exactly d3's successor.
        s4 = ("H", "H", "M", "L")
        book.begin_decision(
            decision_id="d4", peer_id=7, message_id="m4",
            state_t=s4, action_t="KEEP",
        )
        self.assertEqual(t3.next_state, s4)
        self.assertTrue(t3.update_ready)

    def test_5_terminal_and_zero_forwarding_evidence(self):
        book = TransitionBookkeeper()

        terminal = book.begin_decision(
            decision_id="terminal", peer_id=7, message_id="m-last",
            state_t=S1, action_t="KEEP",
        )
        book.attach_reward("terminal", 1.0)
        book.mark_terminal("terminal")

        self.assertTrue(terminal.update_ready)
        self.assertIsNone(terminal.bootstrap_state)

        no_forward = book.begin_decision(
            decision_id="f0", peer_id=8, message_id="m-f0",
            state_t=S2, action_t="KEEP",
        )
        book.close_no_forwarding_evidence("f0")
        book.mark_terminal("f0")

        self.assertFalse(no_forward.reward_ready)
        self.assertIsNone(no_forward.reward_t)
        self.assertFalse(no_forward.update_ready)
        self.assertIsNone(no_forward.bootstrap_state)


if __name__ == "__main__":
    unittest.main()
