# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Reformulation**:
>Whether foreign currency risk arising from an intragroup dividend-related receivable can be designated as a hedged item in consolidated financial statements under IFRS hedge accounting.

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
   - La question vise des comptes consolidés IFRS et un dividende intragroupe libellé dans une devise étrangère donnant lieu à une créance intragroupe comptabilisée.
   - La relation de couverture envisagée porte sur le risque de change de cette créance ou, selon le cas, du dividende avant comptabilisation s'il était encore à l'état de flux prévu.
   - Aucun fait n'indique que la créance de dividende fait partie d'un investissement net dans une activité à l'étranger au sens d'IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le risque de change de la créance/dividende intragroupe reste exposé dans les comptes consolidés. En IFRS 9, un item intragroupe n'est éligible qu'à titre d'exception, notamment pour un risque de change qui n'est pas totalement éliminé en consolidation.

## Points Opérationnels

   - Le point décisif est le moment de la désignation: une fois la créance de dividende comptabilisée, l'analyse porte sur un poste reconnu et non sur une transaction future.
   - En consolidation, il faut démontrer que la créance intragroupe est monétaire et que le risque de change affecte encore le résultat consolidé, typiquement entre entités à monnaies fonctionnelles différentes.
   - La documentation de couverture doit être alignée avec ce périmètre consolidé, car la règle générale exclut les items intragroupe et seule l'exception de change permet la désignation.
   - Si les écarts de change sont entièrement éliminés en consolidation, la désignation du dividende/créance intragroupe comme élément couvert n'est pas soutenable dans cette situation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un élément monétaire intragroupe<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- les écarts de change ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un élément monétaire intragroupe
   - les entités concernées ont des monnaies fonctionnelles différentes
   - les écarts de change ne sont pas totalement éliminés en consolidation

**Raisonnement**:
Une créance de dividende déjà comptabilisée est, par nature, un poste reconnu pouvant relever d'un modèle de couverture d'un item exposé au change. Mais, en comptes consolidés, IFRS 9 exclut en principe les items intragroupe, sauf exception lorsque le risque de change sur un élément monétaire intragroupe génère des écarts non totalement éliminés à la consolidation. IAS 21 confirme qu'un poste monétaire intragroupe entre entités à devises fonctionnelles différentes peut laisser subsister un effet de change en résultat consolidé.

**Implications pratiques**: La désignation n'est défendable en consolidation que si la créance de dividende laisse une exposition de change visible au niveau consolidé.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated** as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise une transaction future hautement probable. Or la question décrit un dividende intragroupe ayant déjà donné lieu à la comptabilisation d'une créance à recevoir, donc un poste déjà reconnu et non un flux futur encore non comptabilisé. Dans ce cas précis, le sujet n'est plus celui d'une transaction prévue mais celui d'une créance existante.

**Implications pratiques**: Ce modèle n'est pas le bon véhicule si le dividende a déjà été déclaré et transformé en créance intragroupe.

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

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le modèle de couverture d'investissement net concerne le risque de change lié aux actifs nets d'une activité à l'étranger, non une créance de dividende intragroupe ordinaire. Les textes fournis traitent séparément les éléments monétaires faisant partie de l'investissement net; rien dans les faits donnés n'indique que la créance de dividende en fasse partie. En l'état, ce n'est donc pas le modèle pertinent.

**Implications pratiques**: Sauf qualification spécifique comme partie de l'investissement net, une créance de dividende ne se traite pas comme une couverture d'investissement net.

**Référence**:
 - ias21 32

    >**Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation** (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 2

    >**Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation** will apply only when the net assets of that foreign operation are included in the financial statements. 1 The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.