# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Reformulation**:
>Which IFRS hedge accounting models are relevant when assessing whether foreign exchange differences on an intragroup dividend receivable recognised in consolidated financial statements can be designated in a hedging relationship.

## Documentation
**Consultée**
   - IAS (`ias21`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IAS (`ias21`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et un receivable intragroupe a été comptabilisé ; la question porte donc sur un poste monétaire reconnu, et non sur une transaction future.
   - Le receivable est libellé dans une monnaie étrangère par rapport à la monnaie fonctionnelle d'au moins une des entités concernées.
   - L'analyse est faite au niveau des comptes consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via la couverture du risque de change d'un poste monétaire intragroupe reconnu si les écarts de change ne sont pas entièrement éliminés en consolidation. Dans cette situation, le modèle pertinent est la couverture de juste valeur ; les modèles de cash flow hedge et de net investment hedge ne sont en principe pas adaptés aux faits décrits.

## Points Opérationnels

   - Vérifier d'abord si le receivable de dividende est bien un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.
   - Documenter que l'exposition de change affecte encore les comptes consolidés et n'est pas entièrement éliminée à la consolidation.
   - La question se tranche au moment où le receivable est comptabilisé : après cette date, on n'est plus dans une logique de transaction future.
   - Si les écarts de change relevaient d'un investissement net au sens d'IAS 21.32, l'analyse basculerait vers le modèle de net investment hedge, pas vers celui retenu ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le receivable de dividende doit être un poste monétaire intragroupe exposé au risque de change.<br>- Les écarts de change doivent ne pas être entièrement éliminés en consolidation, typiquement parce que les entités ont des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le receivable de dividende doit être un poste monétaire intragroupe exposé au risque de change.
   - Les écarts de change doivent ne pas être entièrement éliminés en consolidation, typiquement parce que les entités ont des monnaies fonctionnelles différentes.

**Raisonnement**:
Le receivable de dividende est un actif reconnu, donc un type de hedged item admis en IFRS 9. En comptes consolidés, un poste intragroupe est en principe exclu, sauf pour le risque de change d'un poste monétaire intragroupe si les écarts de change subsistent en consolidation ; IAS 21 précise que c'est le cas entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: La désignation peut être envisagée en couverture de juste valeur du risque de change du receivable intragroupe dans les comptes consolidés.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Ce modèle vise notamment une forecast transaction hautement probable. Or, dans la situation décrite, le dividende a déjà donné lieu à la constatation d'un receivable ; l'exposition analysée est donc la variation de change sur un poste reconnu, pas une transaction future intragroupe hautement probable.

**Implications pratiques**: La question doit être analysée sur la base d'un poste monétaire reconnu, et non comme une transaction future couverte en cash flow hedge.

**Référence**:
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le fait décrit porte sur un receivable de dividende intragroupe, non sur la couverture d'un investissement net dans une activité étrangère. Le modèle de net investment hedge est distinct et vise les écarts de change liés à l'investissement net, avec comptabilisation en OCI dans les états financiers consolidés.

**Implications pratiques**: Sauf si le poste relevait des circonstances d'IAS 21.32, ce modèle n'est pas celui correspondant au dividende à recevoir décrit.

**Référence**:
 - ias21 32

    >Exchange differences arising on a **monetary item that forms part of a reporting entity’s net investment in a foreign operation** (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment** in a foreign operation. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.