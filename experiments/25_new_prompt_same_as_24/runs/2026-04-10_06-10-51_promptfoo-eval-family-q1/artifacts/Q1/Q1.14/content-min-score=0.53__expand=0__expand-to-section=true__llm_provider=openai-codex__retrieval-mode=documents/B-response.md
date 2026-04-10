# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a donné lieu à la comptabilisation d’un montant à recevoir au sein du périmètre consolidé. Peut-on, dans ces circonstances, documenter une couverture portant sur le risque de change afférent à cette exposition ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifric17`
   - `ias7`
   - `ifric16`
   - `ias24`
   - `sic25`

## Hypothèses
   - La question est analysée au niveau des états financiers consolidés.
   - Le dividende intragroupe a été comptabilisé en créance intra-groupe libellée dans une devise créant un risque de change au sein du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais uniquement si la créance de dividende intragroupe est un élément monétaire exposé à un risque de change qui n’est pas entièrement éliminé en consolidation, typiquement entre entités de devises fonctionnelles différentes. Dans ce cas, la voie pertinente est la couverture de juste valeur, et non la couverture de flux futurs ni, en principe, la couverture d’investissement net.

## Points Opérationnels

   - Vérifier d’abord si la créance de dividende est bien un poste monétaire entre entités ayant des devises fonctionnelles différentes.
   - Confirmer que les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation.
   - Si ces conditions sont remplies, la modélisation pertinente est une couverture de juste valeur du risque de change de la créance reconnue.
   - Ne pas documenter la relation comme couverture de flux de trésorerie si le dividende a déjà été déclaré et comptabilisé en créance.
   - La charge de documentation est concentrée sur la démonstration du caractère intragroupe monétaire et de l’impact résiduel en résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change affecte le résultat consolidé car les écarts de change ne sont pas entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change affecte le résultat consolidé car les écarts de change ne sont pas entièrement éliminés en consolidation.

**Raisonnment**:
Ici, l’exposition porte sur une créance déjà comptabilisée. En consolidation, un élément couvert doit en principe être avec une partie externe, mais l’exception vise le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. C’est le cas si les entités concernées ont des devises fonctionnelles différentes.

**Implications pratiques**: La documentation de couverture peut être envisagée sur la créance de dividende, sous réserve que l’exposition de change subsiste au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les extraits fournis sur les opérations intragroupe en couverture de flux visent les transactions intragroupe hautement probables. Or, dans la situation décrite, le dividende a déjà donné lieu à une créance comptabilisée ; l’exposition n’est donc plus celle d’un flux futur hautement probable mais d’un poste monétaire existant.

**Implications pratiques**: Cette voie ne correspond pas au fait générateur décrit, qui est une créance déjà reconnue.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise le risque de change sur un investissement net dans une activité à l’étranger. Une créance de dividende intragroupe comptabilisée correspond ici à un montant à recevoir déterminé, non à un montant de net assets d’une activité étrangère. Les faits fournis ne permettent donc pas de la traiter comme une couverture d’investissement net.

**Implications pratiques**: La documentation ne devrait pas être bâtie comme une couverture d’investissement net sur la seule base d’une créance de dividende intragroupe.

**Référence**:
 - 2
    >the item being hedged ... may be an amount of net assets
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation