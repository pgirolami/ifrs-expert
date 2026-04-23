# Experiment 42: Q1 target recall with minimal document fan-out

## Goal

Find a retrieval policy for the full Q1 variant set (`Q1.0` … `Q1.22`) that always retrieves:

- `ias39`
- `ifrs9`
- `ifric16`

while keeping the number of retrieved documents as low as possible.

This used the same retrieval entry point as prior Q1 experiments:

```bash
uv run python -m src.cli retrieve --policy-config <policy> --json
```

## Setup

- Question set: `experiments/00_QUESTIONS/Q1` (23 variants)
- Search target: document hits for the three target docs above
- Analysis helper: `experiments/analysis/run_q1_target_recall_summary.py`
- Policies evaluated:
  - `policies/policy.baseline.yaml`
  - `policies/policy.optimal.yaml`
- k sweep checked separately: `1`, `2`, `5`, `10`

## Baseline

The baseline was the original default policy at the start of experiment 42.

Key settings:

- `global_d: 25`
- `IFRS-S`: `d: 10`, `min_score: 0.55`
- `IAS-S`: `d: 10`, `min_score: 0.53`
- `IFRIC`: `d: 10`, `min_score: 0.53`
- all other document types used the same broad thresholds as the default policy

## Optimal found

The best configuration found was:

```yaml
retrieval:
  mode: documents2-through-chunks
  query_embedding_mode: enriched
  k: 5
  documents:
    global_d: 5
    by_document_type:
      IFRS-S:
        d: 1
        min_score: 0.683
      IAS-S:
        d: 2
        min_score: 0.699
      IFRIC:
        d: 1
        min_score: 0.671
      # all other document types: kept out of the way
      # with min_score ~= 0.8
```

Notes:

- `similarity_representation` was not tuned here because `documents2-through-chunks` does not use it.
- The `k` sweep (`1`, `2`, `5`, `10`) did not change the top retrieved standard-doc ordering for this Q1 sweep, so `k=5` was retained.
- Non-target standard families were pruned with a high `min_score` (0.8) so they do not compete with the three target standards.
- The target-family thresholds above were chosen just below the lowest observed target scores, leaving a small amount of slack.
- `global_d: 5` leaves one extra slot beyond the observed maximum of 4 retrieved docs.

## Results

### Baseline

- All 3 targets present together: **23 / 23**
- Per-target presence:
  - `ias39`: **23 / 23**
  - `ifrs9`: **23 / 23**
  - `ifric16`: **23 / 23**
- Average document hits: **25.00**
- Max document hits: **25**

### Optimal

- All 3 targets present together: **23 / 23**
- Per-target presence:
  - `ias39`: **23 / 23**
  - `ifrs9`: **23 / 23**
  - `ifric16`: **23 / 23**
- Average document hits: **3.57**
- Max document hits: **4**

Target rank summary in the optimal run:

- `ias39`: mean rank **1.61**, max rank **2**
- `ifrs9`: mean rank **1.78**, max rank **4**
- `ifric16`: mean rank **3.13**, max rank **4**

## Takeaways

1. The Q1 target family can be made extremely compact once the policy is tightened to the three target document families.
2. The large fan-out from experiment 38 was not necessary for this target set.
3. The final policy keeps a small buffer while dropping the average retrieved document count from **25.00** to **3.57**.

## Conclusion

For this experiment’s objective, a standards-only-through-chunks mechanism is sufficient: it retrieves `ias39`, `ifrs9`, and `ifric16` in **23/23** Q1 variants with very low fan-out. That does not prove support documents are useless in general, but they are not needed for this target set.

## Why this is the best operating point

- It achieves the goal exactly: all 3 target standards are retrieved in **23/23** Q1 variants.
- It minimizes fan-out: average retrieved docs is **3.57**, max is **4**.
- It keeps a small safety buffer: `global_d=5` leaves one slot above the observed maximum.
- The target-family `min_score` values sit just below the lowest observed target scores, so there is a little leg room.
- `k` did not change the retrieved standard ordering in the Q1 sweep, so `k=5` is a stable choice.
- `similarity_representation` was not part of the search space here because `documents2-through-chunks` collapses retrieval through chunks.

## Artifacts

- Baseline policy: [`policies/policy.baseline.yaml`](./policies/policy.baseline.yaml)
- Optimal policy: [`policies/policy.optimal.yaml`](./policies/policy.optimal.yaml)
- Baseline run summary: [`runs/baseline/summary.json`](./runs/baseline/summary.json)
- Optimal run summary: [`runs/optimal/summary.json`](./runs/optimal/summary.json)
- Baseline markdown summary: [`runs/baseline/summary.md`](./runs/baseline/summary.md)
- Optimal markdown summary: [`runs/optimal/summary.md`](./runs/optimal/summary.md)
- Reusable evaluator: [`../analysis/run_q1_target_recall_summary.py`](../analysis/run_q1_target_recall_summary.py)
