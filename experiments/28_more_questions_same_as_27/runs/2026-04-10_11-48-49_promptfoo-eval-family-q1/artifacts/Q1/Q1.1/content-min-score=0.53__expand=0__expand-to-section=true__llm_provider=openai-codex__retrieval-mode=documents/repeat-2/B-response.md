# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - La question vise les comptes consolidés IFRS et la documentation de couverture au titre d’IFRS 9 sur le risque de change lié à un dividende intragroupe comptabilisé en créance.
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance au moment où l’on analyse la possibilité de documenter la couverture.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie la plus pertinente est la couverture de juste valeur, mais seulement si la créance intragroupe est un poste monétaire dont l’écart de change n’est pas totalement éliminé en consolidation. La couverture de flux de trésorerie ne correspond pas à une créance déjà comptabilisée, et la couverture d’investissement net ne s’applique que si la relation documentée vise l’investissement net dans une activité à l’étranger, pas le dividende en tant que tel.

## Points Opérationnels

   - Le point décisif en consolidation est de vérifier si la créance de dividende intragroupe est un poste monétaire dont les écarts de change subsistent en résultat consolidé.
   - Si la créance est déjà reconnue, la logique IFRS oriente d’abord vers une couverture de juste valeur plutôt que vers une couverture de flux de trésorerie.
   - La couverture d’investissement net suppose une documentation spécifique au niveau groupe ; elle ne doit pas être confondue avec la couverture d’une créance intragroupe isolée.
   - La documentation doit être appréciée au niveau de reporting consolidé, car IFRS 9 limite en principe les éléments couverts aux expositions avec des tiers, sauf exceptions de change intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe.<br>- Le risque de change sur cette créance affecte le résultat consolidé, car les écarts de change ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | OUI SOUS CONDITIONS | - La documentation de couverture vise l’investissement net dans une activité à l’étranger, et non la seule créance de dividende intragroupe.<br>- L’instrument de couverture est valablement désigné dans une relation de couverture d’investissement net au niveau du groupe. |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe.
   - Le risque de change sur cette créance affecte le résultat consolidé, car les écarts de change ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Ici, l’élément visé est une créance déjà comptabilisée. IFRS 9 admet comme élément couvert un actif reconnu, et en consolidation un poste monétaire intragroupe peut être couvert pour le risque de change si les écarts de change ne sont pas entièrement éliminés. Cela peut donc convenir à une créance de dividende intragroupe uniquement dans ce cas précis.

**Implications pratiques**: La documentation doit viser le risque de change de la créance reconnue, et non le dividende intragroupe en tant que transaction purement interne sans effet P&L consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, le dividende intragroupe est déjà comptabilisé en créance : on n’est donc plus face à une transaction future. Or ce modèle vise des flux futurs variables ou des transactions prévues hautement probables. Pour cette créance déjà reconnue, cette documentation ne correspond pas au fait générateur décrit.

**Implications pratiques**: Ce modèle ne permet pas de documenter, dans l’état actuel des faits, le risque de change de la créance déjà enregistrée.

**Référence**:
 - 6.3.1
    >The hedged item can be ... a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La documentation de couverture vise l’investissement net dans une activité à l’étranger, et non la seule créance de dividende intragroupe.
   - L’instrument de couverture est valablement désigné dans une relation de couverture d’investissement net au niveau du groupe.

**Raisonnment**:
Ce modèle existe bien en comptes consolidés, mais il ne couvre pas en soi une créance de dividende intragroupe. Il n’est pertinent que si la relation documentée porte sur l’investissement net dans une activité à l’étranger, avec un instrument de couverture désigné comme tel. Donc, pour le dividende intragroupe lui-même, ce n’est pas la réponse naturelle sauf si l’objectif de couverture est en réalité l’investissement net.

**Implications pratiques**: Si votre objectif est de couvrir le rapatriement du dividende, ce modèle n’est pertinent que rattaché à une stratégie de couverture de l’investissement net, pas à la créance isolée.

**Référence**:
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation
 - 15
    >the total effective portion of the change is included in other comprehensive income