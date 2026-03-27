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
   - L’élément couvert désigné est un groupe de flux d’intérêts variables futurs sur des prêts homogènes à taux variable, gérés ensemble et présentés comme hautement probables.
   - En T1, la relation de couverture documentée porte sur un nominal désigné de 80 m au sein d’un encours prévisionnel de 100 m.
   - La question porte sur le traitement comptable de l’augmentation du volume désigné en T2, et non sur la comptabilisation séparée des prêts sous-jacents.

## Recommandation

**OUI SOUS CONDITIONS**

La couverture désignée en T1 reste limitée à 80 m tant qu’elle n’est pas modifiée formellement. En pratique, l’augmentation de 50 m doit être désignée séparément comme nouvelle couche de flux, sauf si la banque rééquilibre valablement la relation existante et met à jour sa documentation en T2.

## Points Opérationnels

   - Le nominal couvert reste celui documenté en T1 tant qu’aucune modification formelle n’est effectuée.
   - Le calcul économique d’un 'reste hedgeable' de 70 m n’est pas, à lui seul, une nouvelle quantité désignée au sens d’IFRS 9.
   - Si la banque veut couvrir le supplément de 50 m, la voie la plus robuste est une désignation séparée de cette couche additionnelle avec sa propre documentation.
   - Si la banque préfère modifier la relation existante, elle doit traiter cela comme un rééquilibrage documenté en T2, et non comme un élargissement automatique de la désignation initiale.
   - La discontinuation n’est pertinente que si la relation ne satisfait plus aux critères après prise en compte d’un éventuel rééquilibrage.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | OUI | - (non spécifiées) |
| 2. Rééquilibrage de la couverture | OUI SOUS CONDITIONS | - La banque modifie les quantités désignées de la relation existante pour maintenir un hedge ratio conforme.<br>- La documentation de couverture est mise à jour en T2 pour refléter cette modification. |
| 3. Arrêt de la comptabilité de couverture | NON | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation relève directement d’une couverture de flux de trésorerie d’un groupe d’éléments gérés ensemble.
En T1, la relation désignée couvre 80 m de flux variables; le passage du forecast total à 150 m en T2 n’élargit pas automatiquement cette désignation.
Le supplément de 50 m doit donc être identifié comme quantité nouvellement désignée s’il doit être couvert.

**Implications pratiques**: En T2, le supplément de 50 m n’entre pas dans la relation T1 tant qu’il n’est pas explicitement désigné.

**Référence**:
 - 6.6.1
    >the items in the group are managed together on a group basis
 - B6.6.11
    >requires the specific identification of the nominal amount

### 2. Rééquilibrage de la couverture
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La banque modifie les quantités désignées de la relation existante pour maintenir un hedge ratio conforme.
   - La documentation de couverture est mise à jour en T2 pour refléter cette modification.

**Raisonnment**:
Le rééquilibrage n’est pertinent ici que si la banque ajuste les quantités désignées de la relation existante pour maintenir un hedge ratio conforme après le changement de circonstances en T2.
En revanche, utiliser ce mécanisme uniquement pour 'absorber' automatiquement le supplément de 50 m comme nouveau volume couvert ne ressort pas de la définition fournie.
Donc il peut être utilisé, mais seulement comme modification formelle de la relation existante.

**Implications pratiques**: Si la banque ajuste la relation existante, elle doit redocumenter en T2 les quantités désignées et l’évaluation de l’efficacité.

**Référence**:
 - B6.5.7
    >adjustments made to the designated quantities
 - B6.4.19
    >documentation of the hedging relationship shall be updated

### 3. Arrêt de la comptabilité de couverture
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le seul fait que l’encours prévu passe de 100 m à 150 m ne montre pas, dans ce cas, que la relation existante cesse de satisfaire aux critères.
L’arrêt prospectif n’intervient que si les critères ne sont plus remplis après prise en compte d’un éventuel rééquilibrage, ou si les flux couverts ne sont plus attendus.
Ces faits ne sont pas décrits dans l’exemple.

**Implications pratiques**: Aucun arrêt prospectif n’est requis du seul fait de l’augmentation du forecast en T2.

**Référence**:
 - 6.5.6
    >discontinue hedge accounting prospectively only when
 - 6.5.12
    >if the hedged future cash flows are still expected to occur
