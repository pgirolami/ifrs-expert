# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Peut-on appliquer la comptabilité de couverture en consolidation à l’exposition de change résultant de dividendes intragroupe dès lors que ceux-ci ont été comptabilisés en créance à recevoir ?

**Documentation consultée**
   - `ifrs9`
   - `ifric17`
   - `ias32`
   - `ifrs18`
   - `ias7`
   - `ifric2`
   - `ifrs19`
   - `ifric16`
   - `ifrs7`
   - `ias37`
   - `sic25`

## Hypothèses
   - La question vise les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe a été comptabilisé en créance/dette intragroupe et constitue donc un élément monétaire intragroupe.
   - La créance et la dette sont libellées dans une devise qui crée un risque de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, si la créance de dividende est un élément monétaire intragroupe dont le risque de change n’est pas entièrement éliminé en consolidation. La voie pertinente est une couverture de juste valeur ou de flux de trésorerie selon la désignation retenue; la couverture de net investment n’est pas adaptée au dividende à recevoir lui-même.

## Points Opérationnels

   - Le point clé en consolidation est l’exception d’IFRS 9 pour les éléments monétaires intragroupe: sans écarts de change non entièrement éliminés, pas de hedged item éligible.
   - La comptabilisation préalable du dividende en créance/dette est importante: on n’est plus dans une simple transaction intragroupe future, mais dans un élément monétaire reconnu.
   - Il faut documenter dès l’origine la relation de couverture, le risque de change couvert, l’instrument de couverture et la manière d’apprécier l’efficacité.
   - La couverture d’investissement net reste distincte et ne doit pas être utilisée pour qualifier la créance de dividende elle-même.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un élément monétaire intragroupe<br>- Les entités concernées ont des monnaies fonctionnelles différentes<br>- Les écarts de change ne sont pas totalement éliminés en consolidation<br>- La relation de couverture satisfait aux critères de documentation et d’efficacité d’IFRS 9 |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance de dividende reconnue expose à une variabilité de flux de trésorerie liée au change<br>- Le risque de change de l’élément monétaire intragroupe affecte le résultat consolidé<br>- Les critères de documentation, relation économique et hedge ratio d’IFRS 9 sont respectés |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un élément monétaire intragroupe
   - Les entités concernées ont des monnaies fonctionnelles différentes
   - Les écarts de change ne sont pas totalement éliminés en consolidation
   - La relation de couverture satisfait aux critères de documentation et d’efficacité d’IFRS 9

**Raisonnment**:
La créance de dividende déjà comptabilisée est, dans les faits supposés, un actif reconnu exposé au risque de change. En consolidation, IFRS 9 autorise par exception la désignation du risque de change d’un élément monétaire intragroupe si ce risque génère des écarts de change non totalement éliminés. La relation doit ensuite satisfaire aux critères de désignation et d’efficacité.

**Implications pratiques**: Possible en consolidation, mais seulement si le risque couvert est formellement désigné et mesurable sur la créance reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.4.1
    >there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende reconnue expose à une variabilité de flux de trésorerie liée au change
   - Le risque de change de l’élément monétaire intragroupe affecte le résultat consolidé
   - Les critères de documentation, relation économique et hedge ratio d’IFRS 9 sont respectés

**Raisonnment**:
Le texte IFRS 9 permet une couverture de flux de trésorerie pour la variabilité des flux d’un actif reconnu attribuable à un risque particulier. Dans cette situation, la créance de dividende en devise expose le groupe à une variabilité de flux en monnaie fonctionnelle; l’exception relative aux éléments monétaires intragroupe en consolidation permet la désignation si les écarts de change subsistent en consolidation.

**Implications pratiques**: Peut être envisagée si l’entité documente la couverture comme variabilité de flux de trésorerie du dividende à encaisser.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >there is an economic relationship

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette modalité vise l’exposition de change résultant d’un investissement net dans une activité étrangère, c’est-à-dire des actifs nets de l’opération étrangère. Un dividende intragroupe déjà constaté en créance à recevoir n’est pas, dans cette question, l’investissement net lui-même mais une créance monétaire distincte. L’exposition pertinente est donc celle de l’élément monétaire intragroupe, non celle du net investment.

**Implications pratiques**: La réponse ne doit pas être fondée sur un hedge de net investment pour la créance de dividende elle-même.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.