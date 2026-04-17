# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Reformulation**:
>Éligibilité, dans les comptes consolidés, du risque de change lié à un dividende intragroupe / à une créance intragroupe comme élément couvert dans une relation de comptabilité de couverture

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias21`, `ias32`, `ias12`, `ias24`, `ias7`, `ias33`, `ias40-bciasc`, `ias27`, `ias37`, `ias19`, `ias29`, `ias38`)
   - IFRIC (interpretation) (`ifric17`, `ifric16`, `ifric2`)
   - IFRS-S (standard) (`ifrs17`, `ifrs19`, `ifrs7`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias39`, `ias21`)
   - IFRIC (interpretation) (`ifric16`)

## Hypothèses
   - La question vise les comptes consolidés du groupe, et non les comptes individuels ou séparés.
   - Le dividende intragroupe a déjà été décidé et a donné lieu à la comptabilisation d'une créance intragroupe à recevoir.
   - La créance et la dette correspondante sont libellées dans une devise créant un risque de change au niveau consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, un dividende intragroupe donnant lieu à une créance n'est en principe pas éligible, car les éléments intragroupe sont éliminés. Toutefois, l'exception d'IAS 39.80 permet la désignation du risque de change d'un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un élément monétaire intragroupe.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance doivent ne pas être totalement éliminés en consolidation et affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un élément monétaire intragroupe.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance doivent ne pas être totalement éliminés en consolidation et affecter le résultat consolidé.

**Raisonnement**:
La créance sur dividende est un actif comptabilisé, catégorie visée par IAS 39.78. Mais en comptes consolidés, un élément intragroupe n'est normalement pas éligible ; l'exception d'IAS 39.80 ne joue que pour le risque de change d'un élément monétaire intragroupe lorsque les gains ou pertes de change ne sont pas totalement éliminés. IAS 21.45 confirme qu'un actif/passif monétaire intragroupe entre entités à devises fonctionnelles différentes peut laisser subsister un effet de change dans le résultat consolidé.

**Implications pratiques**: Possible en consolidation seulement si la créance de dividende entre dans l'exception des éléments monétaires intragroupe exposés au risque de change résiduel.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ias39 80

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions that involve a party external to the entity can be designated as hedged items. It follows that hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements. As an exception, the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, [Refer: IFRS 10 paragraph B86]such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise une transaction future hautement probable au sens d'IAS 39.78. Or la question porte sur des dividendes intragroupe ayant déjà donné lieu à la comptabilisation d'une créance à recevoir ; le fait générateur n'est donc plus un flux futur non comptabilisé mais un actif intragroupe déjà reconnu. L'exception d'IAS 39.80 pour les transactions intragroupe hautement probables ne correspond pas à cette situation.

**Implications pratiques**: La relation ne doit pas être structurée comme une couverture de flux de trésorerie si la créance de dividende est déjà comptabilisée.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ias39 80

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions that involve a party external to the entity can be designated as hedged items. It follows that hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements. As an exception, the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question vise le risque de change d'un dividende intragroupe et d'une créance correspondante, non le risque de change d'un investissement net dans une activité à l'étranger. IFRIC 16.2, 10 et 12 circonscrivent cette approche à la couverture des différences de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la société mère sur les actifs nets de l'activité étrangère. Ce modèle ne correspond donc pas au cas d'une créance de dividende intragroupe.

**Implications pratiques**: La documentation ne doit pas qualifier ce risque comme couverture d'investissement net.

**Référence**:
 - ifric16 2

    >**Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation will apply only when the net assets of that foreign operation are included in the financial statements. 1 The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.**
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - ifric16 12

    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity (the immediate, intermediate or ultimate parent entity) of that foreign operation. The fact that the net investment is held through an intermediate parent does not affect the nature of the economic risk arising from the foreign currency exposure to the ultimate parent entity.