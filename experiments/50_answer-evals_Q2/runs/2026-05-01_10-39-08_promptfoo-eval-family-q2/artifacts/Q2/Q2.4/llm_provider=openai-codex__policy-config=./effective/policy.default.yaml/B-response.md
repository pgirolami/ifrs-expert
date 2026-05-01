# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Un instrument peut comporter des dispositions contractuelles entraînant une modification de l’échéancier ou du montant des flux de trésorerie, par exemple à la survenance d’un événement déclencheur. Dans ce cas, peut-il encore répondre au critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Appréciation du critère SPPI d’un actif financier lorsqu’une clause contractuelle peut modifier le calendrier ou le montant des flux de trésorerie en cas d’événement déclencheur.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias33`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question porte uniquement sur l’appréciation du critère SPPI d’un actif financier au regard d’une clause contractuelle modifiant l’échéancier ou le montant des flux de trésorerie en cas d’événement déclencheur.
   - Aucune information n’est fournie sur le modèle économique de détention de l’actif; l’analyse des catégories de mesure est donc conditionnelle à ce point.
   - On suppose que l’instrument est un actif financier relevant d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un tel instrument peut encore satisfaire au critère SPPI si, malgré la clause contingente, les flux contractuels restent compatibles avec un prêt basique dans tous les scénarios contractuels possibles et ne sont pas significativement différents d’un instrument comparable sans cette clause (IFRS 9 B4.1.10, B4.1.10A). Si la clause introduit une exposition à des risques non liés à un prêt basique, le test SPPI échoue et l’actif relève alors du FVTPL (IFRS 9 B4.1.7A, 4.1.4).


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Les flux contractuels restent uniquement des paiements de principal et d’intérêts sur le principal restant dû, avant et après l’événement déclencheur.<br>- Dans tous les scénarios contractuels possibles, la clause ne conduit pas à des flux significativement différents de ceux d’un instrument identique sans cette clause.<br>- L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - Les flux contractuels restent SPPI malgré la clause déclenchée.<br>- Dans tous les scénarios contractuels possibles, l’écart de flux avec un instrument comparable sans la clause n’est pas significatif.<br>- L’actif est détenu dans un modèle économique visant à la fois l’encaissement des flux contractuels et la vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause fait échouer le test SPPI en introduisant des flux incompatibles avec un prêt basique.<br>- Ou bien les conditions de modèle économique du coût amorti ou du FVOCI ne sont pas remplies.<br>- Ou bien l’actif est irrévocablement désigné à la juste valeur par résultat à l’origine pour réduire un mismatch comptable. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels restent uniquement des paiements de principal et d’intérêts sur le principal restant dû, avant et après l’événement déclencheur.
   - Dans tous les scénarios contractuels possibles, la clause ne conduit pas à des flux significativement différents de ceux d’un instrument identique sans cette clause.
   - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause déclenchée ne fait pas perdre le caractère SPPI: il faut apprécier les flux pouvant survenir avant et après le changement, indépendamment de la probabilité de survenance (IFRS 9 B4.1.10). Si, dans tous les scénarios contractuels possibles, les flux demeurent ceux d’un prêt basique et que l’actif est détenu pour encaisser les flux contractuels, la mesure au coût amorti reste possible (IFRS 9 4.1.2, B4.1.10A).

**Implications pratiques**: Si ces conditions sont remplies, la présence d’une clause contingente n’empêche pas, à elle seule, la mesure au coût amorti.

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
   - Les flux contractuels restent SPPI malgré la clause déclenchée.
   - Dans tous les scénarios contractuels possibles, l’écart de flux avec un instrument comparable sans la clause n’est pas significatif.
   - L’actif est détenu dans un modèle économique visant à la fois l’encaissement des flux contractuels et la vente.

**Raisonnement**:
Dans cette situation, la clause contingente n’exclut pas automatiquement le FVOCI si le test SPPI reste satisfait selon l’analyse des flux avant et après modification (IFRS 9 B4.1.10, B4.1.10A). En revanche, cette catégorie n’est applicable que si, en plus, l’actif est détenu dans un modèle économique dont l’objectif est à la fois d’encaisser les flux contractuels et de vendre les actifs financiers (IFRS 9 4.1.2A).

**Implications pratiques**: Si le test SPPI est respecté et que le modèle économique est « collecter et vendre », la présence du déclencheur n’empêche pas le classement en FVOCI.

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
   - La clause fait échouer le test SPPI en introduisant des flux incompatibles avec un prêt basique.
   - Ou bien les conditions de modèle économique du coût amorti ou du FVOCI ne sont pas remplies.
   - Ou bien l’actif est irrévocablement désigné à la juste valeur par résultat à l’origine pour réduire un mismatch comptable.

**Raisonnement**:
Dans cette situation, le FVTPL s’applique si la clause introduit une exposition à des risques ou à une volatilité incompatibles avec un prêt basique, de sorte que les flux ne sont plus uniquement principal et intérêts (IFRS 9 B4.1.7A, B4.1.14). Il s’applique aussi par défaut si les conditions du coût amorti ou du FVOCI ne sont pas remplies, ou sur désignation initiale pour éliminer un décalage comptable (IFRS 9 4.1.4, 4.1.5).

**Implications pratiques**: Si la clause contingente fait perdre le caractère SPPI, l’actif ne peut pas être mesuré au coût amorti ni en FVOCI et bascule en FVTPL.

**Référence**:
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
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 4.1.5

    >Despite paragraphs 4.1.1⁠–⁠4.1.4, an entity may, at initial recognition, irrevocably designate a financial asset as measured at fair value through profit or loss if doing so eliminates or significantly reduces a measurement or recognition inconsistency (sometimes referred to as an ‘accounting mismatch’) that would otherwise arise from measuring assets or liabilities or recognising the gains and losses on them on different bases (see paragraphs B4.1.29⁠–⁠B4.1.32).