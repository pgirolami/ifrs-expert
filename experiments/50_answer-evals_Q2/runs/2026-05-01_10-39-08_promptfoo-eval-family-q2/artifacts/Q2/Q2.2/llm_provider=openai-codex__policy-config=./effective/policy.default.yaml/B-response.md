# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Lorsqu’un instrument comporte des clauses contractuelles susceptibles d’altérer l’échéancier ou le montant des flux de trésorerie, par exemple à la suite d’un événement déclencheur, respecte-t-il le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Évaluation du critère SPPI (« solely payments of principal and interest ») pour un actif financier comportant des clauses contingentes pouvant modifier le montant ou l’échéancier des flux contractuels, et incidence sur sa classification IFRS 9.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias33`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier relevant d’IFRS 9.
   - On suppose que la question porte uniquement sur l’effet des clauses contractuelles contingentes sur le test SPPI, et non sur une analyse factuelle complète du modèle économique de détention.
   - En l’absence de termes contractuels détaillés, on suppose que l’instrument peut soit conserver des flux compatibles avec un prêt basique dans tous les scénarios contractuels, soit au contraire créer une exposition à des risques non basiques.

## Recommandation

**OUI SOUS CONDITIONS**

Une clause modifiant le montant ou l’échéancier des flux n’exclut pas automatiquement le SPPI. L’instrument respecte le critère seulement si, dans tous les scénarios contractuels pertinents, les flux restent des paiements de principal et d’intérêt compatibles avec un prêt basique; sinon, il échoue au SPPI et relève du FVTPL.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Les flux contractuels, dans tous les scénarios contractuels possibles, ne sont pas significativement différents de ceux d’un instrument sans la clause contingente lorsque le déclencheur n’est pas directement lié aux risques et coûts de prêt basiques.<br>- La clause n’introduit pas d’exposition à des risques ou à une volatilité incompatibles avec un prêt basique.<br>- L’actif est détenu dans un modèle économique visant à collecter les flux contractuels. |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - Les flux contractuels restent SPPI malgré la clause contingente.<br>- Si le déclencheur n’est pas directement lié aux risques et coûts de prêt basiques, les flux de tous les scénarios contractuels possibles ne sont pas significativement différents de ceux d’un instrument sans cette clause.<br>- L’actif est détenu dans un modèle économique de collecte et de vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause introduit une exposition à des variables non liées aux risques et coûts de prêt basiques, ou produit des flux significativement différents incompatibles avec SPPI.<br>- L’actif ne remplit pas les conditions du coût amorti ou de la JVOCI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels, dans tous les scénarios contractuels possibles, ne sont pas significativement différents de ceux d’un instrument sans la clause contingente lorsque le déclencheur n’est pas directement lié aux risques et coûts de prêt basiques.
   - La clause n’introduit pas d’exposition à des risques ou à une volatilité incompatibles avec un prêt basique.
   - L’actif est détenu dans un modèle économique visant à collecter les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause contingente ne fait pas sortir l’instrument du cadre d’un prêt basique et si les flux pouvant survenir avant et après le déclencheur restent uniquement principal et intérêts (IFRS 9 B4.1.10, B4.1.10A). Même si le SPPI est respecté, cette catégorie ne s’applique que si l’actif est détenu dans un modèle économique visant à collecter les flux contractuels (IFRS 9 4.1.2).

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être classé au coût amorti.

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

### 2. Juste valeur par OCI

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels restent SPPI malgré la clause contingente.
   - Si le déclencheur n’est pas directement lié aux risques et coûts de prêt basiques, les flux de tous les scénarios contractuels possibles ne sont pas significativement différents de ceux d’un instrument sans cette clause.
   - L’actif est détenu dans un modèle économique de collecte et de vente.

**Raisonnement**:
Dans cette situation, la JVOCI n’est envisageable que si la clause contingente passe le test SPPI selon la même analyse des flux avant et après déclenchement (IFRS 9 B4.1.10, B4.1.10A). En plus, l’actif doit être détenu dans un modèle économique dont l’objectif est à la fois d’encaisser les flux contractuels et de vendre les actifs financiers (IFRS 9 4.1.2A).

**Implications pratiques**: Si le SPPI est satisfait et que le modèle économique est collecter et vendre, l’actif peut être classé en JVOCI.

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
   - La clause introduit une exposition à des variables non liées aux risques et coûts de prêt basiques, ou produit des flux significativement différents incompatibles avec SPPI.
   - L’actif ne remplit pas les conditions du coût amorti ou de la JVOCI.

**Raisonnement**:
Dans cette situation, le FVTPL s’applique si la clause contingente expose le porteur à des risques ou à une volatilité incompatibles avec un prêt basique, de sorte que les flux ne sont pas SPPI (IFRS 9 B4.1.7A, B4.1.14). IFRS 9 prévoit alors que l’actif est mesuré à la juste valeur par résultat dès lors qu’il ne remplit pas les conditions du coût amorti ou de la JVOCI (IFRS 9 4.1.4).

**Implications pratiques**: Si le SPPI échoue en raison de la clause, la classification résiduelle est le FVTPL.

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