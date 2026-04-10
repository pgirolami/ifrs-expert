# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ias21`
   - `ifrs9`
   - `ias32`
   - `ifric17`
   - `ifrs19`
   - `ifrs7`
   - `ifrs12`
   - `ifric2`
   - `ifric16`
   - `ias7`
   - `sic25`
   - `ps1`
   - `ifric14`

## Hypothèses
   - La question vise les états financiers consolidés.
   - Le dividende intragroupe est libellé dans une devise autre que la monnaie fonctionnelle d’au moins une des entités du groupe.
   - Le dividende a déjà été déclaré et a donné lieu à la comptabilisation d’une créance intragroupe, donc l’exposition porte sur un élément monétaire reconnu.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, cela peut être recevable si la créance de dividende constitue un élément monétaire intragroupe exposé à un risque de change non totalement éliminé. En revanche, la documentation comme couverture de flux de trésorerie d’une transaction future n’est pas adaptée une fois la créance reconnue, et la couverture d’investissement net ne vise pas ce cas.

## Points Opérationnels

   - Le point clé est le moment de désignation : après comptabilisation de la créance, l’analyse doit porter sur un poste monétaire reconnu, pas sur un flux futur.
   - La recevabilité dépend du niveau de reporting : l’exception IFRS 9 pour un poste monétaire intragroupe vaut en comptes consolidés.
   - Il faut vérifier que l’écart de change sur la créance n’est pas totalement éliminé en consolidation, ce qui suppose des monnaies fonctionnelles différentes.
   - Si la relation est documentée, les références normatives centrales sont IAS 21.45 et IFRS 9.6.3.6.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie d’une transaction intragroupe future | NON | - (non spécifiées) |
| 2. Couverture de juste valeur d’un poste monétaire intragroupe | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation. |
| 3. Couverture d’investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de flux de trésorerie d’une transaction intragroupe future
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans la situation décrite, le dividende a déjà donné lieu à la reconnaissance d’une créance en consolidation. L’exposition n’est donc plus une transaction intragroupe future hautement probable, mais un poste monétaire déjà comptabilisé. L’exception IFRS 9 pour les transactions intragroupe futures affectant le résultat consolidé ne correspond plus au fait générateur décrit.

**Implications pratiques**: La documentation en cash flow hedge ne convient pas pour une créance de dividende déjà reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 2. Couverture de juste valeur d’un poste monétaire intragroupe
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.

**Raisonnment**:
C’est l’approche qui correspond au cas décrit si la créance de dividende est un poste monétaire intragroupe entre entités de monnaies fonctionnelles différentes. IAS 21 précise que les écarts de change sur un actif ou passif monétaire intragroupe ne sont pas totalement éliminés en consolidation; IFRS 9 permet alors de désigner ce risque de change comme élément couvert en consolidation.

**Implications pratiques**: Si ces conditions sont remplies, la documentation de couverture du risque de change sur la créance est recevable en consolidation.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 45
    >such an exchange difference is recognised in profit or loss

### 3. Couverture d’investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait couvert décrit est une créance de dividende intragroupe déjà reconnue, et non un investissement net dans une activité étrangère. Le modèle de net investment hedge vise le risque de change sur les actifs nets d’une opération étrangère, avec écarts en OCI jusqu’à la cession. Ce n’est pas la qualification naturelle d’une créance de dividende déclarée.

**Implications pratiques**: Cette base de documentation n’est pas appropriée pour un dividende intragroupe devenu créance.

**Référence**:
 - 2
    >The item being hedged ... may be an amount of net assets
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 45
    >if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income