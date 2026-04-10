# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ias21`
   - `ifrs9`
   - `ias32`
   - `ifric17`
   - `ifrs19`
   - `ifrs7`
   - `ifrs12`
   - `ifric2`
   - `ifric16`
   - `ias7`
   - `sic25`
   - `ps1`
   - `ifric14`

## Hypothèses
   - La créance de dividende intragroupe est une créance monétaire libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités du groupe.
   - La question vise les comptes consolidés, puisque la créance est indiquée comme reconnue dans ces comptes.
   - Le risque couvert est le seul risque de change attaché à cette créance de dividende déjà comptabilisée, et non un dividende futur simplement envisagé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en pratique seulement via une couverture de juste valeur du risque de change de la créance intragroupe, si cette créance monétaire génère un écart de change non totalement éliminé en consolidation. La couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas à cette situation telle que décrite.

## Points Opérationnels

   - Le point clé de recevabilité IFRS est le niveau de reporting : l’analyse doit être faite en comptes consolidés, pas dans les comptes individuels.
   - La documentation doit intervenir sur la créance monétaire existante et identifier le risque de change qui subsiste après les éliminations de consolidation.
   - Si les entités concernées n’ont pas des monnaies fonctionnelles différentes, ou si l’effet de change est totalement éliminé en consolidation, la désignation n’est pas recevable.
   - Il faut éviter de documenter cette situation comme une transaction future intragroupe ou comme une couverture d’investissement net, car cela ne correspond pas aux faits décrits.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance est un élément monétaire intragroupe<br>- elle est exposée à un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes<br>- les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation selon IAS 21 |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance est un élément monétaire intragroupe
   - elle est exposée à un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes
   - les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation selon IAS 21

**Raisonnment**:
Ici, le dividende intragroupe a déjà donné lieu à une créance reconnue en consolidation : il s’agit donc d’un élément monétaire existant, non d’un flux futur. IAS 21 précise qu’un actif monétaire intragroupe ne peut pas être éliminé sans faire apparaître l’effet de change en consolidé. IFRS 9 admet précisément, par exception, qu’un élément monétaire intragroupe puisse être désigné comme élément couvert en consolidé pour son risque de change lorsque cet effet n’est pas totalement éliminé.

**Implications pratiques**: La documentation de couverture peut viser la créance intragroupe reconnue, mais seulement pour le risque de change qui subsiste dans les comptes consolidés.

**Référence**:
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite ne porte pas sur une transaction future hautement probable mais sur une créance déjà née et reconnue en consolidation. IFRS 9 réserve la logique de flux de trésorerie aux transactions prévues, et pour l’intragroupe en consolidé à des transactions futures dont le risque de change affectera le résultat consolidé. Ce n’est pas le cas d’une créance de dividende déjà comptabilisée.

**Implications pratiques**: Cette voie ne convient pas pour documenter la couverture d’une créance de dividende intragroupe déjà reconnue.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une couverture d’investissement net vise le risque de change attaché aux actifs nets d’une activité étrangère, pas une créance de dividende intragroupe isolée. Le fait générateur ici est un dividende ayant créé une créance monétaire spécifique en consolidation. Cette exposition est distincte du risque de conversion de l’investissement net dans l’activité étrangère.

**Implications pratiques**: La documentation ne doit pas qualifier cette créance de dividende comme un hedge de net investment.

**Référence**:
 - 2
    >The item being hedged ... may be an amount of net assets
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency