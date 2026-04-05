# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question porte sur la comptabilité de couverture dans des états financiers consolidés selon IFRS 9.
   - Le dividende intragroupe a déjà été reconnu en créance intercompagnie, donc comme élément monétaire comptabilisé et non comme simple transaction future.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en pratique via une couverture de juste valeur, si la créance intragroupe génère un risque de change dont les écarts ne sont pas intégralement éliminés en consolidation. En revanche, ce n’est pas un hedge de net investment, et la voie cash flow hedge n’est pas la plus adaptée ici.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que les écarts de change sur la créance intragroupe ne sont pas entièrement éliminés, typiquement lorsque les entités ont des monnaies fonctionnelles différentes.
   - La désignation doit être formalisée dès l’origine de la relation de couverture avec identification de l’instrument, de l’élément couvert, du risque de change et de la méthode d’évaluation de l’efficacité.
   - Si la créance de dividende est réglée rapidement, la fenêtre de couverture peut être courte et l’intérêt pratique de la désignation limité.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance intragroupe est un élément monétaire<br>- le risque de change génère des gains ou pertes non totalement éliminés en consolidation<br>- ce risque de change est désigné comme composante de risque identifiable et mesurable |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance intragroupe est un élément monétaire
   - le risque de change génère des gains ou pertes non totalement éliminés en consolidation
   - ce risque de change est désigné comme composante de risque identifiable et mesurable

**Raisonnment**:
Ici, la créance de dividende est un actif monétaire comptabilisé. IFRS 9 permet, par exception en consolidation, de désigner le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. Une couverture de juste valeur vise précisément un actif comptabilisé exposé à un risque particulier affectant le résultat.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé en visant le risque de change de la créance intercompagnie.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende n’est plus une transaction future hautement probable mais une créance déjà reconnue. La question vise le risque de change d’un élément monétaire existant, ce qui s’aligne sur une logique de couverture de juste valeur plutôt que sur une variabilité de flux futurs au sens de la cash flow hedge.

**Implications pratiques**: Ne pas structurer la désignation comme cash flow hedge pour cette créance de dividende déjà comptabilisée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La créance de dividende intragroupe est distincte d’un investissement net dans une activité à l’étranger. Le modèle de net investment hedge vise le risque de change sur des net assets d’une activité étrangère, pas une créance intercompagnie issue d’un dividende déclaré.

**Implications pratiques**: Ne pas traiter cette créance de dividende comme un élément couvert au titre d’une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets