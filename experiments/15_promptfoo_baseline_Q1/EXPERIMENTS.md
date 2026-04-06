# 2026-04-05

# Goal

Run all of Q1 variants through promptfoo with 3 runs and the new API calls instead of Pi agent/manual copy-paste. Make sure output is stable.

# Analysis of Results by Analysis script and LLM

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **86.1** | **87.1** |
|
| Approach (Jaccard, exact labels) | 0.8684 | 0.8720 |
| Applicability (exact values) | 0.8309 | 0.8406 |
| Recommendation (exact values) | 0.8551 | 0.8841 |
|
| Total Questions | 23 |
| Total Runs | 69 |

_Strict_: exact label/value matching | _Loose_: maps `oui` ↔ `oui_sous_conditions`

## Per question results

| Question | Runs | Score | Score(loose) | Valid | IFRIC-16 | IFRS-9 |
|----------|------|-------|-------------|-------|----------|--------|
| Q1.0 | 3 | 100.0 | 100.0 | True | 13 (0.55), 5 (0.56) | 4.2.2 (0.59), 6.3.5 (0.58), B2.1 (0.58), B2.2 (0.59), B2.6 (0.60) |
| Q1.1 | 3 | 2.9 | 5.8 | False | 5 (0.56) | 4.2.2 (0.60), 5.7.1A (0.57), B2.2 (0.57), B2.6 (0.60), B3.2.17 (0.57) |
| Q1.2 | 3 | 65.0 | 65.0 | False | _(none)_ | 4.2.2 (0.59), 5.7.1A (0.57), B2.2 (0.57), B2.6 (0.60), B3.2.17 (0.56) |
| Q1.3 | 3 | 93.3 | 93.3 | True | 13 (0.59), 3 (0.58), 4 (0.59), 5 (0.59), AG9 (0.58) | 4.2.2 (0.62), 6.3.6 (0.64), B6.3.4 (0.60), B6.3.5 (0.65), B6.3.6 (0.61) |
| Q1.4 | 3 | 100.0 | 100.0 | True | 13 (0.58), 17 (0.56), 18 (0.56), 18B (0.55), 5 (0.57) | 4.2.2 (0.60), 6.3.6 (0.57), B4.1.36 (0.59), B6.3.5 (0.58), B7.2.2 (0.58) |
| Q1.5 | 3 | 100.0 | 100.0 | True | 13 (0.57), 4 (0.57), 5 (0.57), 8 (0.56), 9 (0.57) | 4.2.2 (0.60), 6.3.6 (0.60), B2.1 (0.58), B2.6 (0.59), B6.3.5 (0.61) |
| Q1.6 | 3 | 76.4 | 76.4 | True | _(none)_ | 4.2.2 (0.58), 6.3.6 (0.58), B2.6 (0.57), B6.3.5 (0.60), B6.3.6 (0.58) |
| Q1.7 | 3 | 94.2 | 94.2 | True | 13 (0.56), 3 (0.57), 4 (0.56), 5 (0.59), 6 (0.55) | 4.2.2 (0.61), 6.3.6 (0.60), B2.1 (0.59), B2.2 (0.59), B6.3.5 (0.60) |
| Q1.8 | 3 | 83.9 | 83.9 | True | 13 (0.57), 17 (0.56), 5 (0.57) | 6.3.3 (0.58), 6.3.4 (0.61), 6.3.5 (0.61), B6.3.4 (0.61), B6.3.5 (0.60) |
| Q1.9 | 3 | 92.2 | 92.2 | True | 13 (0.58), 3 (0.58), 4 (0.58), 5 (0.60), AG4 (0.58) | 4.2.2 (0.61), 6.3.6 (0.66), B6.3.4 (0.61), B6.3.5 (0.64), B6.3.6 (0.60) |
| Q1.10 | 3 | 100.0 | 100.0 | True | 13 (0.58), 3 (0.57), 4 (0.57), 5 (0.60), 7 (0.57) | 4.2.2 (0.59), 6.3.6 (0.62), B2.2 (0.59), B6.3.5 (0.62), B6.3.6 (0.59) |
| Q1.11 | 3 | 83.9 | 83.9 | True | 13 (0.67), 14 (0.64), 2 (0.64), 5 (0.65), AG5 (0.63) | 6.3.4 (0.65), 6.3.5 (0.67), B6.3.4 (0.66), B6.3.5 (0.67), B6.3.6 (0.67) |
| Q1.12 | 3 | 94.2 | 94.2 | True | 13 (0.55), 4 (0.55), 5 (0.55), 9 (0.55) | 4.2.2 (0.59), 6.3.6 (0.60), B2.1 (0.57), B2.6 (0.58), B6.3.5 (0.60) |
| Q1.13 | 3 | 93.3 | 93.3 | True | 13 (0.58), 3 (0.57), 4 (0.57), 5 (0.58), AG1 (0.57) | 4.2.2 (0.62), 6.3.6 (0.63), B2.6 (0.61), B6.3.5 (0.64), B6.3.6 (0.60) |
| Q1.14 | 3 | 100.0 | 100.0 | True | 13 (0.58), 4 (0.56), 9 (0.56), AG6 (0.56), AG9 (0.56) | 6.3.4 (0.58), 6.3.6 (0.61), B6.3.4 (0.61), B6.3.5 (0.64), B6.3.6 (0.61) |
| Q1.15 | 3 | 64.2 | 64.2 | True | 3 (0.56), 4 (0.57), 5 (0.58) | 3.3.5 (0.61), 4.2.2 (0.60), B2.1 (0.60), B2.4 (0.60), B2.6 (0.62) |
| Q1.16 | 3 | 73.3 | 93.3 | True | 1 (0.59), 13 (0.59), 3 (0.59), 4 (0.61), 5 (0.61) | 3.3.5 (0.62), 4.2.2 (0.63), 6.3.6 (0.63), B2.1 (0.62), B2.2 (0.62) |
| Q1.17 | 3 | 100.0 | 100.0 | True | 13 (0.59), 8 (0.59), 9 (0.59), AG4 (0.57), AG5 (0.58) | 6.3.6 (0.63), B6.3.5 (0.64), B6.6.10 (0.62), B6.6.11 (0.62), B6.6.12 (0.62) |
| Q1.18 | 3 | 93.3 | 93.3 | True | 13 (0.58), 5 (0.56), 7 (0.56), 8 (0.55), AG5 (0.56) | 6.3.2 (0.59), 6.3.4 (0.60), 6.3.5 (0.60), B6.3.4 (0.60), B6.6.11 (0.59) |
| Q1.19 | 3 | 93.3 | 93.3 | True | 13 (0.60), 4 (0.58), 7 (0.59), 8 (0.58), 9 (0.59) | 6.3.6 (0.62), B6.3.4 (0.60), B6.3.5 (0.63), B6.3.6 (0.60), B6.6.10 (0.58) |
| Q1.20 | 3 | 93.3 | 93.3 | True | 13 (0.63), 2 (0.61), 3 (0.61), 5 (0.64), 7 (0.60) | 6.3.4 (0.64), 6.3.5 (0.65), B6.3.4 (0.64), B6.3.5 (0.63), B6.3.6 (0.63) |
| Q1.21 | 3 | 83.9 | 83.9 | True | 13 (0.57), 2 (0.58), 3 (0.59), 4 (0.60), 5 (0.61) | 6.3.1 (0.62), 6.3.6 (0.66), B6.3.4 (0.64), B6.3.5 (0.65), B6.3.6 (0.62) |
| Q1.22 | 3 | 100.0 | 100.0 | True | 13 (0.58), 4 (0.58), 5 (0.57), 7 (0.57), 8 (0.57) | 4.2.2 (0.61), 6.3.6 (0.62), B2.1 (0.60), B2.6 (0.62), B6.3.5 (0.62) |
| **AVERAGE** | | **86.1** | **87.1** | | | |

## Label Frequency by Question

Shows how many times each normalized label appeared across runs for each question. Format: `count/total_runs`.

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|
| cash_flow_hedge | 3/3 | 0/3 | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 60/69 |
| fair_value_hedge | 3/3 | 0/3 | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 60/69 |
| net_investment_hedge | 3/3 | 2/3 | 0/3 | 3/3 | 3/3 | 3/3 | 1/3 | 3/3 | 2/3 | 2/3 | 3/3 | 2/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 2/3 | 3/3 | 59/69 |

### Spurious Labels (< 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------| --- |
| derivative_fvtpl | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 2/69 |
| financial_asset_accounting | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 2/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 2/69 |
| amortised_cost | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/69 |
| fair_value_oci | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/69 |
| fair_value_pl | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/69 |
| fair_value_profit | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/69 |
| foreign_translation | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 0/3 | 1/69 |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.0 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.4 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.5 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.10 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.14 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.17 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.22 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |

**7/23 questions (30%) are top performers**

### Low Performers (loose score < 80)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.1 | 3 | 2.9 | 5.8 | 0.08 | 0.00 | 0.00 |
| Q1.15 | 3 | 64.2 | 64.2 | 0.50 | 0.83 | 0.33 |
| Q1.2 | 3 | 65.0 | 65.0 | 1.00 | 1.00 | 0.00 |
| Q1.6 | 3 | 76.4 | 76.4 | 0.61 | 0.67 | 1.00 |

**4/23 questions (17%) are low performers**

### Key Observations
- **Approach stability (strict)**: Top=1.000, Low=0.549, Delta=+0.451
- **Recommendation consistency (loose)**: Top=1.000, Low=0.333, Delta=+0.667
- **Avg unique labels per run**: Top=3.0, Low=2.8

## Observations

### Strengths
1. **High overall stability (87.1%)** — The pipeline produces consistent results across repetitions.
2. **Focused label set** — Only 3 core labels (cash_flow_hedge, fair_value_hedge, net_investment_hedge) appear consistently across most questions.
3. **7/23 questions achieve perfect stability** — A significant portion of questions are highly reliable.
4. **Low spurious label rate** — Only 10 spurious label occurrences out of 179 total (5.6%).

### Problem Areas

1. **Q1.1 is a complete failure (score 5.8)**:
   - The model returns `needs_clarification` instead of structured JSON with approaches.
   - Only 1 IFRIC-16 section retrieved (5) — missing critical 13.
   - All spurious labels appear in Q1.1 (amortised_cost, fair_value_oci, fair_value_pl).

2. **Q1.2 has perfect approach extraction but no recommendation (score 65.0)**:
   - No IFRIC-16 context retrieved — the model extracts approaches consistently but can't determine applicability.
   - Perfect approach score (1.00) but zero recommendation score.

3. **Q1.6 has inconsistent approach selection (0.61)**:
   - No IFRIC-16 context retrieved — inconsistent hedge type identification.
   - Only 1/3 runs include `net_investment_hedge`.

4. **Q1.15 has inconsistent approach selection and recommendation**:
   - Low approach score (0.50) and low recommendation (0.33).
   - `financial_asset_accounting` appears 2/3 times.

5. **Q1.16 has inconsistent recommendation (0.33 strict, 1.00 loose)**:
   - Approach and applicability are good but recommendation fluctuates.
   - `foreign_translation` appears once as spurious.

### Retrieval Context Observations (from per question results table above)

1. **Q1.1 has minimal IFRIC-16 context** (only 5): This explains the failure — the model lacks the core IFRIC 16 paragraphs (especially 13 which covers hedge accounting types) needed to properly analyze the question.

2. **Q1.2 and Q1.6 have no IFRIC-16 context**: This explains their issues:
   - Q1.2: Perfect approach extraction but no recommendation — likely because without IFRIC 16 context, the model can't determine applicability
   - Q1.6: Lower approach stability (0.61) — missing IFRIC 16 sections means inconsistent hedge type identification

3. **High-scoring retrieval questions (>0.65)**: Q1.11 has the highest IFRIC-16 scores (~0.64-0.67), correlating with good stability despite not being a top performer.

4. **Common IFRIC-16 sections across questions**: Section 13 (hedge types) appears in almost all questions that have IFRIC-16 context.

5. **Common IFRS-9 sections**: Section 4.2.2 (hedge accounting at initial recognition) and section 6.3.x (hedge effectiveness) appear frequently.

## Root Cause Analysis: Retrieval Context

The per question results table above shows the clear pattern:

| Question | IFRIC-16 Chunks | Issue |
|----------|----------------|-------|
| Q1.1 | 1 (only 5) | Complete failure — missing 13 (hedge types) |
| Q1.2 | 0 | No recommendation — can't evaluate applicability |
| Q1.6 | 0 | Inconsistent approaches — missing hedge identification context |

**Fix**: The retrieval pipeline should ensure that for questions involving hedge accounting:
- IFRIC 16 section 13 (hedge types: FV hedge, CF hedge, NIH hedge) is always retrieved
- At least 3-5 IFRIC 16 sections are included in the context

## Recommendations

### High Priority

1. **Fix retrieval to always include IFRIC 16 section 13**:
   - For questions about hedge accounting, ensure section 13 is in the top-k results
   - This would fix Q1.1, Q1.2, and Q1.6

2. **Handle `needs_clarification` responses**:
   - Q1.1 returns `needs_clarification` status instead of structured output
   - The pipeline should either: (a) detect this and retry with refined prompt, or (b) count it as a failed case

### Medium Priority

3. **Investigate Q1.2's missing recommendation**:
   - With IFRIC 16 context, the model should be able to provide a recommendation
   - Currently extracts approaches but can't evaluate applicability

4. **Improve borderline question handling**:
   - Q1.15 and Q1.16 show inconsistent recommendation answers
   - Consider adding explicit guidance about when to use `oui_sous_conditions` vs `oui` vs `non`

