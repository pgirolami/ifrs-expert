
---

**Provider:** `content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents`
**Experiment:** `30_same_as_29_with_more_guardrails`
**Run:** `2026-04-10_14-22-29_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 100.0 | 100.0 | True |
| Q1.1 | 3 | 100.0 | 100.0 | True |
| Q1.2 | 3 | 100.0 | 100.0 | True |
| Q1.3 | 3 | 100.0 | 100.0 | True |
| Q1.4 | 3 | 92.2 | 92.2 | True |
| Q1.5 | 3 | 92.2 | 92.2 | True |
| Q1.6 | 3 | 93.3 | 93.3 | True |
| Q1.7 | 3 | 100.0 | 100.0 | True |
| **AVERAGE** |  | **97.2** | **97.2** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.4 | 0.7778 | 0.7778 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.5 | 0.7778 | 0.7778 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.6 | 1.0000 | 1.0000 | 0.7778 | 0.7778 | 1.0000 | 1.0000 |
| Q1.7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **97.2** | **97.2** |
| Approach (Jaccard, exact labels) | 0.9444 | 0.9444 |
| Applicability (exact values) | 0.9722 | 0.9722 |
| Recommendation (exact values) | 1.0000 | 1.0000 |
| | | |
| Total Questions | 8 | |
| Total Runs | 24 | |
| | | |
*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`


## Label Frequency by Question

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Total |
|---|---|---|---|---|---|---|---|---|---|
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 24 |
| fair_value_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 24 |
| net_investment_hedge | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 22 |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.2 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.3 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.1 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.7 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.0 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |

**5/8 questions (62%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|

**0/8 questions (0%) are low performers**

