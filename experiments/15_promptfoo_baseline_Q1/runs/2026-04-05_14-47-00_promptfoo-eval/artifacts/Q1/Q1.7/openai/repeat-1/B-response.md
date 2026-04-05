# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise la comptabilité de couverture selon IFRS 9 du risque de change dans des comptes consolidés.
   - Le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance, de sorte que l’élément envisagé est une créance monétaire intragroupe reconnue.
   - Aucune hypothèse n’est retenue selon laquelle l’entité serait une investment entity au sens d’IFRS 10.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, un élément intragroupe ne peut en principe pas être désigné, sauf exception pour le risque de change d’un élément monétaire intragroupe non totalement éliminé. Une couverture n’est donc recevable ici que si la créance de dividende génère un risque de change affectant encore le résultat consolidé.

## Points Opérationnels

   - Le point décisif est de démontrer, en consolidation, que la créance de dividende intragroupe crée bien un risque de change non totalement éliminé.
   - La documentation doit viser explicitement le risque de change sur l’élément monétaire intragroupe, et non le dividende intragroupe en tant que transaction interne en soi.
   - Si aucun impact de change ne subsiste en résultat consolidé, la couverture comptable n’est pas recevable sur ces faits.
   - La qualification doit être appréciée à la date de désignation, sur la base de la créance déjà reconnue et des monnaies fonctionnelles des entités concernées.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un élément monétaire intragroupe<br>- des écarts de change sur cette créance ne sont pas totalement éliminés en consolidation<br>- le risque couvert est le risque de change affectant le résultat consolidé |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un élément monétaire intragroupe
   - des écarts de change sur cette créance ne sont pas totalement éliminés en consolidation
   - le risque couvert est le risque de change affectant le résultat consolidé

**Raisonnment**:
La créance de dividende reconnue est, dans les faits décrits, un actif monétaire intragroupe déjà comptabilisé. En consolidation, IFRS 9 exclut en principe les éléments intragroupe, mais admet une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés à la consolidation. Dans ce cas précis, une documentation en fair value hedge est recevable seulement pour ce risque de change résiduel.

**Implications pratiques**: Vérifier d’abord si la créance de dividende laisse subsister un effet de change en résultat consolidé ; à défaut, la désignation échoue.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite ne porte pas sur un dividende futur hautement probable ni sur une variabilité future de flux, mais sur une créance déjà reconnue en consolidation. Le modèle cash flow hedge d’IFRS 9 vise des flux variables sur un actif ou passif reconnu ou une transaction future hautement probable ; ce n’est pas le fait décrit ici.

**Implications pratiques**: Sur ces faits, la documentation ne devrait pas être construite comme une cash flow hedge.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé concerne une créance de dividende intragroupe reconnue, non un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change sur les actifs nets d’une activité étrangère ; il ne s’applique pas à une créance de dividende isolée.

**Implications pratiques**: La documentation ne doit pas être fondée sur le modèle de couverture d’investissement net pour cette créance de dividende.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >applies only to hedges of net investments in foreign operations