# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Dans un schéma où des dividendes intragroupe ont déjà été reconnus en créance à recevoir, la question se pose du traitement du risque de change associé en consolidation. Ce risque peut-il être formellement documenté dans une relation de couverture ?

**Reformulation**:
>Hedge accounting for foreign exchange risk on intragroup dividend receivables in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias21`, `ias24`, `ias7`, `ias26`)
   - IFRIC (`ifric16`, `ifric17`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs12`)
   - SIC (`sic25`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias24`, `ias7`, `ias26`)
   - IFRIC (`ifric16`, `ifric17`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs12`)
   - SIC (`sic25`, `sic7`)

## Hypothèses
   - Le dividende intragroupe est enregistré en tant que créance monetary (écrite en compte) dans les états financiers individuels de l'entité qui le reçoit.
   - Les deux entités du groupe ont des devises fonctionnelles différentes, ce qui crée un risque de change sur cette créance.
   - La question porte sur les états financiers consolidés du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

La couverture du risque de change sur une créance de dividende intragroupe en consolidation est possible en vertu de l'exception IFRS 9 §6.3.6, mais uniquement si le dividende crée une exposition aux fluctuations de change qui n'est pas entièrement éliminée à la consolidation (c'est-à-dire lorsque les devises fonctionnelles diffèrent entre entités). En l'absence de ces conditions, le risque de change est reconnu en résultat sans couverture.

## Points Opérationnels

   - Documenter dès l'origine la désignation de couverture et les conditions de son efficacité conformément à IFRS 9 §6.4.1
   - En consolidation, la créance de dividende intragroupe est éliminée ; le risque de change subsiste uniquement si les devises fonctionnelles diffèrent et ne s'éliminent pas fully
   - L'instrument de couverture (dérivé ou non-dérivé) peut être détenu par n'importe quelle entité du groupe sous réserve des exigences de documentation
   - IFRIC 16 §13 précise qu'une même exposition ne peut être couverte qu'une seule fois dans les états consolidés de la mère ultime


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture en juste valeur du risque de change | OUI SOUS CONDITIONS | - Les devises fonctionnelles des deux entités doivent être différentes<br>- La créance de dividende doit être un élément monétaire libellé en monnaie étrangère<br>- Les différences de change ne doivent pas être entièrement éliminées à la consolidation (en pratique, lorsque les entités ont des devises fonctionnelles distinctes)<br>- L'exposition au risque de change doit être quantifiable et fiable<br>- Les critères de efficacité de la couverture selon IFRS 9 §6.4.1 doivent être satisfaits |
| 2. Reconnaissance en résultat sans couverture | OUI SOUS CONDITIONS | - Approche applicable par défaut ou en l'absence de désignation de couverture<br>- Si le dividende fait partie du montant net d'investissement dans l'entreprise étrangère, l'exception IAS 21 §32 permet une reconnaissance initiale en autres éléments du résultat global |

### 1. Couverture en juste valeur du risque de change

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les devises fonctionnelles des deux entités doivent être différentes
   - La créance de dividende doit être un élément monétaire libellé en monnaie étrangère
   - Les différences de change ne doivent pas être entièrement éliminées à la consolidation (en pratique, lorsque les entités ont des devises fonctionnelles distinctes)
   - L'exposition au risque de change doit être quantifiable et fiable
   - Les critères de efficacité de la couverture selon IFRS 9 §6.4.1 doivent être satisfaits

**Raisonnement**:
IFRS 9 §6.3.6 prévoit une exception à l'interdiction générale de désigner des éléments intragroupe comme éléments couverts : le risque de change d'un élément monétaire intragroupe peut être couvert dans les états consolidés si les différences de change ne sont pas totalement éliminées à la consolidation. Un dividende intragroupe en monnaie étrangère constitue un élément monétaire intragroupe, ce qui rend cette approche potentiellement applicable.

**Implications pratiques**: La créance de dividende peut être désignée comme élément couvert dans une relation de couverture de juste valeur, avec comptabilisation des variations de juste valeur attribuables au risque de change en résultat (ou en capitaux propres si couverture de investissement net).

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency

### 2. Reconnaissance en résultat sans couverture

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Approche applicable par défaut ou en l'absence de désignation de couverture
   - Si le dividende fait partie du montant net d'investissement dans l'entreprise étrangère, l'exception IAS 21 §32 permet une reconnaissance initiale en autres éléments du résultat global

**Raisonnement**:
IAS 21 §28 prescribe que les différences de change sur les éléments monétaires sont reconnues en résultat dans la période où elles surviennent. Cette approche s'applique par défaut lorsque les conditions de l'exception IFRS 9 §6.3.6 ne sont pas remplies (devises fonctionnelles identiques ou différences entièrement éliminées), ou lorsque l'entité choisit de ne pas désigner de relation de couverture.

**Implications pratiques**: Les différences de change sur la créance de dividende intragroupe sont reconnues en résultat (ou en OCI si le dividende fait partie d'un investissement net dans une entreprise étrangère), sans mécanisme de couverture.

**Référence**:
 - IAS 21 28

    >Exchange differences arising on the settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition shall be recognised in profit or loss
 - IAS 21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity's net investment in a foreign operation shall be recognised initially in other comprehensive income