import unittest
from gke.app.k5_q_formal_contract import (
    METHODS,SEEDS,NUM_NODES,BA_M,SOURCE_POLICY,MESSAGE_COUNT,MESSAGE_INTERVAL_S,
    CHURN_OFFSETS_S,coordinates,frozen_summary,validate_coordinate,
)

class TestK5QPrep(unittest.TestCase):
    def test_exact_matrix(self):
        self.assertEqual(METHODS,("gossip","structured","dcsoc","ahbn","qahbn2"))
        self.assertEqual(SEEDS,(42,43,44,45,46))
        self.assertEqual(len(coordinates()),25)
        self.assertEqual(len(set(coordinates())),25)

    def test_exact_environment(self):
        self.assertEqual((NUM_NODES,BA_M),(20,2))
        self.assertEqual(SOURCE_POLICY,'inherited_k7_common_non_structural_per_seed')
        self.assertEqual(MESSAGE_COUNT,240)
        self.assertEqual(MESSAGE_INTERVAL_S,0.4)
        self.assertEqual(CHURN_OFFSETS_S,(1.0,26.0,51.0,76.0))

    def test_shared_evidence_roles(self):
        s=frozen_summary()
        self.assertEqual(s['unique_runs'],25)
        self.assertEqual(s['evidence_roles']['k8s_val_q'],['ahbn','qahbn2'])

    def test_formal_runner_locked(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        runner=(root/'gke/scripts/run_k5_q_formal.sh').read_text()
        self.assertIn('METHODS=(gossip structured dcsoc ahbn qahbn2)',runner)
        self.assertIn('SEEDS=(42 43 44 45 46)',runner)
        self.assertIn('validate_k5_q_artifacts.py',runner)
        docker=(root/'gke/app/Dockerfile.qahbn2').read_text()
        self.assertIn('k7_exp11_tools.py',docker)
        self.assertIn('k7_controller.py controller.py',docker)
        self.assertTrue((root/'gke/helm/ahbn/templates/job-controller.yaml').exists())

    def test_preflight_controller_import_is_real_line(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        preflight=(root/'gke/scripts/preflight_k3_q_image.sh').read_text()
        self.assertIn('import qahbn2_runtime\nimport controller', preflight)
        self.assertNotIn(r'import qahbn2_runtime\nimport controller', preflight)

    def test_formal_helper_uses_repo_helm_path(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        helper=(root/'gke/scripts/run_k7_experiment.sh').read_text()
        self.assertGreaterEqual(helper.count('${ROOT_DIR}/gke/helm/ahbn'), 2)
        self.assertNotIn('${ROOT_DIR}/helm/ahbn', helper)

    def test_generated_helm_topology_is_ignored_and_clean_check_is_pre_evidence(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        ignore=(root/'.gitignore').read_text()
        runner=(root/'gke/scripts/run_k5_q_formal.sh').read_text()
        self.assertIn('gke/helm/ahbn/topology.json', ignore)
        self.assertLess(runner.index('PRE_STATUS="$(git status --porcelain)"'),
                        runner.index('mkdir -p "${RESULT_ROOT}"'))

    def test_validator_adaptive_trace_scope(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        validator=(root/'gke/app/k7_exp11_tools.py').read_text()
        self.assertIn('adaptive = algorithm in {"ahbn","qahbn2"}', validator)
        self.assertIn('if adaptive != bool(traces and decisions)', validator)
        self.assertIn('if adaptive:', validator)

    def test_rejects_unfrozen_coordinate(self):
        with self.assertRaises(ValueError): validate_coordinate(47,'ahbn')
        with self.assertRaises(ValueError): validate_coordinate(42,'legacy_qahbn')

if __name__=='__main__':
    unittest.main()
