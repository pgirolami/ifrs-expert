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
   - La question porte sur des comptes consolidés établis selon IFRS 9.
   - La créance de dividende intragroupe est libellée dans une devise étrangère et crée un risque de change.
   - La question vise la situation après comptabilisation de la créance à recevoir.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via une couverture de juste valeur sur la créance intragroupe déjà comptabilisée, si ce poste monétaire intragroupe génère des écarts de change non totalement éliminés en consolidation. La couverture de flux de trésorerie n’est pas adaptée à ce stade, et la couverture d’investissement net ne vise pas ce type d’exposition.

## Points Opérationnels

   - Le point clé est le niveau de reporting : en consolidation, les éléments intragroupe ne sont éligibles qu’à titre exceptionnel pour le seul risque de change non éliminé.
   - Le timing est déterminant : après comptabilisation de la créance, l’analyse se fait comme poste reconnu, pas comme transaction future hautement probable.
   - Il faut documenter précisément pourquoi le risque de change sur cette créance de dividende subsiste en consolidation malgré l’élimination intragroupe.
   - Si les écarts de change liés à la créance sont entièrement éliminés en consolidation, la désignation de couverture en comptes consolidés n’est pas possible.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe doit être un poste monétaire générant des écarts de change non totalement éliminés en consolidation<br>- La documentation de couverture doit être mise en place au niveau consolidé sur ce risque de change spécifique |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe doit être un poste monétaire générant des écarts de change non totalement éliminés en consolidation
   - La documentation de couverture doit être mise en place au niveau consolidé sur ce risque de change spécifique

**Raisonnment**:
Ici, la créance de dividende déjà comptabilisée est un poste reconnu, donc le modèle de couverture d’un élément reconnu est pertinent. En comptes consolidés, un poste intragroupe ne peut toutefois être couvert que si, en tant qu’élément monétaire intragroupe, il crée des écarts de change qui ne sont pas totalement éliminés à la consolidation.

**Implications pratiques**: En pratique, la documentation doit viser la créance de dividende reconnue et démontrer que son risque de change subsiste en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise notamment une transaction future hautement probable. Or, dans votre cas, le dividende a déjà donné lieu à la comptabilisation d’une créance à recevoir : l’exposition n’est plus une transaction future mais un poste reconnu. La question posée ne correspond donc pas à ce modèle à ce stade.

**Implications pratiques**: Cette voie n’est pas la bonne une fois la créance de dividende déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de couverture d’investissement net traite l’exposition de change sur un investissement net dans une activité étrangère. Ici, l’exposition visée porte sur une créance de dividende intragroupe déjà reconnue, et non sur les net assets de l’activité étrangère. Ce n’est donc pas le bon modèle pour votre situation.

**Implications pratiques**: Il ne faut pas assimiler le change sur un dividende intragroupe à une couverture d’investissement net.

**Référence**:
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once in the consolidated financial statements