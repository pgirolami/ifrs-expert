# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise l'application de la comptabilité de couverture dans des comptes consolidés au titre d'IFRS 9.
   - Le dividende intragroupe a donné lieu à la comptabilisation d'une créance à recevoir et le risque visé est le risque de change.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, une couverture du risque de change peut être documentée sur une créance intragroupe si ce risque n'est pas totalement éliminé en consolidation. Le modèle le plus cohérent ici est la fair value hedge; la cash flow hedge n'est envisageable que si l'entité documente bien une variabilité de flux de trésorerie affectant le résultat.

## Points Opérationnels

   - Le point décisif en consolidé est de démontrer que le risque de change sur la créance intragroupe affecte bien le résultat consolidé et n'est pas totalement éliminé.
   - La documentation doit être en place à l'origine de la relation de couverture et identifier l'instrument de couverture, l'élément couvert, le risque couvert et le test d'efficacité.
   - Au vu des faits décrits, la fair value hedge est la qualification la plus naturelle pour une créance de dividende déjà comptabilisée.
   - La net investment hedge doit être écartée car la créance de dividende n'est pas l'investissement net dans l'entité étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un élément monétaire intragroupe exposé au change<br>- Les gains ou pertes de change ne sont pas totalement éliminés en consolidation<br>- La relation de couverture est formellement désignée et documentée dès l'origine selon IFRS 9.6.4.1 |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La variabilité des flux de trésorerie liée au change affecte le résultat consolidé<br>- Le risque de change sur la créance intragroupe n'est pas totalement éliminé en consolidation<br>- La relation remplit les critères de désignation, documentation et efficacité d'IFRS 9.6.4.1 |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un élément monétaire intragroupe exposé au change
   - Les gains ou pertes de change ne sont pas totalement éliminés en consolidation
   - La relation de couverture est formellement désignée et documentée dès l'origine selon IFRS 9.6.4.1

**Raisonnment**:
La créance de dividende déjà comptabilisée est un actif reconnu, ce qui correspond au périmètre d'une fair value hedge. En consolidé, les éléments intragroupe sont en principe exclus, sauf pour le risque de change d'un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. Il faut aussi satisfaire la documentation et les tests d'efficacité IFRS 9.

**Implications pratiques**: Possible en consolidé si vous documentez la couverture du risque de change sur la créance reconnue et démontrez l'effet en résultat consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.4.1
    >at the inception ... there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La variabilité des flux de trésorerie liée au change affecte le résultat consolidé
   - Le risque de change sur la créance intragroupe n'est pas totalement éliminé en consolidation
   - La relation remplit les critères de désignation, documentation et efficacité d'IFRS 9.6.4.1

**Raisonnment**:
IFRS 9 permet une cash flow hedge sur la variabilité des flux de trésorerie d'un actif reconnu. Dans votre cas, cela n'est recevable en consolidé que si la créance intragroupe en devise crée bien une variabilité de flux en monnaie fonctionnelle qui affecte le résultat consolidé et que cette exposition n'est pas totalement éliminée. Cette lecture est plus conditionnelle qu'une fair value hedge pour une créance déjà reconnue.

**Implications pratiques**: En pratique, cette voie demande une documentation plus robuste pour démontrer une véritable exposition de flux en résultat consolidé.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... of ... a recognised asset
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >there is an economic relationship between the hedged item and the hedging instrument

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le sujet posé concerne des dividendes intragroupe déjà constatés en créance, donc un poste monétaire/transactionnel, et non un investissement net dans une activité à l'étranger. IFRIC 16 réserve ce modèle au risque de change lié à la net investment in a foreign operation. Il ne convient donc pas à la couverture d'une créance de dividende intragroupe.

**Implications pratiques**: Ne pas documenter cette couverture comme hedge d'investissement net pour une créance de dividende intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation