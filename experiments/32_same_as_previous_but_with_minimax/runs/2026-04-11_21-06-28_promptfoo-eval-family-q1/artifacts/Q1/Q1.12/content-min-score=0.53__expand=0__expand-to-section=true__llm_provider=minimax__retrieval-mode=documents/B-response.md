# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Est-il possible, au niveau consolidé, de qualifier de manière formelle une couverture du risque de change sur des dividendes intragroupe ayant fait l’objet d’une comptabilisation en créance à recevoir ?

**Reformulation**:
>Eligibility of intragroup dividend receivable for formal hedge accounting of foreign exchange risk at consolidated level

## Documentation
**Consultée**
   - IAS (`ias32`)
   - IFRIC (`ifric17`, `ifric2`, `ifric16`)
   - IFRS (`ifrs9`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - La question porte sur la comptabilisation au niveau des états financiers consolidés du groupe.
   - Les dividendes intragroupe ont été comptabilisés en créance à recevoir (actif financier).
   - Le risque de change existe car la créance est dans une devise différente de la devise fonctionnelle du créancier intragroupe.

## Recommandation

**NON**

L'IFRS 9 paragraphe 6.3.5 interdit explicitement de désigner comme élément couvert un poste avec une partie intragroupe. Une créance de dividende intragroupe ne peut donc pas être désignée comme élément couvert pour un risque de change au niveau consolidé.

## Points Opérationnels

   - Aucune couverture de change ne peut être formellement qualifiée sur cette créance intragroupe au niveau consolidé.
   - Les écarts de change seront automatiquement comptabilisés en résultat à chaque période, sauf si l'entité opte pour un regroupement d'entités操作 (net investment hedge) sur une participation dans une operation étrangère, ce qui est distinct du présent cas.
   - Aucune documentation de couverture au sens de l'IFRS 9 n'est nécessaire ni possible pour ce poste intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation de couverture du risque de change | NON | - (non spécifiées) |
| 2. Traitement par défaut du risque de change (sans désignation de couverture) | OUI | - (non spécifiées) |

### 1. Comptabilisation de couverture du risque de change

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
En vertu de l'IFRS 9 §6.3.5, seuls les actifs, passifs, engagements fermes ou transactions forecast avec une partie externe à l'entité rapportante peuvent être désignés comme éléments couverts. Une créance de dividende intragroupe est une créance entre entités du même groupe, donc avec une partie intragroupe. Cette condition fondamentale n'est pas remplie.

**Implications pratiques**: Aucun traitement comptable de couverture n'est possible pour le risque de change sur cette créance intragroupe.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items**. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.

### 2. Traitement par défaut du risque de change (sans désignation de couverture)

**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
En l'absence de désignation de couverture, l'IFRS 9 §5.7.2 impose de reconnaître les gains et pertes sur actifs financiers évalués au coût amorti en résultat lorsqu'ils sont décomptabilisés, reclassifiés ou via le processus d'amortissement, y compris pour les différences de change. Le dividende intragroupe étant comptabilisé en créance (actif financier à coût amorti), les écarts de change sont reconnus en résultat.

**Implications pratiques**: Les différences de change sur la créance de dividende intragroupe sont reconnues en résultat à chaque clôture.

**Référence**:
 - ifrs9 5.7.2

    >A gain or loss on a financial asset that is measured at amortised cost and is not part of a hedging relationship (see paragraphs 6.5.8⁠–⁠6.5.14 and, if applicable, paragraphs 89⁠–⁠94 of IAS 39 for the fair value hedge accounting for a portfolio hedge of interest rate risk) shall be recognised in profit or loss when the financial asset is derecognised, reclassified in accordance with paragraph 5.6.2, through the amortisation process or in order to recognise impairment gains or losses. An entity shall apply paragraphs 5.6.2 and 5.6.4 if it reclassifies financial assets out of the amortised cost measurement category. A gain or loss on a financial liability that is measured at amortised cost and is not part of a hedging relationship (see paragraphs 6.5.8⁠–⁠6.5.14 and, if applicable, paragraphs 89⁠–⁠94 of IAS 39 for the fair value hedge accounting for a portfolio hedge of interest rate risk) shall be recognised in profit or loss when the financial liability is derecognised and through the amortisation process. (See paragraph B5.7.2 for guidance on foreign exchange gains or losses.)