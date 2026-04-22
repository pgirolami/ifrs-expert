# Experiment 40 — Compare Q1 retrieval modes

## Goal

Experiment 39 showed that retrieval was good in English but not in French. We identified 3 next steps, this is the first one.

In this experiment, we compare three retrieval settings on aligned Q1/Q1en-style evaluation data:

1. **fr_raw** — original French only using `Q1`
2. **fr_enriched** — French plus English normalized glossary terms using `Q1`. The [glossary](../../config/en-fr-glossary.yaml) was created using the 23 questions in French and ChatGPT and then reviewed by the SME.
3. **en_control** — English translation only using `Q1en`

The purpose is to isolate the effect of query enrichment on the real French setting while keeping an English-only control as an upper-bound reference.

## Fixed conditions

All three runs keep the same:
- corpus
- retrieval mode and thresholds
- document routing settings
- expansion settings
- output formatting

Only these things change:
- question family: `Q1` vs `Q1en`
- `retrieval.query_embedding_mode`: `raw` vs `enriched`

## Policies

- `policy.raw.yaml`
- `policy.enriched.yaml`

Both are copies of the current retrieval defaults, differing only in:

```yaml
retrieval:
  query_embedding_mode: raw | enriched
```

## Outputs

Running `./run.sh` generates:

- `generated_fr_raw_target_matrix.md`
- `generated_fr_enriched_target_matrix.md`
- `generated_en_control_target_matrix.md`
- `generated_merged_delta_report.md`
- `generated_merged_delta_report.json`
- `generated_summary.md`
- `generated_summary.json`

## Aggregate results

The summary artifact tracks `IFRIC 16`, `IAS 39`, and `IFRS 9`.

### IFRIC 16

| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank | Mean score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| fr_raw | 18/23 (78.3%) | 2/23 (8.7%) | 2/23 (8.7%) | 4/23 (17.4%) | 11.61 | 0.56 |
| fr_enriched | 23/23 (100.0%) | 16/23 (69.6%) | 20/23 (87.0%) | 20/23 (87.0%) | 2.13 | 0.61 |
| en_control | 23/23 (100.0%) | 23/23 (100.0%) | 23/23 (100.0%) | 23/23 (100.0%) | 1.00 | 0.68 |

`fr_enriched` closes most of the gap to the English control on IFRIC 16. Relative to `fr_raw`, it improves both coverage and rank dramatically:
- retrieval coverage: `18/23 -> 23/23`
- top-1 frequency: `2/23 -> 16/23`
- mean rank: `11.61 -> 2.13`

### IAS 39

| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank | Mean score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| fr_raw | 10/23 (43.5%) | 0/23 (0.0%) | 0/23 (0.0%) | 2/23 (8.7%) | 15.20 | 0.56 |
| fr_enriched | 21/23 (91.3%) | 2/23 (8.7%) | 10/23 (43.5%) | 16/23 (69.6%) | 4.48 | 0.59 |
| en_control | 23/23 (100.0%) | 0/23 (0.0%) | 15/23 (65.2%) | 20/23 (87.0%) | 3.35 | 0.60 |

IAS 39 is the other major beneficiary of enrichment. Relative to `fr_raw`:
- retrieval coverage more than doubles: `10/23 -> 21/23`
- top-3 frequency improves from `0/23` to `10/23`
- mean rank improves from `15.20` to `4.48`

This is still not as strong as the English control, but the French enriched run is much closer to it than the raw French run.

### IFRS 9

| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank | Mean score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| fr_raw | 20/23 (87.0%) | 1/23 (4.3%) | 4/23 (17.4%) | 6/23 (26.1%) | 7.20 | 0.58 |
| fr_enriched | 19/23 (82.6%) | 0/23 (0.0%) | 3/23 (13.0%) | 8/23 (34.8%) | 10.37 | 0.58 |
| en_control | 23/23 (100.0%) | 0/23 (0.0%) | 15/23 (65.2%) | 22/23 (95.7%) | 3.17 | 0.60 |

Unlike IFRIC 16 and IAS 39, IFRS 9 becomes slightly worse under enrichment:
- retrieval coverage: `20/23 -> 19/23`
- top-3 frequency: `4/23 -> 3/23`
- mean rank: `7.20 -> 10.37`

Top-5 frequency improves slightly (`6/23 -> 8/23`), but the overall ranking quality declines.

## Per-question behavior

The merged delta report shows that the enriched run often shifts the same question toward `IFRIC 16` and `IAS 39`, while `IFRS 9` moves down.

Examples from the report:

- **Q1.0**
  - IFRIC 16: `fr_raw` absent → `fr_enriched` rank `1`
  - IAS 39: rank `24` → rank `5`
  - IFRS 9: rank `1` → rank `17`

- **Q1.1**
  - IFRIC 16: `fr_raw` absent → `fr_enriched` rank `1`
  - IAS 39: rank `19` → rank `2`
  - IFRS 9: rank `3` → rank `21`

- **Q1.2**
  - IFRIC 16: `fr_raw` absent → `fr_enriched` rank `1`
  - IAS 39: `fr_raw` absent → `fr_enriched` rank `4`
  - IFRS 9: rank `4` → rank `18`

- **Q1.3**
  - IFRIC 16: rank `10` → rank `2`
  - IAS 39: rank `15` → rank `1`
  - IFRS 9: rank `7` → rank `9`

- **Q1.4**
  - IFRIC 16: rank `19` → rank `1`
  - IAS 39: `fr_raw` absent → rank `2`
  - IFRS 9: rank `10` → rank `4`

These examples are representative of the broader pattern in the merged report:
- `IFRIC 16` becomes much more consistently visible and often moves to the very top
- `IAS 39` moves from rare/late retrieval to frequent early retrieval
- `IFRS 9` is often displaced downward when enrichment is enabled

## Run-level comparison

### fr_raw

The raw French run keeps better balance for IFRS 9 than the enriched French run, but it under-retrieves the other two target authorities:
- `IFRIC 16` is missing on 5 variants and usually ranked late when retrieved
- `IAS 39` is missing on 13 variants and almost never appears near the top
- `IFRS 9` is retrieved on most variants, but often not prominently

### fr_enriched

The enriched French run substantially changes the retrieval profile:
- `IFRIC 16` becomes universal and frequently top-ranked
- `IAS 39` becomes near-universal and often enters the top 5
- `IFRS 9` remains present on many variants, but tends to rank lower than in the raw French run

So the enrichment does not simply raise all three target documents together; it redistributes rank mass in favor of `IFRIC 16` and `IAS 39`.

### en_control

The English control remains clearly strongest overall:
- all three target documents are retrieved on all 23 variants
- `IFRIC 16` is top-1 on all 23 variants
- `IAS 39` and `IFRS 9` are both top-3 on 15/23 variants
- `IFRS 9` mean rank is `3.17`, much better than either French run

This confirms that the document representations and routing setup are capable of retrieving the intended authority set when the query phrasing is close to the document language.

## Diagnostic pass on degraded IFRS 9 cases

To understand the IFRS 9 regression, I reviewed the merged delta report and isolated variants where:
- `fr_raw` retrieved IFRS 9 but `fr_enriched` lost it entirely
- or IFRS 9 rank became materially worse

For this diagnostic pass, a **material drop** means IFRS 9 moved down by at least 5 rank positions, or disappeared entirely.

### Bad IFRS 9 cases

Using that rule, there are **9 degraded IFRS 9 cases**:
- rank drop but still retrieved: `Q1.0`, `Q1.1`, `Q1.2`, `Q1.6`, `Q1.9`, `Q1.13`
- lost entirely: `Q1.12`, `Q1.17`, `Q1.22`

The raw/enriched IFRS 9 ranks are:

| Question | fr_raw IFRS 9 rank | fr_enriched IFRS 9 rank |
| --- | ---: | ---: |
| Q1.0 | 1 | 17 |
| Q1.1 | 3 | 21 |
| Q1.2 | 4 | 18 |
| Q1.6 | 8 | 18 |
| Q1.9 | 8 | 19 |
| Q1.12 | 4 | absent |
| Q1.13 | 8 | 15 |
| Q1.17 | 12 | absent |
| Q1.22 | 7 | absent |

### Bucket 1 — coherent substitution toward IFRIC 16 / IAS 39

In **7 of the 9 degraded cases**, the enriched run moved strongly toward the two target authorities that improved globally:
- `IFRIC 16` moved into the **top 3 in 7/9** cases, and to **rank 1 in 6/9** cases
- `IAS 39` moved into the **top 5 in 7/9** cases, and into the **top 3 in 4/9** cases
- both `IFRIC 16` and `IAS 39` were simultaneously in the enriched top 5 in **7/9** cases

Representative examples:

- **Q1.1**
  - IFRS 9: `3 -> 21`
  - IFRIC 16: `absent -> 1`
  - IAS 39: `19 -> 2`
  - top enriched hits begin with `IFRIC 16`, `IAS 39`, then `IFRS 19`

- **Q1.6**
  - IFRS 9: `8 -> 18`
  - IFRIC 16: `absent -> 2`
  - IAS 39: `absent -> 1`
  - top enriched hits begin with `IAS 39`, `IFRIC 16`, then a NAVIS document

- **Q1.9**
  - IFRS 9: `8 -> 19`
  - IFRIC 16: `11 -> 1`
  - IAS 39: `9 -> 2`
  - this is the clearest case of the enriched run reordering the same question toward the two target authorities while pushing IFRS 9 down

- **Q1.17**
  - IFRS 9: `12 -> absent`
  - IFRIC 16: `10 -> 1`
  - IAS 39: `absent -> 3`
  - the disappearance of IFRS 9 is still paired with stronger ranking for the two other target authorities

Even when the substitution is not the exact `IFRIC 16 rank 1 / IAS 39 rank 2` pattern, the enriched run usually shifts toward those two authorities first, with IFRS 9 displaced afterward.

### Bucket 2 — mixed or noisier substitution

There are **2 clear outliers** where IFRS 9 is lost but the enriched top ranks are not mainly captured by `IFRIC 16` and `IAS 39`:

- **Q1.12**
  - IFRS 9: `4 -> absent`
  - enriched top hits are: NAVIS, NAVIS, `IAS 33`, `IFRIC 17`, `IFRIC 5`
  - `IAS 39` is only rank 6 and `IFRIC 16` rank 7

- **Q1.22**
  - IFRS 9: `7 -> absent`
  - enriched top hits are: `IFRS 19`, NAVIS, `IFRS 17`, `IFRS 12`, `IFRIC 23`
  - `IFRIC 16` only reaches rank 8 and `IAS 39` disappears completely

These two variants look less like a clean substitution toward the intended authoritative set and more like broader drift.

### What replaced IFRS 9 most often?

Across the 9 degraded cases, the enriched top positions are not random, but they are also not limited to `IFRIC 16` and `IAS 39`.

Most frequent documents in the enriched top 5 of the degraded cases are:
- NAVIS `QRIFRS C 2DB 864AD 71978 EFL`: **8** times
- `IFRIC 16`: **7** times
- `IAS 39`: **7** times
- `IFRS 19`: **5** times
- `IFRS 8`: **3** times
- `IAS 33`: **3** times

So the dominant pattern is not generic noise alone. The enriched run often replaces IFRS 9 with:
- `IFRIC 16`
- `IAS 39`
- sometimes a NAVIS document and secondary standards or interpretations

### Result of the diagnostic

The degraded IFRS 9 cases are **mostly** consistent with a narrower but still semantically coherent shift, rather than a pure collapse into unrelated noise.

In most of the bad IFRS 9 variants, the enrichment improves exactly the two authorities that improved in the global summary:
- `IFRIC 16`
- `IAS 39`

The main counterexamples are `Q1.12` and `Q1.22`, where the enriched run loses IFRS 9 without a correspondingly strong takeover by those two authorities.

## Additional run with issue-defining glossary only

### What we did

After identifying that some glossary entries were probably not issue-defining in the IFRS sense, I ran the Q1 target-matrix experiment again using the reduced glossary:
- source glossary: `@config/en-fr-glossary_issues.yaml`
- question family: `Q1`
- retrieval policy: enriched mode (`policy.enriched.yaml`)

The resulting artifact is:
- [generated_fr_enriched_issues_target_matrix.md](./generated_fr_enriched_issues_target_matrix.md)

### What we ran

This was the same target-matrix generation flow as before, but with the active glossary content taken from `en-fr-glossary_issues.yaml` instead of the broader enriched glossary.

### Result

From the totals row of `generated_fr_enriched_issues_target_matrix.md`:
- `IAS 39` is retrieved on **20/23** variants
- `IFRIC 16` is retrieved on **22/23** variants
- `IFRS 9` is retrieved on **19/23** variants

Compared with the broader enriched run (`generated_fr_enriched_target_matrix.md`), this means:
- `IAS 39`: **21/23 -> 20/23**
- `IFRIC 16`: **23/23 -> 22/23**
- `IFRS 9`: **19/23 -> 19/23**

### Conclusion

Using only the reduced issue-defining glossary does **not** recover IFRS 9 coverage relative to the broader enriched run, and it slightly weakens the gains previously observed on IAS 39 and IFRIC 16.

So, based on this target-matrix rerun alone, the narrower glossary does not improve the overall trade-off: it preserves the IFRS 9 coverage issue while giving back a small part of the improvement on the other two target authorities.

## Similarity scores for IFRIC / IFRS / IAS variants

In order to dig deeper into what is happening we created a matrix to compare the scores with and without enrichment. See the [Variant similarity matrix](./variant_similarity_table.md) for reference.

Only the following questions were evaluated Q1.1, Q1.6, Q1.9, Q1.11, Q1.14, Q1.18 and they were chosen because they exhibited poor performance on IFRS 9 but different alternative documents retrieved.

The table contains a lot of detailed information and some alternative scoring.

Here are some elements that stand out when looking at retrieval using the current policy file and comparing "raw" questions to "enriched" questions:
- Q1.1, Q1.6, Q1.9
  - IFRIC 16 and IAS 39 are the scores that increased the most on this question (+46% & +28%) and they are the top 2 retrieved results.
  - IFRS 9 is the document whose score decreased the most !
  -
- Q1.11
  - IAS 39 is the scores that increased the most on this question (+24%) and is the top 2 retrieved results.
  - IFRS 9 is the document whose score decreased the most !
- Q1.14
  - The increases on the question much more muted (<11%)
  - IAS 39 is the second highest increase
  - IFRIC 16 decreased but not enough to be a bottom 5
  - IFRS 9 was not even retrieved (both in raw and enriched)
- Q1.18
  - The increases on the question much more muted (<20%)
  - IFRIC 16 and IAS 39 are the scores that increased the most on this question (+46% & +28%) and they are the top 2 retrieved results.

  This document is titled "The Effects of Changes in Foreign Exchange Rates" so it is relevant to a question mentioning foreign exchange rates.

  The working hypothesis is here again that the enrichment is overweighing "foreign xxx risk" and "FX risk"
- IAS 39 increases very significantly from 0.4799 to 0.6173 (+0.14 = +28%), with the standard variant becoming the winning score for the family.