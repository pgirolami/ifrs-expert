# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Reformulation**:
>Eligibility of an intragroup dividend receivable as a hedged item for foreign currency risk hedge accounting in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias39`, `ias21`, `ias24`, `ias29`)
   - IFRIC (`ifric16`, `ifric17`, `ifric21`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs18`, `ifrs12`)
   - SIC (`sic25`, `sic29`)

**Retenue pour l'analyse**
   - IAS (`ias39`, `ias21`, `ias24`, `ias29`)
   - IFRIC (`ifric16`, `ifric17`, `ifric21`)
   - IFRS (`ifrs9`, `ifrs19`, `ifrs18`, `ifrs12`)
   - SIC (`sic25`, `sic29`)

## Hypothèses
   - La créance dividendes intragroupe est un actif financier moné aires denotionnel entre deux entités d'un même groupe.
   - Les deux entités du groupe ont des devises fonctionnelles différentes, de sorte que l'exposition au risque de change n'est pas éliminée par consolidation.
   - Le risque de change influence le résultat consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

La créance de dividendes intragroupe est un actif monétaire intragroupe. Bien que la règle générale exclue les postes intragroupes de la désignation comme élément couvert (IAS 39 §80 ; IFRS 9 §6.3.5), une exception existe précisément pour le risque de change des postes monétaires intragroupes lorsque les différences de change ne sont pas éliminées en consolidation (IAS 39 §80 ; IFRS 9 §6.3.6). Cette exception s'applique sous réserve que les conditions de IAS 21 soient remplies.

## Points Opérationnels

   - Documenter formellement la relation de couverture dès son inception avec identification de l'instrument de couverture, de l'élément couvert (risque de change sur la créance intragroupe) et de la stratégie de gestion des risques (IAS 39 §88(a) / IFRS 9 §6.4.1).
   - Démontrer l'efficacité de la couverture de manière continue et vérifier que le risque de change affecte effectivement le résultat consolidé (condition cumulative de l'exception).
   - Sélectionner le type de couverture approprié : une couverture de juste valeur est généralement adaptée pour une créance déjà comptabilisée ; une couverture de flux de trésorerie serait envisageable si la créance était encore conditionnelle.
   - Appliquer les dispositions de IAS 39 §89 (fair value hedge) ou §95 (cash flow hedge) pour le traitement comptable des gains et pertes sur l'instrument de couverture et l'élément couvert.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Exclusion de la créance intragroupe comme élément couvert en vertu de l'exigence de partie externe | NON | - (non spécifiées) |
| 2. Couverture du risque de change sur un poste monétaire intragroupe (exception) | OUI SOUS CONDITIONS | - La créance de dividendes est dénommée dans une monnaie autre que la devise fonctionnelle de l'entité qui la comptabilise.<br>- Le risque de change affectera le résultat consolidé (les différences de change ne sont pas éliminées en consolidation). |

### 1. Exclusion de la créance intragroupe comme élément couvert en vertu de l'exigence de partie externe

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
En vertu de la règle générale (IAS 39 §80 et IFRS 9 §6.3.5), seuls les actifs, passifs, engagements ferme ou transactionsForecast hautement probables impliquant une partie externe à l'entité peuvent être désignés comme éléments couverts dans les états financiers consolidés. La créance intragroupe étant éliminée en consolidation, elle ne satisfait pas, en apparence, à cette exigence.

**Implications pratiques**: Cette approche ne constitue pas un obstacle dirimant dès lors que l'exception pour risque de change s'applique.

**Référence**:
 - IAS 39 80

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions that involve a party external to the entity can be designated as hedged items.
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.

### 2. Couverture du risque de change sur un poste monétaire intragroupe (exception)

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividendes est dénommée dans une monnaie autre que la devise fonctionnelle de l'entité qui la comptabilise.
   - Le risque de change affectera le résultat consolidé (les différences de change ne sont pas éliminées en consolidation).

**Raisonnement**:
L'exception prévue par IAS 39 §80 et IFRS 9 §6.3.6 permet de désigner le risque de change d'un poste monétaire intragroupe (tels qu'un dividende à recevoir entre deux filiales) comme élément couvert dans les états financiers consolidés, à condition que ce poste génère une exposition aux gains ou pertes de change qui ne sont pas entièrement éliminés en consolidation. IAS 21 §45 confirme que les postes monétaires intragroupes ne sont pas éliminés lorsque les entités ont des devises fonctionnelles différentes.

**Implications pratiques**: La créance de dividendes intragroupe peut être désignée comme élément couvert dans le cadre d'une relation de couverture de juste valeur ou de couverture de flux de trésorerie, sous réserve du respect des conditions de désignation et de documentation de IAS 39 §88 ou IFRS 9 §6.4.1.

**Référence**:
 - IAS 39 80

    >As an exception, the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21.
 - IFRS 9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21.
 - IAS 21 45

    >However, an intragroup monetary asset (or liability), whether short-term or long-term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements.