# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Dans un contexte de consolidation IFRS, une relation de couverture peut-elle être documentée au titre du risque de change sur des dividendes intragroupe comptabilisés à recevoir ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs17`
   - `ias24`
   - `ifrs12`
   - `ifrs19`
   - `ifric17`
   - `ifric16`
   - `sic25`
   - `ias7`
   - `ifric14`
   - `ifric2`
   - `ps1`

## Hypothèses
   - La question vise les états financiers consolidés en IFRS.
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance à recevoir chez une entité du groupe et en dette à payer chez une autre.
   - La créance et la dette de dividende sont libellées dans une devise créant un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une relation de couverture de juste valeur si le dividende intragroupe comptabilisé à recevoir constitue un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation. La couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas à ce fait précis.

## Points Opérationnels

   - Vérifier si la créance de dividende et la dette correspondante sont bien des postes monétaires entre entités ayant des monnaies fonctionnelles différentes.
   - Confirmer que l’écart de change sur ce dividende intragroupe affecte bien le résultat consolidé et n’est pas entièrement éliminé à la consolidation.
   - Si ces conditions sont remplies, la documentation doit viser le risque de change du poste monétaire intragroupe, pas le dividende en tant que simple flux intragroupe.
   - La qualification en couverture d’investissement net ne doit pas être retenue pour une créance de dividende déjà comptabilisée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le dividende à recevoir doit constituer un poste monétaire intragroupe.<br>- Les deux entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Le risque de change doit générer des écarts non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende à recevoir doit constituer un poste monétaire intragroupe.
   - Les deux entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Le risque de change doit générer des écarts non totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, le dividende intragroupe comptabilisé à recevoir est un poste reconnu, et non une transaction future. En consolidation, IFRS 9 n’autorise en principe que des éléments avec des tiers externes, sauf exception pour un poste monétaire intragroupe exposé à des écarts de change non totalement éliminés. IAS 21 précise justement que ces écarts sur postes monétaires intragroupe entre monnaies fonctionnelles différentes ne disparaissent pas nécessairement en consolidation.

**Implications pratiques**: La documentation de couverture n’est envisageable que sur le risque de change résiduel conservé dans les comptes consolidés.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit porte sur des dividendes intragroupe déjà comptabilisés à recevoir, donc sur un actif monétaire reconnu. Or la logique de la couverture de flux de trésorerie vise notamment les transactions futures prévues et hautement probables. Ce modèle ne correspond pas au cas d’une créance de dividende déjà constatée.

**Implications pratiques**: Une créance de dividende déjà reconnue ne devrait pas être documentée comme couverture de flux de trésorerie dans ce cas.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net vise le risque de change sur les actifs nets d’une opération étrangère, non sur une créance de dividende intragroupe. IFRIC 16 circonscrit ce modèle au risque de change découlant d’un investissement net dans une activité à l’étranger. Un dividende à recevoir est un poste distinct de cet investissement net.

**Implications pratiques**: Il ne faut pas assimiler une créance de dividende intragroupe à un investissement net couvert.

**Référence**:
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation
 - 7
    >applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 8
    >This Interpretation applies only to hedges of net investments in foreign operations