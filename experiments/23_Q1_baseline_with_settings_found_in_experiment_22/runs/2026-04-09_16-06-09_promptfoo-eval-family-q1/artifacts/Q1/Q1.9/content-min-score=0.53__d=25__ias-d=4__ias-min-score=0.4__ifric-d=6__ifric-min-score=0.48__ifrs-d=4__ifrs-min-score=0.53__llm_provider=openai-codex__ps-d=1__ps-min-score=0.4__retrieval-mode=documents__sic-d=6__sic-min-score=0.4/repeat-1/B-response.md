# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ifrs19`
   - `ifric2`
   - `ifric16`
   - `ias32`
   - `ifric17`
   - `sic7`
   - `ias37`

## Hypothèses
   - La question porte sur la comptabilité de couverture selon IFRS 9 dans des comptes consolidés.
   - Le dividende intragroupe a été comptabilisé en créance, créant un élément monétaire reconnu exposé au risque de change.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, un élément intragroupe n’est en principe pas éligible, sauf exception pour le risque de change d’un élément monétaire intragroupe. Donc une créance de dividende intragroupe peut être désignée comme élément couvert seulement si elle génère des écarts de change non entièrement éliminés en consolidation.

## Points Opérationnels

   - Vérifier au moment de la désignation que la créance de dividende est bien un élément monétaire intragroupe.
   - Documenter que les entités liées ont des monnaies fonctionnelles différentes et que les écarts de change ne sont pas entièrement éliminés en consolidation.
   - Ne pas utiliser le modèle de couverture d’investissement net, qui vise les actifs nets d’une activité étrangère et non une créance de dividende.
   - La relation de couverture doit aussi satisfaire aux critères généraux d’IFRS 9, notamment la documentation formelle et l’existence d’une relation économique.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe est un élément monétaire.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance de dividende intragroupe est un élément monétaire reconnu.<br>- Le risque couvert est uniquement le risque de change.<br>- Ce risque affecte le résultat consolidé via des écarts de change non entièrement éliminés. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe est un élément monétaire.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation.

**Raisonnment**:
La créance de dividende reconnue est un actif comptabilisé, donc peut relever d’une couverture de juste valeur d’un risque particulier. Toutefois, en consolidation, un élément intragroupe n’est éligible que par l’exception visant le risque de change d’un élément monétaire intragroupe qui n’est pas entièrement éliminé. Si cette exception est remplie, la composante de change peut être désignée.

**Implications pratiques**: Possible en consolidation uniquement sur la composante de change répondant à l’exception IFRS 9 relative aux éléments monétaires intragroupe.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe est un élément monétaire reconnu.
   - Le risque couvert est uniquement le risque de change.
   - Ce risque affecte le résultat consolidé via des écarts de change non entièrement éliminés.

**Raisonnment**:
IFRS 9 permet la couverture de la variabilité des flux de trésorerie d’un actif reconnu attribuable à un risque particulier. Mais ici, la contrainte décisive reste celle des comptes consolidés: l’élément intragroupe n’est admissible que si la créance de dividende constitue un élément monétaire intragroupe dont le risque de change crée des écarts non totalement éliminés. Sans cela, la désignation n’est pas permise.

**Implications pratiques**: La désignation en couverture de flux de trésorerie n’est envisageable qu’à la condition que le risque de change survive à l’élimination intragroupe en consolidation.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite concerne une créance de dividende intragroupe reconnue, et non un investissement net dans une activité étrangère. IFRS 9 et IFRIC 16 réservent ce modèle à l’exposition de change sur les actifs nets d’une activité étrangère. La créance de dividende ne correspond donc pas à l’élément couvert de ce modèle.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour une créance de dividende intragroupe reconnue.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 7
    >applies only to hedges of net investments in foreign operations
 - 8
    >it should not be applied by analogy to other types of hedge accounting