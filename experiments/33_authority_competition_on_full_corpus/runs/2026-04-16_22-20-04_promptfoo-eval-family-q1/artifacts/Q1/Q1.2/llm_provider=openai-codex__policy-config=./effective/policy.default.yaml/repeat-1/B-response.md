# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Possibilités de documentation de couverture en comptes consolidés pour le risque de change lié à un dividende intragroupe comptabilisé en créance

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias21`, `ias7`, `ias27`, `ias12`, `ias24`, `ias38`, `ias19`, `ias40-bciasc`, `ias33`, `ias37`, `ias29`, `ias20`, `ias23`)
   - IFRIC (interpretation) (`ifric17`, `ifric2`, `ifric23`, `ifric19`)
   - IFRS-S (standard) (`ifrs19`, `ifrs17`, `ifrs9`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias32`, `ias21`, `ias27`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été décidé et comptabilisé en créance avant consolidation.
   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
   - La créance de dividende est libellée dans une devise différente de la devise fonctionnelle d'au moins une des entités concernées.
   - Aucune information n'indique que ce dividende fait partie d'une couverture d'investissement net déjà documentée.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change d'un dividende intragroupe n'est envisageable que de façon limitée. La voie la plus pertinente est la couverture de juste valeur de la créance monétaire reconnue, mais seulement si le risque de change n'est pas totalement éliminé en consolidation au sens d'IAS 21. La couverture de flux de trésorerie n'est pertinente que si la transaction est encore future, et la couverture d'investissement net ne vise pas ce dividende en tant que tel.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Les deux entités ont des devises fonctionnelles différentes.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - Aucune, dans la situation décrite. |
| 3. Couverture d'investissement net | NON | - Aucune, dans la situation décrite. |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Les deux entités ont des devises fonctionnelles différentes.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.

**Raisonnement**:
Dans cette situation, la créance de dividende déjà comptabilisée est un élément reconnu, ce qui entre dans le champ d'un élément couvert possible en couverture selon IFRS 9 6.3.1. En consolidation, un élément intragroupe n'est en principe pas éligible, sauf exception pour un élément monétaire intragroupe exposé à un risque de change non totalement éliminé; c'est précisément l'exception d'IFRS 9 6.3.6, articulée avec IAS 21 45. Donc la documentation est possible uniquement si la créance de dividende constitue bien un élément monétaire intragroupe entre entités à devises fonctionnelles différentes, générant un écart de change qui subsiste en consolidation.

**Implications pratiques**: La relation de couverture peut viser le risque de change de la créance reconnue en consolidation, avec comptabilisation cohérente des effets de change qui subsistent.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, [Refer: IFRS 10 paragraph B86]such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - Aucune, dans la situation décrite.

**Raisonnement**:
La question porte sur un dividende intragroupe déjà comptabilisé en créance; le fait générateur n'est donc plus une transaction future mais un actif reconnu. Or IFRS 9 6.3.1 distingue les transactions prévues des actifs reconnus, et IFRS 9 6.3.6 ne permet l'intragroupe en consolidation, pour ce modèle, que pour une transaction intragroupe hautement probable affectant le résultat consolidé. Sur les faits donnés, ce n'est pas le cas de la créance déjà enregistrée.

**Implications pratiques**: Ce modèle ne convient pas pour couvrir la partie change d'une créance de dividende déjà reconnue en consolidation.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]

### 3. Couverture d'investissement net

**Applicabilité**: NON

**Conditions**:
   - Aucune, dans la situation décrite.

**Raisonnement**:
IFRS 9 6.3.1 reconnaît la couverture d'un investissement net dans une activité à l'étranger comme un modèle distinct. Toutefois, la situation décrite vise la partie change d'un dividende intragroupe comptabilisé en créance, c'est-à-dire une créance spécifique, et non l'exposition de conversion liée à un investissement net. Sur ces faits, ce modèle ne correspond donc pas à l'objet couvert demandé.

**Implications pratiques**: La documentation ne doit pas être construite comme une couverture d'investissement net pour ce dividende intragroupe.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).