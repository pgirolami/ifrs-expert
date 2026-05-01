# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Un instrument dont les termes contractuels peuvent modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas de survenance d’un événement déclencheur, peut-il satisfaire au critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI pour un actif financier dont les clauses contractuelles peuvent modifier le montant ou l’échéancier des flux de trésorerie, y compris via un événement déclencheur contingent

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs19`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier relevant d’IFRS 9 et non d’un dérivé autonome.
   - On suppose que la question porte d’abord sur le test SPPI; le modèle économique (conserver pour encaisser ou encaisser et vendre) n’est pas précisé.
   - On suppose que la clause contractuelle modifiant les flux est une clause véritable et non un événement extrêmement rare, hautement anormal et très improbable.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut satisfaire au critère SPPI si, en tenant compte de tous les scénarios contractuels possibles, les flux restent des paiements de principal et d’intérêts au sens d’un prêt basique. Si la clause introduit une exposition non compatible ou des écarts significatifs, le test SPPI échoue et la catégorie résiduelle est la JV par résultat.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Les flux contractuels, dans tous les scénarios contractuellement possibles, ne sont pas significativement différents de ceux d’un prêt basique comparable.<br>- La clause ne crée pas d’exposition à des risques ou à une volatilité incompatibles avec un prêt basique.<br>- L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - Les flux contractuels restent compatibles avec un prêt basique malgré la clause de modification.<br>- Les écarts potentiels liés à la clause ne sont pas significatifs au regard d’un instrument comparable sans cette clause.<br>- L’actif est détenu dans un modèle économique de collecte des flux et de vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause introduit une exposition incompatible avec un prêt basique, ou<br>- Les flux contractuels possibles deviennent significativement différents de ceux d’un instrument comparable compatible SPPI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels, dans tous les scénarios contractuellement possibles, ne sont pas significativement différents de ceux d’un prêt basique comparable.
   - La clause ne crée pas d’exposition à des risques ou à une volatilité incompatibles avec un prêt basique.
   - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause pouvant modifier l’échéancier ou le montant des flux ne fait pas sortir l’actif du SPPI. IFRS 9 exige d’examiner les flux avant et après le changement, indépendamment de la probabilité du déclencheur, et d’écarter les clauses ayant plus qu’un effet de minimis ou introduisant une exposition étrangère à un prêt basique (IFRS 9 B4.1.10, B4.1.10A, B4.1.18). Si ce test est réussi, le coût amorti reste disponible seulement si le modèle économique est « hold to collect » (IFRS 9 4.1.2).

**Implications pratiques**: Le test SPPI doit être documenté sur la clause de déclenchement avant de conclure à une mesure au coût amorti.

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
   - Les flux contractuels restent compatibles avec un prêt basique malgré la clause de modification.
   - Les écarts potentiels liés à la clause ne sont pas significatifs au regard d’un instrument comparable sans cette clause.
   - L’actif est détenu dans un modèle économique de collecte des flux et de vente.

**Raisonnement**:
Dans cette situation, la présence d’un événement déclencheur n’empêche pas en soi le SPPI; le même examen des flux avant/après modification et des scénarios contractuels s’impose (IFRS 9 B4.1.10, B4.1.10A). Si le critère SPPI est satisfait, cette catégorie n’est ouverte que si le modèle économique est atteint à la fois par l’encaissement des flux et par la vente des actifs (IFRS 9 4.1.2A).

**Implications pratiques**: La conclusion SPPI ne suffit pas seule; il faut aussi démontrer le modèle économique « collect and sell ».

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
   - La clause introduit une exposition incompatible avec un prêt basique, ou
   - Les flux contractuels possibles deviennent significativement différents de ceux d’un instrument comparable compatible SPPI.

**Raisonnement**:
Dans cette situation, la JV par résultat s’applique si la clause de modification fait échouer le SPPI, par exemple si elle expose à autre chose qu’au temps, au risque de crédit ou à d’autres risques/coûts basiques de prêt. IFRS 9 retient la JV par résultat comme catégorie résiduelle lorsque l’actif ne remplit pas les conditions ouvrant le coût amorti ou la JVOCI (IFRS 9 4.1.1, B4.1.7A, B4.1.8A).

**Implications pratiques**: Si le test SPPI échoue, l’actif ne peut pas être classé au coût amorti ni en JVOCI et bascule en JV par résultat.

**Référence**:
 - ifrs9 4.1.1

    >Unless paragraph 4.1.5 applies, an entity shall classify financial assets as subsequently measured at amortised cost, fair value through other comprehensive income or fair value through profit or loss on the basis of both:
(a)the entity’s business model for managing the financial assets and
(b)the contractual cash flow characteristics of the financial asset.
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.8A

    >In assessing whether the contractual cash flows of a financial asset are consistent with a basic lending arrangement, an entity may have to consider the different elements of interest separately. The assessment of interest focuses on what an entity is being compensated for, rather than how much compensation an entity receives. Nonetheless, the amount of compensation an entity receives may indicate that the entity is being compensated for something other than basic lending risks and costs. Contractual cash flows are inconsistent with a basic lending arrangement if they are indexed to a variable that is not a basic lending risk or cost (for example, the value of equity instruments or the price of a commodity) or if they represent a share of the debtor’s revenue or profit, even if such contractual terms are common in the market in which the entity operates.