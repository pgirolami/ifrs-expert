# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Reformulation**:
>Eligibility of intragroup foreign exchange exposures for hedge accounting in consolidated financial statements under IFRS

## Documentation
**Consultée**
   - IAS (`ias24`, `ias27`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric1`, `ifric19`, `ifric21`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs12`, `ifrs18`)
   - SIC (`sic25`, `sic29`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - La créance sur dividendes intragroupe est un actif monétaire libellé dans une devise autre que la fonctionnelle de l'entité débitrice
   - Les entités concernées ont des devises fonctionnelles différentes
   - L'exposition au risque de change résultant n'est pas éliminée lors de la consolidation en vertu d'IAS 21

## Recommandation

**OUI SOUS CONDITIONS**

L'exposition de change identifiée sur la créance intragroupe peut être éligible à la comptabilité de couverture au niveau consolidé, sous réserve que le risque de change affecte réellement le résultat consolidé (condition impérative de l'exception prévue par IFRS 9 §6.3.6). En l'absence de cette condition, l'approche prohibitive générale s'applique.

## Points Opérationnels

   - Vérifier que les différences de change sur la créance ne sont pas éliminées à la consolidation ( IAS 21 ) avant toute désignation
   - Documenter formellement que le risque de change affectera le résultat consolidé, condition impérative de l'exception
   - Qualifier l'instrument de couverture comme derivative ou autre instrument éligible conformément à IFRS 9 sections 6.2-6.5


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Interdiction générale de couverture des opérations intragroupe | NON | - (non spécifiées) |
| 2. Exception pour éléments monétaires intragroupe à exposition de change non éliminée | OUI SOUS CONDITIONS | - L'élément monétaire intragroupe doit être dénommé dans une devise différente de la fonctionnelle de l'entité contractante<br>- Les différences de change ne doivent pas être entièrement éliminées à la consolidation<br>- Le risque de change doit impacter le résultat consolidé (et non être éliminé) |
| 3. Couverture d'investissement net dans une opération étrangère | NON | - (non spécifiées) |

### 1. Interdiction générale de couverture des opérations intragroupe

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche représente le principe général d'IFRS 9 §6.3.5, qui interdit la désignation comme élément couvert d'opérations entre entités du même groupe dans les comptes consolidés. Cependant, l'énoncé indique qu'une exposition de change distincte a été identifiée, suggérant l'existence d'un risque de change non éliminé, ce qui oriente l'analyse vers l'exception applicable.

**Implications pratiques**: Non applicable en présence d'une exposition de change non éliminée sur élément monétaire intragroupe.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items**. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.

### 2. Exception pour éléments monétaires intragroupe à exposition de change non éliminée

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'élément monétaire intragroupe doit être dénommé dans une devise différente de la fonctionnelle de l'entité contractante
   - Les différences de change ne doivent pas être entièrement éliminées à la consolidation
   - Le risque de change doit impacter le résultat consolidé (et non être éliminé)

**Raisonnement**:
IFRS 9 §6.3.6 autorise spécifiquement la désignation comme élément couvert du risque de change d'un élément monétaire intragroupe lorsque, conformément à IAS 21, les différences de change ne sont pas totalement éliminées à la consolidation et que ce risque affecte le résultat consolidé. La créance sur dividendes intragroupe constitue un élément monétaire dont l'exposition au change peut, sous conditions, être couverte.

**Implications pratiques**: La créance sur dividendes intragroupe peut être désignée comme élément couvert dans les comptes consolidés si les trois conditions sont remplies.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'investissement net dans une opération étrangère

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche concernerait la couverture du risque de change lié à un investissement net dans une opération étrangère, conformément à IFRIC 16. La question porte sur une créance sur dividendes intragroupe, instrument financier de type créancier, et non sur un investissement net dans une opération étrangère. Cette approche n'est pas adaptée au fait décrit.

**Implications pratiques**: Non applicable à une créance sur dividendes intragroupe qui ne constitue pas un investissement net.

**Référence**:
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.