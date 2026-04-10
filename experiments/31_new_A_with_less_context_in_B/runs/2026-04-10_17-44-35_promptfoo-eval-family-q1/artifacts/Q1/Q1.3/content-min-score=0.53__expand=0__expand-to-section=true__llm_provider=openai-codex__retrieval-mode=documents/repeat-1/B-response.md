# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Reformulation**:
>Which IFRS hedge accounting models are relevant to foreign exchange risk on intragroup dividend-related balances or transactions in consolidated financial statements.

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
   - La question vise des comptes consolidés.
   - Le dividende intragroupe a déjà été décidé et a donné lieu à la comptabilisation d'une créance intragroupe monétaire à recevoir.
   - La créance est libellée dans une devise étrangère pour au moins l'une des entités concernées.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via le modèle de couverture d'un élément reconnu, si la créance intragroupe crée en consolidation une exposition de change non totalement éliminée. En pratique, cela renvoie à l'exception IFRS 9 sur les éléments monétaires intragroupe; les modèles de cash flow hedge et de net investment hedge ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point déterminant est le moment de la couverture: après comptabilisation de la créance de dividende, on est sur un élément monétaire reconnu, non sur une transaction future.
   - En consolidation, l'exception IFRS 9 ne joue que si les entités ont des monnaies fonctionnelles différentes et que l'écart de change affecte encore le résultat consolidé.
   - La documentation de couverture doit viser explicitement le risque de change de la créance intragroupe, et non le dividende en tant que distribution en soi.
   - IAS 21 fixe le traitement de base des écarts de change, mais la désignation en couverture relève d'IFRS 9.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé au risque de change.<br>- Les gains ou pertes de change doivent ne pas être totalement éliminés en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée au titre d'IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé au risque de change.
   - Les gains ou pertes de change doivent ne pas être totalement éliminés en consolidation.
   - La relation de couverture doit être formellement désignée et documentée au titre d'IFRS 9.

**Raisonnement**:
Ici, le dividende a donné lieu à une créance à recevoir déjà comptabilisée: il s'agit donc d'un élément reconnu, non d'une transaction future. En consolidation, un élément monétaire intragroupe peut être désigné pour son risque de change si les écarts de change ne sont pas totalement éliminés, ce qui est le cas entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: La désignation est envisageable en consolidation pour la créance de dividende si elle génère un risque de change résiduel au niveau du groupe.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items**. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.
 - ias21 28

    >Exchange differences arising on the settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition during the period or in previous financial statements shall be recognised in profit or loss in the period in which they arise, except as described in paragraph 32.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Ce modèle vise une transaction future prévue hautement probable. Or, dans la situation décrite, le dividende a déjà donné naissance à une créance comptabilisée; le risque porte donc sur un solde monétaire existant et non sur des flux futurs encore prévisionnels.

**Implications pratiques**: La couverture de flux de trésorerie n'est pas le bon véhicule comptable pour une créance de dividende déjà enregistrée.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction** or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur le risque de change d'une créance de dividende intragroupe, pas sur le risque de change d'un investissement net dans une activité à l'étranger. IFRIC 16 réserve ce modèle à la couverture de l'exposition entre la monnaie fonctionnelle de l'entité mère et celle de l'activité étrangère.

**Implications pratiques**: Ce modèle ne s'applique pas à une créance de dividende intragroupe isolée.

**Référence**:
 - ifric16 7

    >This Interpretation applies to an entity that **hedges the foreign currency risk arising from its net investments in foreign operations** and wishes to qualify for hedge accounting in accordance with IFRS 9. For convenience this Interpretation refers to such an entity as a parent entity and to the financial statements in which the net assets of foreign operations are included as consolidated financial statements. All references to a parent entity apply equally to an entity that has a net investment in a foreign operation that is a joint venture, an associate or a branch.
 - ifric16 10

    >**Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.**
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.