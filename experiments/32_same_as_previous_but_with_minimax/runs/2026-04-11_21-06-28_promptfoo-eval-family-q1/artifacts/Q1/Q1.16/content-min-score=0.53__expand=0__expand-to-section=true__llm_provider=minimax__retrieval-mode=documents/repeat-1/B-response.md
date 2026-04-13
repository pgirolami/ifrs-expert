# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Au niveau consolidé, l’entité constate une créance liée à des dividendes intragroupe et supporte, de ce fait, une exposition au risque de change. Cette exposition peut-elle faire l’objet d’une documentation de couverture conforme aux IFRS ?

**Reformulation**:
>Whether an intragroup dividend receivable (a monetary item) can be designated as a hedged item for foreign currency risk in consolidated financial statements under IFRS hedge accounting requirements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias21`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric19`, `ifric21`, `ifric23`, `ifric1`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias21`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric16`, `ifric19`, `ifric21`, `ifric23`, `ifric1`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`, `sic7`)

## Hypothèses
   - L'entité prépare des états financiers consolidés selon les IFRS
   - La créance de dividendes intragroupe est un actif monétaire libellé en devises étrangères
   - La créance est entre entités du même groupe (émetteur du dividende et receveur au niveau consolidé)
   - Aucune désignation de couverture n'a encore été établie

## Recommandation

**NON**

La créance de dividendes intragroupe ne peut pas être désignée comme élément couvert dans une relation de couverture au niveau consolidé, car elle n'implique pas une partie externe au groupe (IFRS 9, §6.3.5). L'exception pour les éléments monétaires intragroupe (IFRS 9, §6.3.6) ne s'applique qu'aux couvertures de risques de change sur investissements nets dans des activités étrangères, ce qui ne correspond pas à une créance de dividendes.

## Points Opérationnels

   - L'écart de change sur la créance de dividendes intragroupe doit être reconnu en résultat (ou en OCI en cas d'activité étrangère qualifiée) selon IAS 21
   - Si la créance est liée à une activité étrangère dont l'investissement net fait l'objet d'une couverture distincte, la coordination des désignations doit être évaluée separately (IFRIC 16 §13)
   - La documentation de couverture ne peut pas englober la créance de dividendes intragroupe; seules des couvertures externes sur des éléments externes peuvent être documentées


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Exigence de partie externe pour l'élément couvert | NON | - (non spécifiées) |
| 2. Couverture d'investissement net pour éléments intragroupe | NON | - L'exception ne s'applique qu'aux couvertures d'investissement net dans une activité étrangère, et non aux créances de dividendes |
| 3. Comptabilisation des transactions en devises étrangères | OUI | - (non spécifiées) |

### 1. Exigence de partie externe pour l'élément couvert

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
L'IFRS 9 §6.3.5 exige que les éléments couverts concernent une partie externe à l'entité rapportant. Un dividende intragroupe est une transaction entre entités du même groupe, donc sans partie externe. Cette créance ne peut pas être désignée comme élément couvert dans une documentation de couverture au niveau consolidé.

**Implications pratiques**: L'exposition au risque de change sur la créance de dividendes intragroupe ne peut pas faire l'objet d'une documentation de couverture conforme aux IFRS.

**Référence**:
 - ifrs9 6.3.5

    >**For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.** Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.

### 2. Couverture d'investissement net pour éléments intragroupe

**Applicabilité**: NON

**Conditions**:
   - L'exception ne s'applique qu'aux couvertures d'investissement net dans une activité étrangère, et non aux créances de dividendes

**Raisonnement**:
L'exception de l'IFRS 9 §6.3.6 et les clarifications de l'IFRIC 16 ne s'appliquent qu'aux couvertures du risque de change sur investissements nets dans des activités étrangères. Une créance de dividendes intragroupe n'est pas un investissement net dans une activité étrangère; elle représente un droit de créance courant. Cette exception ne permet donc pas de qualifier la créance de dividende comme élément éligible.

**Implications pratiques**: L'IFRIC 16 et l'IFRS 9 §6.3.6 ne créent pas d'éligibilité pour les créances de dividendes intragroupe en tant qu'éléments couverts.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 3. Comptabilisation des transactions en devises étrangères

**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
En l'absence de désignation de couverture, l'IAS 21 §45 impose que les différences de change sur les actifs monétaires intragroupe (y compris les créances de dividendes) soient reconnues en résultat ou en OCI selon les cas, car ils ne peuvent pas être éliminés contre les passifs intragroupe correspondants. Le risque de change est donc comptabilisé sans être couvert.

**Implications pratiques**: L'exposition au risque de change est reconnue via les écarts de conversion, mais ne peut pas être désignée comme élément couvert dans une documentation de couverture.

**Référence**:
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.