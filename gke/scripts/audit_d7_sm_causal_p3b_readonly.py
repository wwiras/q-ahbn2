#!/usr/bin/env python3
"""P3B: read-only source decision and DC-SoC maintenance attribution audit."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

def read_objects(path):
    decoder = json.JSONDecoder()
    content = path.read_text(encoding="utf-8")
    offset = 0
    while offset < len(content):
        while offset < len(content) and content[offset].isspace():
            offset += 1
        if offset == len(content):
            break
        obj, offset = decoder.raw_decode(content, offset)
        if not isinstance(obj, dict):
            raise ValueError("Expected JSON event object")
        yield obj

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--output-dir", required=True, type=Path)
    args = ap.parse_args()
    root, out = args.root.resolve(), args.output_dir.resolve()
    if not (root / "runs" / "dcsoc" / "peer_stream.jsonl").is_file():
        ap.error("Expected immutable run root with runs/dcsoc/peer_stream.jsonl")
    if root == out or root in out.parents or out in root.parents:
        ap.error("Output and original evidence roots must be independent")
    if out.exists():
        ap.error("Refusing overwrite of existing output directory")

    dpath = root / "runs" / "dcsoc" / "peer_stream.jsonl"
    apath = root / "runs" / "ahbn" / "peer_stream.jsonl"
    d_events = list(read_objects(dpath))
    a_events = list(read_objects(apath))
    maint = sorted([e for e in d_events if e.get("event") == "dcsoc_maintenance"],
                   key=lambda e: (float(e.get("ts", e.get("maintenance_end", 0))), int(e.get("peer_id", -1))))
    source_maint = [e for e in maint if e.get("peer_id") == 1]
    source_failed = sorted([e for e in d_events if e.get("peer_id") == 1 and e.get("event") in
                           ("forward_failed", "forward_rejected")],
                           key=lambda e: float(e.get("ts", 0)))
    source_forward = sorted([e for e in d_events if e.get("peer_id") == 1 and e.get("event") == "forward"],
                            key=lambda e: float(e.get("ts", 0)))
    source_decisions = sorted([e for e in a_events if e.get("event") == "ahbn_forwarding_decision"
                               and e.get("sender") == 1],
                              key=lambda e: float(e.get("ts", 0)))
    all_ahbn = [e for e in a_events if e.get("event") == "ahbn_forwarding_decision"]
    by_mid = collections.defaultdict(list)
    for e in source_decisions:
        by_mid[str(e.get("message_id"))].append(e)
    decision_rows = []
    for n in range(1, 241):
        mid = "m" + str(n)
        ee = by_mid.get(mid, [])
        decision_rows.append({
            "message_id": mid,
            "decision_count": len(ee),
            "decisions": [{
                "ts": e.get("ts"), "sender": e.get("sender"),
                "incoming_sender": e.get("incoming_sender"),
                "mode": e.get("mode"), "controller_fanout": e.get("controller_fanout"),
                "fanout_requested": e.get("fanout_requested"),
                "eligible_neighbors": e.get("eligible_neighbors"),
                "selected_peers": e.get("selected_peers"),
                "unavailable_neighbors": e.get("unavailable_neighbors"),
            } for e in ee]
        })

    source_maint_rows = []
    for e in source_maint:
        source_maint_rows.append({
            "ts": e.get("ts"), "maintenance_start": e.get("maintenance_start"),
            "maintenance_end": e.get("maintenance_end"),
            "maintenance_action": e.get("maintenance_action"),
            "maintenance_reason": e.get("maintenance_reason"),
            "failed_node": e.get("failed_node"),
            "rejoined_node": e.get("rejoined_node"),
            "former_parent": e.get("former_parent"),
            "replacement_core": e.get("replacement_core"),
            "new_cluster": e.get("new_cluster"),
            "structural_generation": e.get("structural_generation"),
            "core_replacement_count": e.get("core_replacement_count"),
            "recluster_count": e.get("recluster_count"),
            "rejoin_assignment_count": e.get("rejoin_assignment_count"),
            "raw_event": e
        })
    report = {
        "gate": "JCC-R1A-C3-D7-SM-POSTRUN-CAUSAL-P3B",
        "classification": "NONFORMAL / LOCAL READ ONLY",
        "decision": "EVIDENCE DIAGNOSTIC ONLY / RECOVERY CONFORMANCE HOLD / D7-F 0/25 AND D8 HOLD",
        "original_input_sha256": {"dcsoc_peer_stream": digest(dpath), "ahbn_peer_stream": digest(apath)},
        "dcsoc": {
            "maintenance_total": len(maint),
            "maintenance_by_action": dict(collections.Counter(e.get("maintenance_action", "UNKNOWN") for e in maint)),
            "source_maintenance_count": len(source_maint),
            "source_maintenance_events": source_maint_rows,
            "all_maintenance_events": maint,
            "source_failures": source_failed,
            "source_successes": source_forward,
            "limitations": [
                "A maintenance event describes the state of its receiving peer; it does not prove all other peers converged.",
                "An updated parent does not itself prove the old parent was removed from unavailable_neighbors.",
                "A failure-to-success comparison needs target identity, timestamps and actual source sends."
            ]
        },
        "ahbn": {
            "all_decisions": len(all_ahbn),
            "source_decisions": len(source_decisions),
            "source_messages_with_decision": sum(bool(r["decisions"]) for r in decision_rows),
            "source_zero_eligible_decisions": sum(e.get("eligible_neighbors")==[] for e in source_decisions),
            "source_zero_selected_decisions": sum(e.get("selected_peers")==[] for e in source_decisions),
            "source_decision_modes": dict(collections.Counter(e.get("mode","UNKNOWN") for e in source_decisions)),
            "source_by_message": decision_rows,
            "limitations": [
                "AHBN decision records identify the origin peer using sender, not peer_id.",
                "The sender field here is the deciding peer; incoming_sender is a distinct value.",
                "A successful forward and a controller decision require separate timing/outcome reconciliation."
            ]
        }
    }
    out.mkdir(parents=True, exist_ok=False)
    p = out / "p3b_recovery_attribution.json"
    p.write_text(json.dumps(report, indent=2, sort_keys=True, default=str)+"\n", encoding="utf-8")
    manifest = out / "SHA256SUMS"
    manifest.write_text(digest(p)+"  "+p.name+"\n", encoding="utf-8")
    print(json.dumps({
        "report": str(p), "sha256": digest(p),
        "dcsoc_maintenance": len(maint), "dcsoc_source_maintenance": len(source_maint),
        "dcsoc_maintenance_actions": report["dcsoc"]["maintenance_by_action"],
        "ahbn_all_decisions": len(all_ahbn), "ahbn_source_decisions": len(source_decisions),
        "ahbn_source_messages_with_decision": report["ahbn"]["source_messages_with_decision"],
        "ahbn_source_zero_eligible": report["ahbn"]["source_zero_eligible_decisions"],
        "status": report["decision"]}, indent=2))

if __name__ == "__main__":
    main()
