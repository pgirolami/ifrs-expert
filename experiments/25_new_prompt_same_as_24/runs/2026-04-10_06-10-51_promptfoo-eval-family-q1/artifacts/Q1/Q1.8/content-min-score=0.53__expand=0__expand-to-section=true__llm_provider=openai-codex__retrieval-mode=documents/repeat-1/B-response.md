# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - La question porte sur les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe a été comptabilisé en créance à recevoir et en dette correspondante entre entités du groupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que l’élément intragroupe crée une exposition de change.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, la comptabilité de couverture peut viser l’exposition de change d’un dividende intragroupe déjà comptabilisé en créance à recevoir si cette créance/dette constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, le modèle pertinent est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point déterminant est le passage d’un dividende prévu à une créance reconnue : cela oriente l’analyse vers un actif reconnu et non vers une transaction future.
   - En consolidation, il faut documenter que l’exposition de change sur la créance/dette intragroupe n’est pas totalement éliminée du fait de monnaies fonctionnelles différentes.
   - Si les conditions de l’exception IFRS 9 sur les éléments monétaires intragroupe ne sont pas remplies, la réponse devient négative en consolidation.
   - La documentation de couverture doit être établie au niveau consolidé et viser spécifiquement le risque de change du poste intragroupe reconnu.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dividende intragroupe doit constituer un élément monétaire intragroupe.<br>- Le risque de change doit générer des gains ou pertes de change non totalement éliminés en consolidation en raison de monnaies fonctionnelles différentes.<br>- L’élément couvert doit être fiable-ment mesurable. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dividende intragroupe doit constituer un élément monétaire intragroupe.
   - Le risque de change doit générer des gains ou pertes de change non totalement éliminés en consolidation en raison de monnaies fonctionnelles différentes.
   - L’élément couvert doit être fiable-ment mesurable.

**Raisonnment**:
Dans cette situation, le dividende intragroupe a déjà donné lieu à une créance reconnue, donc à un actif reconnu pouvant en principe être un élément couvert. En consolidation, IFRS 9 interdit en général les éléments intragroupe, mais prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. C’est précisément le cas visé par l’hypothèse retenue.

**Implications pratiques**: Si ces conditions sont remplies, l’exposition de change sur la créance de dividende peut être désignée comme élément couvert en consolidation dans une relation de couverture de juste valeur.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.2
    >The hedged item must be reliably measurable

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise notamment une transaction prévue hautement probable. Or, ici, la question précise que les dividendes intragroupe ont déjà été comptabilisés en créance à recevoir : l’exposition n’est donc plus une transaction future prévue mais un poste reconnu. Le modèle n’est pas celui qui correspond au fait décrit.

**Implications pratiques**: Une fois la créance de dividende reconnue, la couverture pertinente n’est pas une couverture de flux de trésorerie.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... forecast transaction
 - 6.3.3
    >that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net concerne le risque de change lié à un investissement net dans une activité étrangère, c’est-à-dire aux actifs nets d’une opération étrangère inclus dans les états financiers. Un dividende intragroupe comptabilisé en créance à recevoir correspond ici à un poste intragroupe spécifique, non à l’investissement net lui-même. Ce n’est donc pas le modèle adapté au cas posé.

**Implications pratiques**: La question doit être traitée comme une exposition sur un poste intragroupe reconnu, non comme une couverture d’investissement net.

**Référence**:
 - 2
    >foreign currency risk arising from the net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity