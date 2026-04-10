# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - La question vise les états financiers consolidés, et non les états financiers séparés ou individuels.
   - Un dividende intragroupe a été déclaré, et une créance/dette intragroupe correspondante a été comptabilisée avant les éliminations de consolidation.
   - La question porte sur la désignation d'une relation de couverture du risque de change selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, ce n’est pas le dividende intragroupe en tant que tel qui peut être couvert. Cela n’est possible que si la créance/dette intragroupe constitue un poste monétaire en devise dont les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.

## Points Opérationnels

   - Vérifier la monnaie fonctionnelle des deux entités: l’exception IFRS 9 vise les postes monétaires intragroupe entre entités à monnaies fonctionnelles différentes.
   - Documenter la couverture au niveau consolidé sur la créance/dette monétaire et sur son impact attendu en résultat consolidé, pas sur le dividende éliminé en tant que tel.
   - Tester que les écarts de change sur la créance/dette ne sont pas intégralement éliminés à la consolidation.
   - La simple reconnaissance du droit au dividende dans les comptes séparés ne suffit pas, en elle-même, à rendre la relation de couverture admissible en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilité de couverture selon IFRS 9 | OUI SOUS CONDITIONS | - la créance/dette de dividende est un poste monétaire intragroupe<br>- elle est libellée dans une devise générant des écarts de change entre entités du groupe à monnaies fonctionnelles différentes<br>- ces écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé |
| 2. Comptabilisation en consolidation selon IFRS 10 | NON | - (non spécifiées) |
| 3. États financiers séparés selon IAS 27 | NON | - (non spécifiées) |

### 1. Comptabilité de couverture selon IFRS 9
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance/dette de dividende est un poste monétaire intragroupe
   - elle est libellée dans une devise générant des écarts de change entre entités du groupe à monnaies fonctionnelles différentes
   - ces écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé

**Raisonnment**:
Dans des comptes consolidés, IFRS 9 interdit en principe de désigner des transactions intragroupe comme éléments couverts. Toutefois, une exception existe pour le risque de change d’un poste monétaire intragroupe si les gains/pertes de change ne sont pas totalement éliminés en consolidation. Donc, la documentation peut être mise en place seulement si la créance de dividende reconnue crée une telle exposition résiduelle en résultat consolidé.

**Implications pratiques**: La documentation doit viser le risque de change du poste monétaire intragroupe, pas le dividende intragroupe comme flux interne en lui-même.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Comptabilisation en consolidation selon IFRS 10
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
En consolidation, les créances/dettes, produits/charges et flux intragroupe sont éliminés en totalité. Ainsi, le dividende intragroupe et la créance correspondante ne subsistent pas en tant que tels dans les états financiers consolidés. Cette approche ne fonde donc pas, à elle seule, la possibilité de documenter une couverture en consolidation.

**Implications pratiques**: Il faut analyser l’exposition de change résiduelle après éliminations, et non se fonder sur la seule existence de la créance avant consolidation.

**Référence**:
 - B86
    >eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows

### 3. États financiers séparés selon IAS 27
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
IAS 27 explique qu’en états financiers séparés, le dividende d’une filiale est reconnu lorsque le droit à recevoir est établi. Cela peut expliquer pourquoi une créance a été comptabilisée dans les comptes individuels. Mais cette logique ne répond pas à la question posée en consolidation, où l’éligibilité à la couverture dépend d’IFRS 9 et des éliminations de consolidation.

**Implications pratiques**: La reconnaissance en comptes séparés n’est qu’un point de départ comptable; elle ne suffit pas pour justifier une couverture en comptes consolidés.

**Référence**:
 - 12
    >Dividends from a subsidiary ... are recognised ... when the entity’s right to receive the dividend is established