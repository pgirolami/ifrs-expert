# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs19`
   - `ifrs7`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric17`
   - `ifric2`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic7`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une monnaie étrangère pour au moins une entité du groupe.
   - La question est analysée au niveau des états financiers consolidés IFRS.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d’une créance intragroupe peut être désigné en couverture si cette créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point déterminant est le niveau de reporting : l’analyse se fait en consolidation, pas dans les comptes individuels isolés.
   - Il faut vérifier dès l’origine que la créance de dividende est bien un poste monétaire libellé en devise et que les deux entités ont des monnaies fonctionnelles différentes.
   - La désignation doit être faite formellement au titre du risque de change de la créance intragroupe ; une simple intention de gestion du risque ne suffit pas.
   - Si le dividende n’était pas encore comptabilisé mais seulement envisagé, la logique à examiner serait différente ; ici, le fait générateur est la créance déjà reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé à un risque de change.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes de sorte que l’écart de change ne soit pas totalement éliminé en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée conformément à IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé à un risque de change.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes de sorte que l’écart de change ne soit pas totalement éliminé en consolidation.
   - La relation de couverture doit être formellement désignée et documentée conformément à IFRS 9.

**Raisonnment**:
Ici, la créance de dividende est déjà comptabilisée et constitue un poste reconnu. En consolidation, IFRS 9 autorise exceptionnellement qu’un élément monétaire intragroupe exposé au risque de change soit un élément couvert si les gains/pertes de change ne sont pas totalement éliminés. IAS 21 confirme précisément que de tels écarts subsistent en résultat consolidé lorsque les entités ont des monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation de couverture doit viser le risque de change de la créance intragroupe au niveau consolidé, et non le flux intragroupe en tant que tel.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >cannot be eliminated against the corresponding intragroup liability ... without showing the results of currency fluctuations
 - 6.3.1
    >A hedged item can be a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, le dividende intragroupe est déjà comptabilisé en créance à recevoir ; il ne s’agit donc plus d’une transaction future hautement probable. Le modèle de cash flow hedge vise les transactions futures ou engagements de flux, y compris certains intragroupes, mais pas une créance déjà reconnue.

**Implications pratiques**: Cette voie n’est pas adaptée une fois que le dividende a été reconnu en créance dans les comptes.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé par la question porte sur une créance de dividende intragroupe comptabilisée, non sur le risque de change attaché à un investissement net dans une activité à l’étranger. IFRIC 16 réserve cette mécanique au risque de change sur les actifs nets d’une opération étrangère inclus dans les comptes consolidés.

**Implications pratiques**: Il ne faut pas documenter cette relation comme une couverture d’investissement net, car l’objet couvert n’est pas l’investissement net lui-même.

**Référence**:
 - 7
    >applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 11
    >the hedged item can be an amount of net assets
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency