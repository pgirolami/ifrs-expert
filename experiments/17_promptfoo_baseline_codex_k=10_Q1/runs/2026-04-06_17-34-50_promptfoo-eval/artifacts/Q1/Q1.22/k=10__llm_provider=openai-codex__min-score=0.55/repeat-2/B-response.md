# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les états financiers consolidés établis selon IFRS 9.
   - Le dividende intragroupe a déjà été comptabilisé en créance/dette entre sociétés du groupe.
   - Cette créance/dette est libellée dans une devise créant une exposition de change entre entités du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une couverture de juste valeur de la composante risque de change, si la créance/dette intragroupe est un poste monétaire dont les écarts de change ne sont pas totalement éliminés en consolidation. La couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas, en principe, à cette situation.

## Points Opérationnels

   - Le point clé est le moment où le dividende devient une créance/dette intragroupe reconnue : à ce stade, l’analyse se fait comme pour un poste monétaire reconnu.
   - En consolidation, il faut vérifier que les écarts de change sur cette créance/dette ne sont pas totalement éliminés ; sinon l’élément ne peut pas être désigné comme item couvert.
   - La documentation doit viser spécifiquement la composante risque de change et respecter les critères formels d’IFRS 9 pour une relation de couverture.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende doit constituer un poste monétaire intragroupe<br>- Le risque de change doit générer des gains ou pertes de change non totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende doit constituer un poste monétaire intragroupe
   - Le risque de change doit générer des gains ou pertes de change non totalement éliminés en consolidation

**Raisonnment**:
Dans cette situation, la créance de dividende intragroupe déjà reconnue est un actif reconnu, exposé au risque de change. IFRS 9 autorise une couverture de juste valeur d’un actif ou passif reconnu pour un risque particulier, et admet par exception qu’un poste monétaire intragroupe puisse être désigné en consolidation si les écarts de change ne sont pas totalement éliminés.

**Implications pratiques**: La documentation de couverture peut viser la composante risque de change de la créance/dette de dividende reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk or risks

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le dividende intragroupe est déjà reconnu en créance/dette. Le sujet n’est donc plus une transaction future hautement probable ni une variabilité de flux futurs, mais une exposition de change sur un poste monétaire reconnu. Le modèle de cash flow hedge ne correspond pas au fait décrit.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une couverture de flux de trésorerie pour cette créance déjà comptabilisée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La problématique décrite porte sur une créance de dividende intragroupe reconnue, non sur le risque de change afférent à un investissement net dans une activité à l’étranger. IFRIC 16 vise la couverture du risque de change attaché aux net assets d’une opération étrangère, ce qui est distinct d’un dividende intragroupe à recevoir.

**Implications pratiques**: Il ne faut pas documenter cette exposition comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets