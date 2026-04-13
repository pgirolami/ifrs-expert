# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Reformulation**:
>Whether foreign exchange risk on intercompany dividend receivables can qualify for hedge accounting in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias21`, `ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric16`, `ifric17`, `ifric2`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs7`, `ifrs12`)
   - SIC (`sic25`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric16`, `ifric17`, `ifric2`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs7`, `ifrs12`)
   - SIC (`sic25`, `sic7`)

## Hypothèses
   - L'entité qui se pose la question est une société mère préparant des états financiers consolidés
   - Les dividendes intragroupe sont enregistrés en créance à recevoir dans les comptes individuels des entités du groupe
   - Les entités émettrices et получатели dividendes ont des devises fonctionnelles différentes
   - La relation de couverture serait formellement documentée conformément aux exigences de l'IFRS 9

## Recommandation

**OUI SOUS CONDITIONS**

Le risque de change sur une créance de dividende intragroupe peut faire l'objet d'une couverture documentée au niveau consolidé, car l'IFRS 9 paragraphe 6.3.6 autorise explicitement les éléments monétaires intragroupe lorsque l'exposition au change n'est pas éliminée à la consolidation (IAS 21 paragraphe 45). Cependant, certaines conditions strictes doivent être satisfaites.

## Points Opérationnels

   - La désignation d'une couverture doit être effectuée dès la reconnaissance initiale de la créance de dividende ou à une date ultérieure допускается par l'IFRS 9
   - L'instrument de couverture peut être un dérivé (contrat forward, option) ou un élément non dérivé libellé en devise étrangère
   - Une documentation formelle incluant l'identification de l'élément couvert, de l'instrument de couverture, de la nature du risque et de la méthode d'évaluation de l'efficacité est requise
   - Le risque de change entre la devise fonctionnelle de la filiale et celle de la société mère (et non le risque de conversion vers la devise de présentation) peut être désigné comme risque couvert selon l'IFRIC 16 paragraphe 10
   - Si le même risque de change sur les mêmes actifs nets est déjà couvert par une autre entité du groupe (par exemple une couverture d'investissement net), une seule relation de couverture peut être reconnue dans les états financiers consolidés de la mère ultime (IFRIC 16 paragraphe 13)


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation de couverture pour les éléments monétaires intragroupe | OUI SOUS CONDITIONS | - Le dividende intragroupe doit être un élément monétaire (créance de montant fixe)<br>- L'exposition au change doit résulter de la différence entre devises fonctionnelles (non éliminée à la consolidation)<br>- La relation de couverture doit être formellement documentée conformément à l'IFRS 9 paragraphe 6.4.1<br>- Le risque désigné comme couvert doit être limité au risque de change entre devises fonctionnelles (et non le risque de conversion vers la devise de présentation) |
| 2. Comptabilisation des changes sans Accounting de couverture | OUI SOUS CONDITIONS | - Aucune relation de couverture n'est formellement désignée, ou les conditions de l'IFRS 9 ne sont pas satisfaites<br>- L'exposition au change sur la créance de dividende intragroupe subsiste |

### 1. Comptabilisation de couverture pour les éléments monétaires intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende intragroupe doit être un élément monétaire (créance de montant fixe)
   - L'exposition au change doit résulter de la différence entre devises fonctionnelles (non éliminée à la consolidation)
   - La relation de couverture doit être formellement documentée conformément à l'IFRS 9 paragraphe 6.4.1
   - Le risque désigné comme couvert doit être limité au risque de change entre devises fonctionnelles (et non le risque de conversion vers la devise de présentation)

**Raisonnement**:
Une créance de dividende intragroupe est un élément monétaire générant une exposition au risque de change entre devises fonctionnelles différentes. L'IAS 21 paragraphe 45 confirme que les éléments monétaires intragroupe ne peuvent être éliminés sans reconnaître les effets des fluctuations de change, créant ainsi une exposition qui n'est pas éliminée à la consolidation. L'IFRS 9 paragraphe 6.3.6 permet donc de désigner cette exposition comme élément couvert dans une relation de couverture.

**Implications pratiques**: L'entité peut désigner le risque de change sur la créance de dividende intragroupe comme élément couvert dans unAccounting de couverture (couverture de juste valeur ou de flux de trésorerie selon la nature de la créance).

**Référence**:
 - IFRS 9 6.3.6

    >as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item [...] may qualify as a hedged item in the consolidated financial statements
 - IAS 21 45

    >an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements

### 2. Comptabilisation des changes sans Accounting de couverture

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Aucune relation de couverture n'est formellement désignée, ou les conditions de l'IFRS 9 ne sont pas satisfaites
   - L'exposition au change sur la créance de dividende intragroupe subsiste

**Raisonnement**:
Cette approche constitue le traitement par défaut applicable lorsqu'une relation de couverture n'est pas désignée ou ne satisfait pas aux conditions de l'IFRS 9. Selon l'IAS 21 paragraphe 45, les différences de change sur les éléments monétaires intragroupe sont reconnues en résultat (ou en OCI en cas de cession de l'activité à l'étranger), sans application de l'Accounting de couverture.

**Implications pratiques**: Les écarts de change sur la créance de dividende intragroupe sont reconnus en résultat (ou OCI pour les opérations qualifying) selon les prescriptions de l'IAS 21, sans amortissement仪 instrument de couverture.

**Référence**:
 - IAS 21 45

    >in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income