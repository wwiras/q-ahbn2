# S11 — ControlSim Aggregation

**Status:** ACTIVE — S11-A-1 PASS / CLOSED; S11-B NEXT

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

## S11-A-PREP — Implement Deterministic S11-A Aggregation Script + Unit Test — 2026-09-29

**Status:** PASS / CLOSED.

### Gate
Implement and verify the minimal deterministic analysis script and test suite for S11-A primary RO4 aggregation conforming strictly to `docs/04_STATISTICAL_CONTRACT.md`.

### 1. Created files
- Implementation script: `scripts/aggregate_s11a_formal.py`
- Test suite: `tests/test_aggregate_s11a.py`

### 2. Implementation summary
- **Scope restriction:** S11-A includes only Exp10-Q (Failure), Exp11-Q (Churn), and Exp12-Q (Heterogeneity). Exp13-Q is explicitly excluded and reserved for S11-B.
- **Statistical contract compliance:**
  - Per-cell descriptive metrics ($n=5$): arithmetic mean, sample standard deviation ($s$, `ddof=1`), and two-sided 95% Student-t confidence interval ($df=4$, $t_{0.975,4} = 2.7764451051977987$).
  - Paired comparison: $\Delta_i = QAHBN2_i - AHBN_i$ paired strictly by same seed ($s \in \{42, 43, 44, 45, 46\}$); reports seed differences in seed order, mean paired difference, sample SD of differences, 95% Student-t CI, and relative change percent.
  - Delivery ratio additionally computes absolute percentage-point difference ($\text{mean}(\Delta) \times 100$).
  - Primary outcomes: `delivery_ratio`, `propagation_delay`, `duplicates`, `total_forwards`.
  - Q-AHBN2 learning/adaptation summaries: `mean_reward`, `cumulative_reward`, `q_updates`, `state_action_coverage`, `intervention_count`, `keep_count`, and aggregated action distributions with per-seed retention.
- **Data integrity guards:**
  - Verifies matrix completeness and uniqueness (20 runs for Exp10-Q, 30 runs for Exp11-Q, 30 runs for Exp12-Q; exactly 80 runs and 40 paired comparisons across S11-A).
  - Verifies all primary metrics are finite and within logical domains (`delivery_ratio` $\in [0, 1]$, `propagation_delay` $> 0$, `duplicates` $\ge 0$, `total_forwards` $\ge 0$).
  - Verifies read-only file ingestion with zero mutation of source CSV files.

### 3. Verification and test results
Command:
```bash
PYTHONPATH=. python3 -m unittest tests/test_aggregate_s11a.py -v
```
All 14 unit tests executed and passed (14/14 PASS, 0 failures, 0 errors):
1. `test_exp10q_regression_parity_cell_summaries`: 100% numerical reproduction of Exp10-Q cell summaries against frozen oracle `exp10q_formal_analysis.json` within IEEE double precision ($< 10^{-12}$).
2. `test_exp10q_regression_parity_paired_effects`: 100% numerical reproduction of Exp10-Q paired effects against frozen oracle within $< 10^{-12}$.
3. `test_exp10q_regression_parity_learning`: 100% numerical reproduction of Exp10-Q learning summaries and action distribution against frozen oracle within $< 10^{-12}$.
4. `test_expected_primary_metrics`: verified exact primary metrics and rejection of missing, non-finite, or out-of-bounds metric values.
5. `test_exact_same_seed_ahbn_qahbn2_pairing`: verified pairing invariant across arbitrary row permutations.
6. `test_duplicate_pair_detection`: verified rejection of duplicate cells.
7. `test_missing_pair_detection`: verified rejection of incomplete matrices.
8. `test_deterministic_seed_ordering`: verified deterministic seed ordering ($42, 43, 44, 45, 46$).
9. `test_sample_sd_rather_than_population_sd`: verified sample SD ($ddof=1$) is strictly used over population SD.
10. `test_correct_student_t_ci_computation`: verified Student-t multiplier $t_{0.975,4} = 2.7764451051977987$ and rejection of normal $z=1.96$.
11. `test_no_mutation_of_source_csv_files`: verified SHA-256 invariance of source CSV files before and after aggregation.
12. `test_exp13q_excluded_from_s11a_scope`: verified Exp13-Q is strictly excluded from S11-A configuration.
13. `test_summary_csv_schema_and_generation`: verified summary table schema and column generation.
14. `test_prep_boundary_no_formal_aggregation_released`: verified formal release directory `output/evidence/s11-aggregation/s11a-primary-ro4` does not exist during PREP.

Full test suite execution:
```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```
56 tests executed: 53 passed, 3 skipped (canonical AHBN checkout not present in environment), 0 failures, 0 errors.

### 4. PREP boundary confirmation
- No raw evidence modified (CSV and metadata SHA-256 unchanged).
- No experiment parameter changed.
- No AHBN or Q-AHBN2 algorithmic code changed.
- No formal S11-A aggregation executed or released during this PREP gate.
- Scientific performance of Exp11-Q and Exp12-Q was not evaluated or interpreted.

## Result
$$\boxed{\textbf{S11-A-PREP = PASS / CLOSED}}$$

Minimal deterministic S11-A aggregation script and comprehensive unit test suite implemented, verified against frozen regression oracle, and confirmed compliant with the statistical contract.

## Next permitted action
$$\boxed{\textbf{S11-A-1 — Primary RO4 Deterministic Descriptive + Paired Aggregation}}$$

Execute `scripts/aggregate_s11a_formal.py` over frozen Exp10-Q, Exp11-Q, and Exp12-Q formal datasets to generate `s11a_primary_ro4_aggregation.json` and `s11a_primary_ro4_summary.csv` under `output/evidence/s11-aggregation/s11a-primary-ro4/`.



## S11-A-1 — Primary RO4 Deterministic Descriptive + Paired Aggregation — 2026-09-29

**Status:** PASS / CLOSED.

### Gate
Execute the frozen deterministic S11-A aggregator over Exp10-Q, Exp11-Q and Exp12-Q only, then freeze and reconcile the resulting aggregation evidence without scientific interpretation.

### Execution and artifact freeze
- Executed script: `scripts/aggregate_s11a_formal.py` from Git commit `59ef254099fb3edb617f323dd864324c320d9a85`.
- Actual immutable execution directory: `output/evidence/q-ahbn-29092026111238-s11a-aggregation-formal/`.
- The earlier planned path `output/evidence/s11-aggregation/s11a-primary-ro4/` was not used; the successful timestamped execution directory is authoritative and was not moved or regenerated merely to match the planned pathname.
- Artifacts: `RUN.md`, `manifest.json`, `s11a_primary_ro4_aggregation.json`, `s11a_primary_ro4_summary.csv`.
- Runs ingested: 80/80 (Exp10-Q 20 + Exp11-Q 30 + Exp12-Q 30).
- Same-seed AHBN/Q-AHBN2 paired comparisons: 40/40.
- Exp13-Q excluded from S11-A as required.
- Output SHA-256: aggregation JSON `bec818623c97ae2d9918617694694e90448a2727d703ce72a8923557c48ac337`; summary CSV `9b2d21a103c9cd115acc56a003eb8bab60a49db92bc82af3a8da004d03b33833`.

### Input provenance reconciliation
Direct local SHA-256 readback, S11-A manifest records, and raw-byte Google Drive readback agree exactly:
- Exp10-Q: `c51392ce83435bb15691d60b42cfb5c91971687f05b51c1bd21a2f69444edcf7`
- Exp11-Q: `d869f4c76cd139b2dd554de5e5a8bf61d8403e8b223106f7809200676347f00c`
- Exp12-Q: `dd5504109cae59b1494dc409308585906676f69c79e0c41d3845856e6762bc66`

The different hashes recorded during S11-A-PREP (`fc2bba...`, `e0970a...`, `1f465d...`) are retained as an audit-trail provenance-record discrepancy. They are not evidence of formal-input mutation: the authoritative promoted Drive CSV bytes, current local frozen CSV bytes, and S11-A manifest hashes match exactly. No raw formal evidence was rewritten to reconcile this record.

### Google Drive preservation
- Promoted evidence folder: `q-ahbn-29092026111238-s11a-aggregation-formal`
- Drive folder ID: `1XMWn5FWKwJV78YeTGakJb1bVJ6XKfrLH`
- Readback confirmed all four expected artifacts are present in the designated `output/evidence` hierarchy.
- No duplicate freeze copy was created and no artifact was moved or regenerated.

### Scientific boundary
This gate establishes deterministic aggregation completion, provenance integrity and evidence preservation only. It does not interpret comparative performance, change any metric or parameter, exclude any valid run, or merge Exp13-Q into the primary S11-A result family.

## Result
$$\boxed{\textbf{S11-A-1 = PASS / CLOSED}}$$

## Next permitted action
$$\boxed{\textbf{S11-B — Exp13-Q External Benchmark Aggregation}}$$

Exp13-Q remains a separate bounded five-method external reference analysis at churn=0.40 and must not be merged into S11-A.


## S11-B-PREP — Minimal Deterministic Exp13-Q Aggregation Script + Unit Tests — 2026-09-29

**Status:** PASS / CLOSED.

### Gate
Implement only the deterministic aggregation logic and unit tests required for the frozen Exp13-Q five-method reference benchmark. No formal aggregation execution or scientific interpretation is authorized in PREP.

### Implementation
- Script: `scripts/aggregate_s11b_exp13q.py`
- Tests: `tests/test_aggregate_s11b_exp13q.py`
- Frozen matrix enforced: churn=0.40; methods `{gossip, structured, dcsoc, ahbn, qahbn2}`; seeds `{42,43,44,45,46}`; 25/25 cells.
- Primary metrics only: `delivery_ratio`, `propagation_delay`, `duplicates`, `total_forwards`.
- Per-method summaries: n=5, arithmetic mean, sample SD, two-sided 95% Student-t CI (df=4), ordered seed values.
- Same-seed Q-AHBN2-minus-reference contrasts are structurally defined for AHBN, Gossip, Structured and DC-SoC. No p-values are calculated by default.
- Explicit guards prohibit incomplete/duplicate cells, unexpected methods/seeds/churn, invalid metric domains, and source mutation.
- No omnibus score, cross-metric ranking, winner statistic, or S11-A input is present.
- Formal release pipeline is deliberately absent during PREP.

### Verification state
Researcher-local execution against synchronized `main` completed successfully:
- Dedicated command: `PYTHONPATH=. python3 -m unittest tests/test_aggregate_s11b_exp13q.py -v`
- Dedicated result: **12/12 PASS; 0 failures; 0 errors**.
- Full regression command: `PYTHONPATH=. python3 -m unittest discover -s tests -v`
- Full regression result: **68/68 PASS; 0 failures; 0 errors**.
- PREP boundary remained intact: no formal Exp13-Q aggregation was released during verification.

### Result
$\\boxed{\\textbf{S11-B-PREP = PASS / CLOSED}}$

The deterministic Exp13-Q aggregation implementation and tests are verified and ready for the bounded formal aggregation gate. No scientific interpretation has been performed.

### Next permitted action
$\\boxed{\\textbf{S11-B-1 — Exp13-Q Deterministic Five-Method External Benchmark Aggregation}}$

S11-B-1 may execute only the frozen 25-run Exp13-Q dataset at churn=0.40 under the verified statistical contract. It must preserve S11-A/S11-B separation and must not introduce ranking, omnibus scoring, post-hoc comparator selection, or scientific interpretation.


## S11-B-1 — Exp13-Q Deterministic Five-Method External Benchmark Aggregation — 2026-09-29

**Status:** PASS / CLOSED.

### Formal execution and verification
- Formal aggregation directory: `output/evidence/q-ahbn-29092026121201-s11b-aggregation-formal/`
- Producing Git HEAD recorded by manifest: `3ab956c2de6db9b6c4ae8daec1135669d58ba6fb`
- Dedicated formal-release test: **1/1 PASS; 0 failures; 0 errors**.
- Full repository regression: **69/69 PASS; 0 failures; 0 errors**.
- Frozen input: Exp13-Q only, 25/25 runs, churn=0.40, methods `{gossip, structured, dcsoc, ahbn, qahbn2}`.
- Primary metrics only: `delivery_ratio`, `propagation_delay`, `duplicates`, `total_forwards`.
- Source CSV SHA-256: `5b9f09c8403e7e287d631986fb76727542264eca5f07227b57d3e19b868c4708`; direct local readback equals manifest record.
- Output SHA-256:
  - `RUN.md`: `4fc17f39d2b8fec21de5321d31d3c47a841745f1be2381e117133ca1383d997d`
  - `manifest.json`: `6919e338c1835536a59d063b336d8b85f9990f3b45d8a960cc9b48c48ddac897`
  - `s11b_exp13q_aggregation.json`: `37ba7c1d77c93af21d3c2581d3f95b6752858afd5f461d1231850d625d6ec223`
  - `s11b_exp13q_summary.csv`: `e48c0d2a4479a05ed5826fe83c627dceef71f2629f316e303924d7adb16d0aa3`
- Manifest-recorded aggregation JSON and summary CSV hashes agree exactly with direct SHA-256 readback.
- Repository was clean after formal execution.

### Evidence preservation
- Google Drive evidence folder: `q-ahbn-29092026121201-s11b-aggregation-formal`
- Drive folder ID: `1frfPsofGtbvpRFCxFMjGi_EZUuv8tNxx`
- Drive readback confirms exactly four expected artifacts: `RUN.md`, `manifest.json`, `s11b_exp13q_aggregation.json`, and `s11b_exp13q_summary.csv`.
- The synchronized evidence folder already existed in the designated `output/evidence` hierarchy; no duplicate promotion copy was created.

### Scientific boundary
S11-B-1 establishes deterministic descriptive aggregation and the predeclared same-seed Q-AHBN2-minus-reference contrasts only. It remains separate from S11-A. No p-values, omnibus score, cross-metric ranking, post-hoc comparator selection, winner claim, or scientific interpretation was produced.

## Result
$$\boxed{\textbf{S11-B-1 = PASS / CLOSED}}$$
