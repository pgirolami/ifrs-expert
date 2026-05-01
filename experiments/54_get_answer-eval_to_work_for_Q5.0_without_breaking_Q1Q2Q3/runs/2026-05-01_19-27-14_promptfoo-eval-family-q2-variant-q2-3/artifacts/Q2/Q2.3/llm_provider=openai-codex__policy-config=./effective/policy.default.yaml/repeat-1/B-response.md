# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI en IFRS 9 pour un actif financier comportant des clauses contractuelles pouvant modifier le calendrier ou le montant des flux de trésorerie en cas d’événement déclencheur.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier relevant d’IFRS 9.
   - On suppose que la question porte uniquement sur l’appréciation du critère SPPI d’une clause contractuelle modifiant les flux en cas d’événement déclencheur, sans autres caractéristiques disqualifiantes non mentionnées.
   - On suppose que le modèle économique de détention n’est pas précisé dans les faits et doit donc être apprécié séparément de l’analyse SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut encore satisfaire le critère SPPI si, dans tous les scénarios contractuellement possibles, les flux avant et après le changement restent des paiements de principal et d’intérêt, et si la clause n’introduit pas une exposition à des risques non compatibles avec un prêt basique (IFRS 9 B4.1.10, B4.1.10A). La catégorie de mesure dépend ensuite du modèle économique (IFRS 9 4.1.2, 4.1.2A).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêt.<br>- La clause ne crée pas d’exposition à des risques ou à une volatilité non liés à un prêt basique.<br>- L’actif est détenu dans un modèle économique dont l’objectif est de collecter les flux contractuels. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêt.<br>- Dans tous les scénarios contractuellement possibles, la clause ne produit pas des flux significativement différents de ceux d’un instrument comparable sans cette clause, lorsque IFRS 9 B4.1.10A s’applique.<br>- L’actif est détenu dans un modèle économique dont l’objectif est à la fois de collecter les flux contractuels et de vendre. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause contractuelle modifiant les flux fait perdre le caractère SPPI.<br>- L’instrument ne remplit donc pas les conditions des catégories fondées sur SPPI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêt.
   - La clause ne crée pas d’exposition à des risques ou à une volatilité non liés à un prêt basique.
   - L’actif est détenu dans un modèle économique dont l’objectif est de collecter les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause déclenchée ne fait pas perdre le caractère SPPI : il faut apprécier les flux pouvant survenir avant et après le changement, indépendamment de la probabilité de survenance (IFRS 9 B4.1.10). Si ces flux restent ceux d’un prêt basique et que l’actif est détenu pour encaisser les flux contractuels, la mesure au coût amorti est permise (IFRS 9 4.1.2, 4.1.3, B4.1.10A).

**Implications pratiques**: Si ces conditions sont remplies, l’instrument peut rester dans une catégorie fondée sur SPPI et être évalué au coût amorti selon le modèle économique.

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
 - ifrs9 B4.1.10

    >If a financial asset contains a contractual term that could change the timing or amount of contractual cash flows (for example, if the asset can be prepaid before maturity or its term can be extended), the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest on the principal amount outstanding. To make this determination, the entity must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows, irrespective of the probability of the change in contractual cash flows occurring. The entity may also need to assess the nature of any contingent event (ie the trigger) that would change the timing or amount of the contractual cash flows. While the nature of the contingent event in itself is not a determinative factor in assessing whether the contractual cash flows are solely payments of principal and interest, it may be an indicator. For example, compare a financial instrument with an interest rate that is reset to a higher rate if the debtor misses a particular number of payments to a financial instrument with an interest rate that is reset to a higher rate if a specified equity index reaches a particular level. It is more likely in the former case that the contractual cash flows over the life of the instrument will be solely payments of principal and interest on the principal amount outstanding because of the relationship between missed payments and an increase in credit risk. In the former case, the nature of the contingent event relates directly to, and the contractual cash flows change in the same direction as, changes in basic lending risks and costs. (See also paragraph B4.1.18.)
 - ifrs9 B4.1.10A

    >In some cases, a contingent feature gives rise to contractual cash flows that are consistent with a basic lending arrangement both before and after the change in contractual cash flows, but the nature of the contingent event itself does not relate directly to changes in basic lending risks and costs. For example, the interest rate on a loan is adjusted by a specified amount if the debtor achieves a contractually specified reduction in carbon emissions. In such a case, when applying paragraph B4.1.10, the financial asset has contractual cash flows that are solely payments of principal and interest on the principal amount outstanding if, and only if, in all contractually possible scenarios, the contractual cash flows would not be significantly different from the contractual cash flows on a financial instrument with identical contractual terms, but without such a contingent feature. In some circumstances, the entity may be able to make that determination by performing a qualitative assessment; but, in other circumstances, it may be necessary to perform a quantitative assessment. If it is clear, with little or no analysis, that the contractual cash flows are not significantly different, an entity need not perform a detailed assessment.

### 2. Juste valeur par autres éléments du résultat global

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels avant et après l’événement déclencheur restent uniquement des paiements de principal et d’intérêt.
   - Dans tous les scénarios contractuellement possibles, la clause ne produit pas des flux significativement différents de ceux d’un instrument comparable sans cette clause, lorsque IFRS 9 B4.1.10A s’applique.
   - L’actif est détenu dans un modèle économique dont l’objectif est à la fois de collecter les flux contractuels et de vendre.

**Raisonnement**:
Dans cette situation, la présence d’un déclencheur n’empêche pas à elle seule le SPPI ; il faut vérifier que les flux modifiés restent des paiements de principal et d’intérêt dans tous les scénarios contractuels pertinents (IFRS 9 B4.1.10, B4.1.10A). Si ce test est satisfait et que le modèle économique combine encaissement et vente, la catégorie FVOCI est applicable (IFRS 9 4.1.2A).

**Implications pratiques**: Si le test SPPI est respecté et que le modèle économique est mixte encaissement/vente, l’instrument peut être classé en FVOCI.

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
   - La clause contractuelle modifiant les flux fait perdre le caractère SPPI.
   - L’instrument ne remplit donc pas les conditions des catégories fondées sur SPPI.

**Raisonnement**:
Dans cette situation, la JV résultat s’impose si la clause déclenchée fait échouer le test SPPI, par exemple parce qu’elle expose l’investisseur à des risques non liés à un prêt basique ou à des flux non limités à principal et intérêt (IFRS 9 B4.1.7A, B4.1.14). IFRS 9 prévoit alors la JV résultat comme catégorie résiduelle lorsque les conditions du coût amorti ou de la FVOCI ne sont pas remplies (IFRS 9 4.1.4).

**Implications pratiques**: Si le déclencheur introduit une exposition incompatible avec un prêt basique, l’actif doit être évalué à la juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.
 - ifrs9 B4.1.14

    >The following examples illustrate contractual cash flows that are not solely payments of principal and interest on the principal amount outstanding. This list of examples is not exhaustive.
InstrumentFInstrumentFisabondthatisconvertibleintoafixednumberofequityinstrumentsoftheissuer.The holder would analyse the convertible bond in its entirety.
The contractual cash flows are not payments of principal and interest on the principal amount outstanding because they reflect a return that is inconsistent with a basic lending arrangement (see paragraph B4.1.7A); ie the return is linked to the value of the equity of the issuer.
InstrumentGInstrumentGisaloanthatpaysaninversefloatinginterestrate(ietheinterestratehasaninverserelationshiptomarketinterestrates).The contractual cash flows are not solely payments of principal and interest on the principal amount outstanding.
The interest amounts are not consideration for the time value of money on the principal amount outstanding.
InstrumentHInstrumentHisaperpetualinstrumentbuttheissuermaycalltheinstrumentatanypointandpaytheholdertheparamountplusaccruedinterestdue.InstrumentHpaysamarketinterestratebutpaymentofinterestcannotbemadeunlesstheissuerisabletoremainsolventimmediatelyafterwards.Deferredinterestdoesnotaccrueadditionalinterest.The contractual cash flows are not payments of principal and interest on the principal amount outstanding. That is because the issuer may be required to defer interest payments and additional interest does not accrue on those deferred interest amounts. As a result, interest amounts are not consideration for the time value of money on the principal amount outstanding.
If interest accrued on the deferred amounts, the contractual cash flows could be payments of principal and interest on the principal amount outstanding.
The fact that Instrument H is perpetual does not in itself mean that the contractual cash flows are not payments of principal and interest on the principal amount outstanding. In effect, a ...