# 2026-04-05

# Goal

Rerun all Q1 variants with promptfoo using `openai-codex` and a larger retrieval context (`k=10`), then compare the outcome against experiment 15 (`15_promptfoo_baseline_Q1`).

## Method

Analysis was produced with the existing scripts under `experiments/analysis/`:

```bash
uv run python experiments/analysis/analyze.py \
  'k=10__llm_provider=openai-codex__min-score=0.55' \
  --experiment 17_promptfoo_baseline_codex_k=10_Q1

uv run python experiments/analysis/analyze.py \
  openai \
  --experiment 15_promptfoo_baseline_Q1
```

---

## Automated analysis of Experiment 17

### Aggregate Metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **89.1** | **90.8** |
|
| Approach (Jaccard, exact labels) | 0.9432 | 0.9432 |
| Applicability (exact values) | 0.7995 | 0.8188 |
| Recommendation (exact values) | 0.8551 | 0.9130 |
|
| Total Questions | 23 |
| Total Runs | 69 |
|
| Structural validity | 23/23 questions | |

_Strict_: exact label/value matching  
_Loose_: maps `oui` ↔ `oui_sous_conditions`

### Per-question results

The table below now shows **all non-zero retrieved chunks**, not just the top 5.

| Question | Runs | Score | Score(loose) | Valid | IFRIC-16 | IFRS-9 |
|----------|------|-------|--------------|-------|----------|--------|
| Q1.0 | 3 | 100.0 | 100.0 | True | 5 (0.56), 13 (0.55) | B2.6 (0.60), 4.2.2 (0.59), B2.2 (0.59), 6.3.5 (0.58), B2.1 (0.58), B6.3.5 (0.58), 1.1 (0.58), 5.7.1A (0.58), 2.1 (0.57), 4.3.4 (0.57) |
| Q1.1 | 3 | 80.8 | 80.8 | True | 5 (0.56) | B2.6 (0.60), 4.2.2 (0.60), B3.2.17 (0.57), B2.2 (0.57), 5.7.1A (0.57), B3.2.10 (0.57), B5.7.9 (0.57), B7.2.3 (0.57), 4.3.4 (0.57), B2.1 (0.57) |
| Q1.2 | 3 | 67.5 | 87.5 | True | _(none)_ | B2.6 (0.60), 4.2.2 (0.59), B2.2 (0.57), 5.7.1A (0.57), B3.2.17 (0.56), B7.2.3 (0.56), B2.1 (0.56), B5.7.1 (0.56), B5.7.9 (0.56), B3.2.10 (0.56) |
| Q1.3 | 3 | 92.2 | 92.2 | True | 13 (0.59), 5 (0.59), 4 (0.59), 3 (0.58), AG9 (0.58), 9 (0.57), AG6 (0.57), AG4 (0.57), AG8 (0.57), 2 (0.57) | B6.3.5 (0.65), 6.3.6 (0.64), 4.2.2 (0.62), B6.3.6 (0.61), B6.3.4 (0.60), 5.7.1A (0.60), B2.6 (0.59), B6.6.10 (0.59), 6.3.5 (0.59), 6.3.4 (0.59) |
| Q1.4 | 3 | 100.0 | 100.0 | True | 13 (0.57), 5 (0.57), 18 (0.56), 17 (0.56), 18B (0.55), 18A (0.55) | 4.2.2 (0.60), B4.1.36 (0.59), B6.3.5 (0.58), B7.2.2 (0.58), 6.3.6 (0.57), B2.6 (0.57), 6.3.5 (0.57), B7.2.3 (0.57), B4.1.35 (0.57), B6.3.4 (0.57) |
| Q1.5 | 3 | 93.3 | 93.3 | True | 9 (0.57), 13 (0.57), 4 (0.57), 5 (0.57), 8 (0.56), 7 (0.56), AG1 (0.56), AG9 (0.56), 3 (0.55) | B6.3.5 (0.61), 6.3.6 (0.60), 4.2.2 (0.60), B2.6 (0.59), B2.1 (0.58), 5.7.1A (0.57), B6.3.4 (0.57), B6.6.10 (0.57), B2.2 (0.57), B6.3.6 (0.57) |
| Q1.6 | 3 | 80.0 | 100.0 | True | _(none)_ | B6.3.5 (0.60), 4.2.2 (0.58), B6.3.6 (0.58), 6.3.6 (0.58), B2.6 (0.57), 5.7.1A (0.57), B6.3.4 (0.57), 6.3.4 (0.56), 6.3.5 (0.56), 6.3.1 (0.56) |
| Q1.7 | 3 | 94.2 | 94.2 | True | 5 (0.59), 3 (0.57), 4 (0.56), 13 (0.56), 6 (0.55), 14 (0.55), AG8 (0.55) | 4.2.2 (0.61), 6.3.6 (0.60), B6.3.5 (0.60), B2.2 (0.59), B2.1 (0.59), 5.7.1A (0.59), 5.7.1 (0.58), B4.1.30 (0.58), 5.7.5 (0.58), B2.6 (0.58) |
| Q1.8 | 3 | 83.9 | 83.9 | True | 13 (0.57), 5 (0.57), 17 (0.56) | B6.3.4 (0.61), 6.3.4 (0.61), 6.3.5 (0.61), B6.3.5 (0.60), 6.3.3 (0.58), 5.7.1A (0.58), 6.3.6 (0.58), B6.3.6 (0.58), 6.3.2 (0.58), B2.6 (0.57) |
| Q1.9 | 3 | 93.3 | 93.3 | True | 5 (0.60), 4 (0.58), AG4 (0.58), 13 (0.58), 3 (0.58), AG5 (0.57), AG6 (0.57), AG9 (0.57), AG8 (0.57), AG13 (0.57) | 6.3.6 (0.66), B6.3.5 (0.64), 4.2.2 (0.61), B6.3.4 (0.61), B6.3.6 (0.60), B6.3.15 (0.59), B6.2.1 (0.58), B4.3.4 (0.58), 6.3.1 (0.58), 6.2.2 (0.58) |
| Q1.10 | 3 | 64.0 | 64.0 | True | 5 (0.60), 13 (0.58), 3 (0.57), 7 (0.57), 4 (0.57), AG9 (0.56), 17 (0.56), AG8 (0.56), 6 (0.55) | B6.3.5 (0.62), 6.3.6 (0.62), B6.3.6 (0.59), 4.2.2 (0.59), B2.2 (0.59), 5.7.1A (0.58), B2.1 (0.58), B6.3.4 (0.58), 4 (0.58), 6.3.5 (0.58) |
| Q1.11 | 3 | 93.3 | 93.3 | True | 13 (0.67), 5 (0.65), 14 (0.64), 2 (0.64), AG5 (0.63), 3 (0.63), 10 (0.62), AG4 (0.62), 1 (0.62), AG6 (0.61) | 6.3.5 (0.67), B6.3.5 (0.67), B6.3.6 (0.67), B6.3.4 (0.66), 6.3.4 (0.65), 6.3.6 (0.64), 6.3.3 (0.63), B6.5.39 (0.63), 6.3.2 (0.63), 6.5.12 (0.62) |
| Q1.12 | 3 | 100.0 | 100.0 | True | 13 (0.55), 5 (0.55), 9 (0.55), 4 (0.55) | B6.3.5 (0.60), 6.3.6 (0.60), 4.2.2 (0.59), B2.6 (0.58), B2.1 (0.57), B4.3.4 (0.57), 5.7.1A (0.57), B6.3.4 (0.56), B6.3.6 (0.56), B7.2.3 (0.56) |
| Q1.13 | 3 | 93.3 | 93.3 | True | 5 (0.58), 13 (0.58), 4 (0.57), AG1 (0.57), 3 (0.57), 7 (0.57), AG9 (0.57), 9 (0.56), 8 (0.56), AG4 (0.56) | B6.3.5 (0.64), 6.3.6 (0.63), 4.2.2 (0.62), B2.6 (0.61), B6.3.6 (0.60), B6.3.4 (0.59), B4.3.4 (0.59), B2.1 (0.59), B4.3.7 (0.59), 6.3.1 (0.59) |
| Q1.14 | 3 | 93.3 | 93.3 | True | 13 (0.58), AG9 (0.56), 4 (0.56), 9 (0.56), AG6 (0.56), 5 (0.55), AG4 (0.55) | B6.3.5 (0.64), 6.3.6 (0.61), B6.3.4 (0.61), B6.3.6 (0.61), 6.3.4 (0.58), 6.3.2 (0.58), 6.3.1 (0.58), B6.6.11 (0.57), 6.3.3 (0.57), B6.6.10 (0.57) |
| Q1.15 | 3 | 100.0 | 100.0 | True | 5 (0.58), 4 (0.56), 3 (0.56) | B2.6 (0.62), 3.3.5 (0.61), 4.2.2 (0.60), B2.1 (0.60), B2.4 (0.60), B4.3.4 (0.59), 6.3.6 (0.59), B6.3.5 (0.59), B2.2 (0.58), 6.3.4 (0.58) |
| Q1.16 | 3 | 100.0 | 100.0 | True | 4 (0.61), 5 (0.61), 3 (0.59), 1 (0.59), 13 (0.59), 6 (0.57), 7 (0.57), 2 (0.57), AG1 (0.57), AG9 (0.57) | 4.2.2 (0.63), 6.3.6 (0.63), B2.2 (0.62), 3.3.5 (0.62), B2.1 (0.62), 5.7.5 (0.62), B6.3.3 (0.62), B6.3.4 (0.61), 6.1.2 (0.61), B6.3.5 (0.61) |
| Q1.17 | 3 | 93.3 | 93.3 | True | 8 (0.59), 9 (0.59), 13 (0.59), AG5 (0.58), AG4 (0.57), 7 (0.57), AG3 (0.57), AG9 (0.56), AG6 (0.56), 10 (0.56) | B6.3.5 (0.64), 6.3.6 (0.63), B6.6.11 (0.62), B6.6.10 (0.62), B6.6.12 (0.62), 4.2.2 (0.60), 6.3.5 (0.60), B6.3.6 (0.60), 6.3.4 (0.59), 6.3.1 (0.59) |
| Q1.18 | 3 | 73.3 | 73.3 | True | 13 (0.58), 5 (0.56), AG5 (0.56), 7 (0.56), 8 (0.55), AG4 (0.55) | 6.3.4 (0.60), 6.3.5 (0.60), B6.3.4 (0.60), B6.6.11 (0.59), 6.3.2 (0.59), 6.3.3 (0.59), B6.6.10 (0.59), 6.3.1 (0.58), 6.6.3 (0.58), B2.6 (0.58) |
| Q1.19 | 3 | 93.3 | 93.3 | True | 13 (0.60), 9 (0.59), 7 (0.59), 4 (0.58), 8 (0.58), 5 (0.58), 3 (0.57), AG1 (0.57), AG8 (0.56), AG9 (0.55) | B6.3.5 (0.63), 6.3.6 (0.62), B6.3.4 (0.60), B6.3.6 (0.60), B6.6.10 (0.58), B2.6 (0.58), B6.3.3 (0.58), B4.3.4 (0.58), 6.3.4 (0.57), 4.2.2 (0.57) |
| Q1.20 | 3 | 93.3 | 93.3 | True | 5 (0.64), 13 (0.63), 2 (0.61), 3 (0.61), 7 (0.60), 4 (0.60), 10 (0.59), 1 (0.59), 14 (0.59), AG5 (0.59) | 6.3.5 (0.65), 6.3.4 (0.64), B6.3.4 (0.64), B6.3.6 (0.63), B6.3.5 (0.63), 6.3.3 (0.62), B6.5.39 (0.62), 6.3.2 (0.62), 6.3.1 (0.62), 6.3.6 (0.61) |
| Q1.21 | 3 | 73.3 | 73.3 | True | 5 (0.61), 4 (0.60), 3 (0.59), 2 (0.58), 13 (0.57), AG9 (0.57), 6 (0.56), 14 (0.56), 1 (0.56), 7 (0.56) | 6.3.6 (0.66), B6.3.5 (0.65), B6.3.4 (0.64), 6.3.1 (0.62), B6.3.6 (0.62), 6.3.4 (0.61), B6.6.13 (0.61), 6.3.2 (0.60), B4.3.4 (0.60), 6.3.3 (0.60) |
| Q1.22 | 3 | 93.3 | 93.3 | True | 13 (0.58), 4 (0.58), 8 (0.57), 5 (0.57), 7 (0.57), 3 (0.56), 9 (0.56), 1 (0.56), 2 (0.56), AG5 (0.55) | B2.6 (0.62), B6.3.5 (0.62), 6.3.6 (0.62), 4.2.2 (0.61), B2.1 (0.60), 5.7.1A (0.60), B6.3.6 (0.59), B5.7.3 (0.59), B4.3.11 (0.59), 6.9.4 (0.59) |
| **AVERAGE** | | **89.1** | **90.8** | | | |

### Detailed breakdown

| Question | Approach (strict) | Approach (mapped) |   Applic (strict)|        Applic (loose) |      Rec (strict) |          Rec (loose) |
| --- | --- | --- | --- | --- | --- | --- |
|Q1.0                                  |1.0000   |1.0000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.1                                  |0.8333   |0.8333   |0.5556       |0.5556  |1.0000      |1.0000|
|Q1.2                                  |0.8333   |0.8333   |0.5556       |0.7778  |0.3333      |1.0000|
|Q1.3                                  |0.7778   |0.7778   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.4                                  |1.0000   |1.0000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.5                                  |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.6                                  |1.0000   |1.0000   |0.7778       |1.0000  |0.3333      |1.0000|
|Q1.7                                  |0.8333   |0.8333   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.8                                  |0.7778   |0.7778   |0.7222       |0.7222  |1.0000      |1.0000|
|Q1.9                                  |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.10                                 |0.6389   |0.6389   |0.6667       |0.6667  |0.3333      |0.3333|
|Q1.11                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.12                                 |1.0000   |1.0000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.13                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.14                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.15                                 |1.0000   |1.0000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.16                                 |1.0000   |1.0000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.17                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.18                                 |1.0000   |1.0000   |0.5556       |0.5556  |0.3333      |0.3333|
|Q1.19                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.20                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.21                                 |1.0000   |1.0000   |0.5556       |0.5556  |0.3333      |0.3333|
|Q1.22                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|

### LABEL FREQUENCY BY QUESTION

#### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 69 |
| fair_value_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 69 |
| net_investment_hedge | 3 | 3 | 3 | **2** | 3 | 3 | 3 | 3 | **2** | 3 | **2** | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 66 |

#### Spurious Labels (< 10% of runs)

| Label | Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| no_hedge_accounting | 4 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Label behavior

Core labels are much cleaner than in experiment 15:

| Label | Experiment 15 | Experiment 17 |
|-------|---------------|---------------|
| `fair_value_hedge` | 60/69 runs | 69/69 runs |
| `cash_flow_hedge` | 60/69 runs | 69/69 runs |
| `net_investment_hedge` | 59/69 runs | 66/69 runs |
| Spurious label mentions | 9 | 4 |
| Unique spurious labels | 7 | 1 (`no_hedge_accounting`) |

The only remaining spurious label in experiment 17 is `no_hedge_accounting`, appearing 4 times total.

### Top vs low performers

**Top performers (loose score = 100):** `Q1.0`, `Q1.4`, `Q1.6`, `Q1.12`, `Q1.15`, `Q1.16`  
**Low performers (loose score < 80):** `Q1.10`, `Q1.18`, `Q1.21`

---

## Comparison: Experiment 17 vs Experiment 15

### Overall summary

