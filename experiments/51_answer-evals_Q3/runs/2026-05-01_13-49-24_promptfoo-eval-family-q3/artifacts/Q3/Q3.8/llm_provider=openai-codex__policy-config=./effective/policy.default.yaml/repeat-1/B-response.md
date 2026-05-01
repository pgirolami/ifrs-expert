# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Qu’entend-on par un actif financier générant exclusivement des paiements de principal et d’intérêts selon ses clauses contractuelles ?

**Reformulation**:
>détermination de la signification du critère de flux de trésorerie contractuels constitués uniquement de paiements de principal et d’intérêts (« SPPI ») pour la classification d’un actif financier selon IFRS 9

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias19`)
   - IFRIC (interpretation) (`ifric12`)
   - IFRS-S (standard) (`ifrs9`, `ifrs3`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias32`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question est comprise comme une demande de définition du critère SPPI (« solely payments of principal and interest ») en IFRS 9, et non comme l’analyse d’un instrument précis.
   - Faute de faits contractuels spécifiques, l’applicabilité des catégories de mesure est appréciée de manière conditionnelle selon le respect ou non du test SPPI et selon le modèle économique.

## Recommandation

**OUI**

Selon IFRS 9, un actif financier génère exclusivement des paiements de principal et d’intérêts si ses flux contractuels correspondent à un prêt de base: principal = juste valeur initiale, intérêts = contrepartie de la valeur temps de l’argent, du risque de crédit, d’autres risques/coûts de base et d’une marge. Toute exposition contractuelle à des prix d’actions, de matières premières ou à un levier fait échouer le test SPPI.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.<br>- Les clauses contractuelles donnent lieu, à des dates spécifiées, uniquement à des paiements de principal et d’intérêts. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique combinant encaissement des flux contractuels et ventes.<br>- Les clauses contractuelles donnent lieu, à des dates spécifiées, uniquement à des paiements de principal et d’intérêts. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Les flux contractuels ne satisfont pas au test SPPI ou l’actif ne remplit pas les conditions des autres catégories. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.
   - Les clauses contractuelles donnent lieu, à des dates spécifiées, uniquement à des paiements de principal et d’intérêts.

**Raisonnement**:
Dans cette situation, le coût amorti n’est pertinent que si l’actif satisfait d’abord au test SPPI puis est détenu dans un modèle économique de conservation pour encaisser les flux contractuels (IFRS 9 4.1.2). Le sens de SPPI est donné par IFRS 9 4.1.3 et B4.1.7A: les flux doivent être ceux d’un prêt de base et ne pas exposer le porteur à des risques sans lien avec un prêt de base, comme des prix d’actions ou de matières premières.

**Implications pratiques**: Si ces conditions sont remplies, la catégorie de mesure peut être le coût amorti.

**Référence**:
 - ifrs9 4.1.2

    >A financial asset shall be measured at amortised cost if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is to hold financial assets in order to collect contractual cash flows and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 4.1.3

    >For the purpose of applying paragraphs 4.1.2(b) and 4.1.2A(b) :
(a)principal is the fair value of the financial asset at initial recognition. Paragraph B4.1.7B provides additional guidance on the meaning of principal.
(b)interest consists of consideration for the time value of money, for the credit risk associated with the principal amount outstanding during a particular period of time and for other basic lending risks and costs, as well as a profit margin. Paragraphs B4.1.7A and B4.1.9A⁠–⁠B4.1.9E provide additional guidance on the meaning of interest, including the meaning of the time value of money.
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.

### 2. Juste valeur par autres éléments du résultat global

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique combinant encaissement des flux contractuels et ventes.
   - Les clauses contractuelles donnent lieu, à des dates spécifiées, uniquement à des paiements de principal et d’intérêts.

**Raisonnement**:
Dans cette situation, cette catégorie n’est possible que si le test SPPI est satisfait et si le modèle économique consiste à la fois à encaisser les flux contractuels et à vendre les actifs (IFRS 9 4.1.2A). La notion de SPPI reste la même: flux d’un prêt de base, sans indexation à des variables non basiques comme un indice actions ou le prix d’une matière première (IFRS 9 B4.1.8A).

**Implications pratiques**: Si ces conditions sont remplies, la catégorie de mesure peut être la JV par OCI.

**Référence**:
 - ifrs9 4.1.2A

    >A financial asset shall be measured at fair value through other comprehensive income if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 B4.1.8A

    >In assessing whether the contractual cash flows of a financial asset are consistent with a basic lending arrangement, an entity may have to consider the different elements of interest separately. The assessment of interest focuses on what an entity is being compensated for, rather than how much compensation an entity receives. Nonetheless, the amount of compensation an entity receives may indicate that the entity is being compensated for something other than basic lending risks and costs. Contractual cash flows are inconsistent with a basic lending arrangement if they are indexed to a variable that is not a basic lending risk or cost (for example, the value of equity instruments or the price of a commodity) or if they represent a share of the debtor’s revenue or profit, even if such contractual terms are common in the market in which the entity operates.

### 3. Juste valeur par résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels ne satisfont pas au test SPPI ou l’actif ne remplit pas les conditions des autres catégories.

**Raisonnement**:
Dans cette situation, la JV par résultat devient la conclusion si l’actif échoue au test SPPI. IFRS 9 indique qu’un levier contractuel, ou une exposition à des variables étrangères à un prêt de base, comme un prix de matière première, empêche de conclure à des paiements uniquement de principal et d’intérêts (IFRS 9 B4.1.9, B4.1.14).

**Implications pratiques**: Si le test SPPI échoue, l’actif relève en pratique de la JV par résultat.

**Référence**:
 - ifrs9 B4.1.9

    >Leverage is a contractual cash flow characteristic of some financial assets. Leverage increases the variability of the contractual cash flows with the result that they do not have the economic characteristics of interest. Stand‑alone option, forward and swap contracts are examples of financial assets that include such leverage. Thus, such contracts do not meet the condition in paragraphs 4.1.2(b) and 4.1.2A(b) and cannot be subsequently measured at amortised cost or fair value through other comprehensive income.
 - ifrs9 B4.1.14

    >The following examples illustrate contractual cash flows that are not solely payments of principal and interest on the principal amount outstanding. This list of examples is not exhaustive.
InstrumentFInstrumentFisabondthatisconvertibleintoafixednumberofequityinstrumentsoftheissuer.The holder would analyse the convertible bond in its entirety.
The contractual cash flows are not payments of principal and interest on the principal amount outstanding because they reflect a return that is inconsistent with a basic lending arrangement (see paragraph B4.1.7A); ie the return is linked to the value of the equity of the issuer.
InstrumentGInstrumentGisaloanthatpaysaninversefloatinginterestrate(ietheinterestratehasaninverserelationshiptomarketinterestrates).The contractual cash flows are not solely payments of principal and interest on the principal amount outstanding.
The interest amounts are not consideration for the time value of money on the principal amount outstanding.
InstrumentHInstrumentHisaperpetualinstrumentbuttheissuermaycalltheinstrumentatanypointandpaytheholdertheparamountplusaccruedinterestdue.InstrumentHpaysamarketinterestratebutpaymentofinterestcannotbemadeunlesstheissuerisabletoremainsolventimmediatelyafterwards.Deferredinterestdoesnotaccrueadditionalinterest.The contractual cash flows are not payments of principal and interest on the principal amount outstanding. That is because the issuer may be required to defer interest payments and additional interest does not accrue on those deferred interest amounts. As a result, interest amounts are not consideration for the time value of money on the principal amount outstanding.
If interest accrued on the deferred amounts, the contractual cash flows could be payments of principal and interest on the principal amount outstanding.
The fact that Instrument H is perpetual does not in itself mean that the contractual cash flows are not payments of principal and interest on the principal amount outstanding. In effect, a ...