# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée dans le cadre des comptes consolidés selon IFRS 9.
   - La créance de dividende intragroupe est un élément monétaire intragroupe libellé en devise, générant des écarts de change qui affectent le résultat consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en pratique via une couverture de juste valeur du risque de change porté par la créance reconnue. Cela n’est permis que si le risque de change sur l’élément monétaire intragroupe n’est pas totalement éliminé en consolidation et affecte le résultat consolidé.

## Points Opérationnels

   - Le point clé est le moment de reconnaissance : une fois le dividende enregistré en créance, l’analyse se fait sur un élément monétaire reconnu.
   - En consolidation, la possibilité de couvrir un poste intragroupe est exceptionnelle et limitée ici au risque de change d’un élément monétaire intragroupe affectant le résultat consolidé.
   - La documentation doit identifier clairement le risque couvert, l’instrument de couverture et démontrer que les écarts de change visés ne sont pas totalement éliminés en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe constitue un élément monétaire intragroupe.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.<br>- Le risque de change affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe constitue un élément monétaire intragroupe.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.
   - Le risque de change affecte le résultat consolidé.

**Raisonnment**:
Ici, le dividende intragroupe est déjà reconnu en créance dans les comptes consolidés ; il s’agit donc d’un actif reconnu. IFRS 9 permet, par exception, de désigner le risque de change d’un élément monétaire intragroupe en couverture s’il génère des écarts de change non totalement éliminés en consolidation ; ce risque peut alors être documenté comme risque particulier affectant le résultat.

**Implications pratiques**: La documentation de couverture doit viser spécifiquement le risque de change de la créance reconnue dans une relation de couverture de juste valeur.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende n’est plus un flux intragroupe futur hautement probable : il est déjà reconnu en créance. Le sujet posé porte donc sur le risque de change d’un actif monétaire reconnu, ce qui correspond à une exposition de juste valeur sur l’élément comptabilisé, pas à une variabilité de flux futurs au sens visé ici.

**Implications pratiques**: Ce modèle n’est pas le plus adapté une fois la créance de dividende déjà comptabilisée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque décrit provient d’une créance de dividende intragroupe reconnue, non d’un investissement net dans une activité à l’étranger. IFRIC 16 réserve ce modèle au risque de change lié aux net assets d’une opération étrangère ; il ne doit pas être étendu par analogie à d’autres situations.

**Implications pratiques**: La problématique doit être traitée hors modèle de couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - 10
    >the hedged item can be an amount of net assets