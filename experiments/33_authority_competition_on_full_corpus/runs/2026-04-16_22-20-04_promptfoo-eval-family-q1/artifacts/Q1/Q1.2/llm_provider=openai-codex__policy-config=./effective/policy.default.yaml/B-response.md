# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Possibilités de documentation de couverture en comptes consolidés pour le risque de change attaché à un dividende intragroupe (créance/dividende futur) et identification des modèles IFRS de comptabilité de couverture pertinents

## Documentation
**Consultée**
   - IAS-S (standard) (`ias32`, `ias21`, `ias7`, `ias27`, `ias12`, `ias24`, `ias38`, `ias19`, `ias40-bciasc`, `ias33`, `ias37`, `ias29`, `ias20`, `ias23`)
   - IFRIC (interpretation) (`ifric17`, `ifric2`, `ifric23`, `ifric19`)
   - IFRS-S (standard) (`ifrs19`, `ifrs17`, `ifrs9`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`, `ias27`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe a déjà été décidé et comptabilisé en créance dans les comptes individuels, donc il s'agit d'un poste monétaire libellé en devise.
   - La question porte sur les comptes consolidés du groupe, et la créance/dividende concerne deux entités du groupe ayant des monnaies fonctionnelles différentes.
   - Aucun fait n'indique que cette créance de dividende fasse partie d'un investissement net dans une activité à l'étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente est la documentation de couverture du poste monétaire intragroupe reconnu, donc le fair value hedge, si le risque de change n'est pas entièrement éliminé en consolidation au sens d'IAS 21. Le cash flow hedge ne vise pas un dividende déjà comptabilisé en créance, et la couverture d'investissement net n'est pas étayée par les faits donnés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe libellé dans une monnaie autre que la monnaie fonctionnelle de l'une des entités concernées.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation, conformément à IAS 21. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe libellé dans une monnaie autre que la monnaie fonctionnelle de l'une des entités concernées.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation, conformément à IAS 21.

**Raisonnement**:
Ici, le dividende intragroupe est déjà comptabilisé en créance : il s'agit donc d'un poste reconnu, et IFRS 9 permet de désigner comme élément couvert un actif ou passif reconnu (IFRS 9 6.3.1). En consolidation, l'exception pour les postes monétaires intragroupe ne vaut que si le risque de change crée des écarts non totalement éliminés selon IAS 21, ce qui vise précisément les entités du groupe à monnaies fonctionnelles différentes (IFRS 9 6.3.6; IAS 21 45). IAS 21 impose en outre la conversion des postes monétaires au cours de clôture, ce qui confirme que la composante change de la créance existe jusqu'au règlement (IAS 21 23).

**Implications pratiques**: La documentation de couverture en consolidation peut porter sur la composante change de la créance de dividende déjà reconnue, sous réserve que l'exposition de change subsiste au niveau consolidé.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]
 - ias21 23

    >At the end of each reporting period:
(a)foreign currency monetary items shall be translated using the closing rate ;
(b)non‑monetary items that are measured in terms of historical cost in a foreign currency shall be translated using the exchange rate at the date of the transaction [Refer: paragraph 22]; and
(c)non‑monetary items that are measured at fair value [Refer: IFRS 13]in a foreign currency shall be translated using the exchange rates at the date when the fair value was measured. E3
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, [Refer: IFRS 10 paragraph B86]such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise une transaction future hautement probable, non encore reconnue, alors qu'ici le dividende intragroupe a déjà été comptabilisé en créance. IFRS 9 exige qu'une transaction prévue soit hautement probable pour être un élément couvert (IFRS 9 6.3.3), et l'exception intragroupe en consolidation pour ce modèle vise aussi une transaction future intragroupe, non un receivable déjà enregistré (IFRS 9 6.3.6). Le fait générateur du dividende semble déjà consommé au regard de la reconnaissance de la créance (IAS 27 12).

**Implications pratiques**: Ce modèle n'est pas adapté à la partie change d'un dividende déjà reconnu en créance; il aurait été à envisager avant la reconnaissance, sur une transaction future hautement probable.

**Référence**:
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable. E19
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss. [Refer: paragraph B6.3.5]
 - ias27 12

    >Dividends from a subsidiary, a joint venture or an associate are recognised in the separate financial statements of an entity when the entity’s right to receive the dividend is established. The dividend is recognised in profit or loss unless the entity elects to use the equity method, in which case the dividend is recognised as a reduction from the carrying amount of the investment.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IFRS 9 reconnaît bien la couverture d'un investissement net comme modèle distinct de couverture (IFRS 9 6.3.1). Mais, dans les faits décrits, l'exposition identifiée est la partie change d'une créance de dividende intragroupe déjà comptabilisée, non un investissement net dans une activité à l'étranger. En l'absence d'éléments montrant que cette créance relève de cet investissement net, ce modèle ne s'applique pas à cette situation.

**Implications pratiques**: Cette documentation de couverture n'est pas appropriée pour traiter la composante change d'une créance de dividende intragroupe telle que décrite.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).