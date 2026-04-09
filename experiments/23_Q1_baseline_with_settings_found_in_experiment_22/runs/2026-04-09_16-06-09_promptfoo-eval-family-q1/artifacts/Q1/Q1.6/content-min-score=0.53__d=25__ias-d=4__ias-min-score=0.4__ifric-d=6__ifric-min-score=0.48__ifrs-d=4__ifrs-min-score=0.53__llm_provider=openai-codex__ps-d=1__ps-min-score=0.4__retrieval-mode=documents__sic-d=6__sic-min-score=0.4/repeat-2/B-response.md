# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance monétaire en devise avant son règlement.
   - La question est analysée dans les comptes consolidés établis selon les IFRS.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais en pratique seulement via une désignation de couverture de juste valeur du risque de change d’une créance intragroupe monétaire, si ce risque génère des écarts de change non totalement éliminés en consolidation. Une couverture de flux de trésorerie n’est pas adaptée ici, et une couverture d’investissement net ne l’est pas sauf si l’item fait partie du net investment.

## Points Opérationnels

   - Le point clé est de qualifier la créance de dividende comme poste monétaire intragroupe en devise et d’analyser si les monnaies fonctionnelles différentes créent un écart de change non éliminé en consolidation.
   - Si une couverture est envisagée, la documentation IFRS 9 doit être mise en place dès l’origine de la relation de couverture avec identification précise du risque de change couvert.
   - En l’absence de relation de couverture qualifiante, le traitement par défaut reste IAS 21 avec reconnaissance des écarts de change en résultat consolidé, sauf cas de net investment.
   - Le fait que le poste provienne d’un dividende intragroupe n’ouvre pas en soi un régime spécial de couverture ; l’analyse dépend de la nature monétaire du receivable et de son effet en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe en devise.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation, typiquement parce que les entités ont des monnaies fonctionnelles différentes.<br>- La relation de couverture satisfait aux conditions formelles de désignation et d’efficacité d’IFRS 9. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, il existe déjà une créance intragroupe reconnue. Le risque visé porte sur la variation de change d’un poste monétaire existant, non sur la variabilité de flux d’un élément futur hautement probable. Le modèle de cash flow hedge ne correspond donc pas au fait générateur décrit.

**Implications pratiques**: La variation de change sur la créance ne doit pas être désignée en cash flow hedge dans ce cas.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe en devise.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation, typiquement parce que les entités ont des monnaies fonctionnelles différentes.
   - La relation de couverture satisfait aux conditions formelles de désignation et d’efficacité d’IFRS 9.

**Raisonnment**:
La créance de dividende en devise est un poste monétaire reconnu. En comptes consolidés, IFRS 9 permet, par exception, de désigner le risque de change d’un poste monétaire intragroupe comme élément couvert si les écarts de change ne sont pas totalement éliminés en consolidation. Cela correspond précisément à une exposition sur un actif reconnu pouvant affecter le résultat.

**Implications pratiques**: Si ces conditions sont remplies, la désignation en fair value hedge du risque de change est envisageable en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit est une créance de dividende constatée, donc un montant destiné à être réglé, et non un poste faisant partie de l’investissement net dans une activité étrangère. La couverture d’investissement net vise l’exposition de conversion sur les net assets d’une foreign operation, pas un dividende intragroupe à recevoir.

**Implications pratiques**: Sauf démonstration très spécifique qu’il s’agit d’un élément du net investment, cette voie n’est pas la bonne pour un dividende intragroupe à recevoir.

**Référence**:
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets
 - 32
    >a monetary item that forms part of a reporting entity’s net investment in a foreign operation

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de désignation de couverture éligible, IAS 21 s’applique à la créance monétaire en devise. En consolidation, les écarts de change sur un poste monétaire intragroupe ne sont pas nécessairement éliminés et sont reconnus en résultat, sauf cas de net investment. C’est donc le traitement de base dans cette situation.

**Implications pratiques**: Sans hedge accounting valide, la variation de change sur la créance intragroupe est comptabilisée selon IAS 21, en principe en résultat consolidé.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items ... shall be recognised in profit or loss
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 32
    >shall be recognised initially in other comprehensive income