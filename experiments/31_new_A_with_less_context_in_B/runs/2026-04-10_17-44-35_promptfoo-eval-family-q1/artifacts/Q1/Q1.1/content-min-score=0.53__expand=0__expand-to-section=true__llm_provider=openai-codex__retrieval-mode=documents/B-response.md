# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Reformulation**:
>Which IFRS hedge accounting models can be documented in consolidated financial statements for foreign exchange risk arising from an intragroup dividend receivable.

## Documentation
**Consultée**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs18`, `ifrs9`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`, `ifrs18`)

## Hypothèses
   - Le dividende intragroupe a été constaté en créance avant la date de clôture et la question vise les comptes consolidés.
   - La créance de dividende est libellée dans une devise autre que la monnaie fonctionnelle d'au moins une des entités concernées.
   - Aucun autre fait n'indique que la créance de dividende ferait partie d'une relation de couverture d'un investissement net dans une activité à l'étranger.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change n'est envisageable ici que de manière ciblée, principalement via une couverture de juste valeur, si la créance intragroupe constitue un élément monétaire dont l'effet de change n'est pas totalement éliminé en consolidation. La couverture de flux de trésorerie n'est en principe pas adaptée à une créance déjà comptabilisée, et la couverture d'investissement net ne convient que si le risque couvert est celui d'un investissement net, non celui du dividende.

## Points Opérationnels

   - Le test clé en consolidation est de vérifier si la créance de dividende est un élément monétaire intragroupe et si son effet de change n'est pas totalement éliminé.
   - Comme la créance est déjà comptabilisée, l'analyse doit être faite à la date de reconnaissance et à la clôture, pas comme une transaction future.
   - Si un dérivé est désigné en couverture, IFRS 18 impose de classer ses gains et pertes dans la même catégorie que l'élément couvert ; à défaut, un risque de classement en opérationnel existe.
   - Même hors désignation formelle, IFRS 18 prévoit un traitement de présentation pour un dérivé utilisé pour gérer un risque identifié, sous réserve des contraintes de gross-up ou d'effort excessif.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un élément monétaire intragroupe exposé au risque de change.<br>- Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un élément monétaire intragroupe exposé au risque de change.
   - Les gains ou pertes de change correspondants ne doivent pas être totalement éliminés en consolidation.

**Raisonnement**:
La créance de dividende est déjà comptabilisée, ce qui cadre avec un modèle de couverture portant sur un élément existant. En consolidation, IFRS 9 exclut en principe les éléments intragroupe, sauf pour le risque de change d'un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés ; c'est le point décisif ici.

**Implications pratiques**: Si ces conditions sont remplies, la documentation peut viser le risque de change de la créance en consolidation via une relation de couverture formelle.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and **not in the consolidated financial statements** of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset** or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Dans la situation décrite, le dividende intragroupe n'est plus une transaction future hautement probable : il a déjà été comptabilisé en créance. Le modèle de cash flow hedge vise plutôt des flux futurs ou transactions prévues ; sur ces faits, ce n'est pas la qualification naturelle de l'exposition.

**Implications pratiques**: Ce modèle ne paraît pas approprié pour couvrir la partie change d'une créance de dividende déjà reconnue.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur la partie change d'une créance de dividende intragroupe, non sur le risque de conversion attaché à un investissement net dans une activité à l'étranger. IFRIC 16 traite d'un modèle distinct, centré sur l'investissement net du groupe, ce qui ne correspond pas aux faits exposés.

**Implications pratiques**: Cette documentation n'est pas adaptée si l'objet couvert est uniquement la créance de dividende intragroupe.

**Référence**:
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency the hedged risk is measured, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, **the total effective portion of the change is included in other comprehensive income**. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.