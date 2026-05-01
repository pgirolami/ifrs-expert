# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Certains instruments prévoient des termes contractuels pouvant modifier l’échéancier ou le montant des flux de trésorerie, notamment en cas d’événement déclencheur : un tel instrument peut-il néanmoins être considéré comme respectant le critère de « prêt basique » (SPPI) ?

**Reformulation**:
>Déterminer si des clauses contractuelles pouvant modifier le calendrier ou le montant des flux de trésorerie, y compris des clauses conditionnelles avec événement déclencheur, restent compatibles avec le critère SPPI d’un « prêt basique » au sens d’IFRS 9, et donc avec les catégories de classement ultérieur correspondantes.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose qu’il s’agit d’un actif financier relevant d’IFRS 9 et que la question porte uniquement sur le critère SPPI, pas sur l’appréciation détaillée du business model.
   - On suppose qu’aucun autre fait non mentionné (effet de levier, indexation sur actions/commodities, clause de conversion en actions, structure non-recourse ou tranchée complexe) ne vient, à lui seul, faire échouer le test SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, un terme contractuel pouvant modifier le calendrier ou le montant des flux peut rester compatible avec SPPI si, dans les scénarios contractuellement possibles, les flux demeurent des paiements de principal et d’intérêt d’un prêt basique et ne sont pas significativement différents lorsqu’un déclencheur non lié aux risques de prêt basiques intervient. Sinon, l’actif bascule en FVTPL.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.<br>- La clause ne crée pas des flux significativement différents d’un instrument identique sans cette clause lorsque le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique.<br>- Les flux avant et après modification restent des paiements de principal et d’intérêt. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est à la fois d’encaisser les flux contractuels et de vendre.<br>- La clause conditionnelle respecte SPPI selon l’analyse avant/après modification.<br>- En cas de déclencheur non directement lié aux risques et coûts d’un prêt basique, les flux restent non significativement différents d’un instrument identique sans cette clause. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - La clause conditionnelle introduit une exposition incompatible avec un prêt basique ou fait échouer le test SPPI.<br>- Les flux contractuels possibles deviennent significativement différents d’un instrument de prêt basique comparable. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique visant à encaisser les flux contractuels.
   - La clause ne crée pas des flux significativement différents d’un instrument identique sans cette clause lorsque le déclencheur n’est pas directement lié aux risques et coûts d’un prêt basique.
   - Les flux avant et après modification restent des paiements de principal et d’intérêt.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si la clause de modification des flux reste compatible avec SPPI. IFRS 9 B4.1.10 exige d’analyser les flux avant et après le changement, et IFRS 9 B4.1.10A précise que, si le déclencheur ne se rattache pas directement aux risques et coûts d’un prêt basique, les flux ne doivent pas être significativement différents dans tous les scénarios contractuels possibles. Si ce test SPPI est satisfait, le classement au coût amorti reste ouvert sous le business model de détention pour encaissement (IFRS 9 4.1.2).

**Implications pratiques**: Si ces conditions sont remplies, l’instrument peut rester éligible au coût amorti malgré la clause conditionnelle.

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
   - L’actif est détenu dans un modèle économique dont l’objectif est à la fois d’encaisser les flux contractuels et de vendre.
   - La clause conditionnelle respecte SPPI selon l’analyse avant/après modification.
   - En cas de déclencheur non directement lié aux risques et coûts d’un prêt basique, les flux restent non significativement différents d’un instrument identique sans cette clause.

**Raisonnement**:
Dans cette situation, la présence d’un déclencheur n’empêche pas automatiquement le classement en FVOCI. Les mêmes exigences SPPI s’appliquent: analyse des flux avant/après modification selon IFRS 9 B4.1.10 et, si le déclencheur n’est pas directement lié aux risques de prêt basiques, absence de différence significative dans tous les scénarios selon IFRS 9 B4.1.10A. Si SPPI est respecté et que l’objectif du business model combine encaissement et vente, IFRS 9 4.1.2A permet FVOCI.

**Implications pratiques**: Si SPPI est préservé et que le business model est collect-and-sell, le classement FVOCI reste possible.

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
   - La clause conditionnelle introduit une exposition incompatible avec un prêt basique ou fait échouer le test SPPI.
   - Les flux contractuels possibles deviennent significativement différents d’un instrument de prêt basique comparable.

**Raisonnement**:
Dans cette situation, FVTPL s’applique si la clause de déclenchement fait échouer SPPI, par exemple si elle introduit une exposition non compatible avec un prêt basique ou des flux significativement différents. IFRS 9 B4.1.7A exclut les expositions à des risques sans lien avec un prêt basique, et IFRS 9 4.1.4 impose alors FVTPL comme catégorie résiduelle. Ainsi, ce traitement ne vaut ici que si l’analyse SPPI de la clause est négative.

**Implications pratiques**: Si SPPI échoue à cause de la clause, l’actif ne peut pas être classé au coût amorti ni en FVOCI et doit être en FVTPL.

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