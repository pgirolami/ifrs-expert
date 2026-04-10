
---

**Provider:** `content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents`
**Experiment:** `28_more_questions_same_as_27`
**Run:** `2026-04-10_11-48-49_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 92.2 | 92.2 | True |
| Q1.1 | 3 | 93.3 | 93.3 | True |
| Q1.2 | 3 | 28.3 | 28.3 | False |
| Q1.3 | 3 | 62.8 | 62.8 | True |
| Q1.4 | 3 | 35.0 | 37.9 | True |
| Q1.5 | 3 | 92.2 | 92.2 | True |
| Q1.6 | 3 | 93.3 | 93.3 | True |
| Q1.7 | 3 | 81.3 | 88.3 | True |
| **AVERAGE** |  | **72.3** | **73.6** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 0.7778 | 0.7778 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.1 | 1.0000 | 1.0000 | 0.7778 | 0.7778 | 1.0000 | 1.0000 |
| Q1.2 | 0.3333 | 0.3333 | 0.3333 | 0.3333 | 0.3333 | 0.3333 |
| Q1.3 | 0.2222 | 0.2222 | 0.6667 | 0.6667 | 1.0000 | 1.0000 |
| Q1.4 | 0.0000 | 0.0833 | 0.0000 | 0.0000 | 1.0000 | 1.0000 |
| Q1.5 | 0.7778 | 0.7778 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.6 | 1.0000 | 1.0000 | 0.7778 | 0.7778 | 1.0000 | 1.0000 |
| Q1.7 | 0.4667 | 0.6667 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **72.3** | **73.6** |
| Approach (Jaccard, exact labels) | 0.5722 | 0.6076 |
| Applicability (exact values) | 0.6944 | 0.6944 |
| Recommendation (exact values) | 0.9167 | 0.9167 |
| | | |
| Total Questions | 8 | |
| Total Runs | 24 | |
| | | |
*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`


## Label Frequency by Question

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Total |
|---|---|---|---|---|---|---|---|---|---|
| fair_value_hedge | 3 | 3 | 2 | 2 | 1 | 3 | 3 | 2 | 19 |
| cash_flow_hedge | 3 | 3 | 2 | 1 | 1 | 3 | 3 | 2 | 18 |
| net_investment_hedge | 2 | 3 | 2 | 2 | 1 | 2 | 3 | 3 | 18 |

### Spurious Labels (< 10% of runs)

| Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Label |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | forecast_intragroup_hedge |
| 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | intragroup_monetary_hedge |
| 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | fx_hedge_accounting |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | intragroup_fx_hedge |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|

**0/8 questions (0%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.2 | 3 | 28.3 | 28.3 | 0.33 | 0.33 | 0.33 |
| Q1.4 | 3 | 35.0 | 37.9 | 0.00 | 0.00 | 1.00 |
| Q1.3 | 3 | 62.8 | 62.8 | 0.22 | 0.67 | 1.00 |

**3/8 questions (38%) are low performers**

