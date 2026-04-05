# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>À partir du moment où des dividendes intragroupe sont reconnus en créance dans les comptes consolidés, une problématique de change apparaît. Dans une telle situation, est-il permis de documenter une couverture sur cette composante de risque ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - Le dividende intragroupe est devenu une créance/dette intragroupe monétaire comptabilisée.
   - L'exposition de change provient du fait que les entités concernées ont des monnaies fonctionnelles différentes.
   - La question est analysée dans le cadre des comptes consolidés et du modèle de comptabilité de couverture d'IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais uniquement si le dividende reconnu constitue un élément monétaire intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Dans cette situation, la voie cohérente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d'un investissement net.

## Points Opérationnels

   - Le point clé est le moment où le dividende devient une créance/dette monétaire reconnue : à ce stade, l'analyse se fait sur un élément comptabilisé et non sur une transaction future.
   - En consolidation, la documentation n'est recevable que si le risque de change sur cet élément intragroupe affecte effectivement le résultat consolidé parce qu'il n'est pas entièrement éliminé.
   - La documentation doit être faite au niveau de la relation de couverture IFRS 9 avec désignation formelle, risque couvert identifié et démonstration de l'efficacité selon 6.4.1.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un élément monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.<br>- Le risque couvert est limité au risque de change affectant le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un élément monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.
   - Le risque couvert est limité au risque de change affectant le résultat consolidé.

**Raisonnment**:
Ici, le dividende est supposé déjà comptabilisé en créance/dette intragroupe monétaire. IFRS 9 permet, par exception en consolidation, de désigner le risque de change d'un élément monétaire intragroupe comme élément couvert s'il génère des écarts de change non totalement éliminés; cela cadre avec une couverture d'un actif/passif comptabilisé exposé à une variation de valeur liée à un risque particulier.

**Implications pratiques**: La documentation de couverture doit viser explicitement le risque de change sur la créance/dette intragroupe reconnue, au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le sujet n'est plus une transaction intragroupe future hautement probable mais une créance de dividende déjà comptabilisée. Le texte d'IFRS 9 réserve expressément l'ouverture intragroupe en cash flow hedge aux transactions intragroupe futures hautement probables, alors qu'ici l'exposition décrite est celle d'un élément monétaire reconnu.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une cash flow hedge sur ce dividende déjà reconnu.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify

### 3. Couverture d'un investissement net à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait générateur décrit est une créance de dividende intragroupe comptabilisée, et non un investissement net dans une activité à l'étranger. IFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change attaché aux net assets d'une foreign operation; ce n'est pas la nature du poste visé ici.

**Implications pratiques**: Il ne faut pas documenter cette exposition comme une net investment hedge.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets