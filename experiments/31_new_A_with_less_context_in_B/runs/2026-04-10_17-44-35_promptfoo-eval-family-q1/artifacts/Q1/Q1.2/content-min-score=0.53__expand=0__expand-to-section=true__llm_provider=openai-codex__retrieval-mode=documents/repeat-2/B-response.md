# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Identification of the hedge accounting models that could be documented in consolidated financial statements for the foreign exchange risk on an intragroup dividend recognised as a receivable

## Documentation
**Consultée**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été décidé et comptabilisé en créance au moment où l'on envisage la documentation de couverture.
   - La question porte sur les comptes consolidés du groupe, et non sur les comptes individuels ou séparés.
   - La créance de dividende est libellée dans une devise créant un risque de change entre deux entités du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la seule voie directement pertinente sur la créance de dividende déjà comptabilisée est la couverture de juste valeur, mais uniquement si la créance intragroupe entre dans l'exception IFRS 9 pour les éléments monétaires intragroupe dont l'effet de change n'est pas totalement éliminé. La couverture de flux de trésorerie n'est pas adaptée à une créance déjà reconnue, et la couverture d'investissement net vise une exposition différente.

## Points Opérationnels

   - Le point décisif en consolidation est de vérifier si la créance de dividende est un élément monétaire intragroupe générant des écarts de change non totalement éliminés.
   - Le moment de la documentation est essentiel : une fois la créance comptabilisée, la logique 'transaction prévue' n'est plus adaptée.
   - La documentation doit être rédigée au niveau consolidé, car la règle générale exclut les éléments intragroupe sauf exception expresse.
   - Si les deux entités ont des monnaies fonctionnelles différentes, cet élément factuel est central pour soutenir l'exception IFRS 9.
   - La couverture d'investissement net reste un modèle distinct, à réserver à une exposition de change sur investissement net et non au dividende intragroupe lui-même.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un élément monétaire intragroupe.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.<br>- Cette absence d'élimination provient d'entités du groupe ayant des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un élément monétaire intragroupe.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.
   - Cette absence d'élimination provient d'entités du groupe ayant des monnaies fonctionnelles différentes.

**Raisonnement**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance, donc on est face à un élément reconnu. En consolidation, un élément intragroupe n'est en principe pas éligible, sauf exception pour un élément monétaire intragroupe exposé à des écarts de change non totalement éliminés. Si cette créance de dividende produit un tel risque résiduel, une documentation de couverture de juste valeur sur la composante change peut être envisagée.

**Implications pratiques**: La documentation doit viser la composante change de la créance reconnue, au niveau des comptes consolidés.

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

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Dans les faits décrits, le dividende intragroupe n'est plus une transaction future hautement probable mais une créance déjà comptabilisée. Le modèle de couverture de flux de trésorerie vise des flux futurs ou des transactions prévues, ce qui ne correspond pas à cette situation au stade de reconnaissance en créance. L'exception IFRS 9 mentionne bien des transactions intragroupe prévues, mais pas une créance déjà reconnue.

**Implications pratiques**: Ce modèle n'est pas approprié pour documenter après comptabilisation de la créance de dividende.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction** or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette documentation ne couvre pas la créance de dividende en tant que telle, mais l'exposition de change liée à un investissement net dans une activité à l'étranger. Le fait qu'un dividende intragroupe soit comptabilisé en créance ne suffit pas, à lui seul, à transformer ce poste en investissement net couvert. Dans la situation posée, l'objet à couvrir est la partie change du dividende, pas l'investissement net.

**Implications pratiques**: Ce modèle ne doit pas être utilisé pour couvrir directement la créance de dividende intragroupe décrite.

**Référence**:
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency **the hedged risk is measured**, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, the total effective portion of the change is included in other comprehensive income. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.