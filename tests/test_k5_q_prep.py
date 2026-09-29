import unittest
from gke.app.k5_q_formal_contract import (
    METHODS,SEEDS,NUM_NODES,BA_M,SOURCE,MESSAGE_COUNT,MESSAGE_INTERVAL_S,
    CHURN_OFFSETS_S,coordinates,frozen_summary,validate_coordinate,
)

class TestK5QPrep(unittest.TestCase):
    def test_exact_matrix(self):
        self.assertEqual(METHODS,("gossip","structured","dcsoc","ahbn","qahbn2"))
        self.assertEqual(SEEDS,(42,43,44,45,46))
        self.assertEqual(len(coordinates()),25)
        self.assertEqual(len(set(coordinates())),25)

    def test_exact_environment(self):
        self.assertEqual((NUM_NODES,BA_M,SOURCE),(20,2,0))
        self.assertEqual(MESSAGE_COUNT,240)
        self.assertEqual(MESSAGE_INTERVAL_S,0.4)
        self.assertEqual(CHURN_OFFSETS_S,(1.0,26.0,51.0,76.0))

    def test_shared_evidence_roles(self):
        s=frozen_summary()
        self.assertEqual(s['unique_runs'],25)
        self.assertEqual(s['evidence_roles']['k8s_val_q'],['ahbn','qahbn2'])

    def test_rejects_unfrozen_coordinate(self):
        with self.assertRaises(ValueError): validate_coordinate(47,'ahbn')
        with self.assertRaises(ValueError): validate_coordinate(42,'legacy_qahbn')

if __name__=='__main__':
    unittest.main()
