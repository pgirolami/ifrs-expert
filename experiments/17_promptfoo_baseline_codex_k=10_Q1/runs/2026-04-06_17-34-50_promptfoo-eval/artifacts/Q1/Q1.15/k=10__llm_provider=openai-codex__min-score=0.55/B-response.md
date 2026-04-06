# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée au niveau des états financiers consolidés selon IFRS 9.
   - L’exposition visée est un risque de change sur une créance intragroupe monétaire issue d’une distribution de dividendes.
   - Cette créance est entre entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance intragroupe crée un risque de change qui n’est pas intégralement éliminé en consolidation. En consolidation, les expositions intragroupe ne sont en principe pas éligibles, sauf l’exception IFRS 9 relative au risque de change d’un élément monétaire intragroupe.

## Points Opérationnels

   - Point clé en consolidation : l’éligibilité ne repose pas sur le fait que la créance est reconnue, mais sur le fait que le risque de change n’est pas entièrement éliminé à la consolidation.
   - Si la créance de dividende est entre entités de monnaies fonctionnelles différentes, analyser si les écarts de change sur l’élément monétaire subsistent en résultat consolidé.
   - La documentation de couverture doit identifier précisément le risque de change couvert et démontrer le respect des critères d’IFRS 9 à l’origine de la relation.
   - Si l’exposition de change est totalement éliminée en consolidation, la réponse est non en pratique.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit constituer un élément monétaire intragroupe.<br>- Le risque de change doit générer des gains ou pertes qui ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance doit être un élément monétaire intragroupe exposé au change.<br>- L’exposition de change doit affecter le résultat consolidé parce qu’elle n’est pas totalement éliminée en consolidation. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit constituer un élément monétaire intragroupe.
   - Le risque de change doit générer des gains ou pertes qui ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
La créance est un actif comptabilisé, donc elle peut en principe entrer dans une relation de couverture. Toutefois, en consolidation, les éléments intragroupe ne sont pas éligibles sauf pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans cette situation, la désignation n’est possible que si cette exception est satisfaite.

**Implications pratiques**: Documenter que la créance de dividende est monétaire et que ses écarts de change affectent encore le résultat consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un élément monétaire intragroupe exposé au change.
   - L’exposition de change doit affecter le résultat consolidé parce qu’elle n’est pas totalement éliminée en consolidation.

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie pour la variabilité des flux d’un actif comptabilisé. Mais, en consolidation, un élément intragroupe ne peut être couvert que dans les cas expressément admis. Pour une créance intragroupe déjà comptabilisée, l’exception pertinente est celle des éléments monétaires intragroupe avec risque de change non totalement éliminé.

**Implications pratiques**: Vérifier que le risque couvert est bien la variabilité des flux en monnaie fonctionnelle liée au change et non un simple flux intragroupe éliminé.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe comptabilisée, non sur un investissement net dans une activité à l’étranger. Le modèle de couverture d’investissement net vise le risque de change attaché aux net assets d’une activité étrangère, pas une créance de dividende intragroupe isolée.

**Implications pratiques**: Ne pas traiter la créance de dividende comme un investissement net couvert.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets