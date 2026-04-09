# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - La question vise les comptes consolidés IFRS et une créance de dividende intragroupe déjà comptabilisée.
   - La créance de dividende est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une entité du groupe, de sorte qu’un risque de change existe.
   - Le dividende intragroupe ne constitue pas ici une couverture de l’investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une relation de couverture de juste valeur sur la créance intragroupe déjà reconnue, si le risque de change sur cet élément monétaire n’est pas entièrement éliminé en consolidation. La couverture de flux de trésorerie n’est pas adaptée ici car l’exposition n’est plus une transaction future, et la couverture d’investissement net ne vise pas cette situation.

## Points Opérationnels

   - Le point clé est le moment : avant comptabilisation du dividende, on discute d’une transaction future ; après comptabilisation, on est sur une créance reconnue.
   - En consolidation, il faut démontrer que la créance de dividende est bien un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés.
   - La documentation doit être établie au niveau consolidé en visant explicitement le risque de change de la créance, pas le dividende comme distribution intra-groupe en tant que telle.
   - Si la créance et la dette de dividende sont intégralement éliminées sans résidu de change en consolidation, la base IFRS pour la couverture en consolidé disparaît.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Le risque de change sur cette créance génère des écarts de change non entièrement éliminés en consolidation.<br>- La documentation de couverture est mise en place au niveau consolidé sur ce risque de change. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Le risque de change sur cette créance génère des écarts de change non entièrement éliminés en consolidation.
   - La documentation de couverture est mise en place au niveau consolidé sur ce risque de change.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu, donc un type d’élément pouvant relever de la comptabilité de couverture. En comptes consolidés, seuls les éléments avec des tiers externes sont normalement éligibles, sauf exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés à la consolidation. Une créance de dividende intragroupe peut entrer dans cette exception si elle est monétaire et exposée à ce risque résiduel.

**Implications pratiques**: Vous pouvez documenter une couverture au niveau consolidé sur le change de la créance, uniquement si l’exception intragroupe sur le risque de change est remplie.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction future hautement probable. Or, dans votre cas, une créance à recevoir a déjà été comptabilisée au titre du dividende intragroupe : l’exposition n’est donc plus une transaction future mais un poste reconnu. La logique de couverture pertinente n’est pas celle des flux futurs sur dividende attendu.

**Implications pratiques**: Une fois la créance de dividende constatée, il ne faut pas documenter ce risque comme une couverture de flux de trésorerie.

**Référence**:
 - 6.3.1
    >The hedged item can be ... a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Votre question porte sur le change d’une créance de dividende intragroupe déjà comptabilisée, pas sur l’exposition de conversion liée à un investissement net dans une activité à l’étranger. La couverture d’investissement net traite le risque de change sur les net assets d’une activité étrangère, ce qui est d’une nature différente d’un dividende intragroupe à recevoir.

**Implications pratiques**: Ne documentez pas cette relation comme une couverture d’investissement net ; ce n’est pas l’objet du poste couvert décrit.

**Référence**:
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once