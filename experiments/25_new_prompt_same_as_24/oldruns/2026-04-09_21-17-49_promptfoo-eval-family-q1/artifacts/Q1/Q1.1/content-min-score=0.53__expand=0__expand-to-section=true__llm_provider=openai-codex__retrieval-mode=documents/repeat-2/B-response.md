# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs9`
   - `ifrs12`
   - `ias37`
   - `ifric19`
   - `ifric16`

## Hypothèses
   - La question porte uniquement sur l’application de la comptabilité de couverture en comptes consolidés au risque de change lié à un dividende intragroupe comptabilisé en créance.
   - Selon les faits non fournis, l’exposition peut correspondre soit à une créance intragroupe monétaire déjà comptabilisée, soit à un flux futur, soit éventuellement à une exposition de type investissement net.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie la plus crédible est la couverture de juste valeur uniquement si la créance de dividende constitue un poste monétaire intragroupe dont le risque de change n’est pas entièrement éliminé en consolidation. La couverture de flux de trésorerie n’est pas adaptée au dividende lui-même, et la couverture d’investissement net ne vise pas, en l’état, la créance de dividende comptabilisée.

## Points Opérationnels

   - La documentation doit être appréciée au niveau des comptes consolidés, pas seulement dans les comptes individuels des entités du groupe.
   - Le point décisif est de démontrer que l’écart de change sur la créance intragroupe reste en résultat consolidé ; sinon l’élément couvert n’est pas éligible.
   - Si le dividende n’est encore qu’un flux futur, le modèle de cash flow hedge reste bloqué ici car le dividende est une distribution en capitaux propres et non un flux affectant le résultat consolidé.
   - La couverture d’investissement net ne doit être retenue que si l’exposition couverte est l’investissement net dans l’activité étrangère, et non la créance de dividende comptabilisée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe reconnu<br>- Le risque de change sur ce poste affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe reconnu
   - Le risque de change sur ce poste affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation

**Raisonnment**:
Dans cette situation, la créance de dividende déjà comptabilisée peut entrer dans un modèle de couverture d’un élément reconnu. Mais en comptes consolidés, un élément intragroupe n’est éligible que, pour le change, s’il s’agit d’un poste monétaire dont les écarts de change ne sont pas totalement éliminés en consolidation. Si cette condition n’est pas remplie, la documentation de couverture ne s’applique pas.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé sur la créance intragroupe et sur le seul risque de change restant en résultat consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction future hautement probable qui affectera le résultat consolidé. Or un dividende versé à des propriétaires est présenté comme une distribution en capitaux propres, pas comme un élément de résultat. Sur les faits donnés, le dividende intragroupe lui-même ne remplit donc pas, en consolidation, la condition d’un impact en profit ou perte.

**Implications pratiques**: Une documentation de cash flow hedge sur le dividende intragroupe lui-même ne paraît pas défendable en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... forecast transaction
 - 6.3.6
    >a highly probable forecast intragroup transaction may qualify ... provided that ... the foreign currency risk will affect consolidated profit or loss
 - 35
    >Distributions to holders of an equity instrument shall be recognised by the entity directly in equity

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net est un modèle distinct visant le risque de change d’un investissement net dans une activité à l’étranger. Ici, le fait décrit est une créance de dividende intragroupe déjà comptabilisée. Sur cette base, l’objet couvert n’est pas l’investissement net lui-même mais une créance spécifique ; cette approche ne correspond donc pas à la situation décrite.

**Implications pratiques**: Ne pas documenter la créance de dividende comme une couverture d’investissement net sans exposition distincte à l’investissement net identifiée.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation