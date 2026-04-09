# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Documentation consultée**
   - `ias32`
   - `ifric2`
   - `ifrs19`
   - `ifrs7`
   - `ifric17`
   - `ifrs9`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ias24`
   - `ifric16`
   - `ifric19`
   - `sic29`
   - `ifric21`
   - `ps1`
   - `ias37`

## Hypothèses
   - La question porte sur la comptabilité de couverture dans les états financiers consolidés.
   - La créance de dividende intragroupe reconnue génère une exposition de change.
   - La créance est libellée en devise étrangère par rapport à la monnaie fonctionnelle de l'entité qui la comptabilise.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une telle exposition ne peut être désignée comme élément couvert que de façon limitée, via une couverture de juste valeur, si la créance est un poste monétaire intragroupe et si le risque de change affecte le résultat consolidé sans être entièrement éliminé. Les modèles de couverture de flux de trésorerie et de couverture d'investissement net ne correspondent pas à ce fait précis.

## Points Opérationnels

   - Vérifier si la créance de dividende est bien un poste monétaire en devise.
   - Documenter si les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas intégralement éliminés.
   - Si ces critères ne sont pas remplis, la réponse IFRS dans ce cas est non.
   - Ne pas confondre cette créance avec une transaction intragroupe future hautement probable ni avec un investissement net dans une entité étrangère.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe constitue un poste monétaire.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.<br>- Cette exposition de change affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe constitue un poste monétaire.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.
   - Cette exposition de change affecte le résultat consolidé.

**Raisonnment**:
La créance est un actif comptabilisé, ce qui correspond en principe au champ d'une couverture de juste valeur. Toutefois, en consolidation, les éléments intragroupe ne sont normalement pas éligibles, sauf exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Dans cette situation précise, la désignation n'est donc possible que si cette exception est satisfaite.

**Implications pratiques**: La documentation de couverture doit viser uniquement le risque de change de la créance intragroupe remplissant cette exception.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit n'est pas une transaction intragroupe future hautement probable, mais une créance déjà reconnue au titre d'un dividende déclaré. Le modèle de couverture de flux de trésorerie vise une variabilité de flux de trésorerie sur un actif/passif ou une transaction future, alors qu'ici la question porte sur l'exposition de change d'une créance comptabilisée. Dans cette situation, le traitement pertinent n'est donc pas la couverture de flux de trésorerie.

**Implications pratiques**: La créance de dividende reconnue ne doit pas être documentée comme élément couvert en cash flow hedge.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividende intragroupe reconnue, et non le risque de change attaché à un investissement net dans une activité à l'étranger. Le modèle de couverture d'investissement net est réservé à ce risque spécifique. Il ne s'applique donc pas à cette créance de dividende dans les faits exposés.

**Implications pratiques**: Cette exposition de change ne doit pas être classée comme hedge de net investment.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations