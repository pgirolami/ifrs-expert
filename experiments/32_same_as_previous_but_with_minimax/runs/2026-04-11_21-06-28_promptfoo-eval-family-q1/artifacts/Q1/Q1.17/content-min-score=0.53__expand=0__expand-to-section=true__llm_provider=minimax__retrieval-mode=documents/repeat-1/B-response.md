# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Reformulation**:
>Whether intragroup dividend receivables creating foreign currency exposure in consolidated financial statements can qualify as hedged items under IFRS 9 hedge accounting

## Documentation
**Consultée**
   - IAS (`ias21`, `ias24`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric1`, `ifric23`, `ifric22`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs2`, `ifrs12`)
   - SIC (`sic25`, `sic7`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias24`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric1`, `ifric23`, `ifric22`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs2`, `ifrs12`)
   - SIC (`sic25`, `sic7`, `sic29`)

## Hypothèses
   - Le dividende intragroupe à recevoir constitue un élément monétaire libellé en devise étrangère
   - Les deux entités intragroupe concernées ont des devises fonctionnelles différentes
   - Les états financiers considérés sont les états financiers consolidés
   - La variation de change связана с foreign exchange differences qui ne sont pas éliminées à la consolidation conformément à IAS 21

## Recommandation

**OUI SOUS CONDITIONS**

Sous réserve que les conditions de l'approche 1 soient remplies, la couverture de la composante change d'une créance de dividende intragroupe est possible en vertu de l'exception prévue par IFRS 9 paragraphe 6.3.6

## Points Opérationnels

   - Vérifier que les devises fonctionnelles des entités intragroupe sont bien différentes avant de conclure à l'éligibilité
   - Documenter la relation de couverture conformément à IFRS 9 §6.4.1 dès la désignation
   - Évaluer si l'approche 1 (couverture générale) ou l'approche 2 (couverture d'investissement net) est plus appropriée selon la substance économique de la créance de dividende
   - Si aucune couverture n'est désignée, la variation de change sera reconnue en résultat en vertu de IAS 21 §28


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de la composante change d'un élément monétaire intragroupe | OUI SOUS CONDITIONS | - Les entités intragroupe doivent avoir des devises fonctionnelles différentes<br>- La variation de change ne doit pas être éliminée à la consolidation<br>- Tous les critères de désignation et de documentation de l'IFRS 9 §6.4.1 doivent être satisfaits |
| 2. Couverture d'investissement net dans une opération étrangère | OUI SOUS CONDITIONS | - Le dividende doit être lié à un investissement net dans une opération étrangère<br>- Le risque de change couvert doit être la différence entre la devise fonctionnelle de l'opération étrangère et celle de l'entité présentant les comptes consolidés<br>- Seule une relation de couverture par entité du groupe est admise pour le même risque (IFRIC 16 §13) |
| 3. Reconnaissance des différences de change sans couverture | OUI | - (non spécifiées) |

### 1. Couverture de la composante change d'un élément monétaire intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les entités intragroupe doivent avoir des devises fonctionnelles différentes
   - La variation de change ne doit pas être éliminée à la consolidation
   - Tous les critères de désignation et de documentation de l'IFRS 9 §6.4.1 doivent être satisfaits

**Raisonnement**:
Le dividende intragroupe à recevoir est un élément monétaire. Lorsque les deux entités ont des devises fonctionnelles différentes, la variation de change n'est pas éliminée à la consolidation (IAS 21 §32). L'IFRS 9 §6.3.6 permet alors de désigner ce risque de change comme élément couvert dans les comptes consolidés.

**Implications pratiques**: Désignation possible du risque de change sur le dividende intragroupe à recevoir comme élément couvert dans une relation de couverture.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IAS 21 28

    >Exchange differences arising on the settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition during the period shall be recognised in profit or loss

### 2. Couverture d'investissement net dans une opération étrangère

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende doit être lié à un investissement net dans une opération étrangère
   - Le risque de change couvert doit être la différence entre la devise fonctionnelle de l'opération étrangère et celle de l'entité présentant les comptes consolidés
   - Seule une relation de couverture par entité du groupe est admise pour le même risque (IFRIC 16 §13)

**Raisonnement**:
Si le dividende intragroupe provient d'un investissement net dans une opération étrangère, IFRIC 16 §7 et §10 autorisent la couverture du risque de change dans les comptes consolidés du fait que le risque de change n'est pas éliminé.

**Implications pratiques**: Possibilité alternative de qualifier la relation de couverture comme couverture d'investissement net, avec reconnaissance initiale en OCI des gains et pertes de change efficaces.

**Référence**:
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency
 - IFRIC 16 7

    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations

### 3. Reconnaissance des différences de change sans couverture

**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IAS 21 §28 impose de reconnaître les différences de change des éléments monétaires en résultat. La mise en place d'une relation de couverture est optional; en l'absence de désignation, les écarts de change sont simplement comptabilisés en résultat.

**Implications pratiques**: Traitement de base sans désignation de couverture: la variation de change est reconnue immédiatement en résultat conformément à IAS 21.

**Référence**:
 - IAS 21 28

    >Exchange differences arising on monetary items shall be recognised in profit or loss in the period in which they arise