# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifrs10`
   - `ifrs12`
   - `ifrs19`
   - `ias24`
   - `ifrs9`
   - `ias7`
   - `ifric17`
   - `ias27`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric2`

## Hypothèses
   - La question porte sur des états financiers consolidés IFRS.
   - Une créance de dividende intragroupe a été comptabilisée avant les écritures de consolidation.
   - La documentation de couverture visée porte sur le risque de change attaché à la créance intragroupe reconnue, et non sur le dividende intragroupe en tant que produit/charge consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une couverture ne peut pas viser le dividende intragroupe éliminé en tant que tel. En revanche, elle peut être documentée sur la créance intragroupe reconnue si celle-ci constitue un élément monétaire intragroupe dont le risque de change n’est pas entièrement éliminé en consolidation.

## Points Opérationnels

   - Vérifier la date de reconnaissance de la créance de dividende : la documentation ne peut viser qu’un élément existant et identifié.
   - Tester si les entités concernées ont des monnaies fonctionnelles différentes et si les écarts de change sur la créance affectent le résultat consolidé.
   - Éviter de désigner le dividende intragroupe éliminé comme élément couvert ; viser uniquement la créance intragroupe reconnue si l’exception IFRS 9 est satisfaite.
   - Conserver la démonstration de l’articulation entre éliminations de consolidation et risque de change résiduel au niveau du groupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilité de couverture | OUI SOUS CONDITIONS | - La créance de dividende intragroupe reconnue doit être traitée comme un élément monétaire intragroupe.<br>- Les écarts de change sur cette créance doivent affecter le résultat consolidé et ne pas être entièrement éliminés en consolidation.<br>- La désignation doit porter sur la créance intragroupe reconnue, pas sur le dividende intragroupe éliminé. |
| 2. Comptabilisation en consolidation | OUI | - (non spécifiées) |
| 3. Comptes séparés | NON | - (non spécifiées) |

### 1. Comptabilité de couverture
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe reconnue doit être traitée comme un élément monétaire intragroupe.
   - Les écarts de change sur cette créance doivent affecter le résultat consolidé et ne pas être entièrement éliminés en consolidation.
   - La désignation doit porter sur la créance intragroupe reconnue, pas sur le dividende intragroupe éliminé.

**Raisonnment**:
Dans les comptes consolidés, IFRS 9 exclut en principe les transactions intragroupe comme éléments couverts. L’exception vise les éléments monétaires intragroupe, par exemple une créance/dette entre entités du groupe, lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Ici, cela ne peut fonctionner que si la créance de dividende reconnue entre dans cette exception ; le dividende intragroupe lui-même, éliminé en consolidation, ne peut pas être l’élément couvert.

**Implications pratiques**: La documentation de couverture doit viser le receivable intragroupe et démontrer que son risque de change subsiste au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item

### 2. Comptabilisation en consolidation
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La consolidation impose l’élimination intégrale des actifs, passifs, produits, charges et flux intragroupe. Donc la créance de dividende, la dette correspondante et le dividende intragroupe sont éliminés dans les comptes consolidés. Cette mécanique limite la couverture possible au seul risque de change résiduel admis par IFRS 9 sur un élément monétaire intragroupe.

**Implications pratiques**: Avant toute documentation de couverture, il faut identifier ce qui est éliminé en consolidation et ce qui peut encore créer un effet de change au niveau consolidé.

**Référence**:
 - B86
    >eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows
 - 4
    >Intragroup related party transactions and outstanding balances are eliminated

### 3. Comptes séparés
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche ne répond pas à la situation posée, qui vise explicitement la consolidation. IFRS 9 précise que les transactions intragroupe peuvent être couvertes dans les états individuels ou séparés, mais pas dans les états consolidés, sauf exceptions limitées. Elle ne permet donc pas de fonder la réponse recherchée en consolidation.

**Implications pratiques**: Le fait qu’une couverture puisse exister en comptes séparés ne suffit pas à la transposer en comptes consolidés.

**Référence**:
 - 6.3.5
    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements
 - 4
    >Separate financial statements are those presented by an entity