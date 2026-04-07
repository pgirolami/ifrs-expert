# 2026-04-08

# Goal
Get a baseline if the Q1 family after ingesting **all** free IFRS documentation on ifrs.org to evaluate the impact of a much larger context.

# Analysis
The analysis is succint and qualitative because the full experiment didn't run because of usage limits.

## Q1.0
There is a very strong regression on this question. The approaches identified in step A are completely broken:
- consolidation_accounting (x2)
- hedge_accounting (x2)
- ias39_hedging
- foreign_currency
- foreign_currency_translation
- consolidation_accounting

Gone are cash_flow_hedge, fair_value_hedge and net_investmenet_hedge !

This may indicate that the LLM is overwhelmed by the amount of information and unable to correctly identify the relevant approaches all relate to hedging rather than consolidation or foreign_currency.

The `ias39_hedging` approach is also interesting because IAS 39 and IFRS 9 are closely related: it is likely we need to change the prompt to better handle overlapping documents.

## Q1.1
On this question, both runs correctly identified only the 3 expected approaches. So, even in the face of a huge context, the LLM was still able to identify the correct approaches. Therefore it is likely that we have in fact, a retrieval issue on the first question.
We should compare what chunks were returned for each question

# Retrieval comparison
| Question | Correct approaches identified | Number of chunks in context | Number of documents | Includes IFRIC 16 | Includes IFRS 3.6.3 |
| --- | --- | --- | --- | --- | --- |
| Q1.0 | No | 2207 | 64 | Yes : 10-18B & AG1-AG15 | Yes : 6.3.1-6.3.6 as well as 6.4.1, 6.5.x, 6.6x, 6.7.x, 6.9.x, 6.1x, 6.10.x, 6.2.x and others|
| Q1.1 | Yes | 2157 | 59 | Yes : 10-18B & AG1-AG15 | Yes : 6.3.1-6.3.6 as well as 6.4.1, 6.5.x, 6.6x, 6.7.x, 6.9.x, 6.1x, 6.10.x, 6.2.x and others|

The only difference on IFRS 9 is that Q1.1 is not given all the chunks in section "Presentation of hedging instrument gains or losses": ifrs9-B6.6.13, ifrs9-B6.6.14, ifrs9-B6.6.15 and ifrs9-B6.6.16.

We fed the context of one question to the other question to confirm whether the retrieval is the issue and the results were surprising
- with the chunks retrieved using Q1.0, the output of prompt A became correct when the question given was Q1.1
- with the chunks retrieved using Q1.1, the output of prompt A became correct with question 1.0


## Using the context retrieved by Q1.0
<details>
<summary>The output of the prompt with question Q1.1 becomes correct !</summary>

```json
{
  "status": "pass",
  "assumptions": [
    "The intragroup dividend receivable creates a foreign-currency monetary item in at least one group entity.",
    "The question is about hedge accounting possibilities in consolidated financial statements for the foreign-exchange risk element."
  ],
  "approaches": [
    {
      "id": "approach_1",
      "label": "Fair value hedge accounting",
      "normalized_label": "fair_value_hedge",
      "rationale_for_inclusion": "IFRS 9 identifies fair value hedge as a distinct hedge accounting model for hedging exposure to changes in fair value attributable to a particular risk, including foreign currency risk."
    },
    {
      "id": "approach_2",
      "label": "Cash flow hedge accounting",
      "normalized_label": "cash_flow_hedge",
      "rationale_for_inclusion": "IFRS 9 identifies cash flow hedge as a distinct hedge accounting model for hedging variability in cash flows attributable to a particular risk, including foreign currency risk."
    },
    {
      "id": "approach_3",
      "label": "Hedge of a net investment in a foreign operation",
      "normalized_label": "net_investment_hedge",
      "rationale_for_inclusion": "IFRS 9 and IAS 21 identify hedge accounting for a net investment in a foreign operation as a separate top-level hedge accounting model for foreign exchange risk."
    },
    {
      "id": "approach_4",
      "label": "Foreign currency accounting without hedge accounting",
      "normalized_label": "foreign_currency_translation",
      "rationale_for_inclusion": "IAS 21 provides the baseline accounting for foreign-currency monetary items and intragroup monetary items in consolidated financial statements when hedge accounting is not applied."
    }
  ]
}
```
</details>
but 

<details>
<summary>the output of the prompt with question Q1.0 continues to be bad!</summary>

