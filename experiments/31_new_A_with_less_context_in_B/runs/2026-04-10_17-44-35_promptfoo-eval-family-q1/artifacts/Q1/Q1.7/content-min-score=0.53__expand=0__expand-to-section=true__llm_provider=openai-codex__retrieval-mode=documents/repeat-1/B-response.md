# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Reformulation**:
>Whether foreign currency risk on an intragroup dividend receivable recognised in consolidated financial statements can be designated in a hedge accounting relationship under IFRS.

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
   - La créance de dividende intragroupe est une créance monétaire libellée dans une devise différente de la monnaie fonctionnelle d'au moins l'une des entités concernées.
   - La question vise les comptes consolidés, puisque la créance est indiquée comme reconnue en consolidation.
   - Le dividende intragroupe ne constitue pas ici une couverture d'un investissement net dans une activité à l'étranger, sauf si ce fait est expressément documenté séparément.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le risque de change sur cette créance intragroupe n'est pas entièrement éliminé en consolidation. En IFRS, l'exception de l'IFRS 9 pour certains éléments monétaires intragroupe permet alors une désignation en couverture dans les comptes consolidés.

## Points Opérationnels

   - Vérifier d'abord si la créance de dividende est bien un poste monétaire intragroupe exposé à un risque de change résiduel en consolidation.
   - L'analyse doit être faite au niveau des comptes consolidés, car la règle générale d'inéligibilité des éléments intragroupe y est seulement levée par exception.
   - Si les gains/pertes de change sont entièrement éliminés en consolidation, la documentation de couverture n'est pas recevable pour cet élément.
   - Ne pas utiliser le modèle de couverture d'investissement net sauf si l'objet couvert est réellement l'exposition sur les actifs nets d'une activité étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un élément monétaire intragroupe.<br>- Le risque de change doit produire des gains ou pertes de change non totalement éliminés en consolidation.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un élément monétaire intragroupe.
   - Le risque de change doit produire des gains ou pertes de change non totalement éliminés en consolidation.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.

**Raisonnement**:
Une créance de dividende déjà reconnue est, en principe, un élément reconnu pouvant entrer dans un modèle de couverture. En consolidation, un élément intragroupe n'est normalement pas éligible, sauf pour le risque de change d'un élément monétaire intragroupe qui génère des écarts non totalement éliminés selon IAS 21.

**Implications pratiques**: La documentation de couverture n'est recevable qu'à hauteur du risque de change qui subsiste réellement dans les comptes consolidés.

**Référence**:
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
La situation décrite porte sur des dividendes intragroupe ayant déjà donné lieu à la reconnaissance d'une créance en consolidation. Or l'exception IFRS 9 relative aux transactions intragroupe hautement probables vise une transaction future intragroupe, pas une créance déjà constatée.

**Implications pratiques**: Ce modèle n'est pas adapté au fait décrit, car le risque porte sur un poste reconnu et non sur un flux futur hautement probable.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction** or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).

### 3. Couverture d'un investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le fait décrit concerne une créance de dividende intragroupe reconnue, et non l'exposition de conversion sur les actifs nets d'une activité étrangère. IFRIC 16 réserve ce modèle au risque de change entre la monnaie fonctionnelle de l'activité étrangère et celle d'une entité mère sur l'investissement net.

**Implications pratiques**: La reconnaissance d'une créance de dividende ne doit pas être assimilée à elle seule à une couverture d'investissement net.

**Référence**:
 - ifric16 2

    >Hedge accounting of the **foreign currency risk arising from a net investment in a foreign operation** will apply only when the net assets of that foreign operation are included in the financial statements. 1 The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
 - ifric16 3

    >IFRS 9 requires the designation of an eligible hedged item and eligible hedging instruments in a hedge accounting relationship. If there is a designated hedging relationship, in the case of a net investment hedge, the gain or loss on the hedging instrument that is determined to be an **effective hedge of the net investment is recognised in other comprehensive income** and is included with the foreign exchange differences arising on translation of the results and financial position of the foreign operation.