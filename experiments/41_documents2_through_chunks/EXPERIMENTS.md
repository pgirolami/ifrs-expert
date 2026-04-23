# Experiment 41 — `documents2-through-chunks`

## Goal

Check whether the new chunk-first routing mode, `retrieval.mode: documents2-through-chunks`, can retrieve **IFRIC 16**, **IAS 39**, and **IFRS 9** consistently across Q1.

A secondary question was whether English glossary enrichment still helps once routing changes.

## Setup

I ran two comparison batches with the Q1 / Q1en question sets using the experiment 40 comparison script pattern, but with policies derived from the current [`config/policy.default.yaml`](../../config/policy.default.yaml).

Outputs are separated by batch:

- [`current_routing/`](./current_routing)
- [`old_routing/`](./old_routing)

### Batch 1 — current routing

This batch uses the current default policy for both French runs:

- `fr_raw`: current default policy with `query_embedding_mode: raw`
- `fr_enriched`: current default policy with `query_embedding_mode: enriched`
- `en_control`: current default policy with `query_embedding_mode: raw`

Outputs:

- [`current_routing/q1-target-retrieval__documents2-through-chunks__fr-raw-target-matrix.md`](./current_routing/q1-target-retrieval__documents2-through-chunks__fr-raw-target-matrix.md)
- [`current_routing/q1-target-retrieval__documents2-through-chunks__fr-enriched-target-matrix.md`](./current_routing/q1-target-retrieval__documents2-through-chunks__fr-enriched-target-matrix.md)
- [`current_routing/q1-target-retrieval__documents2-through-chunks__en-control-target-matrix.md`](./current_routing/q1-target-retrieval__documents2-through-chunks__en-control-target-matrix.md)
- [`current_routing/q1-target-retrieval__documents2-through-chunks__merged-delta-report.md`](./current_routing/q1-target-retrieval__documents2-through-chunks__merged-delta-report.md)
- [`current_routing/q1-target-retrieval__documents2-through-chunks__summary.md`](./current_routing/q1-target-retrieval__documents2-through-chunks__summary.md)

### Batch 2 — old routing baseline

This batch compares the old `documents2` routing against the new chunk-first routing while keeping the query embedding mode enriched for the French arms:

- `fr_raw`: [`experiments/41_documents2_through_chunks/old_routing/policy.documents2-enriched.yaml`](./old_routing/policy.documents2-enriched.yaml) — old `documents2` routing with enriched query embeddings
- `fr_enriched`: current default policy with `query_embedding_mode: enriched` — `documents2-through-chunks`
- `en_control`: current default policy with `query_embedding_mode: raw` — required by the comparison script as a reference arm

Outputs:

- [`old_routing/q1-target-retrieval__documents2-baseline__fr-raw-target-matrix.md`](./old_routing/q1-target-retrieval__documents2-baseline__fr-raw-target-matrix.md)
- [`old_routing/q1-target-retrieval__documents2-baseline__fr-enriched-target-matrix.md`](./old_routing/q1-target-retrieval__documents2-baseline__fr-enriched-target-matrix.md)
- [`old_routing/q1-target-retrieval__documents2-baseline__en-control-target-matrix.md`](./old_routing/q1-target-retrieval__documents2-baseline__en-control-target-matrix.md)
- [`old_routing/q1-target-retrieval__documents2-baseline__merged-delta-report.md`](./old_routing/q1-target-retrieval__documents2-baseline__merged-delta-report.md)
- [`old_routing/q1-target-retrieval__documents2-baseline__summary.md`](./old_routing/q1-target-retrieval__documents2-baseline__summary.md)

## Results

### English enrichment is still very useful under the new routing

Under `documents2-through-chunks`, the enriched French run is clearly better than raw French on all three targets.

#### IFRIC 16

| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| fr_raw | 20/23 | 0/23 | 0/23 | 1/23 | 14.50 |
| fr_enriched | 23/23 | 0/23 | 3/23 | 21/23 | 4.48 |

#### IAS 39

| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| fr_raw | 23/23 | 0/23 | 7/23 | 13/23 | 5.57 |
| fr_enriched | 23/23 | 7/23 | 22/23 | 23/23 | 2.13 |

#### IFRS 9

| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| fr_raw | 17/23 | 0/23 | 0/23 | 3/23 | 11.65 |
| fr_enriched | 23/23 | 3/23 | 20/23 | 23/23 | 2.43 |

So the glossary expansion still matters a lot, especially for IFRS 9 coverage and rank quality.

### New routing vs old routing

Comparing the enriched French arms in the two batches:

| Target | New routing `documents2-through-chunks` | Old routing `documents2` |
| --- | ---: | ---: |
| IFRIC 16 retrieved | 23/23 | 23/23 |
| IFRIC 16 top 1 | 0/23 | 23/23 |
| IFRIC 16 mean rank | 4.48 | 1.00 |
| IAS 39 retrieved | 23/23 | 23/23 |
| IAS 39 top 1 | 7/23 | 0/23 |
| IAS 39 mean rank | 2.13 | 5.57 |
| IFRS 9 retrieved | 23/23 | 17/23 |
| IFRS 9 top 1 | 3/23 | 0/23 |
| IFRS 9 mean rank | 2.43 | 11.65 |

### Interpretation

- **IFRIC 16**: the old routing is stronger on top-1 dominance, but the new routing still retrieves it on every Q1 variant and keeps it in the top 5 on 21/23.
- **IAS 39**: the new routing is materially better. It lifts IAS 39 to the top more often and improves the mean rank substantially.
- **IFRS 9**: the new routing is much better. The old routing misses it on 6 variants; the new routing retrieves it on all 23.

## Conclusion

`documents2-through-chunks` does achieve the main goal: it retrieves **IFRIC 16**, **IAS 39**, and **IFRS 9** consistently across Q1 when paired with enriched query embeddings.

Compared with the old `documents2` routing, the new chunk-first routing is the better overall fit for this trio because it substantially improves **IAS 39** and **IFRS 9** coverage and ranking, even though it gives up the old routing's perfect top-1 behavior for **IFRIC 16**.

So the answer is: **yes, the new routing works better overall for this experiment's objective**.
