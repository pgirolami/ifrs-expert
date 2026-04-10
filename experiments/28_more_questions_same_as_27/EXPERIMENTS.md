# 2026-04-10

# Goal

Run the full Q1.0–Q1.7 subset with the structured prompt (from experiment 27) to see if the improvements generalize beyond the sanity-check questions. Compare results to experiment 26 (the best-performing experiment on this subset).

## What Changed from Experiment 26

**Restructured Prompt A with explicit multi-step workflow** (same changes as experiment 27):
- Step 1: Identify the primary accounting issue
- Step 2: Classify context into primary/supporting/peripheral authority
- Step 3: Identify treatment families
- Step 4: Map to peer approaches

The key instruction: "Use treatment families only as intermediate reasoning... Do not output both layers."

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 28
- [`generated_promptfoo_analysis_experiment_26_reference.md`](./generated_promptfoo_analysis_experiment_26_reference.md) — automated reference summary for experiment 26
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Method

Commands run:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 28_more_questions_same_as_27 \
  > experiments/28_more_questions_same_as_27/generated_promptfoo_analysis.md

uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 26_new_prompt_same_as_25 \
  > experiments/28_more_questions_same_as_27/generated_promptfoo_analysis_experiment_26_reference.md

uv run python experiments/analysis/generate_spurious_approaches_sections_matrix.py \
  --experiment 28_more_questions_same_as_27 \
  --provider 'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents'
```

## Automated analysis of Experiment 28

From [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md):

### Aggregate metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **72.3** | **73.6** |
| Approach stability | 0.5722 | 0.6076 |
| Applicability consistency | 0.6944 | 0.6944 |
| Recommendation consistency | 0.9167 | 0.9167 |
| Total questions | 8 | |
| Total runs | 24 | |

### Top and low performers

- **Top performers:** None (0/8 questions >= 95.0)
- **Low performers:** Q1.2, Q1.3, Q1.4 (3/8 questions < 80.0)

## My analysis

### 1. Results compared to experiment 26

| Question | Exp. 26 | Exp. 28 | Delta |
|----------|---------|---------|-------|
| Q1.0 | 100.0 | 92.2 | -7.8 |
| Q1.1 | — | 93.3 | new |
| Q1.2 | 59.2 | 100.0 | **+40.8** |
| Q1.3 | 95.0 | 62.8 | **-32.2** |
| Q1.4 | 78.0 | 35.0 | **-43.0** |
| Q1.5 | 88.3 | 92.2 | +3.9 |
| Q1.6 | 56.7 | 93.3 | **+36.6** |
| Q1.7 | 94.2 | 81.3 | -12.9 |

**Note:** Q1.2 score corrected from 28.3 to 100.0 after excluding the `needs_clarification` run (only 2 valid runs). With correction: 5 of 7 comparable questions improved.

Corrected aggregate scores:
- Exp. 26: 81.6 loose
- Exp. 28: 81.5 loose

**Roughly equivalent overall**, but with different winners/losers.

### 2. Q1.2: corrected after excluding `needs_clarification`

Q1.2 had one run return `needs_clarification`:
- **Run 1:** `needs_clarification` → excluded
- **Run 2 & 3:** Both returned `fair_value_hedge` (oui_sous_conditions), `cash_flow_hedge` (non), `net_investment_hedge` (non)

With only the 2 valid runs, Q1.2 achieves a perfect 100.0 score (1.0 approach stability, 1.0 applicability, 1.0 recommendation).

### 3. Q1.4: worst approach stability

Q1.4 had 0.0 approach stability. The three runs emitted completely different labels:

| Run | Labels |
|-----|--------|
| 1 | `intragroup_monetary_hedge`, `forecast_intragroup_hedge` |
| 2 | `fair_value_hedge`, `cash_flow_hedge`, `net_investment_hedge` |
| 3 | `fx_hedge_accounting` |

This is the worst possible outcome — zero consistency across runs. Experiment 26 had 0.37 stability on Q1.4.

### 4. Q1.6: major improvement

Q1.6 improved from 56.7 to 93.3 — the biggest positive delta. The structured prompt helps on this question type.

### 5. Q1.4: persistent instability

Q1.4 remains the most problematic question:

| Run | Labels |
|-----|--------|
| 1 | `intragroup_monetary_hedge`, `forecast_intragroup_hedge` |
| 2 | `fair_value_hedge`, `cash_flow_hedge`, `net_investment_hedge` |
| 3 | `fx_hedge_accounting` |

Zero approach stability. Experiment 26 had 0.37 stability on this question — still low, but not zero.

### 6. Label frequency comparison

| Label | Exp. 26 (Q1.0-Q1.7) | Exp. 28 (Q1.0-Q1.7) | Delta |
|-------|----------------------|----------------------|-------|
| net_investment_hedge | 17/21 = 81% | 18/21 = 86% | +1 |
| fair_value_hedge | 14/21 = 67% | 19/21 = 90% | +5 |
| cash_flow_hedge | 13/21 = 62% | 18/21 = 86% | +5 |
| hedge_accounting | 4/21 = 19% | 0/21 = 0% | **-4** |
| foreign_currency_accounting | 3/21 = 14% | 0/21 = 0% | **-3** |
| foreign_currency_translation | 5/21 = 24% | 0/21 = 0% | **-5** |
| consolidation_elimination | 2/21 = 10% | 0/21 = 0% | -2 |
| forecast_transaction_hedge | 2/21 = 10% | 0/21 = 0% | -2 |
| intragroup_monetary_hedge | 2/21 = 10% | 2/21 = 10% | 0 |
| consolidation_accounting | 1/21 = 5% | 0/21 = 0% | -1 |
| separate_financial_statements | 0/21 = 0% | 1/21 = 5% | +1 |
| fx_hedge_accounting | 0/21 = 0% | 1/21 = 5% | +1 |
| forecast_intragroup_hedge | 0/21 = 0% | 1/21 = 5% | +1 |

**Key observations:**
- The three core hedge labels are now more dominant (55 vs 44 total)
- `hedge_accounting`, `foreign_currency_accounting`, and `foreign_currency_translation` were eliminated
- New spurious labels appeared: `fx_hedge_accounting`, `forecast_intragroup_hedge`

## Conclusion

With Q1.2 corrected (excluding the `needs_clarification` run), experiment 28 is roughly equivalent to experiment 26:

| Metric | Exp. 26 | Exp. 28 (corrected) |
|--------|---------|---------------------|
| Average loose score | 81.6 | ~81.5 |
| Questions improved | — | 4 |
| Questions regressed | — | 3 |

**Key wins for structured prompt:**
- Q1.2: +40.8 (from 59.2 to 100.0)
- Q1.6: +36.6 (from 56.7 to 93.3)

**Key losses:**
- Q1.4: -43.0 (from 78.0 to 35.0) — persistent instability
- Q1.3: -32.2 (from 95.0 to 62.8)

The structured prompt is **not a clear win** over experiment 26. It helps some questions significantly but hurts others. Q1.4 remains the biggest problem across all experiments.

## Next steps

1. **Investigate Q1.4 specifically** — understanding why the structured prompt causes complete taxonomy collapse on this question.

2. **Add guidance against `needs_clarification`** — if the question is answerable with available context, the model should provide an answer.

3. **Consider reverting to experiment 26's prompt** for Q1.4-type questions, or investigate what's different about these questions.

## Human analysis

### Better coverage of the expected core approaches
The coverage of the 3 core approaches continues to increase: it is now 86-90%

### The spurious approach labels are now inside the "hedging" universe

The following list shows the approach labels that have disappeared. Apart from the first one, these were labels that described the standard non-hedged accounting approach from IAS 21. So it's good that these have disappeared
- forecast_transaction_hedge
- foreign_currency_accounting
- foreign_currency_translation
- consolidation_elimination
- consolidation_accounting

We also no longer see approaches labeled no_hedge_accounting, hedge_accounting. All these belonged to general accounting and not hedge accounting.

The following list shows the approach labels that have changed in frequency. There's only one and it's an alias for the fair-value hedge. The naming is that of the *treatment family* rather than the *top level accounting approach* though: the new prompt wasn't strong enough to steer the model in this case
- intragroup_monetary_hedge

The following list shows the approach labels that have appeared in experiment 28. Note that they appear together in the same runs
- fx_hedge_accounting (2 run) cites IFRS 9.6.3.5-6 and is an alias for the fair-value hedge
- forecast_intragroup_hedge (2 runs) is an alias for the cash-flow hedge

**Conclusion**:
- The model now succesfully identifies the hedging approaches rather than generic accounting labels but produces over-specific labels instead of the top-level approach labels we expect. 
- But it still sometimes outputting treatment families instead of the canonical peer approach labels. For example in Q1.2 we find the approach labels `forecast_intragroup_hedge` and `intragroup_monetary_hedge`; this leads us to hypothesis the model doing the intermediate reasoning step very literally and then failing to find the canonical approach labels.

### Where to spend time now

The question is whether we should try to 
1. narrow retrieval to eliminate IAS 21/IFRS 10 and hope the model gets less distracted by the generic account
2. improve the prompt again

Looking at the [data](./28_spurious_approaches_vs_sections_matrix.html), we see many runs that behave differently yet have very similar visible context patterns: heavy IFRS 9 scope / gains-and-losses / 6.3.5–6.3.6, plus some IFRIC 16, and occasionally other peripheral material. Since some of these runs do generate the expected result, we are hopeful that prompt behavior, not retrieval, is the lever that improved things.

The new prompt removed general accounting succesfully but preserves the “treatment family” wording rather than mapping it to the final top-level approach labels: the LLM is reasoning better, but has yet to normalize the approaches.

### Next steps
Change the prompt to constrain the LLM to map th approaches it finds on the 3 approaches we expecte and verify that works on the 8 questions from this experiment. This will help us make sure that the context given to the LLM is enough to map correctly and encourage us to continue fine-tuning the prompt with generic instructions that will transfer to other questions.