Experiment 17 is the better baseline overall.

| Metric | Experiment 15 | Experiment 17 | Delta |
|--------|---------------|---------------|-------|
| Strict stability score | 86.1 | 89.1 | **+3.0** |
| Loose stability score | 87.1 | 90.8 | **+3.7** |
| Structural validity | 21/23 questions | 23/23 questions | **+2 questions** |
| Approach stability (strict) | 0.8684 | 0.9432 | **+0.0748** |
| Approach stability (canonical) | 0.8720 | 0.9432 | **+0.0712** |
| Applicability consistency (strict) | 0.8309 | 0.7995 | **-0.0314** |
| Applicability consistency (loose) | 0.8406 | 0.8188 | **-0.0218** |
| Recommendation consistency (strict) | 0.8551 | 0.8551 | 0.0000 |
| Recommendation consistency (loose) | 0.8841 | 0.9130 | **+0.0289** |
| Questions with loose score ≥ 95 | 7 | 6 | -1 |
| Questions with loose score < 80 | 4 | 3 | **-1** |

### Score deltas by question

| Question | Exp. 15 loose | Exp. 17 loose | Delta |
|----------|---------------|---------------|-------|
| Q1.1 | 5.8 | 80.8 | **+75.0** |
| Q1.15 | 64.2 | 100.0 | **+35.8** |
| Q1.6 | 76.4 | 100.0 | **+23.6** |
| Q1.2 | 65.0 | 87.5 | **+22.5** |
| Q1.11 | 83.9 | 93.3 | +9.4 |
| Q1.16 | 93.3 | 100.0 | +6.7 |
| Q1.12 | 94.2 | 100.0 | +5.8 |
| Q1.9 | 92.2 | 93.3 | +1.1 |
| Q1.0 | 100.0 | 100.0 | 0.0 |
| Q1.4 | 100.0 | 100.0 | 0.0 |
| Q1.7 | 94.2 | 94.2 | 0.0 |
| Q1.8 | 83.9 | 83.9 | 0.0 |
| Q1.13 | 93.3 | 93.3 | 0.0 |
| Q1.19 | 93.3 | 93.3 | 0.0 |
| Q1.20 | 93.3 | 93.3 | 0.0 |
| Q1.3 | 93.3 | 92.2 | -1.1 |
| Q1.5 | 100.0 | 93.3 | -6.7 |
| Q1.14 | 100.0 | 93.3 | -6.7 |
| Q1.17 | 100.0 | 93.3 | -6.7 |
| Q1.22 | 100.0 | 93.3 | -6.7 |
| Q1.21 | 83.9 | 73.3 | -10.6 |
| Q1.18 | 93.3 | 73.3 | -20.0 |
| Q1.10 | 100.0 | 64.0 | **-36.0** |

### Biggest improvements

1. **Q1.1 was effectively fixed**
   - Experiment 15 had one empty/invalid run and two divergent runs with spurious labels (`amortised_cost`, `fair_value_oci`, `fair_value_pl`).
   - Experiment 17 produced 3 structurally valid runs, all with `oui_sous_conditions` and the expected hedge taxonomy.

2. **Q1.15 moved from unstable/off-taxonomy to perfect stability**
   - Experiment 15 oscillated between `oui` and `non`, and sometimes emitted `financial_asset_accounting` / `foreign_translation` instead of the hedge taxonomy.
   - Experiment 17 converged on `fair_value_hedge`, `cash_flow_hedge`, `net_investment_hedge` in all 3 runs with `oui_sous_conditions` every time.

3. **Q1.2 became structurally usable**
   - Experiment 15 often failed to produce a valid recommendation at all.
   - Experiment 17 now consistently returns the three expected hedge approaches and a valid recommendation in every run.
   - Remaining issue: the recommendation still fluctuates between `oui` and `oui_sous_conditions`, so the strict score remains modest.

4. **Q1.6 improved materially in loose stability**
   - Experiment 15 often dropped `net_investment_hedge` and even produced `fair_value_profit` once.
   - Experiment 17 always returns the three core hedge labels.
   - Remaining instability is recommendation wording (`oui` vs `oui_sous_conditions`), not taxonomy.

### Biggest regressions

1. **Q1.10 is the clearest regression**
   - Experiment 15 was perfectly stable.
   - In experiment 17, one run recommended `non` and omitted `net_investment_hedge`; another added `no_hedge_accounting` as a fourth approach.
   - This drives both approach instability and recommendation instability.

2. **Q1.18 and Q1.21 regress mostly on recommendation/applicability, not approach extraction**
   - In both questions, experiment 17 still returns the expected hedge labels.
   - The instability comes from one run flipping from `oui_sous_conditions` to `non`, which drags down both applicability and recommendation consistency.

3. **Several former perfect performers slipped slightly**
   - `Q1.5`, `Q1.14`, `Q1.17`, and `Q1.22` each fell from 100.0 to 93.3.
   - These are small regressions, usually a single applicability disagreement rather than a taxonomy collapse.

### Retrieval comparison with experiment 15

Two important points came out of the comparison:

1. **The top retrieved evidence did not change**
   - For all **23/23 questions**, the top-5 non-zero retrieved chunks per document are identical between experiments 15 and 17.
   - So the major score changes are **not** explained by different top-ranked evidence.

2. **Experiment 17 supplies much more total context**
   - Average non-zero retrieved chunks per question:
     - Experiment 15: **9.0**
     - Experiment 17: **16.8**
   - This is consistent with the larger `k=10` retrieval setting.
   - In practice, experiment 17 mostly adds lower-ranked IFRS 9 background/context around the same core hits already present in experiment 15.

### Interpretation

The comparison suggests a mixed but favorable trade-off:

- **Better structure and taxonomy discipline** in experiment 17:
  - all runs are structurally valid at the question level,
  - the three expected hedge labels appear much more consistently,
  - spurious labels collapse from seven different variants to a single recurring outlier.

- **Slightly worse applicability precision** in experiment 17:
  - the model is more willing to hedge with `oui_sous_conditions`,
  - but it occasionally over-corrects to `non` on borderline cases (`Q1.10`, `Q1.18`, `Q1.21`).

- **The remaining instability is now concentrated**:
  - experiment 15 had broad taxonomy problems in several weak questions,
  - experiment 17 concentrates the remaining risk into a smaller set of recommendation-flip cases.

---

## Conclusion

Experiment 17 is the stronger overall baseline than experiment 15.

Why:
- higher overall stability,
- perfect structural validity,
- much better recovery of the intended hedge taxonomy,
- fewer spurious labels,
- major fixes on the worst questions from experiment 15 (`Q1.1`, `Q1.2`, `Q1.15`, `Q1.16`).

What still needs attention:
- suppressing or banning the fallback label `no_hedge_accounting`,
- tightening prompt guidance on when to answer `non` versus `oui_sous_conditions`,
- deep-diving `Q1.10`, `Q1.18`, and `Q1.21`, which are now the main stability risks.

## Recommended next step

Keep experiment 17 as the better baseline candidate, but run one follow-up prompt iteration aimed specifically at:

1. forbidding extra taxonomy labels such as `no_hedge_accounting`,
2. forcing the model to preserve the three hedge approaches even when the final recommendation is negative or conditional,
3. clarifying the decision rule for borderline intragroup FX cases so `non` is used only when the IFRS 9 exception is clearly unavailable.

## Human analysis of Experiment 17
Results in this experiment are much better than experiment 15. Approach stability is almost achieved perfectly. The problems we seem to have but didn't experimentally is that the recommendation may be wrong or the applicability may be wrong and the eval doesn't check that.

Event with k=10, retrieval is still problematic when we look at the chunks for question 1.2 for example. None of the paragraphs from sections 6 are retrieved !

### Next steps

1. add checks on the applicability for each approach
2. evaluate matching on the section titles