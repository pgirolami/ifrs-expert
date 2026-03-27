# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I have a technical question on practicalities of applying Cash Flow Hedging under IFRS 9 for grouped items.

Under IFRS 9 cash flow hedge accounting, how should a bank treat subsequent increases in the notional balance of a homogeneous group of floating-rate loans (contractual maturities > 5 years) that has been designated as a group of items sharing the same risk characteristics?

Specifically, assume the bank designates the variable interest cash flows of the loan portfolio as a highly probable forecast transaction and enters into a cash flow hedge in Period 1.

Example:
Q1: Highly probable forecast balance = 100m
Hedge designated in Q1 = 80m

Q2: Forecast balance increases to 150m
In Q2, should the bank:
- Treat the hedge designation on a cumulative basis, such that the remaining hedgeable amount becomes 70m (i.e., 150m – 80m), or
- Treat the incremental 50m increase as a separate forecast transaction / separate hedge layer, requiring separate designation and documentation?

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La documentation de couverture en Q1 a désigné 80m de flux d’intérêts variables hautement probables du portefeuille, et non un portefeuille dynamique ouvert couvrant automatiquement toute hausse future.
   - Le portefeuille de prêts est homogène et géré ensemble, de sorte qu’il peut être traité comme un groupe d’éléments partageant les mêmes caractéristiques de risque.
   - L’augmentation à 150m en Q2 reflète des flux prévisionnels additionnels devenus hautement probables après la désignation initiale.

## Recommandation

**OUI**

Dans ces faits, la relation désignée en Q1 reste 80m. Le « 70m restant » n’est qu’un solde économique non couvert; les 50m additionnels de Q2 ne s’intègrent pas automatiquement à la désignation initiale et doivent être formellement désignés/documentés s’ils sont ajoutés à la couverture.

## Points Opérationnels

   - La relation ouverte en Q1 continue d’être suivie et mesurée sur la base de 80m à partir de son inception.
   - Si la banque veut couvrir une partie du supplément de 50m en Q2, elle doit le désigner prospectivement avec une documentation explicite de la quantité nominale couverte.
   - Le montant de 70m représente l’exposition économiquement non couverte après Q2; ce n’est pas une désignation comptable automatique au titre de la relation de Q1.
   - Un ajustement des quantités ne peut être présenté comme rééquilibrage que s’il vise à maintenir le hedge ratio de la relation existante et qu’il est dûment documenté.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre cas, IFRS 9 s’applique à la relation effectivement désignée: 80m de flux variables hautement probables en Q1. Le passage du forecast de 100m à 150m en Q2 n’élargit pas automatiquement cette quantité désignée; au sein d’un groupe, la quantité nominale couverte doit être spécifiquement identifiée et documentée. En pratique, le supplément de 50m constitue une exposition additionnelle à désigner prospectivement, tandis que 70m n’est qu’un reliquat économique non couvert.

**Implications pratiques**: En Q2, maintenir la relation existante sur 80m et documenter séparément toute couverture nouvelle portant sur les flux additionnels.

**Référence**:
 - 6.5.11
    >the cumulative gain or loss on the hedging instrument from inception of the hedge
 - B6.5.7
    >Rebalancing refers to the adjustments made to the designated quantities
 - B6.4.19
    >The documentation of the hedging relationship shall be updated
 - B6.6.11
    >requires the specific identification of the nominal amount
