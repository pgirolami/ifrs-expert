# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Reformulation**:
>Déterminer, en comptes consolidés, quels modèles de comptabilité de couverture IFRS peuvent être envisagés pour le risque de change lié à des dividendes intragroupe, en tenant compte des règles d’éligibilité des éléments intragroupe comme éléments couverts.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`, `ifrs7`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et une créance/dette correspondante a été comptabilisée dans les comptes individuels des entités du groupe.
   - La question porte sur les comptes consolidés, et non sur les comptes individuels ou séparés.
   - La créance de dividende est analysée comme un poste monétaire intragroupe distinct d’un élément faisant partie d’un investissement net dans une activité à l’étranger, sauf indication contraire.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une désignation de couverture n’est envisageable pour une créance de dividende intragroupe reconnue que si cette créance constitue un poste monétaire intragroupe exposé à un risque de change non intégralement éliminé en consolidation. Dans ce cas, le modèle pertinent est le fair value hedge, pas le cash flow hedge ni la couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Le risque de change doit générer des écarts de change non totalement éliminés en consolidation, parce que les entités concernées ont des monnaies fonctionnelles différentes.<br>- La relation de couverture doit satisfaire aux conditions de désignation, documentation et efficacité d’IFRS 9 6.4.1. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Le risque de change doit générer des écarts de change non totalement éliminés en consolidation, parce que les entités concernées ont des monnaies fonctionnelles différentes.
   - La relation de couverture doit satisfaire aux conditions de désignation, documentation et efficacité d’IFRS 9 6.4.1.

**Raisonnement**:
Une créance de dividende déjà reconnue est un actif reconnu ; IFRS 9 admet un fair value hedge d’un actif reconnu exposé à un risque particulier affectant le résultat (IFRS 9 6.5.2(a)). En consolidation, un élément intragroupe n’est en principe pas éligible, sauf pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés selon IAS 21 ; c’est précisément le cas visé pour certains postes monétaires entre entités à monnaies fonctionnelles différentes (IFRS 9 6.3.5, 6.3.6 ; IAS 21 45).

**Implications pratiques**: Possible en consolidation uniquement comme couverture de juste valeur du risque de change porté par la créance reconnue, sous réserve de l’exception intragroupe IFRS 9.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.4.1

    >A hedging relationship qualifies for hedge accounting only if all of the following criteria are met:
(a)the hedging relationship consists only of eligible hedging instruments and eligible hedged items.
(b)at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship and the entity’s risk management objective and strategy for undertaking the hedge. That documentation shall include identification of the hedging instrument, the hedged item, the nature of the risk being hedged and how the entity will assess whether the hedging relationship meets the hedge effectiveness requirements (including its analysis of the sources of hedge ineffectiveness and how it determines the hedge ratio).
(c)the hedging relationship meets all of the following hedge effectiveness requirements:
(i)there is an economic relationship between the hedged item and the hedging instrument (see paragraphs B6.4.4⁠–⁠B6.4.6);
(ii)the effect of credit risk does not dominate the value changes that result from that economic relationship (see paragraphs B6.4.7⁠–⁠B6.4.8); and
(iii)the hedge ratio of the hedging relationship is the same as that resulting from the quantity of the hedged item that the entity actually hedges and the quantity of the hedging instrument that the entity actually uses to hedge that quantity of hedged item. However, that designation shall not reflect an imbalance between the weightings of the hedged item and the hedging instrument that would create hedge ineffectiveness (irrespective of whether recognised or not) that could result in an accounting outcome that would be inconsistent with the purpose of hedge accounting (see paragraphs B6.4.9⁠–⁠B6.4.11).
 - ifrs9 6.5.2

    >There are three types of hedging relationships:
(a)fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.
(b)cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.
(c)hedge of a net investment in a foreign operation as defined in IAS 21.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question vise un dividende intragroupe pour lequel une créance a déjà été reconnue ; il ne s’agit donc plus d’une transaction future hautement probable mais d’un actif déjà comptabilisé. Or IFRS 9 réserve le cash flow hedge à la variabilité de flux d’un actif/passif ou d’une transaction future hautement probable ; le cas spécifique du dividende reconnu correspond davantage à une exposition de poste monétaire qu’à une transaction future (IFRS 9 6.5.2(b), 6.3.6).

**Implications pratiques**: La documentation de couverture ne devrait pas être structurée comme un cash flow hedge une fois la créance de dividende reconnue.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.5.2

    >There are three types of hedging relationships:
(a)fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.
(b)cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.
(c)hedge of a net investment in a foreign operation as defined in IAS 21.

### 3. Couverture d’un investissement net dans une activité à l’étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur une créance de dividende intragroupe reconnue, non sur l’exposition de conversion liée à un investissement net dans une activité à l’étranger. IFRIC 16 limite ce modèle au risque de change entre la monnaie fonctionnelle de l’activité étrangère et celle de la société mère, tandis qu’IAS 21 réserve le traitement OCI aux postes monétaires faisant partie de l’investissement net ; par hypothèse, la créance de dividende n’entre pas dans cette catégorie (IFRIC 16 10, 12 ; IAS 21 32, 33).

**Implications pratiques**: Sauf si la créance faisait réellement partie de l’investissement net, ce modèle n’est pas adapté à un dividende intragroupe reconnu.

**Référence**:
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - ifric16 12

    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.
 - ias21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ias21 33

    >When a monetary item forms part of a reporting entity’s net investment in a foreign operation and is denominated in the functional currency of the reporting entity, an exchange difference arises in the foreign operation’s individual financial statements in accordance with paragraph 28. If such an item is denominated in the functional currency of the foreign operation, an exchange difference arises in the reporting entity’s separate financial statements in accordance with paragraph 28. If such an item is denominated in a currency other than the functional currency of either the reporting entity or the foreign operation, an exchange difference arises in the reporting entity’s separate financial statements and in the foreign operation’s individual financial statements in accordance with paragraph 28. Such exchange differences are recognised in other comprehensive income in the financial statements that include the foreign operation and the reporting entity (ie financial statements in which the foreign operation is consolidated or accounted for using the equity method).