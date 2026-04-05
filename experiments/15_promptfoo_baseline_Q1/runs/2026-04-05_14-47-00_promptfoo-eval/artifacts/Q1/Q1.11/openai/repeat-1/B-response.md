# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise l'application du hedge accounting selon IFRS 9 dans des comptes consolidés.
   - Le dividende intragroupe a déjà donné lieu à la comptabilisation d'une créance, créant une exposition de change sur un élément monétaire reconnu.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe via une couverture de juste valeur de l'exposition de change sur la créance intragroupe reconnue. Cela n'est possible en consolidé que si cette créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.

## Points Opérationnels

   - Le point clé en consolidé est de démontrer que la créance de dividende est un élément monétaire intragroupe dont le risque de change affecte encore le résultat consolidé.
   - La documentation doit être mise en place à l'inception de la relation de couverture et identifier l'instrument, l'élément couvert et le risque de change visé.
   - Si le dividende n'était pas encore comptabilisé mais seulement prévu, l'analyse relèverait d'une transaction future et non de la présente situation.
   - Le traitement doit être apprécié au niveau des comptes consolidés, pas seulement dans les comptes individuels des entités du groupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est libellée dans une devise créant un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.<br>- Les gains ou pertes de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est libellée dans une devise créant un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - Les gains ou pertes de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Ici, l'exposition porte sur une créance intragroupe déjà comptabilisée, donc sur un actif reconnu. IFRS 9 permet une fair value hedge d'un actif reconnu pour un risque particulier affectant le résultat, et prévoit une exception en consolidé pour le risque de change d'un élément monétaire intragroupe lorsqu'il n'est pas totalement éliminé en consolidation.

**Implications pratiques**: La documentation de couverture en consolidé peut viser spécifiquement le risque de change de la créance reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite ne porte pas sur un dividende intragroupe futur hautement probable, mais sur une créance déjà enregistrée. Une fois la créance constatée, l'enjeu est l'exposition de change sur un élément monétaire reconnu, ce qui correspond au modèle de fair value hedge plutôt qu'à une variabilité de flux d'une transaction future.

**Implications pratiques**: La relation ne devrait pas être documentée comme cash flow hedge pour la créance déjà reconnue.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 3. Couverture d'un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividende intragroupe après comptabilisation, non une exposition sur des net assets d'une activité étrangère. Le modèle de net investment hedge est réservé au risque de change provenant d'un investissement net dans une activité étrangère, pas à une créance de dividende intragroupe isolée.

**Implications pratiques**: Il ne faut pas documenter cette couverture comme hedge of a net investment.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 2
    >The item being hedged ... may be an amount of net assets