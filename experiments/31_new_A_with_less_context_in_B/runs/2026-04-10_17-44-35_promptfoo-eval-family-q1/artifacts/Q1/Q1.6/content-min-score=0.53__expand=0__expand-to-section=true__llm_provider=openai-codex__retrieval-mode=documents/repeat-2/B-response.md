# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Reformulation**:
>Whether foreign exchange risk on an intragroup dividend receivable recognised in consolidated financial statements can be designated as a hedged item under IFRS hedge accounting.

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
   - Le dividende intragroupe a donné lieu à la comptabilisation d'une créance monétaire avant son règlement.
   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
   - La créance de dividende est libellée dans une devise pouvant générer un écart de change entre entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via l'exception IFRS 9 applicable à un poste monétaire intragroupe en consolidation. Il faut que le risque de change sur la créance de dividende ne soit pas totalement éliminé à la consolidation et affecte le résultat consolidé.

## Points Opérationnels

   - Le point décisif en consolidation est le niveau de reporting : la règle générale exclut l'intragroupe, sauf l'exception de l'IFRS 9 pour certains postes monétaires en devise.
   - Il faut vérifier au moment de la désignation si la créance de dividende génère bien des écarts de change non totalement éliminés en consolidation.
   - Si les écarts de change relèvent d'un investissement net, leur logique comptable bascule vers l'OCI et non vers une couverture de juste valeur de la créance de dividende.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.<br>- Le risque de change affecte le résultat consolidé plutôt que d'être traité comme faisant partie d'un investissement net. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.
   - Le risque de change affecte le résultat consolidé plutôt que d'être traité comme faisant partie d'un investissement net.

**Raisonnement**:
Dans cette situation, la créance de dividende déjà comptabilisée est un poste reconnu et, si elle est monétaire, son risque de change peut entrer dans l'exception des éléments intragroupe en consolidation. Cela n'est possible que si les écarts de change ne sont pas totalement éliminés à la consolidation, ce qui peut arriver entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: La désignation est envisageable en consolidation si la documentation vise spécifiquement le risque de change résiduel sur la créance intragroupe.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.
 - ifrs9 6.3.2

    >**The hedged item must be reliably measurable.**

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur une créance de dividende déjà constatée, donc sur un poste reconnu dont la variation de change est déjà attachée à un solde monétaire existant. Dans ce cas précis, l'enjeu n'est pas une transaction future hautement probable, mais le risque de change d'une créance reconnue en consolidation.

**Implications pratiques**: Ce modèle n'est pas le plus adapté aux faits décrits, car l'exposition visée n'est plus au stade d'un flux futur non encore reconnu.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions** with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.

### 3. Couverture d'un investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Un dividende intragroupe à recevoir correspond normalement à une créance destinée à être réglée, non à un élément faisant partie de l'investissement net dans une activité à l'étranger. Le modèle de couverture d'investissement net vise les expositions de change relevant d'un investissement net, avec comptabilisation en OCI en consolidation.

**Implications pratiques**: Sauf si le poste relevait en substance d'un investissement net, ce qui n'est pas le cas décrit, ce modèle ne s'applique pas.

**Référence**:
 - ias21 32

    >Exchange differences arising on a **monetary item that forms part of a reporting entity’s net investment** in a foreign operation (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment** in a foreign operation. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.