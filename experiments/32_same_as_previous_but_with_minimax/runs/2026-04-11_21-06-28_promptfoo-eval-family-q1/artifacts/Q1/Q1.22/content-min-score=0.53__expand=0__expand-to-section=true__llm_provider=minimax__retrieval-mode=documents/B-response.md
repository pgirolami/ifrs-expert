# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Reformulation**:
>Whether foreign currency risk arising from intra-group dividend receivables recognized in consolidated financial statements can be designated as a hedged item under hedge accounting rules

## Documentation
**Consultée**
   - IAS (`ias21`, `ias7`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric2`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs17`, `ifrs19`, `ifrs7`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic7`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias7`, `ias37`, `ias26`)
   - IFRIC (`ifric17`, `ifric16`, `ifric2`, `ifric19`)
   - IFRS (`ifrs9`, `ifrs17`, `ifrs19`, `ifrs7`)
   - PS (`ps1`)
   - SIC (`sic25`, `sic7`)

## Hypothèses
   - La créance de dividende intragroupe est comptabilisée dans les états financiers consolidés.
   - Le risque de change survient parce que le dividende est libellé dans une devise différente de la devise fonctionnelle de l'entité qui le reçoit.
   - La question porte sur l'éligibilité à la comptabilité de couverture de ce risque de change dans les états financiers consolidés.

## Recommandation

**NON**

IFRS 9.6.3.5 interdit expressément de désigner des actifs, passifs ou engagements fermes avec une partie interne au groupe comme éléments couverts à des fins de comptabilité de couverture. La créance de dividende intragroupe ne constitue pas une transaction avec une partie externe, ce qui exclut toute désignation de couverture, que ce soit en couverture de juste valeur ou en couverture d'investissement net.

## Points Opérationnels

   - Les écarts de change sur la créance de dividende intragroupe doivent être reconnus en résultat (ou en OCI si elle fait partie d'un net investment) conformément à IAS 21, sans possibilité de désigner une couverture comptable.
   - Il est recommandé de documenter dans les notes l'exposition au risque de change sur les créances intragroupes et les méthodes de gestion de ce risque (par exemple, couverture au niveau de l'entité qui émet le dividende si celle-ci est externe au groupe consolidant).
   - Si une entité du groupe souhaite couvrir ce risque, elle devrait le faire au niveau de la société qui verse le dividende (si celle-ci est externe) plutôt que sur la créance comptabilisée dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture d'investissement net | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | NON | - (non spécifiées) |
| 3. Aucune comptabilité de couverture (restriction intragroupe) | OUI | - La créance doit résulter d'un dividende décidé par une entité du même groupe.<br>- Le risque de change doit être lié à une différence entre la devise fonctionnelle de l'entité qui reçoit le dividende et celle de l'entité qui le verse. |

### 1. Couverture d'investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
IFRIC 16.10 précise que la comptabilité de couverture d'investissement net s'applique uniquement aux différences de change entre la devise fonctionnelle de l'opération étrangère et celle de la société mère. Une créance de dividende intragroupe ne constitue pas un élément faisant partie intégrante du net investment d'une opération étrangère au sens de IFRIC 16, sauf si le dividende est dû par une operation étrangère dont les capitaux propres sont traduits dans les états consolidés. La créance de dividende intragroupe immédiate ne répond pas à cette définition.

**Implications pratiques**: Cette approche ne s'applique pas aux créances de dividendes intragroupe sauf si elles émanent directement d'une opération étrangère dont les capitaux propres consolidables sont traduits.

**Référence**:
 - IFRIC 16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency.
 - IAS 21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity's net investment in a foreign operation shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate.

### 2. Couverture de juste valeur

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Bien que la couverture de juste valeur soit autorisee par IFRS 9 pour le risque de change sur les éléments monétaires, IFRS 9.6.3.5 restreint expressément les éléments couverts aux transactions avec des parties externes au groupe. La créance de dividende intragroupe est une transaction intragroupe, ce qui la rend inéligible à toute designation de couverture.

**Implications pratiques**: Cette approche ne s'applique pas car la créance de dividende est un élément intragroupe et non une transaction avec une partie externe.

**Référence**:
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.

### 3. Aucune comptabilité de couverture (restriction intragroupe)

**Applicabilité**: OUI

**Conditions**:
   - La créance doit résulter d'un dividende décidé par une entité du même groupe.
   - Le risque de change doit être lié à une différence entre la devise fonctionnelle de l'entité qui reçoit le dividende et celle de l'entité qui le verse.

**Raisonnement**:
IFRS 9.6.3.5 pose une interdiction générale et explicite de désigner des éléments couverts dans le cadre de couvertures comptables lorsqu'ils concernent des transactions intragroupe. La créance de dividende intragroupe tombe sous cette interdiction car elle représente un actif monétaire entre entités du même groupe. L'exception de IAS 21.32 relative aux écarts de change sur les postes monétaires faisant partie de l'investissement net dans une operation étrangère ne modifie pas cette restriction pour les créances de dividendes intragroupe immédiates.

**Implications pratiques**: Les écarts de change sur la créance de dividende intragroupe sont reconnus en résultat (ou en OCI si la créance fait partie d'un net investment dans une operation étrangère) mais ne peuvent pas être couverts par une relation de couverture désignée.

**Référence**:
 - IFRS 9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.
 - IAS 21 45

    >an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements.