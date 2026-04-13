# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Reformulation**:
>Eligibility for hedge accounting of foreign currency risk arising from an intragroup dividend receivable recognised in consolidated financial statements

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
   - La créance de dividendes intragroupe est un actif monétaire libellé en devise étrangère
   - L'exposition au risque de change n'est pas éliminée à la consolidation car les entités ont des devises fonctionnelles différentes
   - L'entité dispose d'une stratégie de gestion des risques documentée et peut satisfaire aux critères de effectiveness

## Recommandation

**OUI SOUS CONDITIONS**

La couverture du risque de change d'une créance de dividendes intragroupe est possible en vertu de l'exception prévue par IAS 39§80 et IFRS 9§6.3.6, sous réserve que les critères de qualification soient remplis et que l'exposition ne soit pas éliminée à la consolidation.

## Points Opérationnels

   - Documenter la relation de couverture dès l'origine avec identification de l'instrument de couverture, l'élément hedgé et le risque de change
   - Vérifier que l'exposition au change n'est pas éliminée à la consolidation (IAS 21§45) avant de appliquer l'exception
   - S'assurer que l'instrument de couverture implique une partie externe à l'entité rapportée (IAS 39§73 / IFRS 9§6.3.5)
   - Tester l'effectiveness de manière continue conformément à IAS 39§88(e) ou IFRS 9§6.4.1(c)
   - En cas de transition vers des taux de référence (IBOR reform), les amendements IAS 39§102A-102N ou IFRS 9§6.8.4-6.8.12 peuvent s'appliquer


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture en fair value hedge du risque de change | OUI SOUS CONDITIONS | - L'exposition au change ne doit pas être éliminée à la consolidation (différence de devises fonctionnelles entre les entités)<br>- L'entité doit satisfaire aux critères de qualification d'IAS 39§88 ou IFRS 9§6.4.1<br>- Documentation formelle et stratégie de risque documentée requises |
| 2. Couverture en cash flow hedge du risque de change | OUI SOUS CONDITIONS | - Même conditions que le fair value hedge : exception intragroupe applicable et critères IAS 39§88 ou IFRS 9§6.4.1 réunis<br>- La créance doit présenter une exposition à des variations de flux de trésorerie liées au change |
| 3. Reconnaissance des écarts de change en résultat | OUI | - Aucune condition spécifique ; traitement par défaut applicable en l'absence de désignation de couverture |

### 1. Couverture en fair value hedge du risque de change

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'exposition au change ne doit pas être éliminée à la consolidation (différence de devises fonctionnelles entre les entités)
   - L'entité doit satisfaire aux critères de qualification d'IAS 39§88 ou IFRS 9§6.4.1
   - Documentation formelle et stratégie de risque documentée requises

**Raisonnement**:
La créance de dividendes intragroupe est un actif monétaire reconnu exposé au risque de change. L'exception d'IAS 39§80 et IFRS 9§6.3.6 permet de désigner ce risque comme élément couvert dans les états consolidés, à condition que l'exposition ne soit pas éliminée à la consolidation.

**Implications pratiques**: Le gain ou la perte sur l'instrument de couverture et l'ajustement de fair value sur la créance hedgée sont reconnus en résultat.

**Référence**:
 - IAS 39 §80

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements
 - IFRS 9 §6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements

### 2. Couverture en cash flow hedge du risque de change

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Même conditions que le fair value hedge : exception intragroupe applicable et critères IAS 39§88 ou IFRS 9§6.4.1 réunis
   - La créance doit présenter une exposition à des variations de flux de trésorerie liées au change

**Raisonnement**:
Une créance de dividendes génère des flux de trésorerie futurs en devise étrangère. Le risque de variation de ces flux peut être éligible au cash flow hedge sous réserve des mêmes conditions d'exception et de qualification.

**Implications pratiques**: La portion efficace de la variation de fair value de l'instrument de couverture est reconnue en OCI ; la portion inefficace en résultat.

**Référence**:
 - IAS 39 §88(c)

    >the forecast transaction that is the subject of the hedge must be highly probable
 - IFRS 9 §6.5.8-6.5.14

    >accounting for the gain or loss on the hedging instrument and the hedged item

### 3. Reconnaissance des écarts de change en résultat

**Applicabilité**: OUI

**Conditions**:
   - Aucune condition spécifique ; traitement par défaut applicable en l'absence de désignation de couverture

**Raisonnement**:
En l'absence de désignation de relation de couverture, les écarts de change sur la créance de dividendes intragroupe sont reconnus en résultat conformément à IAS 21§28, comme c'est le cas pour tout élément monétaire.

**Implications pratiques**: Les variations de change sur la créance sont comptabilisées directement en profit ou perte sans mécanisme de offset.

**Référence**:
 - IAS 21 §28

    >Exchange differences arising on the settlement of monetary items or on translating monetary items at rates different from those at which they were translated on initial recognition shall be recognised in profit or loss