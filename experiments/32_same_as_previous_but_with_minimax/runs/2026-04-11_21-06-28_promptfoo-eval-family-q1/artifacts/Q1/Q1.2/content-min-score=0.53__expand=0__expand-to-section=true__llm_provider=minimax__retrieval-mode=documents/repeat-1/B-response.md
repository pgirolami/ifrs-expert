# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Reformulation**:
>Hedge accounting for foreign exchange risk of an intragroup dividend recognized as a receivable in consolidated financial statements

## Documentation
**Consultée**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs17`, `ifrs12`, `ifrs9`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IAS (`ias32`, `ias7`, `ias37`)
   - IFRIC (`ifric17`, `ifric2`, `ifric19`, `ifric16`)
   - IFRS (`ifrs19`, `ifrs17`, `ifrs12`, `ifrs9`)
   - SIC (`sic25`)

## Hypothèses
   - Le dividende intragroupe est libellé dans une devise étrangère différente de la devise fonctionnelle de l'entité qui le comptabilise en créance
   - Le dividende n'a pas encore été réglé en trésorerie à la date d'évaluation
   - L'entité consolidante n'est pas une entité d'investissement au sens d'IFRS 10
   - Le dividende est versé par une filiale étrangère (opération étrangère) dont l'investissement net a été qualifié comme tel

## Recommandation

**OUI SOUS CONDITIONS**

La couverture du risque de change sur un dividende intragroupe en créance est possible via la méthode de la couverture d'investissement net, sous réserve que le dividende soit lié à une opération étrangère et que les instruments de couverture soient externalisés. L'approche « entité d'investissement » ne s'applique pas ici car cette condition n'est pas remplie.

## Points Opérationnels

   - Documenter dès l'origine la relation de couverture désignant explicitement le risque de change sur la créance de dividende comme élément couvert
   - S'assurer que l'instrument de couverture est détenu par une entité ayant une partie externe au groupe (filiale avec contreparties tierces ou société mère)
   - Évaluer l'efficacité de la relation de couverture et documenter la méthode utilisée
   - Qualifier l'investissement sous-jacent comme investissement net dans une opération étrangère avant de désigner la couverture


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture d'investissement net | OUI SOUS CONDITIONS | - L'investissement net dans l'opération étrangère (filiale) doit exister et être documenté<br>- L'instrument de couverture doit être émis par une partie externe au groupe consolidé<br>- La relation de couverture doit être documentée dès l'origine et être efficace |
| 2. Exception d'entité d'investissement | NON | - L'entité consolidante doit être qualifiée d'entité d'investissement selon IFRS 10 |

### 1. Couverture d'investissement net

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'investissement net dans l'opération étrangère (filiale) doit exister et être documenté
   - L'instrument de couverture doit être émis par une partie externe au groupe consolidé
   - La relation de couverture doit être documentée dès l'origine et être efficace

**Raisonnement**:
IFRIC 16 autorise la désignation d'un instrument de couverture (dérivé ou non dérivé) dans une couverture d'investissement net en operaciones étrangères. Cependant, en vertu d'IFRS 9 §6.3.5, les transactions intragroupes ne sont généralement pas éligibles comme éléments couverts dans les comptes consolidés. La exception textsuelle vise les couvertures d'investissement net (IFRIC 16 §14) qui permettent de couvrir le risque de change sur la partie du investissement net représentée par la créance de dividende, à condition que les instruments de couverture soient détenus par une entité externe au groupe.

**Implications pratiques**: Il faut identifier l'instrument de couverture externe (dérivé de change ou dette en devise) et documenter la relation de couverture d'investissement net dans les comptes consolidés.

**Référence**:
 - IFRIC 16 14

    >A derivative or a non-derivative instrument may be designated as a hedging instrument in a hedge of a net investment in a foreign operation.
 - IFRS 9 6.3.5

    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.

### 2. Exception d'entité d'investissement

**Applicabilité**: NON

**Conditions**:
   - L'entité consolidante doit être qualifiée d'entité d'investissement selon IFRS 10

**Raisonnement**:
L'exception d'IFRS 9 §6.3.5 permet la comptabilité de couverture sur des transactions intragroupes dans les comptes consolidés d'une entité d'investissement. Toutefois, cette approche ne s'applique que si l'entité consolidante est une entité d'investissement au sens d'IFRS 10 qui évalue ses filiales à la juste valeur par le résultat. En l'absence de précision sur ce statut dans la question, cette condition n'est pas satisfaite et l'approche n'est pas applicable.

**Implications pratiques**: Non applicable en l'absence de statut d'entité d'investissement.

**Référence**:
 - IFRS 9 6.3.5

    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements... except for the consolidated financial statements of an investment entity.