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
   - Le dividende intragroupe a été comptabilisé en créance avant son règlement.
   - La question vise les états financiers consolidés établis selon les IFRS.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, le risque de change d’une créance intragroupe peut être désigné comme élément couvert uniquement via l’exception visant un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, le modèle pertinent est la couverture de juste valeur ; les modèles de cash flow hedge et de net investment hedge ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point clé est le timing : une fois le dividende comptabilisé en créance, l’analyse pertinente n’est plus celle d’une transaction future hautement probable.
   - Au niveau consolidé, il faut démontrer que l’exposition de change sur la créance/dette intragroupe n’est pas entièrement éliminée lors de la consolidation.
   - La documentation de couverture doit être portée au niveau des états financiers consolidés, avec identification précise du poste monétaire intragroupe et du risque de change couvert.
   - Si la créance ne génère pas d’écarts de change résiduels dans le résultat consolidé, la désignation comme élément couvert n’est pas justifiée dans cette situation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance et la dette de dividende constituent un poste monétaire intragroupe<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- les écarts de change correspondants ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance et la dette de dividende constituent un poste monétaire intragroupe
   - les entités concernées ont des monnaies fonctionnelles différentes
   - les écarts de change correspondants ne sont pas totalement éliminés en consolidation

**Raisonnment**:
La créance de dividende déjà comptabilisée est un actif reconnu, donc un type d’élément pouvant être couvert. En consolidation, les éléments intragroupe sont en principe exclus, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés. Une créance/dette intragroupe entre entités de monnaies fonctionnelles différentes entre dans ce cas si elle génère encore une exposition de change au niveau du groupe.

**Implications pratiques**: Une relation de couverture formellement documentée au niveau consolidé est possible si l’exposition de change subsiste dans le résultat consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, le dividende a déjà été comptabilisé en créance à recevoir : il ne s’agit donc plus d’une transaction future hautement probable mais d’un poste reconnu. L’exception IFRS 9 en consolidation pour les transactions intragroupe hautement probables vise les opérations futures, pas une créance de dividende déjà constatée.

**Implications pratiques**: Ce modèle ne convient pas à une créance de dividende déjà enregistrée dans les comptes.

**Référence**:
 - 6.3.3
    >if a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur le risque de change d’un dividende intragroupe comptabilisé en créance, non sur le risque de change attaché à un investissement net dans une activité à l’étranger. Le cadre IFRIC 16 vise les écarts entre la monnaie fonctionnelle de l’opération étrangère et celle du parent sur les actifs nets de l’opération étrangère ; une créance de dividende reconnue ne correspond pas à cet objet couvert.

**Implications pratiques**: La documentation de couverture ne doit pas être structurée comme une couverture d’investissement net pour cette créance de dividende.

**Référence**:
 - 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity