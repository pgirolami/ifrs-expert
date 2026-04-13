# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Reformulation**:
>Eligibility of intragroup dividend receivable for designation as a hedged item in a hedge accounting relationship for foreign currency risk

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
   - La question porte sur la désignation d'une relation de couverture pour le risque de change d'une créance de dividende intragroupe comptabilisée dans les comptes consolidés.
   - Le contexte implique une exposition au risque de change découlant de la créance de dividende intragroupe elle-même, et non du dividende en tant que distribué entre parties externes.

## Recommandation

**NON**

La créance de dividende intragroupe est un actif financier intragroupe qui est éliminé en consolidation. Selon IFRS 9 paragraphes 6.3.1 et 6.3.5, un élément ne peut être désigné comme élément couvert que s'il implique une partie externe à l'entité présentant l'information. L'exception de IFRIC 16 paragraphe 6 relative aux postes monétaires intragroupe dont le risque de change n'est pas éliminé ne s'applique pas ici.

## Points Opérationnels

   - Aucune désignation de couverture n'est possible pour le risque de change lié à la créance de dividende intragroupe dans les états financiers consolidés.
   - Le risque de change associé au dividende intragroupe est éliminé lors du processus de consolidation car la créance et la dette correspondante s'annulent.
   - Si une entité souhaite gérer le risque de change lié aux dividendes intragroupe, elle devrait le faire au niveau de l'entité individuelle où l'exposition existe avant élimination.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture autorisée pour exposition de change intragroupe | NON | - L'exception IFRIC 16 paragraphe 6 ne s'applique qu'aux postes monétaires intragroupe dont le risque de change n'est pas éliminé en consolidation |
| 2. Couverture non autorisée pour créance de dividende intragroupe | OUI | - Applicable aux créances de dividendes intragroupe comptabilisées dans les comptes consolidés |

### 1. Couverture autorisée pour exposition de change intragroupe

**Applicabilité**: NON

**Conditions**:
   - L'exception IFRIC 16 paragraphe 6 ne s'applique qu'aux postes monétaires intragroupe dont le risque de change n'est pas éliminé en consolidation

**Raisonnement**:
Bien que IFRIC 16 paragraphe 6 permette une couverture pour le risque de change d'un poste monétaire intragroupe dont l'exposition n'est pas éliminée en consolidation, cette exception ne s'applique pas à une créance de dividende intragroupe, car elle est éliminée lors de la consolidation et ne génère pas d'exposition au change dans les états financiers consolidés.

**Implications pratiques**: Aucun élément couvert admissible ne subsiste après élimination intragroupe dans les comptes consolidés.

**Référence**:
 - IFRIC 16 6

    >an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation

### 2. Couverture non autorisée pour créance de dividende intragroupe

**Applicabilité**: OUI

**Conditions**:
   - Applicable aux créances de dividendes intragroupe comptabilisées dans les comptes consolidés

**Raisonnement**:
IFRS 9 paragraphe 6.3.5 exige que les éléments couverts soient des actifs, passifs, engagements ferme ou transactions forecast avec une partie externe à l'entité d'information. Une créance de dividende intragroupe est un poste intragroupe eliminated in consolidation, de sorte qu'elle ne remplit pas la condition de partie externe. IFRIC 16 paragraphe 10 confirme que la comptabilité de couverture ne s'applique qu'aux différences de change entre la monnaie fonctionnelle de l'opération étrangère et celle de l'entité mère.

**Implications pratiques**: Il n'est pas permis de désigner une créance de dividende intragroupe comme élément couvert dans une relation de couverture de risque de change.

**Référence**:
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency