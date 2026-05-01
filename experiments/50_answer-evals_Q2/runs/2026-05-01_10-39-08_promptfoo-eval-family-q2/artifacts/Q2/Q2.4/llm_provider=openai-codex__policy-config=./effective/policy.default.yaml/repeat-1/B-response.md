# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI (« prêt basique ») en IFRS 9 lorsqu’une clause contractuelle peut modifier le calendrier ou le montant des flux de trésorerie à la survenance d’un événement déclencheur.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias33`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose que l’instrument en cause est un actif financier relevant d’IFRS 9.
   - On suppose que la question porte uniquement sur l’effet d’une clause contractuelle modifiant les flux à la survenance d’un événement déclencheur, sans autres caractéristiques non décrites.
   - Le modèle économique de détention de l’actif n’est pas précisé ; la conclusion sur le classement entre coût amorti et FVOCI dépendra donc de ce point en plus du test SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut encore satisfaire le critère SPPI si, malgré la clause déclenchante, les flux contractuels possibles restent des paiements de principal et d’intérêt et ne diffèrent pas significativement d’un prêt basique comparable (IFRS 9 B4.1.10, B4.1.10A). Si la clause introduit une exposition non compatible avec un prêt basique, l’actif échoue au test SPPI et relève du FVTPL (IFRS 9 B4.1.7A, 4.1.4).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - La clause déclenchante ne doit pas introduire d’exposition à des risques ou une variabilité incompatibles avec un prêt basique.<br>- Dans tous les scénarios contractuellement possibles, les flux doivent rester des paiements de principal et d’intérêt, ou ne pas être significativement différents d’un instrument identique sans cette clause lorsque IFRS 9 B4.1.10A s’applique.<br>- Le modèle économique doit être de type « hold to collect ». |
| 2. Juste valeur par OCI (titres de dette) | OUI SOUS CONDITIONS | - La clause déclenchante doit laisser subsister des flux contractuels de principal et d’intérêt au sens d’IFRS 9.<br>- Si le déclencheur ne se rattache pas directement aux risques et coûts de base d’un prêt, les flux ne doivent pas être significativement différents de ceux d’un instrument identique sans cette clause.<br>- Le modèle économique doit être de type « collect and sell ». |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause déclenchante introduit une exposition incompatible avec un prêt basique, ou les flux possibles deviennent significativement différents de ceux d’un instrument comparable sans cette clause.<br>- L’actif ne remplit donc pas la condition SPPI nécessaire au coût amorti ou à la FVOCI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause déclenchante ne doit pas introduire d’exposition à des risques ou une variabilité incompatibles avec un prêt basique.
   - Dans tous les scénarios contractuellement possibles, les flux doivent rester des paiements de principal et d’intérêt, ou ne pas être significativement différents d’un instrument identique sans cette clause lorsque IFRS 9 B4.1.10A s’applique.
   - Le modèle économique doit être de type « hold to collect ».

**Raisonnement**:
Dans cette situation, le coût amorti reste possible si la clause qui modifie l’échéancier ou le montant des flux ne fait pas échouer le test SPPI : il faut apprécier les flux pouvant survenir avant et après le déclenchement, sans tenir compte de la probabilité de l’événement (IFRS 9 B4.1.10). En plus, l’actif ne peut être au coût amorti que s’il est détenu dans un modèle visant à collecter les flux contractuels (IFRS 9 4.1.2).

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être classé au coût amorti ; sinon, ce traitement ne s’applique pas.

**Référence**:
 - ifrs9 4.1.2

    >A financial asset shall be measured at amortised cost if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is to hold financial assets in order to collect contractual cash flows and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 B4.1.10

    >If a financial asset contains a contractual term that could change the timing or amount of contractual cash flows (for example, if the asset can be prepaid before maturity or its term can be extended), the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest on the principal amount outstanding. To make this determination, the entity must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows, irrespective of the probability of the change in contractual cash flows occurring. The entity may also need to assess the nature of any contingent event (ie the trigger) that would change the timing or amount of the contractual cash flows. While the nature of the contingent event in itself is not a determinative factor in assessing whether the contractual cash flows are solely payments of principal and interest, it may be an indicator. For example, compare a financial instrument with an interest rate that is reset to a higher rate if the debtor misses a particular number of payments to a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level. It is more likely in the former case that the contractual cash flows over the life of the instrument will be solely payments of principal and interest on the principal amount outstanding because of the relationship between missed payments and an increase in credit risk. In the former case, the nature of the contingent event relates directly to, and the contractual cash flows change in the same direction as, changes in basic lending risks and costs. (See also paragraph B4.1.18.)
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.

### 2. Juste valeur par OCI (titres de dette)

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause déclenchante doit laisser subsister des flux contractuels de principal et d’intérêt au sens d’IFRS 9.
   - Si le déclencheur ne se rattache pas directement aux risques et coûts de base d’un prêt, les flux ne doivent pas être significativement différents de ceux d’un instrument identique sans cette clause.
   - Le modèle économique doit être de type « collect and sell ».

**Raisonnement**:
Dans cette situation, la FVOCI demeure possible si la clause déclenchante est compatible avec SPPI selon la même analyse des flux avant et après l’événement déclencheur (IFRS 9 B4.1.10, B4.1.10A). Toutefois, ce classement n’est applicable que si le modèle économique combine encaissement des flux contractuels et cession des actifs (IFRS 9 4.1.2A).

**Implications pratiques**: Si SPPI est satisfait et que le modèle économique est mixte collecte/vente, l’actif peut être classé en FVOCI.

**Référence**:
 - ifrs9 4.1.2A

    >A financial asset shall be measured at fair value through other comprehensive income if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 B4.1.10

    >If a financial asset contains a contractual term that could change the timing or amount of contractual cash flows (for example, if the asset can be prepaid before maturity or its term can be extended), the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest on the principal amount outstanding. To make this determination, the entity must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows, irrespective of the probability of the change in contractual cash flows occurring. The entity may also need to assess the nature of any contingent event (ie the trigger) that would change the timing or amount of the contractual cash flows. While the nature of the contingent event in itself is not a determinative factor in assessing whether the contractual cash flows are solely payments of principal and interest, it may be an indicator. For example, compare a financial instrument with an interest rate that is reset to a higher rate if the debtor misses a particular number of payments to a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level. It is more likely in the former case that the contractual cash flows over the life of the instrument will be solely payments of principal and interest on the principal amount outstanding because of the relationship between missed payments and an increase in credit risk. In the former case, the nature of the contingent event relates directly to, and the contractual cash flows change in the same direction as, changes in basic lending risks and costs. (See also paragraph B4.1.18.)
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.

### 3. Juste valeur par résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause déclenchante introduit une exposition incompatible avec un prêt basique, ou les flux possibles deviennent significativement différents de ceux d’un instrument comparable sans cette clause.
   - L’actif ne remplit donc pas la condition SPPI nécessaire au coût amorti ou à la FVOCI.

**Raisonnement**:
Dans cette situation, le FVTPL s’applique si la clause déclenchante fait échouer le test SPPI, par exemple parce qu’elle introduit une exposition à des risques non propres à un prêt basique ou une divergence significative des flux (IFRS 9 B4.1.7A, B4.1.10A). IFRS 9 prévoit alors que l’actif est mesuré à la juste valeur par résultat s’il ne relève ni du coût amorti ni de la FVOCI (IFRS 9 4.1.4).

**Implications pratiques**: Si le test SPPI échoue à cause de la clause contractuelle, le classement résiduel est le FVTPL.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.