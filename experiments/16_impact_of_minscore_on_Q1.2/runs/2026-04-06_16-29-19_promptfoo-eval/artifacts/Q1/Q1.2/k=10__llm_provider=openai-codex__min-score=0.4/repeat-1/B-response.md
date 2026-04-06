# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle pertinente au niveau de consolidation, ce qui crée une exposition de change dans les comptes consolidés.
   - La question porte sur la possibilité d'appliquer la comptabilité de couverture IFRS 9 à cette exposition de change, et non sur la simple comptabilisation des écarts de change sans relation de couverture documentée.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie la plus cohérente est la couverture de juste valeur sur le risque de change de la créance déjà comptabilisée. La couverture de flux de trésorerie n'est pas adaptée à une créance déjà reconnue, et la couverture d'investissement net ne vise pas un dividende intragroupe.

## Points Opérationnels

   - Le point de départ est d'identifier l'exposition dans les comptes consolidés : la partie change d'une créance monétaire déjà reconnue.
   - Si vous souhaitez la comptabilité de couverture, la documentation doit être formalisée comme relation de couverture IFRS 9 et non comme simple intention de gestion.
   - Dans les faits décrits, la couverture de juste valeur est la piste opérationnelle à documenter ; la couverture d'investissement net ne cible pas un dividende intragroupe.
   - À défaut de documentation qualifiante, les écarts de change sur la créance restent comptabilisés en résultat.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La couverture est documentée dès l'origine comme relation de couverture au sens d'IFRS 9.<br>- L'élément couvert est la partie change de la créance de dividende comptabilisée dans les comptes consolidés.<br>- Les exigences de désignation, documentation et efficacité de la relation de couverture sont satisfaites. |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le dividende a déjà été comptabilisé en créance : l'exposition porte donc sur un actif monétaire reconnu, pas sur des flux futurs hautement probables non encore reconnus. Dans ce cas précis, la logique IFRS fournie renvoie plutôt aux écarts de change sur actif monétaire déjà comptabilisé, pas à une variabilité de flux futurs à couvrir en OCI.

**Implications pratiques**: Cette documentation n'est pas la bonne base pour couvrir la partie change d'une créance de dividende déjà constatée.

**Référence**:
 - B5.7.2
    >IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss.
 - 5.7.3
    >A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised in accordance

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La couverture est documentée dès l'origine comme relation de couverture au sens d'IFRS 9.
   - L'élément couvert est la partie change de la créance de dividende comptabilisée dans les comptes consolidés.
   - Les exigences de désignation, documentation et efficacité de la relation de couverture sont satisfaites.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif financier monétaire déjà reconnu, dont la composante change affecte le résultat. Une documentation de couverture de juste valeur est cohérente si la relation de couverture est formellement désignée et satisfait aux exigences IFRS 9 sur la relation de couverture.

**Implications pratiques**: C'est l'approche la plus défendable pour faire transiter en résultat les effets de change du dérivé et de l'élément couvert de manière cohérente.

**Référence**:
 - 5.7.3
    >A gain or loss on financial assets or financial liabilities that are hedged items in a hedging relationship shall be recognised in accordance
 - B5.7.2
    >IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss.
 - 4.3.1
    >An embedded derivative is a component of a hybrid contract

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
IFRIC 16 vise le risque de change sur un investissement net dans une activité étrangère, c'est-à-dire un montant de net assets de l'opération étrangère. Un dividende intragroupe comptabilisé en créance n'est pas, dans les faits décrits, un investissement net mais une créance de dividende distincte.

**Implications pratiques**: Cette documentation ne correspond pas à l'objet couvert décrit par la question.

**Référence**:
 - 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture qualifiante, la règle applicable dans cette situation est la comptabilisation des écarts de change en résultat sur l'actif monétaire. C'est donc le traitement de repli certain si aucune documentation IFRS 9 n'est mise en place ou ne qualifie pas.

**Implications pratiques**: Les écarts de change sur la créance de dividende restent en résultat, sans mécanisme de compensation OCI/résultat propre à la comptabilité de couverture.

**Référence**:
 - B5.7.2
    >IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss.
 - 5.7.2
    >A gain or loss on a financial asset that is measured at amortised cost ... shall be recognised in profit or loss