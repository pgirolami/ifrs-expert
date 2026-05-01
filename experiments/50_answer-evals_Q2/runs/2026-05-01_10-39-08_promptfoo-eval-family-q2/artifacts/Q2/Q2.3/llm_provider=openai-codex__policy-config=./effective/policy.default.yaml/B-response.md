# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation, au titre d’IFRS 9, du respect du critère SPPI (« prêt basique ») pour un actif financier comportant des clauses contractuelles ou des événements déclencheurs modifiant le calendrier ou le montant des flux de trésorerie

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier entrant dans le champ d’IFRS 9 et non d’un instrument de capitaux propres.
   - On suppose que la question porte uniquement sur l’appréciation du critère SPPI en présence d’une clause contractuelle ou d’un événement déclencheur, sans faits supplémentaires sur le modèle économique de gestion.
   - En l’absence de termes contractuels détaillés, l’analyse conclut par conditions lorsque le caractère SPPI dépend de l’ampleur et de la nature de la modification des flux.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un instrument avec clause modifiant le calendrier ou le montant des flux peut encore satisfaire SPPI si, dans tous les scénarios contractuellement possibles, les flux restent des paiements de principal et d’intérêt, ou ne sont pas significativement différents, selon IFRS 9 B4.1.10, B4.1.10A et B4.1.18. La classification ultérieure dépend ensuite aussi du modèle économique selon IFRS 9 4.1.2 ou 4.1.2A.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Les flux contractuels avant et après déclenchement restent uniquement des paiements de principal et d’intérêt sur le principal restant dû.<br>- Si l’événement déclencheur n’est pas directement lié aux risques et coûts basiques de prêt, les flux de tous les scénarios possibles ne doivent pas être significativement différents d’un instrument identique sans cette clause.<br>- L’effet de la clause est au plus de minimis, ou la clause n’est pas genuine, le cas échéant.<br>- L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - Les flux contractuels avant et après déclenchement satisfont le test SPPI.<br>- Lorsque le déclencheur n’est pas directement lié aux risques et coûts basiques de prêt, les flux ne sont pas significativement différents d’un instrument identique sans cette clause dans tous les scénarios contractuellement possibles.<br>- Toute incidence de la clause est de minimis ou la clause n’est pas genuine, le cas échéant.<br>- L’actif est détenu dans un modèle économique visant à la fois l’encaissement des flux contractuels et la vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause modifiant les flux fait échouer le test SPPI.<br>- Ou bien les flux dans un ou plusieurs scénarios contractuellement possibles sont significativement différents de ceux d’un instrument identique sans la clause.<br>- Ou bien l’effet de la clause n’est pas seulement de minimis et la clause est genuine. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels avant et après déclenchement restent uniquement des paiements de principal et d’intérêt sur le principal restant dû.
   - Si l’événement déclencheur n’est pas directement lié aux risques et coûts basiques de prêt, les flux de tous les scénarios possibles ne doivent pas être significativement différents d’un instrument identique sans cette clause.
   - L’effet de la clause est au plus de minimis, ou la clause n’est pas genuine, le cas échéant.
   - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause de déclenchement n’empêche pas le test SPPI: IFRS 9 B4.1.10 exige d’examiner les flux avant et après la modification, dans tous les scénarios contractuellement possibles. Si les flux restent des paiements de principal et d’intérêt, ou si l’effet est seulement de minimis / non genuine au sens d’IFRS 9 B4.1.18, l’actif peut rester SPPI; il faudra alors aussi que le modèle économique soit « hold to collect » selon IFRS 9 4.1.2.

**Implications pratiques**: Si ces conditions sont remplies, l’instrument peut être classé au coût amorti; sinon, il bascule hors des catégories fondées sur SPPI.

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

### 2. Juste valeur par OCI

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels avant et après déclenchement satisfont le test SPPI.
   - Lorsque le déclencheur n’est pas directement lié aux risques et coûts basiques de prêt, les flux ne sont pas significativement différents d’un instrument identique sans cette clause dans tous les scénarios contractuellement possibles.
   - Toute incidence de la clause est de minimis ou la clause n’est pas genuine, le cas échéant.
   - L’actif est détenu dans un modèle économique visant à la fois l’encaissement des flux contractuels et la vente.

**Raisonnement**:
Dans cette situation, la présence d’une clause modifiant les flux n’exclut pas en soi SPPI; IFRS 9 B4.1.10 et B4.1.10A permettent encore le critère de prêt basique si les flux demeurent assimilables à principal et intérêt dans tous les scénarios pertinents. Si ce test est satisfait, la catégorie FVOCI est possible seulement si le modèle économique combine encaissement des flux et ventes, conformément à IFRS 9 4.1.2A.

**Implications pratiques**: Si SPPI est respecté et que le modèle économique est collect-and-sell, l’instrument peut être classé en FVOCI.

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
   - La clause modifiant les flux fait échouer le test SPPI.
   - Ou bien les flux dans un ou plusieurs scénarios contractuellement possibles sont significativement différents de ceux d’un instrument identique sans la clause.
   - Ou bien l’effet de la clause n’est pas seulement de minimis et la clause est genuine.

**Raisonnement**:
Dans cette situation, la JV par résultat s’applique si la clause ou l’événement déclencheur fait échouer SPPI, par exemple si les flux après déclenchement ne restent pas des paiements de principal et d’intérêt, ou diffèrent significativement d’un prêt basique selon IFRS 9 B4.1.10 et B4.1.10A. IFRS 9 4.1.4 prévoit alors la JV par résultat dès lors que l’actif ne relève ni du coût amorti ni du FVOCI.

**Implications pratiques**: Si SPPI n’est pas respecté, l’instrument est classé à la juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.10

    >If a financial asset contains a contractual term that could change the timing or amount of contractual cash flows (for example, if the asset can be prepaid before maturity or its term can be extended), the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest on the principal amount outstanding. To make this determination, the entity must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows, irrespective of the probability of the change in contractual cash flows occurring. The entity may also need to assess the nature of any contingent event (ie the trigger) that would change the timing or amount of the contractual cash flows. While the nature of the contingent event in itself is not a determinative factor in assessing whether the contractual cash flows are solely payments of principal and interest, it may be an indicator. For example, compare a financial instrument with an interest rate that is reset to a higher rate if the debtor misses a particular number of payments to a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level. It is more likely in the former case that the contractual cash flows over the life of the instrument will be solely payments of principal and interest on the principal amount outstanding because of the relationship between missed payments and an increase in credit risk. In the former case, the nature of the contingent event relates directly to, and the contractual cash flows change in the same direction as, changes in basic lending risks and costs. (See also paragraph B4.1.18.)
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.
 - ifrs9 B4.1.18

    >A contractual cash flow characteristic does not affect the classification of the financial asset if it could have only a de minimis effect on the contractual cash flows of the financial asset. To make this determination, an entity must consider the possible effect of the contractual cash flow characteristic in each reporting period and cumulatively over the life of the financial instrument. In addition, if a contractual cash flow characteristic could have an effect on the contractual cash flows that is more than de minimis (either in a single reporting period or cumulatively) but that cash flow characteristic is not genuine, it does not affect the classification of a financial asset. A cash flow characteristic is not genuine if it affects the instrument’s contractual cash flows only on the occurrence of an event that is extremely rare, highly abnormal and very unlikely to occur.