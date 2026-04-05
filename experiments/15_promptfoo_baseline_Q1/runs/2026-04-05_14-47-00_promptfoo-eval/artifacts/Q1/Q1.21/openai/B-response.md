# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Le groupe a comptabilisé un receivable au titre de dividendes intragroupe, créant ainsi une exposition au risque de change dans les comptes consolidés. Cette exposition peut-elle être désignée comme élément couvert au sens des IFRS ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les comptes consolidés du groupe au sens d’IFRS 9.
   - Le receivable de dividende intragroupe est un poste monétaire entre entités du groupe.
   - L’exposition de change naît parce que les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le receivable de dividende intragroupe entre dans l’exception IFRS 9 applicable aux postes monétaires intragroupe en consolidation. Dans ce cas, la désignation est défendable surtout comme élément couvert d’un fair value hedge du risque de change.

## Points Opérationnels

   - Le point clé est de vérifier si les écarts de change sur le dividende intragroupe ne sont pas entièrement éliminés en consolidation.
   - Si cette condition n’est pas remplie, la réponse devient non en comptes consolidés, en raison de la règle générale d’externalité des éléments couverts.
   - La désignation doit être faite dès l’origine avec documentation formelle de l’instrument de couverture, de l’élément couvert et du risque de change visé.
   - L’analyse doit être menée au niveau consolidé, pas seulement dans les comptes individuels des entités concernées.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le receivable de dividende constitue un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le receivable de dividende constitue un poste monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé.

**Raisonnment**:
En principe, un élément intragroupe ne peut pas être désigné comme élément couvert dans les comptes consolidés. Toutefois, IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés en consolidation. Un receivable de dividende déjà comptabilisé correspond, dans cette situation, à un actif reconnu exposé au risque de change pouvant affecter le résultat consolidé.

**Implications pratiques**: La documentation de couverture doit viser spécifiquement le risque de change du receivable intragroupe dans les comptes consolidés.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrits portent sur un receivable de dividende déjà comptabilisé, donc sur une exposition de bilan liée à un poste monétaire existant. Dans cette situation, le sujet n’est pas une transaction future hautement probable ni une variabilité de flux décrite comme telle dans le dossier, mais la réévaluation en change d’un actif reconnu. Le modèle cash flow hedge n’est donc pas celui qui correspond au cas présenté.

**Implications pratiques**: Le groupe ne devrait pas structurer cette désignation comme une couverture de flux sur la seule base du receivable de dividende déjà reconnu.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici provient d’un receivable de dividende intragroupe, pas d’un investissement net dans une activité étrangère. IFRIC 16 réserve ce modèle au risque de change lié aux net assets d’une foreign operation inclus dans les états financiers. Le cas décrit ne correspond pas à cette nature d’élément couvert.

**Implications pratiques**: La relation ne doit pas être documentée comme une couverture d’investissement net.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16.2
    >the item being hedged ... may be an amount of net assets
 - ifric-16.6
    >applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations