# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs9`
   - `ifric16`

## Hypothèses
   - Le dividende intragroupe a déjà été comptabilisé en créance avant consolidation.
   - La question vise l'application de la comptabilité de couverture IFRS 9 dans les comptes consolidés, uniquement sur le risque de change.
   - La créance de dividende est une créance intragroupe entre entités dont les monnaies fonctionnelles peuvent être différentes.

## Recommandation

**OUI SOUS CONDITIONS**

En comptes consolidés, la voie la plus défendable est la couverture de juste valeur, mais seulement si la créance intragroupe constitue un poste monétaire dont l'écart de change n'est pas totalement éliminé en consolidation. La couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas, en l'état des faits, à une créance de dividende déjà reconnue.

## Points Opérationnels

   - Le point clé en consolidation est l'éligibilité de la créance intragroupe au regard de l'exception des postes monétaires intragroupe de l'IFRS 9 6.3.6.
   - La documentation doit être formalisée à l'origine de la relation de couverture et identifier l'instrument, l'élément couvert, le risque de change couvert et le test d'efficacité.
   - Si la créance est éliminée sans impact résiduel en résultat consolidé, la couverture ne tient pas en consolidation.
   - Si le dividende n'était pas encore reconnu mais seulement prévu, l'analyse pourrait être différente; avec une créance déjà comptabilisée, la piste à examiner est la juste valeur.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation<br>- Le risque de change de cette créance peut affecter le résultat consolidé |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation
   - Le risque de change de cette créance peut affecter le résultat consolidé

**Raisonnment**:
Ici, le dividende est déjà comptabilisé en créance, donc il s'agit d'un élément reconnu, ce qui correspond au modèle de juste valeur. En consolidation, un élément intragroupe n'est éligible que s'il entre dans l'exception des postes monétaires intragroupe générant un risque de change non totalement éliminé et affectant le résultat consolidé.

**Implications pratiques**: Si ces conditions sont remplies, la documentation peut viser le risque de change de la créance reconnue en couverture de juste valeur.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.5.8
    >the hedging gain or loss on the hedged item shall adjust the carrying amount

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende n'est plus une transaction future hautement probable : il a déjà été constaté en créance. Le cas décrit correspond donc mal au modèle de flux de trésorerie, que la norme illustre surtout pour des flux variables futurs ou des transactions prévues.

**Implications pratiques**: La documentation en cash flow hedge ne paraît pas adaptée à une créance de dividende déjà reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external

### 3. Couverture d'un investissement net à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque couvert dans ce modèle porte sur un investissement net dans une activité à l'étranger, c'est-à-dire un montant de net assets, pas sur une créance de dividende intragroupe. Une créance de dividende traduit au contraire une intention de règlement, et non la couverture d'un investissement net maintenu.

**Implications pratiques**: Cette documentation ne convient pas à la partie change d'une créance de dividende intragroupe.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric16.11
    >The hedged item can be an amount of net assets
 - ifric16.10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency