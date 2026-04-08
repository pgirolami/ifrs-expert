# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ias26`
   - `ias34`
   - `ifrs3`
   - `ias38`
   - `ias24`
   - `ias19`
   - `ifrs11`
   - `ias2`
   - `ifric6`
   - `ias21`
   - `ifric22`
   - `ifrs18`
   - `ifric16`
   - `ias28`
   - `ias40`
   - `sic25`
   - `ifric2`
   - `ias41`
   - `ifrs9`
   - `ias27`
   - `ifrs8`
   - `ifrs12`
   - `ias33`
   - `ifrs2`
   - `ifrs16`
   - `ias20`
   - `ias29`
   - `ifrs17`
   - `ifrs7`
   - `ifrs1`
   - `ifrs14`
   - `ias16`
   - `ifric12`
   - `ifric23`
   - `ifrs19`
   - `ps2`
   - `ifric7`
   - `ias7`
   - `ias37`
   - `ifric21`
   - `ias8`
   - `ias36`
   - `ias10`
   - `ias32`
   - `ifric17`
   - `ifrs13`
   - `ifrs15`
   - `ifrs6`
   - `ifric5`
   - `ias39`
   - `ias12`
   - `ifrs5`
   - `ias23`
   - `ps1`
   - `ifric14`
   - `ifric19`
   - `ifrs10`
   - `ifric1`
   - `sic29`

## Hypothèses
   - La question vise les états financiers consolidés IFRS.
   - La créance de dividende intragroupe a déjà été comptabilisée et constitue donc un poste monétaire intragroupe.
   - La créance est libellée dans une devise telle que les écarts de change ne sont pas entièrement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais en pratique seulement si la créance de dividende constitue un poste monétaire intragroupe exposé à un risque de change non entièrement éliminé en consolidation. Dans ce cas, la voie IFRS pertinente est la couverture de juste valeur, pas la couverture de flux de trésorerie.

## Points Opérationnels

   - Le point déterminant est de qualifier la créance de dividende comme poste monétaire intragroupe et de vérifier que son risque de change affecte bien le résultat consolidé.
   - Si cette condition est satisfaite, la documentation devrait viser une couverture de juste valeur du risque de change, et non une couverture de flux de trésorerie.
   - À défaut de couverture qualifiante, IAS 21 s’applique : conversion au cours de clôture et écart de change en résultat consolidé.
   - Le simple fait qu’il s’agisse d’un dividende intragroupe n’empêche pas l’analyse; ce qui compte est l’existence d’un poste monétaire en devise et l’absence d’élimination complète du risque de change en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Le risque de change doit générer des gains ou pertes de change non entièrement éliminés en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, la question porte sur une créance de dividende déjà comptabilisée. Ce n’est pas une transaction future hautement probable, mais un poste monétaire reconnu. La logique IFRS des exceptions intragroupe en consolidation pour le change vise surtout les transactions intragroupe futures hautement probables qui affecteront le résultat consolidé, ce qui ne correspond pas à ce fait précis.

**Implications pratiques**: La documentation de couverture en cash flow hedge n’est pas la base adaptée pour cette créance de dividende déjà reconnue.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - 80
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Le risque de change doit générer des gains ou pertes de change non entièrement éliminés en consolidation.

**Raisonnment**:
La créance de dividende reconnue est, sous l’hypothèse retenue, un poste monétaire intragroupe. En consolidation, un poste monétaire intragroupe en devise peut rester exposé à des écarts de change non entièrement éliminés; dans ce cas, le risque de change peut être désigné comme élément couvert. Comme il s’agit d’un actif reconnu, le modèle pertinent est la couverture de juste valeur.

**Implications pratiques**: Si ces conditions sont remplies, une documentation de couverture en fair value hedge est envisageable dans les comptes consolidés.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividende à recevoir comptabilisée, donc un flux de règlement intragroupe attendu, et non un élément dont le règlement n’est ni planifié ni probable dans un avenir prévisible. Le traitement d’investissement net vise un poste monétaire faisant, en substance, partie de l’investissement net dans une activité étrangère; ce n’est pas le cas normal d’un dividende à recevoir.

**Implications pratiques**: La couverture d’investissement net n’est généralement pas appropriée pour une créance de dividende intragroupe reconnue.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 15
    >An item for which settlement is neither planned nor likely to occur in the foreseeable future is, in substance, a part of the entity’s net investment
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture qualifiante, la créance de dividende en devise suit IAS 21. Comme il s’agit d’un poste monétaire en devise, il est converti au cours de clôture et les écarts de change sont reconnus en résultat, sauf cas particulier d’investissement net. C’est donc le traitement de base applicable dans votre situation.

**Implications pratiques**: Sans hedge accounting qualifiant, les écarts de change sur la créance intragroupe passent en résultat consolidé.

**Référence**:
 - 23(a)
    >foreign currency monetary items shall be translated using the closing rate
 - 28
    >Exchange differences ... shall be recognised in profit or loss
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations