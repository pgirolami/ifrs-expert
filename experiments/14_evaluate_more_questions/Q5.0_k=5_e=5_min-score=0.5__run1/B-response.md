# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I have a technical question on practicalities of applying Cash Flow Hedging under IFRS 9 for grouped items.
>
>Under IFRS 9 cash flow hedge accounting, how should a bank treat subsequent increases in the notional balance of a homogeneous group of floating-rate loans (contractual maturities > 5 years) that has been designated as a group of items sharing the same risk characteristics?
>
>Specifically, assume the bank designates the variable interest cash flows of the loan portfolio as a highly probable forecast transaction and enters into a cash flow hedge in Period 1.
>
>Example:
>Q1: Highly probable forecast balance = 100m Hedge designated in Q1 = 80m
>
>Q2: Forecast balance increases to 150m
>In Q2, should the bank:
>- Treat the hedge designation on a cumulative basis, such that the remaining hedgeable amount becomes 70m (i.e., 150m – 80m), or
>- Treat the incremental 50m increase as a separate forecast transaction / separate hedge layer, requiring separate designation and documentation?

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - L’exposition couverte est la variabilité des flux d’intérêts variables futurs contractuels d’un portefeuille homogène de prêts à taux variable.
   - Le portefeuille est traité comme un groupe d’éléments partageant les mêmes caractéristiques de risque et géré ensemble à des fins de gestion du risque.
   - En P1, la relation de couverture documentée vise un nominal de 80m au sein d’un solde hautement probable de 100m.

## Recommandation

**OUI SOUS CONDITIONS**

Dans votre cas, les 80m désignés en P1 restent la relation couverte. Le passage du solde prévu à 150m en P2 ne transforme pas automatiquement la désignation en un reliquat cumulatif de 70m ; l’augmentation de 50m doit être explicitement désignée et documentée comme tranche additionnelle, sauf rebalancement formel limité au maintien du hedge ratio.

## Points Opérationnels

   - En P2, conserver la documentation de P1 sur les 80m déjà désignés ; ne pas la redéfinir automatiquement par référence au nouveau total de 150m.
   - Si la banque veut couvrir la hausse de 50m, documenter en P2 un nominal additionnel clairement identifié au sein du groupe homogène.
   - N’utiliser un rebalancement que pour maintenir le hedge ratio de la relation existante ; une simple croissance du portefeuille ne suffit pas à étendre automatiquement la désignation initiale.
   - Le suivi opérationnel est plus robuste si les montants désignés sont tracés par tranche de désignation et par date de documentation.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - Le nominal additionnel de 50m n’entre dans la couverture qu’avec une désignation et une documentation explicites en P2.<br>- Si la banque modifie la relation existante, cette modification doit constituer un rebalancement visant à maintenir un hedge ratio conforme au même objectif de gestion du risque. |

### 1. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le nominal additionnel de 50m n’entre dans la couverture qu’avec une désignation et une documentation explicites en P2.
   - Si la banque modifie la relation existante, cette modification doit constituer un rebalancement visant à maintenir un hedge ratio conforme au même objectif de gestion du risque.

**Raisonnment**:
Dans cette situation, IFRS 9 permet de couvrir un groupe d’éléments, mais la relation désignée porte sur des quantités désignées et identifiées. Le fait que le solde prévu passe de 100m à 150m en P2 n’élargit pas automatiquement la relation de P1 : les 80m désignés restent couverts, et l’augmentation de 50m doit faire l’objet d’une désignation/documentation explicite si la banque veut la couvrir. Un rebalancement n’est pertinent que s’il sert à maintenir le hedge ratio de la relation existante.

**Implications pratiques**: En pratique, ne traitez pas automatiquement le solde non couvert comme 70m dans la relation existante ; suivez les 80m de P1 séparément et documentez toute tranche additionnelle en P2.

**Référence**:
 - 6.6.1
    >managed together on a group basis for risk management purposes
 - B6.5.7
    >adjustments made to the designated quantities
 - B6.6.11
    >requires the specific identification of the nominal amount
