# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question porte sur l’application de la comptabilité de couverture en comptes consolidés selon IFRS 9.
   - La créance de dividende intragroupe a été comptabilisée et constitue une créance monétaire exposée au risque de change.
   - Le dividende intragroupe est entre entités du groupe et non avec une partie externe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidé, un poste intragroupe n’est en principe pas éligible comme élément couvert. Toutefois, l’exception IFRS 9 permet de couvrir le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, la voie la plus cohérente ici est la couverture du poste reconnu, pas une couverture de net investment.

## Points Opérationnels

   - En consolidé, partez d’abord de l’interdiction générale des postes intragroupe, puis documentez explicitement pourquoi l’exception de 6.3.6 s’applique.
   - La documentation doit être établie dès l’origine de la relation de couverture et identifier l’instrument, la créance couverte, le risque de change et le test d’efficacité.
   - Le point décisif est de démontrer que les écarts de change sur la créance de dividende ne sont pas totalement éliminés en consolidation, notamment si les entités ont des monnaies fonctionnelles différentes.
   - La piste net investment hedge doit être écartée ici, car elle vise les net assets d’une activité étrangère, non une créance de dividende intragroupe reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit créer une exposition de change non totalement éliminée en consolidation.<br>- Le risque couvert doit être limité à la composante change de la créance reconnue.<br>- La relation doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance intragroupe doit entraîner une variabilité de flux liée au change affectant le résultat consolidé.<br>- Les écarts de change sur cet élément monétaire ne doivent pas être totalement éliminés en consolidation.<br>- La relation doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit créer une exposition de change non totalement éliminée en consolidation.
   - Le risque couvert doit être limité à la composante change de la créance reconnue.
   - La relation doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
La créance de dividende déjà comptabilisée est un actif reconnu. En consolidé, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans cette situation, une documentation de couverture peut donc être mise en place sur la composante change du poste reconnu.

**Implications pratiques**: Possible en consolidé si vous démontrez que le change sur la créance intragroupe subsiste au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit entraîner une variabilité de flux liée au change affectant le résultat consolidé.
   - Les écarts de change sur cet élément monétaire ne doivent pas être totalement éliminés en consolidation.
   - La relation doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
IFRS 9 admet la couverture des flux variables d’un actif reconnu et, en consolidé, l’exception sur les éléments monétaires intragroupe vise aussi le risque de change. Donc ce traitement n’est pas exclu dans votre cas. Il reste toutefois conditionné au fait que l’exposition de change sur la créance intragroupe affecte le résultat consolidé et ne soit pas totalement éliminée.

**Implications pratiques**: Possible seulement si vous pouvez justifier que l’exposition couverte est bien une variabilité de flux de change pertinente au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item... may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.4.1
    >there is formal designation and documentation of the hedging relationship

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Votre question vise la composante change d’une créance de dividende intragroupe déjà reconnue, pas le risque de change sur un investissement net dans une activité à l’étranger. IFRIC 16 encadre spécifiquement la couverture du risque de change lié aux net assets d’une foreign operation. Ce modèle ne correspond donc pas au fait générateur décrit.

**Implications pratiques**: Ne pas documenter cette créance de dividende comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets