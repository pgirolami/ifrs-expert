
---

**Provider:** `content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents`
**Experiment:** `26_new_prompt_same_as_25`
**Run:** `2026-04-10_09-55-52_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 100.0 | 100.0 | True |
| Q1.2 | 3 | 53.3 | 59.2 | True |
| Q1.3 | 3 | 95.0 | 95.0 | True |
| Q1.4 | 3 | 78.0 | 78.0 | True |
| Q1.5 | 3 | 88.3 | 88.3 | True |
| Q1.6 | 3 | 53.9 | 56.7 | True |
| Q1.7 | 3 | 94.2 | 94.2 | True |
| **AVERAGE** |  | **80.4** | **81.6** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 0.3333 | 0.5000 | 0.2222 | 0.2222 | 1.0000 | 1.0000 |
| Q1.3 | 1.0000 | 1.0000 | 0.8333 | 0.8333 | 1.0000 | 1.0000 |
| Q1.4 | 0.3722 | 0.3722 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.5 | 0.6667 | 0.6667 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.6 | 0.2556 | 0.3333 | 0.3333 | 0.3333 | 1.0000 | 1.0000 |
| Q1.7 | 0.8333 | 0.8333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **80.4** | **81.6** |
| Approach (Jaccard, exact labels) | 0.6373 | 0.6722 |
| Applicability (exact values) | 0.7698 | 0.7698 |
| Recommendation (exact values) | 1.0000 | 1.0000 |
| | | |
| Total Questions | 7 | |
| Total Runs | 21 | |
| | | |
*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`


## Label Frequency by Question

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Total |
|---|---|---|---|---|---|---|---|---|
| net_investment_hedge | 3 | 2 | 3 | 0 | 3 | 3 | 3 | 17 |
| fair_value_hedge | 3 | 1 | 3 | 0 | 3 | 1 | 3 | 14 |
| cash_flow_hedge | 3 | 1 | 3 | 0 | 2 | 1 | 3 | 13 |
| foreign_currency_translation | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 5 |
| hedge_accounting | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 4 |
| foreign_currency_accounting | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 3 |

### Spurious Labels (< 10% of runs)

| Total | Q1.0 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Label |
|---|---|---|---|---|---|---|---|---|
| 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | consolidation_elimination |
| 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | forecast_transaction_hedge |
| 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | intragroup_monetary_hedge |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | consolidation_accounting |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | foreign_currency_hedge |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | monetary_item_translation |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | separate_financial_statements |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | separate_fs_accounting |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.0 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.3 | 3 | 95.0 | 95.0 | 1.00 | 0.83 | 1.00 |

**2/7 questions (29%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.6 | 3 | 53.9 | 56.7 | 0.26 | 0.33 | 1.00 |
| Q1.2 | 3 | 53.3 | 59.2 | 0.33 | 0.22 | 1.00 |
| Q1.4 | 3 | 78.0 | 78.0 | 0.37 | 1.00 | 1.00 |

**3/7 questions (43%) are low performers**

### Key Observations

- **Approach stability (strict)**: Top=1.000, Low=0.320, Delta=+0.680
- **Approach stability (canonical)**: Top=1.000, Low=0.402, Delta=+0.598
- **Applicability consistency (loose)**: Top=0.917, Low=0.519, Delta=+0.398
- **Recommendation consistency (loose)**: Top=1.000, Low=1.000, Delta=+0.000
- **Avg unique labels per run**: Top=3.5, Low=5.7

