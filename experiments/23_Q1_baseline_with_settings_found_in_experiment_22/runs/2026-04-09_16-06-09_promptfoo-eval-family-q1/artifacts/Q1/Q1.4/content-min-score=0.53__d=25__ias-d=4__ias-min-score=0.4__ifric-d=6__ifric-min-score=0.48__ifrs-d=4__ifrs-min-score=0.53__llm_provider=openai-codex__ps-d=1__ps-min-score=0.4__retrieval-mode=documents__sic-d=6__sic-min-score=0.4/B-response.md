# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - La question porte sur des états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe a été déclaré et a donné lieu à la comptabilisation d’une créance et d’une dette intragroupe avant élimination de consolidation.
   - La créance et la dette sont libellées dans une devise générant un risque de change entre entités du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une couverture peut être documentée sur la composante change d’un dividende intragroupe seulement si, après reconnaissance de la créance, l’élément est traité comme un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. En pratique, cela oriente vers une couverture de juste valeur, pas vers une couverture de flux de trésorerie.

## Points Opérationnels

   - Le point de départ est la date de reconnaissance de la créance de dividende : avant cette date, la logique serait celle d’une transaction future ; après cette date, celle d’un poste reconnu.
   - En consolidation, il faut démontrer explicitement que le risque de change du poste monétaire intragroupe n’est pas totalement éliminé et affecte bien le résultat consolidé.
   - La documentation de couverture doit désigner le risque de change du poste monétaire reconnu, avec une documentation IFRS 9 complète dès l’origine de la relation de couverture.
   - Si aucun écart de change ne subsiste au niveau consolidé après éliminations, aucune désignation de couverture ne peut être maintenue pour cette situation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende constitue un poste monétaire intragroupe<br>- le risque de change sur ce poste affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation<br>- les conditions de désignation et de documentation de couverture d’IFRS 9 sont respectées |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Éliminations de consolidation | OUI SOUS CONDITIONS | - la créance et la dette intragroupe sont éliminées en consolidation<br>- seul un écart de change non totalement éliminé peut rester pertinent au niveau consolidé |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation posée, il existe déjà une créance reconnue : on n’est plus face à une transaction future hautement probable mais à un poste existant. En outre, l’exception IFRS 9 visant les transactions intragroupe futures suppose un impact sur le résultat consolidé, ce qui ne ressort pas ici pour un dividende intragroupe déjà déclaré.

**Implications pratiques**: La documentation en cash flow hedge n’est pas le modèle adapté une fois la créance de dividende comptabilisée.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende constitue un poste monétaire intragroupe
   - le risque de change sur ce poste affecte le résultat consolidé car il n’est pas totalement éliminé en consolidation
   - les conditions de désignation et de documentation de couverture d’IFRS 9 sont respectées

**Raisonnment**:
Ici, une créance a été reconnue : il s’agit donc d’un actif existant, ce qui correspond au champ d’une couverture de juste valeur. En consolidation, un poste intragroupe n’est normalement pas éligible, sauf pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés à la consolidation.

**Implications pratiques**: La documentation doit viser le risque de change du poste monétaire reconnu, et non le dividende intragroupe en tant que flux interne éliminé.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >not in the consolidated financial statements of the group
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise un dividende intragroupe avec créance correspondante, non une exposition de conversion sur un investissement net dans une activité à l’étranger. Le modèle pertinent d’IFRS 9/IFRIC 16 concerne les net assets d’une activité étrangère inclus dans les états financiers, pas une créance de dividende intragroupe.

**Implications pratiques**: Il ne faut pas documenter cette relation comme une couverture d’investissement net.

**Référence**:
 - 2
    >foreign currency risk arising from a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets

### 4. Éliminations de consolidation
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance et la dette intragroupe sont éliminées en consolidation
   - seul un écart de change non totalement éliminé peut rester pertinent au niveau consolidé

**Raisonnment**:
En consolidation, la créance et la dette de dividende intragroupe sont éliminées intégralement. Toutefois, cette élimination n’empêche pas, dans le cas étroit admis par IFRS 9, qu’un risque de change sur un poste monétaire intragroupe subsiste au niveau du résultat consolidé et soit alors potentiellement couvert.

**Implications pratiques**: L’analyse doit partir des éliminations de consolidation avant de conclure sur l’existence d’un risque de change encore observable au niveau consolidé.

**Référence**:
 - B86
    >eliminate in full intragroup assets and liabilities
 - 6.3.6
    >gains or losses that are not fully eliminated on consolidation
 - 4
    >Intragroup related party transactions and outstanding balances are eliminated