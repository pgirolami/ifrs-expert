# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI en IFRS 9 pour un actif financier comportant des clauses contractuelles pouvant modifier le montant ou l’échéancier des flux de trésorerie, notamment en présence d’un événement déclencheur

## Documentation
**Consultée**
   - IAS-S (standard) (`ias33`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose que l’instrument analysé est un actif financier relevant d’IFRS 9.
   - On suppose que les faits fournis ne précisent ni le modèle économique de gestion de l’actif ni la nature exacte du déclencheur ; l’analyse porte donc d’abord sur le seul critère SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, une clause modifiant le montant ou l’échéancier des flux n’exclut pas automatiquement le critère SPPI. L’actif respecte SPPI seulement si, dans tous les scénarios contractuels possibles, les flux restent des paiements de principal et d’intérêts, et si un déclencheur non lié aux risques de prêt basiques n’entraîne pas de différences significatives de flux (IFRS 9 B4.1.10, B4.1.10A).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Le modèle économique doit être de détenir l’actif pour encaisser les flux contractuels.<br>- La clause de modification ne doit pas faire sortir les flux du schéma principal + intérêts.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts basiques d’un prêt, les écarts de flux avec un instrument identique sans cette clause ne doivent pas être significatifs. |
| 2. Juste valeur par capitaux propres (FVOCI) | OUI SOUS CONDITIONS | - Le modèle économique doit être de collecter les flux contractuels et de vendre les actifs.<br>- La clause de modification doit rester compatible avec des flux de principal et d’intérêts.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts basiques d’un prêt, les scénarios contractuels possibles ne doivent pas conduire à des flux significativement différents. |
| 3. Juste valeur par résultat (FVTPL) | OUI SOUS CONDITIONS | - La clause expose les flux à des risques ou une volatilité incompatibles avec un prêt basique.<br>- Ou bien, pour un déclencheur non lié aux risques et coûts basiques d’un prêt, les flux deviennent significativement différents selon les scénarios contractuels possibles.<br>- Ou bien le modèle économique ne satisfait pas les conditions du coût amorti ou du FVOCI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique doit être de détenir l’actif pour encaisser les flux contractuels.
   - La clause de modification ne doit pas faire sortir les flux du schéma principal + intérêts.
   - Si le déclencheur n’est pas directement lié aux risques et coûts basiques d’un prêt, les écarts de flux avec un instrument identique sans cette clause ne doivent pas être significatifs.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si l’actif satisfait d’abord SPPI malgré la clause de modification des flux, puis s’il est détenu dans un modèle visant à encaisser les flux contractuels (IFRS 9 4.1.2, B4.1.10). Si l’événement déclencheur ne concerne pas directement les risques et coûts basiques d’un prêt, il faut en plus vérifier que, dans tous les scénarios contractuels possibles, les flux ne sont pas significativement différents de ceux d’un instrument identique sans cette clause (IFRS 9 B4.1.10A).

**Implications pratiques**: Si ces conditions sont réunies, la présence d’une clause déclenchée n’empêche pas, à elle seule, la mesure au coût amorti.

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

### 2. Juste valeur par capitaux propres (FVOCI)

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique doit être de collecter les flux contractuels et de vendre les actifs.
   - La clause de modification doit rester compatible avec des flux de principal et d’intérêts.
   - Si le déclencheur n’est pas directement lié aux risques et coûts basiques d’un prêt, les scénarios contractuels possibles ne doivent pas conduire à des flux significativement différents.

**Raisonnement**:
Dans cette situation, le FVOCI est envisageable si l’actif passe le test SPPI malgré la clause contractuelle et si le modèle économique combine encaissement des flux et ventes (IFRS 9 4.1.2A, B4.1.10). La même analyse des clauses déclenchées s’applique : avant et après modification, les flux doivent rester de type principal + intérêts, et un déclencheur non lié aux risques de prêt basiques ne doit pas produire d’écarts significatifs de flux (IFRS 9 B4.1.10A).

**Implications pratiques**: Si SPPI est respecté et que le modèle économique est mixte collecte/vente, l’actif peut être classé en FVOCI.

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

### 3. Juste valeur par résultat (FVTPL)

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause expose les flux à des risques ou une volatilité incompatibles avec un prêt basique.
   - Ou bien, pour un déclencheur non lié aux risques et coûts basiques d’un prêt, les flux deviennent significativement différents selon les scénarios contractuels possibles.
   - Ou bien le modèle économique ne satisfait pas les conditions du coût amorti ou du FVOCI.

**Raisonnement**:
Dans cette situation, le FVTPL s’impose si la clause contractuelle fait échouer SPPI, par exemple parce qu’elle expose les flux à des risques non compatibles avec un prêt basique, ou si les flux possibles deviennent significativement différents dans les scénarios contractuels pertinents (IFRS 9 B4.1.7A, B4.1.10A). Il s’applique aussi si, même avec SPPI respecté, le modèle économique n’est ni “collecte” ni “collecte et vente” au sens d’IFRS 9 (IFRS 9 4.1.4).

**Implications pratiques**: Si SPPI échoue ou si le modèle économique requis manque, l’actif est mesuré à la juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.