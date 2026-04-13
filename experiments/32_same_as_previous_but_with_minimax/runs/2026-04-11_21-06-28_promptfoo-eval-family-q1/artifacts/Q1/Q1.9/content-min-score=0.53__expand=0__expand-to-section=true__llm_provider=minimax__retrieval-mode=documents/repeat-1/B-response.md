# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>La composante de risque de change liée à des dividendes intragroupe reconnus sous forme de créance peut-elle être désignée comme élément couvert dans les comptes consolidés ?

**Reformulation**:
>Whether foreign currency risk arising from intercompany dividend receivables can be designated as a hedged item in consolidated financial statements under IFRS 9 hedge accounting requirements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias37`)
   - IFRIC (`ifric2`, `ifric16`, `ifric17`)
   - IFRS (`ifrs9`, `ifrs19`)
   - SIC (`sic7`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias37`)
   - IFRIC (`ifric2`, `ifric16`, `ifric17`)
   - IFRS (`ifrs9`, `ifrs19`)
   - SIC (`sic7`)

## Hypothèses
   - Les dividendes intragroupe sont reconnus comme une créance monétaire entre entités du même groupe (non éliminée en consolidation)
   - La créance de dividende est libellée dans une devise différente de la fonctionnelle de l'entité qui la comptabilise dans les comptes consolidés
   - Le risque de change lié à cette créance affecte effectivement le résultat consolidé du fait de l'élimination partielle des écarts de change sur les éléments intragroupe selon IAS 21

## Recommandation

**OUI SOUS CONDITIONS**

La créance de dividende intragroupe est un élément monétaire. Selon IFRS 9§6.3.6, le risque de change d'un élément monétaire intragroupe peut être désigné comme élément couvert en consolidation, sous réserve que les devises fonctionnelles diffèrent et que le risque de change affecte le résultat consolidé.

## Points Opérationnels

   - Documenter la relation de couverture en specifying que l'élément couvert est la composante risque de change de la créance de dividende intragroupe
   - Vérifier que les devises fonctionnelles des deux entités diffèrent et que l'écart de change n'est pas éliminé en consolidation selon IAS 21
   - S'assurer que le risque de change affectera le résultat consolidé au moment du règlement de la créance


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture du risque de change d'un élément monétaire intragroupe | OUI SOUS CONDITIONS | - Les deux entités du groupe doivent avoir des devises fonctionnelles différentes (IAS 21)<br>- Le risque de change doit affecter le résultat consolidé (et non être éliminé fully)<br>- La créance doit être un élément monétaire (elle est dénouée en numéraire à terme) |
| 2. Couverture d'une transaction intragroupe prévue (forecast) | NON | - (non spécifiées) |

### 1. Couverture du risque de change d'un élément monétaire intragroupe

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Les deux entités du groupe doivent avoir des devises fonctionnelles différentes (IAS 21)
   - Le risque de change doit affecter le résultat consolidé (et non être éliminé fully)
   - La créance doit être un élément monétaire (elle est dénouée en numéraire à terme)

**Raisonnement**:
Une créance de dividende intragroupe constitue un élément monétaire. L'exception de l'IFRS 9§6.3.6 permet de désigner le risque de change de tels éléments en consolidation, contrairement à la règle générale de l'IFRS 9§6.3.5 qui interdit les éléments intragroupe. Les conditions à respecter portent sur la différence de devises fonctionnelles et l'impact sur le résultat consolidé.

**Implications pratiques**: L'entité peut désigner le risque de change de la créance de dividende comme élément couvert dans une relation de couverture en consolidation, sous réserve de satisfies les conditions de documentation et d'efficacité.

**Référence**:
 - IFRS 9 6.3.5

    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - IFRS 9 6.3.6

    >the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation

### 2. Couverture d'une transaction intragroupe prévue (forecast)

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche concerne les transactions prévues (forecast transactions) hautement probables, alors que la question porte sur des dividendes déjà reconnus comme créances. Une créance de dividende comptabilisée n'est pas une transaction future prévue mais un élément monétaire existant, relevant de l'approche 1.

**Implications pratiques**: Non applicable car le dividende est déjà reconnu comme créance et non comme transaction prévisionnelle.

**Référence**:
 - IFRS 9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable
 - IFRS 9 6.3.5

    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements