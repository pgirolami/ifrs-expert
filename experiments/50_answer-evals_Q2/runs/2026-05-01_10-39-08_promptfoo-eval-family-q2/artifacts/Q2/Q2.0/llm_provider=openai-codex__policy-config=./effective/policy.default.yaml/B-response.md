# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Un instrument assorti de termes contractuels pouvant modifier l'échéancier ou le montant des flux de
trésorerie (par exemple, à la suite de la survenance d'un événement déclencheur) peut-il respecter le critère
de « prêt basique » (SPPI) ?

**Reformulation**:
>Déterminer si des flux contractuels variables ou contingents peuvent satisfaire au critère SPPI (« prêt basique ») d’IFRS 9 et, par conséquent, quelles bases de classement ultérieur d’un actif financier restent ouvertes.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias2`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question porte sur un actif financier de type dette relevant d’IFRS 9, et non sur un instrument de capitaux propres.
   - Les faits fournis ne permettent pas d’identifier le modèle économique ; la réponse vise donc d’abord le respect du critère SPPI, puis les bases de classement qui restent ouvertes selon le modèle économique.
   - Le terme contractuel envisagé peut modifier l’échéancier ou le montant des flux, y compris via un événement déclencheur contractuel.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut respecter SPPI si, dans tous les scénarios contractuels pertinents, les flux restent uniquement des remboursements de principal et d’intérêts d’un prêt basique et ne diffèrent pas de façon significative d’un instrument sans cette clause. Sinon, l’actif échoue au test SPPI et relève du FVTPL.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêts sur le principal restant dû.<br>- La clause contingente ne crée pas d’écart significatif de flux par rapport à un instrument identique sans cette clause.<br>- La caractéristique n’introduit ni levier ni exposition à des risques incompatibles avec un prêt basique.<br>- Le modèle économique est de détenir l’actif pour encaisser les flux contractuels. |
| 2. Juste valeur par OCI - titres de dette | OUI SOUS CONDITIONS | - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêts sur le principal restant dû.<br>- La clause contingente ne crée pas d’écart significatif de flux par rapport à un instrument identique sans cette clause.<br>- La caractéristique n’introduit ni levier ni exposition à des risques incompatibles avec un prêt basique.<br>- Le modèle économique est atteint à la fois par l’encaissement des flux contractuels et par la vente des actifs financiers. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause modifiant les flux fait échouer le test SPPI, notamment en créant une exposition à des risques ou une volatilité étrangers à un prêt basique.<br>- Ou les flux contractuels possibles deviennent significativement différents de ceux d’un instrument identique sans la clause contingente. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêts sur le principal restant dû.
   - La clause contingente ne crée pas d’écart significatif de flux par rapport à un instrument identique sans cette clause.
   - La caractéristique n’introduit ni levier ni exposition à des risques incompatibles avec un prêt basique.
   - Le modèle économique est de détenir l’actif pour encaisser les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause contractuelle modifiant les flux ne fait pas perdre le caractère SPPI : il faut apprécier les flux avant et après le changement, indépendamment de la probabilité de survenance du déclencheur (IFRS 9 B4.1.10). Si, dans tous les scénarios contractuels, les flux restent des paiements de principal et d’intérêts d’un prêt basique et que le modèle économique est de détenir pour encaisser, le classement au coût amorti reste ouvert (IFRS 9 4.1.2, B4.1.10A, B4.1.18).

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être mesuré ultérieurement au coût amorti ; sinon cette base est exclue.

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

### 2. Juste valeur par OCI - titres de dette

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêts sur le principal restant dû.
   - La clause contingente ne crée pas d’écart significatif de flux par rapport à un instrument identique sans cette clause.
   - La caractéristique n’introduit ni levier ni exposition à des risques incompatibles avec un prêt basique.
   - Le modèle économique est atteint à la fois par l’encaissement des flux contractuels et par la vente des actifs financiers.

**Raisonnement**:
Dans cette situation, le classement en FVOCI pour un instrument de dette reste possible si la clause de variabilité ou de contingence respecte SPPI selon la même analyse que ci-dessus : les flux potentiels doivent demeurer ceux d’un prêt basique (IFRS 9 B4.1.10, B4.1.10A). En plus, le modèle économique doit être atteint à la fois par l’encaissement des flux contractuels et par la vente des actifs (IFRS 9 4.1.2A).

**Implications pratiques**: Si ces conditions sont remplies, le classement en FVOCI pour dette reste disponible ; sinon il ne l’est pas.

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
   - La clause modifiant les flux fait échouer le test SPPI, notamment en créant une exposition à des risques ou une volatilité étrangers à un prêt basique.
   - Ou les flux contractuels possibles deviennent significativement différents de ceux d’un instrument identique sans la clause contingente.

**Raisonnement**:
Dans cette situation, le FVTPL s’applique si la clause qui modifie les flux introduit une exposition incompatible avec un prêt basique, par exemple un lien avec des prix d’actions, de matières premières, un levier, ou des flux significativement différents d’un instrument sans cette clause (IFRS 9 B4.1.7A, B4.1.9, B4.1.10A). IFRS 9 prévoit alors que l’actif est mesuré au FVTPL dès lors qu’il n’est ni au coût amorti ni en FVOCI (IFRS 9 4.1.4).

**Implications pratiques**: Si la clause fait échouer SPPI, le classement résiduel est le FVTPL.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.9

    >Leverage is a contractual cash flow characteristic of some financial assets. Leverage increases the variability of the contractual cash flows with the result that they do not have the economic characteristics of interest. Stand‑alone option, forward and swap contracts are examples of financial assets that include such leverage. Thus, such contracts do not meet the condition in paragraphs 4.1.2(b) and 4.1.2A(b) and cannot be subsequently measured at amortised cost or fair value through other comprehensive income.
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.