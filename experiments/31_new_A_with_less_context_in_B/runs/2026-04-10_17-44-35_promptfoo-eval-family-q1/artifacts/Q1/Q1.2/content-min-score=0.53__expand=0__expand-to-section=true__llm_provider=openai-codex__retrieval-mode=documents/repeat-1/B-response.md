# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Identifying the hedge accounting models that could be documented in consolidated financial statements for the foreign exchange risk arising from an intragroup dividend receivable

## Documentation
**Consultée**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été reconnu en créance à la date considérée.
   - La question porte sur les comptes consolidés du groupe.
   - La créance de dividende est exposée à un risque de change intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie pertinente pour la créance déjà comptabilisée est la couverture de juste valeur, mais seulement si le risque de change de cette créance intragroupe n'est pas totalement éliminé à la consolidation. La couverture de flux de trésorerie ne vise pas une créance déjà reconnue, et la couverture d'investissement net ne vise pas ce dividende en tant que tel.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que le risque de change de la créance intragroupe n'est pas totalement éliminé.
   - Le niveau de reporting importe : un traitement admis en comptes individuels/séparés n'est pas automatiquement admis en comptes consolidés.
   - Le timing est structurant : une créance déjà reconnue renvoie au modèle de poste reconnu, pas au modèle de transaction future.
   - Si le groupe souhaite utiliser la comptabilité de couverture, la documentation doit être alignée sur l'exposition effectivement couverte en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Le risque de change sur cette créance n'est pas totalement éliminé en consolidation.<br>- Les entités concernées ont des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Le risque de change sur cette créance n'est pas totalement éliminé en consolidation.
   - Les entités concernées ont des monnaies fonctionnelles différentes.

**Raisonnement**:
Ici, le dividende est déjà comptabilisé en créance, donc il s'agit d'un poste monétaire reconnu. En consolidation, un poste intragroupe n'est éligible que par exception pour son risque de change si les écarts de change ne sont pas totalement éliminés, notamment entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation doit viser le risque de change de la créance reconnue, pas le dividende en tant que transaction interne éliminée.

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
Cette approche vise une transaction future prévue, en particulier une transaction intragroupe hautement probable répondant à l'exception IFRS 9. Or, dans votre cas, le dividende n'est plus une transaction future : il a déjà été comptabilisé en créance.

**Implications pratiques**: Cette documentation n'est pas adaptée pour couvrir la composante change d'une créance de dividende déjà reconnue.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions** with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le modèle IFRIC 16/IFRS 9 concerne la couverture d'un investissement net dans une activité étrangère au niveau du groupe. La question porte ici sur la composante change d'une créance de dividende intragroupe, qui n'est pas, en elle-même, l'investissement net couvert.

**Implications pratiques**: Ce modèle ne documente pas la créance de dividende ; il couvrirait une exposition différente, celle de l'investissement net.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment** in a foreign operation. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency **the hedged risk is measured**, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, the total effective portion of the change is included in other comprehensive income. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.