```json
{
  "status": "pass",
  "assumptions": [
    "The question concerns IFRS consolidated financial statements.",
    "The intragroup dividend has given rise to a recognised intragroup receivable before consolidation eliminations.",
    "The issue is limited to accounting models relevant to foreign exchange effects and consolidation treatment of that intragroup balance."
  ],
  "approaches": [
    {
      "id": "approach_1",
      "label": "Hedge accounting",
      "normalized_label": "hedge_accounting",
      "rationale_for_inclusion": "The context includes IFRS 9 and IAS 39 hedge accounting models for foreign currency risk, including hedged items and hedging instruments in consolidated financial statements."
    },
    {
      "id": "approach_2",
      "label": "Foreign currency translation",
      "normalized_label": "foreign_currency_translation",
      "rationale_for_inclusion": "The context includes IAS 21 accounting for foreign currency monetary items and exchange differences, which is the baseline model for an FX-denominated receivable."
    },
    {
      "id": "approach_3",
      "label": "Consolidation elimination",
      "normalized_label": "consolidation_elimination",
      "rationale_for_inclusion": "The context includes IFRS 10 requirements to eliminate intragroup assets, liabilities, income and expenses in consolidated financial statements, which is directly relevant to an intragroup dividend receivable."
    }
  ]
}
```
</details>


## Using the context retrieved by  Q1.1
<details>
<summary>The output of the prompt with question Q1.0 becomes correct !</summary>

```json
{
  "status": "pass",
  "assumptions": [
    "The issue concerns IFRS consolidated financial statements and a foreign-currency-denominated intragroup dividend receivable that has been recognised before settlement.",
    "The question is about the accounting model potentially applicable to the FX exposure arising from that recognised amount."
  ],
  "approaches": [
    {
      "id": "approach_1",
      "label": "Cash flow hedge accounting",
      "normalized_label": "cash_flow_hedge",
      "rationale_for_inclusion": "IFRS 9 identifies cash flow hedges as a distinct hedge accounting model for exposures to variability in cash flows that could affect profit or loss."
    },
    {
      "id": "approach_2",
      "label": "Fair value hedge accounting",
      "normalized_label": "fair_value_hedge",
      "rationale_for_inclusion": "IFRS 9 identifies fair value hedges as a distinct hedge accounting model for exposures to changes in fair value of recognised assets or liabilities that could affect profit or loss."
    },
    {
      "id": "approach_3",
      "label": "Net investment hedge accounting",
      "normalized_label": "net_investment_hedge",
      "rationale_for_inclusion": "IFRS 9 and IFRIC 16 identify hedges of a net investment in a foreign operation as a separate hedge accounting model relevant to foreign currency exposures in consolidated financial statements."
    },
    {
      "id": "approach_4",
      "label": "Foreign currency transaction accounting",
      "normalized_label": "foreign_currency_translation",
      "rationale_for_inclusion": "IAS 21 provides the default accounting model for foreign-currency monetary items, including recognising exchange differences in profit or loss unless another IFRS treatment applies."
    }
  ]
}
```
</details>
and 

<details>
<summary>the output of the prompt with question Q1.1 continues to be perfect!</summary>

```json
{
  "status": "pass",
  "assumptions": [
    "The issue concerns foreign exchange risk on an intragroup dividend receivable in consolidated financial statements.",
    "The question asks for IFRS hedge accounting models potentially relevant to foreign exchange exposure in consolidation."
  ],
  "approaches": [
    {
      "id": "approach_1",
      "label": "Fair value hedge",
      "normalized_label": "fair_value_hedge",
      "rationale_for_inclusion": "IFRS 9 identifies fair value hedge as a distinct hedge accounting model for exposure to changes in fair value attributable to a particular risk."
    },
    {
      "id": "approach_2",
      "label": "Cash flow hedge",
      "normalized_label": "cash_flow_hedge",
      "rationale_for_inclusion": "IFRS 9 identifies cash flow hedge as a separate hedge accounting model for exposure to variability in cash flows attributable to a particular risk, including foreign currency risk."
    },
    {
      "id": "approach_3",
      "label": "Hedge of a net investment in a foreign operation",
      "normalized_label": "net_investment_hedge",
      "rationale_for_inclusion": "IFRS 9 and IFRIC 16 identify hedge of a net investment in a foreign operation as a separate hedge accounting model specifically for foreign currency exposure in consolidation."
    }
  ]
}
```
</details>

## Comparison conclusion
The recap of this analysis is the following
| Question \ Context | Q1.0 | Q1.1 |
| --- | --- | --- |
| Q1.0 | ❌ Bad | ✅ Good |
| Q1.1 | ✅ Good | ✅ Good |

It looks like there is a particular negative interaction between the question Q1.0 and the context retrieved with Q1.0.

# Prompt sizes
The sizes of the prompt are becoming problematic:
| Question | Prompt | Size in bytes |
| --- | --- | --- |
| Q1.0 | A | 1.4 M | 
| Q1.0 | B | 1.4 M |
| Q1.1 | A | 1.4 M | 
| Q1.1 | B | 1.4 M |

Some LLMs won't support prompts this size because once tokenized, they will be larger than the context window. And that's not even considering the cost of prompting.

From inspection, a lot of sections returned are not that relevant.

# Next steps
- work on reducing the amount of sections returned