# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs9`
   - `ifrs12`
   - `ias37`
   - `ifric19`
   - `ifric16`

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance dans les comptes individuels avant la consolidation.
   - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle d'au moins une entité du groupe.
   - L'analyse porte sur les comptes consolidés et sur la seule composante de risque de change de cette créance intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie pertinente est la couverture de juste valeur, mais seulement si la créance intragroupe constitue un poste monétaire générant un risque de change non totalement éliminé en consolidation. La couverture de flux de trésorerie n'est pas adaptée à une créance déjà comptabilisée, et la couverture d'investissement net vise une autre exposition.

## Points Opérationnels

   - Le niveau d'analyse pertinent est la consolidation : la recevabilité IFRS dépend de l'existence d'un risque de change intragroupe non totalement éliminé en consolidation.
   - Le moment est déterminant : une fois le dividende comptabilisé en créance, l'exposition est un poste reconnu et non une transaction future hautement probable.
   - La documentation doit être ciblée sur la seule composante change de la créance et rédigée au niveau du groupe.
   - Si les écarts de change sur la créance sont totalement éliminés en consolidation, l'intérêt et l'éligibilité de la couverture en comptes consolidés tombent.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Le risque de change doit générer des écarts qui ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Le risque de change doit générer des écarts qui ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est déjà comptabilisée : il s'agit donc d'un poste reconnu, ce qui correspond au modèle de fair value hedge parmi les approches proposées. En consolidation, un poste intragroupe ne peut être couvert que par exception s'il s'agit d'un poste monétaire intragroupe dont l'effet de change n'est pas totalement éliminé, notamment entre entités ayant des monnaies fonctionnelles différentes.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé sur la créance intragroupe reconnue, limitée au risque de change effectivement exposé en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise des transactions prévues hautement probables ou, par exception, certaines transactions intragroupe prévues en devise dans les comptes consolidés. Or ici le dividende intragroupe est déjà comptabilisé en créance ; l'exposition n'est donc plus une transaction future prévue mais un poste reconnu.

**Implications pratiques**: La documentation en cash flow hedge ne correspond pas au fait générateur décrit, car le dividende n'est plus au stade de flux futur prévu.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net concerne le risque de change attaché à un investissement net dans une activité à l'étranger, pas la créance de dividende intragroupe elle-même. Le fait décrit est une créance de dividende reconnue ; ce n'est pas, en tant que telle, l'exposition de conversion visée par ce modèle.

**Implications pratiques**: Cette documentation n'est pas la bonne réponse pour couvrir la partie change d'une créance de dividende intragroupe déjà enregistrée.

**Référence**:
 - 6.3.1
    >The hedged item can be ... a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation