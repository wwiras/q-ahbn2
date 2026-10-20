"""Regression tests for D8-B recovery attribution and timing calculations."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "gke/scripts"))
import audit_d8_b_offline as audit


class D8BRecoveryTests(unittest.TestCase):
    def make_topology(self):
        return {"num_nodes": 2, "settle_time": 18.0}

    def test_recovery_search_can_find_full_delivery_after_censor_value(self):
        rows = [
            {"event": "churn_leave_scheduled", "event_index": 1, "target_peer": 1, "ts": 0.5},
            {"event": "pod_unavailability_observed", "event_index": 1, "target_peer": 1, "ts": 0.6},
            {"event": "churn_rejoined", "event_index": 1, "target_peer": 1, "ts": 1.0},
            {"event": "message_injected", "message_id": "m1", "ts": 28.0},
            {"event": "received_new", "message_id": "m1", "peer_id": 0, "ts": 28.1},
            {"event": "received_new", "message_id": "m1", "peer_id": 1, "ts": 29.0},
        ]
        for index in range(2, 5):
            rows.extend(
                [
                    {"event": "churn_leave_scheduled", "event_index": index,
                     "target_peer": 0, "ts": 40.0 + index},
                    {"event": "pod_unavailability_observed", "event_index": index,
                     "target_peer": 0, "ts": 40.1 + index},
                    {"event": "churn_rejoined", "event_index": index,
                     "target_peer": 0, "ts": 40.2 + index},
                ]
            )
        result = audit.recovery_observations(rows, self.make_topology(), expected_count=1)[0]
        self.assertTrue(result["recovered"])
        self.assertAlmostEqual(result["recovery_time_s"], 28.0)
        self.assertFalse(result["search_is_bounded_by_censor_value"])

    def test_one_message_can_anchor_multiple_rejoin_events(self):
        rows = [
            {"event": "churn_leave_scheduled", "event_index": 1, "target_peer": 0, "ts": 1.1},
            {"event": "churn_leave_scheduled", "event_index": 2, "target_peer": 1, "ts": 2.1},
            {"event": "pod_unavailability_observed", "event_index": 1, "target_peer": 0, "ts": 1.2},
            {"event": "pod_unavailability_observed", "event_index": 2, "target_peer": 1, "ts": 2.2},
            {"event": "churn_rejoined", "event_index": 1, "target_peer": 0, "ts": 1.5},
            {"event": "churn_rejoined", "event_index": 2, "target_peer": 1, "ts": 2.5},
            {"event": "churn_leave_scheduled", "event_index": 3, "target_peer": 0, "ts": 4.1},
            {"event": "churn_leave_scheduled", "event_index": 4, "target_peer": 1, "ts": 5.1},
            {"event": "pod_unavailability_observed", "event_index": 3, "target_peer": 0, "ts": 4.2},
            {"event": "pod_unavailability_observed", "event_index": 4, "target_peer": 1, "ts": 5.2},
            {"event": "churn_rejoined", "event_index": 3, "target_peer": 0, "ts": 4.5},
            {"event": "churn_rejoined", "event_index": 4, "target_peer": 1, "ts": 5.5},
            {"event": "message_injected", "message_id": "m1", "ts": 3.0},
            {"event": "received_new", "message_id": "m1", "peer_id": 0, "ts": 3.1},
            {"event": "received_new", "message_id": "m1", "peer_id": 1, "ts": 3.2},
        ]
        result = audit.recovery_observations(rows, self.make_topology(), expected_count=1)
        self.assertEqual(
            [item["recovery_message_id"] for item in result[:2]], ["m1", "m1"]
        )
        self.assertTrue(
            all(item["anchor_reused_within_run"] for item in result[:2])
        )

    def test_exact_concatenated_record_deduplication(self):
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.jsonl"
            path.write_text('{"event":"x","ts":1}{"ts":1,"event":"x"}\n{"event":"x","ts":2}\n')
            rows, duplicates = audit.read_records(path)
        self.assertEqual((len(rows), duplicates), (2, 1))


if __name__ == "__main__":
    unittest.main()
