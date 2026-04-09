
================================================================================
PROVIDER: content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents
EXPERIMENT: 24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22
RUN: 2026-04-09_20-36-57_promptfoo-eval-family-q1
================================================================================


================================================================================
PER QUESTION RESULTS
================================================================================

| Question |       Runs |      Score | Score(loose) |      Valid |
| -------- | ----- | ------- | ------------ | ----- |
| Q1.0     |     3 |    75.5 |         75.5 |  True |
| Q1.1     |     3 |    94.2 |         94.2 |  True |
| Q1.2     |     3 |   100.0 |        100.0 |  True |
| Q1.3     |     3 |    76.7 |         76.7 |  True |
| Q1.4     |     3 |    93.3 |        100.0 |  True |
| Q1.5     |     3 |    81.3 |         81.3 |  True |
| Q1.6     |     3 |    71.7 |         76.7 |  True |
| Q1.7     |     3 |    64.7 |         64.7 |  True |
|          |       |         |              |       |
| AVERAGE  |       |    82.2 |         83.6 |       |

================================================================================
DETAILED BREAKDOWN
================================================================================
Question                            Approach Approach   Applic        Applic      Rec          Rec
                                    (strict) (mapped) (strict)       (loose) (strict)      (loose)
----------------------------------- -------- -------- -------- ------------- -------- ------------
Q1.0                                  0.3000   0.3000   1.0000        1.0000   1.0000       1.0000
Q1.1                                  0.8333   0.8333   1.0000        1.0000   1.0000       1.0000
Q1.2                                  1.0000   1.0000   1.0000        1.0000   1.0000       1.0000
Q1.3                                  0.3333   0.3333   1.0000        1.0000   1.0000       1.0000
Q1.4                                  1.0000   1.0000   0.7778        1.0000   1.0000       1.0000
Q1.5                                  0.4667   0.4667   1.0000        1.0000   1.0000       1.0000
Q1.6                                  0.3333   0.3333   0.8333        1.0000   1.0000       1.0000
Q1.7                                  0.2778   0.2778   0.6667        0.6667   1.0000       1.0000

================================================================================
AGGREGATE METRICS
================================================================================

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **82.2** | **83.6** |
|
| Approach (Jaccard, exact labels) | 0.5681 | 0.5681 |
| Applicability (exact values) | 0.9097 | 0.9583 |
| Recommendation (exact values) | 1.0000 | 1.0000 |
|
| Total Questions | 8 |
| Total Runs | 24 |
|
_Strict_: exact label/value matching | _Loose_: maps `oui` ↔ `oui_sous_conditions` |

================================================================================
LABEL FREQUENCY BY QUESTION
================================================================================

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Total |
|---|---|---|---|---|---|---|---|---|---|
| hedge_accounting | 2 | 0 | 0 | 3 | 3 | 2 | 3 | 2 | 15 |
| net_investment_hedge | 3 | 3 | 3 | 1 | 0 | 1 | 1 | 2 | 14 |
| cash_flow_hedge | 1 | 3 | 3 | 0 | 0 | 1 | 0 | 1 | 9 |
| fair_value_hedge | 1 | 3 | 3 | 0 | 0 | 1 | 0 | 1 | 9 |
| foreign_currency_accounting | 0 | 0 | 0 | 2 | 0 | 3 | 2 | 1 | 8 |
| foreign_currency_translation | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 4 |
| consolidation_accounting | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 |
| separate_financials | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 |

### Spurious Labels (< 10% of runs)

| Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Label |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | no_hedge_accounting |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | dividend_recognition |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | net_investment_accounting |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ordinary_accounting |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | undesignated_derivative |

================================================================================
COMPARISON: TOP VS LOW PERFORMERS
================================================================================

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.2 | 3 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.4 | 3 | 93.3 | 100.0 | 1.00 | 1.00 | 1.00 |

**2/8 questions (25%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.7 | 3 | 64.7 | 64.7 | 0.28 | 0.67 | 1.00 |
| Q1.0 | 3 | 75.5 | 75.5 | 0.30 | 1.00 | 1.00 |
| Q1.3 | 3 | 76.7 | 76.7 | 0.33 | 1.00 | 1.00 |
| Q1.6 | 3 | 71.7 | 76.7 | 0.33 | 1.00 | 1.00 |

**4/8 questions (50%) are low performers**

### Key Observations
- **Approach stability (strict)**: Top=1.000, Low=0.311, Delta=+0.689
- **Approach stability (canonical)**: Top=1.000, Low=0.311, Delta=+0.689
- **Applicability consistency (loose)**: Top=1.000, Low=0.917, Delta=+0.083
- **Recommendation consistency (loose)**: Top=1.000, Low=1.000, Delta=+0.000
- **Avg unique labels per run**: Top=3.0, Low=5.5
