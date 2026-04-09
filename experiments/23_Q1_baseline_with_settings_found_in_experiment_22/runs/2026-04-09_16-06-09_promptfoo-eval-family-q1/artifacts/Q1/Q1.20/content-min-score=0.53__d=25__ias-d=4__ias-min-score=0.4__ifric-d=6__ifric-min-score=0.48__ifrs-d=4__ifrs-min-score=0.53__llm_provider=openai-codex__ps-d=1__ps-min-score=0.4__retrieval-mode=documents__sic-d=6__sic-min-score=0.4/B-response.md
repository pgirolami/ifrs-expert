# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ias39`
   - `ifrs9`
   - `ias21`
   - `ifric16`
   - `ifrs19`
   - `ias24`
   - `ifrs18`
   - `ias29`
   - `ifrs12`
   - `ifric17`
   - `ifric21`
   - `sic25`
   - `sic29`

## Hypothèses
   - L’exposition visée est un risque de change sur une créance de dividendes intragroupe reconnue dans les états financiers consolidés.
   - La question porte sur la possibilité de désigner cette exposition comme élément couvert en hedge accounting dans les comptes consolidés.
   - La créance est traitée comme un élément monétaire générant des écarts de change en résultat selon IAS 21, sauf si elle fait en substance partie d’un investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, seulement si la créance de dividendes intragroupe constitue un élément monétaire dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, une documentation de hedge accounting peut être envisagée ; sinon, la règle générale d’exclusion des éléments intragroupe s’applique.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que la créance de dividendes est bien un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés.
   - Si cette démonstration n’est pas possible, aucune hedge documentation IFRS ne peut viser cette créance dans les comptes consolidés.
   - Si elle est possible, la documentation doit être mise en place dès l’origine de la relation de couverture avec désignation formelle, risque couvert et méthode d’évaluation de l’efficacité.
   - En l’absence de hedge accounting qualifiant, les écarts de change suivent IAS 21 et passent en résultat.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividendes doit être un élément monétaire intragroupe.<br>- Les écarts de change correspondants doivent ne pas être totalement éliminés en consolidation.<br>- La relation de couverture doit satisfaire aux critères formels de désignation et d’efficacité applicables. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change sans hedge accounting | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividendes doit être un élément monétaire intragroupe.
   - Les écarts de change correspondants doivent ne pas être totalement éliminés en consolidation.
   - La relation de couverture doit satisfaire aux critères formels de désignation et d’efficacité applicables.

**Raisonnment**:
Dans les comptes consolidés, un élément intragroupe ne peut en principe pas être désigné comme élément couvert. Toutefois, IAS 39 et IFRS 9 prévoient une exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il crée des gains ou pertes de change non totalement éliminés en consolidation. Si la créance de dividendes répond à ce cas, une couverture de juste valeur est envisageable car le risque couvert affecte le résultat.

**Implications pratiques**: Possible en consolidation uniquement si l’exposition de change subsiste réellement après éliminations ; sinon, pas de fair value hedge documentable.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 86(a)
    >fair value hedge: a hedge of the exposure to changes in fair value
 - 88
    >At the inception of the hedge there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite vise une créance déjà reconnue, dont la sensibilité provient d’écarts de change sur un montant monétaire existant. Le contexte fourni rattache l’exception intragroupe à un élément monétaire exposé à des gains ou pertes de change non éliminés, ce qui correspond ici à une exposition sur poste reconnu, pas à une transaction future hautement probable à documenter en cash flow hedge.

**Implications pratiques**: Dans ce cas précis, la piste opérationnelle n’est pas la cash flow hedge mais, le cas échéant, une hedge documentation de type juste valeur.

**Référence**:
 - 86(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 88(c)
    >For cash flow hedges, a forecast transaction ... must be highly probable
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividendes intragroupe n’est pas, en elle-même, le risque de change d’un investissement net dans une activité à l’étranger. IFRIC 16 et IAS 21 visent le montant de l’intérêt dans les actifs nets d’une activité étrangère, ou un élément monétaire dont le règlement n’est ni planifié ni probable à court terme ; une créance de dividendes n’est pas décrite ainsi ici.

**Implications pratiques**: La documentation de net investment hedge ne paraît pas adaptée à une créance de dividendes exigible figurant en consolidation.

**Référence**:
 - 2
    >The item being hedged ... may be an amount of net assets
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 15
    >An item for which settlement is neither planned nor likely to occur in the foreseeable future is, in substance, a part of the entity’s net investment

### 4. Comptabilisation du change sans hedge accounting
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut d’une désignation admissible en couverture, IAS 21 constitue le traitement de base. Les écarts de change sur un élément monétaire en devise sont reconnus en résultat, sauf cas particuliers comme l’investissement net. Cette approche s’applique nécessairement si les conditions de l’exception intragroupe pour hedge accounting ne sont pas remplies.

**Implications pratiques**: En l’absence de couverture qualifiante, la volatilité de change de la créance reste comptabilisée selon IAS 21.

**Référence**:
 - 23(a)
    >foreign currency monetary items shall be translated using the closing rate
 - 28
    >Exchange differences ... shall be recognised in profit or loss
 - 5
    >This Standard does not apply to hedge accounting for foreign currency items