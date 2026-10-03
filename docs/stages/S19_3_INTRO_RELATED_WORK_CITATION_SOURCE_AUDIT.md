# S19-3 — Introduction / Related Work Citation-Source Audit

**Status:** PASS / CLOSED — 2026-10-03

## Objective
Audit MI-02 only: determine which existing Introduction / Related Work claims require stronger source support, identify suitable verified sources, and freeze a claim-to-source integration plan for S19-4.

This gate is audit-only. It does **not** insert citations, add bibliography entries, restructure sections, or change scientific claims.

## Authoritative inputs
- `docs/00_QAHBN2_MASTER.md`
- `docs/00_SOURCE_AUTHORITY_REGISTER.md`
- `docs/stages/S19_2_RO2_AHBN_QAHBN_PROGRESSION_CLARIFICATION.md`
- manuscript `wwiras/QAHBN2-Manuscript/versions/v0.0/main.tex`
- manuscript `docs/MANUSCRIPT_MASTER.md`
- manuscript `docs/PROVENANCE.md`
- existing S13 Related Work source audit
- science Drive root ID `1a6_WrsZL2iXbFVeMemdujYxvzEqcBFC5`
- manuscript Drive folder ID `1oQxyLENPvG-r10zuq62Au7AFyeeSpDxj`
- latest AHBN Scientific Reports reference manuscript supplied by researcher
- vetted primary-paper PDFs available in Google Drive

Pinned manuscript science baseline remains:
`6ccc94e5df770d588a5ccfa592f603a9a8ab2c68`

## Reconciliation findings
- GitHub remains authoritative for source/control state.
- Both Drive roots were read back successfully and match the expected synchronized science/manuscript workspaces.
- Repository-local `output/` remains working output unless deliberately promoted; no evidence promotion is involved in S19-3.
- Active manuscript source was **not modified** at this gate.
- Existing `versions/v0.0/references.bib` is currently empty; existing citation keys are nevertheless already registered in S13 control records and remain researcher-managed for later bibliography synchronization.

## Existing verified source set retained from S13
The prior S13 source audit already verified the following source set against original Drive PDFs or frozen thesis verification records:

| Citation key | Source role already authorized |
|---|---|
| `berendea_fair_2020` | blockchain gossip mechanisms; propagation latency / bandwidth trade-off |
| `felber_pulp_2012` | adaptive push/pull gossip; coverage / redundancy / delay trade-off |
| `rohrer_kadcast-ng_2023` | structured Kademlia-derived blockchain broadcast; tunable delay / overhead / reliability trade-offs |
| `shen_sekad_2024` | clustered / Kademlia structured blockchain dissemination |
| `dong_dc-soc_2024` | density-clustered + gossip-oriented consortium-blockchain dissemination |
| `choi_optimizing_2024` | blockchain-specific RL/DQN neighbour-selection adaptation |
| `boyan_packet_1993` | foundational Q-routing in dynamically changing networks |
| `polverini_-network_2025` | decentralized Q-learning packet forwarding / network adaptation |

S19-3 does not reopen the accuracy of those already-verified citation relationships.

## Additional vetted sources identified for MI-02 strengthening
The audit identified several already-held Drive papers that directly support currently uncited framing claims:

1. **Shahsavari, Zhang and Talhi (2022), _A Theoretical Model for Block Propagation Analysis in Bitcoin Network_**
   - Drive ID: `1i2eRhdyvhM3D1ro1UUKu4-M2aAxmQer1`
   - Direct support:
     - blockchain P2P performance depends on configurable network/design parameters;
     - propagation delay and traffic overhead are jointly affected by network configuration;
     - performance behaviour varies with parameters rather than admitting one context-free setting;
     - simulation/modeling is used to study these trade-offs.

2. **Pei et al. (2024), _Matching-Gossip: Optimizing Blockchain Broadcast Performance to Address the CAP Trilemma_**
   - Drive ID: `1ZPuC-p5kJAKKBH_7msoCxvF9ldsEKjva`
   - Direct support:
     - Gossip randomness can cause link/message duplication and extra traffic;
     - topology mismatch influences propagation efficiency;
     - network-layer broadcast design is a material blockchain performance factor;
     - both simulation and real-world evaluation are used.

3. **Rohrer and Tschorsch (2023), _Kadcast-NG_**
   - already in retained source set
   - original Drive PDF rechecked:
     - unstructured blockchain broadcast is robust but duplication-heavy;
     - limiting gossip scope can reduce load but add delay;
     - structured broadcast exposes explicit delay/overhead/reliability trade-offs.

4. **Berendea et al. (2020), _Fair and Efficient Gossip in Hyperledger Fabric_**
   - already in retained source set
   - original Drive PDF rechecked:
     - block dissemination is critical for performance/consistency;
     - Fabric gossip exhibits heavy-tail propagation latency;
     - improved gossip jointly optimizes propagation time, tail latency, and bandwidth.

5. **Optional source family, not yet required for S19-4 unless exact claim need remains**
   - Perigee / topology-learning blockchain literature held in Drive;
   - recent overlay/topology studies and surveys held in Drive.
   These are not released for insertion by default because the current paper can be strengthened adequately without broadening the literature footprint unnecessarily.

## Claim-to-source audit matrix

