# Experiment 43 — `standards_only_through_chunks__enriched`

## Goal

Verify that the assembled retrieval policy `standards_only_through_chunks__enriched` retrieves all three target standards on the full Q1 variant set:

- `IAS 39`
- `IFRIC 16`
- `IFRS 9`

This experiment exercises the post-cleanup retrieval policy catalog in `config/policy.default.yaml` and uses the new retrieval-policy selection path.

## Setup

- Question set: `experiments/00_QUESTIONS/Q1` (`Q1.0` … `Q1.22`)
- Policy config: [`config/policy.default.yaml`](../../config/policy.default.yaml)
- Retrieval policy: `standards_only_through_chunks__enriched`
- Analysis helper: [`../analysis/run_q1_retrieve_target_matrix.py`](../analysis/run_q1_retrieve_target_matrix.py)
- Summary helper: [`../analysis/run_q1_target_recall_summary.py`](../analysis/run_q1_target_recall_summary.py)

## Results

The run retrieved all three target standards in **23 / 23** Q1 variants.

### Target coverage

| Target | Present | Mean rank | Max rank |
| --- | ---: | ---: | ---: |
| IAS 39 | 23 / 23 | 1.61 | 2 |
| IFRIC 16 | 23 / 23 | 3.39 | 5 |
| IFRS 9 | 23 / 23 | 1.83 | 4 |

### Fan-out

- Average document hits per question: **5.00**
- Max document hits per question: **5**

### Comparison with experiment 42

Experiment 42 found a more compact Q1 policy that also retrieved all three targets in **23 / 23** variants:

- Experiment 42 average document hits: **3.57**
- Experiment 42 max document hits: **4**
- Experiment 42 target presence:
  - `ias39`: **23 / 23**
  - `ifrs9`: **23 / 23**
  - `ifric16`: **23 / 23**

So this experiment shows **no recall regression** versus experiment 42. The apparent fan-out regression is due to the fact that we increased the number of documents retrieved in the document-routing phase (from 1 to 2).

### Interpretation

- The policy satisfies the main retrieval requirement exactly: all three target standards are always present.
- IAS 39 and IFRS 9 are very stable at the top of the result set.
- IFRIC 16 is still consistently retrieved, but it tends to sit lower than the other two targets and occasionally falls to rank 5.
- Compared with experiment 42, recall is unchanged but the policy is less compact.
- The policy is reliable for recall, but it does not reduce fan-out below five documents per question in this Q1 sweep.

## Artifacts

- Single-run matrix: [`q1-target-retrieval__documents2-through-chunks__single-run.md`](./q1-target-retrieval__documents2-through-chunks__single-run.md)
- Summary markdown: [`runs/summary/summary.md`](./runs/summary/summary.md)
- Summary JSON: [`runs/summary/summary.json`](./runs/summary/summary.json)
- Run script: [`run.sh`](./run.sh)
