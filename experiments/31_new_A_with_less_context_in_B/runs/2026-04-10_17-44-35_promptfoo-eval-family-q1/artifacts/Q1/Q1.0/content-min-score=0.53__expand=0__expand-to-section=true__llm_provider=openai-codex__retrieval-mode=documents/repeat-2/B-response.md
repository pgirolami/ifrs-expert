# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Reformulation**:
>Whether foreign exchange risk on an intragroup dividend receivable recognised in the consolidated financial statements can be designated in a hedge accounting relationship, and which IFRS hedge accounting models are the relevant peer models.

## Documentation
**Consultée**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et une créance/dividende à recevoir a été comptabilisée avant la date de clôture.
   - La question porte sur les comptes consolidés du groupe, et non sur les comptes individuels ou séparés.
   - La documentation de couverture viserait uniquement le risque de change attaché à cette créance intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une couverture du risque de change sur un élément monétaire intragroupe reconnu si ce risque n'est pas totalement éliminé en consolidation. En revanche, une couverture de flux de trésorerie n'est pas adaptée ici et la couverture d'investissement net ne vise pas ce type d'exposition.

## Points Opérationnels

   - Le point clé est le niveau de reporting : en comptes consolidés, l'exception IFRS 9 ne joue que pour le risque de change sur un élément monétaire intragroupe non totalement éliminé.
   - Le timing est déterminant : dès lors qu'une créance de dividende est comptabilisée, l'analyse relève d'un élément reconnu et non d'une transaction future.
   - La documentation doit circonscrire le risque couvert à la seule composante change de la créance intragroupe.
   - Si les écarts de change sont totalement éliminés en consolidation, la désignation comme élément couvert ne fonctionne pas dans cette situation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un élément monétaire intragroupe.<br>- Le risque de change doit générer des écarts non totalement éliminés en consolidation.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un élément monétaire intragroupe.
   - Le risque de change doit générer des écarts non totalement éliminés en consolidation.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.

**Raisonnement**:
Ici, la question vise une créance intragroupe déjà comptabilisée, donc un élément reconnu. En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés, notamment entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation peut être mise en place en consolidation uniquement sur la composante change résiduelle de la créance intragroupe reconnue.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise une transaction future prévue et hautement probable. Or, dans votre cas, une créance à recevoir a déjà été comptabilisée sur le dividende intragroupe, donc l'exposition décrite n'est plus une transaction future mais un élément reconnu.

**Implications pratiques**: Cette voie n'est pas la bonne pour un dividende déjà constaté en créance dans les comptes consolidés.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions** with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of **a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IFRIC 16 traite du risque de change provenant d'un investissement net dans une activité étrangère, mesuré entre la monnaie fonctionnelle de l'activité étrangère et celle du parent. Un dividende intragroupe comptabilisé en créance constitue une exposition distincte sur un poste intragroupe, et non le risque de conversion de l'investissement net lui-même.

**Implications pratiques**: La couverture d'investissement net ne doit pas être utilisée pour documenter le change d'une créance de dividende intragroupe reconnue.

**Référence**:
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
 - ifric16 11

    >In a hedge of the foreign currency risks arising from a net investment in a foreign operation, **the hedged item can be an amount of net assets** equal to or less than the carrying amount of the net assets of the foreign operation in the consolidated financial statements of the parent entity. The carrying amount of the net assets of a foreign operation that may be designated as the hedged item in the consolidated financial statements of a parent depends on whether any lower level parent of the foreign operation has applied hedge accounting for all or part of the net assets of that foreign operation and that accounting has been maintained in the parent’s consolidated financial statements.
 - ifric16 12

    >**The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation** and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.