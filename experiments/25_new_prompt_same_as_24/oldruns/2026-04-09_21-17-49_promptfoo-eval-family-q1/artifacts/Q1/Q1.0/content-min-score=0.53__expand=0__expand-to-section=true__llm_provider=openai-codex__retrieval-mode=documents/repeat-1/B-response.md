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
   - La question vise les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe a déjà été déclaré et une créance à recevoir a été comptabilisée chez une entité du groupe.
   - Le risque visé est uniquement le risque de change sur cette créance intragroupe libellée dans une devise différente de la monnaie fonctionnelle de l'une des entités concernées.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie pertinente est la couverture de juste valeur sur la créance intragroupe reconnue, mais seulement si le risque de change génère des écarts non totalement éliminés en consolidation. La couverture de flux de trésorerie n'est pas adaptée à une créance déjà reconnue, et la couverture d'investissement net ne vise pas un dividende intragroupe à recevoir.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que la créance de dividende est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés.
   - Si la créance a déjà été reconnue, la logique IFRS est celle d'un actif reconnu, pas celle d'une transaction future hautement probable.
   - La documentation doit être mise en place comme relation de couverture IFRS 9 sur le risque de change identifié de la créance reconnue.
   - La conclusion porte sur les comptes consolidés ; IFRS 9 rappelle que les transactions intragroupe sont en principe exclues en consolidation sauf exception de change sur élément monétaire intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe est un élément monétaire exposé au risque de change.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.<br>- La relation de couverture est documentée et satisfait aux exigences de désignation et d'efficacité d'IFRS 9. |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise notamment des transactions futures hautement probables. Or, dans votre cas, le dividende a déjà donné lieu à la comptabilisation d'une créance à recevoir ; on n'est plus sur un flux futur non reconnu mais sur un actif déjà comptabilisé. En consolidation, l'enjeu décrit concerne donc la créance monétaire reconnue, pas une transaction future intragroupe.

**Implications pratiques**: Cette documentation n'est pas la bonne base si le dividende intragroupe est déjà comptabilisé en créance.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe est un élément monétaire exposé au risque de change.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.
   - La relation de couverture est documentée et satisfait aux exigences de désignation et d'efficacité d'IFRS 9.

**Raisonnment**:
Ici, il existe une créance à recevoir déjà reconnue, donc un actif monétaire intragroupe. IFRS 9 permet, en consolidation, qu'un élément monétaire intragroupe soit désigné comme élément couvert pour le seul risque de change si ce risque produit des écarts de change non intégralement éliminés en consolidation. C'est donc l'approche potentiellement applicable dans votre cas.

**Implications pratiques**: La documentation peut être mise en place sur le risque de change de la créance reconnue, sous réserve du test spécifique d'éligibilité en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise l'exposition de change sur un investissement net dans une activité à l'étranger, non le risque de change sur un dividende intragroupe déclaré et devenu créance. Le fait générateur que vous décrivez est une créance de dividende à encaisser, distincte d'une désignation d'investissement net. Elle n'entre donc pas, sur ces faits, dans cette catégorie.

**Implications pratiques**: La couverture d'investissement net ne doit pas être utilisée pour documenter le change sur cette créance de dividende intragroupe.

**Référence**:
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once