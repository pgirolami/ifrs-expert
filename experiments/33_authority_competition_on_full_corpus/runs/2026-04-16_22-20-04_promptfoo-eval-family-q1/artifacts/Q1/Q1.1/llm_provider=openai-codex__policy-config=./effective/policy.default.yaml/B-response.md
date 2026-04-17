# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Reformulation**:
>Application de la comptabilité de couverture en consolidation au risque de change attaché à une créance de dividende intragroupe comptabilisée

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias21`, `ias7`, `ias12`, `ias27`, `ias24`, `ias38`, `ias19`, `ias34`, `ias33`, `ias40-bciasc`, `ias37`, `ias29`, `ias23`)
   - IFRIC (interpretation) (`ifric17`, `ifric2`, `ifric23`, `ifric19`)
   - IFRS-S (standard) (`ifrs17`, `ifrs19`, `ifrs9`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias32`, `ias21`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance, donc l’exposition visée porte sur une créance monétaire de dividende existante.
   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
   - La créance de dividende est libellée dans une devise qui crée un risque de change au niveau consolidé entre entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change est envisageable principalement en couverture de juste valeur si la créance intragroupe crée un écart de change non totalement éliminé (IFRS 9 6.3.6 ; IAS 21 45). La couverture de flux de trésorerie n’est pertinente que si l’on vise une transaction intragroupe future hautement probable, pas la créance déjà comptabilisée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.<br>- Le risque couvert doit être limité à la composante change de la créance comptabilisée dans les comptes consolidés. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - Le risque couvert doit être limité à la composante change de la créance comptabilisée dans les comptes consolidés.

**Raisonnement**:
Dans cette situation, la créance de dividende intragroupe est déjà comptabilisée ; IFRS 9 admet qu’un élément couvert puisse être un actif ou un passif comptabilisé (IFRS 9 6.3.1). En consolidation, un poste monétaire intragroupe peut être couvert pour son risque de change uniquement s’il génère des écarts de change non totalement éliminés, ce que IAS 21 confirme pour les postes monétaires intragroupe entre entités à monnaies fonctionnelles différentes (IFRS 9 6.3.6 ; IAS 21 45).

**Implications pratiques**: C’est l’approche la plus directement mobilisable ici si la créance de dividende intragroupe crée bien une exposition de change résiduelle au niveau consolidé.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, [Refer: IFRS 10 paragraph B86]such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Dans les faits décrits, le dividende intragroupe a déjà été comptabilisé en créance ; on n’est donc plus face à une transaction future. IFRS 9 réserve cette logique aux transactions prévues hautement probables, y compris intragroupe sous conditions en consolidation, ce qui ne correspond pas à une créance déjà reconnue (IFRS 9 6.3.3 ; IFRS 9 6.3.6).

**Implications pratiques**: Cette approche ne convient pas pour couvrir la partie change d’une créance de dividende déjà enregistrée en consolidation.

**Référence**:
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable. E19
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]

### 3. Couverture d’un investissement net dans une activité à l’étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le risque visé par la question est celui d’une créance de dividende intragroupe comptabilisée, non celui d’un investissement net dans une activité à l’étranger. IFRS 9 cite la couverture d’investissement net comme une catégorie distincte d’élément couvert, mais rien dans les faits fournis n’indique que la créance de dividende serait elle-même cet investissement net (IFRS 9 6.3.1).

**Implications pratiques**: Cette voie n’est pas adaptée au traitement de change d’une créance intragroupe de dividende en tant que telle.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).