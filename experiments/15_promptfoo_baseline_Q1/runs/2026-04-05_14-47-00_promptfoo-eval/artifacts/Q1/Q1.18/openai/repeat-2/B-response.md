# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question porte sur la comptabilité de couverture selon IFRS 9 dans des comptes consolidés.
   - L’exposition de change identifiée provient d’un solde ou d’une transaction intragroupe.
   - La créance sur dividendes intragroupe est analysée comme une créance monétaire intragroupe déjà comptabilisée.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, une telle exposition n’est éligible que par exception si la créance constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. À défaut de cette exception, les éléments intragroupe ne sont pas des éléments couverts éligibles.

## Points Opérationnels

   - Le point décisif est de vérifier si l’écart de change sur la créance intragroupe affecte réellement le résultat consolidé au lieu d’être éliminé.
   - Si cette condition n’est pas satisfaite, l’exposition n’est pas éligible comme élément couvert au niveau consolidé.
   - Si elle l’est, la documentation de couverture doit identifier la créance, le risque de change couvert et le fait qu’il s’agit d’un risque résiduel en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit constituer un élément monétaire intragroupe.<br>- Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit constituer un élément monétaire intragroupe.
   - Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance sur dividendes est un poste intragroupe, donc en principe non éligible en consolidation. Elle ne peut devenir éligible que si elle relève de l’exception visant le risque de change d’un élément monétaire intragroupe générant des écarts non totalement éliminés en consolidation. Si cette condition est remplie, une couverture de juste valeur est le modèle le plus cohérent pour une créance reconnue.

**Implications pratiques**: Documenter précisément que l’élément couvert est uniquement le risque de change résiduel au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit est une créance intragroupe déjà comptabilisée, pas une exposition à une variabilité de flux de trésorerie d’une transaction future hautement probable. Le modèle de cash flow hedge vise surtout des flux variables ou des transactions futures, ce qui ne correspond pas à une créance de dividendes reconnue.

**Implications pratiques**: Ne pas retenir ce modèle pour une créance de dividendes intragroupe déjà constatée en consolidation.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.2
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
L’exposition identifiée provient ici d’une créance de dividendes intragroupe, non d’un investissement net dans une activité à l’étranger. IFRIC 16 réserve ce modèle au risque de change sur les net assets d’une opération étrangère inclus dans les états financiers, ce qui est distinct d’une créance de dividende.

**Implications pratiques**: Ne pas assimiler la créance de dividendes à l’investissement net dans l’entité étrangère.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16 1
    >The item being hedged ... may be an amount of net assets
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations