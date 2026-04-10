# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs12`
   - `ifrs19`
   - `ifrs7`
   - `ifric17`
   - `ifric16`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ias37`
   - `sic7`

## Hypothèses
   - La question vise les comptes consolidés établis selon les IFRS.
   - Le dividende intragroupe est libellé dans une devise autre que la monnaie fonctionnelle d’au moins une des entités concernées.
   - La mise en dividende a déjà créé une créance intragroupe monétaire à recevoir et une dette correspondante avant élimination de consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d’une créance de dividende intragroupe peut être désigné dans une relation de couverture si cette créance est un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas précis, la voie pertinente est la couverture de juste valeur ; à défaut, IAS 21 s’applique en traitement de base.

## Points Opérationnels

   - Le point décisif est le niveau de reporting : en comptes consolidés, un poste intragroupe n’est éligible que via l’exception IFRS 9 relative au risque de change des postes monétaires intragroupe.
   - Le facteur de timing est essentiel : une fois le dividende déclaré et la créance comptabilisée, on analyse un poste reconnu, non une transaction future hautement probable.
   - Il faut établir que les entités concernées ont des monnaies fonctionnelles différentes et que les écarts de change affectent bien le résultat consolidé.
   - La documentation de couverture doit être concomitante à la désignation et viser explicitement cette exposition de change intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un poste monétaire intragroupe en devise.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.<br>- La relation de couverture doit être formellement documentée. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation de change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un poste monétaire intragroupe en devise.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.
   - La relation de couverture doit être formellement documentée.

**Raisonnment**:
Ici, la créance de dividende déjà comptabilisée est un actif reconnu, donc un candidat possible comme élément couvert. En consolidation, les éléments intragroupe sont en principe exclus, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Cette exception vise précisément la situation d’une créance/dette intragroupe en devises entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: La désignation est envisageable en consolidation sur la créance de dividende reconnue, sous réserve de démontrer l’exposition de change résiduelle au niveau du groupe.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise notamment une transaction future hautement probable. Or, dans les faits posés, le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance à recevoir : l’exposition n’est donc plus une transaction future, mais un poste monétaire reconnu. La question porte sur cette créance existante, pas sur un dividende futur avant déclaration.

**Implications pratiques**: La couverture de flux de trésorerie n’est pas la qualification adaptée une fois la créance de dividende déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise le risque de change d’un dividende intragroupe devenu une créance à recevoir, donc un poste monétaire de règlement, et non une exposition de change sur un investissement net dans une activité à l’étranger. Le modèle de couverture d’investissement net traite les différences de conversion liées aux net assets d’une activité étrangère, avec recyclage à la cession, ce qui ne correspond pas à la créance de dividende décrite.

**Implications pratiques**: Le modèle de couverture d’investissement net n’est pas approprié pour une créance de dividende intragroupe déclarée.

**Référence**:
 - 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation

### 4. Comptabilisation de change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut d’une couverture qualifiante, le traitement de base est IAS 21. Une créance de dividende intragroupe en devise est un poste monétaire ; les écarts de change sont comptabilisés en résultat, et, en consolidation, les écarts sur postes monétaires intragroupe entre entités à monnaies fonctionnelles différentes ne disparaissent pas entièrement. Ce traitement constitue donc le socle comptable de la situation décrite.

**Implications pratiques**: Sans relation de couverture admissible, les écarts de change sur la créance de dividende sont constatés en résultat consolidé selon IAS 21.

**Référence**:
 - 28
    >Exchange differences ... on translating monetary items ... shall be recognised in profit or loss
 - 45
    >such an exchange difference is recognised in profit or loss
 - 5
    >This Standard does not apply to hedge accounting for foreign currency items