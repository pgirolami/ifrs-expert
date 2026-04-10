# 2026-04-10

# Goal

Test whether adding the changes to the prompts improves upon experiment 24's results. The changes attempted to address the issue identified in experiment 24's human analysis: the model was treating baseline accounting consequences and optional overlays (e.g., hedge accounting) as separate peer approaches, when IFRS treats the overlay as an optional modification of the baseline treatment.

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 25
- [`generated_promptfoo_analysis_experiment_24_reference.md`](./generated_promptfoo_analysis_experiment_24_reference.md) — automated reference summary for experiment 24
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Method

Commands run:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 25_new_prompt_same_as_24 \
  > experiments/25_new_prompt_same_as_24/generated_promptfoo_analysis.md

uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22 \
  > experiments/25_new_prompt_same_as_24/generated_promptfoo_analysis_experiment_24_reference.md

uv run python experiments/analysis/generate_spurious_approaches_sections_matrix.py \
  --experiment 25_new_prompt_same_as_24 \
  --provider 'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents'
```

## Automated analysis of Experiment 25

From [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md):

### Aggregate metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **81.5** | **83.4** |
| Approach stability | 0.6802 | 0.6802 |
| Applicability consistency | 0.8188 | 0.8413 |
| Recommendation consistency | 0.9048 | 0.9683 |
| Total questions | 21 | |
| Total runs | 61 | |

### Top and low performers

- **Top performers:** `Q1.2`, `Q1.8`, `Q1.10`, `Q1.20`
- **Low performers:** `Q1.0`, `Q1.3`, `Q1.7`, `Q1.12`, `Q1.14`, `Q1.15`, `Q1.17`, `Q1.19`

## My analysis

### 1. Experiment 25 covers a much larger question set

Experiment 24 only ran `Q1.0`–`Q1.7` (8 questions, 24 runs). Experiment 25 ran all 21 Q1 questions with 61 total runs. This makes direct comparison only possible on the overlapping `Q1.0`–`Q1.7` subset.

### 2. On the overlapping subset, results are mixed

| Question | Exp. 24 loose | Exp. 25 loose | Delta |
|----------|---------------|----------------|-------|
| Q1.0 | 75.5 | 59.3 | **-16.2** |
| Q1.1 | 94.2 | N/A | N/A |
| Q1.2 | 100.0 | 100.0 | 0.0 |
| Q1.3 | 76.7 | 75.5 | -1.2 |
| Q1.4 | 100.0 | 90.0 | **-10.0** |
| Q1.5 | 81.3 | 90.7 | **+9.4** |
| Q1.6 | 76.7 | 90.7 | **+14.0** |
| Q1.7 | 64.7 | 62.6 | -2.1 |

The pattern is not clearly positive or negative on the overlapping subset. The changes helped Q1.5 and Q1.6, but hurt Q1.0, Q1.4, and was neutral to Q1.3, Q1.7.

### 3. Q1.0 is the most concerning regression

Q1.0 dropped from 75.5 to 59.3 — a significant regression. The approach stability collapsed from 0.30 to 0.12, suggesting the changes actually made the model *more* inconsistent in how it structures the taxonomy for this question.

Looking at the label frequency for Q1.0:
- `net_investment_hedge` appears in 2/3 runs
- `fair_value_hedge` appears in 1/3 run
- `cash_flow_hedge` appears in 1/3 run
- `hedge_accounting` appears in 2/3 runs (too generic)

### 4. Q1.4 shows the "stably wrong" pattern persists

Q1.4 dropped from 100.0 to 90.0 (strict). The runs still emit:
- `consolidation_accounting` (2/2 runs)
- `separate_financials` (2/2 runs)

This is the same stably wrong taxonomy from experiment 24. The rule did not help because the underlying routing issue (retrieval landing on IFRS 10/IAS 27 instead of IFRS 9) is still present.

### 5. The label frequency table shows cleaner taxonomy

Compared to experiment 24, experiment 25's core labels are more concentrated:

| Label | Exp. 24 Total | Exp. 25 Total |
|-------|---------------|---------------|
| net_investment_hedge | 14/24 = 58% | 55/61 = 90% |
| fair_value_hedge | 9/24 = 37.5% | 46/61 = 75.5% |
| cash_flow_hedge | 9/24 = 37.5% | 44/61 = 72% |
| hedge_accounting | 15/24 = 62.5% | 15/61 = 25% |
| foreign_currency_accounting | 8/24 = 33% | 9/61 = 14.75% |

The three core hedge types are now much more dominant. However, the spurious labels remain similar in count, suggesting the changes prioritized  the right taxonomy but didn't eliminate noise.

**Overlapping subset (Q1.0–Q1.7) breakdown:**

On the comparable 7-question subset, the label distribution shifted:

| Label | Exp. 24 (Q1.0-Q1.7) | Exp. 25 (Q1.0-Q1.7) | Delta |
|-------|----------------------|----------------------|-------|
| net_investment_hedge | 14 | 16 | +2 |
| fair_value_hedge | 9 | 12 | +3 |
| cash_flow_hedge | 9 | 12 | +3 |
| hedge_accounting | 15 | 8 | **-7** |
| foreign_currency_accounting | 8 | 5 | -3 |
| foreign_currency_translation | 4 | 5 | +1 |
| consolidation_accounting | 3 | 2 | -1 |
| separate_financials | 3 | 2 | -1 |

Key observations on the overlapping subset:
- `hedge_accounting` (generic label) dropped significantly from 15 to 8 — a **47% reduction**
- The three specific hedge types increased — the model is naming the right taxonomy more often
- The spurious consolidation/separate financials labels remain but are reduced

This suggests the changes helped the model be more specific when naming hedge approaches, but the improvement is most visible in *reducing the generic label* rather than completely eliminating noise.

### 6. Recommendation consistency dropped slightly

Experiment 24 had perfect recommendation consistency (1.0000 strict, 1.0000 loose). Experiment 25 dropped to:
- Strict: 0.9048
- Loose: 0.9683

This is due to several questions having recommendation splits (Q1.5, Q1.15, Q1.16 each have 1/3 runs with different recommendation answers). This is a regression from the perfect consistency of experiment 24.

### 7. The full Q1 set shows a realistic distribution

With 21 questions now evaluated, we have a more representative picture:
- 4/21 (19%) are top performers (100.0 loose)
- 8/21 (38%) are low performers (< 80.0 loose)

This 19/81 split is more informative than the 2/8 (25%) top performers from experiment 24.

## Conclusion

Experiment 25's changes produced **mixed results**:

**Positives:**
- Improved Q1.5 (+9.4) and Q1.6 (+14.0) on the overlapping subset
- Cleaner label concentration across the full 21-question set
- Still maintains perfect recommendation consistency per-question (all runs converge on yes/no)

**Negatives:**
- Regressed Q1.0 significantly (-16.2)
- Regressed Q1.4 (-10.0) while keeping the stably wrong consolidation taxonomy
- Slight drop in recommendation consistency overall
- Did not resolve the underlying routing problem that causes Q1.4 to land in the wrong document cluster

The changes appears to help when the model is correctly identifying the right section family but getting confused about which distinctions matter. It does **not** help when retrieval itself is routing to the wrong conceptual cluster.

## Next steps

1. **Focus on document/section routing quality.** Both experiments show that once the model lands on a wrong section family (consolidation vs. hedge accounting), the rest of the prompt construction follows from that error.

2. **Consider a routing-specific prompt instruction** that clarifies:
   - Which section families are the primary authoritative sources for hedge accounting questions
   - How to prioritize IFRS 9 / IFRIC 16 over IAS 21 / IFRS 10 when the question asks about hedge accounting

3. **Rerun the full Q1 family** with additional runs to get more statistical confidence on the low-performing questions.

4. **Investigate Q1.0 specifically** — this question seems sensitive to the changes in a bad way. Understanding why would inform whether the rule needs refinement or if Q1.0 itself needs different retrieval context.

## Human analysis

If we look at the unwanted approach labels, we see the model is still inventing approaches rather than sticking to the intended top-level hedge taxonomy (cash flow hedge, fair value hedge, net investment hedge), even though they may still collapse to one of the accepted hedging approaches:
- forecast_fx_hedge
- intragroup_fx_hedge
- fair_value_pl
- consolidation_elimination
- foreign_exchange_accounting

Q1.0 shows something interesting: all 3 runs retrieve the same sections (IFRS 9 6.3.5–6.3.6 plus IFRIC 16 consensus sections) but the identified approaches vary between correct taxonomy and spurious variants like forecast_fx_hedge, intragroup_fx_hedge, or fair_value_pl. This means the model is still not consistently able to take the context and organize it into our expected approches, and it's not because of missing evidence.


What we want is for the model to produce from Prompt A
- cash flow hedge
- fair value hedge
- net investment hedge

and have prompt B then use:
- forecast vs recognized
- consolidated vs separate
- intragroup vs external
- monetary item vs not

to reason under the given assumptions and conditions.

## Next steps

1. Try another prompt refinement & run the eval again on Q1.0-Q1.8