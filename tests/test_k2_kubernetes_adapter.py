import unittest

from qahbn2.kubernetes_adapter import KubernetesQAHBN2Adapter, AttemptLedger
from qahbn2.learning import QAHBN2Learner
from qahbn2.kubernetes_integration import realize_inherited_targets, register_realized_targets


class TestKubernetesQAHBN2Adapter(unittest.TestCase):
    def test_state_uses_frozen_discretization_and_s5_proposal(self):
        learner=QAHBN2Learner(seed=42, epsilon=0.0, epsilon_min=0.0)
        # Force KEEP as unique greedy action.
        state=("L","M","H","L")
        learner.q_table[state]["KEEP"]=1.0
        a=KubernetesQAHBN2Adapter(learner)
        q=a.decide(peer_id=3,message_id="m1",d_hat=.1,l_hat=.5,u_hat=.9,c_hat=.2,
                   mode_ahbn="gossip",k_ahbn=5)
        self.assertEqual(q.state,state)
        self.assertEqual((q.mode_ahbn,q.k_ahbn),("gossip",5))
        self.assertEqual((q.mode_q,q.k_q),("gossip",5))

    def test_all_actions_exact_and_bounded(self):
        for action,expected in {
            "KEEP":("gossip",3),
            "FANOUT_DOWN":("gossip",2),
            "FANOUT_UP":("gossip",4),
            "SET_GOSSIP":("gossip",3),
            "SET_STRUCTURED":("structured",3),
        }.items():
            learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
            s=("L","L","L","L")
            for x in learner.q_table[s]: learner.q_table[s][x]=0.0
            learner.q_table[s][action]=1.0
            q=KubernetesQAHBN2Adapter(learner).decide(
                peer_id=1,message_id=action,d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                mode_ahbn="gossip",k_ahbn=3)
            self.assertEqual((q.mode_q,q.k_q),expected)
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        s=("L","L","L","L"); learner.q_table[s]["FANOUT_DOWN"]=1.0
        q=KubernetesQAHBN2Adapter(learner).decide(
            peer_id=1,message_id="low",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
            mode_ahbn="gossip",k_ahbn=2)
        self.assertEqual(q.k_q,2)
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        learner.q_table[s]["FANOUT_UP"]=1.0
        q=KubernetesQAHBN2Adapter(learner).decide(
            peer_id=1,message_id="high",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
            mode_ahbn="gossip",k_ahbn=6)
        self.assertEqual(q.k_q,6)

    def test_ack_semantics_new_duplicate_failed_and_reward(self):
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        s=("L","L","L","L"); learner.q_table[s]["KEEP"]=1
        a=KubernetesQAHBN2Adapter(learner)
        q=a.decide(peer_id=1,message_id="m",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                   mode_ahbn="gossip",k_ahbn=3)
        a.register_targets(q.decision_id,[2,3,4])
        a.record_ack(q.decision_id,2,ack_ok=True)
        a.record_ack(q.decision_id,3,ack_ok=False)
        a.record_failure(q.decision_id,4)
        rec=learner.transitions.get(q.decision_id)
        self.assertTrue(rec.reward_ready)
        self.assertAlmostEqual(rec.reward_t,-1/3)

    def test_f0_no_update(self):
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        s=("L","L","L","L"); learner.q_table[s]["KEEP"]=1
        a=KubernetesQAHBN2Adapter(learner)
        q=a.decide(peer_id=1,message_id="m0",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                   mode_ahbn="gossip",k_ahbn=3)
        a.register_targets(q.decision_id,[])
        rec=learner.transitions.get(q.decision_id)
        self.assertTrue(rec.no_forwarding_evidence)
        self.assertEqual(learner.update_count,0)

    def test_same_peer_successor_and_delayed_reward(self):
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        low=("L","L","L","L"); high=("H","H","H","H")
        learner.q_table[low]["KEEP"]=1; learner.q_table[high]["KEEP"]=1
        a=KubernetesQAHBN2Adapter(learner)
        q1=a.decide(peer_id=7,message_id="m1",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                    mode_ahbn="gossip",k_ahbn=3)
        a.register_targets(q1.decision_id,[8])
        q2=a.decide(peer_id=7,message_id="m2",d_hat=1,l_hat=1,u_hat=1,c_hat=1,
                    mode_ahbn="gossip",k_ahbn=3)
        self.assertEqual(learner.transitions.get(q1.decision_id).next_state,high)
        a.record_ack(q1.decision_id,8,ack_ok=True)
        self.assertTrue(learner.transitions.get(q1.decision_id).update_consumed)

    def test_terminal_zero_bootstrap(self):
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        s=("L","L","L","L"); learner.q_table[s]["KEEP"]=1
        a=KubernetesQAHBN2Adapter(learner)
        q=a.decide(peer_id=1,message_id="t",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                   mode_ahbn="gossip",k_ahbn=3)
        a.register_targets(q.decision_id,[2])
        a.record_ack(q.decision_id,2,ack_ok=True)
        self.assertFalse(learner.transitions.get(q.decision_id).update_consumed)
        a.terminal(q.decision_id)
        self.assertTrue(learner.transitions.get(q.decision_id).update_consumed)

    def test_ledger_guards(self):
        l=AttemptLedger((2,3))
        l.record(2,"NEW")
        with self.assertRaises(ValueError): l.record(2,"FAILED")
        with self.assertRaises(ValueError): l.record(9,"NEW")
        with self.assertRaises(ValueError): AttemptLedger((2,)).record(2,"OTHER")

    def test_inherited_gossip_realization_and_registration(self):
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        s=("L","L","L","L"); learner.q_table[s]["KEEP"]=1
        a=KubernetesQAHBN2Adapter(learner)
        q=a.decide(peer_id=1,message_id="g",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                   mode_ahbn="gossip",k_ahbn=3)
        realized=realize_inherited_targets(
            q=q,sender_id=9,gossip_eligible=[2,3,4,5],
            structured_selector=lambda sender,budget: (),
            rng_sample=lambda population,k: population[:k],
        )
        self.assertEqual(realized.eligible_targets,(2,3,4,5))
        self.assertEqual(realized.realized_targets,(2,3,4))
        register_realized_targets(a,realized)
        self.assertEqual(a.ledger(q.decision_id).expected_targets,(2,3,4))

    def test_structured_delegates_to_inherited_selector(self):
        learner=QAHBN2Learner(seed=1,epsilon=0.0,epsilon_min=0.0)
        s=("L","L","L","L"); learner.q_table[s]["SET_STRUCTURED"]=1
        a=KubernetesQAHBN2Adapter(learner)
        q=a.decide(peer_id=1,message_id="s",d_hat=0,l_hat=0,u_hat=0,c_hat=0,
                   mode_ahbn="gossip",k_ahbn=4)
        calls=[]
        realized=realize_inherited_targets(
            q=q,sender_id=7,gossip_eligible=[2,3],
            structured_selector=lambda sender,budget: calls.append((sender,budget)) or (8,9),
            rng_sample=lambda population,k: (),
        )
        self.assertEqual(calls,[(7,4)])
        self.assertEqual(realized.realized_targets,(8,9))

if __name__=="__main__":
    unittest.main()
