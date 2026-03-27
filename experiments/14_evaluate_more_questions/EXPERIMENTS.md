# 2026-03-27

# Goal

Evaluate whether correctness and stability achieved on the initial question transfers to practical questions still related to IFRS 9 found on https://ifrscommunity.com

# Qualitative analysis of results with SME

In this section, we evaluated retrieval quality and answer correctness via another LLM. We made sure the judge LLM grounded its answer through web searches of normative documents. 
   1. are the responses equivalent & correct ?
   2. was the correct achievable through the grounding context provided. If not, what was missing ?
       3. if yes, can the prompts be improved to improve the answer to be correct ?

## Question 5

[Question 5](../00_QUESTIONS/Q5/Q5.0.txt) opens with a lot of context and ends with a precise question scoped as an alternative:
```
In Q2, should the bank:
- Treat the hedge designation on a cumulative basis, such that the remaining hedgeable amount becomes 70m (i.e., 150m - 80m), or
- Treat the incremental 50m increase as a separate forecast transaction / separate hedge layer, requiring separate designation and documentation?
```

### Retrieval

| Section Path | Score | Range (±5 in DB order) |
|--------------|-------|------------------------|
| 6.5.11 | 0.7228 | 6.5.6 - 6.5.16 |
| 6.5.12 | 0.6917 | 6.5.7 - 6.6.1 |
| 6.9.9 | 0.6892 | 6.9.4 - 6.10.2 |
| B6.5.2 | 0.6917 | B6.4.16 - B6.5.7 |
| B6.6.9 | 0.7282 | B6.6.4 - B6.6.14 |
| 3 | 0.6727 | 1 - 8 |
| 5 | 0.6732 | 1 - 10 |
| 13 | 0.6367 | 8 - 18 |
| 14 | 0.6384 | 9 - 18A |
| 16 | 0.6349 | 11 - 19 | |

### Answers
The recommendations given by the assistant were
|  Run |  Recommendation | Justification |
| ---- | --------------- | ------------- |
| 1 | Oui sous conditions | Dans votre cas, les 80m désignés en P1 restent la relation couverte. Le passage du solde prévu à 150m en P2 ne transforme pas automatiquement la désignation en un reliquat cumulatif de 70m ; l'augmentation de 50m doit être explicitement désignée et documentée comme tranche additionnelle, sauf rebalancement formel limité au maintien du hedge ratio. |
| 2 | Oui sous conditions | La couverture désignée en T1 reste limitée à 80 m tant qu'elle n'est pas modifiée formellement. En pratique, l'augmentation de 50 m doit être désignée séparément comme nouvelle couche de flux, sauf si la banque rééquilibre valablement la relation existante et met à jour sa documentation en T2. |
| 3 | Oui | Dans ces faits, la relation désignée en Q1 reste 80m. Le « 70m restant » n'est qu'un solde économique non couvert; les 50m additionnels de Q2 ne s'intègrent pas automatiquement à la désignation initiale et doivent être formellement désignés/documentés s'ils sont ajoutés à la couverture. |

The approaches evaluated were:

| Run | cash_flow_hedge | hedge_rebalancing | hedge_discontinuation |
| ---- | --------------- | ----------------- | --------------------- |
| 1 | oui_sous_conditions | - | - |
| 2 | oui | oui_sous_conditions | non |
| 3 | oui | - | - |

### LLM-as-a-judge
An LLM was used to judge these recommendations and it found them mostly equivalent. However, it criticized them for being
>slightly incomplete because IFRS 9 allows that formal inclusion either as a separate designation or, where appropriate, through rebalancing of the existing relationship, which effectively creates an added layer within the continuing relationship.

When given the full markdown document, the judge realized the `separate designtation` and `rebalancing` were in fact found in the responses (although not as clearly in each run). It indicated that
>If your question is: are they correct?
>
>Run 1: broadly correct
>Run 2: correct and best framed
>Run 3: broadly correct on outcome, but less complete and less well supported

and it found that the most important point missing was the following
>Rebalancing is not a generic way to absorb new forecast volume. It is allowed only to adjust designated quantities of an already existing hedging relationship for the purpose of maintaining a qualifying hedge ratio, and the added volume is then treated from the rebalancing date as an added layer, not as an automatic recomputation of the original designation.

It also pointed out that all answers were missing section 6.4.1(b) so this was a retrieval issue. It is worth pointing out the among the sections retrieved, some of them reference 6.4.1 so **a smarter expansion algorithm would solve this issue.**

## Question 6

[Question 6](../00_QUESTIONS/Q6/Q6.0.txt)
```
I have a question in relation to the accounting for a profit participating loan liability. For instance, a limited recourse loan where principal is payable on maturity but the interest on such loan is linked to profits i.e. based on a priority of payments if there is residual profits that is the interest expense on the loan for the period.

Now, per my understanding I believe this amounts to the case for an embedded derivative i.e. the host contract being principal payments and interest being paid only if there is residual profit left per the waterfall priority of payments. Thus, the loan liability should be held at fair value through profit or loss.

I have come across many opinions for it to be accounted on an amortised cost basis at EIR, however, given the payments of interest are variable and based on if there is residual profit left, would it be accounted for at FVTPL or amortised cost.
```

### Retrieval

| Section Path | Score | Range (±5 in DB order) |
|--------------|-------|------------------------|
| 3.2.17 | 0.6499 | 3.2.12 - 3.2.22 |
| 4.2.1 | 0.6934 | 4.1.2 - 4.3.4 |
| 5.7.2 | 0.6495 | 5.6.5 - 5.7.7 |
| B4.3.8 | 0.6545 | B4.3.3 - B4.4.1 |
| B5.4.6 | 0.6611 | B5.4.1 - B5.5.2 |
| 9 | 0.5514 | 4 - 14 |
| 17 | 0.5587 | 12 - AG1 |
| AG7 | 0.5500 | AG2 - AG12 |
| AG8 | 0.5456 | AG3 - AG13 |
| AG14 | 0.5511 | AG9 - AG15 |

### Answers
The recommendations given by the assistant were:
| Run | Recommendation | Justification |
| ---- | --------------- | ------------- |
| 1 | Oui | Dans les faits décrits, le traitement recommandé est le coût amorti. IFRS 9 pose le coût amorti comme règle générale pour les passifs financiers, et la clause d'intérêt liée aux profits résiduels ne conduit pas ici, sur la base du texte fourni, à une séparation obligatoire d'un dérivé incorporé; la JVPR ne serait envisageable que par désignation initiale. |
| 2 | Oui | Dans cette situation, le traitement le plus étayé est le coût amorti. IFRS 9 mesure par défaut les passifs financiers au coût amorti, sauf désignation irrévocable à la JVPR lors de la comptabilisation initiale. Sur les faits fournis, la clause de rémunération variable ne suffit pas à imposer une mesure à la JVPR. |
| 3 | Oui sous conditions | Au vu des faits fournis, la dette n'est pas automatiquement comptabilisée à la juste valeur par résultat. Cependant, si une désignation irrévocable à la JVPR existe dès l'origine, ce traitement s'applique. À défaut, le coût amorti est le traitement de base. |

The approaches evaluated were:

| Run | amortised_cost | fair_value_profit_loss | fair_value_pl | separated_embedded_derivative | embedded_derivative_separation |
| ---- | --------------- | ---------------------- | -------------- | ----------------------------- | ------------------------------ |
| 1 | oui | oui_sous_conditions | - | non | - |
| 2 | oui | non | non | - | non |
| 3 | oui_sous_conditions | non | - | - | oui_sous_conditions |

### LLM-as-a-judge

#### Were all 3 responses equivalent
>No.
>
>They are not equivalent, and only part of them is correct.
>
>The closest to a defensible IFRS 9 answer is Answer 3, but it is still incomplete. Answers 1 and 2 are too categorical on the embedded-derivative point.
>Answers 1 and 2 say, in substance, that the instrument should be at amortised cost and that the profit-linked return does not give rise to a separable embedded derivative. They are broadly equivalent to each other.
>
>Answer 3 says something different: it agrees that the whole liability is not automatically FVTPL, but it leaves open that the profit-participation clause might need to be separated if paragraph 4.3.3 is met. That is materially different from Answers 1 and 2.

#### Where all 3 responses are correct
1. Point #1
   >the whole liability being at FVTPL because there is an embedded derivative is not right under IFRS 9.
   >
   >Even if there is a separable embedded derivative, the normal consequence is split accounting: host at amortised cost, embedded derivative at FVTPL, unless the entity elected the fair value option for the entire hybrid instrument at inception or cannot reliably separate the derivative.

2. Point #2
   >amortised cost with EIR can indeed accommodate variable/contingent cash flows, because IFRS 9’s EIR definition is based on estimated cash flows and B5.4.6 requires remeasurement for revised estimates

#### Incorrectness: responses are too definite
>Answers 1 and 2 effectively say the embedded-derivative analysis “fails” because the profit measure is a variable specific to a party to the contract, and therefore is not a derivative. That is too definite.
>
>There is official IFRIC material on contracts indexed to an entity’s own EBITDA or revenue saying it was unclear under the standard whether revenue or EBITDA are financial or non-financial variables. IFRIC noted that if they are non-financial, they are plainly specific to a party; but it also noted the standard was unclear on whether revenue/EBITDA are financial or non-financial in the first place.
>
>So, on the facts you gave, it is too strong to say categorically that the profit-linked return cannot be a derivative simply because it references the borrower’s profits. The standards material supports a more cautious conclusion: the issue needs a careful derivative-definition analysis, and there is some interpretive uncertainty around issuer-performance metrics.


It is hard to diagnose here whether this is a retrieval issue (we are probably missing IFRIC documents) or a reasoning issue: was the LLM too definitive based on the retrieved results ?

More investigation is required.

#### Could the correct response be inferred from the grounding context ?
>From the grounding context, you can infer the core measurement framework, but you cannot fully justify the strongest parts of the earlier answer.
>
>You cannot infer with confidence, from this context alone, that the profit-participation feature definitely is not a separable embedded derivative.
>
>The issue is:
> - the rule is present,
> - but the conclusion is not mechanically determined by the text for this precise fact pattern.

#### Additional documents that would have helped get the correct answer

## Question 7

[Question 7](../00_QUESTIONS/Q7/Q7.0.txt)
```
I would appreciate your help with the accounting for a forward foreign exchange contract under IFRS 9.

Background:

We have a forward FX contract (not designated as a hedge) that is correctly classified at Fair Value Through Profit or Loss (FVTPL).

The contract started in June 2025.

We have been remeasuring it to fair value at each period-end, posting entries like the one below for June 2025:

30 June 2025:

Dr. Financial Asset - Derivative

Cr. Derivative Fair Value Gain (in P&L)

Situation:
The contract is scheduled to mature and be settled on 20 December 2025. I need to confirm the correct final journal entries on the settlement date.

My Question:
What are the specific journal entries to record the final fair value remeasurement and the physical settlement of the contract? Specifically, how do we derecognize the derivative asset and record the actual currency exchange?
```

The recommendations given by the assistant were:
| Run | Recommendation | Justification |
| ---- | --------------- | ------------- |
| 1 | Oui | Dans cette situation, le traitement applicable est celui du dérivé à la juste valeur par résultat. Il faut d'abord comptabiliser la dernière variation de juste valeur au 20 décembre 2025, puis solder l'actif ou le passif dérivé lors du règlement physique, sans OCI ni comptabilité de couverture. |
| 2 | Oui | Oui. Dans cette situation, le traitement applicable est la juste valeur par résultat: il faut comptabiliser la dernière variation de juste valeur au 20 décembre 2025, puis solder l'actif ou le passif dérivé lors du règlement physique, sans OCI ni comptabilité de couverture. |
| 3 | Oui | Dans cette situation, seul le traitement à la juste valeur par résultat s'applique. Il faut enregistrer la dernière variation de juste valeur au 20 décembre 2025, puis solder l'actif ou le passif dérivé lors du règlement physique, sans OCI ni comptabilité de couverture. |

The approaches evaluated were:

| Run | fair_value_profit_loss | hedge_accounting | settlement_date_accounting |
| ---- | ---------------------- | ---------------- | -------------------------- |
| 1 | oui | non | - |
| 2 | oui | non | non |
| 3 | oui | non | - |

### Retrieval

| Section Path | Score | Range (±5 in DB order) |
|--------------|-------|------------------------|
| 5.7.2 | 0.6426 | 5.6.5 - 5.7.7 |
| 5.7.4 | 0.6430 | 5.6.7 - 5.7.9 |
| B5.7.2A | 0.6364 | B5.6.1 - B5.7.7 |
| B6.5.36 | 0.6740 | B6.5.31 - B6.6.2 |
| B6.6.9 | 0.6372 | B6.6.4 - B6.6.14 |
| 3 | 0.6285 | 1 - 8 |
| 5 | 0.6203 | 1 - 10 |
| 6 | 0.6374 | 1 - 11 |
| 16 | 0.6480 | 11 - 19 |
| 17 | 0.5919 | 12 - AG1 |

The answer to this question is problematic because the assistant gave an answer indicating which approach was acceptable when, in fact, the user was asking for journal entries.
>(...) What are the specific journal entries to record (...)

The prompt's guardrails probably prevented the LLM from answering at a more precise level than the "approaches". **This is a failure worth investigating after building an eval harness with the existing acceptable questions & answers.**


## Question 8

[Question 8](../00_QUESTIONS/Q8/Q8.0.txt)
```
When a financial asset becomes credit-impaired after origination (i.e. moves to Stage 3 under IFRS 9), the manner of recognizing interest income changes. Initially, while the asset is performing (Stage 1 or 2), interest is calculated on the gross carrying amount using the effective interest rate (EIR) determined at origination.

However, once the asset is assessed as credit-impaired, IFRS 9 paragraph 5.4.1 (b) requires that interest income be recognized by applying the EIR (which I believe is not credit adjusted EIR because that bit specially applies to purchased or originated credit impaired financial assets) to the amortized cost of the asset that is, the gross carrying amount less the loss allowance (expected credit loss).

Also, another matter is the unwinding of the discount on the loss allowance as "unwinding of ECL" as interest income for credit impaired loans, which represents the time-value effect on expected recoveries. This unwinding is separate from any changes in the loss allowance due to revised expectations. The complexity for me lies in keeping these two movements distinct. I find it difficult to understand whether the unwinding of ECL is different from the increase or decrease in the total ECL allowance on the reporting date.

Another area of confusion is whether "unwinding of ECL" also applies to performing loans and how this interacts with the presentation of income "at net" when Stage 2 or Stage 3 interest recognition is applied. Because it is not clear to me from IFRS 9 paragraphs whether the interest income calculation methodology for credit impaired loans results in only presentation changes or not.
```

The recommendations given by the assistant were:
| Run | Recommendation | Justification |
| ---- | --------------- | ------------- |
| 1 | Oui | Oui. Dans votre cas, l'intérêt en Stage 3 se calcule sur le coût amorti avec le taux effectif d'origine, et non avec un taux crédit-ajusté réservé aux actifs POCI. L'« unwinding » vient de l'actualisation de l'ECL et doit être distingué des réestimations de l'ECL dues aux nouvelles attentes de recouvrement. |
| 2 | Oui | Dans cette situation, il faut combiner la méthode du TIE et le modèle ECL: l'intérêt d'un actif devenu déprécié après l'origination se calcule sur le coût amorti avec le TIE d'origine; l'effet temps de l'ECL doit être distingué de sa réestimation. |
| 3 | Oui sous conditions | Oui, pour un actif devenu déprécié après l'origination et non POCI, les deux traitements s'appliquent: le TIE sur le coût amorti pour l'intérêt, et l'effet temps d'actualisation sur l'ECL en résultat. La distinction est importante pour éviter de comptabiliser deux fois le même effet. |

The approaches evaluated were:

| Run | effective_interest_method | expected_credit_losses | credit_adjusted_eir |
| ---- | ------------------------- | ---------------------- | ------------------- |
| 1 | oui | oui | - |
| 2 | oui | oui | non |
| 3 | oui_sous_conditions | oui | - |

### Retrieval

| Section Path | Score | Range (±5 in DB order) |
|--------------|-------|------------------------|
| 7.3.2 | 0.7297 | 7.2.46 - B2.4 |
| B5.4.7 | 0.7083 | B5.4.2 - B5.5.3 |
| B5.5.33 | 0.7256 | B5.5.28 - B5.5.38 |
| B5.5.47 | 0.7133 | B5.5.42 - B5.5.52 |
| B5.6.1 | 0.7102 | B5.5.51 - B5.7.2A |
| 3 | 0.6270 | 1 - 8 |
| 5 | 0.5840 | 1 - 10 |
| 6 | 0.6471 | 1 - 11 |
| 16 | 0.5999 | 11 - 19 |
| AG8 | 0.5847 | AG3 - AG13 |

## Question 9

[Question 9](../00_QUESTIONS/Q9/Q9.0.txt)
```
Company A has received an unsecured, interest free loan from one of its shareholders. The loan has no fixed repayment period. How do I recognize its fair value by measuring the present value of all future cashflows from this instrument.
```

The recommendations given by the assistant were:
| Run | Recommendation | Justification |
| ---- | --------------- | ------------- |
| 1 | Oui sous conditions | IFRS 9 permet de comptabiliser initialement un prêt sans intérêt / hors marché à la juste valeur par actualisation des flux futurs au taux de marché d'un instrument similaire. Ici, l'absence d'échéance fixe impose de documenter l'hypothèse de remboursement; si la juste valeur diffère du montant reçu et n'est pas étayée uniquement par des données observables, l'écart est différé. |
| 2 | Oui sous conditions | Dans cette situation, l'approche pertinente est la juste valeur initiale plutôt que le simple prix de transaction. Pour un prêt sans intérêt consenti par un actionnaire, il faut déterminier la juste valeur par actualisation des flux de remboursement au taux de marché d'un instrument similaire. Si cette juste valeur diffère du montant reçu et n'est pas entièrement observable, l'écart est différé. |
| 3 | Oui sous conditions | L'approche pertinente est l'évaluation initiale à la juste valeur par actualisation pour un prêt sans échéance fixe. Si la juste valeur diffère du montant reçu et que l'évaluation repose sur des hypothèses non observables, l'écart doit être différé selon IFRS 9 B5.1.2A. |

The approaches evaluated were:

| Run | transaction_price_recognition | transaction_price | fair_value_recognition | initial_fair_value | present_value_measurement | day_one_gain_loss | day_one_deferral | day_one_difference | deferred_difference |
| ---- | ----------------------------- | ----------------- | ---------------------- | ------------------ | ------------------------ | ----------------- | ---------------- | ------------------ | -------------------- |
| 1 | non | - | oui_sous_conditions | - | - | non | oui_sous_conditions | - | - |
| 2 | - | non | - | oui_sous_conditions | - | - | - | oui_sous_conditions | - |
| 3 | oui_sous_conditions | - | - | - | oui_sous_conditions | non | - | - | oui_sous_conditions |

### Retrieval

| Section Path | Score | Range (±5 in DB order) |
|--------------|-------|------------------------|
| 3.2.14 | 0.6718 | 3.2.9 - 3.2.19 |
| B4.1.9D | 0.6483 | B4.1.8A - B4.1.12 |
| B5.1.1 | 0.7464 | B4.3.12 - B5.2.2A |
| B5.1.2 | 0.6761 | B4.4.1 - B5.2.3 |
| B5.7.18 | 0.6594 | B5.7.13 - B6.2.3 |
| 15 | 0.5189 | 10 - 18B |

The LLM generated by far the most number of approaches for a question so far; this was considered a potential failure and elicited a bit more investigation.

An LLM(-as-judge) was asked to determine if the 3 answers were equivalent. They were equivalent but they were not a satisfactory answer to the question:
>What is important, though, is that these three answers are all about IFRS 9 impairment / Stage 3 / ECL mechanics. Your original question was about initial fair value measurement of an unsecured, interest-free shareholder loan with no fixed repayment term. That is a different issue.

The LLM used for judging offered to give the correct answer and made extensive queries to ifrs.org, ey.com, kpmg.com, ifrscommunity.com to do so. The answer correctly highlighted that a definitive position hinges on the repayment period:
>- If "no fixed repayment period" = repayable on demand: initial fair value is usually face value / amount advanced.
>- If "no fixed repayment period" does not give a real demand right: initial fair value is discounted present value using a market rate and an estimated expected term.

When prompted with the grounding context used by the assistant, the LLM posited that the grounding was missing IFRS 13:
>What was missing
>
>The critical missing piece was the IFRS 13 rule for a liability with a demand feature.
>
>The key authority is IFRS 13 paragraph 47, which says, in substance, that the fair value of a financial liability with a demand feature is not less than the amount payable on demand, discounted from the first date the amount could be required to be paid.
>
>That is the rule that prevents an agent from automatically applying a long-dated discounted-cash-flow model when the instrument is in fact callable immediately.
>
>Without that paragraph, the agent has no solid basis to conclude:
>
> - "no fixed repayment period" might mean repayable on demand, and
> - in that case, fair value is generally not determined by discounting an indefinite stream or a guessed long maturity.

Therefore this was deemed a grounding failure from a lack of corpus because the question chosen wasn't specific to IFRS 9.

Consequently, it will be kept for future reference because the large number of "accounting approaches" was probably a good indicator of an inability to answer.