# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - L’exposition visée est un risque de change constaté dans les états financiers consolidés.
   - La créance de dividendes intragroupe est une créance monétaire reconnue en consolidation et sa sensibilité de change n’est pas entièrement éliminée en consolidation.
   - La question porte sur la possibilité de documenter une relation de couverture au sens d’IFRS 9 pour cette exposition spécifique.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, seulement si la créance de dividendes intragroupe génère un risque de change non entièrement éliminé à la consolidation. Dans ce cas, une documentation de hedge accounting peut être envisagée, en pratique plutôt en fair value hedge, tandis que la couverture de net investment n’est pas adaptée à cette créance.

## Points Opérationnels

   - Le point décisif est de vérifier que la créance de dividendes intragroupe crée encore un risque de change non entièrement éliminé en consolidation.
   - La documentation doit identifier l’instrument de couverture, la créance couverte, le risque de change couvert et la méthode d’évaluation de l’efficacité dès l’origine.
   - Si l’exposition est bien celle d’un élément monétaire intragroupe reconnu en consolidation, le modèle de fair value hedge sera généralement le plus direct à documenter.
   - Une couverture de net investment ne doit pas être utilisée pour requalifier une créance de dividendes qui n’est pas un montant de net assets d’une activité étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être reconnue en consolidation comme élément monétaire.<br>- Le risque de change sur cette créance ne doit pas être entièrement éliminé en consolidation.<br>- La variation liée au risque couvert doit pouvoir affecter le résultat. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La variabilité des flux de trésorerie de la créance doit être attribuable au risque de change.<br>- Le risque de change sur l’élément intragroupe doit ne pas être entièrement éliminé en consolidation.<br>- L’exposition couverte doit pouvoir affecter le résultat. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être reconnue en consolidation comme élément monétaire.
   - Le risque de change sur cette créance ne doit pas être entièrement éliminé en consolidation.
   - La variation liée au risque couvert doit pouvoir affecter le résultat.

**Raisonnment**:
La créance de dividendes est, dans cette situation, un actif reconnu en consolidation. IFRS 9 permet de couvrir un actif reconnu contre un risque particulier affectant le résultat, et admet exceptionnellement en consolidation le risque de change d’un élément monétaire intragroupe s’il n’est pas totalement éliminé à la consolidation.

**Implications pratiques**: Possible si la documentation vise précisément le risque de change de la créance reconnue en consolidation.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.4.1
    >the hedging relationship consists only of eligible hedging instruments and eligible hedged items

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La variabilité des flux de trésorerie de la créance doit être attribuable au risque de change.
   - Le risque de change sur l’élément intragroupe doit ne pas être entièrement éliminé en consolidation.
   - L’exposition couverte doit pouvoir affecter le résultat.

**Raisonnment**:
IFRS 9 permet une cash flow hedge d’un actif reconnu lorsqu’il existe une variabilité de flux attribuable à un risque particulier. Dans cette situation, cela n’est envisageable que si la créance de dividendes reconnue en consolidation porte bien une variabilité de flux en monnaie fonctionnelle liée au change et que cette exposition subsiste en consolidation.

**Implications pratiques**: Possible en principe, mais il faut démontrer que l’exposition de change de cette créance se prête au modèle de variabilité de flux.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >there is an economic relationship between the hedged item and the hedging instrument

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe reconnue en consolidation, non un montant de net assets d’une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change sur un investissement net dans une opération étrangère, pas à une créance de dividendes isolée.

**Implications pratiques**: Ce modèle ne convient pas à une créance de dividendes intragroupe prise isolément.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16.2
    >The item being hedged ... may be an amount of net assets
 - ifric-16.10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets