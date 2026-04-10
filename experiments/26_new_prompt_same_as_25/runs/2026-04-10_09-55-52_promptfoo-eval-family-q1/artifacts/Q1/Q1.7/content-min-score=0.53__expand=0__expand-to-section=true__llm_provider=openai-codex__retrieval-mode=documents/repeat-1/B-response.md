# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ias21`
   - `ifrs9`
   - `ias32`
   - `ifric17`
   - `ifrs19`
   - `ifrs7`
   - `ifrs12`
   - `ifric2`
   - `ifric16`
   - `ias7`
   - `sic25`
   - `ps1`
   - `ifric14`

## Hypothèses
   - L’analyse est effectuée dans les comptes consolidés.
   - La relation envisagée est une relation de comptabilité de couverture au titre d’IFRS 9 portant sur un risque de change.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe, si le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance monétaire exposée au change qui n’est pas totalement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; les modèles de cash flow hedge et de net investment hedge ne correspondent pas, en l’état, au fait décrit.

## Points Opérationnels

   - Le point déterminant est le moment: une fois le dividende déclaré et la créance reconnue, l’analyse bascule d’une transaction future vers un actif monétaire reconnu.
   - En consolidation, la recevabilité dépend du caractère intragroupe monétaire de la créance et de l’existence de monnaies fonctionnelles différentes entre les entités concernées.
   - Le traitement IAS 21 des écarts de change est le référentiel de base; la comptabilité de couverture IFRS 9 ne vient qu’en surcouche.
   - Si la documentation vise les dividendes avant reconnaissance de la créance, ce ne serait plus la même analyse que celle du cas posé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Le risque de change doit donner lieu à des écarts de change non totalement éliminés en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, le dividende intragroupe a déjà donné lieu à la reconnaissance d’une créance dans les comptes consolidés. On n’est donc plus face à une transaction future hautement probable, mais face à un actif monétaire déjà comptabilisé. Le modèle de cash flow hedge n’est pas celui qui correspond au fait générateur décrit.

**Implications pratiques**: Cette documentation ne serait pas cohérente avec un dividende déjà déclaré et devenu créance comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation.
 - 6.3.3
    >If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable.

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Le risque de change doit donner lieu à des écarts de change non totalement éliminés en consolidation.

**Raisonnment**:
Ici, le fait décrit est une créance déjà reconnue au titre d’un dividende intragroupe. IFRS 9 permet de couvrir un actif reconnu, et prévoit explicitement qu’en consolidation le risque de change d’un élément monétaire intragroupe peut être un élément couvert s’il génère des écarts de change non totalement éliminés selon IAS 21. C’est le cas seulement si les entités du groupe concernées ont des monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation IFRS de couverture est recevable si elle vise la créance intragroupe reconnue et le risque de change résiduel en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise le risque de change attaché à l’investissement net dans une activité à l’étranger, c’est-à-dire aux actifs nets de cette activité, et non une créance de dividende intragroupe déjà comptabilisée. Le fait que des écarts de conversion soient reconnus en OCI pour une activité étrangère ne transforme pas la créance de dividende en investissement net couvert.

**Implications pratiques**: La créance de dividende ne doit pas être documentée comme une couverture d’investissement net.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability ... or a net investment in a foreign operation.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Indépendamment de toute désignation de couverture, IAS 21 fournit ici le traitement de base. En consolidation, un actif monétaire intragroupe ne peut pas être éliminé sans faire apparaître les effets des fluctuations de change; ces écarts sont comptabilisés en résultat, ou en OCI dans le cas particulier visé au paragraphe 32. C’est le socle sur lequel une éventuelle couverture IFRS 9 peut s’ajouter.

**Implications pratiques**: Il faut d’abord constater le traitement IAS 21 de la créance intragroupe avant d’apprécier l’effet d’une couverture IFRS 9.

**Référence**:
 - 45
    >such an exchange difference is recognised in profit or loss
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated