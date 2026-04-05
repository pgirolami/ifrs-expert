# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Un dividende intragroupe a donné lieu à la comptabilisation d’un montant à recevoir au sein du périmètre consolidé. Peut-on, dans ces circonstances, documenter une couverture portant sur le risque de change afférent à cette exposition ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée au niveau des états financiers consolidés.
   - Le dividende intragroupe a fait naître une créance intragroupe monétaire comptabilisée, exposée à un risque de change.
   - Cette créance est libellée dans une devise telle qu’un écart de change peut exister entre les entités concernées.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si le risque de change de la créance intragroupe n’est pas entièrement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur ; les modèles de couverture de flux de trésorerie et de couverture d’investissement net ne correspondent pas, en principe, à cette situation.

## Points Opérationnels

   - Vérifier en premier lieu si les écarts de change sur la créance intragroupe restent en résultat consolidé et ne sont pas entièrement éliminés à la consolidation.
   - La documentation doit être établie dès l’origine de la relation de couverture et identifier l’instrument de couverture, la créance couverte, le risque de change couvert et le ratio de couverture.
   - Si l’exposition ne remplit pas l’exception applicable aux postes monétaires intragroupe, aucune désignation comme élément couvert n’est possible en consolidation.
   - Le fait générateur ici est la créance déjà comptabilisée issue du dividende ; il ne s’agit pas d’une transaction intragroupe future hautement probable ni d’un investissement net.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le risque de change sur la créance intragroupe doit donner lieu à des gains ou pertes de change non totalement éliminés en consolidation.<br>- Cela suppose en pratique que les entités concernées aient des monnaies fonctionnelles différentes. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le risque de change sur la créance intragroupe doit donner lieu à des gains ou pertes de change non totalement éliminés en consolidation.
   - Cela suppose en pratique que les entités concernées aient des monnaies fonctionnelles différentes.

**Raisonnment**:
La créance de dividende est un actif monétaire intragroupe déjà comptabilisé. En consolidation, un poste intragroupe n’est en principe pas éligible, sauf pour son risque de change si les écarts de change ne sont pas totalement éliminés ; dans ce cas, il peut être désigné comme élément couvert. Le modèle de juste valeur correspond ici à une exposition d’un actif comptabilisé aux variations dues au risque de change.

**Implications pratiques**: Une documentation de couverture peut être mise en place sur le risque de change de la créance, sous réserve de satisfaire les critères de désignation et d’efficacité.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, l’exposition naît d’une créance intragroupe monétaire déjà comptabilisée au titre d’un dividende déclaré. Le sujet principal est la réévaluation de ce poste monétaire en devise, non la variabilité de flux futurs d’une transaction hautement probable. Le modèle de flux de trésorerie n’est donc pas le traitement adapté au cas décrit.

**Implications pratiques**: La documentation devrait être orientée vers une couverture de juste valeur plutôt que vers une couverture de flux de trésorerie.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe, pas sur le risque de change attaché à un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change d’un investissement net en opérations étrangères. Les faits décrits ne relèvent pas de cette catégorie.

**Implications pratiques**: Le modèle de couverture d’investissement net ne doit pas être retenu pour cette créance de dividende.

**Référence**:
 - 6.3.1
    >A hedged item can be ... a net investment in a foreign operation
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations