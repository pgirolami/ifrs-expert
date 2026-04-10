# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Reformulation**:
>Identification of the hedge accounting models that can be documented in consolidated financial statements for foreign exchange risk on an intragroup dividend receivable.

## Documentation
**Consultée**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe est déjà comptabilisé en créance à la date d'analyse.
   - La question vise les comptes consolidés du groupe.
   - La partie change concerne une créance intragroupe monétaire libellée dans une devise générant potentiellement des écarts de change en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change est envisageable principalement en couverture de juste valeur de la créance intragroupe, si l'écart de change n'est pas totalement éliminé en consolidation. La couverture de flux de trésorerie ne convient pas à une créance déjà comptabilisée, et la couverture d'investissement net relève d'un autre objet.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que l'écart de change sur la créance intragroupe n'est pas totalement éliminé.
   - Le choix du modèle dépend du moment de la désignation : après comptabilisation de la créance, la logique pertinente est celle d'un poste reconnu, non d'une transaction future.
   - La documentation doit être préparée au niveau consolidé, car la règle générale exclut les intragroupes sauf exception spécifique sur le risque de change.
   - Si l'exposition provient d'entités ayant des monnaies fonctionnelles différentes, l'exception IFRS 9 sur les éléments monétaires intragroupe devient le fondement technique principal.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit créer un écart de change non totalement éliminé en consolidation.<br>- L'exposition doit concerner le risque de change d'un élément monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit créer un écart de change non totalement éliminé en consolidation.
   - L'exposition doit concerner le risque de change d'un élément monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.

**Raisonnement**:
Ici, l'exposition porte sur une créance intragroupe déjà reconnue, donc sur un élément monétaire existant. En consolidation, IFRS 9 permet par exception de désigner le risque de change d'un élément monétaire intragroupe comme élément couvert si les gains/pertes de change ne sont pas entièrement éliminés, notamment lorsque les entités ont des monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation peut viser le risque de change de la créance reconnue en consolidation, sous réserve de l'exception intragroupe d'IFRS 9.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and **not in the consolidated financial statements of the group**, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise des transactions prévues, notamment des transactions intragroupe hautement probables dans des cas limités en consolidation. Or, dans la situation décrite, le dividende intragroupe a déjà été comptabilisé en créance ; l'exposition n'est donc plus une transaction future mais un poste monétaire reconnu.

**Implications pratiques**: Cette documentation n'est pas adaptée à la créance déjà enregistrée ; elle aurait visé l'étape antérieure de transaction future hautement probable.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, **a forecast transaction** or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of **a highly probable forecast intragroup transaction may qualify as a hedged item** in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.3.4

    >An aggregated exposure that is a combination of an exposure that could qualify as a hedged item in accordance with paragraph 6.3.1 and a derivative may be designated as a hedged item (see paragraphs B6.3.3⁠–⁠B6.3.4). **This includes a forecast transaction** of an aggregated exposure (ie uncommitted but anticipated future transactions that would give rise to an exposure and a derivative) if that aggregated exposure is highly probable and, once it has occurred and is therefore no longer forecast, is eligible as a hedged item.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le modèle IFRS 9 / IFRIC 16 vise la couverture d'un investissement net dans une activité à l'étranger au niveau du groupe. La situation décrite porte sur une créance de dividende intragroupe déjà comptabilisée ; ce n'est pas, sur les faits fournis, l'objet d'une relation de couverture d'investissement net.

**Implications pratiques**: Ce modèle ne répond pas à la couverture du risque de change d'une créance de dividende intragroupe en tant que telle.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or **a net investment in a foreign operation**. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency the hedged risk is measured, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, **the total effective portion of the change is included in other comprehensive income**. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.