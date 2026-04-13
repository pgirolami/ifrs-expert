# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Reformulation**:
>Eligibility of intragroup monetary items (dividend receivable) to be designated as hedged items in hedge accounting for foreign exchange risk under IFRS

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias24`, `ias37`)
   - IFRIC (`ifric2`, `ifric17`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias24`, `ias37`)
   - IFRIC (`ifric2`, `ifric17`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS (`ifrs19`, `ifrs7`, `ifrs9`, `ifrs12`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic29`)

## Hypothèses
   - La créance dividends intragroupe est dénommée en devise étrangère.
   - L'entité prépare des états financiers consolidés.
   - La question porte sur la désignation de l'exposition de change de cette créance intragroupe comme élément couvert dans une relation de couverture de change.

## Recommandation

**OUI SOUS CONDITIONS**

En vertu d'IFRS 9 §6.3.6, une créance intragroupe libellée en devise étrangère peut être désignée comme élément couvert dans les états financiers consolidés, mais uniquement pour couvrir le risque de change lié à un investissement net dans une opération étrangère, et uniquement si ce risque n'est pas éliminé par consolidation.

## Points Opérationnels

   - Vérifier si le risque de change de la créance dividendes intragroupe est éliminé à la consolidation avant toute désignation.
   - Si la créance est éliminée à la consolidation (même devise fonctionnelle), aucune désignation n'est possible.
   - Si la créance n'est pas éliminée et concerne l'investissement net dans une opération étrangère, la désignation est possible dans une couverture de investissement net.
   - Pour tout autre type de couverture (flux de trésorerie, juste valeur), la désignation est interdite.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Créance intragroupe éligible uniquement en couverture d'investissement net | OUI SOUS CONDITIONS | - La créance constitue un élément monétaire intragroupe.<br>- L'exposition de change n'est pas éliminée à la consolidation (IAS 21).<br>- La relation de couverture vise spécifiquement le risque de change lié à l'investissement net dans l'opération étrangère (couverture de'investissement net). |
| 2. Créance intragroupe non éligible pour les couvertures autres que l'investissement net | NON | - Restriction : cette approche n'est pas applicable si la relation de couverture est une couverture d'investissement net dans une opération étrangère. |

### 1. Créance intragroupe éligible uniquement en couverture d'investissement net

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance constitue un élément monétaire intragroupe.
   - L'exposition de change n'est pas éliminée à la consolidation (IAS 21).
   - La relation de couverture vise spécifiquement le risque de change lié à l'investissement net dans l'opération étrangère (couverture de'investissement net).

**Raisonnement**:
IFRS 9 §6.3.6 autorise la désignation du risque de change d'un élément monétaire intragroupe comme élément couvert dans les états consolidés, mais cette exception est limitée aux couvertures d'investissement net dans une opération étrangère dont l'exposition de change n'est pas éliminée à la consolidation.

**Implications pratiques**: Si ces conditions sont satisfaites, la créance peut être désignée comme élément couvert dans une couverture de investissement net.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifric16 8

    >**This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting**.

### 2. Créance intragroupe non éligible pour les couvertures autres que l'investissement net

**Applicabilité**: NON

**Conditions**:
   - Restriction : cette approche n'est pas applicable si la relation de couverture est une couverture d'investissement net dans une opération étrangère.

**Raisonnement**:
IFRS 9 §6.3.5 exige qu'un élément couvert soit une partie externe à l'entité déclarante. IFRIC 16 §8 confirme que l'exception pour les éléments intragroupe est limitée aux couvertures d'investissement net et ne peut être appliquée par analogie à d'autres types de couvertures.

**Implications pratiques**: Une créance dividendes intragroupe ne peut pas être désignée comme élément couvert dans une couverture de flux de trésorerie ou une couverture de juste valeur.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items**. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifric16 8

    >**This Interpretation applies only to hedges of net investments in foreign operations**; it should not be applied by analogy to other types of hedge accounting.