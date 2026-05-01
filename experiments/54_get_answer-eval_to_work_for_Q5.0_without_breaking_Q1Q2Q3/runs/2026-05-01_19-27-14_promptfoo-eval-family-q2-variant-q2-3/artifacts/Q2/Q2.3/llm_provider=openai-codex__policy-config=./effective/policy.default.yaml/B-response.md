# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI en IFRS 9 pour un actif financier dont des clauses contractuelles peuvent modifier le calendrier ou le montant des flux de trésorerie en cas d’événement déclencheur.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question porte sur un actif financier relevant d’IFRS 9, et non sur un instrument de capitaux propres ou un passif financier.
   - Le fait décrit est limité à l’existence d’une clause contractuelle pouvant modifier la date ou le montant des flux en cas d’événement déclencheur; le modèle économique de détention n’est pas précisé.
   - L’analyse demandée vise d’abord le test SPPI; la catégorie de mesure finale dépendra ensuite aussi du modèle économique selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui. Un instrument avec clause déclenchée peut encore respecter SPPI si, dans tous les scénarios contractuels pertinents, les flux avant et après modification restent des paiements de principal et d’intérêt, ou ne sont pas significativement différents lorsque le déclencheur n’est pas lié aux risques de prêt basiques (IFRS 9 B4.1.10, B4.1.10A, B4.1.18).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est de percevoir les flux contractuels.<br>- Les flux contractuels avant et après l’éventuel changement restent uniquement des remboursements de principal et d’intérêt.<br>- Si le déclencheur n’est pas lié directement aux risques et coûts d’un prêt basique, les écarts de flux par rapport à un instrument identique sans cette clause ne sont pas significatifs.<br>- La clause n’a qu’un effet de minimis ou n’est pas genuine, le cas échéant. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par la perception des flux contractuels et par la vente.<br>- Les flux contractuels avant et après l’éventuel changement restent uniquement des remboursements de principal et d’intérêt.<br>- Si le déclencheur n’est pas lié directement aux risques et coûts d’un prêt basique, les écarts de flux par rapport à un instrument identique sans cette clause ne sont pas significatifs.<br>- La clause n’a qu’un effet de minimis ou n’est pas genuine, le cas échéant. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause contractuelle introduit des flux incompatibles avec un prêt basique.<br>- Ou bien, dans des scénarios contractuels possibles, les flux deviennent significativement différents de ceux d’un instrument identique sans la clause.<br>- Ou bien le modèle économique n’est ni hold to collect ni collect and sell. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est de percevoir les flux contractuels.
   - Les flux contractuels avant et après l’éventuel changement restent uniquement des remboursements de principal et d’intérêt.
   - Si le déclencheur n’est pas lié directement aux risques et coûts d’un prêt basique, les écarts de flux par rapport à un instrument identique sans cette clause ne sont pas significatifs.
   - La clause n’a qu’un effet de minimis ou n’est pas genuine, le cas échéant.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause déclenchée n’empêche pas le test SPPI: il faut apprécier les flux pouvant survenir avant et après le changement, sans tenir compte de la probabilité du déclenchement (IFRS 9 B4.1.10). Si le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, l’actif reste SPPI seulement si, dans tous les scénarios contractuels possibles, les flux ne sont pas significativement différents de ceux d’un instrument identique sans cette clause (IFRS 9 B4.1.10A). En plus, le modèle économique doit être "hold to collect" (IFRS 9 4.1.2).

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être classé au coût amorti; sinon, cette catégorie est exclue.

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
 - ifrs9 B4.1.18

    >A contractual cash flow characteristic does not affect the classification of the financial asset if it could have only a de minimis effect on the contractual cash flows of the financial asset. To make this determination, an entity must consider the possible effect of the contractual cash flow characteristic in each reporting period and cumulatively over the life of the financial instrument. In addition, if a contractual cash flow characteristic could have an effect on the contractual cash flows that is more than de minimis (either in a single reporting period or cumulatively) but that cash flow characteristic is not genuine, it does not affect the classification of a financial asset. A cash flow characteristic is not genuine if it affects the instrument’s contractual cash flows only on the occurrence of an event that is extremely rare, highly abnormal and very unlikely to occur.

### 2. Juste valeur par autres éléments du résultat global

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par la perception des flux contractuels et par la vente.
   - Les flux contractuels avant et après l’éventuel changement restent uniquement des remboursements de principal et d’intérêt.
   - Si le déclencheur n’est pas lié directement aux risques et coûts d’un prêt basique, les écarts de flux par rapport à un instrument identique sans cette clause ne sont pas significatifs.
   - La clause n’a qu’un effet de minimis ou n’est pas genuine, le cas échéant.

**Raisonnement**:
Dans cette situation, la catégorie FVOCI reste possible si l’actif passe le même test SPPI malgré la clause déclenchée, selon l’analyse des flux avant et après changement et, le cas échéant, de l’écart non significatif par rapport à un instrument sans la clause (IFRS 9 B4.1.10, B4.1.10A). La différence avec le coût amorti ne porte pas sur SPPI, mais sur le modèle économique: il faut un objectif de collecte et de vente (IFRS 9 4.1.2A).

**Implications pratiques**: Si SPPI est satisfait et que le modèle est collect-and-sell, l’actif peut être classé en FVOCI.

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
 - ifrs9 B4.1.18

    >A contractual cash flow characteristic does not affect the classification of the financial asset if it could have only a de minimis effect on the contractual cash flows of the financial asset. To make this determination, an entity must consider the possible effect of the contractual cash flow characteristic in each reporting period and cumulatively over the life of the financial instrument. In addition, if a contractual cash flow characteristic could have an effect on the contractual cash flows that is more than de minimis (either in a single reporting period or cumulatively) but that cash flow characteristic is not genuine, it does not affect the classification of a financial asset. A cash flow characteristic is not genuine if it affects the instrument’s contractual cash flows only on the occurrence of an event that is extremely rare, highly abnormal and very unlikely to occur.

### 3. Juste valeur par résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La clause contractuelle introduit des flux incompatibles avec un prêt basique.
   - Ou bien, dans des scénarios contractuels possibles, les flux deviennent significativement différents de ceux d’un instrument identique sans la clause.
   - Ou bien le modèle économique n’est ni hold to collect ni collect and sell.

**Raisonnement**:
Cette catégorie s’applique dans cette situation si la clause déclenchée fait échouer SPPI, par exemple parce qu’elle introduit une exposition non compatible avec un prêt basique, ou parce que les flux peuvent devenir significativement différents de ceux d’un instrument identique sans cette clause (IFRS 9 B4.1.7A, B4.1.10A). Elle s’applique aussi si l’actif ne relève pas d’un modèle économique permettant le coût amorti ou FVOCI, puisque seules ces deux catégories exigent SPPI (IFRS 9 4.1.1, 4.1.2, 4.1.2A).

**Implications pratiques**: Si SPPI échoue ou si le modèle économique requis n’est pas rempli, l’actif est mesuré à la juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.1

    >Unless paragraph 4.1.5 applies, an entity shall classify financial assets as subsequently measured at amortised cost, fair value through other comprehensive income or fair value through profit or loss on the basis of both:
(a)the entity’s business model for managing the financial assets and
(b)the contractual cash flow characteristics of the financial asset.
 - ifrs9 4.1.2

    >A financial asset shall be measured at amortised cost if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is to hold financial assets in order to collect contractual cash flows and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 4.1.2A

    >A financial asset shall be measured at fair value through other comprehensive income if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.