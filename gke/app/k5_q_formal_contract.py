from __future__ import annotations

METHODS=("gossip","structured","dcsoc","ahbn","qahbn2")
SEEDS=(42,43,44,45,46)
NUM_NODES=20
BA_M=2
SOURCE_POLICY="inherited_k7_common_non_structural_per_seed"
MESSAGE_COUNT=240
MESSAGE_INTERVAL_S=0.4
CHURN_OFFSETS_S=(1.0,26.0,51.0,76.0)

def coordinates():
    return [(seed,method) for seed in SEEDS for method in METHODS]

def validate_coordinate(seed:int, method:str)->None:
    if seed not in SEEDS:
        raise ValueError(f"seed not frozen: {seed}")
    if method not in METHODS:
        raise ValueError(f"method not frozen: {method}")

def frozen_summary()->dict:
    return {
        "methods":list(METHODS),
        "seeds":list(SEEDS),
        "unique_runs":len(METHODS)*len(SEEDS),
        "num_nodes":NUM_NODES,
        "ba_m":BA_M,
        "source_policy":SOURCE_POLICY,
        "message_count":MESSAGE_COUNT,
        "message_interval_s":MESSAGE_INTERVAL_S,
        "churn_offsets_s":list(CHURN_OFFSETS_S),
        "evidence_roles":{
            "k8s_val_q":["ahbn","qahbn2"],
            "exp13_q_k8s":list(METHODS),
        },
    }
