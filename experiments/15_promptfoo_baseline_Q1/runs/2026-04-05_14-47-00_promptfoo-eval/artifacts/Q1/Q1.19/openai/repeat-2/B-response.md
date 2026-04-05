# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans un schéma où des dividendes intragroupe ont déjà été reconnus en créance à recevoir, la question se pose du traitement du risque de change associé en consolidation. Ce risque peut-il être formellement documenté dans une relation de couverture ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question est analysée au niveau des états financiers consolidés.
   - Le dividende intragroupe a déjà été comptabilisé comme une créance à recevoir libellée en devise étrangère par une entité du groupe sur une autre entité du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d'une créance intragroupe peut être documenté dans une relation de couverture uniquement s'il s'agit d'un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, la voie la plus directement alignée avec les faits est la couverture de juste valeur ; la couverture de flux de trésorerie n'est envisageable que si l'exposition est effectivement désignée comme variabilité de flux de trésorerie.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés.
   - La documentation doit identifier l'élément couvert, le risque de change couvert et l'effet attendu sur le résultat consolidé.
   - Si l'exposition n'affecte pas le résultat consolidé, la relation de couverture ne peut pas être soutenue au niveau consolidé.
   - Au vu des faits décrits, la qualification en couverture de juste valeur est généralement la plus directement cohérente avec une créance déjà reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe constitue un élément monétaire.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.<br>- Le risque couvert est celui de change susceptible d'affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La relation est désignée comme couverture de la variabilité des flux liée au risque de change.<br>- Le risque de change sur la créance intragroupe affecte le résultat consolidé.<br>- L'exception IFRS 9 pour l'élément monétaire intragroupe est satisfaite. |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe constitue un élément monétaire.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.
   - Le risque couvert est celui de change susceptible d'affecter le résultat consolidé.

**Raisonnment**:
Ici, la créance de dividende est déjà reconnue : il s'agit donc d'un actif comptabilisé. En consolidation, un élément intragroupe est en principe exclu, mais IFRS 9 admet une exception pour le risque de change d'un élément monétaire intragroupe si les gains/pertes de change ne sont pas totalement éliminés. Dans ce cas précis, une documentation formelle en couverture de juste valeur est possible.

**Implications pratiques**: Documenter la relation dès lors que la créance en devise expose encore le groupe à un effet de change en résultat consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La relation est désignée comme couverture de la variabilité des flux liée au risque de change.
   - Le risque de change sur la créance intragroupe affecte le résultat consolidé.
   - L'exception IFRS 9 pour l'élément monétaire intragroupe est satisfaite.

**Raisonnment**:
IFRS 9 permet en principe une couverture de flux de trésorerie sur un actif ou passif comptabilisé. Dans cette situation, elle n'est recevable que si l'exposition visée est bien la variabilité des flux en monnaie fonctionnelle liée au change et si cette variabilité affecte le résultat consolidé malgré l'intragroupe. Ce n'est donc pas l'option la plus évidente, mais elle n'est pas exclue par principe sur les textes fournis.

**Implications pratiques**: N'utiliser cette qualification que si la documentation vise clairement la variabilité des flux en devise convertis en monnaie fonctionnelle.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits portent sur une créance de dividende intragroupe déjà reconnue, et non sur un montant de net assets d'une activité étrangère. Le modèle IFRIC 16 vise exclusivement le risque de change lié à un investissement net dans une activité à l'étranger. Il ne s'applique donc pas à cette créance de dividende en tant que telle.

**Implications pratiques**: Ne pas documenter cette exposition comme couverture d'investissement net.

**Référence**:
 - ifric-16.7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16.10
    >the hedged item can be an amount of net assets