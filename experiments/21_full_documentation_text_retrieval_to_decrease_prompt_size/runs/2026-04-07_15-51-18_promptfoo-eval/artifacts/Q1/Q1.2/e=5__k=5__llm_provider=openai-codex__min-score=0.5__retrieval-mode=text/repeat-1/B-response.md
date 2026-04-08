# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs6`
   - `ias7`
   - `ias29`
   - `ifrs2`
   - `ps2`
   - `ias26`
   - `ifrs16`
   - `ifrs11`
   - `sic25`
   - `ifrs8`
   - `ifrs18`
   - `ifrs12`
   - `ias24`
   - `ifric2`
   - `ifrs13`
   - `ias40`
   - `ifrs17`
   - `ps1`
   - `ias32`
   - `ias23`
   - `ias10`
   - `ias12`
   - `ias38`
   - `ias2`
   - `ifric12`
   - `ias19`
   - `ifrs10`
   - `ias20`
   - `ias21`
   - `ias28`
   - `ifric21`
   - `ifric17`
   - `sic29`
   - `ias34`
   - `ifric1`
   - `ias37`
   - `ifrs1`
   - `ifrs7`
   - `ifric16`
   - `ifrs14`
   - `ias41`
   - `ifrs3`
   - `ias16`
   - `ifric14`
   - `ifrs15`
   - `ifric19`
   - `ifrs19`
   - `ias27`
   - `ifrs5`
   - `ifrs9`
   - `ifric5`
   - `ias39`
   - `ifric23`
   - `ias36`
   - `ifric7`
   - `ias33`
   - `ias8`

## Hypothèses
   - La question porte sur des comptes consolidés IFRS.
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance, donc il ne s’agit plus d’une transaction future hautement probable.
   - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une entité du groupe, de sorte qu’un risque de change existe avant élimination de consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie IFRS pertinente est la couverture de juste valeur sur le risque de change du poste monétaire intragroupe, mais seulement si ce risque de change n’est pas intégralement éliminé en consolidation. La couverture de flux futurs ne convient pas à une créance déjà comptabilisée, et la couverture d’investissement net ne convient que si la créance fait partie de l’investissement net dans une activité étrangère.

## Points Opérationnels

   - Qualifier d’abord la créance de dividende comme poste monétaire intragroupe en devise, puis vérifier si l’écart de change subsiste en résultat consolidé avant règlement.
   - Si vous documentez une couverture, la cible IFRS à retenir dans ce cas est la juste valeur sur le risque de change du poste reconnu, pas une couverture de flux futurs.
   - La couverture d’investissement net n’est envisageable que si la créance est, en substance, une composante de financement à long terme de l’activité étrangère ; ce n’est pas le cas par défaut d’un dividende déclaré.
   - Même avec IFRS 19, l’analyse de fond reste celle des autres IFRS ; seule la couche de disclosures est remplacée par IFRS 19.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.<br>- La documentation de couverture doit viser le risque de change de ce poste reconnu. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation de change ordinaire | OUI | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le dividende intragroupe a déjà été comptabilisé en créance. Ce n’est donc plus une transaction future hautement probable mais un poste monétaire existant.
Le modèle de couverture de flux de trésorerie visé dans le contexte concerne surtout des transactions intragroupe futures ; il ne correspond pas à ce fait précis.

**Implications pratiques**: Cette documentation ne convient pas pour couvrir la partie change d’une créance de dividende déjà reconnue.

**Référence**:
 - 80
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements
 - 4
    >if an entity applying this Standard applies IFRS 8 Operating Segments, IFRS 17 Insurance Contracts or IAS 33 Earnings per Share, it shall apply all the disclosure requirements in those Standards.

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - La documentation de couverture doit viser le risque de change de ce poste reconnu.

**Raisonnment**:
Une créance de dividende intragroupe en devise est, dans les faits décrits, un poste monétaire existant. Le contexte IFRS admet qu’un poste monétaire intragroupe puisse être un élément couvert en consolidation si le risque de change n’est pas totalement éliminé.
C’est donc l’approche de couverture la plus adaptée dans cette situation, sous réserve que la créance génère bien des écarts de change conservés dans le résultat consolidé avant règlement.

**Implications pratiques**: C’est l’unique modèle de couverture IFRS réellement pertinent ici pour documenter la composante change du dividende comptabilisé.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations
 - 28
    >Exchange differences arising on the settlement of monetary items or on translating monetary items ... shall be recognised in profit or loss

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise le risque de change d’un investissement net dans une activité étrangère. Une créance de dividende intragroupe n’est pas, par nature, la même chose qu’un investissement net.
Dans les faits donnés, rien n’indique que cette créance fasse partie du financement à long terme assimilable à un investissement net ; elle correspond plutôt à un dividende déclaré et à régler.

**Implications pratiques**: À défaut d’élément montrant que la créance fait partie de l’investissement net, cette documentation ne doit pas être retenue.

**Référence**:
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 8
    >This Interpretation applies only to hedges of net investments in foreign operations

### 4. Comptabilisation de change ordinaire
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
En l’absence de couverture éligible, le traitement de base est IAS 21 sur les postes monétaires en devise. Pour un poste intragroupe monétaire, les écarts de change ne sont pas nécessairement neutralisés en consolidation.
Cette approche constitue donc le traitement plancher dans votre cas, même si une couverture de juste valeur est éventuellement mise en place.

**Implications pratiques**: À défaut de couverture de juste valeur valide, les écarts de change vont en résultat selon IAS 21.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items or on translating monetary items ... shall be recognised in profit or loss
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations
 - 2
    >An entity electing to apply this Standard applies the requirements in other IFRS Accounting Standards, except for the disclosure requirements.