# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Reformulation**:
>Possibilité d’appliquer une comptabilité de couverture en consolidation sur le risque de change d’un dividende intragroupe comptabilisé en créance

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias21`, `ias7`, `ias12`, `ias27`, `ias24`, `ias38`, `ias19`, `ias34`, `ias33`, `ias40-bciasc`, `ias37`, `ias29`, `ias23`)
   - IFRIC (interpretation) (`ifric17`, `ifric2`, `ifric23`, `ifric19`)
   - IFRS-S (standard) (`ifrs17`, `ifrs19`, `ifrs9`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été comptabilisé en créance dans les comptes individuels de l'entité prêteuse et constitue donc un élément monétaire en devise.
   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
   - Aucun fait n'indique que cette créance de dividende fait partie d'une couverture d'investissement net dans une activité à l'étranger.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change est envisageable principalement sur la créance intragroupe déjà comptabilisée, mais seulement si elle crée un risque de change non totalement éliminé en consolidation. Sur les faits donnés, l'approche pertinente est la fair value hedge; les deux autres ne s'appliquent pas sauf faits additionnels différents.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance et la dette intragroupe correspondante sont entre des entités du groupe ayant des monnaies fonctionnelles différentes.<br>- Le risque de change sur cette créance intragroupe affecte le résultat consolidé car il n'est pas totalement éliminé en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance et la dette intragroupe correspondante sont entre des entités du groupe ayant des monnaies fonctionnelles différentes.
   - Le risque de change sur cette créance intragroupe affecte le résultat consolidé car il n'est pas totalement éliminé en consolidation.

**Raisonnement**:
La créance de dividende déjà comptabilisée est, dans les faits décrits, un élément monétaire en devise qui entre dans la catégorie des actifs reconnus pouvant être désignés comme élément couvert (IFRS 9 6.3.1). En consolidation, l'exception pour un poste monétaire intragroupe ne joue que si le risque de change génère des gains/pertes non totalement éliminés, ce qui suppose des monnaies fonctionnelles différentes entre entités du groupe (IFRS 9 6.3.6; IAS 21 45).

**Implications pratiques**: La documentation de couverture peut viser le risque de change de la créance de dividende intragroupe dans les comptes consolidés si l'exposition subsiste au niveau consolidé.

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
   - (conditions non spécifiées)

**Raisonnement**:
Dans la situation décrite, le dividende intragroupe n'est plus une transaction future: il a déjà été comptabilisé en créance. Or IFRS 9 réserve ce terrain aux transactions prévues hautement probables, y compris certaines transactions intragroupe futures en devise affectant le résultat consolidé (IFRS 9 6.3.3 et 6.3.6).

**Implications pratiques**: Cette voie ne convient pas à une créance de dividende déjà reconnue; elle viserait plutôt un dividende intragroupe futur encore non comptabilisé.

**Référence**:
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable. E19
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IFRS 9 reconnaît la couverture d'un investissement net comme modèle distinct (IFRS 9 6.3.1), mais les faits fournis portent seulement sur une créance de dividende intragroupe comptabilisée. Rien n'indique ici que l'exposition visée soit l'investissement net dans une activité étrangère plutôt qu'un simple poste monétaire intragroupe traité par IAS 21 45.

**Implications pratiques**: Sur les faits donnés, cette documentation ne correspond pas à l'objet économique décrit.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, [Refer: IFRS 10 paragraph B86]such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.