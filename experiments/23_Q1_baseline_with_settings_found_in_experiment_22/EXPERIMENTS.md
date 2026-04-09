# 2026-04-09

# Goal

Evalute if our new retrieval system narrows the LLM's focus enough to maintain the performance of experiment 17 (the corpus of which only contained IFRIC 16 and IFRS 9): 
- rerun all Q1 variants with promptfoo using `openai-codex` and the optimal per-document-type retrieval settings found in experiment 22
- compare to experiment 17

Note: not all questions were processed because we hit usage limits when running.

## Method

Analysis was produced with the existing scripts under `experiments/analysis/`:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__d=25__ias-d=4__ias-min-score=0.4__ifric-d=6__ifric-min-score=0.48__ifrs-d=4__ifrs-min-score=0.53__llm_provider=openai-codex__ps-d=1__ps-min-score=0.4__retrieval-mode=documents__sic-d=6__sic-min-score=0.4' \
  --experiment 23_Q1_baseline_with_settings_found_in_experiment_22
```

⚠️ An incorrect configuration made this run with a default +/- 5 chunk expansion and not the expansion to all the chunks in a section. This was not the plan but it will serve as a way to estimate the performance impact of expanding to a whole section.

## Automated analysis of Experiment 23

### Aggregate Metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **81.6** | **81.7** |
|
| Approach (Jaccard, exact labels) | 0.7477 | 0.7477 |
| Applicability (exact values) | 0.7059 | 0.7108 |
| Recommendation (exact values) | 0.9608 | 0.9608 |
|
| Total Questions | 17 |
| Total Runs | 50 |
|
_Strict_: exact label/value matching  
_Loose_: maps `oui` ↔ `oui_sous_conditions`

### Per-question results

| Question | Runs | Score | Score(loose) | Valid |
|----------|------|-------|--------------|-------|
| Q1.0 | 3 | 89.5 | 89.5 | True |
| Q1.1 | 3 | 93.3 | 93.3 | True |
| Q1.2 | 3 | 100.0 | 100.0 | True |
| Q1.3 | 3 | 90.0 | 90.0 | True |
| Q1.4 | 3 | 83.4 | 83.4 | True |
| Q1.5 | 3 | 82.3 | 84.8 | True |
| Q1.6 | 3 | 61.2 | 61.2 | True |
| Q1.7 | 3 | 95.0 | 95.0 | True |
| Q1.8 | 3 | 53.3 | 53.3 | True |
| Q1.9 | 3 | 93.3 | 93.3 | True |
| Q1.11 | 3 | 84.0 | 84.0 | True |
| Q1.12 | 3 | 53.8 | 53.8 | True |
| Q1.13 | 3 | 43.3 | 43.3 | True |
| Q1.14 | 3 | 84.8 | 84.8 | True |
| Q1.15 | 3 | 93.3 | 93.3 | True |
| Q1.16 | 3 | 93.3 | 93.3 | True |
| Q1.17 | 2 | 92.5 | 92.5 | True |
| **AVERAGE** | | **81.6** | **81.7** | |

### Detailed breakdown

| Question | Approach (strict) | Approach (mapped) |   Applic (strict)|        Applic (loose) |      Rec (strict) |          Rec (loose) |
| --- | --- | --- | --- | --- | --- | --- |
|Q1.0                                  |0.7000   |0.7000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.1                                  |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.2                                  |1.0000   |1.0000   |1.0000       |1.0000  |1.0000      |1.0000|
|Q1.3                                  |1.0000   |1.0000   |0.6667       |0.6667  |1.0000      |1.0000|
|Q1.4                                  |0.7167   |0.7167   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.5                                  |0.7333   |0.7333   |0.7222       |0.8056  |1.0000      |1.0000|
|Q1.6                                  |0.1778   |0.1778   |0.6667       |0.6667  |1.0000      |1.0000|
|Q1.7                                  |1.0000   |1.0000   |0.8333       |0.8333  |1.0000      |1.0000|
|Q1.8                                  |0.3333   |0.3333   |0.2222       |0.2222  |1.0000      |1.0000|
|Q1.9                                  |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.11                                 |0.7333   |0.7333   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.12                                 |0.2500   |0.2500   |0.3333       |0.3333  |1.0000      |1.0000|
|Q1.13                                 |0.3333   |0.3333   |0.3333       |0.3333  |0.3333      |0.3333|
|Q1.14                                 |0.7333   |0.7333   |0.8056       |0.8056  |1.0000      |1.0000|
|Q1.15                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.16                                 |1.0000   |1.0000   |0.7778       |0.7778  |1.0000      |1.0000|
|Q1.17                                 |1.0000   |1.0000   |0.7500       |0.7500  |1.0000      |1.0000|

### LABEL FREQUENCY BY QUESTION

#### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 45 |
| fair_value_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 45 |
| net_investment_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 45 |
| foreign_currency_accounting | 0 | 0 | 0 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 | 17 |
| hedge_accounting | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 5 |

#### Spurious Labels (< 10% of runs)

| Label | Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| --- |
| consolidation_elimination | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| foreign_currency_translation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| no_hedge_accounting | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| fair_value_pl | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| financial_instrument_accounting | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| foreign_exchange_accounting | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| fvtpl_derivative_accounting | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| general_accounting | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

### Label behavior

Experiment 23 has much more label noise than experiment 17:

| Label | Experiment 17 | Experiment 23 |
|-------|---------------|---------------|
| `fair_value_hedge` | 69/69 runs | 45/50 runs |
| `cash_flow_hedge` | 69/69 runs | 45/50 runs |
| `net_investment_hedge` | 66/69 runs | 45/50 runs |
| `foreign_currency_accounting` | 0 | 17/50 runs |
| `hedge_accounting` | 0 | 5/50 runs |
| Spurious label mentions | 4 | 12 |
| Unique spurious labels | 1 | 8 |

The three core hedge labels are no longer consistent - experiment 23 introduces significant label noise with `foreign_currency_accounting` appearing in 34% of runs.

### Top vs low performers

**Top performers (loose score = 100):** `Q1.2`, `Q1.7`  
**Low performers (loose score < 80):** `Q1.13`, `Q1.8`, `Q1.12`, `Q1.6`

---

## Comparison: Experiment 23 vs Experiment 17

### Overall summary

Experiment 17 is significantly better than experiment 23 overall.

| Metric | Experiment 17 | Experiment 23 | Delta |
|--------|---------------|---------------|-------|
| Strict stability score | 89.1 | 81.6 | **-7.5** |
| Loose stability score | 90.8 | 81.7 | **-9.1** |
| Questions evaluated | 23 | 17 | -6 questions |
| Total Runs | 69 | 50 | -19 runs |
| Approach stability (strict) | 0.9432 | 0.7477 | **-0.1955** |
| Approach stability (canonical) | 0.9432 | 0.7477 | **-0.1955** |
| Applicability consistency (strict) | 0.7995 | 0.7059 | **-0.0936** |
| Applicability consistency (loose) | 0.8188 | 0.7108 | **-0.1080** |
| Recommendation consistency (strict) | 0.8551 | 0.9608 | **+0.1057** |
| Recommendation consistency (loose) | 0.9130 | 0.9608 | **+0.0478** |
| Questions with loose score ≥ 95 | 6 | 2 | -4 |
| Questions with loose score < 80 | 3 | 4 | +1 |

### Score deltas by question (shared questions only)

| Question | Exp. 17 loose | Exp. 23 loose | Delta |
|----------|---------------|---------------|-------|
| Q1.2 | 87.5 | 100.0 | **+12.5** |
| Q1.7 | 94.2 | 95.0 | +0.8 |
| Q1.1 | 80.8 | 93.3 | **+12.5** |
| Q1.15 | 100.0 | 93.3 | -6.7 |
| Q1.16 | 100.0 | 93.3 | -6.7 |
| Q1.11 | 93.3 | 84.0 | -9.3 |
| Q1.9 | 93.3 | 93.3 | 0.0 |
| Q1.4 | 100.0 | 83.4 | **-16.6** |
| Q1.3 | 92.2 | 90.0 | -2.2 |
| Q1.5 | 93.3 | 84.8 | -8.5 |
| Q1.14 | 93.3 | 84.8 | -8.5 |
| Q1.1 | 80.8 | 93.3 | +12.5 |
| Q1.0 | 100.0 | 89.5 | **-10.5** |
| Q1.6 | 100.0 | 61.2 | **-38.8** |
| Q1.8 | 83.9 | 53.3 | **-30.6** |
| Q1.13 | 93.3 | 43.3 | **-50.0** |
| Q1.12 | 100.0 | 53.8 | **-46.2** |
| Q1.17 | 93.3 | 92.5 | -0.8 |

### Biggest improvements in Experiment 23

1. **Q1.2 achieved perfect stability**
   - Experiment 17 had recommendation instability (0.3333 strict, 1.0 loose).
   - Experiment 23 achieved 100.0 on both strict and loose metrics.
   - All 3 runs converge perfectly.

2. **Q1.1 improved significantly**
   - Experiment 17 had one run with `no_hedge_accounting` spurious label.
   - Experiment 23 shows perfect approach extraction.

### Biggest regressions in Experiment 23

1. **Q1.13 collapsed from 93.3 to 43.3**
   - Approach stability dropped from 1.0 to 0.33
   - Applicability consistency dropped from 0.78 to 0.33
   - Recommendation consistency dropped from 1.0 to 0.33
   - The model is producing highly divergent answers across runs

2. **Q1.12 collapsed from 100.0 to 53.8**
   - Approach stability dropped from 1.0 to 0.25
   - Applicability dropped from 1.0 to 0.33
   - Core hedge labels are missing in multiple runs

3. **Q1.6 regressed from 100.0 to 61.2**
   - Approach stability dropped from 1.0 to 0.18
   - Only 1/3 runs include all three core hedge labels
   - New spurious labels: `hedge_accounting`, `foreign_currency_accounting`

4. **Q1.8 regressed from 83.9 to 53.3**
   - Approach stability dropped from 0.78 to 0.33
   - Applicability dropped from 0.72 to 0.22

### Label quality degradation

The most concerning finding is the explosion of spurious labels in experiment 23:

- **Experiment 17**: Only 4 mentions of 1 spurious label (`no_hedge_accounting`)
- **Experiment 23**: 12 mentions across 8 different spurious labels

The new spurious labels suggest the model is misinterpreting what constitutes an "approach":
- `foreign_currency_accounting` (17 mentions)
- `hedge_accounting` (5 mentions)
- `consolidation_elimination` (3 mentions)
- `foreign_currency_translation` (2 mentions)

### Interpretation

The 30-fold increase in corpus documents appears to be hurting performance, which was to be expected:

1. **Label noise increased dramatically**: The three core hedge labels are no longer consistent across runs
2. **Several questions collapsed**: Q1.6, Q1.8, Q1.12, Q1.13 all show significant regressions
3. **Spurious labels exploded**: From 1 spurious label to 8 different ones

The only improvements are in recommendation consistency (which was already high in experiment 17) and two questions (Q1.2, Q1.1).


## Human analysis of Experiment 23

### Qualitative analysis of spurious approaches

Overall, the results are encouraging: despite a corpus 30x larger, the 3 approaches are mostly always identified.

Unfortunately, a lot of spurious approaches also appeared. We need to distinguish those that appeared consistently across runs and whether they could be accepted after-all.

**Approaches that appeared often**
| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| foreign_currency_accounting | 0 | 0 | 0 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 | 17 |
| hedge_accounting | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 5 |

   `foreign_currency_accounting` appears 17 times across 8 questions = 2 runs per question on average (1/3 of runs). In each case, it is a "fallback" case if hedging isn't done so it is not incorrect to list it, it's just not very useful. This suggests the model is being pulled toward IAS 21 / consolidation topics rather than focusing on the core hedge accounting approaches.

   `hedge_accounting` appears 6 times across 4 questions = 1.5 runs per question on average. This is a regression on its face. However
   - in all but one cases, the reasoning correctly identified that hedge accounting could be done to cover the foreign currency risk on the dividends since they are a monetary Xxx. It also correctly cityed IFR 9 6.3.5/6.3.6
   - on question Q1.13, only one run didn't identify the 3 approaches and, moreover, the LLM responded with a "no" saying the exclusion didn't apply here. This was clearly a reasoning mistake. We will get back to this in a later experiment
   - so 4/5 times, the answer was in fact correct

**Approaches that appeared less often**
| Label | Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| --- |
| consolidation_elimination | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| foreign_currency_translation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| no_hedge_accounting | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| fair_value_pl | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| financial_instrument_accounting | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| foreign_exchange_accounting | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| fvtpl_derivative_accounting | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| general_accounting | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

   `consolidation_elimination` is an interesting case: it says you have to eliminate intra-group flows. 
      - In Q1.4: it does mention the IFRS 9 6.3.6 exclusion so again, the answer is correct. It's just not needed since the approaches are the 3 we expect
      - In Q.13, it doesn't
   `foreign_currency_translation` appears once and is another "fallback" approach to standard IAS 21 / IFRS 9. The answer is not detailed enough

### Canonical mapping
Based on a review of each prompt-B response, we can map the spurious approaches to the following groups

| Approach label | Approach group | Notes |
| --- | --- | --- |
| foreign_currency_accounting | no_hedge_accounting | |
| hedge_accounting | hedge_accounting | A generic label that identify hedging but doesn't distinguish the types |
| consolidation_elimination | no_hedge_accounting | The reasoning is unstable: the 6.3.6 exception is mentioned 1/3 times but doesn't elaborate, the exception is noted without a citation in 1/3 times | 
| foreign_currency_translation | no_hedge_accounting | |
| no_hedge_accounting | no_hedge_accounting | |
| fair_value_pl | fair_value_pl |
| financial_instrument_accounting | no_hedge_accounting | |
| foreign_exchange_accounting | no_hedge_accounting |
| fvtpl_derivative_accounting | no_hedge_accounting | The reasoning mentions a "derivative" which I don't think the dividend is |
| general_accounting | no_hedge_accounting |

This is encouraging because most of the spurious approaches actually map to "default accounting" so they're the "fallback" mentioned earlier.

### Quantitative analysis to find correlations between retrieval and approaches identified

We built an [approach x sections matrix](./runs/2026-04-09_16-06-09_promptfoo-eval-family-q1/artifacts/Q1/spurious_approaches_vs_sections_matrix.html) to get a feel for what was happening across all the runs.

Some of things we noticed:
1. ⚠️ the matrix was built assuming we were expanding to whole sections but in fact we were expanding +/-5 so the results are probably not 100% correct
2. ❌ ~~The IFRS 9 paragraph containing the exhaustive list and precise definition of all possible hedging relationships (6.5.2) is never retrieved, across all runs.~~ It was in fact retrieved but via expansion and that version of the HTML page excluded sections with only expanded chunks.

   💡 *It would be worth manually adding it to the context to see the impact on the approaches identified*

3. **(foreign_currency_accounting,foreign_currency_translation,foreign_exchange_accounting) group**

   The clearest correlation is with the retrieval of IAS 21 paragraphs, it is a near perfect match except for
      - Q1.4 repeat 1: has `foreign_currency_accounting` but no IAS sections at all
      - every other run that surfaced one of these approaches had at least `IAS 21::44-47`
      - given the approaches can differ across runs for a given question, it is likely we can't find much stronger correlations

# Next steps
1. Rerun the promptfoo eval with the section expansion and analyze
2. Compare the results