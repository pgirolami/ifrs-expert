# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - La question porte sur la comptabilité de couverture dans les états financiers consolidés selon IFRS 9.
   - Le dividende intragroupe a été comptabilisé en créance intercompagnie, donc comme un élément monétaire libellé en monnaie étrangère.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via la logique applicable aux éléments monétaires intragroupe en risque de change dans les comptes consolidés. Cela suppose que la créance de dividende crée des écarts de change qui ne sont pas intégralement éliminés en consolidation, typiquement entre entités de groupe ayant des monnaies fonctionnelles différentes.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que les écarts de change sur la créance de dividende intragroupe ne sont pas totalement éliminés.
   - L’exception IFRS 9 vise le risque de change d’un élément monétaire intragroupe ; il faut donc confirmer la nature monétaire de la créance de dividende.
   - La couverture doit être documentée dans les comptes consolidés, et non seulement dans les comptes individuels des entités du groupe.
   - Si l’exposition provient de monnaies fonctionnelles identiques ou d’écarts entièrement éliminés, la désignation comme élément couvert en consolidation ne fonctionne pas.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change génère des gains ou pertes de change non entièrement éliminés en consolidation.<br>- Les entités concernées ont des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change génère des gains ou pertes de change non entièrement éliminés en consolidation.
   - Les entités concernées ont des monnaies fonctionnelles différentes.

**Raisonnment**:
Dans cette situation, la créance de dividende déjà comptabilisée est un actif reconnu, donc elle peut en principe être un élément couvert. En comptes consolidés, IFRS 9 interdit en général les éléments intragroupe, mais prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il génère des écarts de change non totalement éliminés à la consolidation.

**Implications pratiques**: La désignation peut être envisagée en couverture du risque de change de la créance reconnue dans les comptes consolidés, sous réserve de documenter la relation de couverture.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les couvertures de flux de trésorerie visent notamment des transactions prévues hautement probables. Ici, l’hypothèse donnée est qu’un dividende intragroupe est déjà reconnu sous forme de créance ; il ne s’agit donc plus d’une transaction future hautement probable mais d’un actif monétaire existant.

**Implications pratiques**: Ce modèle ne correspond pas aux faits décrits, car l’exposition visée provient d’une créance déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise le risque de change sur une créance de dividende intragroupe reconnue, non le risque de change sur un investissement net dans une activité à l’étranger. Le modèle de couverture d’investissement net concerne les net assets d’une opération étrangère, pas une créance intercompagnie de dividende isolée.

**Implications pratiques**: Cette voie n’est pas adaptée aux faits, car l’élément visé n’est pas un investissement net dans une activité étrangère.

**Référence**:
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation