# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Reformulation**:
>Possibilité d’appliquer la comptabilité de couverture en comptes consolidés à un risque de change lié à des dividendes intragroupe comptabilisés en créance à recevoir

## Documentation
**Consultée**
   - IAS-S (standard) (`ias12`, `ias39`, `ias32`, `ias21`, `ias7`, `ias24`, `ias27`, `ias40-bciasc`, `ias34`, `ias37`, `ias20`, `ias33`, `ias29`, `ias38`, `ias23`)
   - IFRIC (interpretation) (`ifric17`, `ifric23`, `ifric16`, `ifric19`, `ifric21`)
   - IFRS-S (standard) (`ifrs9`, `ifrs19`, `ifrs18`, `ifrs3`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a été déclaré et a donné lieu à la comptabilisation d’une créance à recevoir et d’une dette correspondante avant consolidation.
   - La créance et la dette intragroupe sont des éléments monétaires libellés dans une devise qui n’est pas la même pour au moins l’une des entités concernées.
   - La question porte sur les comptes consolidés du groupe, et non sur des comptes individuels ou séparés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui en consolidation si la créance de dividende intragroupe crée un risque de change qui n’est pas totalement éliminé à la consolidation, ce qui vise un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes. Dans ce cas, le modèle pertinent est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe doit être un élément monétaire exposé au change.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes, de sorte que les écarts de change ne soient pas totalement éliminés en consolidation.<br>- La documentation de couverture doit viser uniquement le risque de change de cette créance reconnue dans les comptes consolidés. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe doit être un élément monétaire exposé au change.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes, de sorte que les écarts de change ne soient pas totalement éliminés en consolidation.
   - La documentation de couverture doit viser uniquement le risque de change de cette créance reconnue dans les comptes consolidés.

**Raisonnement**:
Dans votre situation, la créance de dividende déjà comptabilisée est un élément reconnu ; IFRS 9 permet qu’un passif ou actif reconnu soit un élément couvert (IFRS 9 6.3.1). En consolidation, un élément intragroupe n’est normalement pas éligible, sauf pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés selon IAS 21 ; c’est précisément l’exception visée pour des entités du groupe ayant des monnaies fonctionnelles différentes (IFRS 9 6.3.6, IAS 21 45).

**Implications pratiques**: Une documentation de couverture est possible en consolidation sur le risque de change de la créance de dividende déjà reconnue, si l’exposition survit à la consolidation.

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
Votre question vise des dividendes intragroupe pour lesquels une créance a déjà été comptabilisée ; il ne s’agit donc plus d’une transaction future hautement probable mais d’un élément monétaire reconnu. IFRS 9 6.3.6 mentionne bien les transactions intragroupe futures hautement probables, mais ce cas ne correspond pas aux faits décrits ici ; la logique applicable est celle d’un receivable intragroupe existant (IFRS 9 6.3.6, IFRS 9 6.3.1).

**Implications pratiques**: La couverture de flux de trésorerie n’est pas le bon modèle si le dividende a déjà donné lieu à une créance comptabilisée.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).

### 3. Couverture d’un investissement net dans une activité à l’étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le risque visé ici porte sur une créance de dividende intragroupe comptabilisée, non sur l’exposition de conversion liée à un investissement net dans une activité étrangère. IFRS 9 6.3.1 distingue expressément le net investment comme une catégorie différente, et IFRIC 16 limite cette couverture aux différences de change entre la monnaie fonctionnelle de l’activité étrangère et celle de la société mère ; cela ne décrit pas une créance de dividende intragroupe (IFRS 9 6.3.1, IFRIC 16 10).

**Implications pratiques**: Le modèle de couverture d’investissement net ne convient pas pour couvrir le change sur une créance de dividende intragroupe reconnue.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.