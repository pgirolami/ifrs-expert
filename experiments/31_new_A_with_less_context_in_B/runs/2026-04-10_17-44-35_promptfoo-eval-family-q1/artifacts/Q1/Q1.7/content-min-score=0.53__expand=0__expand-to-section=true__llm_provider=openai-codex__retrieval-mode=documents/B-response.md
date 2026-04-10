# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Reformulation**:
>Whether foreign currency risk on an intragroup dividend receivable recognised in consolidated financial statements can be designated in hedge accounting under IFRS.

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
   - Le dividende intragroupe est libellé dans une devise différente de la monnaie fonctionnelle de l'entité qui porte la créance ou la dette correspondante.
   - La créance de dividende constitue un élément monétaire intragroupe entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
   - L'analyse est faite au niveau des comptes consolidés, où la question est celle de l'éligibilité de l'exposition de change résiduelle à la comptabilité de couverture.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, un élément monétaire intragroupe ne peut être couvert que par l'exception IFRS 9 visant le risque de change non totalement éliminé. Cela peut être recevable pour une créance de dividende déjà reconnue, mais pas au titre d'une couverture de flux futurs ni, en principe, comme couverture d'investissement net.

## Points Opérationnels

   - Le point décisif est le niveau de reporting: en comptes consolidés, la règle générale exclut l'intragroupe, sauf l'exception ciblée sur le risque de change des éléments monétaires intragroupe.
   - Le fait générateur est le moment où le dividende a déjà créé une créance: on est alors sur un élément reconnu, pas sur une transaction intragroupe future hautement probable.
   - La documentation doit démontrer que l'exposition de change subsiste en consolidation parce que les entités concernées ont des monnaies fonctionnelles différentes.
   - Si l'exposition de change est totalement éliminée en consolidation, l'exception IFRS 9 6.3.6 ne peut pas être mobilisée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende doit exposer le groupe à des écarts de change non totalement éliminés en consolidation<br>- la créance doit résulter d'un lien intragroupe entre entités ayant des monnaies fonctionnelles différentes<br>- la désignation doit viser le risque de change de l'élément monétaire reconnu |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende doit exposer le groupe à des écarts de change non totalement éliminés en consolidation
   - la créance doit résulter d'un lien intragroupe entre entités ayant des monnaies fonctionnelles différentes
   - la désignation doit viser le risque de change de l'élément monétaire reconnu

**Raisonnement**:
Ici, la créance de dividende déjà reconnue est un élément monétaire intragroupe. En comptes consolidés, un tel élément n'est en principe pas éligible, sauf pour son risque de change lorsqu'il génère des écarts de change non totalement éliminés à la consolidation entre entités à monnaies fonctionnelles différentes. Dans ce cas, cette exposition peut relever du modèle de couverture sur élément comptabilisé.

**Implications pratiques**: La documentation doit cibler l'exposition de change résiduelle en consolidation sur la créance de dividende reconnue.

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
La question vise des dividendes intragroupe ayant déjà donné lieu à la reconnaissance d'une créance. Or le modèle de cash flow hedge vise notamment une transaction prévue hautement probable ; ici, l'exposition décrite n'est plus un flux futur non comptabilisé mais un élément monétaire déjà comptabilisé. Le cas correspond donc mal à ce modèle.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une couverture de flux de trésorerie pour cette créance déjà reconnue.

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

### 3. Couverture d'investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La couverture d'investissement net vise le risque de change sur les actifs nets d'une activité étrangère. Une créance de dividende intragroupe reconnue est un élément monétaire distinct, relevant des écarts de change IAS 21 sur positions intragroupe, et non la couverture du montant des actifs nets d'une activité étrangère. Ce n'est donc pas le bon modèle pour la situation décrite.

**Implications pratiques**: Il ne faut pas documenter cette créance de dividende comme une couverture d'investissement net.

**Référence**:
 - ifric16 2

    >**Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation** will apply only when the net assets of that foreign operation are included in the financial statements. 1 The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
 - ifric16 3

    >IFRS 9 requires the designation of an eligible hedged item and eligible hedging instruments in a hedge accounting relationship. If there is a designated hedging relationship, in the case of a net investment hedge, the gain or loss on the hedging instrument that is determined to be an effective hedge of the net investment is recognised in other comprehensive income and is included with the foreign exchange differences arising on translation of the results and financial position of the foreign operation.