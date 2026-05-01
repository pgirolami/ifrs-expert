# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>À quoi correspond un actif dont les flux de trésorerie contractuels ne comprennent que le principal et les intérêts ?

**Reformulation**:
>qualification IFRS 9 d’un actif financier dont les flux de trésorerie contractuels sont uniquement des remboursements de principal et d’intérêts, et identification des catégories de mesure possibles

## Documentation
**Consultée**
   - IAS-S (standard) (`ias7`, `ias39`)
   - IFRS-S (standard) (`ifrs9`, `ifrs17`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - On suppose que l’actif visé est un actif financier entrant dans le champ d’IFRS 9.
   - On suppose que les faits fournis ne précisent pas le modèle économique de détention ni l’existence d’une désignation à la juste valeur par résultat.

## Recommandation

**OUI SOUS CONDITIONS**

Un actif dont les flux contractuels ne comprennent que le principal et les intérêts correspond, en IFRS 9, à un instrument de dette satisfaisant le test SPPI. Cette caractéristique, à elle seule, ne fixe pas la catégorie de mesure: il sera au coût amorti, en FVOCI ou en FVTPL selon le modèle économique ou une éventuelle désignation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est de collecter les flux de trésorerie contractuels. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par la collecte des flux contractuels et par la vente d’actifs financiers. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Le modèle économique ne remplit pas les critères du coût amorti ou de la FVOCI.<br>- Ou l’entité désigne irrévocablement l’actif à la juste valeur par résultat à l’origine pour éliminer ou réduire significativement une incohérence comptable. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est de collecter les flux de trésorerie contractuels.

**Raisonnement**:
Dans cette situation, le seul fait que les flux soient uniquement du principal et des intérêts satisfait la jambe SPPI, mais cela ne suffit pas pour conclure au coût amorti. D’après IFRS 9 4.1.2, cette mesure ne s’applique que si l’actif est détenu dans un modèle dont l’objectif est de collecter les flux contractuels; IFRS 9 4.1.3 et B4.1.7A rattachent ces flux à un « basic lending arrangement ».

**Implications pratiques**: Si cette condition de modèle économique est remplie, l’actif peut être classé et évalué au coût amorti.

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
 - ifrs9 B4.1.7A

    >Contractual cash flows that are solely payments of principal and interest on the principal amount outstanding are consistent with a basic lending arrangement. In a basic lending arrangement, consideration for the time value of money (see paragraphs B4.1.9A⁠–⁠B4.1.9E) and credit risk are typically the most significant elements of interest. However, in such an arrangement, interest can also include consideration for other basic lending risks (for example, liquidity risk) and costs (for example, administrative costs) associated with holding the financial asset for a particular period of time. In addition, interest can include a profit margin that is consistent with a basic lending arrangement. In extreme economic circumstances, interest can be negative if, for example, the holder of a financial asset either explicitly or implicitly pays for the deposit of its money for a particular period of time (and that fee exceeds the consideration that the holder receives for the time value of money, credit risk and other basic lending risks and costs). However, contractual terms that introduce exposure to risks or volatility in the contractual cash flows that is unrelated to a basic lending arrangement, such as exposure to changes in equity prices or commodity prices, do not give rise to contractual cash flows that are solely payments of principal and interest on the principal amount outstanding. An originated or a purchased financial asset can be a basic lending arrangement irrespective of whether it is a loan in its legal form.

### 2. Juste valeur par autres éléments du résultat global

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est atteint à la fois par la collecte des flux contractuels et par la vente d’actifs financiers.

**Raisonnement**:
Dans cette situation, la présence de flux SPPI rend aussi possible une classification en FVOCI, mais uniquement si le modèle économique combine encaissement des flux et ventes. IFRS 9 4.1.2A l’exige expressément, tandis que IFRS 9 B4.1.7 confirme que le test des flux contractuels sert précisément à cette classification lorsque le modèle économique pertinent existe.

**Implications pratiques**: Si ce modèle économique mixte est démontré, l’actif peut être classé en FVOCI.

**Référence**:
 - ifrs9 4.1.2A

    >A financial asset shall be measured at fair value through other comprehensive income if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 B4.1.7

    >Paragraph 4.1.1(b) requires an entity to classify a financial asset on the basis of its contractual cash flow characteristics if the financial asset is held within a business model whose objective is to hold assets to collect contractual cash flows or within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets, unless paragraph 4.1.5 applies. To do so, the condition in paragraphs 4.1.2(b) and 4.1.2A(b) requires an entity to determine whether the asset’s contractual cash flows are solely payments of principal and interest on the principal amount outstanding.

### 3. Juste valeur par résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique ne remplit pas les critères du coût amorti ou de la FVOCI.
   - Ou l’entité désigne irrévocablement l’actif à la juste valeur par résultat à l’origine pour éliminer ou réduire significativement une incohérence comptable.

**Raisonnement**:
Dans cette situation, la FVTPL n’est pas la conséquence automatique du seul critère SPPI, car IFRS 9 4.1.4 la prévoit comme catégorie résiduelle lorsque l’actif n’est ni au coût amorti ni en FVOCI. Elle peut aussi s’appliquer malgré des flux SPPI si l’entité exerce, à l’origine, la désignation irrévocable pour éliminer ou réduire significativement une incohérence comptable selon IFRS 9 4.1.5.

**Implications pratiques**: À défaut des conditions des catégories SPPI fondées sur le modèle économique, ou en cas de désignation valable, l’actif est évalué en FVTPL.

**Référence**:
 - ifrs9 4.1.4

    >A financial asset shall be measured at fair value through profit or loss unless it is measured at amortised cost in accordance with paragraph 4.1.2 or at fair value through other comprehensive income in accordance with paragraph 4.1.2A. However an entity may make an irrevocable election at initial recognition for particular investments in equity instruments that would otherwise be measured at fair value through profit or loss to present subsequent changes in fair value in other comprehensive income (see paragraphs 5.7.5⁠–⁠5.7.6). E13, E14
 - ifrs9 4.1.5

    >Despite paragraphs 4.1.1⁠–⁠4.1.4, an entity may, at initial recognition, irrevocably designate a financial asset as measured at fair value through profit or loss if doing so eliminates or significantly reduces a measurement or recognition inconsistency (sometimes referred to as an ‘accounting mismatch’) that would otherwise arise from measuring assets or liabilities or recognising the gains and losses on them on different bases (see paragraphs B4.1.29⁠–⁠B4.1.32).