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

# Next steps
It would be interesting to feed the context and cross it with the other question to confirm whether the retrieval is the issue... it must be because Q1.0 used to work.
