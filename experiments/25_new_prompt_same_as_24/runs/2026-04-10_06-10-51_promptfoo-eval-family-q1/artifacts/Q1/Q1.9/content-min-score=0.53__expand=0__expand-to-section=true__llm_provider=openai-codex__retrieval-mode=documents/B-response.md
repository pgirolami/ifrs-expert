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
   - La question vise des comptes consolidés et une créance de dividende intragroupe déjà comptabilisée, libellée en devise étrangère.
   - La créance de dividende constitue un élément monétaire intragroupe entre des entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, la composante de risque de change d’une créance de dividende intragroupe peut être désignée comme élément couvert si elle correspond à un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. En pratique, cela pointe vers l’exception d’IFRS 9 pour le risque de change sur éléments monétaires intragroupe.

## Points Opérationnels

   - Le point clé en consolidation est l’exception IFRS 9 relative aux éléments monétaires intragroupe, et non la règle générale réservant les éléments couverts aux positions avec des tiers.
   - Il faut vérifier dès la mise en place de la relation de couverture que les entités concernées ont des monnaies fonctionnelles différentes.
   - La désignation doit être faite au niveau des comptes consolidés, car c’est à ce niveau qu’il faut apprécier la non-élimination complète des écarts de change.
   - Une créance de dividende déjà reconnue s’analyse différemment d’une transaction intragroupe future hautement probable : ici, le sujet est le poste monétaire reconnu.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La désignation porte sur le risque de change de la créance intragroupe reconnue.<br>- La créance est un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.<br>- Le risque de change affecte un montant non totalement éliminé en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
La créance de dividende est, dans les faits supposés, un actif reconnu. IFRS 9 permet qu’un actif reconnu soit un élément couvert, et prévoit une exception en consolidation pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans cette situation, la désignation est donc possible sous cette exception.

**Implications pratiques**: La documentation de couverture doit viser spécifiquement le risque de change de la créance intragroupe dans les comptes consolidés.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La désignation porte sur le risque de change de la créance intragroupe reconnue.
   - La créance est un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.
   - Le risque de change affecte un montant non totalement éliminé en consolidation.

**Raisonnment**:
IFRS 9 traite la couverture de flux de trésorerie comme un modèle distinct et un élément couvert peut être un actif ou passif reconnu. Pour cette créance intragroupe, la recevabilité en consolidation dépend toutefois de la même exception spécifique sur le risque de change des éléments monétaires intragroupe. L’applicabilité n’existe donc que si cette exception est satisfaite.

**Implications pratiques**: Il faut démontrer que le modèle de couverture retenu reflète bien l’exposition de change portée en résultat consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe reconnue n’est pas un montant de net assets d’une activité étrangère ; c’est un poste monétaire distinct. Les textes sur la couverture d’investissement net visent le risque de change lié à l’investissement net dans une activité étrangère, non un dividende intragroupe à recevoir. Cette voie ne correspond donc pas à la situation décrite.

**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme un hedge de net investment.

**Référence**:
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment