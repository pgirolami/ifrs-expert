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
   - La question vise les comptes consolidés IFRS.
   - Le dividende intragroupe a déjà été déclaré et une créance intragroupe a déjà été comptabilisée.
   - La créance de dividende est libellée dans une devise créant un risque de change entre entités du groupe.
   - L’analyse porte uniquement sur les trois modèles de comptabilité de couverture fournis.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, cela peut être documenté en couverture uniquement si la créance de dividende intragroupe constitue un poste monétaire exposé à un risque de change dont les écarts ne sont pas totalement éliminés en consolidation. Dans ce cas, l’approche pertinente parmi celles listées est la couverture de juste valeur ; les deux autres ne conviennent pas aux faits décrits.

## Points Opérationnels

   - Le point clé est le niveau de reporting : l’exception IFRS concerne les comptes consolidés, pas la règle générale applicable aux transactions intragroupe.
   - Le timing est déterminant : une créance de dividende déjà comptabilisée s’analyse différemment d’un dividende simplement anticipé.
   - La documentation doit être limitée à la composante change du poste intragroupe et non au dividende en tant que tel.
   - Si les écarts de change sont totalement éliminés en consolidation, il n’y a pas de base pour une relation de couverture en consolidé sur ce poste.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende intragroupe est un poste monétaire<br>- le risque couvert est uniquement le risque de change<br>- les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende intragroupe est un poste monétaire
   - le risque couvert est uniquement le risque de change
   - les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation

**Raisonnment**:
Ici, la question porte sur une créance de dividende déjà comptabilisée, donc sur un poste reconnu et non sur un flux futur seulement prévu. En consolidation, les éléments intragroupe ne sont en principe pas éligibles, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation de couverture n’est envisageable en consolidé que sur la composante change résiduelle du poste intragroupe reconnu.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les extraits fournis rattachent cette logique aux transactions prévues hautement probables. Or, dans votre cas, il ne s’agit plus d’un dividende futur attendu mais d’une créance déjà comptabilisée. Sur les faits décrits, l’enjeu est donc un poste reconnu exposé au change, pas un flux futur à désigner comme tel.

**Implications pratiques**: Ce modèle ne correspond pas à une créance de dividende intragroupe déjà reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise le risque de change lié à un investissement net dans une activité à l’étranger. Une créance de dividende intragroupe déjà comptabilisée est distincte du net investment et correspond au contraire à un poste intragroupe spécifique. Les textes fournis sur la couverture d’investissement net ne visent pas ce cas.

**Implications pratiques**: Il ne faut pas documenter ce dividende à recevoir comme une couverture d’investissement net.

**Référence**:
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity
 - 13
    >An exposure to foreign currency risk arising from a net investment in a foreign operation may qualify for hedge accounting only once