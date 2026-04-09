# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance monétaire reconnue dans les états financiers consolidés.
   - L’analyse est menée au niveau des comptes consolidés, et non des comptes individuels ou séparés.
   - La couverture envisagée porte sur le risque de change au sens d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, si la créance de dividende intragroupe est un poste monétaire exposant effectivement le groupe à des écarts de change non totalement éliminés. Dans ce cas, la voie pertinente est la couverture d’un poste reconnu, et non une couverture de flux futurs ni une couverture d’investissement net.

## Points Opérationnels

   - La documentation doit être appréciée au niveau consolidé, car IFRS 9 limite en principe les éléments couverts aux expositions avec des tiers externes, sous l’exception spécifique des postes monétaires intragroupe en devises.
   - Le point décisif est de démontrer que la créance de dividende expose bien le groupe à des écarts de change non totalement éliminés en consolidation.
   - Si la créance est déjà reconnue, la piste opérationnelle pertinente est celle d’une couverture d’un poste reconnu; la qualification en cash flow hedge devient inadaptée.
   - Il faut aligner la documentation de couverture avec le traitement IAS 21 des écarts de change de la créance dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation du change selon IAS 21 | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire.<br>- Elle génère des écarts de change non totalement éliminés en consolidation. |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est reconnue dans les comptes consolidés.<br>- Le risque de change sur cette créance n’est pas totalement éliminé en consolidation. |
| 3. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 4. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire.
   - Elle génère des écarts de change non totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, IAS 21 confirme qu’un actif monétaire intragroupe ne peut pas être éliminé sans faire apparaître les effets de change en consolidation. Donc, si la créance de dividende est libellée dans une devise créant une exposition de change entre entités de devises fonctionnelles différentes, un risque de change existe bien au niveau consolidé.

**Implications pratiques**: Il faut d’abord établir que la créance de dividende crée une exposition de change reconnue en résultat ou, le cas échéant, en OCI selon IAS 21.

**Référence**:
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated
 - 45
    >such an exchange difference is recognised in profit or loss

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est reconnue dans les comptes consolidés.
   - Le risque de change sur cette créance n’est pas totalement éliminé en consolidation.

**Raisonnment**:
Cette approche est recevable ici car IFRS 9 permet de désigner un actif reconnu comme élément couvert. En consolidation, l’exception d’IFRS 9 vise précisément le risque de change d’un poste monétaire intragroupe lorsque les gains ou pertes de change ne sont pas totalement éliminés selon IAS 21, ce qui correspond à une créance de dividende reconnue et exposée au change.

**Implications pratiques**: La documentation de couverture peut viser la créance reconnue comme élément couvert du risque de change en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.6
    >not fully eliminated on consolidation in accordance with IAS 21

### 3. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche ne correspond pas aux faits décrits, car la question porte sur des dividendes intragroupe ayant déjà donné lieu à la reconnaissance d’une créance en consolidation. IFRS 9 réserve ici la logique de cash flow hedge aux transactions prévues hautement probables, y compris certains flux intragroupe futurs, et non à une créance déjà comptabilisée.

**Implications pratiques**: Une fois la créance de dividende reconnue, l’analyse se déplace vers la couverture d’un poste monétaire existant, pas d’un flux futur.

**Référence**:
 - 6.3.1
    >a forecast transaction
 - 6.3.3
    >that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 4. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche n’est pas la bonne au vu des faits, car le risque visé porte sur une créance de dividende intragroupe reconnue, non sur l’exposition de change attachée à un investissement net dans une activité à l’étranger. IFRIC 16 rattache cette couverture aux écarts entre la devise fonctionnelle de l’activité étrangère et celle du parent, avec accumulation en OCI jusqu’à la disposition.

**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme une couverture d’investissement net.

**Référence**:
 - 2
    >foreign currency risk arising from the net investment in a foreign operation
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 3
    >the gain or loss on the hedging instrument ... is recognised in other comprehensive income