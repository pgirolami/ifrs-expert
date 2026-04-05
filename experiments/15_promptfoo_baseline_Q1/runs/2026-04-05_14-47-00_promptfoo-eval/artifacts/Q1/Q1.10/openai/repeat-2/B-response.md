# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans un contexte de consolidation IFRS, une relation de couverture peut-elle être documentée au titre du risque de change sur des dividendes intragroupe comptabilisés à recevoir ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question porte sur des états financiers consolidés en IFRS.
   - Le poste visé est un dividende intragroupe déjà comptabilisé à recevoir, donc un solde intragroupe reconnu.
   - Le risque analysé est uniquement le risque de change attaché à ce solde intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le dividende à recevoir constitue un élément monétaire intragroupe exposé à des écarts de change non totalement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Vérifier dès l’origine si la créance de dividende est bien un élément monétaire intragroupe en devise.
   - Documenter explicitement pourquoi les écarts de change sur ce solde ne sont pas totalement éliminés en consolidation.
   - Éviter une documentation en cash flow hedge si le dividende est déjà comptabilisé à recevoir.
   - Ne pas assimiler ce solde à une couverture d’investissement net : l’objet couvert doit être les actifs nets de l’opération étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le dividende à recevoir est un élément monétaire intragroupe reconnu<br>- Les entités concernées ont des monnaies fonctionnelles différentes<br>- Les gains ou pertes de change sur ce solde ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende à recevoir est un élément monétaire intragroupe reconnu
   - Les entités concernées ont des monnaies fonctionnelles différentes
   - Les gains ou pertes de change sur ce solde ne sont pas totalement éliminés en consolidation

**Raisonnment**:
Dans cette situation, le dividende intragroupe comptabilisé à recevoir est un actif reconnu. En consolidation, les éléments intragroupe sont en principe exclus, sauf l’exception visant un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés. Si ce cas est rempli, le risque de change sur la créance peut être documenté comme risque couvert sur un actif reconnu.

**Implications pratiques**: La documentation doit viser le risque de change sur la créance intragroupe reconnue, avec démonstration de l’effet résiduel en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le cas décrit vise un dividende déjà comptabilisé à recevoir, donc non une transaction future hautement probable. Or, dans le contexte intragroupe en consolidation, IFRS 9 ne prévoit l’exception qu’à propos de transactions intragroupe futures hautement probables affectant le résultat consolidé. Ce n’est pas le cadrage naturel du fait décrit.

**Implications pratiques**: La relation ne devrait pas être documentée comme cash flow hedge sur la base des faits décrits.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Un dividende intragroupe à recevoir n’est pas un investissement net dans une activité étrangère. La couverture d’investissement net vise le risque de change sur les actifs nets d’une opération étrangère inclus dans les comptes consolidés, pas un solde intragroupe de dividende.

**Implications pratiques**: Cette voie ne convient pas pour documenter le risque de change d’un dividende intragroupe à recevoir.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets