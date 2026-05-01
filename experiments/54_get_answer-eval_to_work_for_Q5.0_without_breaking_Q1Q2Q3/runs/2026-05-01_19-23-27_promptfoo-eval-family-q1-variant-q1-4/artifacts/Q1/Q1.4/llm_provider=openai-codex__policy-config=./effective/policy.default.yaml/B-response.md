# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Reformulation**:
>Détermination, en comptes consolidés, du modèle de comptabilité de couverture IFRS potentiellement applicable à la composante change de dividendes intragroupe, selon que l’élément couvert est une transaction intragroupe prévue ou une créance intragroupe reconnue.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`, `ifrs7`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe est libellé dans une devise autre que la monnaie fonctionnelle d’au moins une des entités concernées.
   - La créance de dividende reconnue est un élément monétaire intragroupe encore existant à la date de désignation en comptes consolidés.
   - Cette créance ne fait pas partie d’un investissement net dans une activité à l’étranger au sens d’IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, une documentation de couverture peut viser la composante change d’une créance intragroupe reconnue si cette créance monétaire crée un risque de change non intégralement éliminé en consolidation entre entités à monnaies fonctionnelles différentes (IFRS 9 6.3.6; IAS 21 45). Dans ce cas, le modèle pertinent est la fair value hedge; le cash flow hedge vise plutôt une transaction intragroupe prévue, et la net investment hedge n’est pertinente que si l’élément relève d’un investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un élément monétaire exposé à un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance doivent ne pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un élément monétaire exposé à un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance doivent ne pas être totalement éliminés en consolidation.

**Raisonnement**:
Dans la situation décrite, la créance de dividende déjà comptabilisée est un actif reconnu; IFRS 9 6.5.2(a) vise précisément un actif ou passif reconnu exposé à un risque pouvant affecter le résultat. En consolidation, l’exception d’IFRS 9 6.3.6 permet de désigner le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés; IAS 21 45 confirme que ces écarts subsistent pour des entités du groupe ayant des monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation de couverture en consolidation peut porter sur la composante change de la créance reconnue, sous le modèle de couverture de juste valeur.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.5.2

    >There are three types of hedging relationships:
(a)fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.
(b)cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.
(c)hedge of a net investment in a foreign operation as defined in IAS 21.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur un dividende intragroupe dès lors qu’une créance correspondante a été reconnue; à ce stade, il ne s’agit plus d’une transaction future hautement probable mais d’un actif déjà comptabilisé. IFRS 9 6.5.2(b) réserve la cash flow hedge à la variabilité de flux d’un actif/passif ou d’une transaction prévue, et IFRS 9 6.3.6 ne vise les transactions intragroupe prévues qu’avant leur comptabilisation.

**Implications pratiques**: Une fois la créance de dividende reconnue, la couverture de flux de trésorerie n’est pas le modèle adapté en consolidation pour cette situation.

**Référence**:
 - ifrs9 6.5.2

    >There are three types of hedging relationships:
(a)fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.
(b)cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.
(c)hedge of a net investment in a foreign operation as defined in IAS 21.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d’un investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le modèle de net investment hedge ne s’applique qu’aux expositions de change liées à un investissement net dans une activité à l’étranger. IFRS 9 6.5.2(c) renvoie à IAS 21, et IAS 21 32-33 ainsi qu’IFRIC 16 10 limitent ce modèle aux éléments monétaires faisant partie de l’investissement net; une créance de dividende intragroupe reconnue n’entre pas dans ce cadre selon les faits décrits.

**Implications pratiques**: La créance de dividende reconnue ne doit pas être documentée comme couverture d’un investissement net, sauf si elle faisait partie d’un investissement net au sens strict d’IAS 21.

**Référence**:
 - ifrs9 6.5.2

    >There are three types of hedging relationships:
(a)fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.
(b)cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.
(c)hedge of a net investment in a foreign operation as defined in IAS 21.
 - ias21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ias21 33

    >When a monetary item forms part of a reporting entity’s net investment in a foreign operation and is denominated in the functional currency of the reporting entity, an exchange difference arises in the foreign operation’s individual financial statements in accordance with paragraph 28. If such an item is denominated in the functional currency of the foreign operation, an exchange difference arises in the reporting entity’s separate financial statements in accordance with paragraph 28. If such an item is denominated in a currency other than the functional currency of either the reporting entity or the foreign operation, an exchange difference arises in the reporting entity’s separate financial statements and in the foreign operation’s individual financial statements in accordance with paragraph 28. Such exchange differences are recognised in other comprehensive income in the financial statements that include the foreign operation and the reporting entity (ie financial statements in which the foreign operation is consolidated or accounted for using the equity method).
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.