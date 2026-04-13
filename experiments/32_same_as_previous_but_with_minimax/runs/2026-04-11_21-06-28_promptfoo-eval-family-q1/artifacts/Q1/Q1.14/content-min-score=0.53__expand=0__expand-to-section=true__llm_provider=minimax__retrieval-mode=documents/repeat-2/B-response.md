# Analyse d'une question comptable

**Date**: 2026-04-11

## Question

**Utilisateur**:
>Un dividende intragroupe a donné lieu à la comptabilisation d’un montant à recevoir au sein du périmètre consolidé. Peut-on, dans ces circonstances, documenter une couverture portant sur le risque de change afférent à cette exposition ?

**Reformulation**:
>Eligibility of an intragroup dividend receivable as a hedged item for foreign exchange risk under IFRS 9 hedge accounting requirements

## Documentation
**Consultée**
   - IAS (`ias21`, `ias7`, `ias24`)
   - IFRIC (`ifric17`, `ifric16`)
   - IFRS (`ifrs9`)
   - SIC (`sic25`)

**Retenue pour l'analyse**
   - IAS (`ias21`, `ias7`, `ias24`)
   - IFRIC (`ifric17`, `ifric16`)
   - IFRS (`ifrs9`)
   - SIC (`sic25`)

## Hypothèses
   - L'exposition concerne un dividende intragroupe comptabilisé en tant qu'actif financier dans les états financiers consolidés du groupe.
   - Le dividende est libellé dans une devise différente de la devise fonctionnelle de l'entité qui le reçoit au sein du groupe.
   - La question porte sur la possibilité d'appliquer la comptabilité de couverture au risque de change associé à cette créance dividendes intragroupe.

## Recommandation

**NON**

IFRS 9 paragraphe 6.3.5 exclut explicitement les transactions intragroupe des éléments éligibles en couverture. Une créance dividendes intragroupe ne constitue pas une transaction avec une partie externe au groupe, ce qui rend impossible la désignation d'une relation de couverture pour le risque de change, sauf à prouver qu'il s'agit d'un élément d'un investissement net dans une activité à l'étranger.

## Points Opérationnels

   - Les écarts de change sur la créance dividendes intragroupe doivent être reconnus en résultat selon IAS 21 paragraphe 28, car il ne s'agit pas d'un élément faisant partie de l'investissement net dans une opération étrangère au sens de IAS 21 paragraphe 32.
   - Aucune désignation de couverture au titre d'IFRS 9 ne peut être documentée pour cette exposition intragroupe.
   - Si l'opération implique une entité étrangère dont la devise fonctionnelle diffère, les règles de conversion de l'investissement net s'appliquent séparément.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilité de couverture d'un investissement net dans une activité à l'étranger | NON | - La créance doit représenter une composante identifiable d'un investissement net dans une opération étrangère<br>- L'écart de change doit naître entre la devise fonctionnelle de l'opération étrangère et celle de l'entité mère immédiate |
| 2. Interdiction de couverture comptable des éléments intragroupe | OUI | - La créance dividendes est une transaction intragroupe, c'est-à-dire entre deux entités du même périmètre de consolidation |
| 3. Reconnaissance des écarts de change sur les éléments monétaires intragroupe sans comptabilité de couverture | OUI | - L'élément monétaire intragroupe crée une exposition à des gains ou pertes de change qui affectent le résultat consolidé |

### 1. Comptabilité de couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - La créance doit représenter une composante identifiable d'un investissement net dans une opération étrangère
   - L'écart de change doit naître entre la devise fonctionnelle de l'opération étrangère et celle de l'entité mère immédiate

**Raisonnement**:
Si la créance dividendes fait partie d'un investissement net dans une opération étrangère, IAS 21 paragraphe 32 et IFRIC 16 paragraphe 10 permettent la comptabilisation des écarts de change en capitaux propres. Cependant, la créance dividendes intragroupe elle-même n'est pas un investissement net direct ; le dividende est une créance intercalaire éliminée en consolidation.

**Implications pratiques**: L'approche ne s'applique pas directement à la créance dividendes intragroupe elle-même, mais les écarts de change sur cette créance peuvent être reconnus selon les règles de conversion des investissements nets.

**Référence**:
 - IFRIC 16 paragraph 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity's functional currency.
 - IAS 21 paragraph 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity's net investment in a foreign operation shall be recognised initially in other comprehensive income.

### 2. Interdiction de couverture comptable des éléments intragroupe

**Applicabilité**: OUI

**Conditions**:
   - La créance dividendes est une transaction intragroupe, c'est-à-dire entre deux entités du même périmètre de consolidation

**Raisonnement**:
IFRS 9 paragraphe 6.3.5 dispose que seuls les actifs, passifs, engagements fermes ou transactions prévues hautement probables avec une partie externe à l'entité déclarante peuvent être désignés comme éléments couverts. Un dividende intragroupe est une transaction entre entités du même groupe, ce qui exclut toute désignation de couverture pour son risque de change.

**Implications pratiques**: Aucune documentation de couverture ne peut être établie pour le risque de change de cette créance intragroupe selon IFRS 9.

**Référence**:
 - IFRS 9 paragraph 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items.

### 3. Reconnaissance des écarts de change sur les éléments monétaires intragroupe sans comptabilité de couverture

**Applicabilité**: OUI

**Conditions**:
   - L'élément monétaire intragroupe crée une exposition à des gains ou pertes de change qui affectent le résultat consolidé

**Raisonnement**:
IAS 21 paragraphe 45 reconnaît que les éléments monétaires intragroupe ne peuvent être éliminés sans reconnaître l'effet des fluctuations de change dans les états financiers consolidés. Cependant, cela n'autorise pas une comptabilité de couverture ; les écarts de change sont simplement reconnus en résultat ou en capitaux propres selon les circonstances.

**Implications pratiques**: Les écarts de change sur la créance dividendes intragroupe sont reconnus en résultat ou en capitaux propres selon IAS 21, mais sans application de la comptabilité de couverture.

**Référence**:
 - IAS 21 paragraph 45

    >An intragroup monetary asset (or liability), whether short-term or long-term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements.