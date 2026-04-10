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
   - L’analyse est effectuée au niveau des états financiers consolidés.
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance/dette monétaire intragroupe.
   - Le risque visé est un risque de change sur cette créance monétaire reconnue en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, la couverture est recevable si le dividende déclaré a créé un poste monétaire intragroupe exposé à des écarts de change non intégralement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; les modèles de cash flow hedge et de net investment hedge ne correspondent pas à ce fait précis.

## Points Opérationnels

   - Le point clé de timing est que le dividende est déjà déclaré et a créé une créance: l’exposition est donc un poste monétaire existant.
   - Au niveau consolidé, l’exception IFRS ne joue que si le risque de change sur le poste intragroupe subsiste parce que les monnaies fonctionnelles diffèrent.
   - La documentation doit être alignée sur le niveau de reporting pertinent, ici la consolidation, et non uniquement sur les comptes individuels.
   - Si l’exposition de change ne subsiste pas en consolidation, la désignation de couverture ne serait pas recevable pour ce poste.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance/dette intragroupe est un poste monétaire<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- le risque de change sur ce poste n’est pas intégralement éliminé en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance/dette intragroupe est un poste monétaire
   - les entités concernées ont des monnaies fonctionnelles différentes
   - le risque de change sur ce poste n’est pas intégralement éliminé en consolidation

**Raisonnment**:
Dans cette situation, le dividende intragroupe déclaré a déjà créé une créance monétaire reconnue en consolidation. IAS 21 précise que les écarts de change sur un poste monétaire intragroupe ne peuvent pas être éliminés sans apparaître dans les comptes consolidés, et IFRS 9 permet explicitement de désigner ce risque de change comme élément couvert si les gains/pertes ne sont pas totalement éliminés en consolidation.

**Implications pratiques**: La documentation de couverture doit viser la créance de dividende reconnue en consolidation comme exposition de change sur poste monétaire intragroupe.

**Référence**:
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated
 - 45
    >such an exchange difference is recognised in profit or loss
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le cas décrit ne porte pas sur une transaction future hautement probable, mais sur un dividende déjà déclaré ayant donné lieu à une créance reconnue. Le modèle de cash flow hedge vise notamment des transactions prévues; ici, l’exposition pertinente en consolidation est celle d’un poste monétaire existant, non celle d’un flux futur non encore comptabilisé.

**Implications pratiques**: Cette voie ne correspond pas au fait générateur déjà survenu et à la présence d’une créance comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise le risque de change sur un dividende intragroupe matérialisé par une créance, non le risque de change sur les actifs nets d’une activité étrangère. Le modèle de net investment hedge concerne l’investissement net dans une opération étrangère et les différences de conversion y afférentes, ce qui est distinct d’une créance de dividende intragroupe reconnue.

**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme une couverture d’investissement net.

**Référence**:
 - 2
    >foreign currency risk arising from the net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation.