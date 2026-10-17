#!/usr/bin/env python3
"""P3 NONFORMAL causal evidence reconstruction. No GKE or original evidence writes."""
import argparse
import collections
import hashlib
import json
from pathlib import Path


def read_objects(path):
    text = path.read_text(encoding="utf-8")
    decoder = json.JSONDecoder()
    index = 0
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text):
            break
        obj, index = decoder.raw_decode(text, index)
        if not isinstance(obj, dict):
            raise ValueError("unexpected non-object peer event")
        yield obj


def message_sort(item):
    if item.startswith("m") and item[1:].isdigit():
        return (0, int(item[1:]))
    return (1, item)


def audit(root):
    summary = {"gate": "JCC-R1A-C3-D7-SM-POSTRUN-CAUSAL-P3",
               "classification": "NONFORMAL / READ-ONLY",
               "evidence_root": str(root),
               "methods": {},
               "decision": "DIAGNOSTIC ONLY / DESIGN VS IMPLEMENTATION UNRESOLVED / D7-F AND D8 HOLD"}
    for method in ("structured", "dcsoc", "ahbn", "qahbn2"):
        folder = root / "runs" / method
        events_path = folder / "peer_stream.jsonl"
        rows = list(read_objects(events_path))
        opportunities = json.loads((folder / "churn_events.json").read_text())["delivery_opportunities"]
        by_message = collections.defaultdict(list)
        unscoped = collections.Counter()
        for event in rows:
            key = event.get("message_id")
            if key is None:
                unscoped[event.get("event", "UNKNOWN")] += 1
            else:
                by_message[str(key)].append(event)
        results = []
        for index in range(1, 241):
            mid = "m" + str(index)
            evs = by_message.get(mid, [])
            source = [e for e in evs if e.get("peer_id") == 1]
            def compact(event):
                return {k: event[k] for k in (
                    "ts", "event", "peer_id", "src_peer", "dst_peer", "mode",
                    "mode_ahbn", "mode_q", "action", "fanout", "canonical_fanout",
                    "requested_fanout", "actual_fanout", "eligible_neighbors",
                    "eligible_targets", "selected_peers", "realized_targets",
                    "unavailable_neighbors", "error", "outcome", "decision_id",
                    "reward", "parent_before", "parent_after") if k in event}
            candidate_events = {"message_injected", "received_new", "received_duplicate",
                "ahbn_forwarding_decision", "qahbn2_decision", "k7_forward_attempt",
                "forward", "forward_failed", "forward_rejected",
                "forward_duplicate_ack", "qahbn2_attempt_outcome"}
            chain = [compact(e) for e in evs if e.get("event") in candidate_events]
            decisions = [compact(e) for e in source if e.get("event") in
                         ("ahbn_forwarding_decision", "qahbn2_decision")]
            attempts = [e for e in evs if e.get("event") == "k7_forward_attempt"]
            terminal = [e for e in evs if e.get("event") in
                        ("forward", "forward_failed", "forward_rejected",
                         "forward_duplicate_ack", "qahbn2_attempt_outcome")]
            results.append({
                "message_id": mid,
                "delivered_count": opportunities[index - 1]["delivered_count"],
                "source_decisions": decisions,
                "attempts_count": len(attempts),
                "recorded_terminal_events_count": len(terminal),
                "first_pass_trace": chain,
            })
        maintenance = [compact(e) for e in rows if e.get("event") == "dcsoc_maintenance"]
        summary["methods"][method] = {
            "events_sha256": hashlib.sha256(events_path.read_bytes()).hexdigest(),
            "peer_records": len(rows),
            "delivery_opportunities": len(opportunities),
            "source_only": sum(m["delivered_count"] == 1 for m in results),
            "unscoped_event_counts": dict(unscoped),
            "maintenance": maintenance,
            "messages": results,
            "limitations": [
                "Event counts, attempts, ACKs and outcomes may have different cardinalities.",
                "No inferred retries or failed packets where there is no logged event.",
                "Code design conformity and deployed-image provenance require separate contract review.",
                "Missing target/availability fields remain UNKNOWN, never silently empty.",
            ],
        }
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    dest = args.output_dir.resolve()
    if dest == root or root in dest.parents:
        parser.error("output directory must be outside the immutable original evidence root")
    if dest.exists() and any(dest.iterdir()):
        parser.error("output directory must be absent or empty")
    report = audit(root)
    dest.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    out = dest / "p3_message_trace.json"
    out.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    (dest / "SHA256SUMS").write_text(f"{digest}  p3_message_trace.json\n", encoding="utf-8")
    print(json.dumps({"output": str(out), "sha256": digest, "methods":
        {k: {"messages": len(v["messages"]), "source_only": v["source_only"]}
         for k, v in report["methods"].items()},
        "status": report["decision"]}, indent=2))


if __name__ == "__main__":
    main()
