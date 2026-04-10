# 2026-04-10

# Goal

Verify the conclusion from experiment 27 that we should continue working on the prompt because retrieval is sufficient to find the relevant approaches.

## What Changed from Experiment 26

Added to prompt A clear rules for returning on of the 3 top-level approaches

```
Final-label mapping rule for this diagnostic experiment:
- For hedge-accounting questions, the final emitted approaches must be canonical peer IFRS hedge-accounting model labels.
- If your intermediate reasoning identifies a recognized-item hedge family, emit the canonical top-level hedge model label, not a fact-pattern-specific variant.
- If your intermediate reasoning identifies a forecast-transaction hedge family, emit the canonical top-level hedge model label, not a fact-pattern-specific variant.
- If your intermediate reasoning identifies a net-investment hedge family, emit the canonical top-level hedge model label.
- For hedge-accounting questions, prefer these canonical final labels when applicable:
  - fair_value_hedge
  - cash_flow_hedge
  - net_investment_hedge
- Do not emit final labels that merely restate the identified exposure or qualifier, such as:
  - intragroup_monetary_hedge
  - forecast_intragroup_hedge
  - intragroup_fx_hedge
  - fx_hedge_accounting
```

All other settings remain identical to experiment 27 (same retrieval settings, same section expansion, same model).

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 28
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Human analysis

### Uneven coverage of the expected core approaches
The coverage of "fair_value_hedge" (the applicable approach) increased to 100% while the rest decreased. There were no spurious approaches, as expected.

| Label | Exp. 29 (Q1.0-Q1.7) | Exp. 28 (Q1.0-Q1.7) |
|-------|----------------------|----------------------|
| net_investment_hedge | 16/23 = 70% | 18/21 = 86% |
| fair_value_hedge | 23/23 = 100% | 19/21 = 90% |
| cash_flow_hedge | 17/23 = 74% | 18/21 = 86% |

Other remarks
- On Q1.5, only fair_value_hedge is identified consistently: cash_flow_hedge is never returned and fair_value_hedge is returned only once
- cash_flow_hedge and net_investment_hedge each appear as many times as the other in all questions but Q1.4 and Q1.5
    - Q1.4 is the only question that retrieves chunks from IFRS 10 and IAS 24 in the experiment
    - Q1.5 is the only question where the operating chunks in IFRS 9 (6.3.5-6) have a very high score of 0.63


### Conclusion
The key insights from this experiment:
 - the applicable approach is always returned
 - the non-applicable approaches are returned inconsistently, even across runs for a given question

We posit Prompt A may still be deciding on the most applicable approach and returning only that, rather than getting lost in the unimportant documents (IAS 24, IFRS 10). But that is prompt B's job.

Reasons this could be:
- we're asking for the model to list *assumptions* so it may be trying to find applicability because of that. This is a left-over from when there was a single prompt.
- we don't guardrail it enough from doing that

### Next steps

Update prompt to handle the conclusion & rerun experiment