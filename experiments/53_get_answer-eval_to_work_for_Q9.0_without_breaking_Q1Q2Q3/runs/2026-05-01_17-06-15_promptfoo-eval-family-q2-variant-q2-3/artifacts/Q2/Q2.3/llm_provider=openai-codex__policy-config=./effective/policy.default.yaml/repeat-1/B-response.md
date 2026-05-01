# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Déterminer si des flux contractuels susceptibles de varier selon un événement déclencheur peuvent néanmoins satisfaire le critère SPPI d’un « prêt basique » au sens d’IFRS 9, et donc rester éligibles aux catégories de classement fondées sur ce critère.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question vise un actif financier relevant d’IFRS 9 et non un instrument de capitaux propres.
   - Les seuls faits disponibles sont l’existence d’un terme contractuel pouvant modifier le calendrier ou le montant des flux en cas d’événement déclencheur; aucun autre fait de business model n’est précisé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut encore satisfaire le critère SPPI si, dans tous les scénarios contractuellement possibles, les flux demeurent des paiements de principal et d’intérêts, y compris avant et après le déclenchement (IFRS 9 B4.1.10). Si le déclencheur ne se rattache pas directement aux risques et coûts d’un prêt basique, il faut en plus que l’effet ne rende pas les flux significativement différents d’un instrument identique sans cette clause (IFRS 9 B4.1.10A).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est de détenir les actifs pour en percevoir les flux contractuels.<br>- Dans tous les scénarios contractuellement possibles, les flux modifiés restent uniquement des paiements de principal et d’intérêts.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, la clause ne doit pas rendre les flux significativement différents de ceux d’un instrument identique sans cette clause. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par la collecte des flux contractuels et par la vente d’actifs financiers.<br>- Dans tous les scénarios contractuellement possibles, les flux modifiés restent uniquement des paiements de principal et d’intérêts.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, la clause ne doit pas rendre les flux significativement différents de ceux d’un instrument identique sans cette clause. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause déclenchante conduit à des flux qui ne sont pas uniquement des paiements de principal et d’intérêts.<br>- Ou bien, lorsque le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, les flux deviennent significativement différents de ceux d’un instrument identique sans cette clause. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est de détenir les actifs pour en percevoir les flux contractuels.
   - Dans tous les scénarios contractuellement possibles, les flux modifiés restent uniquement des paiements de principal et d’intérêts.
   - Si le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, la clause ne doit pas rendre les flux significativement différents de ceux d’un instrument identique sans cette clause.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause déclenchante ne fait pas sortir l’instrument du critère SPPI et si les flux restent des paiements de principal et d’intérêts avant et après la modification (IFRS 9 4.1.2(b), B4.1.10). Si le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, l’instrument peut néanmoins rester SPPI seulement si les flux ne sont pas significativement différents de ceux d’un instrument identique sans cette clause (IFRS 9 B4.1.10A).

**Implications pratiques**: Le coût amorti reste possible seulement si la clause contingente passe le test SPPI et si le modèle économique est « hold to collect ».

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
   - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par la collecte des flux contractuels et par la vente d’actifs financiers.
   - Dans tous les scénarios contractuellement possibles, les flux modifiés restent uniquement des paiements de principal et d’intérêts.
   - Si le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, la clause ne doit pas rendre les flux significativement différents de ceux d’un instrument identique sans cette clause.

**Raisonnement**:
Dans cette situation, la catégorie FVOCI pour un actif de dette reste envisageable si la clause déclenchante respecte le critère SPPI selon la même analyse des flux avant et après déclenchement (IFRS 9 4.1.2A(b), B4.1.10). En plus, il faut que le modèle économique soit atteint à la fois par la collecte des flux contractuels et par la vente; à défaut, cette catégorie ne s’applique pas même si l’instrument est SPPI (IFRS 9 4.1.2A(a)).

**Implications pratiques**: La FVOCI n’est possible que si la clause contingente passe le test SPPI et si le modèle économique est « collect and sell ».

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
   - La clause déclenchante conduit à des flux qui ne sont pas uniquement des paiements de principal et d’intérêts.
   - Ou bien, lorsque le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique, les flux deviennent significativement différents de ceux d’un instrument identique sans cette clause.

**Raisonnement**:
Dans cette situation, la JV par résultat s’applique si la clause déclenchante fait échouer le test SPPI, par exemple parce qu’elle introduit une exposition incompatible avec un prêt basique ou parce que les flux après déclenchement deviennent significativement différents d’un instrument identique sans la clause (IFRS 9 B4.1.7A, B4.1.10A). IFRS 9 prévoit alors que l’actif est mesuré à la juste valeur par résultat sauf s’il relève du coût amorti ou de la FVOCI (IFRS 9 4.1.4).

**Implications pratiques**: Si la clause contingente fait perdre le caractère SPPI, l’actif bascule vers la juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.