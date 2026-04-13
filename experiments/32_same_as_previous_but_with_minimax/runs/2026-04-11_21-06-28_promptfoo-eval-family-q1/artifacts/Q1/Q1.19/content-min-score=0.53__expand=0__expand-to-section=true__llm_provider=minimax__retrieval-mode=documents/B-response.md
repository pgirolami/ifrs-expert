# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Dans un schéma où des dividendes intragroupe ont déjà été reconnus en créance à recevoir, la question se pose du traitement du risque de change associé en consolidation. Ce risque peut-il être formellement documenté dans une relation de couverture ?

**Reformulation**:
>Hedge accounting for foreign currency risk on intragroup dividend receivable in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias21`, `ias24`, `ias7`, `ias26`)
   - IFRIC (`ifric16`, `ifric17`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs12`)
   - SIC (`sic25`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias24`, `ias7`, `ias26`)
   - IFRIC (`ifric16`, `ifric17`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs12`)
   - SIC (`sic25`, `sic7`)

## Hypothèses
   - Les dividendes intragroupe ont été reconnus comme une créance monétaire libellée en devise étrangère
   - La question porte sur les états financiers consolidés du groupe
   - Aucune autre information factuelle ne vient modifier les conditions d'application des approches identifiées

## Recommandation

**OUI SOUS CONDITIONS**

L'exception de l'IFRS 9 paragraphe 6.3.6 permet de désigner le risque de change des postes monétaires intragroupe dans les comptes consolidés. Sous réserve que le risque de change ne soit pas éliminé par la consolidation et que la documentation soit effectuée, un risque de change sur une créance de dividende intragroupe peut être couvert.

## Points Opérationnels

   - La désignation de la relation de couverture doit être документация à la date de désignation et préciser l'objectif et la stratégie de gestion des risques
   - L'entité doit appliquer les tests d'efficacité conformément à l'IFRS 9 paragraphs 6.4.1 et suivants
   - Une seule relation de couverture peut être qualifiée pour les mêmes actifs nets d'une même operation étrangère dans les états consolidés de la mère ultime (IFRIC 16.13)
   - En cas de désignation dans une couverture d'investissement net, le cumul des gains et pertes sur l'instrument de couverture déterminé comme couverture efficace est reconnu en OCI et reclassé en résultat à la cession de l'investissement net
   - En cas de désignation dans une couverture de juste valeur, la composante de change de la créance est ajustée à chaque date de clôture


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture d'investissement net | OUI SOUS CONDITIONS | - Le dividende est libellé dans une devise différente de la devise fonctionnelle de la société mère<br>- Les écarts de change ne sont pas éliminés sur consolidation (différence de devises fonctionnelles entre les entités du groupe)<br>- L'entité doit être partie à l'instrument de couverture ou documenter la relation de couverture<br>- Le risque désigné se limite aux écarts de change entre devises fonctionnelles (interprétation IFRIC 16.10)<br>- Le montant couvert ne peut excéder la valeur comptable des actifs nets de l'opération étrangère dans les états consolidés |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un actif financier relevant de l'IFRS 9<br>- Le risque de change doit être identifié et documenté comme risque couvert à la date de désignation<br>- L'instrument de couverture doit être un dérivé ou un autre instrument financier éligible<br>- La documentation doit démontrer l'efficacité de la relation de couverture |

### 1. Couverture d'investissement net

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende est libellé dans une devise différente de la devise fonctionnelle de la société mère
   - Les écarts de change ne sont pas éliminés sur consolidation (différence de devises fonctionnelles entre les entités du groupe)
   - L'entité doit être partie à l'instrument de couverture ou documenter la relation de couverture
   - Le risque désigné se limite aux écarts de change entre devises fonctionnelles (interprétation IFRIC 16.10)
   - Le montant couvert ne peut excéder la valeur comptable des actifs nets de l'opération étrangère dans les états consolidés

**Raisonnement**:
Un dividende intragroupe constitue un poste monétaire dont le risque de change peut, en vertu de l'exception IFRS 9.6.3.6, être désigné comme élément couvert dans une couverture d'investissement net, dès lors que le dividende est libellé dans une devise différente de la devise fonctionnelle de la société mère et que les écarts de change ne sont pas éliminés par la consolidation.

**Implications pratiques**: Les écarts de change efficaces sont reconnus en OCI dans la réserve de conversion, puis reclassés en résultat lors de la cession de l'investissement net.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency

### 2. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un actif financier relevant de l'IFRS 9
   - Le risque de change doit être identifié et documenté comme risque couvert à la date de désignation
   - L'instrument de couverture doit être un dérivé ou un autre instrument financier éligible
   - La documentation doit démontrer l'efficacité de la relation de couverture

**Raisonnement**:
La créance de dividende intragroupe étant un actif financier monétaire libellé en devise étrangère, son risque de change peut être désigné comme risque couvert dans une couverture de juste valeur. Les variations de juste valeur attribuables au risque de change sont reconnues en résultat et compensent la variation de juste valeur de l'élément couvert.

**Implications pratiques**: Les variations de juste valeur dues au risque de change sont comptabilisées en résultat (contrepartie des variations de juste valeur de la créance), permettant une compensation économique.

**Référence**:
 - IFRS 9 6.3.1

    >A hedged item can be a recognised asset or liability
 - IFRS 9 6.3.2

    >The hedged item must be reliably measurable