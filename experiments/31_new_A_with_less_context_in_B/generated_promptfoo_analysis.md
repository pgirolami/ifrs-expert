
---

**Provider:** `content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents`
**Experiment:** `31_new_A_with_less_context_in_B`
**Run:** `2026-04-10_17-44-35_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 100.0 | 100.0 | True |
| Q1.1 | 3 | 100.0 | 100.0 | True |
| Q1.2 | 3 | 86.7 | 86.7 | True |
| Q1.3 | 3 | 100.0 | 100.0 | True |
| Q1.4 | 3 | 80.0 | 80.0 | True |
| Q1.5 | 3 | 100.0 | 100.0 | True |
| Q1.6 | 3 | 100.0 | 100.0 | True |
| Q1.7 | 3 | 100.0 | 100.0 | True |
| **AVERAGE** |  | **95.8** | **95.8** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 1.0000 | 1.0000 | 0.5556 | 0.5556 | 1.0000 | 1.0000 |
| Q1.3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.4 | 1.0000 | 1.0000 | 0.7778 | 0.7778 | 0.3333 | 0.3333 |
| Q1.5 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.6 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **95.8** | **95.8** |
| Approach (Jaccard, exact labels) | 1.0000 | 1.0000 |
| Applicability (exact values) | 0.9167 | 0.9167 |
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
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 24 |
| fair_value_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 24 |
| net_investment_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 24 |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.5 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.3 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.1 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.6 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.7 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.0 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |

**6/8 questions (75%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|

**0/8 questions (0%) are low performers**

