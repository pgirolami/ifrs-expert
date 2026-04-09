# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Documentation consultée**
   - `ias32`
   - `ifric2`
   - `ifrs19`
   - `ifrs7`
   - `ifric17`
   - `ifrs9`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ias24`
   - `ifric16`
   - `ifric19`
   - `sic29`
   - `ifric21`
   - `ps1`
   - `ias37`

## Hypothèses
   - La question vise les états financiers consolidés et une créance de dividende intragroupe libellée en devise, générant une exposition de change.
   - La créance correspond à un poste monétaire intragroupe reconnu en consolidation.
   - L’analyse porte uniquement sur la possibilité de désigner cette exposition comme élément couvert au sens d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si l’exposition de change sur cette créance intragroupe n’est pas totalement éliminée en consolidation et affecte le résultat consolidé. Dans ce cas, elle peut être désignée comme élément couvert, en pratique au titre d’une couverture de juste valeur ou de flux de trésorerie, mais pas comme couverture d’un investissement net.

## Points Opérationnels

   - Le point décisif est de vérifier si, dans les comptes consolidés, les écarts de change sur la créance de dividende intragroupe affectent bien le résultat consolidé.
   - Si l’exposition de change est totalement éliminée en consolidation, la désignation comme élément couvert n’est pas possible.
   - La documentation initiale de couverture doit identifier explicitement le risque de change couvert et démontrer que l’élément couvert est admissible au niveau consolidé.
   - La qualification pertinente ici n’est pas la couverture d’investissement net, sauf si l’élément couvert était l’investissement net lui-même et non la créance de dividende.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende constitue un poste monétaire intragroupe<br>- les écarts de change correspondants ne sont pas totalement éliminés en consolidation<br>- le risque couvert est le risque de change affectant le résultat consolidé |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - la créance de dividende est un poste monétaire intragroupe reconnu<br>- l’exposition de change entraîne une variabilité des flux affectant le résultat consolidé<br>- les écarts de change ne sont pas totalement éliminés en consolidation |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende constitue un poste monétaire intragroupe
   - les écarts de change correspondants ne sont pas totalement éliminés en consolidation
   - le risque couvert est le risque de change affectant le résultat consolidé

**Raisonnment**:
La créance de dividende est supposée être un actif reconnu ; IFRS 9 permet une couverture de juste valeur d’un actif reconnu pour un risque particulier. En consolidation, un poste monétaire intragroupe peut être un élément couvert pour le risque de change si les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé.

**Implications pratiques**: Possible seulement si la documentation de couverture vise l’exposition de change résiduelle au niveau consolidé.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un poste monétaire intragroupe reconnu
   - l’exposition de change entraîne une variabilité des flux affectant le résultat consolidé
   - les écarts de change ne sont pas totalement éliminés en consolidation

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie d’un actif reconnu ou d’une transaction prévue. Pour cette créance de dividende intragroupe déjà reconnue, l’applicabilité reste conditionnée au fait que l’exposition de change sur le poste monétaire intragroupe ne soit pas totalement éliminée en consolidation et affecte le résultat consolidé.

**Implications pratiques**: La relation doit être documentée comme couverture du risque de change sur les flux liés à l’encaissement de la créance.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite porte sur une créance de dividende intragroupe reconnue, pas sur un investissement net dans une activité à l’étranger. IFRIC 16 réserve ce modèle au risque de change provenant d’un investissement net en activité étrangère ; une créance de dividende n’est pas cet élément.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour couvrir la créance de dividende elle-même.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.