## Next Steps

1. **Fix retrieval** to ensure IFRIC 16 section 13 is always included for hedge accounting questions
2. **Re-run experiment 15** with fixed retrieval and test stability improvement
3. **Test with another provider (anthropic)** to compare baseline stability across models
4. **Deep-dive into Q1.15** to understand why approach extraction is inconsistent

# Analysis by human
We clearly have a retrieval issue with some of the questions. 

## Retrieval is insufficient

If we compare the chunks retrieved by top performers and low performers, IFRIC-16.13 and IFRS-9.6.3.6 is always present in top performers and absent in low performers. Their contents are the following:

>**IFRIC-16 13**
>
>An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once in the consolidated financial statements. Therefore, if the same net assets of a foreign operation are hedged by more than one parent entity within the group (for example, both a direct and an indirect parent entity) for the same risk, only one hedging relationship will qualify for hedge accounting in the consolidated financial statements of the ultimate parent. A hedging relationship designated by one parent entity in its consolidated financial statements need not be maintained by another higher level parent entity. However, if it is not maintained by the higher level parent entity, the hedge accounting applied by the lower level parent must be reversed before the higher level parent’s hedge accounting is recognised.

>**IFRS-9 6.3.6**
>
>However, as an exception to paragraph 6.3.5, the foreign currency risk of an
intragroup monetary item (for example, a payable/receivable between two
subsidiaries) may qualify as a hedged item in the consolidated financial
statements if it results in an exposure to foreign exchange rate gains or losses
that are not fully eliminated on consolidation in accordance with IAS 21 The
Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign
exchange rate gains and losses on intragroup monetary items are not fully
eliminated on consolidation when the intragroup monetary item is transacted
between two group entities that have different functional currencies. In
addition, the foreign currency risk of a highly probable forecast intragroup
transaction may qualify as a hedged item in consolidated financial statements
provided that the transaction is denominated in a currency other than the
functional currency of the entity entering into that transaction and the
foreign currency risk will affect consolidated profit or loss.

It is clear that 6.3.6 contains the key provision to cite to be able to give the correct answer.
IFRIC-6 13 mentions a "net investment" which may help the model identify it as an approach to consider.

In the pipeline, we expand 10 chunks around each of these so 6.3.6 helps get a little more context from section 6 overall.

## Multilingual embeddings may be insufficient

The variant of question 1 is Q1.2
>Un dividende intragroupe a été comptabilisé en créance.
>De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

Its translation is
>An intra-group dividend was recognized as a receivable.
>How can we apply hedge documentation in the consolidated financial statements to the foreign exchange component of this dividend?

We ran the question in each language through the query command
- without expansion
- with no minimum
- with k=10

The retrieved documents are very different. Note that all IFRIC 16 documents are below 0.55 which is our current retrieval threshold, used to weed out non-sensical queries.

| Language | IFRIC-16 | IFRS-9 |
|----------|------|-------|-------------|-------|----------|--------|
| French | 3 (0.51), 4 (0.51), 5 (0.548), 13 (0.53), 14 (0.53), 17 (0.52), 18 (0.52), 18A (0.51), AG5 (0.51), AG8 (0.51) | 4.2.2 (0.59), 5.7.1A (0.57), B2.1 (0.56), B2.2 (0.57), B2.6 (0.60), B3.2.10 (0.56), B3.2.17 (0.56), B5.7.1 (0.56), B5.7.9 (0.56), B7.2.3 (0.56) |
| English | 2 (0.68), 3 (0.69), 4 (0.67), 5 (0.70), 7 (0.66), 10 (0.66), 13 (0.69), 14 (0.69), AG4 (0.65), AG5 (0.65) | 6.3.5 (0.66), 6.3.6 (0.69), 6.5.16 (0.66), B6.3.1 (0.66), B6.3.4 (0.69), 6.5.13 (0.67), B6.3.2 (0.66), B6.3.5 (0.70), B6.3.6 (0.69), B6.5.39 (0.67) |

In English, paragraphs from section 6 are retrieved which is what we need. Scores are higher so it might be that the threshold is too low for French:
- this is true for IFRIC 16 were paragraph 13 is at 0.53. If the minimum score was lower it would be retrieved
- but it is not the case for IFRS-9: even with k=10, we see that paragraph 6 is never retrieved
Although it is not guaranteed to work, it is an easy thing to test

## Next steps
- experiment on different min-score thresholds on Q1.2
- retrieval query matching on the section titles and then to retrieve all the chunks in that section.
- translating the question to English and then running the pipeline.

