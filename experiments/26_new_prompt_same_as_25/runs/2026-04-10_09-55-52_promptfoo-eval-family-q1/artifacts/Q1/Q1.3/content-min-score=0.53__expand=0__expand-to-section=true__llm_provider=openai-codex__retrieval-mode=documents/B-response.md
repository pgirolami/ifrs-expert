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
   - La question vise les comptes consolidés.
   - Le dividende intragroupe est libellé en devise étrangère.
   - Le cas principal visé est celui où le dividende a déjà donné lieu à la comptabilisation d’une créance intragroupe à recevoir.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, le risque de change d’une créance intragroupe de dividende peut être désigné seulement si cette créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Si la créance relève d’un investissement net dans une activité à l’étranger, le traitement bascule vers IAS 21 / couverture d’investissement net, et non vers une couverture classique de la créance.

## Points Opérationnels

   - Le point décisif est le niveau consolidé : la règle générale exclut les éléments intragroupe, sauf l’exception ciblée des éléments monétaires intragroupe en devise.
   - Le moment de l’analyse est essentiel : avant comptabilisation d’une créance, on serait dans la logique d’une transaction future; après comptabilisation, on est sur un poste monétaire reconnu.
   - Il faut vérifier si la créance de dividende affecte le résultat consolidé ou relève de l’investissement net, car cela change le modèle de couverture pertinent.
   - La documentation de couverture doit être concomitante à la désignation et cohérente avec le risque effectivement conservé en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire.<br>- Les sociétés liées doivent avoir des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance ne doivent pas être totalement éliminés en consolidation.<br>- La relation de couverture doit être documentée. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | OUI SOUS CONDITIONS | - La créance doit former partie de l’investissement net dans une activité à l’étranger. |
| 4. Comptabilisation IAS 21 du change | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire.
   - Les sociétés liées doivent avoir des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance ne doivent pas être totalement éliminés en consolidation.
   - La relation de couverture doit être documentée.

**Raisonnment**:
La créance de dividende comptabilisée est, dans la situation décrite, un actif reconnu pouvant en principe être désigné comme élément couvert. En consolidation, un élément intragroupe n’est toutefois éligible que s’il entre dans l’exception des éléments monétaires intragroupe dont les écarts de change ne sont pas totalement éliminés; c’est le cas lorsque les entités ont des monnaies fonctionnelles différentes et que le risque de change affecte le résultat consolidé.

**Implications pratiques**: Une désignation est envisageable pour la créance reconnue, mais seulement dans le périmètre étroit de l’exception IFRS 9 sur les éléments monétaires intragroupe en devise.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction intragroupe future hautement probable. Or la question porte sur un dividende ayant déjà donné lieu à la comptabilisation d’une créance à recevoir; l’exposition n’est donc plus un flux futur non reconnu mais un poste monétaire déjà comptabilisé.

**Implications pratiques**: Dans les faits décrits, la couverture de flux de trésorerie n’est pas le bon modèle, car le dividende n’est plus à l’état de transaction prévue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit former partie de l’investissement net dans une activité à l’étranger.

**Raisonnment**:
Cette approche n’est pertinente que si la créance intragroupe de dividende fait en substance partie de l’investissement net dans une activité à l’étranger. Dans ce cas, les écarts de change sont reconnus en autres éléments du résultat global en consolidation; sinon, un dividende à recevoir ordinaire ne relève pas d’une couverture d’investissement net.

**Implications pratiques**: Si la créance est assimilable à l’investissement net, il faut analyser une couverture d’investissement net plutôt qu’une couverture classique de la créance.

**Référence**:
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation

### 4. Comptabilisation IAS 21 du change
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut ou en amont de la couverture, IAS 21 fournit le traitement de base. Une créance intragroupe monétaire en devise génère des écarts de change reconnus en résultat, sauf si elle fait partie de l’investissement net dans une activité à l’étranger, auquel cas l’écart est porté initialement en OCI en consolidation.

**Implications pratiques**: Il faut d’abord qualifier la créance au regard d’IAS 21 pour déterminer si le risque affecte le résultat consolidé ou l’OCI.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items or on translating monetary items ... shall be recognised in profit or loss
 - 32
    >shall be recognised initially in other comprehensive income
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations in the consolidated financial statements