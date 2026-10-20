"""Regression tests for independent metric reconstruction, including censoring."""
import importlib.util
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'gke/scripts'))
import audit_d8_a_offline as audit

class ReconstructionTests(unittest.TestCase):
    def test_active_denominator_delay_and_counts(self):
        rows = [dict(event='pod_unavailability_observed',ts=1,target_peer=1),
                dict(event='churn_rejoined',ts=3,target_peer=1,event_index=1),
                dict(event='message_injected',ts=2,message_id='m1'),
                dict(event='received_new',ts=2,peer_id=0,message_id='m1'),
                dict(event='received_new',ts=2.5,peer_id=1,message_id='m1'),
                dict(event='received_duplicate',ts=2.6),dict(event='forward',ts=2.7),
                dict(event='k7_forward_attempt',ts=2.4),dict(event='k7_forward_attempt',ts=2.6)]
        result, opp, _ = audit.reconstruct(rows,dict(num_nodes=2,settle_time=18))
        self.assertEqual(result['delivery_ratio'],1)
        self.assertEqual(opp[0]['expected_count'],1)
        self.assertEqual(result['propagation_delay'],0.5)
        self.assertEqual((result['duplicates'],result['F_success'],result['F_attempt']),(1,1,2))
        self.assertEqual(result['recovery_events'][0]['censored_at_s'],18)

    def test_recovery_search_is_not_bounded_by_18_seconds(self):
        rows=[dict(event='churn_rejoined',ts=1,target_peer=1,event_index=1),
              dict(event='message_injected',ts=28,message_id='m1'),
              dict(event='received_new',ts=28,peer_id=0,message_id='m1'),
              dict(event='received_new',ts=29,peer_id=1,message_id='m1')]
        result, _, _=audit.reconstruct(rows,dict(num_nodes=2,settle_time=18))
        self.assertEqual(result['recovery_events'][0]['recovery_time_s'],28)
        self.assertFalse(result['recovery_events'][0]['censored'])

    def test_exact_record_dedup_preserves_distinct_events(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'rows'
            p.write_text('{"event":"forward","ts":1}\n{"ts":1,"event":"forward"}\n{"event":"forward","ts":2}\n')
            rows,duplicates,_=audit.records(p)
            self.assertEqual((len(rows),duplicates),(2,1))
            p.write_text('{bad}\n')
            with self.assertRaises(ValueError): audit.records(p)

if __name__=='__main__': unittest.main()
