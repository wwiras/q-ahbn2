import csv, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from scripts.run_s11b_exp13q_formal import run_formal

class TestS11BFormalRelease(unittest.TestCase):
 def test_formal_release_artifacts_and_boundaries(self):
    with tempfile.TemporaryDirectory() as td:
      root=Path(td); src=root/"exp13q.csv"
      fields=["churn_level","method","seed","delivery_ratio","propagation_delay","duplicates","total_forwards"]
      methods=("gossip","structured","dcsoc","ahbn","qahbn2")
      with src.open("w",newline="",encoding="utf-8") as f:
       w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
       for mi,m in enumerate(methods):
        for si,s in enumerate((42,43,44,45,46)):
         w.writerow({"churn_level":.4,"method":m,"seed":s,"delivery_ratio":.7+.01*mi+.001*si,
          "propagation_delay":2+mi+.1*si,"duplicates":1000+mi*100+si,"total_forwards":2000+mi*100+si})
      with patch("scripts.run_s11b_exp13q_formal.datetime") as dt:
       dt.now.return_value.strftime.return_value="29092026130000"
       out=run_formal(src,root/"evidence")
      self.assertTrue((out/"RUN.md").is_file())
      self.assertTrue((out/"manifest.json").is_file())
      self.assertTrue((out/"s11b_exp13q_aggregation.json").is_file())
      self.assertTrue((out/"s11b_exp13q_summary.csv").is_file())
      data=json.loads((out/"s11b_exp13q_aggregation.json").read_text())
      man=json.loads((out/"manifest.json").read_text())
      self.assertEqual(data["total_runs"],25)
      self.assertEqual(set(data["methods"]),set(methods))
      self.assertFalse(data["p_values_calculated"])
      self.assertFalse(data["omnibus_score_calculated"])
      self.assertEqual(man["scope"],"Exp13-Q external benchmark only")
      self.assertEqual(set(man["artifacts"]),{"s11b_exp13q_aggregation.json","s11b_exp13q_summary.csv"})
      with (out/"s11b_exp13q_summary.csv").open() as f:
       rows=list(csv.DictReader(f))
      self.assertEqual(len(rows),20) # 5 methods x 4 metrics

if __name__=="__main__": unittest.main()
