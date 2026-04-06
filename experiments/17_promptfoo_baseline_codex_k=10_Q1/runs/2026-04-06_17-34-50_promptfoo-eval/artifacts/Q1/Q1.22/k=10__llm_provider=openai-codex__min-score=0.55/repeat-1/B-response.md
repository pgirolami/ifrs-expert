# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les comptes consolidés sous IFRS 9.
   - La créance/dette de dividende intragroupe est libellée dans une devise générant un risque de change sur un poste monétaire.
   - Le sujet porte sur l'éligibilité de ce risque de change à la comptabilité de couverture, et non sur une simple couverture économique sans hedge accounting.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance/dette de dividende intragroupe constitue un poste monétaire intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Dans ce cas, le modèle pertinent est la couverture de juste valeur; les modèles de cash flow hedge et de net investment hedge ne correspondent pas à cette situation.

## Points Opérationnels

   - Le point de départ pratique est la date à laquelle le dividende intragroupe est constaté en créance/dette: avant cela, l'analyse n'est pas celle d'un poste monétaire reconnu.
   - En consolidation, il faut vérifier explicitement si les écarts de change sur cette créance/dette sont ou non totalement éliminés.
   - Si cette condition n'est pas satisfaite, aucune documentation de couverture IFRS 9 n'est possible sur cette composante de change dans la situation décrite.
   - Si la couverture est documentée, elle doit être calibrée sur le risque de change qui affecte le résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un poste monétaire intragroupe.<br>- Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation.<br>- Le risque couvert est bien le risque de change affectant le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un poste monétaire intragroupe.
   - Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation.
   - Le risque couvert est bien le risque de change affectant le résultat consolidé.

**Raisonnment**:
Dans la situation décrite, la créance de dividende reconnue devient un poste monétaire intragroupe exposé au change. IFRS 9 admet, en consolidation, qu'un poste monétaire intragroupe puisse être un élément couvert pour son risque de change si les écarts de change ne sont pas totalement éliminés en consolidation. La documentation d'une couverture est donc envisageable sur cette composante de risque dans ce cas précis.

**Implications pratiques**: La documentation doit viser le risque de change du poste monétaire intragroupe reconnu, une fois le dividende constaté en créance/dette.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le dividende a déjà été reconnu en créance/dette intragroupe: il ne s'agit plus d'une transaction future hautement probable mais d'un poste monétaire existant. Le risque décrit porte sur la réévaluation de change d'un montant fixé, non sur une variabilité de flux futurs au sens du cash flow hedge. Cette voie ne correspond donc pas à cette situation.

**Implications pratiques**: Une documentation en cash flow hedge ne serait pas alignée avec le fait que l'exposition existe déjà sous forme de créance/dette reconnue.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation porte sur une créance de dividende intragroupe reconnue, et non sur le risque de change attaché à un investissement net dans une activité étrangère. Le modèle IFRS 9 / IFRIC 16 vise les net assets d'une activité étrangère, pas un dividende intragroupe à recevoir ou à payer. Ce traitement n'est donc pas applicable ici.

**Implications pratiques**: Il ne faut pas documenter ce risque comme une couverture d'investissement net.

**Référence**:
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21