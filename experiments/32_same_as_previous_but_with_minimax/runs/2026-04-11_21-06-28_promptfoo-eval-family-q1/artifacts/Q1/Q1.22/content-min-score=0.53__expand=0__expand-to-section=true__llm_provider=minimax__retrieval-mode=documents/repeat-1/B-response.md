# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Reformulation**:
>Whether foreign currency risk arising from intragroup dividend receivables in consolidated financial statements can be designated as a hedged item under hedge accounting rules

## Documentation
**Consultée**
   - IAS (`ias21`, `ias7`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric2`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs17`, `ifrs19`, `ifrs7`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias7`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric2`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs17`, `ifrs19`, `ifrs7`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic7`)

## Hypothèses
   - Les dividendes intragroupe sont reconnus en tant que créance dans les comptes consolidés du groupe.
   - Les entités concernées ont des devises fonctionnelles différentes, créant ainsi une exposition au risque de change.
   - L'exposition au risque de change affecte le résultat consolidé (elle n'est pas éliminée par consolidation).

## Recommandation

**OUI**

IFRS 9 §6.3.6 autorise explicitement la désignation du risque de change d'un élément monétaire intragroupe comme élément couvert dans les états financiers consolidés, lorsque l'exposition aux gains ou pertes de change n'est pas entièrement éliminée par consolidation et affecte le résultat consolidé. IFRIC 16 confirme l'éligibilité de cette couverture.

## Points Opérationnels

   - Documenter la relation de couverture conformément à IFRS 9 §6.4.1 dès la reconnaissance initiale de la créance de dividende.
   - Identifier l'instrument de couverture éligible (dérivé ou non-dérivé) et désigner le risque de change entre les devises fonctionnelles des entités concernées.
   - Évaluer l'efficacité de la relation de couverture à chaque date de reporting et appliquer le traitement approprié des gains ou pertes (OCI pour la partie efficace dans le cas d'une couverture d'investissement net).
   - Respecter les exigences de IAS 21 §45 lors des éliminations intragroupe pour，确保 la présentation correcte des effets de change.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture comptable du risque de change sur l'investissement net dans une opération étrangère | OUI | - L'exposition au change ne doit pas être entièrement éliminée par consolidation.<br>- Le risque de change doit affecter le résultat consolidé.<br>- Les conditions de désignation et de documentation d'IFRS 9 §6.4.1 doivent être satisfaites. |
| 2. Reconnaissance des différences de change en résultat | OUI SOUS CONDITIONS | - L'entreprise n'a pas désigné de relation de couverture, ou la désignation ne satisfait pas aux exigences d'IFRS 9. |
| 3. Élimination intragroupe avec reconnaissance du change | OUI | - Aucune condition supplémentaire — cette exigence s'applique toujours lors de l'élimination des soldes intragroupe. |

### 1. Couverture comptable du risque de change sur l'investissement net dans une opération étrangère

**Applicabilité**: OUI

**Conditions**:
   - L'exposition au change ne doit pas être entièrement éliminée par consolidation.
   - Le risque de change doit affecter le résultat consolidé.
   - Les conditions de désignation et de documentation d'IFRS 9 §6.4.1 doivent être satisfaites.

**Raisonnement**:
La créance de dividende intragroupe constitue un élément monétaire entre entités de devises fonctionnelles différentes. Selon IFRS 9 §6.3.6, ce type d'élément peut être désigné comme élément couvert si l'exposition au change n'est pas éliminée par consolidation et affecte le résultat consolidé. IFRIC 16 §9-12 confirme l'application de la comptabilité de couverture aux risques de change sur investissements nets.

**Implications pratiques**: L'entreprise peut désigner le risque de change entre la devise fonctionnelle de l'entité distributrice et celle de l'entité receveuse comme risque couvert, avec un instrument de couverture éligible.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation.
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency.

### 2. Reconnaissance des différences de change en résultat

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'entreprise n'a pas désigné de relation de couverture, ou la désignation ne satisfait pas aux exigences d'IFRS 9.

**Raisonnement**:
IAS 21 §28 exige que les différences de change sur les éléments monétaires soient reconnues en résultat dans la période où elles surviennent. Cette approche s'applique par défaut si la comptabilité de couverture n'est pas élue ou si les conditions de désignation ne sont pas satisfaites.

**Implications pratiques**: Les écarts de change sur la créance de dividende sont reconnus immédiatement en résultat net du période, sans effets compensatoires via le réserve de couverture.

**Référence**:
 - IAS 21 28

    >Exchange differences arising on the settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition during the period or in previous financial statements shall be recognised in profit or loss in the period in which they arise.

### 3. Élimination intragroupe avec reconnaissance du change

**Applicabilité**: OUI

**Conditions**:
   - Aucune condition supplémentaire — cette exigence s'applique toujours lors de l'élimination des soldes intragroupe.

**Raisonnement**:
IAS 21 §45 établit que les actifs et passifs monétaires intragroupe ne peuvent être éliminés sans montrer les effets des fluctuations de change dans les états financiers consolidés. Cela garantit que le résultat de change lié aux créances de dividendes intragroupe est présenté, que la comptabilité de couverture soit appliquée ou non.

**Implications pratiques**: Même en l'absence de désignation de couverture, les éliminations de consolidation doivent permettre la reconnaissance单独的 écarts de change sur les créances intragroupe.

**Référence**:
 - IAS 21 45

    >an intragroup monetary asset (or liability)... cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements.