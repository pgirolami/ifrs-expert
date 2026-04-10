# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs19`
   - `ias32`
   - `ifric17`
   - `ifrs17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ifrs9`
   - `ifric19`
   - `ias37`
   - `ifric16`

## Hypothèses
   - Le dividende intragroupe est libellé dans une devise différente de la devise fonctionnelle d’au moins une des entités concernées.
   - Le dividende a déjà été comptabilisé en créance/dette à la date d’analyse ; il ne s’agit donc plus d’un dividende seulement prévu.
   - La réponse est donnée au niveau des comptes consolidés IFRS, en se limitant à la couverture du risque de change.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente en consolidation est la couverture d’un poste monétaire intragroupe déjà reconnu, donc la fair value hedge, sous réserve que le risque de change affecte le résultat consolidé. La cash flow hedge ne vise pas un dividende déjà comptabilisé, et la net investment hedge ne couvre pas ce dividende reconnu en tant que tel.

## Points Opérationnels

   - Le point décisif est le niveau de reporting : en comptes consolidés, les postes intragroupe sont exclus sauf exception spécifique pour le risque de change sur un poste monétaire intragroupe.
   - Le timing est déterminant : une fois le dividende comptabilisé en créance, l’analyse ne relève plus d’une transaction future hautement probable.
   - Il faut vérifier si les écarts de change sur la créance/dette de dividende traversent bien le résultat consolidé, faute de quoi la base de désignation en couverture disparaît.
   - La documentation doit cibler strictement la composante change du poste reconnu et non le dividende intragroupe en général.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende constitue un poste monétaire intragroupe.<br>- Le risque de change sur ce poste affecte le résultat consolidé et n’est pas intégralement éliminé en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende constitue un poste monétaire intragroupe.
   - Le risque de change sur ce poste affecte le résultat consolidé et n’est pas intégralement éliminé en consolidation.

**Raisonnment**:
Le dividende intragroupe a déjà été comptabilisé en créance : il s’agit donc d’un poste reconnu, ce qui correspond au modèle de couverture d’un actif ou passif comptabilisé. En consolidation, un poste intragroupe n’est en principe pas éligible, sauf pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés et affectent le résultat consolidé.

**Implications pratiques**: La documentation de couverture peut viser le risque de change du dividende intragroupe reconnu, si ce risque subsiste en résultat consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise une transaction future prévue. Or, dans votre cas, le dividende intragroupe est déjà comptabilisé en créance, donc l’exposition n’est plus un flux futur seulement anticipé mais un poste reconnu. La base IFRS pour une forecast intragroup transaction ne correspond donc pas aux faits décrits.

**Implications pratiques**: Cette documentation ne convient pas pour un dividende déjà inscrit en créance dans les comptes.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... forecast transaction
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
En consolidation, la couverture d’investissement net vise le risque de change d’une participation nette dans une activité à l’étranger. Ici, la question porte sur un dividende intragroupe déjà comptabilisé en créance ; ce poste reconnu est distinct de l’investissement net lui-même. Cette approche ne couvre donc pas, en tant que telle, la partie change de ce dividende reconnu.

**Implications pratiques**: La documentation de net investment hedge n’est pas la réponse adaptée pour couvrir le change du dividende intragroupe déjà comptabilisé.

**Référence**:
 - 6.3.1
    >a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation