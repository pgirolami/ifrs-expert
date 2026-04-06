# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La créance de dividende intragroupe génère une exposition de change dans les comptes consolidés.
   - La question porte sur les modèles IFRS de comptabilité de couverture susceptibles d'être documentés en consolidation pour cette composante change.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change est envisageable principalement via une couverture de juste valeur, une couverture de flux de trésorerie, ou, dans un cas différent, une couverture d'investissement net. En l'état des seuls faits fournis, le choix dépend de la nature exacte de l'exposition couverte sur le dividende intragroupe.

## Points Opérationnels

   - La documentation doit être mise en place dès la désignation de la relation de couverture dans les comptes consolidés.
   - Le point décisif est de qualifier l'exposition couverte : créance déjà comptabilisée, flux futur de dividende, ou investissement net dans l'entité étrangère.
   - Une couverture d'investissement net n'est pas un substitut automatique à la couverture d'une créance de dividende ; elle répond à un risque différent.
   - En l'absence de documentation qualifiante, le traitement par défaut reste la comptabilisation des effets de change en résultat.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être l'exposition de change effectivement désignée dans les comptes consolidés.<br>- Une relation de couverture documentée doit exister pour cette exposition spécifique. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - L'exposition couverte doit être formulée comme un risque de change sur des flux de trésorerie affectant ultérieurement le résultat consolidé.<br>- La relation doit être formellement désignée et suivie comme couverture de flux de trésorerie. |
| 3. Couverture d'investissement net | OUI SOUS CONDITIONS | - L'exposition couverte doit être celle d'un investissement net dans une opération étrangère inclus dans les comptes consolidés.<br>- Le risque désigné doit être le risque de change entre la monnaie fonctionnelle de l'opération étrangère et celle du parent concerné. |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être l'exposition de change effectivement désignée dans les comptes consolidés.
   - Une relation de couverture documentée doit exister pour cette exposition spécifique.

**Raisonnment**:
La créance de dividende comptabilisée est décrite comme une créance, donc elle peut porter un risque de change déjà existant en consolidation. Le contexte IFRS 9 admet la comptabilisation des gains et pertes sur éléments couverts dans une relation de couverture ; cette voie peut donc convenir si l'objectif est de couvrir la variation de valeur liée au change sur cette créance précise.

**Implications pratiques**: La variation de change de l'élément couvert et celle de l'instrument de couverture sont reflétées en résultat selon la logique de couverture de juste valeur.

**Référence**:
 - 5.7.3
    >A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised
 - 4.4.2
    >an item that was previously a designated and effective hedging instrument in a cash flow hedge or net investment hedge

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'exposition couverte doit être formulée comme un risque de change sur des flux de trésorerie affectant ultérieurement le résultat consolidé.
   - La relation doit être formellement désignée et suivie comme couverture de flux de trésorerie.

**Raisonnment**:
Si, dans les comptes consolidés, l'exposition visée est le flux de change attaché à l'encaissement du dividende plutôt qu'une créance déjà réévaluée, une documentation en cash flow hedge peut être envisagée. Le contexte cite explicitement ce modèle et la mécanique de reclassement en résultat lorsque le flux affecte le résultat.

**Implications pratiques**: La part efficace est d'abord enregistrée en autres éléments du résultat global puis reclassée en résultat lorsque le flux couvert affecte le résultat.

**Référence**:
 - 4.4.2
    >an item that was previously a designated and effective hedging instrument in a cash flow hedge
 - B6.6.14
    >reclassified hedging instrument gains or losses shall be apportioned to the line items affected

### 3. Couverture d'investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'exposition couverte doit être celle d'un investissement net dans une opération étrangère inclus dans les comptes consolidés.
   - Le risque désigné doit être le risque de change entre la monnaie fonctionnelle de l'opération étrangère et celle du parent concerné.

**Raisonnment**:
Ce modèle ne vise pas une créance de dividende en tant que telle, mais le risque de change lié à un investissement net dans une opération étrangère. Il ne serait pertinent ici que si, en substance, la question porte en consolidation sur la couverture du risque de change de l'investissement net dans la filiale étrangère, et non sur la créance de dividende isolée.

**Implications pratiques**: La part efficace de l'instrument de couverture est comptabilisée en OCI avec les écarts de conversion jusqu'à la cession de l'opération étrangère.

**Référence**:
 - 1
    >the gain or loss on the hedging instrument that is determined to be an effective hedge of the net investment is recognised in other comprehensive income
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture qualifiante et documentée, le traitement de base IFRS 9 s'applique. Le contexte indique que les gains ou pertes sur actifs et passifs financiers mesurés au coût amorti sont reconnus en résultat, y compris via les effets de change mentionnés dans les renvois de guidance.

**Implications pratiques**: Les écarts de change sur la créance/dividende et sur l'instrument éventuellement détenu sont comptabilisés selon les règles normales, sans neutralisation comptable de couverture.

**Référence**:
 - 5.7.2
    >A gain or loss on a financial asset that is measured at amortised cost ... shall be recognised in profit or loss
 - B5.7.4
    >changes in the foreign currency component of those financial instruments are presented in profit or loss