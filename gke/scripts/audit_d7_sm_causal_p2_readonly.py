#!/usr/bin/env python3
"""P2 readonly causal trace from intact D7-SM evidence; no GKE calls."""
import argparse, json, collections, pathlib
def read_objects(text):
    decoder=json.JSONDecoder(); i=0; out=[]
    while i<len(text):
        while i<len(text) and text[i].isspace(): i+=1
        if i>=len(text):break
        obj,n=decoder.raw_decode(text,i); out.append(obj); i=n
    return out
def main():
    p=argparse.ArgumentParser();p.add_argument("root",type=pathlib.Path); a=p.parse_args()
    root=a.root
    methods=("structured","dcsoc","ahbn","qahbn2"); output=[]
    for method in methods:
        d=root/"runs"/method
        rows=read_objects((d/"peer_stream.jsonl").read_text())
        src=[e for e in rows if e.get("peer_id")==1 or e.get("sender")==1]
        c=collections.Counter(e.get("event") for e in rows)
        sc=collections.Counter(e.get("event") for e in src)
        opportunities=json.loads((d/"churn_events.json").read_text())["delivery_opportunities"]
        decisions=[e for e in rows if e.get("event")=="qahbn2_decision"]
        src_decisions=[e for e in decisions if e.get("peer_id")==1]
        decision_modes=collections.Counter(e.get("mode_q") for e in src_decisions)
        decision_actions=collections.Counter(e.get("action") for e in src_decisions)
        selected=collections.Counter(len(e.get("realized_targets",[])) for e in src_decisions)
        empty_by_mode=collections.Counter(e.get("mode_q") for e in src_decisions if not e.get("realized_targets"))
        ahbn_decisions=[e for e in rows if e.get("event")=="ahbn_forwarding_decision" and e.get("peer_id")==1]
        ahbn_empty=collections.Counter(e.get("mode") for e in ahbn_decisions if not e.get("selected_peers"))
        failures=[{"message_id":e.get("message_id"),"dst_peer":e.get("dst_peer"),"error_code":("UNAVAILABLE" if "UNAVAILABLE" in str(e.get("error")) else "DEADLINE_EXCEEDED" if "DEADLINE_EXCEEDED" in str(e.get("error")) else "OTHER")} for e in src if e.get("event")=="forward_failed"]
        row={"method":method,"peer_stream_records":len(rows),"event_counts":dict(c),"source_event_counts":dict(sc),"source_forward_failures":failures,"source_only_messages":sum(x["delivered_count"]==1 for x in opportunities),"first_20_deliveries":[x["delivered_count"] for x in opportunities[:20]]}
        if src_decisions:row["q_source"]={"decisions":len(src_decisions),"actions":dict(decision_actions),"modes":dict(decision_modes),"realized_target_counts":dict(selected),"empty_by_mode":dict(empty_by_mode)}
        if ahbn_decisions:row["ahbn_source"]={"decisions":len(ahbn_decisions),"empty_target_by_mode":dict(ahbn_empty),"first_10":[{"message_id":x.get("message_id"),"mode":x.get("mode"),"selected_peers":x.get("selected_peers")} for x in ahbn_decisions[:10]]}
        output.append(row)
    print(json.dumps({"gate":"JCC-R1A-C3-D7-SM-POSTRUN-CAUSAL-P2","classification":"NONFORMAL, READ-ONLY","runs":output,"decision":"DIAGNOSTIC ONLY; D7-F AND D8 HOLD"},indent=2))
if __name__=="__main__":main()
