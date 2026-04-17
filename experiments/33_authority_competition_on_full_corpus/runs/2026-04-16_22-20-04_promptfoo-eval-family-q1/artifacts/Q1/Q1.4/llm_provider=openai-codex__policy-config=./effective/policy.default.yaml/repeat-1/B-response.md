# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Reformulation**:
>Éligibilité, en comptes consolidés, d’un dividende intragroupe / de la créance intragroupe correspondante comme élément couvert au titre du risque de change dans une relation de couverture

## Documentation
**Consultée**
   - IAS-S (standard) (`ias21`, `ias12`, `ias7`, `ias39`, `ias32`, `ias24`, `ias37`, `ias27`, `ias40-bciasc`, `ias34`, `ias33`, `ias29`, `ias38`)
   - IFRIC (interpretation) (`ifric17`, `ifric16`, `ifric2`, `ifric23`)
   - IFRS-S (standard) (`ifrs10`, `ifrs12`, `ifrs19`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`, `ias39`)
   - IFRIC (interpretation) (`ifric16`)

## Hypothèses
   - Le dividende intragroupe a été déclaré et une créance intragroupe correspondante a déjà été comptabilisée à la date de la documentation de couverture.
   - La question porte sur des comptes consolidés du groupe, et non sur des comptes individuels ou séparés.
   - La créance et la dette intragroupe correspondante sont libellées dans une devise créant un risque de change en consolidation.
   - Aucune analyse n’est faite ici des autres critères de documentation et d’efficacité de la relation de couverture, hors éligibilité de l’élément couvert.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture peut viser le risque de change de la créance intragroupe reconnue seulement si cette créance est un élément monétaire intragroupe entre entités de monnaies fonctionnelles différentes et si l’écart de change n’est pas totalement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’un investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende et la dette correspondante constituent un poste monétaire intragroupe.<br>- Les deux entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende et la dette correspondante constituent un poste monétaire intragroupe.
   - Les deux entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.

**Raisonnement**:
Dans cette situation, la créance de dividende déjà reconnue est un poste comptabilisé; IAS 39 78 admet qu’un élément couvert puisse être un actif ou passif comptabilisé. En consolidation, IAS 39 80 prévoit une exception pour le risque de change d’un élément monétaire intragroupe si l’exposition aux gains ou pertes de change n’est pas totalement éliminée; IAS 21 45 précise que c’est le cas pour un poste monétaire intragroupe entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation de couverture en consolidation peut porter sur la composante change de la créance intragroupe reconnue si les écarts de change subsistent au niveau consolidé.

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
Cette approche vise notamment une transaction future hautement probable, comme le rappelle IAS 39 78, et IAS 39 80 admet à titre d’exception certaines transactions intragroupe futures hautement probables. Or, dans la situation décrite, le dividende a déjà donné lieu à une créance reconnue; l’exposition n’est donc plus une transaction future mais un poste comptabilisé.

**Implications pratiques**: Une fois la créance de dividende comptabilisée, la qualification pertinente n’est plus une couverture de flux de trésorerie du dividende intragroupe.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ias39 80

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions that involve a party external to the entity can be designated as hedged items. It follows that hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements. As an exception, the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d’un investissement net dans une activité à l’étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question vise la composante change d’un dividende intragroupe / d’une créance intragroupe reconnue, et non le risque de change attaché à un investissement net dans une activité à l’étranger. IFRIC 16 8 précise que son champ est limité aux couvertures d’investissements nets et ne doit pas être appliqué par analogie à d’autres types de couverture; IAS 39 78 traite cette couverture comme un modèle distinct.

**Implications pratiques**: Le modèle de couverture d’investissement net n’est pas la base appropriée pour documenter le change sur une créance de dividende intragroupe reconnue.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ifric16 8

    >This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting.