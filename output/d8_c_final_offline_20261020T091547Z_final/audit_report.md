# D8-C final offline evidence integrity audit

**Decision: PARTIAL — D8-C evidence-reproducibility gate only.** Statistical values reproduce from the current archived local bytes, but historical execution-time byte integrity remains unverified; D8-A and D8-B remain PARTIAL and are not promoted.

## Evidence matrix and reconciliation

- Verified distinct method–seed identities: **25/25** (five methods × seeds 42–46; identity checked from manifests and metrics, not directory names alone).
- Source-to-report primary metric values: **100/100 matched** within absolute tolerance 5e-10.
- Original files hashed: **100**; current hashes matched prior D8-A audit fingerprints: **100/100**. No trusted execution-time SHA256 baseline exists.
- Independent statistical outputs agree with the prior D8-C per-seed and summary CSVs: method_summaries.csv 20, paired_seed_differences.csv 20, paired_qahbn2_vs_ahbn_summaries.csv 4 rows.
- Protocol/source checks: all five root commit records and expected image digests match the frozen records; per-run runtime image identifiers and experiment/cleanup status records were checked. No new experiment or live cluster access was performed.

## Five-seed method summaries

Arithmetic mean, sample SD (n−1), and two-sided 95% Student-t confidence intervals (df=4); intervals are unadjusted.

| Method | Metric | Mean | Sample SD | Unadjusted 95% t CI (df=4) |
|---|---|---:|---:|---|
| Gossip | delivery_ratio (proportion) | 0.876779 | 0.012188 | [0.861646, 0.891912] |
| Gossip | propagation_delay (seconds) | 0.089328 | 0.029595 | [0.052581, 0.126074] |
| Gossip | duplicates (count) | 3479.200000 | 1262.506911 | [1911.590621, 5046.809379] |
| Gossip | total_forwards (count) | 3958.400000 | 77.442237 | [3862.242763, 4054.557237] |
| Structured | delivery_ratio (proportion) | 0.081396 | 0.000269 | [0.081062, 0.081729] |
| Structured | propagation_delay (seconds) | 0.003677 | 0.000824 | [0.002654, 0.004700] |
| Structured | duplicates (count) | 0.000000 | 0.000000 | [0.000000, 0.000000] |
| Structured | total_forwards (count) | 152.000000 | 0.000000 | [152.000000, 152.000000] |
| DC-SoC | delivery_ratio (proportion) | 0.407186 | 0.437704 | [-0.136296, 0.950667] |
| DC-SoC | propagation_delay (seconds) | 0.093072 | 0.118831 | [-0.054475, 0.240620] |
| DC-SoC | duplicates (count) | 0.000000 | 0.000000 | [0.000000, 0.000000] |
| DC-SoC | total_forwards (count) | 1710.600000 | 2095.416379 | [-891.203079, 4312.403079] |
| AHBN | delivery_ratio (proportion) | 0.200718 | 0.074113 | [0.108694, 0.292742] |
| AHBN | propagation_delay (seconds) | 0.017040 | 0.009303 | [0.005488, 0.028591] |
| AHBN | duplicates (count) | 341.600000 | 200.342956 | [92.841364, 590.358636] |
| AHBN | total_forwards (count) | 726.000000 | 354.732998 | [285.540807, 1166.459193] |
| Q-AHBN2 | delivery_ratio (proportion) | 0.411666 | 0.182140 | [0.185510, 0.637823] |
| Q-AHBN2 | propagation_delay (seconds) | 0.037168 | 0.018099 | [0.014695, 0.059642] |
| Q-AHBN2 | duplicates (count) | 608.000000 | 274.509563 | [267.151359, 948.848641] |
| Q-AHBN2 | total_forwards (count) | 1738.200000 | 873.423265 | [653.701777, 2822.698223] |

## Prespecified paired Q-AHBN2 − AHBN contrasts

| Metric | Mean Q-AHBN2 − AHBN | Sample SD | Unadjusted 95% paired t CI (df=4) |
|---|---:|---:|---|
| delivery_ratio (proportion) | 0.210948 | 0.149696 | [0.025075, 0.396821] |
| propagation_delay (seconds) | 0.020129 | 0.014211 | [0.002483, 0.037774] |
| duplicates (count) | 266.400000 | 176.105934 | [47.735602, 485.064398] |
| total_forwards (count) | 1012.200000 | 717.532369 | [121.265890, 1903.134110] |

Per-seed values:

| Seed | Metric | AHBN | Q-AHBN2 | Q-AHBN2 − AHBN |
|---:|---|---:|---:|---:|
| 42 | delivery_ratio | 0.132843651626 | 0.336264656616 | 0.20342100499 |
| 43 | delivery_ratio | 0.138912133891 | 0.131171548117 | -0.00774058577406 |
| 44 | delivery_ratio | 0.312067156348 | 0.470169562487 | 0.158102406139 |
| 45 | delivery_ratio | 0.18777475403 | 0.541745134965 | 0.353970380936 |
| 46 | delivery_ratio | 0.231993299832 | 0.578980490875 | 0.346987191042 |
| 42 | propagation_delay | 0.00931108792623 | 0.0284162064393 | 0.0191051185131 |
| 43 | propagation_delay | 0.00929693977038 | 0.0097732792298 | 0.000476339459419 |
| 44 | propagation_delay | 0.0305002123117 | 0.0441956371069 | 0.0136954247952 |
| 45 | propagation_delay | 0.0133910586437 | 0.0494975487391 | 0.0361064900955 |
| 46 | propagation_delay | 0.0226985216141 | 0.0539577732484 | 0.0312592516343 |
| 42 | duplicates | 146 | 403 | 257 |
| 43 | duplicates | 200 | 232 | 32 |
| 44 | duplicates | 531 | 767 | 236 |
| 45 | duplicates | 249 | 776 | 527 |
| 46 | duplicates | 582 | 862 | 280 |
| 42 | total_forwards | 397 | 1380 | 983 |
| 43 | total_forwards | 432 | 391 | -41 |
| 44 | total_forwards | 1257 | 2020 | 763 |
| 45 | total_forwards | 666 | 2362 | 1696 |
| 46 | total_forwards | 878 | 2538 | 1660 |

The mean delivery difference is 21.0948 percentage points. Observed higher mean delivery comes with higher mean propagation delay, duplicates, and total forwards: a delivery-versus-overhead trade-off, not overall superiority. The five-seed sample is small; intervals are unadjusted across endpoints and comparisons.

## Gate and scientific limitations

PARTIAL is recommended because the evidence content and calculations agree, but historical byte integrity cannot be certified without an execution-time hash baseline. This supports reproducibility from the bytes currently archived only; it does not prove those bytes have remained unchanged since execution. D8-A/D8-B limitations, recovery interpretation caveats, and unproven causal mechanisms remain. D8-C does not close the final D8 scientific decision. See `discrepancies.md` for the full register.