| ID | Current manuscript claim / location | Audit status | Verified support released for S19-4 | Integration instruction |
|---|---|---|---|---|
| C19-3-01 | Introduction opening: changing network conditions can alter timely-delivery / communication-overhead balance | **NEEDS CITATION** | Shahsavari 2022; Berendea 2020; Kadcast-NG 2023 | Add 1–2 citations at paragraph end; do not add new factual detail |
| C19-3-02 | Introduction: peer failures, churn, heterogeneous processing, transient load and topology opportunities affect dissemination behaviour | **PARTIALLY SUPPORTED / CLAIM TOO BROAD FOR ONE SOURCE** | Kadcast-NG supports node failures; Berendea supports challenging broadcast conditions incl. churn/packet loss; Shahsavari supports parameter sensitivity; AHBN manuscript/project lineage supports evaluated condition set | Prefer a compact multi-citation set and retain cautious “can alter” wording; do not claim every source studies every factor |
| C19-3-03 | Introduction: fixed dissemination characterization motivates runtime adaptation; fanout / structure / operating conditions shift delay-delivery-redundancy trade-off | **NEEDS CITATION** | Existing S13 gossip/structured sources + Shahsavari 2022 + Kadcast-NG 2023 | Cite literature for general trade-off; prior-project characterization remains internal lineage and should not be represented as an external paper unless publication source exists |
| C19-3-04 | Introduction: no uniformly preferable static operating point | **SUPPORTABLE ONLY AS BOUNDED SYNTHESIS** | Multiple trade-off sources collectively support condition dependence | Keep wording bounded; cite 2–3 sources. Do not phrase as a universal theorem |
| C19-3-05 | Introduction AHBN mechanism description | **NO EXTERNAL CITATION REQUIRED FOR CURRENT PAPER MECHANISM** | canonical AHBN authority / latest AHBN manuscript | If citation architecture permits self-citation in S19-4, cite AHBN manuscript; otherwise method section remains primary internal authority |
| C19-3-06 | Related Work opening: dissemination research spans probabilistic, structured, adaptive/composite, learning-assisted strands | **CITATION DENSITY CAN BE STRENGTHENED** | retained S13 source set covers all four strands | Add a compact citation cluster, not one citation after every noun |
| C19-3-07 | Gossip paragraph: redundancy can help progress but duplicates consume resources | **NEEDS DIRECT SUPPORT** | Berendea 2020; Matching-Gossip 2024; Pulp 2012 | Add 1–2 citations near trade-off sentence |
| C19-3-08 | Gossip family variability in neighbour selection / push-pull / forwarding / recovery | **SUPPORTABLE** | Berendea 2020; Pulp 2012; Matching-Gossip 2024 | Existing Berendea citation may remain; optionally augment with Pulp/Matching-Gossip |
| C19-3-09 | Structured paragraph: structure constrains redundant dissemination / shapes propagation paths | **SUPPORTABLE** | Kadcast-NG 2023; SEKad 2024 | Existing citations are sufficient; no mandatory increase |
| C19-3-10 | Hybrid paragraph: composition ≠ runtime adaptation | **CONCEPTUAL DEFINITION / NO NEW SOURCE REQUIRED** | DC-SoC example + paper's explicit distinction | Retain as analytical distinction; existing DC-SoC citation sufficient |
| C19-3-11 | Runtime-adaptive networking links observations/events to subsequent forwarding/routing changes | **CITATION SHOULD BE STRENGTHENED** | Pulp 2012; Choi 2024; Boyan 1993; Polverini 2025 | Add 2-source support spanning networking + blockchain-specific adaptation |
| C19-3-12 | AHBN adaptation is informed by condition-dependent trade-offs from prior systematic characterization | **PROJECT-LINEAGE CLAIM** | Q-AHBN2 master + AHBN scientific authority; external literature supports general trade-off only | If citing AHBN manuscript is acceptable, use it; do not substitute unrelated external papers as proof of project lineage |
| C19-3-13 | Learning paragraph: RL has been applied to changing network observations / routing decisions | **ALREADY WELL SUPPORTED** | Choi 2024; Boyan 1993; Polverini 2025 | Existing citations sufficient |
| C19-3-14 | Q-AHBN architecture positioning vs literature | **NO ADDITIONAL EXTERNAL SOURCE REQUIRED** | current paper mechanism + cited comparator literature | Keep architecture-based positioning; avoid uniqueness claim |

## S19-4 released citation set
S19-4 may use:
- the existing eight S13-verified citation keys;
- **Shahsavari 2022**;
- **Matching-Gossip 2024**;
- the latest AHBN Scientific Reports manuscript as a self-citation / lineage source if the researcher-managed bibliography provides or creates the corresponding key.

No other source is needed unless S19-4 encounters an exact unsupported sentence that cannot be covered by this set.

## Bibliography control finding
`versions/v0.0/references.bib` is currently empty even though `main.tex` already contains citation keys. This is a **production/bibliography synchronization issue**, not a scientific source-validity defect.

S19-3 does not populate the bibliography because:
- this gate is audit-only;
- the prior S13 contract explicitly left Zotero/BibTeX synchronization researcher-managed;
- actual citation insertion and bibliography synchronization belong to S19-4 / later production closure.

S19-4 must verify that every newly inserted citation key is present in the eventual active bibliography before S19-7 compile/proof closure.

## Scientific boundary verification
No new novelty, gap, superiority, ranking, convergence, optimality, generic low-overhead, causal, or cross-environment claim is authorized by this audit.

The audit distinguishes:
- external literature support for general dissemination/networking claims;
- internal canonical authority for AHBN/Q-AHBN mechanism and project lineage;
- experimental evidence for Q-AHBN results.

These evidence types must not be substituted for one another.

## Result
**S19-3 = PASS / CLOSED.**

## Next permitted task
**S19-4 — Citation-Density Integration** is the next and only released action.

S19-4 may add only citations released by this audit and make minimal local wording adjustments required for citation fit. It must not restructure Introduction/Related Work or introduce stronger claims.
