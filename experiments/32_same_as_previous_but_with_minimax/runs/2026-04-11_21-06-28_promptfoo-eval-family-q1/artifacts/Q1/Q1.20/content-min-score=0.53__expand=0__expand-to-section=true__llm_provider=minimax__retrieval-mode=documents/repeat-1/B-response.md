# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Reformulation**:
>Eligibility for hedge accounting of foreign currency risk on an intragroup dividend receivable in consolidated financial statements

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
   - La créance de dividendes intragroupe est un élément monétaire (contrairement à un élément non-monétaire, elle sera traduite au cours de clôture à chaque clôture).
   - Les deux entités intragroupe ont des devises fonctionnelles différentes, de sorte que les écarts de change ne sont pas éliminés à la consolidation conformément à IAS 21.
   - Le dividende est bien un элемент de type créance/payable (et non une participation en capitaux propres réévaluée).
   - L'entité souhaitant appliquer la comptabilité de couverture utilise IAS 39 (et non IFRS 9 only), ou utilise IFRS 9 avec les mêmes exceptions.

## Recommandation

**OUI SOUS CONDITIONS**

L'exception prévue par IAS 39 §80 et IFRS 9 §6.3.6 permet de désigner le risque de change d'un élément monétaire intragroupe comme élément couvert dans les états financiers consolidés, à condition que l'écart de change ne soit pas intégralement éliminé à la consolidation. Le dividende intragroupe créance constitue un élément monétaire dont l'exposition au change n'est pas éliminée si les devises fonctionnelles des entités concernées diffèrent. Il faut ensuite que les conditions de qualification du §88 soient satisfaites (documentation formelle, efficacité attendue, mesurabilité).

## Points Opérationnels

   - Vérifier que les deux entités intragroupe ont des devises fonctionnelles différentes (condition nécessaire pour que les écarts de change ne soient pas éliminés à la consolidation).
   - Établir la documentation formelle de couverture à l'origine, identifiant l'instrument de couverture, l'élément couvert (le risque de change de la créance de dividende), la nature du risque et la méthode d'évaluation de l'efficacité (§88a IAS 39).
   - S'assurer que l'efficacité de la couverture peut être mesurée de façon fiable et que la couverture est attendue comme hautement efficace (§88b et §88d IAS 39).
   - Choisir le type de couverture (fair value hedge ou cash flow hedge) en fonction de la structure de l'instrument de couverture désigné.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture permissible du risque de change d'un élément monétaire intragroupe en consolidation | OUI SOUS CONDITIONS | - L'écart de change sur la créance n'est pas intégralement éliminé à la consolidation ( IAS 21 §45), c'est-à-dire que les deux entités intragroupe ont des devises fonctionnelles différentes.<br>- L'élément monétaire est effectivement un poste créance (et non une participation éliminée).<br>- La relation de couverture satisfait toutes les conditions de qualification du §88 d'IAS 39 (documentation formelle à l'origine, efficacité attendue et démontrée, mesurabilité fiable). |
| 2. Exclusion générale de la couverture des éléments intragroupe en consolidation | NON | - (non spécifiées) |

### 1. Couverture permissible du risque de change d'un élément monétaire intragroupe en consolidation

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'écart de change sur la créance n'est pas intégralement éliminé à la consolidation ( IAS 21 §45), c'est-à-dire que les deux entités intragroupe ont des devises fonctionnelles différentes.
   - L'élément monétaire est effectivement un poste créance (et non une participation éliminée).
   - La relation de couverture satisfait toutes les conditions de qualification du §88 d'IAS 39 (documentation formelle à l'origine, efficacité attendue et démontrée, mesurabilité fiable).

**Raisonnement**:
IAS 39 §80 et IFRS 9 §6.3.6 offrent une exception explicite : le risque de change d'un élément monétaire intragroupe peut être désigné comme élément couvert dans les états financiers consolidés, pour autant que l'écart de change ne soit pas entièrement éliminé à la consolidation en vertu d'IAS 21. Une créance de dividende intragroupe est un élément monétaire ; si les deux filiales ont des devises fonctionnelles distinctes, les écarts de change ne sont pas éliminés et l'exception s'applique.

**Implications pratiques**: Désigner explicitement le risque de change de la créance de dividende intragroupe comme risque couvert dans la documentation de hedge accounting, et appliquer le traitement comptable prévu (fair value hedge ou cash flow hedge selon la nature de la couverture).

**Référence**:
 - IAS 39 80

    >As an exception, the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21.
 - IAS 39 88

    >A hedging relationship qualifies for hedge accounting under paragraphs 89–102 if, and only if, all of the following conditions are met: (a) formal designation and documentation; (b) expected highly effective; (c) for cash flow hedges, highly probable forecast transaction; (d) effectiveness can be reliably measured; (e) assessed ongoing basis.
 - IFRS 9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21.
 - IAS 21 45

    >an intragroup monetary asset (or liability), whether short-term or long-term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements.

### 2. Exclusion générale de la couverture des éléments intragroupe en consolidation

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche décrit la règle générale selon laquelle les éléments intragroupe ne peuvent pas être désignés comme éléments couverts en consolidation (éliminés à la consolidation). Cependant, cette règle est concurrencée par l'exception explicite en IAS 39 §80 / IFRS 9 §6.3.6 qui s'applique précisément à la créance de dividendes intragroupe en devise étrangère. L'exception l'emporte sur la règle générale dans ce cas précis.

**Implications pratiques**: La règle générale ne bloque pas la désignation dans cette situation en raison de l'exception applicable.

**Référence**:
 - IAS 39 80

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions that involve a party external to the entity can be designated as hedged items.
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.