# JCC-R1A-C3-D7-SM-POSTRUN-AUDIT-P1 — NONFORMAL post-run causal and integrity audit

**Date:** 2026-10-17. **Decision:** EVIDENCE TRACE / CAUSAL DIAGNOSIS PARTIAL PASS; **FULL CHECKSUM AUDIT PENDING; SCIENTIFIC RELEASE HOLD**. No further GKE runs authorized by this review. Formal D7-F 0/25 HOLD; D8 HOLD.

## Evidence authority and scope
- GitHub experiment source: [wwiras/q-ahbn2](https://github.com/wwiras/q-ahbn2), live experiment checkout `68aa0830873b9d8cb231d9a27bff1bbc19477128`.
- Canonical Drive corpus: [q-ahbn2/output/evidence/20261017T133327Z-D7-SM-remaining](https://drive.google.com/drive/folders/1ol3d0N5lOg1k_KFyvPI93qm5-7o2hM_s).
- Analysis performed against `gke/app/k7_exp11_tools.py` (delivery/recovery calculator), `gke/app/peer.py` (forwarding, unavailability cache), `gke/app/k7_controller.py` (absolute scheduler), generated per-method YAML, `churn_events.json`, `metrics.json`, and separately fetched per-method `peer_stream.jsonl`.
- Prior Q-AHBN GKE comparison: [NONFORMAL Gossip canary post-run](https://github.com/wwiras/q-ahbn2/blob/main/docs/stages/JCC_R1A_C3_D7_SM_CANARY_POSTRUN_20261017.md). Historical Gossip seed42 under comparable K7 protocol had delivery 0.851464, duplicates 2206 and 2/4 recovered churn events. The canary source checkout differed; this is *context*, not an extra formal matched run.
- Thesis authority [MUM_FIT_ThesisWira](https://github.com/wwiras/MUM_FIT_ThesisWira), [thesis corpus](https://drive.google.com/drive/folders/1MbsZ9nnndGBKo0ciAx54bFOD9sx_RgDR), [RO4 manuscript repo](https://github.com/wwiras/QAHBN2-Manuscript), [RO4 manuscript corpus](https://drive.google.com/drive/folders/1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj). Manuscript *Q-AHBN as a Bounded Q-Learning Refinement for Adaptive Blockchain Dissemination under Dynamic Network Conditions* is submitted to **Journal of Cloud Computing, under peer review, not published, without DOI**. No manuscript performance claims revised.

## 1. Exact metric reconstruction (confirmed)
`validate_run()` uses `received_new` events from deduplicated combined `logs.jsonl`. For each `message_injected`, it reconstructs peers active **at injection time** based on observed churn downs/rejoins. It counts unique peers that have `received_new` for that message, intersected with the active-at-injection set. Therefore:
`delivery_ratio = sum(delivered_count) / sum(expected_count)` over 240 message opportunities; the denominator varies with concurrent churn and is **not** simply 240×20.

Downloaded `churn_events.json` `delivery_opportunities` readback:
| Method | Injected | Expected peer–message opportunities | Delivered opportunities | Recomputed delivery | Full delivery messages | Source-only messages |
|---|---:|---:|---:|---:|---:|---:|
| Structured | 240 | 4774 | 388 | 0.0812735651 | 8 | 232 |
| DC-SoC | 240 | 4760 | 423 | 0.0888655462 | 10 | 230 |
| AHBN | 240 | 4765 | 623 | 0.1307450157 | 0 | 178 |
| Q-AHBN2 | 240 | 4785 | 1633 | 0.3412748171 | 0 | 63 |

All four recalculated values agree with stored `metrics.json`. This is *not* a denominator arithmetic error. The current `propagation_delay` is the mean maximum receipt timestamp minus injection time for **messages with at least one receipt**, so it is conditional on successful reach and must not be used as evidence of faster network-wide propagation in these low-delivery runs. Zero duplicate counts for Structured/DC-SoC are consistent with extremely restricted reach and do not demonstrate efficiency.

## 2. Experiment configuration alignment (confirmed)
Generated four YAML configurations share `numNodes=20`, `BA_m=2`, seed 42, source peer **1**, targets `[0,5,10,15]`, 240 injections at 0.4 s, absolute churn offsets `[1,26,51,76]` seconds, `settleTime=18`, `k5_h2.actuator_treatment=S5`. Only method/strategy-specific treatment and DC-SoC dynamic-maintenance isolation differ. This rules out a gross discrepancy in these *declared* common inputs, not runtime state divergence. Observed workload is not equivalent to old control-simulator results.

## 3. Forwarding failure mechanism (confirmed for Structured; partially supported for DC-SoC)
- Structured source peer 1 is a leaf whose `cluster_head_id=0`; DC-SoC source peer 1 is also a leaf with `dcsoc_parent=0` in generated topology.
- Structured reaches all expected peers for messages m1–m8. At **m9**, peer 1 logs `k7_forward_attempt` to peer 0 followed by `forward_failed` with `StatusCode.UNAVAILABLE`; m9 reaches only the source. For m10–m240, source-only receipt persists **without forwarding attempts** in captured `peer_stream.jsonl`. One `neighbor_unavailable_observed` event is present.
- Source review of `peer.py` shows failure of `forward_to_peer` marks a peer unavailable; non-head Structured `cluster_targets()` returns `[]` when its cluster head is in `unavailable_neighbors`. Cache clearing happens upon successful later forwarding ACK, while target selection excludes that unavailable peer, so the source cannot initiate the retry through this path. This is a **demonstrated stuck-eligibility mechanism for Structured in the current test**, not proof the frozen AHBN controller is defective.
- DC-SoC delivers m1–m10 to nearly all peers, then m11 reaches only the source and the source logs repeated `DEADLINE_EXCEEDED` forwarding failures to parent 0. DC-SoC `target_peers()` also filters unavailable parents. Its maintenance/rejoin interaction must be separately traced before confirming a complete DC-SoC root cause.
- AHBN peer stream shows 32 forwarding failures, including source 1 → 0, and progressive reach loss; Q-AHBN2 peer stream shows no `forward_failed` events, yet many messages reach few peers. Thus **do not assign the Structured cache mechanism as the sole cause of Q-AHBN2 low delivery** without action/realized-target and per-hop trace analysis.

## 4. Prior-script comparison and interpretation
The prior Gossip canary delivered ~85.15% under the documented seed-42 K7 workload, versus 8.13–34.13% for remaining methods. Gossip selects from the physical neighbor set while Structured/DC-SoC use a single structural gateway from source 1, making gateway loss especially consequential. The compared runs are NONFORMAL and from different source checkouts; neither this contrast nor Q-AHBN2's relative 34.13% permits formal efficacy or superiority claims. A previous 80% research acceptance guideline is not satisfied by the remaining four runs. Report the failure, do not defend it or modify frozen controllers.

## 5. Evidence-integrity audit (partly independently verified)
- Independently traversed canonical RO4 Drive to locate outer evidence tree; found top-level SHA256SUMS plus four per-run SHA256SUMS.
- SHA256 manifest inventories: **108 top-level-referenced files** (the outer file list spans nested folders but excludes SHA256SUMS files by design); **23 entries in each of four run-local manifests**. This proves manifests are present and internally enumerable, **not** full byte-for-byte validation.
- Downloaded all four per-method `peer_stream.jsonl` and independently SHA256-hashed the raw bytes; all four match their run-local Drive checksum records:
  - Structured `77b5ad24e5f71e335dcf5c023d7e3b596d2e0a0a6e763f2546fd57b6f0fbbf30`
  - DC-SoC `a109ad9e4326dc5caa361a0d344157312649c7a6f6bda9229e693afd92622747`
  - AHBN `f087c9a9252bd4e69e17cb954efc2c3bb24fb118b3c83efb0dfdbd57c89d307a`
  - Q-AHBN2 `62ac0ca7ac2515600c1b352231135f94ce3b63e6694000cf75be1275547f1ee0`.
- Also SHA256-checked four downloaded generated YAML files against the outer checksum records: all **4/4 MATCH**.
- Per-method `validation.txt` returned `K7 RESULT VALIDATION PASS` after the metrics JSON; recorded exit/cleanup statuses are zero/PASS, pod spec/runtime parity was earlier checked 20/20 per method. A fresh kubectl cleanup inventory was **not** performed in this read-only post-run audit.
- **Not yet verified:** every one of the 108 outer-listed files and the 23×4 run-local checksums on researcher checkout. Dedicated read-only verifier `gke/scripts/audit_d7_sm_postrun_readonly.py` prepared; run it on existing untouched evidence. Do not mark FULL CHECKSUM PASS beforehand.

## 6. Controlled decision and next action
**P1 causal audit: root-cause candidate for Structured is strongly evidenced; other methods require further mechanism audit. Full evidence integrity verification PENDING.** Operational four-method smoke **4/4 PASS** for scripted validator and recorded cleanup, but **scientific adequacy HOLD**. `D7-F 0/25 HOLD`; `D8 HOLD`. No algorithm, actuator, RL, metric, experiment or publication changes authorized.

Researcher next executes ONLY the read-only audit script against existing evidence, preserves its JSON output separately, and reports checksum status. Next technical gate should inspect post-churn neighbor re-eligibility and AHBN/Q-AHBN2 realized-target propagation without changing frozen designs or running GKE until an explicitly reviewed correction and new smoke plan exists.
