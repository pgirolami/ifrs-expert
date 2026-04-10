# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Which hedge accounting models can be documented in consolidated financial statements for the foreign exchange risk arising from an intragroup dividend receivable.

## Documentation
**Consultée**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été comptabilisé en créance au moment considéré.
   - La question vise les comptes consolidés du groupe.
   - La couverture recherchée porte uniquement sur le risque de change attaché à cette créance de dividende intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la créance de dividende intragroupe ne peut pas, en principe, être désignée comme élément couvert car elle est intragroupe. Une documentation de couverture n'est envisageable que dans les cas expressément admis : exposition de change intragroupe non totalement éliminée, couverture en amont d'une transaction intragroupe hautement probable, ou couverture d'un investissement net.

## Points Opérationnels

   - En consolidation, le point de départ est l'interdiction des éléments couverts intragroupe, avec exceptions limitées pour certains risques de change.
   - Si la créance de dividende est déjà comptabilisée, l'analyse pertinente est d'abord celle de l'élément monétaire intragroupe et de la non-élimination complète des écarts de change.
   - Si la couverture est envisagée avant comptabilisation, la documentation doit viser la transaction intragroupe hautement probable et non la créance ultérieure.
   - La couverture d'investissement net relève d'un objectif différent : elle ne remplace pas une couverture de la créance de dividende prise isolément.
   - La documentation doit être alignée sur le niveau de reporting concerné, ici les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un élément monétaire intragroupe.<br>- Les gains ou pertes de change liés à cette créance ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La documentation doit porter sur un dividende intragroupe hautement probable avant comptabilisation de la créance.<br>- Le dividende doit être libellé dans une devise autre que la monnaie fonctionnelle de l'entité qui entre dans la transaction.<br>- Le risque de change doit affecter le résultat consolidé. |
| 3. Couverture d'un investissement net dans une activité à l'étranger | OUI SOUS CONDITIONS | - L'élément couvert documenté doit être l'investissement net dans une activité à l'étranger, pas la créance de dividende elle-même.<br>- La stratégie, la désignation, la documentation et l'efficacité de la couverture doivent être établies au niveau du groupe. |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un élément monétaire intragroupe.
   - Les gains ou pertes de change liés à cette créance ne doivent pas être totalement éliminés en consolidation.

**Raisonnement**:
Une créance reconnue peut en principe être un élément couvert. Mais en comptes consolidés, IFRS 9 exclut les postes intragroupe, sauf exception pour le risque de change d'un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation. Donc, pour ce dividende mis en créance, cela n'est possible que s'il s'agit d'un poste monétaire intragroupe générant encore un risque de change au niveau consolidé.

**Implications pratiques**: Documenter la couverture au niveau consolidé uniquement sur la composante change qui subsiste effectivement après consolidation.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity** can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 2. Couverture de flux de trésorerie

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La documentation doit porter sur un dividende intragroupe hautement probable avant comptabilisation de la créance.
   - Le dividende doit être libellé dans une devise autre que la monnaie fonctionnelle de l'entité qui entre dans la transaction.
   - Le risque de change doit affecter le résultat consolidé.

**Raisonnement**:
Cette approche ne vise pas la créance déjà comptabilisée, mais la transaction future avant sa comptabilisation. IFRS 9 permet exceptionnellement en consolidation de couvrir le risque de change d'une transaction intragroupe hautement probable si elle est libellée dans une devise autre que la monnaie fonctionnelle de l'entité qui la conclut et si ce risque affectera le résultat consolidé. Donc elle n'est pertinente ici que si la documentation est positionnée sur le dividende intragroupe futur, pas sur la créance existante.

**Implications pratiques**: Approche utilisable en amont de la mise en créance, pas comme désignation de la créance déjà reconnue.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item** in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'élément couvert documenté doit être l'investissement net dans une activité à l'étranger, pas la créance de dividende elle-même.
   - La stratégie, la désignation, la documentation et l'efficacité de la couverture doivent être établies au niveau du groupe.

**Raisonnement**:
Cette documentation ne couvre pas la créance de dividende en tant que telle, mais un investissement net dans une activité à l'étranger. IFRS 9 admet un investissement net comme élément couvert et IFRIC 16 précise qu'un instrument de couverture peut être détenu par toute entité du groupe. Donc cette voie n'est pertinente que si le dividende s'inscrit dans une stratégie de couverture du risque de change de l'investissement net, et non de la créance intragroupe isolée.

**Implications pratiques**: Utiliser ce modèle seulement si l'objectif économique est la couverture de l'investissement net de la filiale étrangère.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency **the hedged risk is measured**, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, the total effective portion of the change is included in other comprehensive income. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.