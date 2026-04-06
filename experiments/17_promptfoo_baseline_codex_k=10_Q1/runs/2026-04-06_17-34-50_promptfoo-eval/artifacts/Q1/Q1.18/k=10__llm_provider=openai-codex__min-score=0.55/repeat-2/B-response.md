# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - L’analyse est faite au niveau des comptes consolidés.
   - La créance sur dividendes intragroupe est une exposition de change issue d’un élément intragroupe monétaire.
   - La question vise l’éligibilité de cette exposition de change comme élément couvert, et non l’éligibilité de l’instrument de couverture.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, un élément intragroupe n’est en principe pas éligible. Toutefois, l’exception IFRS 9 permet la couverture du risque de change d’un élément monétaire intragroupe si ce risque génère des écarts de change non totalement éliminés en consolidation. Dans ce cas, l’exposition peut être éligible.

## Points Opérationnels

   - Point décisif : vérifier si les écarts de change sur la créance de dividendes sont non totalement éliminés en consolidation.
   - Si cette condition n’est pas remplie, l’exposition n’est pas éligible au niveau consolidé malgré son identification comptable distincte.
   - Parmi les modèles fournis, la couverture de juste valeur est le cadre le plus naturel pour une créance déjà reconnue ; la couverture de flux n’est envisageable que si la documentation vise bien la variabilité des flux.
   - La couverture d’investissement net doit être écartée car elle vise les net assets d’une activité étrangère, pas une créance de dividendes intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance sur dividendes est un élément monétaire intragroupe.<br>- Le risque de change sur cette créance génère des écarts non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La relation est documentée comme couvrant la variabilité des flux en devise de la créance reconnue.<br>- Le risque de change de l’élément monétaire intragroupe affecte le résultat consolidé car il n’est pas totalement éliminé. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance sur dividendes est un élément monétaire intragroupe.
   - Le risque de change sur cette créance génère des écarts non totalement éliminés en consolidation.

**Raisonnment**:
La créance sur dividendes déjà comptabilisée est un actif reconnu, ce qui correspond au champ possible d’une couverture de juste valeur. En consolidation, l’obstacle intragroupe est levé uniquement si le risque de change sur cet élément monétaire n’est pas totalement éliminé à la consolidation. Sans cette condition, l’élément n’est pas éligible.

**Implications pratiques**: Documenter la relation comme couverture du risque de change de la créance reconnue, seulement pour la part non éliminée en consolidation.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La relation est documentée comme couvrant la variabilité des flux en devise de la créance reconnue.
   - Le risque de change de l’élément monétaire intragroupe affecte le résultat consolidé car il n’est pas totalement éliminé.

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie sur un actif reconnu lorsqu’il existe une variabilité de flux attribuable à un risque particulier. Dans cette situation, ce modèle n’est envisageable qu’à la même condition d’exception applicable aux éléments intragroupe en consolidation, à savoir un risque de change non totalement éliminé.

**Implications pratiques**: Possible en théorie, mais la documentation doit viser une variabilité de flux et non seulement la réévaluation de la créance.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance sur dividendes intragroupe comptabilisée, donc sur un poste monétaire intragroupe distinct. Ce n’est pas une couverture du risque de change attaché à un investissement net dans une opération étrangère ; ce modèle ne correspond donc pas aux faits décrits.

**Implications pratiques**: Ne pas traiter la créance sur dividendes comme un investissement net couvert.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations