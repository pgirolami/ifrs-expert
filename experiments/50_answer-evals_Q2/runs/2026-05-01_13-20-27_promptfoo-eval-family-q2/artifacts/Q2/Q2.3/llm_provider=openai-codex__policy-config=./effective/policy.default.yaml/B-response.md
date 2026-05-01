# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI (« prêt basique ») en IFRS 9 pour un actif financier dont des clauses contractuelles contingentes peuvent modifier le calendrier ou le montant des flux de trésorerie

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier entrant dans le champ d’IFRS 9.
   - On suppose que la question porte sur une clause contractuelle contingente modifiant le calendrier ou le montant des flux de trésorerie, sans autres caractéristiques non décrites.
   - Le modèle économique de gestion de l’actif n’est pas précisé ; l’analyse de classement ultérieur est donc conditionnelle à ce point.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un instrument avec clause contingente peut encore satisfaire le test SPPI si, en toutes circonstances contractuellement possibles, les flux restent des paiements de principal et d’intérêt ou ne sont pas significativement différents d’un instrument identique sans cette clause (IFRS 9 B4.1.10, B4.1.10A). Si la clause introduit une exposition à des risques non compatibles avec un prêt basique, le test SPPI échoue et l’actif relève alors du FVTPL (IFRS 9 B4.1.7A, 4.1.4).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Le modèle économique est de détenir l’actif pour encaisser les flux contractuels.<br>- En toutes circonstances contractuellement possibles, la clause ne crée pas des flux incompatibles avec des paiements de principal et d’intérêt.<br>- La clause n’entraîne pas des flux significativement différents d’un instrument identique sans cette caractéristique lorsqu’elle n’est pas directement liée aux risques et coûts de prêt basiques. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - Le modèle économique est atteint à la fois par l’encaissement des flux contractuels et par la vente d’actifs financiers.<br>- La clause contingente satisfait au test SPPI après examen des flux avant et après la modification.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts de prêt basiques, les flux restent non significativement différents de ceux d’un instrument identique sans cette clause. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause contingente introduit une exposition incompatible avec un prêt basique.<br>- Ou les flux potentiels deviennent significativement différents d’un instrument de référence lorsque l’analyse IFRS 9 B4.1.10A est requise.<br>- Ou le modèle économique ne permet ni le coût amorti ni le FVOCI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique est de détenir l’actif pour encaisser les flux contractuels.
   - En toutes circonstances contractuellement possibles, la clause ne crée pas des flux incompatibles avec des paiements de principal et d’intérêt.
   - La clause n’entraîne pas des flux significativement différents d’un instrument identique sans cette caractéristique lorsqu’elle n’est pas directement liée aux risques et coûts de prêt basiques.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause contingente ne fait pas échouer le test SPPI et si l’actif est détenu dans un modèle visant à collecter les flux contractuels (IFRS 9 4.1.2, B4.1.10). IFRS 9 admet qu’un terme pouvant modifier le montant ou l’échéancier des flux peut rester compatible avec un prêt basique, à condition d’examiner les flux avant et après la modification ; pour certaines clauses non liées directement aux risques de prêt basiques, les flux ne doivent pas être significativement différents d’un instrument identique sans la clause (IFRS 9 B4.1.10A).

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être classé au coût amorti ; sinon ce traitement n’est pas disponible.

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
   - Le modèle économique est atteint à la fois par l’encaissement des flux contractuels et par la vente d’actifs financiers.
   - La clause contingente satisfait au test SPPI après examen des flux avant et après la modification.
   - Si le déclencheur n’est pas directement lié aux risques et coûts de prêt basiques, les flux restent non significativement différents de ceux d’un instrument identique sans cette clause.

**Raisonnement**:
Dans cette situation, le FVOCI n’est envisageable que si la clause contingente respecte SPPI selon la même analyse que ci-dessus et si le modèle économique combine encaissement des flux contractuels et vente (IFRS 9 4.1.2A, B4.1.10). Le seul fait qu’un événement déclencheur puisse modifier les flux n’exclut donc pas ce classement, sauf si cette clause introduit une exposition étrangère à un prêt basique ou des écarts significatifs incompatibles avec IFRS 9 B4.1.10A.

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être classé en FVOCI ; à défaut, ce traitement n’est pas disponible.

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
   - La clause contingente introduit une exposition incompatible avec un prêt basique.
   - Ou les flux potentiels deviennent significativement différents d’un instrument de référence lorsque l’analyse IFRS 9 B4.1.10A est requise.
   - Ou le modèle économique ne permet ni le coût amorti ni le FVOCI.

**Raisonnement**:
Dans cette situation, le FVTPL s’applique si la clause contingente fait échouer SPPI ou si, même avec SPPI, les conditions de modèle économique pour le coût amorti ou le FVOCI ne sont pas remplies (IFRS 9 4.1.4). C’est notamment le cas si la clause expose l’investisseur à des risques ou à une volatilité non liés à un prêt basique, par exemple des variables de prix d’actions ou de matières premières, ce qui est incompatible avec IFRS 9 B4.1.7A et B4.1.8A.

**Implications pratiques**: Si l’une de ces conditions est présente, l’actif doit être évalué à la juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.8A

    >In assessing whether the contractual cash flows of a financial asset are consistent with a basic lending arrangement, an entity may have to consider the different elements of interest separately. The assessment of interest focuses on what an entity is being compensated for, rather than how much compensation an entity receives. Nonetheless, the amount of compensation an entity receives may indicate that the entity is being compensated for something other than basic lending risks and costs. Contractual cash flows are inconsistent with a basic lending arrangement if they are indexed to a variable that is not a basic lending risk or cost (for example, the value of equity instruments or the price of a commodity) or if they represent a share of the debtor’s revenue or profit, even if such contractual terms are common in the market in which the entity operates.