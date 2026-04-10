# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifric17`
   - `ifrs9`
   - `ifrs18`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic25`
   - `ifric16`
   - `sic29`
   - `ifric19`

## Hypothèses
   - La créance de dividende intragroupe a été comptabilisée avant consolidation et constitue un poste monétaire.
   - La créance et la dette correspondante sont libellées dans une devise étrangère par rapport à la monnaie fonctionnelle d’au moins une entité du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, une documentation de couverture peut être envisagée sur le risque de change de la créance de dividende intragroupe si cette créance est un poste monétaire entre entités de monnaies fonctionnelles différentes et si les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, le modèle pertinent est celui de la couverture de juste valeur, pas celui de cash flow hedge ni celui de couverture d’investissement net.

## Points Opérationnels

   - Le point clé est le niveau de reporting: en comptes consolidés, un poste intragroupe n’est éligible qu’au titre de l’exception visant le risque de change d’un poste monétaire intragroupe.
   - Le timing compte: une fois le dividende déclaré et la créance comptabilisée, l’analyse relève d’un élément reconnu, non d’une transaction future hautement probable.
   - La justification technique doit démontrer que les écarts de change sur la créance ne sont pas totalement éliminés en consolidation du fait de monnaies fonctionnelles différentes.
   - Le modèle de couverture à documenter, si les conditions sont remplies, est celui d’une couverture de juste valeur du risque de change sur la créance reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un poste monétaire intragroupe<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre cas, le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance à recevoir. Le sujet n’est donc plus une transaction future hautement probable, mais un actif déjà reconnu. L’exception IFRS 9 pour certaines transactions intragroupe futures en devise ne vise pas ce fait précis.

**Implications pratiques**: Ce modèle n’est pas adapté si le dividende est déjà constaté en créance dans les comptes avant consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un poste monétaire intragroupe
   - les entités concernées ont des monnaies fonctionnelles différentes
   - les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation

**Raisonnment**:
La créance de dividende déjà comptabilisée est, dans cette lecture, un actif reconnu. En consolidation, les éléments intragroupe ne sont en principe éligibles que s’ils concernent une partie externe, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. C’est précisément le cas visé si les entités ont des monnaies fonctionnelles différentes.

**Implications pratiques**: Si ces conditions sont réunies, la documentation de couverture peut être mise en place au niveau consolidé sur le risque de change de la créance reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise l’exposition de change sur un investissement net dans une activité à l’étranger. Votre question porte sur une créance de dividende intragroupe déjà reconnue, c’est-à-dire sur un flux déclaré et détaché de l’investissement net lui-même. Les extraits fournis ne permettent pas de traiter cette créance comme une couverture d’investissement net.

**Implications pratiques**: Ce n’est pas le bon modèle de couverture pour un dividende intragroupe déjà mis en créance.

**Référence**:
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity