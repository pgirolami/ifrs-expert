# 2026-04-10

# Goal

Test whether extending the Composition rule with explicit guidance on how to handle qualifying labels (timing, scope, reporting-level, fact-pattern qualifiers) further improves upon experiment 25's results.

## What Changed from Experiment 25

**Extended the Composition rule section with additional guidance:**

```
If two candidate labels differ only because one adds a timing, scope, reporting-level, 
or fact-pattern qualifier to the other, prefer the broader top-level accounting treatment 
label unless the context clearly supports both as peer treatments
```

This addresses a remaining ambiguity from experiment 25: the Composition rule said not to treat overlays as peers with baselines, but it didn't explicitly address how to handle labels that differ only by a qualifying adjective (e.g., "forecast_transaction_hedge" vs "cash_flow_hedge").

All other settings remain identical to experiment 25 (same retrieval settings, same section expansion, same model).

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 26
- [`generated_promptfoo_analysis_experiment_25_reference.md`](./generated_promptfoo_analysis_experiment_25_reference.md) — automated reference summary for experiment 25
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Method

Commands run:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 26_new_prompt_same_as_25 \
  > experiments/26_new_prompt_same_as_25/generated_promptfoo_analysis.md

uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 25_new_prompt_same_as_24 \
  > experiments/26_new_prompt_same_as_25/generated_promptfoo_analysis_experiment_25_reference.md

uv run python experiments/analysis/generate_spurious_approaches_sections_matrix.py \
  --experiment 26_new_prompt_same_as_25 \
  --provider 'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents'
```

## Automated analysis of Experiment 26

From [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md):

### Aggregate metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **80.4** | **81.6** |
| Approach stability | 0.6373 | 0.6722 |
| Applicability consistency | 0.7698 | 0.7698 |
| Recommendation consistency | 1.0000 | 1.0000 |
| Total questions | 7 | |
| Total runs | 21 | |

### Top and low performers

- **Top performers:** `Q1.0`, `Q1.3`
- **Low performers:** `Q1.2`, `Q1.4`, `Q1.6`

## My analysis

### 1. Experiment 26 ran only Q1.0–Q1.7 (7 questions, 21 runs)

Unlike experiment 25 which ran all 21 Q1 questions, experiment 26 only ran the same subset as experiment 24. This makes direct comparison possible on all 7 questions.

### 2. Results are highly volatile across questions

| Question | Exp. 25 loose | Exp. 26 loose | Delta |
|----------|---------------|----------------|-------|
| Q1.0 | 59.3 | **100.0** | **+40.7** |
| Q1.2 | 100.0 | 59.2 | **-40.8** |
| Q1.3 | 75.5 | **95.0** | **+19.5** |
| Q1.4 | 90.0 | 78.0 | -12.0 |
| Q1.5 | 90.7 | 88.3 | -2.4 |
| Q1.6 | 90.7 | 56.7 | **-34.0** |
| Q1.7 | 62.6 | **94.2** | **+31.6** |

The deltas are very large in both directions:
- **Major improvements:** Q1.0 (+40.7), Q1.7 (+31.6), Q1.3 (+19.5)
- **Major regressions:** Q1.2 (-40.8), Q1.6 (-34.0)

This suggests the new qualifier guidance is either:
1. Highly sensitive to question phrasing
2. Interacting with the retrieval context in unpredictable ways
3. Making different mistakes than experiment 25

### 3. Q1.0: dramatic turnaround

Q1.0 went from the worst performer in experiment 25 (59.3) to a perfect 100.0. This is remarkable. Looking at the label frequency:

**Exp. 25 Q1.0:** `net_investment_hedge` (2), `hedge_accounting` (2), `fair_value_hedge` (1), `cash_flow_hedge` (1)

**Exp. 26 Q1.0:** `net_investment_hedge` (3), `fair_value_hedge` (3), `cash_flow_hedge` (3)

All 3 runs now emit the correct three-hedge taxonomy with perfect consistency. The additional qualifier guidance seems to have fixed whatever was causing the taxonomy fracture in Q1.0.

### 4. Q1.2: dramatic collapse

Q1.2 went from perfect (100.0) to 59.2. The label frequency shows:

**Exp. 25 Q1.2:** `net_investment_hedge` (3), `fair_value_hedge` (3), `cash_flow_hedge` (3) — all 3 runs perfect

**Exp. 26 Q1.2:** `net_investment_hedge` (2), `fair_value_hedge` (1), `cash_flow_hedge` (1), `forecast_transaction_hedge` (2), `intragroup_monetary_hedge` (2)

The new guidance appears to have caused the model to emit qualified labels like `forecast_transaction_hedge` and `intragroup_monetary_hedge` instead of collapsing to the broader `cash_flow_hedge`. This is the intended behavior for cases where context supports the specific label, but it hurt the stability score because now there's more variation.

### 5. Q1.7: strong improvement

Q1.7 went from 62.6 to 94.2. This question benefits from the same convergence effect as Q1.0 — the model now consistently names the right taxonomy.

### 6. Q1.6: major regression

Q1.6 went from 90.7 to 56.7. This is puzzling. The label frequency shows:

**Exp. 26 Q1.6:** `net_investment_hedge` (3), `foreign_currency_accounting` (2), `cash_flow_hedge` (1), `fair_value_hedge` (1), `hedge_accounting` (1), `foreign_currency_hedge` (1), `monetary_item_translation` (1)

Too many distinct labels are appearing. The qualifier guidance may be causing the model to be *too* granular, treating different qualifying circumstances as requiring different labels.

### 7. The spurious labels changed in character

**Exp. 25 spurious labels:** `hedge_accounting`, `foreign_currency_accounting`, `foreign_currency_translation`

**Exp. 26 spurious labels:** `foreign_currency_translation`, `hedge_accounting`, `foreign_currency_accounting`, `consolidation_elimination`, `forecast_transaction_hedge`, `intragroup_monetary_hedge`

The new qualifying labels `forecast_transaction_hedge` and `intragroup_monetary_hedge` appear in Exp. 26 but not Exp. 25. These are the intended targets of the new guidance — labels that add a qualifier to a broader treatment. But the guidance says to prefer the broader unless context supports the specific — which may explain why these appear but are still counted as spurious.

### 8. Label frequency comparison on overlapping subset

| Label | Exp. 25 (Q1.0-Q1.7) | Exp. 26 (Q1.0-Q1.7) | Delta |
|-------|----------------------|----------------------|-------|
| net_investment_hedge | 16 | 17 | +1 |
| fair_value_hedge | 12 | 14 | +2 |
| cash_flow_hedge | 12 | 13 | +1 |
| hedge_accounting | 8 | 4 | **-4** |
| foreign_currency_accounting | 5 | 3 | -2 |
| foreign_currency_translation | 5 | 5 | 0 |
| consolidation_accounting | 2 | 1 | -1 |
| separate_financials | 2 | 0 | **-2** |
| consolidation_elimination | 0 | 2 | +2 |
| forecast_transaction_hedge | 0 | 2 | +2 |
| intragroup_monetary_hedge | 0 | 2 | +2 |

Key observations:
- `hedge_accounting` (generic) dropped further from 8 to 4 — the new guidance reduced it even more
- `separate_financials` dropped to 0 — excellent
- New qualifying labels appeared: `forecast_transaction_hedge`, `intragroup_monetary_hedge`, `consolidation_elimination`

The overall trend is toward more specific but still within the hedge accounting family.

## Conclusion

Experiment 26's qualifier guidance produced **extreme volatility**:

**Major improvements:**
- Q1.0: +40.7 (worst → perfect)
- Q1.7: +31.6 (low performer → top performer)
- Q1.3: +19.5 (low → top performer)

**Major regressions:**
- Q1.2: -40.8 (perfect → low performer)
- Q1.6: -34.0 (top performer → low performer)

**Interpretation:**

The new guidance appears to work well for questions where the model was previously "fracturing" the taxonomy (Q1.0, Q1.7) but causes problems for questions where the model was already stable (Q1.2, Q1.6) by introducing excessive granularity.

The fundamental tension is:
- When the model correctly identifies the right treatment but adds a qualifier, the guidance says to prefer the broader label
- But if the model then *doesn't* use the qualifier, it may be under-specifying the treatment
- The guidance doesn't clearly resolve this when retrieval context includes qualifying details

**Overall:** The aggregate scores are similar (Exp 25: 83.4 loose, Exp 26: 81.6 loose), suggesting the guidance shifts which questions perform well rather than improving overall performance.

## Conclusion

The qualifier guidance is addressing the right concept — distinguishing between top-level treatments and their scoped variants. But the implementation reveals a deeper problem:

When the model sees "forecast intragroup monetary item hedge" in the context, should it emit:
- `cash_flow_hedge` (broader, matches the base model)
- `forecast_transaction_hedge` (specific, matches the qualifier)

The current guidance says prefer broader unless context supports both as peer treatments. But this creates an ambiguity: "supports" is not well-defined. Does seeing the term in context mean "supports"? Or does it require a specific treatment path in the standard?

A possible refinement:
```
When a qualified label and its broader counterpart both appear relevant, prefer the broader 
label unless the accounting standard explicitly provides different treatment paths for the 
qualifier dimension. In other words, the qualifier must affect the accounting outcome, 
not just the eligibility conditions.
```

## Next steps

1. **Investigate Q1.0 vs Q1.2 specifically** — understanding what makes Q1.0 benefit while Q1.2 collapses would clarify when the qualifier guidance helps vs hurts.

2. **Consider a hybrid approach:**
   - Keep the qualifier guidance as a conditional: "only apply when the broader label would be misleading"
   - Add examples of when to preserve the qualifier

3. **Rerun with full Q1 set** to see if the pattern holds across more questions.

4. **Review the spurious label list** — the new qualifying labels (`forecast_transaction_hedge`, `intragroup_monetary_hedge`) may need to be added to the canonical mapping to reduce their impact on stability scores.

