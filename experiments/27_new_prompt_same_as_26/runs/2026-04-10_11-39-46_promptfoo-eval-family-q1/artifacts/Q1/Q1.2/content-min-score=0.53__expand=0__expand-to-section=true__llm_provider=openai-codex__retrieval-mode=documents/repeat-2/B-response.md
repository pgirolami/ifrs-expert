# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs19`
   - `ias32`
   - `ifric17`
   - `ifrs17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ifrs9`
   - `ifric19`
   - `ias37`
   - `ifric16`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise créant un risque de change au niveau des comptes consolidés.
   - La question porte uniquement sur les modèles de comptabilité de couverture envisageables dans les comptes consolidés.

## Recommandation

**OUI**

Dans cette situation, seule la couverture de juste valeur est directement applicable, car il s'agit d'une créance intragroupe déjà comptabilisée, donc d'un poste reconnu. La couverture de flux de trésorerie vise une transaction future hautement probable, et la couverture d'investissement net vise un investissement net dans une activité à l'étranger, pas une créance de dividende déjà enregistrée.

## Points Opérationnels

   - Le point clé de timing est que le dividende est déjà comptabilisé en créance : cela oriente vers un élément couvert reconnu, pas vers une transaction future.
   - En comptes consolidés, la contrainte générale d'externalité des éléments couverts connaît une exception limitée au risque de change d'un poste monétaire intragroupe.
   - Si la documentation vise la partie change, elle doit être rédigée au niveau consolidé, puisque c'est à ce niveau que l'exception IFRS 9 pour les postes monétaires intragroupe s'apprécie.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI | - La créance de dividende doit constituer un poste monétaire intragroupe exposé au risque de change dans les comptes consolidés. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI

**Conditions**:
   - La créance de dividende doit constituer un poste monétaire intragroupe exposé au risque de change dans les comptes consolidés.

**Raisonnment**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance : il s'agit donc d'un actif reconnu. IFRS 9 permet, en comptes consolidés, de désigner le risque de change d'un poste monétaire intragroupe comme élément couvert. Cette voie correspond donc directement au fait décrit.

**Implications pratiques**: La documentation de couverture peut viser la composante change de la créance intragroupe déjà reconnue au bilan consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction future prévue et hautement probable. Or, dans votre cas, le dividende intragroupe n'est plus une transaction future : il a déjà été comptabilisé en créance. Le fait déclencheur ne correspond donc pas au modèle de cash flow hedge dans cette situation précise.

**Implications pratiques**: Cette documentation n'est pas adaptée à la partie change d'une créance de dividende déjà enregistrée.

**Référence**:
 - 6.3.1
    >a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de net investment hedge concerne la couverture d'un investissement net dans une activité à l'étranger au sein du groupe. La situation décrite porte au contraire sur une créance de dividende intragroupe déjà comptabilisée. Sur ces faits, le risque couvert n'est pas celui de l'investissement net lui-même.

**Implications pratiques**: Cette voie ne couvre pas, dans ce cas, la composante change attachée à la créance de dividende reconnue.

**Référence**:
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation