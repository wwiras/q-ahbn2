# JCC-R1A-C3-D7-SM-CANARY — Live GKE post-run evidence audit (2026-10-17)

## Decision
**PASS — one NONFORMAL Gossip seed-42 canary (1/1).** This closes the single-canary execution and evidence gate only. Remaining smoke methods **0/4 HOLD**; formal D7-F **0/25 HOLD**; D8 **HOLD**. Future runs need separate controlled release. Scientific controllers/design unchanged.

## Provenance
- Researcher executed the canary locally on 2026-10-17 using synchronized source commit `40f596411060da1a9bc9ee4458b2c2195375033b`; terminal preflight showed clean worktree and same local/remote commit.
- Workload: Gossip, seed 42, N=20, BA(m=2), 240 messages at 0.4 s spacing, four churn events; dedicated namespace `qahbn2-d7-smoke-gossip`; pinned container digest `sha256:8a47cedb378d9387b87e7e2d5924a4aa2f87053e71da757509b1f19667332466`.
- Canonical evidence location, independently located in connected Drive: https://drive.google.com/drive/folders/1drKb5LsU9CxGAeB34r-TvZrNiu-c5CN_ (`q-ahbn2/output/evidence/20261017T112101Z-D7-SM-canary`).
- Read back Drive `runs/gossip/validation.txt`, `cleanup_status.txt`, and `experiment_exit_status.txt`. Researcher supplied full terminal SHA256SUMS verification output: all listed entries OK; no independent cross-file byte comparison was performed in this audit.

## Operational outcome
- Helm install/upgrade completed, 20/20 peer pods reached Ready, controller Job completed.
- `experiment_exit_status.txt=0`; `cleanup_status.txt=PASS`; `K7 RESULT VALIDATION PASS`.
- Researcher post-run namespace query produced no namespace output, consistent with successful removal.
- Top-level status states `canary NONFORMAL SMOKE RUNS COMPLETED; awaiting independent evidence review` (historical launcher-written text, not a new run).

## Observations — one nonformal run only
- delivery_ratio = 0.8514644351464435 (85.15%); propagation_delay = 0.10765208701292674 s as reported; duplicates = 2206; total_forwards = 3848; F_attempt = 6096; F_success = 3848.
- churn_events = 4; recovered_events = 2. Event 1 recovery_time_s = 27.619971990585327; event 2 = 2.8216521739959717. Events 3 and 4 are right-censored at 18 s, **not successful recovery events**.
- Exceeding the working operational 80% delivery threshold is not an across-method, multiseed, or formal scientific conclusion. Do not extrapolate comparative superiority or statistical significance from this one canary.

## Limitation and next gate
This is a successful live feasibility/validation canary, not formal D7-F evidence. No algorithms, outcomes, statistical analyses, manuscript results or claims are revised. Follow-up requires separately reviewed workflow for the other four smoke methods (the current launcher only permits `SMOKE_MODE=canary`) before D7-F formal entry.
The Q-AHBN manuscript remains **under peer review at Journal of Cloud Computing**, unpublished, without DOI.
