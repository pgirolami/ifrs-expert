# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs19`
   - `ifrs7`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric17`
   - `ifric2`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic7`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une monnaie étrangère du point de vue d’au moins une entité du groupe.
   - La question est analysée au niveau des états financiers consolidés en IFRS.
   - Le dividende a été déclaré et comptabilisé en créance/dette intragroupe, de sorte qu’il existe un poste monétaire intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, une couverture formellement documentée est possible seulement si la créance de dividende constitue un poste monétaire intragroupe exposant le groupe à des écarts de change non intégralement éliminés en consolidation. Dans ce cas, la voie pertinente est la comptabilité de couverture IFRS 9, et non un hedge de flux futurs ni un hedge de net investment, sauf faits différents.

## Points Opérationnels

   - Vérifier que la créance de dividende est bien un poste monétaire intragroupe au moment de la désignation.
   - Documenter dès l’origine la relation de couverture, l’instrument de couverture, le risque de change couvert et les tests d’efficacité requis par IFRS 9.
   - Démontrer en consolidé que le risque de change sur la créance/dette intragroupe n’est pas totalement éliminé, en pratique lorsqu’il existe des monnaies fonctionnelles différentes.
   - Si ces conditions ne sont pas remplies, appliquer uniquement IAS 21 aux écarts de change sur le poste intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe reconnu.<br>- Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation, notamment parce que les entités concernées ont des monnaies fonctionnelles différentes.<br>- La relation de couverture est formellement désignée et documentée conformément à IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe reconnu.
   - Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation, notamment parce que les entités concernées ont des monnaies fonctionnelles différentes.
   - La relation de couverture est formellement désignée et documentée conformément à IFRS 9.

**Raisonnment**:
La créance de dividende déjà comptabilisée est, dans cette situation, un actif reconnu. IFRS 9 admet par exception qu’un poste monétaire intragroupe soit désigné comme élément couvert en consolidé si le risque de change crée des écarts non totalement éliminés. La relation suppose alors une documentation formelle et le respect des critères de couverture.

**Implications pratiques**: Possible en consolidé, mais seulement si l’entité démontre que le risque de change subsiste au niveau du groupe sur la créance intragroupe.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise un dividende intragroupe déjà comptabilisé en créance à recevoir, donc un poste reconnu, et non une transaction future hautement probable. Dans ces faits, le risque porte sur la réévaluation d’un poste monétaire existant, ce qui ne correspond pas au modèle principal de cash flow hedge décrit par IFRS 9.

**Implications pratiques**: Cette voie ne convient pas à une créance de dividende déjà reconnue dans les comptes consolidés.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici est celui d’une créance de dividende intragroupe, pas celui de l’investissement net dans une activité étrangère. IFRIC 16 circonscrit ce modèle au risque de change entre la monnaie fonctionnelle de l’activité étrangère et celle de l’entité mère sur les actifs nets de cette activité.

**Implications pratiques**: À écarter pour un dividende intragroupe comptabilisé en receivable ; ce n’est pas un hedge de net investment.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture qualifiante, IAS 21 s’applique au poste monétaire intragroupe en devise. En consolidé, les soldes intragroupe sont éliminés, mais les effets de change sur un poste monétaire entre entités à monnaies fonctionnelles différentes ne disparaissent pas nécessairement et sont reconnus selon IAS 21.

**Implications pratiques**: Le traitement par défaut est la comptabilisation des écarts de change en consolidation selon IAS 21, sauf si une couverture IFRS 9 qualifie.

**Référence**:
 - 3
    >This Standard shall be applied ... in accounting for transactions and balances in foreign currencies
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations
 - 5
    >This Standard does not apply to hedge accounting for foreign currency items. IFRS 9 applies to hedge accounting.