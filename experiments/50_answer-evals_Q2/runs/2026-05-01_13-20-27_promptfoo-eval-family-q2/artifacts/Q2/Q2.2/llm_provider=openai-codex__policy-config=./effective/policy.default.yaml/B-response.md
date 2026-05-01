# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI (« prêt basique ») pour un actif financier comportant des clauses contractuelles contingentes pouvant modifier le calendrier ou le montant des flux de trésorerie, et incidence sur sa catégorie de mesure IFRS 9.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias33`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier relevant d’IFRS 9.
   - On suppose que les clauses visées sont des clauses contractuelles authentiques pouvant modifier le calendrier ou le montant des flux de trésorerie sur la durée de vie de l’instrument.
   - Le modèle de gestion de l’actif (conserver pour encaisser, encaisser et vendre, ou autre) n’est pas précisé dans la question.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut respecter le critère SPPI, mais seulement si, dans tous les scénarios contractuellement possibles, les flux restent uniquement des remboursements de principal et d’intérêts au sens d’un prêt basique et ne sont pas significativement différents lorsque le déclencheur n’est pas lié directement aux risques et coûts de base du prêt (IFRS 9 B4.1.10, B4.1.10A). La catégorie de mesure dépend ensuite aussi du business model (IFRS 9 4.1.2, 4.1.2A, 4.1.4).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle de gestion dont l’objectif est de percevoir les flux contractuels.<br>- Les flux contractuels, y compris après activation de la clause, restent uniquement des paiements de principal et d’intérêts.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts de base du prêt, les écarts de flux par rapport à un instrument identique sans la clause ne sont pas significatifs. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle de gestion dont l’objectif est atteint à la fois par l’encaissement des flux contractuels et par la vente.<br>- Les flux contractuels, y compris après activation de la clause, restent uniquement des paiements de principal et d’intérêts.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts de base du prêt, les écarts de flux par rapport à un instrument identique sans la clause ne sont pas significatifs. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Le test SPPI n’est pas satisfait du fait de la clause contingente.<br>- Ou le modèle de gestion n’est ni « détenir pour encaisser » ni « encaisser et vendre ». |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle de gestion dont l’objectif est de percevoir les flux contractuels.
   - Les flux contractuels, y compris après activation de la clause, restent uniquement des paiements de principal et d’intérêts.
   - Si le déclencheur n’est pas directement lié aux risques et coûts de base du prêt, les écarts de flux par rapport à un instrument identique sans la clause ne sont pas significatifs.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause contingente n’empêche pas le test SPPI: il faut apprécier les flux avant et après le changement, indépendamment de sa probabilité, selon IFRS 9 B4.1.10. Si le déclencheur ne se rattache pas directement aux risques et coûts de base du prêt, les flux ne doivent pas être significativement différents de ceux d’un instrument identique sans cette clause, selon IFRS 9 B4.1.10A. En plus, le business model doit être « détenir pour encaisser » selon IFRS 9 4.1.2.

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être évalué au coût amorti; sinon, cette catégorie est exclue.

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

### 2. Juste valeur par autres éléments du résultat global

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle de gestion dont l’objectif est atteint à la fois par l’encaissement des flux contractuels et par la vente.
   - Les flux contractuels, y compris après activation de la clause, restent uniquement des paiements de principal et d’intérêts.
   - Si le déclencheur n’est pas directement lié aux risques et coûts de base du prêt, les écarts de flux par rapport à un instrument identique sans la clause ne sont pas significatifs.

**Raisonnement**:
Dans cette situation, la clause contingente peut rester compatible avec SPPI selon la même analyse des flux avant et après changement imposée par IFRS 9 B4.1.10. Si le déclencheur n’est pas directement lié aux risques et coûts de base du prêt, il faut encore démontrer que, dans tous les scénarios contractuels, les flux ne diffèrent pas significativement d’un instrument identique sans cette clause, selon IFRS 9 B4.1.10A. Cette catégorie n’est toutefois ouverte que si le business model est à la fois d’encaisser les flux et de vendre, selon IFRS 9 4.1.2A.

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être évalué à la JV par OCI; sinon, cette catégorie est exclue.

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
   - Le test SPPI n’est pas satisfait du fait de la clause contingente.
   - Ou le modèle de gestion n’est ni « détenir pour encaisser » ni « encaisser et vendre ».

**Raisonnement**:
Dans cette situation, la JV par résultat s’applique si la clause contingente fait échouer le test SPPI, notamment lorsque les flux exposent à des risques non compatibles avec un prêt basique, selon IFRS 9 B4.1.7A, ou lorsque le business model ne permet ni le coût amorti ni la JV par OCI, selon IFRS 9 4.1.4. C’est aussi l’issue si l’analyse exigée par IFRS 9 B4.1.10 et B4.1.10A montre que les flux possibles ne sont pas uniquement du principal et des intérêts.

**Implications pratiques**: Si le critère SPPI échoue ou si le business model ne qualifie pas, l’actif est évalué à la JV par résultat.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.10

    >If a financial asset contains a contractual term that could change the timing or amount of contractual cash flows (for example, if the asset can be prepaid before maturity or its term can be extended), the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest on the principal amount outstanding. To make this determination, the entity must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows, irrespective of the probability of the change in contractual cash flows occurring. The entity may also need to assess the nature of any contingent event (ie the trigger) that would change the timing or amount of the contractual cash flows. While the nature of the contingent event in itself is not a determinative factor in assessing whether the contractual cash flows are solely payments of principal and interest, it may be an indicator. For example, compare a financial instrument with an interest rate that is reset to a higher rate if the debtor misses a particular number of payments to a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level. It is more likely in the former case that the contractual cash flows over the life of the instrument will be solely payments of principal and interest on the principal amount outstanding because of the relationship between missed payments and an increase in credit risk. In the former case, the nature of the contingent event relates directly to, and the contractual cash flows change in the same direction as, changes in basic lending risks and costs. (See also paragraph B4.1.18.)
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.