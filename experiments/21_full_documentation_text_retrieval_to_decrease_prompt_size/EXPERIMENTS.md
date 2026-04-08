# 2026-04-07

# Goal

Test whether using the full IFRS free documentation text (instead of just IFRIC 16, IFRS 9 and a few more) with `k=5` retrieval can decrease prompt size while maintaining or improving stability scores. Compare against experiment 17 (`17_promptfoo_baseline_codex_k=10_Q1`) which used excerpted chunks.

## Method

Analysis was produced with the existing scripts under `experiments/analysis/`:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'e=5__k=5__llm_provider=openai-codex__min-score=0.5__retrieval-mode=text' \
  --experiment 21_full_documentation_text_retrieval_to_decrease_prompt_size
```

**Note:** This experiment uses a **larger corpus** (all available free IFRS documents) compared to experiment 17 (targeted documents). The larger corpus means more candidate documents for retrieval, which can lead to more irrelevant context being included.

---

## Automated analysis of Experiment 21

### Aggregate Metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **68.3** | **68.3** |
|
| Approach (Jaccard, exact labels) | 0.6333 | 0.6333 |
| Applicability (exact values) | 0.5185 | 0.5185 |
| Recommendation (exact values) | 0.7778 | 0.7778 |
|
| Total Questions | 3 |
| Total Runs | 9 |
|
| Structural validity | 3/3 questions | |

_Strict_: exact label/value matching  
_Loose_: maps `oui` ↔ `oui_sous_conditions`

### Per-question results

| Question | Runs | Score | Score(loose) | Valid |
|----------|------|-------|--------------|-------|
| Q1.0 | 3 | 35.3 | 35.3 | True |
| Q1.1 | 3 | 86.7 | 86.7 | True |
| Q1.2 | 3 | 82.8 | 82.8 | True |
| **AVERAGE** | | **68.3** | **68.3** | |

### Detailed breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
| --- | --- | --- | --- | --- | --- | --- |
| Q1.0 | 0.2000 | 0.2000 | 0.2222 | 0.2222 | 0.3333 | 0.3333 |
| Q1.1 | 1.0000 | 1.0000 | 0.5556 | 0.5556 | 1.0000 | 1.0000 |
| Q1.2 | 0.7000 | 0.7000 | 0.7778 | 0.7778 | 1.0000 | 1.0000 |

### LABEL FREQUENCY BY QUESTION

#### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Total |
|---|---|---|---|---|
| cash_flow_hedge | 2 | 3 | 3 | 8 |
| fair_value_hedge | 2 | 3 | 3 | 8 |
| net_investment_hedge | 2 | 3 | 3 | 8 |

#### Spurious Labels (< 10% of runs)

| Label | Total | Q1.0 | Q1.1 | Q1.2 |
|---|---|---|---|---|
| foreign_currency_accounting | 1 | 1 | 0 | 0 |
| foreign_currency_translation | 1 | 1 | 0 | 0 |
| foreign_exchange_accounting | 1 | 0 | 0 | 1 |
| ias21_fx_accounting | 1 | 1 | 0 | 0 |
| ias39_hedge_accounting | 1 | 1 | 0 | 0 |
| ifrs9_hedge_accounting | 1 | 1 | 0 | 0 |
| no_hedge_accounting | 1 | 0 | 0 | 1 |

### Label behavior

Experiment 21 shows significant label instability compared to experiment 17:

| Label | Experiment 17 | Experiment 21 |
|-------|---------------|---------------|
| `fair_value_hedge` | 69/69 runs | 8/9 runs |
| `cash_flow_hedge` | 69/69 runs | 8/9 runs |
| `net_investment_hedge` | 66/69 runs | 8/9 runs |
| Spurious label mentions | 4 | 6 |
| Unique spurious labels | 1 | 6 |

### Top vs low performers

**Top performers (loose score = 100):** None  
**Low performers (loose score < 80):** `Q1.0`

---

## Comparison: Experiment 21 vs Experiment 17

### Overall summary

Experiment 21 significantly underperforms experiment 17.

| Metric | Experiment 17 | Experiment 21 | Delta |
|--------|---------------|---------------|-------|
| Strict stability score | 89.1 | 68.3 | **-20.8** |
| Loose stability score | 90.8 | 68.3 | **-22.5** |
| Structural validity | 23/23 questions | 3/3 questions | N/A |
| Approach stability (strict) | 0.9432 | 0.6333 | **-0.3099** |
| Approach stability (canonical) | 0.9432 | 0.6333 | **-0.3099** |
| Applicability consistency (strict) | 0.7995 | 0.5185 | **-0.2810** |
| Applicability consistency (loose) | 0.8188 | 0.5185 | **-0.3003** |
| Recommendation consistency (strict) | 0.8551 | 0.7778 | **-0.0773** |
| Recommendation consistency (loose) | 0.9130 | 0.7778 | **-0.1352** |
| Questions with loose score ≥ 95 | 6 | 0 | **-6** |
| Questions with loose score < 80 | 3 | 1 | N/A |

### Score deltas by question

| Question | Exp. 17 loose | Exp. 21 loose | Delta |
|----------|---------------|---------------|-------|
| Q1.0 | 100.0 | 35.3 | **-64.7** |
| Q1.1 | 80.8 | 86.7 | +5.9 |
| Q1.2 | 87.5 | 82.8 | -4.7 |

### Analysis by Question

1. **Q1.0: Major Regression**
   - Experiment 17: Perfect score (100.0)
   - Experiment 21: Very poor score (35.3)
   - Problem: Q1.0 shows severe instability
     - Approach stability: only 0.20 (very low)
     - Applicability stability: only 0.22 (very low)
     - Recommendation stability: only 0.33 (very low)
   - Labels are inconsistent: `foreign_currency_accounting`, `foreign_currency_translation`, `ias21_fx_accounting`, `ias39_hedge_accounting`, `ifrs9_hedge_accounting` appear as spurious labels

2. **Q1.1: Slight Improvement**
   - Experiment 17: 80.8
   - Experiment 21: 86.7 (+5.9)
   - Approach stability: 1.00 (perfect)
   - Still some applicability instability (0.56)

3. **Q1.2: Slight Regression**
   - Experiment 17: 87.5
   - Experiment 21: 82.8 (-4.7)
   - Approach stability: 0.70 (some divergence)
   - One spurious label: `foreign_exchange_accounting`

### Spurious Labels Comparison

Experiment 21 generates far more spurious labels:

| Label | Exp. 17 | Exp. 21 |
|-------|---------|---------|
| `no_hedge_accounting` | 4 | 1 |
| `foreign_currency_accounting` | 0 | 1 |
| `foreign_currency_translation` | 0 | 1 |
| `foreign_exchange_accounting` | 0 | 1 |
| `ias21_fx_accounting` | 0 | 1 |
| `ias39_hedge_accounting` | 0 | 1 |
| `ifrs9_hedge_accounting` | 0 | 1 |

---

## Prompt Size Context

The corpus composition differs between experiments:

| Aspect | Experiment 17 | Experiment 21 |
|--------|---------------|---------------|
| Retrieval mode | Excerpted chunks | Full text |
| k value | 10 | 5 |
| Corpus | Targeted IFRS documents | All available free IFRS documents |
| Number of documents | Smaller, focused | Larger, comprehensive |

**Note:** The prompt size difference between experiments is primarily due to the **corpus size** (more documents = more candidates to retrieve from), not the retrieval method. The goal of experiment 21 was to test if full text retrieval with a larger corpus could still produce good results.

---

## Conclusion

Experiment 21 performs significantly worse than experiment 17.

Why experiment 21 underperforms:
- **Larger corpus** (all free IFRS documents) introduces more irrelevant documents as retrieval candidates
- **Full text retrieval** means the model sees entire sections, not just the most relevant excerpts
- **Severe instability on Q1.0**: The model diverges significantly, producing inconsistent approach labels and spurious FX accounting labels

The root cause is likely the **combination** of:
1. A larger, less focused corpus
2. Full text (not excerpted chunks) providing more noise

Experiment 17's excerpted chunks act as an implicit quality filter - only the most relevant excerpts are included.

What might work:
- **Corpus filtering**: Restrict retrieval to hedge-accounting-relevant documents only
- **Controlled comparison**: Same documents, comparing chunk vs full-text to isolate retrieval method effects
- **Document-type metadata**: Add metadata to help weight or filter retrieved content by relevance

---

## Root Cause Analysis

The poor performance on Q1.0 is likely due to the **larger corpus** introducing more irrelevant documents, not just the full text retrieval method:

1. **More candidate documents** in the larger corpus increases the chance of retrieving irrelevant sections
2. **Full text retrieval** means the model sees entire sections, not just the most relevant excerpts
3. The combination leads to:
   - Irrelevant IAS 21 (foreign exchange) paragraphs being retrieved
   - The model picking up spurious FX accounting labels instead of the hedge taxonomy
   - Inconsistent application of the three hedge approach framework

The excerpted chunks in experiment 17 act as an implicit filter - only the most relevant excerpts are included. Full text with a larger corpus loses this filtering effect.

---

## Recommended next steps

1. **Compare retrieval results** - audit what documents/sections are retrieved for Q1.0 in experiment 21 vs experiment 17 to identify which documents are causing the spurious labels

2. **Filter corpus by document type** - restrict retrieval to hedge-accounting-relevant documents (IFRS 9, IFRIC 16) and exclude or downweight general IFRS documents that are unlikely to be relevant

3. **Test with same corpus, different retrieval** - run a controlled comparison with the same documents but comparing chunk vs full-text retrieval to isolate the effect of retrieval method

4. **Add document-type filtering** - if a retrieved chunk comes from a document that's not directly about hedge accounting, either exclude it or add metadata to help the model weight it appropriately

The core issue: *a larger, less focused corpus with full text retrieval introduces too much noise*.

# Human analysis

## Impact of running retrieval on full corpus
- Prompt size went from 100k to 1.4M when the corpus expanded. This is way too much even just in terms of pricing.
- Query wording still changes which key IFRS 9 sections are retrieved, so retrieval is not robust yet
   - Global chunk retrieval with expansion gives too much context and is unstable: we need to find a way to focus retrieval on the most relevant documents (this is a generalization of recommended next-step #2 and #4).
   - Section titles cannot always correctly retrieve matching information because of generic titles like “Consensus”, which is typical in IFRIC documents. However, expert feedback confirms that sections, not chunks, are the right level of analysis since a section contains logically-grouped chunks.

## Retrieval score of key chunk IFRS 9 6.3.6

Paragraph 6.3.6 is the key provision in that it mentions foreign currency risk of a monetary item such as a recognizeed dividend can be covered by a hedge. However, its similarity to question Q1.0 is huge, in fact at 0.58 it's ranked lower than a chunk in IAS 21 and a chunk in IFRIC 17. The question is why ?!


IFRS9 6.3.6 says:
>the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated..."                                                                  

so, it specifically mentions "payable/receivable between two subsidiaries" - but not dividends. It is likely the embeddings don't identify these as being similar in semantic meaning. Perhaps some fine-tuning would help here ?

## Retrieval score of key chunk IFRS 9 B6.3.5
Another interesting case is IFRS9 B6.3.5 which provides additional guidance in that it excludes:
>royalty payments, interest payments or management charges between members of the same group, unless there is a related external transaction

Here again, "dividends" are not listed as explicitly eligible or ineligible so this chunk will not match the question well.

The LLM might be able to reason that dividends are not part of the exclusion... but only if the chunk is retrieved ! This is where retrieving all chunks of a section makes sense since standards documents will often have the following chunks within a section:
- rule
- exception
- example

## Suggestions

We can probably address all this issues by doing the following

1. Add document-selection stage before chunk retrieval
   - build a document-level representation from title, objective, scope, maybe intro
   - query with similarity and use top-d
      - then run chunk retrieval inside those documents
2. Do section-based expansion but without matching on the sections' titles
   - retrieve top chunks for each selected document
   - map them to their sections and expand to full section
      - extra idea: if retrieving chunks from sibling branches, expand to chunks that are children of common parent node (that's only one level up) rather than just the two sibling sections
