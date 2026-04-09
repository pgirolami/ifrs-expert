# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Documentation consultée**
   - `ias24`
   - `ifrs9`
   - `ifric17`
   - `ifrs19`
   - `ifric16`
   - `ifrs12`
   - `ifrs18`
   - `ifric1`
   - `ias27`
   - `sic25`
   - `ias37`
   - `ifric19`
   - `ifric21`
   - `sic29`
   - `ias26`

## Hypothèses
   - La question porte sur des états financiers consolidés établis selon les IFRS.
   - La créance sur dividendes intragroupe est une créance monétaire libellée dans une devise qui crée un risque de change entre entités du groupe.
   - L’exposition visée provient d’un solde intragroupe lié au dividende et non d’un investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, une exposition de change sur une créance de dividendes intragroupe n’est éligible que si elle correspond à un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation, typiquement entre entités ayant des monnaies fonctionnelles différentes. En revanche, cette exposition n’est pas, en elle-même, une couverture d’investissement net.

## Points Opérationnels

   - Le point décisif est de vérifier si la créance de dividendes intragroupe est un élément monétaire dont les écarts de change subsistent en résultat consolidé.
   - Si les deux entités du groupe ont la même monnaie fonctionnelle, l’exception IFRS 9 sur les éléments monétaires intragroupe ne joue en pratique pas.
   - Même si l’exposition est éligible, la comptabilité de couverture exige la désignation formelle et la documentation dès l’origine de la relation de couverture.
   - La qualification comme couverture d’investissement net doit être écartée sauf si l’élément couvert est réellement un montant de net assets d’une activité à l’étranger.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance sur dividendes est un élément monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation, notamment parce que les entités concernées ont des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance sur dividendes constitue un solde monétaire intragroupe exposé au change.<br>- Le risque de change affecte le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance sur dividendes est un élément monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation, notamment parce que les entités concernées ont des monnaies fonctionnelles différentes.

**Raisonnment**:
En consolidation, IFRS 9 exclut en principe les éléments intragroupe comme éléments couverts. Toutefois, une exception existe pour le risque de change d’un élément monétaire intragroupe lorsque les gains ou pertes de change ne sont pas entièrement éliminés en consolidation. Si la créance de dividendes intragroupe répond à ce cas, une relation de couverture peut être désignée, sous réserve des critères de documentation et d’efficacité.

**Implications pratiques**: Tester d’abord si le solde de dividende intragroupe génère bien un risque de change résiduel au niveau consolidé avant de documenter une couverture de juste valeur.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance sur dividendes constitue un solde monétaire intragroupe exposé au change.
   - Le risque de change affecte le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation.

**Raisonnment**:
La même restriction de principe s’applique en consolidation aux éléments intragroupe. Néanmoins, si la créance de dividendes intragroupe constitue un élément monétaire intragroupe exposé à un risque de change non entièrement éliminé, cette exposition peut être désignée comme élément couvert. L’applicabilité dépend donc du caractère monétaire du solde et du maintien d’un effet de change en résultat consolidé.

**Implications pratiques**: La documentation de couverture doit viser l’exposition de change résiduelle constatée en consolidation, et non le simple fait qu’il s’agit d’un dividende intragroupe.

**Référence**:
 - 6.3.5
    >not in the consolidated financial statements of the group
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe comptabilisée, donc un solde distinct lié à un dividende, et non un montant de net assets d’une activité à l’étranger. IFRIC 16 précise que la couverture d’investissement net vise le risque de change sur un investissement net dans une activité étrangère. Une créance de dividendes intragroupe n’est pas, en elle-même, cet investissement net.

**Implications pratiques**: Ne pas traiter automatiquement la créance de dividendes comme une composante d’investissement net couvert au sens d’IFRS 9 / IFRIC 16.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity