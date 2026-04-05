# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Est-il possible, au niveau consolidé, de qualifier de manière formelle une couverture du risque de change sur des dividendes intragroupe ayant fait l’objet d’une comptabilisation en créance à recevoir ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les états financiers consolidés appliquant la comptabilité de couverture d’IFRS 9.
   - Le dividende intragroupe a été déclaré et comptabilisé en créance/dette intragroupe, donc comme un élément monétaire reconnu.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, au consolidé, seulement si la créance de dividende intragroupe constitue un élément monétaire dont le risque de change génère des écarts de change non totalement éliminés en consolidation. Dans cette situation, la voie pertinente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point décisif est de démontrer que la créance/dette de dividende intragroupe crée, au consolidé, une exposition de change non totalement éliminée.
   - La désignation doit être faite formellement dès l’existence de la relation de couverture, avec documentation conforme à IFRS 9 6.4.1.
   - Si la créance est entre entités ayant la même monnaie fonctionnelle, l’exception intragroupe de 6.3.6 ne serait en pratique pas satisfaite.
   - La piste cash flow hedge reste pertinente seulement avant déclaration/comptabilisation, pour une transaction intragroupe future hautement probable, pas pour une créance déjà reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change sur cette créance entraîne des gains ou pertes de change non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change sur cette créance entraîne des gains ou pertes de change non totalement éliminés en consolidation.

**Raisonnment**:
Ici, le dividende a déjà été comptabilisé en créance intragroupe : il s’agit donc d’un actif reconnu. En consolidation, IFRS 9 n’admet un élément intragroupe comme élément couvert que, par exception, pour le risque de change d’un élément monétaire intragroupe générant des écarts non totalement éliminés ; dans ce cas, une désignation formelle est possible.

**Implications pratiques**: Si ces conditions sont remplies, la documentation de couverture peut viser le risque de change de la créance reconnue au niveau consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite ne porte pas sur une transaction future hautement probable mais sur un dividende déjà déclaré et comptabilisé en créance. L’exception IFRS 9 concernant les transactions intragroupe en consolidation vise des transactions prévisionnelles hautement probables ; elle ne correspond pas à une créance déjà reconnue.

**Implications pratiques**: La qualification en cash flow hedge ne correspond pas au fait générateur déjà comptabilisé.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >forecast sales or purchases of inventories between members of the same group

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici est celui d’une créance de dividende intragroupe, non celui d’un investissement net dans une activité étrangère. IFRIC 16 réserve ce modèle à la couverture du risque de change sur les net assets d’une opération étrangère inclus dans les états financiers ; ce n’est pas le cas d’un dividende à recevoir.

**Implications pratiques**: Ce modèle ne doit pas être utilisé pour couvrir une créance de dividende intragroupe.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 2
    >the item being hedged ... may be an amount of net assets