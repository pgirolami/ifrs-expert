
---

**Provider:** `content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents`
**Experiment:** `27_new_prompt_same_as_26`
**Run:** `2026-04-10_11-39-46_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 100.0 | 100.0 | True |
| Q1.2 | 3 | 80.0 | 100.0 | True |
| **AVERAGE** |  | **90.0** | **100.0** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 1.0000 | 1.0000 | 0.7778 | 1.0000 | 0.3333 | 1.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **90.0** | **100.0** |
| Approach (Jaccard, exact labels) | 1.0000 | 1.0000 |
| Applicability (exact values) | 0.8889 | 1.0000 |
| Recommendation (exact values) | 0.6667 | 1.0000 |
| | | |
| Total Questions | 2 | |
| Total Runs | 6 | |
| | | |
*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`


## Label Frequency by Question

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.2 | Total |
|---|---|---|---|
| cash_flow_hedge | 3 | 3 | 6 |
| fair_value_hedge | 3 | 3 | 6 |
| net_investment_hedge | 3 | 3 | 6 |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.2 | 3 | 80.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.0 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |

**2/2 questions (100%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|

**0/2 questions (0%) are low performers**

