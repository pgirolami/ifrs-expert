# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ias21`
   - `ifrs9`
   - `ias32`
   - `ifric17`
   - `ifrs19`
   - `ifrs7`
   - `ifrs12`
   - `ifric2`
   - `ifric16`
   - `ias7`
   - `sic25`
   - `ps1`
   - `ifric14`

## Hypothèses
   - La question vise des comptes consolidés IFRS, puisque la créance de dividende est indiquée comme reconnue dans les comptes consolidés.
   - Le dividende intragroupe a déjà été déclaré de sorte qu’une créance monétaire existe à la date de documentation envisagée.
   - La créance et l’engagement corrélatif sont libellés dans une monnaie exposant le groupe à un risque de change non totalement éliminé en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe, si la créance de dividende déjà reconnue constitue dans les comptes consolidés un poste monétaire intragroupe exposant le groupe à un risque de change non totalement éliminé. Dans ce cas, la voie pertinente est la couverture de juste valeur; la couverture de flux de trésorerie ne vise pas ce fait générateur déjà reconnu, et la couverture d’investissement net répond à un autre risque.

## Points Opérationnels

   - Le point clé de recevabilité est le niveau de reporting: il faut démontrer l’existence d’une exposition de change résiduelle dans les comptes consolidés.
   - Le timing est déterminant: avant reconnaissance du dividende, la logique pourrait relever d’un flux futur; après reconnaissance de la créance, l’analyse bascule sur un poste monétaire reconnu.
   - La documentation doit être cohérente avec IAS 21: les écarts de change sur le poste monétaire intragroupe doivent être de ceux qui ne sont pas totalement éliminés en consolidation.
   - Si l’entité applique la comptabilité de couverture, elle doit aligner la désignation sur le bon objet couvert: créance reconnue, et non investissement net ni simple flux futur.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire reconnu dans les comptes consolidés<br>- Le risque de change sur cette créance n’est pas totalement éliminé en consolidation<br>- L’exposition concerne une contrepartie intragroupe ayant une monnaie fonctionnelle différente |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire reconnu dans les comptes consolidés
   - Le risque de change sur cette créance n’est pas totalement éliminé en consolidation
   - L’exposition concerne une contrepartie intragroupe ayant une monnaie fonctionnelle différente

**Raisonnment**:
Dans cette situation, l’élément visé est une créance déjà reconnue en consolidation. IFRS 9 admet comme élément couvert un actif ou passif reconnu, et IAS 21 précise qu’un actif monétaire intragroupe ne peut pas être éliminé sans laisser apparaître l’effet de change en consolidation si les monnaies fonctionnelles diffèrent. La documentation est donc recevable si la créance de dividende crée bien cette exposition résiduelle au niveau consolidé.

**Implications pratiques**: La documentation de couverture peut viser la créance reconnue en consolidation comme élément couvert de risque de change, sous réserve de démontrer l’exposition résiduelle au niveau groupe.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise des transactions prévues hautement probables. Or la question porte sur des dividendes intragroupe ayant déjà donné lieu à la reconnaissance d’une créance dans les comptes consolidés. Une fois la créance reconnue, le risque porte sur un poste monétaire existant, non sur un flux futur encore seulement prévu.

**Implications pratiques**: La documentation en cash flow hedge n’est pas adaptée au fait décrit, car le dividende n’est plus un flux futur simplement anticipé.

**Référence**:
 - 6.3.1
    >a forecast transaction
 - 6.3.3
    >that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net concerne le risque de change afférent aux actifs nets d’une opération étrangère. Ici, le risque visé porte sur une créance de dividende intragroupe déjà constatée, c’est-à-dire un poste monétaire distinct de l’investissement net lui-même. Le fait décrit ne correspond donc pas au modèle de net investment hedge.

**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme une couverture d’investissement net; ce modèle vise les actifs nets de l’opération étrangère.

**Référence**:
 - 6.3.1
    >a net investment in a foreign operation
 - 2
    >The item being hedged ... may be an amount of net assets
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency