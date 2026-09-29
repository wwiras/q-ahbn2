# S11 — ControlSim Aggregation

**Status:** ACTIVE — S11-RECON-1 PASS / S11-A-PREP RELEASED

## Objective
Aggregate only completed, integrity-verified formal ControlSim evidence according to `docs/04_STATISTICAL_CONTRACT.md`.

## S11-A — Primary RO4 aggregation
Aggregate Exp10-Q, Exp11-Q and Exp12-Q as the primary AHBN-versus-Q-AHBN2 evidence. Preserve paired seed analysis, condition-specific trade-offs, dissemination outcomes, and frozen learning/action evidence.

## S11-B — Exp13-Q external benchmark aggregation
Aggregate Exp13-Q separately as bounded five-method publication-positioning evidence under the single frozen churn=0.40 scenario. Do not merge Exp13 into the primary RO4 causal result family.

## Boundary
No experimental parameter may change here. No unfavorable valid run may be silently excluded. No omnibus winner score, global algorithm ranking, or post-hoc test shopping is permitted.

## S11-RECON-1 — Frozen Input / Schema / Analysis-Code Reconciliation — 2026-09-29

**Status:** PASS / CLOSED.

### Gate
Read-only scientific reconciliation and analysis-readiness audit over frozen formal inputs, schemas, pairing keys, analysis code, and execution specifications for Stage S11.

### 1. Repository reconciliation
- Current GitHub HEAD: `ff567b2ed4e844d3943f6669d1dcc31e8fbc1782`
- Working tree: clean on branch `main`, synchronized with `origin/main`
- Stage closure status of predecessors:
  - S08 (Exp10-Q Failure): PASS / CLOSED (`S08-CLOSE`, commit `2ad57c8`)
  - S09 (Exp11-Q Churn): PASS / CLOSED (`S09-CLOSE`, commit `d781b0f`)
  - S10 (Exp12-Q Heterogeneity): PASS / CLOSED (`S10.6`, commit `e999951`)
  - S10A (Exp13-Q Reference Benchmark): PASS / CLOSED (`S10A-FREEZE`, commit `cdba851`)
- Exclusions / reruns across all experiments: 0 exclusions, 0 reruns (105/105 valid runs).
- Scientific parameters: immutable.

### 2. Frozen input reconciliation
All four formal datasets verified directly against disk and provenance metadata:
- **Exp10-Q Failure:**
  - Formal CSV: `output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal/exp10q_formal.csv`
  - Provenance: `manifest.json`, `RUN.md`
  - Runs: 20/20 data rows; methods: `{ahbn, qahbn2}`; seeds: `{42, 43, 44, 45, 46}`; conditions: `{control, failure}`; exclusions: 0, reruns: 0.
- **Exp11-Q Churn:**
  - Formal CSV: `output/evidence/q-ahbn-28092026203251-exp11q-formal/exp11q_formal.csv`
  - Provenance: `manifest.json`, `RUN.md`, `integrity_report.json`
  - Runs: 30/30 data rows; methods: `{ahbn, qahbn2}`; seeds: `{42, 43, 44, 45, 46}`; churn levels: `{0.0, 0.2, 0.4}`; exclusions: 0, reruns: 0.
- **Exp12-Q Heterogeneity:**
  - Formal CSV: `output/evidence/Exp12-Q/q-ahbn-28092026215008-exp12q-formal/exp12q_formal.csv`
  - Provenance: `manifest.json`, `RUN.md`
  - Runs: 30/30 data rows; methods: `{ahbn, qahbn2}`; seeds: `{42, 43, 44, 45, 46}`; resource profiles: `{balanced, moderate_heterogeneity, weak_heavy}`; exclusions: 0, reruns: 0.
- **Exp13-Q Reference Benchmark:**
  - Formal CSV: `output/evidence/Exp13-Q/q-ahbn-29092026081836-exp13q-formal/exp13q_formal.csv`
  - Provenance: `manifest.json`, `RUN.md`
  - Runs: 25/25 data rows; methods: `{gossip, structured, dcsoc, ahbn, qahbn2}`; seeds: `{42, 43, 44, 45, 46}`; churn level: `{0.4}`; exclusions: 0, reruns: 0.

### 3. Schema and deterministic pairing key reconciliation
- Primary outcomes verified across all rows:
  - `delivery_ratio`: float in [0, 1]
  - `propagation_delay`: float > 0
  - `duplicates`: float/int >= 0
  - `total_forwards`: float/int >= 0
- Deterministic pairing key:
  - Exp10-Q: `(condition, seed)` -> exactly 10 pairs (5 control, 5 failure)
  - Exp11-Q: `(churn_level, seed)` -> exactly 15 pairs (5 per churn level: 0.0, 0.2, 0.4)
  - Exp12-Q: `(resource_profile, seed)` -> exactly 15 pairs (5 per profile: balanced, moderate_heterogeneity, weak_heavy)
  - Exp13-Q: `(churn_level, seed)` -> exactly 5 AHBN vs Q-AHBN2 pairs, plus 5 same-seed runs for Gossip, Structured, and DC-SoC.
- Pairing check result: 100% matched across all conditions and seeds. Zero missing, duplicate, or unpaired cells.

### 4. Preservation of scientific separation
- **S11-A (Primary RO4/RQ4 Causal Evaluation):**
  - Consists strictly of Exp10-Q, Exp11-Q, and Exp12-Q (total 80 runs, 40 paired AHBN vs Q-AHBN2 comparisons).
  - Evaluates causal adaptation across failure, churn, and heterogeneity.
- **S11-B (Bounded External Reference Positioning):**
  - Consists strictly of Exp13-Q (total 25 runs, 5 methods at churn=0.40).
  - Strict boundary: Exp13-Q is not merged into S11-A.

### 5. Frozen statistical contract verification
- Per-cell descriptive metrics (n=5): arithmetic mean, sample standard deviation (s, ddof=1), and two-sided 95% Student-t confidence interval (df=4, t_0.975,4 = 2.7764451051977987).
- Paired differences: Delta_i = QAHBN2_i - AHBN_i, mean paired difference, sample standard deviation of paired differences, two-sided 95% Student-t confidence interval, and individual 5 seed differences.
- Metric directions:
  - `delivery_ratio`: positive Delta = higher Q-AHBN2 delivery
  - `propagation_delay`: negative Delta = lower Q-AHBN2 delay
  - `duplicates`: negative Delta = fewer Q-AHBN2 duplicates
  - `total_forwards`: negative Delta = fewer Q-AHBN2 forwards
- Learning/adaptation summaries (n=5): `mean_reward`, `cumulative_reward`, `q_updates`, `state_action_coverage`, `intervention_count`, `keep_count`, and aggregated action distributions with per-seed retention.
- Strictly prohibited: no composite Adaptation Efficiency score, no omnibus winner score, no global ranking, no post-hoc metric selection, no hypothesis test shopping.

### 6. Existing analysis-code audit
- Repository audit confirms no tracked standalone aggregation script exists in `scripts/` or `qahbn2/`.
- The Exp10-Q analysis artifact (`output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal-analysis/exp10q_formal_analysis.json`) was generated during S08-FORMAL-3 using an ad-hoc inline Python script specialized to Exp10-Q conditions ('control', 'failure').
- Classification: **Option C** — a new minimal deterministic S11 aggregation script is required (`scripts/aggregate_s11a_formal.py`), generalizing the verified S08 analysis prototype to handle the full S11-A matrix without modifying mathematical formulas or statistical contracts.

### 7. S11-A execution specification
- **Target subgate:** `S11-A-PREP — Implement Deterministic S11-A Aggregation Script + Unit Test`
- **Followed by:** `S11-A-1 — Primary RO4 Deterministic Descriptive + Paired Aggregation`
- **Inputs:**
  - `output/evidence/Exp10-Q/q-ahbn-28092026183635-exp10q-formal/exp10q_formal.csv`
  - `output/evidence/q-ahbn-28092026203251-exp11q-formal/exp11q_formal.csv`
  - `output/evidence/Exp12-Q/q-ahbn-28092026215008-exp12q-formal/exp12q_formal.csv`
- **Output directory:** `output/evidence/s11-aggregation/s11a-primary-ro4/`
- **Expected artifacts:**
  - `s11a_primary_ro4_aggregation.json` (machine-readable, full precision)
  - `s11a_primary_ro4_summary.csv` (human/publication-auditable summary table)
  - `RUN.md` and `manifest.json` (metadata and verification provenance)
- **Validation assertions:**
  - 80/80 input rows ingested and validated
  - Exactly 40 paired comparisons verified
  - Exact numerical reproduction of previously verified Exp10-Q formal analysis values
  - Zero NaN or non-finite values in primary outcomes
  - Action distribution sums reconcile with total intervention + keep counts.
- **Execution actor:** Safe for deterministic execution by Antigravity under the Master workflow once S11-A-PREP is complete.

## Result
$$\boxed{\textbf{S11-RECON-1 = PASS / CLOSED}}$$

All authoritative inputs reconciled; schemas known; pairing verified; S11-A/S11-B scientific separation preserved; statistical contract verified; exact deterministic next action defined.

## Next permitted action
$$\boxed{\textbf{S11-A-PREP — Implement Deterministic S11-A Aggregation Script + Unit Test}}$$

