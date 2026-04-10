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
   - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée dans les comptes individuels de l'entité bénéficiaire.
   - La créance et la dette de dividende sont libellées dans une devise étrangère pour au moins une entité du groupe.
   - La question vise les comptes consolidés IFRS du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais uniquement via une relation de couverture de type fair value hedge sur le risque de change de la créance intragroupe, si cette créance constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. En revanche, le cash flow hedge et le net investment hedge ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point déterminant est le niveau de reporting : l'exception vise les comptes consolidés, pas simplement les comptes individuels.
   - Il faut démontrer que la créance de dividende est bien un élément monétaire intragroupe et que ses écarts de change affectent encore le résultat consolidé.
   - Si le dividende n'avait pas encore été comptabilisé et restait à l'état de flux futur hautement probable, l'analyse aurait relevé du cash flow hedge ; ce n'est pas le cas ici.
   - La documentation doit identifier précisément le risque couvert comme étant la seule composante change de la créance de dividende.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Le risque de change sur cette créance doit donner lieu à des écarts de change non totalement éliminés en consolidation.<br>- La documentation de couverture doit être établie au niveau des comptes consolidés. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Le risque de change sur cette créance doit donner lieu à des écarts de change non totalement éliminés en consolidation.
   - La documentation de couverture doit être établie au niveau des comptes consolidés.

**Raisonnment**:
Dans votre cas, il existe une créance de dividende déjà comptabilisée : on n'est donc plus sur une transaction future mais sur un poste reconnu. IFRS 9 permet, en consolidation, de désigner le risque de change d'un élément monétaire intragroupe comme élément couvert si ce risque génère des écarts de change non totalement éliminés en consolidation.

**Implications pratiques**: Possible en consolidation pour le seul risque de change de la créance reconnue, si l'exception IFRS 9 sur les éléments monétaires intragroupe est remplie.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise des transactions futures hautement probables. Or, d'après les faits donnés, le dividende a déjà donné lieu à la comptabilisation d'une créance à recevoir ; le sujet n'est donc plus un flux futur non reconnu mais un poste existant.

**Implications pratiques**: Non adapté ici, car le dividende n'est plus une transaction future hautement probable mais une créance déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net concerne l'exposition de change liée à une participation nette dans une activité à l'étranger. Une créance de dividende intragroupe comptabilisée ne constitue pas, en elle-même, l'investissement net dans l'activité étrangère visé par IFRS 9 et IFRIC 16.

**Implications pratiques**: À écarter pour la créance de dividende elle-même ; ce modèle vise un autre risque couvert.

**Référence**:
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting