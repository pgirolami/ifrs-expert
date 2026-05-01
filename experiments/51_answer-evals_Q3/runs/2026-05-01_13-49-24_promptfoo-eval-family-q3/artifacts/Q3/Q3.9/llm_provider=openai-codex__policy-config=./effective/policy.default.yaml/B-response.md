# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>Un actif financier peut être caractérisé par des flux de trésorerie limités au principal et aux intérêts.
Comment définit-on précisément ce type d’actif dont les termes contractuels ne prévoient que ces paiements ?

**Reformulation**:
>Détermination du critère SPPI (« solely payments of principal and interest ») dans la classification IFRS 9 des actifs financiers et des modèles de mesure qui en découlent

## Documentation
**Consultée**
   - IAS-S (standard) (`ias7`, `ias36`)
   - IFRS-S (standard) (`ifrs9`, `ifrs19`)

**Retenue pour l'analyse**
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La question est interprétée comme portant sur la définition IFRS 9 du critère SPPI (« solely payments of principal and interest »), sans autre fait spécifique sur le modèle économique de détention.
   - On suppose que l’actif examiné est un actif financier relevant du champ de classement d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

IFRS 9 définit précisément un actif à flux contractuels limités au principal et aux intérêts : les termes doivent générer, à des dates spécifiées, uniquement des paiements de principal et d’intérêts au sens d’IFRS 9. La catégorie de mesure en résultant dépend ensuite du modèle économique de gestion de l’actif.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique dont l’objectif est de détenir les actifs pour en percevoir les flux contractuels.<br>- Les termes contractuels génèrent, à des dates spécifiées, uniquement des paiements de principal et d’intérêts au sens d’IFRS 9. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - L’actif est détenu dans un modèle économique combinant encaissement des flux contractuels et vente.<br>- Les termes contractuels génèrent, à des dates spécifiées, uniquement des paiements de principal et d’intérêts au sens d’IFRS 9. |
| 3. Juste valeur par résultat | OUI SOUS CONDITIONS | - Le modèle économique n’est ni « détenir pour encaisser » ni « détenir pour encaisser et vendre ».<br>- Ou bien les termes contractuels ne satisfont pas au critère SPPI. |

### 1. Coût amorti

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’actif est détenu dans un modèle économique dont l’objectif est de détenir les actifs pour en percevoir les flux contractuels.
   - Les termes contractuels génèrent, à des dates spécifiées, uniquement des paiements de principal et d’intérêts au sens d’IFRS 9.

**Raisonnement**:
Dans cette situation, le coût amorti n’est possible que si l’actif répond à la définition SPPI et s’il est détenu dans un modèle économique visant à encaisser les flux contractuels (IFRS 9 4.1.2). La définition précise du SPPI repose sur des flux, à des dates spécifiées, constitués uniquement de principal et d’intérêts; le principal est la juste valeur initiale et l’intérêt rémunère le temps, le risque de crédit et d’autres risques/coûts de prêt de base (IFRS 9 4.1.3, B4.1.7A).

**Implications pratiques**: Si ces deux conditions sont réunies, l’actif peut être classé au coût amorti.

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
   - L’actif est détenu dans un modèle économique combinant encaissement des flux contractuels et vente.
   - Les termes contractuels génèrent, à des dates spécifiées, uniquement des paiements de principal et d’intérêts au sens d’IFRS 9.

**Raisonnement**:
Dans cette situation, la JV par OCI s’applique seulement si l’actif satisfait d’abord la définition SPPI, puis s’il est détenu dans un modèle dont l’objectif est à la fois de collecter les flux contractuels et de vendre les actifs (IFRS 9 4.1.2A). La définition SPPI reste identique : principal = juste valeur initiale; intérêts = rémunération d’un prêt de base, sans exposition à des risques non basiques (IFRS 9 4.1.3, B4.1.7).

**Implications pratiques**: Si ces conditions sont remplies, l’actif peut être classé à la juste valeur par OCI.

**Référence**:
 - ifrs9 4.1.2A

    >A financial asset shall be measured at fair value through other comprehensive income if both of the following conditions are met:
(a)the financial asset is held within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets and
(b)the contractual terms of the financial asset give rise on specified dates to cash flows that are solely payments of principal and interest on the principal amount outstanding.
Paragraphs B4.1.1⁠–⁠B4.1.26 provide guidance on how to apply these conditions.
 - ifrs9 4.1.3

    >For the purpose of applying paragraphs 4.1.2(b) and 4.1.2A(b) :
(a)principal is the fair value of the financial asset at initial recognition. Paragraph B4.1.7B provides additional guidance on the meaning of principal.
(b)interest consists of consideration for the time value of money, for the credit risk associated with the principal amount outstanding during a particular period of time and for other basic lending risks and costs, as well as a profit margin. Paragraphs B4.1.7A and B4.1.9A⁠–⁠B4.1.9E provide additional guidance on the meaning of interest, including the meaning of the time value of money.
 - ifrs9 B4.1.7

    >Paragraph 4.1.1(b) requires an entity to classify a financial asset on the basis of its contractual cash flow characteristics if the financial asset is held within a business model whose objective is to hold assets to collect contractual cash flows or within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets, unless paragraph 4.1.5 applies. To do so, the condition in paragraphs 4.1.2(b) and 4.1.2A(b) requires an entity to determine whether the asset’s contractual cash flows are solely payments of principal and interest on the principal amount outstanding.

### 3. Juste valeur par résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique n’est ni « détenir pour encaisser » ni « détenir pour encaisser et vendre ».
   - Ou bien les termes contractuels ne satisfont pas au critère SPPI.

**Raisonnement**:
Dans cette situation, la JV par résultat devient la catégorie résiduelle lorsque l’actif n’entre pas dans un modèle « encaisser » ni « encaisser et vendre », ou lorsqu’il ne satisfait pas au test SPPI (IFRS 9 4.1.1, B4.1.5). Ainsi, même un actif dont les flux sont limités au principal et aux intérêts peut être en JV par résultat si le modèle économique est fondé sur la juste valeur ou la vente active (IFRS 9 B4.1.6).

**Implications pratiques**: À défaut de satisfaire la combinaison modèle économique + SPPI requise pour les autres catégories, l’actif est classé en juste valeur par résultat.

**Référence**:
 - ifrs9 4.1.1

    >Unless paragraph 4.1.5 applies, an entity shall classify financial assets as subsequently measured at amortised cost, fair value through other comprehensive income or fair value through profit or loss on the basis of both:
(a)the entity’s business model for managing the financial assets and
(b)the contractual cash flow characteristics of the financial asset.
 - ifrs9 B4.1.5

    >Financial assets are measured at fair value through profit or loss if they are not held within a business model whose objective is to hold assets to collect contractual cash flows or within a business model whose objective is achieved by both collecting contractual cash flows and selling financial assets (but see also paragraph 5.7.5). One business model that results in measurement at fair value through profit or loss is one in which an entity manages the financial assets with the objective of realising cash flows through the sale of the assets. The entity makes decisions based on the assets’ fair values and manages the assets to realise those fair values. In this case, the entity’s objective will typically result in active buying and selling. Even though the entity will collect contractual cash flows while it holds the financial assets, the objective of such a business model is not achieved by both collecting contractual cash flows and selling financial assets. This is because the collection of contractual cash flows is not integral to achieving the business model’s objective; instead, it is incidental to it.
 - ifrs9 B4.1.6

    >A portfolio of financial assets that is managed and whose performance is evaluated on a fair value basis (as described in paragraph 4.2.2(b)) is neither held to collect contractual cash flows nor held both to collect contractual cash flows and to sell financial assets. The entity is primarily focused on fair value information and uses that information to assess the assets’ performance and to make decisions. In addition, a portfolio of financial assets that meets the definition of held for trading is not held to collect contractual cash flows or held both to collect contractual cash flows and to sell financial assets. For such portfolios, the collection of contractual cash flows is only incidental to achieving the business model’s objective. Consequently, such portfolios of financial assets must be measured at fair value through profit or loss.