
---

**Provider:** `content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents`
**Experiment:** `29_same_8_questions_prompt_with_hedging`
**Run:** `2026-04-10_13-42-42_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 84.4 | 84.4 | True |
| Q1.1 | 2 | 100.0 | 100.0 | True |
| Q1.2 | 3 | 100.0 | 100.0 | True |
| Q1.3 | 3 | 81.1 | 81.1 | True |
| Q1.4 | 3 | 92.2 | 92.2 | True |
| Q1.5 | 3 | 88.3 | 88.3 | True |
| Q1.6 | 3 | 93.3 | 93.3 | True |
| Q1.7 | 3 | 81.1 | 81.1 | True |
| **AVERAGE** |  | **90.1** | **90.1** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 0.5556 | 0.5556 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.3 | 0.5556 | 0.5556 | 0.8889 | 0.8889 | 1.0000 | 1.0000 |
| Q1.4 | 0.7778 | 0.7778 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.5 | 0.6667 | 0.6667 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.6 | 1.0000 | 1.0000 | 0.7778 | 0.7778 | 1.0000 | 1.0000 |
| Q1.7 | 0.5556 | 0.5556 | 0.8889 | 0.8889 | 1.0000 | 1.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **90.1** | **90.1** |
| Approach (Jaccard, exact labels) | 0.7639 | 0.7639 |
| Applicability (exact values) | 0.9444 | 0.9444 |
| Recommendation (exact values) | 1.0000 | 1.0000 |
| | | |
| Total Questions | 8 | |
| Total Runs | 23 | |
| | | |
*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`


## Label Frequency by Question

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Total |
|---|---|---|---|---|---|---|---|---|---|
| fair_value_hedge | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 23 |
| cash_flow_hedge | 2 | 2 | 3 | 2 | 3 | 0 | 3 | 2 | 17 |
| net_investment_hedge | 2 | 2 | 3 | 2 | 1 | 1 | 3 | 2 | 16 |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.2 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.1 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |

**2/8 questions (25%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|

**0/8 questions (0%) are low performers**

