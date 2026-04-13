# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Reformulation**:
>Application of hedge accounting to foreign exchange risk on intragroup dividend receivable in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs18`, `ifrs9`, `ifrs12`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs18`, `ifrs9`, `ifrs12`)
   - SIC (`sic25`)

## Hypothèses
   - Le dividende intragroupe est libellé dans une devise étrangère à celle de l'entité consolidante
   - Les entités du groupe ont des devises fonctionnelles différentes
   - Les états financiers concernés sont les comptes consolidés du groupe

## Recommandation

**OUI SOUS CONDITIONS**

L'approche 1 (exception paragraphe 6.3.6) est applicable sous réserve que le risque de change du dividende intragroupe ne soit pas éliminé totalement lors de la consolidation. L'approche 2 (règle générale paragraphe 6.3.5) n'est pas applicable car elle interdit la désignation d'éléments intragroupe comme éléments couverts.

## Points Opérationnels

   - Documenter la relation de couverture en identifiant le dividende intragroupe comme élément couvert et en désignant le risque de change comme risque couvert
   - S'assurer que les conditions d'efficacité de la couverture sont satisfaites selon IFRS 9 paragraphes 6.4.1 et suivants
   - Vérifier que les écarts de change sur le dividende intragroupe ne sont pas éliminés à la consolidation du fait de la différence de devises fonctionnelles
   - Présenter les variations de juste valeur du dérivé de couverture dans la même catégorie que le résultat sur l'élément couvert selon IFRS 18 paragraphes B70-B76


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de change стандарт IFRS 9 (exigence de contrepartie externe) | NON | - N/A - Non applicable |
| 2. Exception pour les postes monétaires intragroupe (paragraphe 6.3.6) | OUI SOUS CONDITIONS | - Les entités émettrice et destinataire du dividende ont des devises fonctionnelles différentes<br>- Les écarts de change ne sont pas totalement éliminés lors de la consolidation conformément à IAS 21<br>- Le risque de change affecte le résultat consolidé du groupe |

### 1. Couverture de change стандарт IFRS 9 (exigence de contrepartie externe)

**Applicabilité**: NON

**Conditions**:
   - N/A - Non applicable

**Raisonnement**:
La règle générale du paragraphe 6.3.5 exige qu'un élément désigné comme élément couvert soit avec une partie externe à l'entité déclarante. Un dividende intragroupe est une créance entre entités du même groupe, hence this condition is not met for standard hedge accounting.

**Implications pratiques**: Aucun traitement de couverture possible en vertu de cette approche pour le dividende intragroupe.

**Référence**:
 - IFRS 9 6.3.5

    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items

### 2. Exception pour les postes monétaires intragroupe (paragraphe 6.3.6)

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les entités émettrice et destinataire du dividende ont des devises fonctionnelles différentes
   - Les écarts de change ne sont pas totalement éliminés lors de la consolidation conformément à IAS 21
   - Le risque de change affecte le résultat consolidé du groupe

**Raisonnement**:
En vertu du paragraphe 6.3.6, le risque de change d'un poste monétaire intragroupe (telle qu'une créance dividende) peut qualify as a hedged item dans les états financiers consolidés si l'exposition aux gains ou pertes de change n'est pas totalement éliminée lors de la consolidation. Cette condition est remplie lorsque les devises fonctionnelles des entités sont différentes et que les écarts de change affectent le résultat consolidé.

**Implications pratiques**: Possibilité de désigner le risque de change du dividende intragroupe comme risque couvert dans une relation de couverture au niveau des comptes consolidés.

**Référence**:
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation