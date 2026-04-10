# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Reformulation**:
>Whether foreign exchange risk arising on an intragroup dividend receivable recognised in consolidated financial statements can be designated as a hedged item under IFRS hedge accounting.

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
   - Le dividende intragroupe a déjà été décidé et a donné lieu à la comptabilisation d'une créance intragroupe.
   - La question vise les comptes consolidés du groupe.
   - La créance de dividende est un élément monétaire libellé dans une devise étrangère par rapport à la monnaie fonctionnelle d'au moins une des entités concernées.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une créance intragroupe n'est en principe pas un élément couvert, sauf exception IFRS 9 pour le risque de change d'un élément monétaire intragroupe. L'éligibilité existe seulement si la variation de change n'est pas totalement éliminée en consolidation et affecte le résultat consolidé.

## Points Opérationnels

   - Le point décisif est le niveau de reporting: en comptes consolidés, la règle générale exclut l'intragroupe, avec une exception limitée au risque de change sur éléments monétaires intragroupe.
   - L'analyse doit être faite après constatation de la créance: à ce stade, on n'est plus dans une transaction future hautement probable.
   - Il faut démontrer que l'écart de change sur la créance de dividende n'est pas totalement éliminé en consolidation, typiquement en présence de monnaies fonctionnelles différentes.
   - Si cette condition n'est pas remplie, la désignation en comptabilité de couverture n'est pas éligible dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque couvert est uniquement le risque de change.<br>- Les gains ou pertes de change sur cette créance ne sont pas entièrement éliminés en consolidation.<br>- Cette variation de change affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque couvert est uniquement le risque de change.
   - Les gains ou pertes de change sur cette créance ne sont pas entièrement éliminés en consolidation.
   - Cette variation de change affecte le résultat consolidé.

**Raisonnement**:
Ici, il existe une créance intragroupe déjà comptabilisée, donc un élément reconnu pouvant relever en théorie d'une couverture. Mais en comptes consolidés, IFRS 9 exclut en principe les éléments intragroupe, sauf pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés en consolidation. C'est seulement dans ce cas précis que la créance de dividende peut être désignée.

**Implications pratiques**: Possible uniquement comme désignation ciblée du risque de change sur la créance reconnue, si l'exposition subsiste au niveau consolidé.

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
La situation décrite ne porte pas sur une transaction future hautement probable, mais sur un dividende intragroupe pour lequel une créance a déjà été constatée. Une fois la créance reconnue, l'exposition traitée est celle d'un élément monétaire existant, pas celle d'un flux futur encore prévu. Cette approche ne correspond donc pas aux faits décrits.

**Implications pratiques**: La désignation en cash flow hedge ne convient pas à une créance de dividende déjà comptabilisée.

**Référence**:
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable.
 - ifrs9 6.3.4

    >An aggregated exposure that is a combination of an exposure that could qualify as a hedged item in accordance with paragraph 6.3.1 and a derivative may be designated as a hedged item (see paragraphs B6.3.3⁠–⁠B6.3.4). **This includes a forecast transaction of an aggregated exposure** (ie uncommitted but anticipated future transactions that would give rise to an exposure and a derivative) if that aggregated exposure is highly probable and, once it has occurred and is therefore no longer forecast, is eligible as a hedged item.
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
La question vise la variation de change sur une créance de dividende intragroupe, non la couverture d'un investissement net dans une activité étrangère. Le modèle IAS 21/IFRIC 16 concerne les éléments monétaires faisant partie de l'investissement net et les effets cumulés en OCI jusqu'à la cession. Rien dans les faits décrits n'indique qu'une créance de dividende fasse partie d'un tel investissement net.

**Implications pratiques**: Le modèle de net investment hedge n'est pas celui à retenir pour une créance de dividende intragroupe ordinaire.

**Référence**:
 - ias21 32

    >Exchange differences arising on **a monetary item that forms part of a reporting entity’s net investment in a foreign operation** (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ias21 48

    >On the disposal of a foreign operation, the cumulative amount of the exchange differences relating to that foreign operation, recognised in other comprehensive income and accumulated in the separate component of equity, **shall be reclassified from equity to profit or loss** (as a reclassification adjustment) when the gain or loss on disposal is recognised (see IFRS 18 Presentation and Disclosure in Financial Statements).