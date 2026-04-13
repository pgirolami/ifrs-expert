# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Hedge accounting for foreign exchange risk on an intragroup dividend receivable recognized in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs17`, `ifrs12`, `ifrs9`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IAS (`ias7`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - Le dividende intragroupe est comptabilisé en créance dans les comptes consolidés
   - Les deux entités ont des devises fonctionnelles différentes
   - Le risque de change n'est pas éliminé à la consolidation car les devises fonctionnelles diffèrent
   - Le contexte est celui des états financiers consolidés d'un groupe

## Recommandation

**OUI SOUS CONDITIONS**

L'approche 3 (couverture d'investissement net) est la plus adaptée si les conditions d'IFRIC 16 sont remplies. L'approche 2 (couverture en juste valeur) est également possible via l'exception d'IFRS 9 §6.3.6. L'approche 1 est le traitement de base sans couverture.

## Points Opérationnels

   - Documenter dès l'origine la relation de couverture avec désignation explicite du risque de change couvert
   - S'assurer que l'instrument de couverture (dérivé ou non-dérivé) est détenu par une entité appropriée du groupe
   - Mettre en place un processus de测试 d'efficacité à chaque période de reporting
   - En cas de couverture d'investissement net (approche 3), la portion efficace est recyclée en OCI et la portion inefficace en résultat
   - Les flux de trésorerie liés aux dividendes sont présentés en activités de financement selon IAS 7 §33A


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Reconnaissance directe des effets de change sans comptabilité de couverture | NON | - (non spécifiées) |
| 2. Couverture en juste valeur du risque de change sur la créance de dividende | OUI SOUS CONDITIONS | - Les entités ont des devises fonctionnelles différentes<br>- Le risque de change sur la créance n'est pas éliminé à la consolidation<br>- L'exposition affectera le résultat consolidé<br>- La documentation satisfies aux exigences d'IFRS 9 §6.4.1 |
| 3. Couverture d'investissement net dans une opération étrangère | OUI SOUS CONDITIONS | - Le dividende est reçu d'une filiale étrangère (investissement net dans une opération étrangère)<br>- La transaction est libellée dans une devise autre que la devise fonctionnelle de l'entité qui reçoit le dividende<br>- Le risque de change affectera le résultat consolidé<br>- La stratégie de couverture est clairement documentée conformément à IFRS 9 §6.4.1<br>- L'instrument de couverture peut être détenu par n'importe quelle entité du groupe |

### 1. Reconnaissance directe des effets de change sans comptabilité de couverture

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche représente le traitement de base par défaut selon IAS 21, mais la question porte spécifiquement sur l'application d'une documentation de couverture, ce qui exclut cette option comme réponse à la question posée.

**Implications pratiques**: Les différences de change sur la créance de dividende sont reconnues directement en résultat sans mécanisme de couverture.

**Référence**:
 - ias21 général

    >Les différences de change sur les éléments monétaires sont généralement reconnues en résultat.

### 2. Couverture en juste valeur du risque de change sur la créance de dividende

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les entités ont des devises fonctionnelles différentes
   - Le risque de change sur la créance n'est pas éliminé à la consolidation
   - L'exposition affectera le résultat consolidé
   - La documentation satisfies aux exigences d'IFRS 9 §6.4.1

**Raisonnement**:
IFRS 9 §6.3.6 permet de désigner le risque de change d'un élément monétaire intragroupe comme élément couvert dans les états consolidés, à condition que l'exposition aux gains ou pertes de change ne soit pas éliminée à la consolidation (IAS 21). Ici, les devises fonctionnelles différentes créent une telle exposition.

**Implications pratiques**: La variation de juste valeur attribuable au risque de change peut être reconnue en résultat, compensant partiellement la variation de la créance.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 5.7.1

    >**A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss** unless:
(a)it is part of a hedging relationship (see paragraphs 6.5.8⁠–⁠6.5.14 and, if applicable, paragraphs 89⁠–⁠94 of IAS 39 for the fair value hedge accounting for a portfolio hedge of interest rate risk);
(b)it is an investment in an equity instrument and the entity has elected to present gains and losses on that investment in other comprehensive income in accordance with paragraph 5.7.5;
(c)it is a financial liability designated as at fair value through profit or loss and the entity is required to present the effects of changes in the liability’s credit risk in other comprehensive income in accordance with paragraph 5.7.7; or
(d)it is a financial asset measured at fair value through other comprehensive income in accordance with paragraph 4.1.2A and the entity is required to recognise some changes in fair value in other comprehensive income in accordance with paragraph 5.7.10.

### 3. Couverture d'investissement net dans une opération étrangère

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende est reçu d'une filiale étrangère (investissement net dans une opération étrangère)
   - La transaction est libellée dans une devise autre que la devise fonctionnelle de l'entité qui reçoit le dividende
   - Le risque de change affectera le résultat consolidé
   - La stratégie de couverture est clairement documentée conformément à IFRS 9 §6.4.1
   - L'instrument de couverture peut être détenu par n'importe quelle entité du groupe

**Raisonnement**:
IFRIC 16 §§14-15 confirme que le risque de change d'éléments monétaires intragroupe peut être désigné comme élément couvert dans les comptes consolidés. La créance de dividende en monnaie étrangère constitue une exposition au risque de change qui peut être couverte comme partie d'une relation de couverture d'investissement net.

**Implications pratiques**: La partie efficace de la variation de valeur de l'instrument de couverture est incluse en autres éléments du résultat全局, tandis que la partie inefficace est reconnue en résultat.

**Référence**:
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) may be designated as a hedging instrument in a hedge of a net investment in a foreign operation. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.
 - ifric16 15

    >For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency the hedged risk is measured, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, the total effective portion of the change is included in other comprehensive income. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.