# Analyse d'une question comptable

**Date**: 2026-05-13

## Question

**Utilisateur**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Reformulation**:
>Éligibilité, dans les comptes consolidés, de la composante de risque de change d’une créance de dividende intragroupe comptabilisée comme élément couvert en comptabilité de couverture

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
   - La créance de dividende intragroupe est déjà comptabilisée et constitue un élément monétaire entre deux entités du groupe.
   - La question vise les comptes consolidés IFRS du groupe, et non les comptes individuels ou séparés.
   - Le dividende intragroupe est libellé dans une devise créant un risque de change entre des entités ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, une créance de dividende intragroupe n’est éligible que via l’exception visant le risque de change d’un élément monétaire intragroupe non totalement éliminé en consolidation. En pratique, cela peut être documenté comme couverture de juste valeur, pas comme couverture de flux de trésorerie ni comme couverture d’investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Les deux entités concernées doivent avoir des monnaies fonctionnelles différentes, de sorte que le risque de change affecte le résultat consolidé.<br>- La relation de couverture doit être formellement désignée et documentée dès l’origine conformément à IFRS 9 6.4.1. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Les deux entités concernées doivent avoir des monnaies fonctionnelles différentes, de sorte que le risque de change affecte le résultat consolidé.
   - La relation de couverture doit être formellement désignée et documentée dès l’origine conformément à IFRS 9 6.4.1.

**Raisonnement**:
En consolidation, la règle générale exclut les éléments intragroupe comme éléments couverts, mais IFRS 9 6.3.6 prévoit une exception pour le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés. IAS 21 45 précise justement qu’un actif/passif monétaire intragroupe entre entités à monnaies fonctionnelles différentes laisse apparaître un résultat de change en consolidation. Une créance de dividende déjà comptabilisée est un actif reconnu, ce qui la fait entrer dans le champ d’une couverture de juste valeur au titre d’IFRS 9 6.5.2(a), sous réserve des critères de documentation et d’efficacité d’IFRS 9 6.4.1.

**Implications pratiques**: Possible en consolidation si la créance de dividende génère un risque de change résiduel au niveau consolidé et si la documentation de couverture est mise en place selon IFRS 9.

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
La question porte sur des dividendes intragroupe pour lesquels une créance a déjà été comptabilisée : il ne s’agit donc plus d’une transaction future hautement probable mais d’un actif reconnu. IFRS 9 6.5.2(b) vise la variabilité de flux de trésorerie d’un actif/passif ou d’une transaction future hautement probable ; ici, le sujet est le risque de change sur une créance comptabilisée, que l’exception d’IFRS 9 6.3.6 traite comme élément monétaire intragroupe en consolidation, non comme flux futur.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une couverture de flux de trésorerie pour cette créance de dividende déjà reconnue.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.5.2

    >There are three types of hedging relationships:
(a)fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.
(b)cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.
(c)hedge of a net investment in a foreign operation as defined in IAS 21.

### 3. Couverture d’un investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le risque visé ici est celui d’une créance de dividende intragroupe comptabilisée, non celui des actifs nets d’une opération étrangère. IFRIC 16 10 et 12 limitent la couverture d’investissement net au risque de change entre la monnaie fonctionnelle de l’opération étrangère et celle de la société mère sur l’investissement net lui-même ; cela ne correspond pas à une créance de dividende à recevoir.

**Implications pratiques**: Ce modèle n’est pas adapté pour couvrir le change sur un dividende intragroupe déclaré et comptabilisé.

**Référence**:
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - ifric16 12

    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.
 - ifric16 2

    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation will apply only when the net assets of that foreign operation are included in the financial statements. 1 The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.