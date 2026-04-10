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
   - Le dividende intragroupe est libellé dans une devise différente de la monnaie fonctionnelle d'au moins une des entités concernées.
   - La créance de dividende est un poste monétaire reconnu avant éliminations de consolidation.
   - La question vise les comptes consolidés et la couverture du risque de change attaché à cette créance intragroupe déjà comptabilisée.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente est la couverture de juste valeur du risque de change sur un poste monétaire intragroupe reconnu, mais seulement si l'écart de change n'est pas totalement éliminé en consolidation. La couverture de flux de trésorerie ne vise pas une créance déjà comptabilisée et la couverture d'investissement net répond à un risque différent.

## Points Opérationnels

   - Le point clé en consolidation est de vérifier si l'écart de change sur la créance intragroupe est ou non totalement éliminé.
   - Le fait que le dividende soit déjà comptabilisé oriente l'analyse vers un poste reconnu, et non vers une transaction future hautement probable.
   - Si un instrument de couverture est désigné, IFRS 18 impose ensuite de classer ses gains et pertes dans la même catégorie que les éléments affectés par le risque couvert, sous réserve des règles de gross-up.
   - La documentation de couverture doit donc être alignée sur le niveau de reporting consolidé et sur le risque effectivement conservé après éliminations.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit créer en consolidation une exposition de change non totalement éliminée.<br>- L'exposition doit porter sur le risque de change d'un poste monétaire reconnu. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit créer en consolidation une exposition de change non totalement éliminée.
   - L'exposition doit porter sur le risque de change d'un poste monétaire reconnu.

**Raisonnement**:
La créance de dividende déjà comptabilisée est, dans les faits décrits, un élément reconnu. IFRS 9 permet une désignation en couverture sur un poste intragroupe en consolidation uniquement pour le risque de change d'un poste monétaire intragroupe qui génère des écarts de change non totalement éliminés en consolidation. Si cette condition est remplie, cette approche peut documenter la partie change de la créance.

**Implications pratiques**: C'est l'approche à retenir si la créance de dividende reste source d'écarts de change en consolidation.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs18 B70

    >Paragraph 47 requires an entity to classify income and expenses in categories in the statement of profit or loss. To apply paragraph 47, an entity shall classify gains and losses included in the statement of profit or loss on a financial instrument designated as a hedging instrument applying IFRS 9 in the same category as the income and expenses affected by the risks the financial instrument is used to manage. However, if doing so would require the grossing up of gains and losses, an entity shall classify all such gains and losses in the operating category (see paragraphs B74⁠–⁠B75).

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise une transaction future hautement probable. Or, dans la situation donnée, le dividende intragroupe a déjà été comptabilisé en créance, donc le risque porte sur un poste reconnu et non sur un flux futur encore non comptabilisé. La base IFRS fournie sur les transactions intragroupe hautement probables ne correspond donc pas au fait décrit.

**Implications pratiques**: Cette documentation n'est pas adaptée à la créance de dividende déjà enregistrée.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item** in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche couvre le risque de change d'un investissement net dans une activité à l'étranger, pas le risque de change d'une créance de dividende intragroupe déjà comptabilisée. Les textes fournis sur IFRIC 16 traitent de l'instrument de couverture et de son portage dans le groupe, mais ne requalifient pas une créance de dividende en investissement net couvert.

**Implications pratiques**: À écarter ici, sauf si l'objectif de couverture porte en réalité sur l'investissement net lui-même, ce qui n'est pas le cas décrit.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency the hedged risk is measured, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, **the total effective portion of the change is included in other comprehensive income**. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.