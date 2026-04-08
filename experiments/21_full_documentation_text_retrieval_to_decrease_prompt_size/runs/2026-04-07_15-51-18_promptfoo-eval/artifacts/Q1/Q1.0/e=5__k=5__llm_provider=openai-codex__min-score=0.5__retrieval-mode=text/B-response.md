# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ps1`
   - `ias7`
   - `ias28`
   - `ias19`
   - `sic25`
   - `ifrs3`
   - `ias23`
   - `ifric12`
   - `ias16`
   - `ifric17`
   - `ias39`
   - `ias37`
   - `ifrs15`
   - `ias21`
   - `ifrs11`
   - `ifric19`
   - `ias41`
   - `ifrs2`
   - `ifrs9`
   - `ias40`
   - `ias10`
   - `ias36`
   - `ifric22`
   - `ifrs6`
   - `ifrs19`
   - `ias34`
   - `ifric14`
   - `ifric7`
   - `ifric23`
   - `ifrs18`
   - `ifrs7`
   - `ias32`
   - `ias29`
   - `ps2`
   - `ifrs1`
   - `ifrs17`
   - `ifric21`
   - `ifrs5`
   - `ifric6`
   - `ias12`
   - `ias24`
   - `ifrs16`
   - `ias8`
   - `ifric2`
   - `ifrs13`
   - `ias26`
   - `ifric5`
   - `ifrs12`
   - `ifric16`
   - `sic29`
   - `ias20`
   - `ias38`
   - `ifrs8`
   - `ifrs10`
   - `ifric1`
   - `ifrs14`
   - `ias33`
   - `ias2`
   - `ias27`

## Hypothèses
   - La question vise les comptes consolidés.
   - Le dividende intragroupe a donné lieu à la comptabilisation d'une créance/dette intragroupe libellée en devise.
   - La question porte sur la possibilité de documenter une relation de couverture de change, et non sur les effets fiscaux ou juridiques locaux.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, vous ne pouvez pas couvrir le dividende intragroupe en tant que tel. En revanche, vous pouvez documenter une couverture sur le risque de change porté par la créance/dette intragroupe reconnue, mais seulement si cette exposition de change n'est pas intégralement éliminée en consolidation, typiquement entre entités ayant des monnaies fonctionnelles différentes.

## Points Opérationnels

   - Point clé: distinguer le dividende intragroupe éliminé en consolidation de la créance/dette intragroupe monétaire qui porte le risque de change.
   - La documentation doit identifier comme élément couvert la créance/dette monétaire intragroupe et démontrer que les écarts de change affectent le résultat consolidé.
   - Si la créance/dette fait partie d'un investissement net au sens IAS 21, le traitement bascule vers l'OCI puis recyclage à la cession, ce qui change l'analyse.
   - Si le groupe n'applique pas la comptabilité de couverture ou si les conditions ne sont pas remplies, IAS 21 s'applique directement aux écarts de change.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilité de couverture IFRS 9 | OUI SOUS CONDITIONS | - La créance/dette intragroupe doit être un élément monétaire libellé dans une devise créant un risque de change entre entités ayant des monnaies fonctionnelles différentes.<br>- Le risque de change doit affecter le résultat consolidé, c'est-à-dire ne pas être totalement éliminé en consolidation. |
| 2. Comptabilité de couverture IAS 39 | OUI SOUS CONDITIONS | - L'entité doit être dans le champ où IAS 39 reste utilisée pour la couverture.<br>- La créance/dette liée au dividende doit constituer un élément monétaire intragroupe générant des écarts de change non totalement éliminés en consolidation. |
| 3. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Comptabilité de couverture IFRS 9
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette intragroupe doit être un élément monétaire libellé dans une devise créant un risque de change entre entités ayant des monnaies fonctionnelles différentes.
   - Le risque de change doit affecter le résultat consolidé, c'est-à-dire ne pas être totalement éliminé en consolidation.

**Raisonnment**:
Dans cette situation, la documentation de couverture en consolidation n'est possible que sur le risque de change de la créance/dette intragroupe reconnue, si cette exposition affecte le résultat consolidé. IFRS 9 exclut en principe les éléments intragroupe, sauf pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation.

**Implications pratiques**: Documenter la couverture sur la créance/dette intragroupe monétaire et non sur le dividende intragroupe en tant que distribution.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group unless there is a related external transaction.

### 2. Comptabilité de couverture IAS 39
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L'entité doit être dans le champ où IAS 39 reste utilisée pour la couverture.
   - La créance/dette liée au dividende doit constituer un élément monétaire intragroupe générant des écarts de change non totalement éliminés en consolidation.

**Raisonnment**:
Si le groupe applique encore IAS 39 pour la couverture autorisée, la logique est la même dans ce cas. Les opérations intragroupe ne sont pas des éléments couverts en consolidation, sauf l'exception visant le risque de change d'un élément monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés.

**Implications pratiques**: Sous IAS 39 également, la couverture ne vise pas le dividende intragroupe comme tel, mais l'exposition FX sur la créance/dette monétaire reconnue.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - AG99A
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group unless there is a related external transaction.

### 3. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut ou en complément de la couverture, IAS 21 reste le modèle de base applicable à cette créance/dette intragroupe en devise. En consolidation, un élément monétaire intragroupe ne peut pas être éliminé sans faire apparaître l'effet des variations de change; si l'item n'est pas un quasi-investissement net, ces écarts vont en résultat.

**Implications pratiques**: Sans relation de couverture éligible, les écarts de change sur la créance/dette intragroupe sont comptabilisés selon IAS 21.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items or on translating monetary items ... shall be recognised in profit or loss
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements
 - 32
    >such exchange differences shall be recognised initially in other comprehensive income