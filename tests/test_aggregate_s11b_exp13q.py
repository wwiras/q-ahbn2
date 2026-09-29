import copy, math, unittest
from scripts.aggregate_s11b_exp13q import (
 FROZEN_SEEDS,METHODS,PRIMARY_METRICS,STUDENT_T_95_DF4,
 aggregate_rows,metric_summary,paired_contrast,validate_rows
)

def rows():
    out=[]
    for mi,m in enumerate(METHODS):
        for si,s in enumerate(FROZEN_SEEDS):
            out.append({"churn_level":"0.4","method":m,"seed":str(s),
             "delivery_ratio":str(.70+.01*mi+.001*si),
             "propagation_delay":str(2+mi+.1*si),
             "duplicates":str(1000+100*mi+si),
             "total_forwards":str(2000+100*mi+si)})
    return out

class TestS11BPrep(unittest.TestCase):
 def test_exact_matrix(self):
    validate_rows(rows()); self.assertEqual(len(rows()),25)
 def test_missing_and_duplicate_rejected(self):
    with self.assertRaises(ValueError): validate_rows(rows()[:-1])
    x=rows(); x[-1]=copy.deepcopy(x[0])
    with self.assertRaises(ValueError): validate_rows(x)
 def test_method_set_enforced(self):
    x=rows(); x[0]["method"]="other"
    with self.assertRaises(ValueError): validate_rows(x)
 def test_churn_frozen(self):
    x=rows(); x[0]["churn_level"]="0.2"
    with self.assertRaises(ValueError): validate_rows(x)
 def test_metric_domains(self):
    x=rows(); x[0]["delivery_ratio"]="1.1"
    with self.assertRaises(ValueError): validate_rows(x)
 def test_seed_order_retained(self):
    a=aggregate_rows(list(reversed(rows())))
    self.assertEqual(list(a["method_summaries"]["ahbn"]["delivery_ratio"]["seed_values"]),[str(s) for s in FROZEN_SEEDS])
 def test_sample_sd(self):
    v={42:10,43:20,44:30,45:40,46:50}; a=metric_summary(v)
    self.assertTrue(math.isclose(a["sd"],math.sqrt(250),rel_tol=1e-12))
 def test_student_t_ci(self):
    self.assertEqual(STUDENT_T_95_DF4,2.7764451051977987)
    v={42:10,43:20,44:30,45:40,46:50}; a=metric_summary(v)
    margin=STUDENT_T_95_DF4*math.sqrt(250)/math.sqrt(5)
    self.assertTrue(math.isclose(a["ci95_low"],30-margin,rel_tol=1e-12))
 def test_same_seed_q_minus_reference(self):
    q={s:float(s) for s in FROZEN_SEEDS}; r={s:float(s-1) for s in FROZEN_SEEDS}
    a=paired_contrast(q,r,"ahbn")
    self.assertEqual(a["mean"],1.0); self.assertEqual(a["sd"],0.0)
 def test_four_predeclared_contrasts_only(self):
    a=aggregate_rows(rows())
    self.assertEqual(set(a["qahbn2_paired_contrasts"]),{"ahbn","gossip","structured","dcsoc"})
    self.assertFalse(a["p_values_calculated"]); self.assertFalse(a["omnibus_score_calculated"])
 def test_s11a_separation(self):
    a=aggregate_rows(rows())
    self.assertNotIn("exp10q",str(a).lower()); self.assertNotIn("exp11q",str(a).lower()); self.assertNotIn("exp12q",str(a).lower())
 def test_prep_execution_disabled(self):
    # Formal release is not exposed by this module; only pure aggregation functions exist.
    import scripts.aggregate_s11b_exp13q as m
    self.assertFalse(hasattr(m,"run_s11b_pipeline"))

if __name__=="__main__": unittest.main()
