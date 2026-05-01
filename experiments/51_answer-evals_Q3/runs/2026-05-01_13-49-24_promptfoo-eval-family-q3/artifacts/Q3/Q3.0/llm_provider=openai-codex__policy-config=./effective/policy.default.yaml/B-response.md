# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Qu'est-ce qu'un actif dont les termes contractuels donnent droit uniquement au paiement du principal et des intérêts ?

**Reformulation**:
>Détermination du critère SPPI (« solely payments of principal and interest ») pour la classification des actifs financiers selon IFRS 9

## Documentation
**Consultée**
   - IFRS-S (standard) (`ifrs9`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question est interprétée comme une demande de définition du critère SPPI au sens d’IFRS 9, sans actif précis ni modèle économique déterminé.
   - En l’absence de faits spécifiques, l’applicabilité des traitements est appréciée de manière conditionnelle selon le modèle économique et le respect effectif du critère SPPI.

## Recommandation

**OUI SOUS CONDITIONS**

Un actif répond au critère SPPI lorsque ses flux contractuels sont uniquement des paiements de principal et d’intérêts dans le cadre d’un prêt basique. S’il respecte ce critère, il peut relever du coût amorti ou de la FVOCI selon le modèle économique ; sinon, il relève de la FVTPL.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est de détenir les actifs pour en percevoir les flux contractuels. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par l’encaissement des flux contractuels et par la vente. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Les flux contractuels ne sont pas uniquement des paiements de principal et d’intérêts.<br>- Ou l’actif ne relève d’aucun des deux modèles économiques SPPI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est de détenir les actifs pour en percevoir les flux contractuels.

**Raisonnement**:
Dans cette situation, le coût amorti n’est pertinent que si l’actif remplit le critère SPPI et est détenu dans un modèle visant à encaisser les flux contractuels. IFRS 9 4.1.2 exige à la fois un objectif de détention pour encaissement et des flux constitués uniquement de principal et d’intérêts ; IFRS 9 4.1.3 précise que le principal est la juste valeur initiale et que l’intérêt rémunère notamment la valeur temps de l’argent et le risque de crédit.

**Implications pratiques**: Si le critère SPPI est satisfait et que le modèle est « hold to collect », la mesure ultérieure est au coût amorti.

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

### 2. Juste valeur par autres éléments du résultat global

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par l’encaissement des flux contractuels et par la vente.

**Raisonnement**:
Dans cette situation, la FVOCI n’est possible que si l’actif respecte d’abord le critère SPPI, puis si le modèle économique combine encaissement des flux et vente. IFRS 9 4.1.2A retient exactement ces deux conditions ; IFRS 9 B4.1.7A précise qu’un actif SPPI correspond à une « basic lending arrangement », sans exposition à des risques comme les prix d’actions ou de matières premières.

**Implications pratiques**: Si le critère SPPI est satisfait et que le modèle est « collect and sell », la mesure ultérieure est à la FVOCI.

**Référence**:
 - ifrs9 4.1.2A

    >A financial asset shall be measured at fair value through other comprehensive income if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.

### 3. Juste valeur par résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les flux contractuels ne sont pas uniquement des paiements de principal et d’intérêts.
   - Ou l’actif ne relève d’aucun des deux modèles économiques SPPI.

**Raisonnement**:
Dans cette situation, la FVTPL s’applique si l’actif ne respecte pas le critère SPPI ou ne relève pas des deux catégories fondées sur SPPI. IFRS 9 4.1.4 pose la FVTPL comme catégorie résiduelle ; IFRS 9 B4.1.9 indique qu’un levier contractuel empêche le test SPPI, et IFRS 9 B4.1.14 illustre qu’un instrument convertible en un nombre fixe d’actions ne constitue pas un paiement de principal et d’intérêts.

**Implications pratiques**: Si le critère SPPI échoue, ou si l’actif n’entre pas dans les catégories SPPI, la mesure ultérieure est à la FVTPL.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 B4.1.9

    >Leverage is a contractual cash flow characteristic of some financial assets. Leverage increases the variability of the contractual cash flows with the result that they do not have the economic characteristics of interest. Stand‑alone option, forward and swap contracts are examples of financial assets that include such leverage. Thus, such contracts do not meet the condition in paragraphs 4.1.2(b) and 4.1.2A(b) and cannot be subsequently measured at amortised cost or fair value through other comprehensive income.
 - ifrs9 B4.1.14

    >The following examples illustrate contractual cash flows that are not solely payments of principal and interest on the principal amount outstanding. This list of examples is not exhaustive.
InstrumentFInstrumentFisabondthatisconvertibleintoafixednumberofequityinstrumentsoftheissuer.The holder would analyse the convertible bond in its entirety.
The contractual cash flows are not payments of principal and interest on the principal amount outstanding because they reflect a return that is inconsistent with a basic lending arrangement (see paragraph B4.1.7A); ie the return is linked to the value of the equity of the issuer.
InstrumentGInstrumentGisaloanthatpaysaninversefloatinginterestrate(ietheinterestratehasaninverserelationshiptomarketinterestrates).The contractual cash flows are not solely payments of principal and interest on the principal amount outstanding.
The interest amounts are not consideration for the time value of money on the principal amount outstanding.
InstrumentHInstrumentHisaperpetualinstrumentbuttheissuermaycalltheinstrumentatanypointandpaytheholdertheparamountplusaccruedinterestdue.InstrumentHpaysamarketinterestratebutpaymentofinterestcannotbemadeunlesstheissuerisabletoremainsolventimmediatelyafterwards.Deferredinterestdoesnotaccrueadditionalinterest.The contractual cash flows are not payments of principal and interest on the principal amount outstanding. That is because the issuer may be required to defer interest payments and additional interest does not accrue on those deferred interest amounts. As a result, interest amounts are not consideration for the time value of money on the principal amount outstanding.
If interest accrued on the deferred amounts, the contractual cash flows could be payments of principal and interest on the principal amount outstanding.
The fact that Instrument H is perpetual does not in itself mean that the contractual cash flows are not payments of principal and interest on the principal amount outstanding. In effect, a ...