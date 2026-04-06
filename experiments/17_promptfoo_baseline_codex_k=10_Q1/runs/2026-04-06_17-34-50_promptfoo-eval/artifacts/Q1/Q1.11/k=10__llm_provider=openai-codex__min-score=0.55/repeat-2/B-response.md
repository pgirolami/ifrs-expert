# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise un dividende intragroupe libellé en devise, pour lequel une créance intra-groupe a déjà été comptabilisée avant l’établissement des comptes consolidés.
   - L’analyse est limitée au hedge accounting IFRS 9, dans les comptes consolidés, sur le seul risque de change de cette créance intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende constitue un élément monétaire intragroupe dont le risque de change génère des écarts non intégralement éliminés en consolidation. À défaut, l’élément intragroupe ne peut pas être désigné comme élément couvert dans les comptes consolidés.

## Points Opérationnels

   - Le point décisif en consolidation est l’exception IFRS 9 sur les éléments monétaires intragroupe : sans écarts de change non totalement éliminés, pas de hedge accounting.
   - La documentation doit être mise en place au moment de la désignation du hedge relationship et identifier clairement la créance, le risque de change couvert et l’instrument de couverture.
   - Le modèle de net investment hedge doit être écarté ici, sauf si la relation de couverture vise en réalité des net assets d’une foreign operation et non la créance de dividende elle-même.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change sur cette créance génère des écarts qui ne sont pas entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change affecte encore le résultat consolidé car les écarts ne sont pas totalement éliminés. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change sur cette créance génère des écarts qui ne sont pas entièrement éliminés en consolidation.

**Raisonnment**:
La créance de dividende déjà comptabilisée est, dans les faits posés, un actif reconnu. IFRS 9 permet une couverture de juste valeur d’un actif reconnu pour un risque particulier. Toutefois, en consolidation, un élément intragroupe n’est éligible que par exception s’il s’agit d’un élément monétaire intragroupe dont le risque de change crée des gains/pertes non totalement éliminés.

**Implications pratiques**: Si ces conditions sont remplies, une documentation de fair value hedge du risque de change est envisageable au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change affecte encore le résultat consolidé car les écarts ne sont pas totalement éliminés.

**Raisonnment**:
IFRS 9 admet la couverture de flux de trésorerie d’un actif reconnu pour une variabilité de flux attribuable à un risque particulier. Dans cette situation, l’obstacle principal reste l’intragroupe : en comptes consolidés, la créance de dividende ne peut être un élément couvert que si l’exception relative aux éléments monétaires intragroupe et aux écarts de change non éliminés est satisfaite.

**Implications pratiques**: En pratique, sans impact résiduel du change au niveau consolidé, une cash flow hedge ne peut pas être documentée sur cette créance intragroupe.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability
 - 6.3.5
    >not in the consolidated financial statements of the group

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe déjà enregistrée, et non sur une exposition de conversion liée à un investissement net dans une opération étrangère. Le modèle de net investment hedge vise les net assets d’une foreign operation, pas une créance de dividende intragroupe isolée.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule comptable pour couvrir la créance de dividende intragroupe décrite.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount