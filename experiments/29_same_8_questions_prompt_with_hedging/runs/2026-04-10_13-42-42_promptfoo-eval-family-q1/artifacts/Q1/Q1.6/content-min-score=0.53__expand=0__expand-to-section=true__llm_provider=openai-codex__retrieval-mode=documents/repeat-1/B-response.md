# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Documentation consultée**
   - `ifric17`
   - `ifrs9`
   - `ifrs19`
   - `ias21`
   - `ias7`
   - `sic25`
   - `ifric16`
   - `ias37`

## Hypothèses
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance monétaire reconnue.
   - L’analyse est faite au niveau des comptes consolidés et porte sur le risque de change de cette créance.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais pas de façon générale. En comptes consolidés, seule l’exposition de change d’un élément monétaire intragroupe dont les écarts ne sont pas totalement éliminés à la consolidation peut être désignée; sinon, non. Le modèle de couverture de flux de trésorerie ne convient pas ici une fois la créance reconnue.

## Points Opérationnels

   - Le point décisif en consolidé est de savoir si l’écart de change sur la créance intragroupe subsiste après éliminations.
   - Si la créance est déjà reconnue, l’analyse pertinente n’est plus celle d’une transaction future hautement probable.
   - Si le poste relève de l’investissement net dans une activité à l’étranger, le traitement bascule vers le modèle de couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle de l’une des entités concernées.<br>- Les écarts de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | OUI SOUS CONDITIONS | - La créance monétaire intragroupe forme partie de l’investissement net dans une activité à l’étranger. |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle de l’une des entités concernées.
   - Les écarts de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est un élément monétaire reconnu. En comptes consolidés, IFRS 9 exclut en principe les éléments intragroupe, mais admet une exception pour le risque de change d’un élément monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés en consolidation. IAS 21 confirme qu’un tel écart de change peut subsister en résultat consolidé.

**Implications pratiques**: Possible uniquement pour le risque de change résiduel visible en consolidé; sinon la désignation n’est pas recevable.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise un dividende intragroupe pour lequel une créance a déjà été constatée. Or le modèle de cash flow hedge vise notamment une transaction future hautement probable; ici, l’exposition décrite n’est plus une transaction future mais un poste monétaire reconnu. L’approche n’est donc pas adaptée à cette situation précise.

**Implications pratiques**: Une fois la créance de dividende comptabilisée, il faut analyser l’éligibilité comme poste monétaire reconnu, pas comme flux futur.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance monétaire intragroupe forme partie de l’investissement net dans une activité à l’étranger.

**Raisonnment**:
Cette voie n’est ouverte que si la créance de dividende fait partie de l’investissement net dans une activité à l’étranger. Dans ce cas, IAS 21 prévoit une comptabilisation initiale des écarts de change en OCI en consolidé, et IFRIC 16 confirme qu’un instrument peut être désigné en couverture d’un investissement net. À défaut de lien avec un investissement net, cette approche ne s’applique pas.

**Implications pratiques**: À retenir seulement dans le cas particulier d’un poste assimilable à l’investissement net; sinon, ne pas utiliser ce modèle.

**Référence**:
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation
 - 45
    >if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income