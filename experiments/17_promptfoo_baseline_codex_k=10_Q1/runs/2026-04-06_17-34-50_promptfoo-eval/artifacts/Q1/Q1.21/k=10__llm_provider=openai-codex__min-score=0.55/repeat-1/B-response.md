# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Le groupe a comptabilisé un receivable au titre de dividendes intragroupe, créant ainsi une exposition au risque de change dans les comptes consolidés. Cette exposition peut-elle être désignée comme élément couvert au sens des IFRS ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée au niveau des comptes consolidés du groupe, dans le cadre de la comptabilité de couverture d'IFRS 9.
   - Le receivable de dividendes est une créance intragroupe libellée en devise, née d'une distribution entre entités du groupe.
   - Aucun fait n'indique que cette créance de dividendes intragroupe affecterait le résultat consolidé autrement que par un écart de change lié à une position intragroupe éliminée en consolidation.

## Recommandation

**NON**

Dans cette situation, la créance de dividendes intragroupe n'est pas un élément couvert éligible en consolidation. IFRS 9 limite les éléments couverts aux positions avec des tiers externes, sauf exceptions ciblées qui ne visent pas, sur les faits donnés, un dividende intragroupe.

## Points Opérationnels

   - En consolidation, partir de la règle de base IFRS 9: seuls les éléments avec des tiers externes sont éligibles, sauf exceptions expressément prévues.
   - Pour un poste intragroupe en devise, vérifier spécifiquement si l'écart de change affecte réellement le résultat consolidé et n'est pas totalement éliminé à la consolidation.
   - Un dividende intragroupe doit être distingué d'un investissement net dans une activité étrangère: ce ne sont pas les mêmes éléments couverts.
   - Si une couverture existe dans les comptes individuels ou séparés d'une entité du groupe, cela ne signifie pas automatiquement qu'elle est éligible dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | NON | - (non spécifiées) |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
En consolidation, IFRS 9 n'autorise comme éléments couverts que des actifs, passifs, engagements fermes ou transactions prévues avec une partie externe. L'exception vise certains postes monétaires intragroupe dont les écarts de change ne sont pas totalement éliminés, mais les faits décrivent ici une créance de dividendes intragroupe, non une exposition externe affectant le résultat consolidé.

**Implications pratiques**: Le groupe ne devrait pas désigner cette créance de dividendes intragroupe comme élément couvert dans une couverture de juste valeur en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify ... if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
IFRS 9 admet exceptionnellement certaines transactions intragroupe prévues hautement probables si le risque de change affecte le résultat consolidé. Le contexte cite surtout des flux comme ventes/achats intragroupe avec effet ultérieur en résultat; un dividende intragroupe est une distribution interne et, sur les faits donnés, ne remplit pas ce critère d'effet sur le résultat consolidé.

**Implications pratiques**: Le groupe ne devrait pas traiter le dividende intragroupe comme élément couvert d'une couverture de flux de trésorerie en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify ... provided that ... the foreign currency risk will affect consolidated profit or loss
 - B6.3.5
    >If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item.
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net vise le risque de change sur un investissement net dans une activité étrangère, c'est-à-dire un montant de net assets de l'opération étrangère. Une créance de dividendes intragroupe comptabilisée n'est pas, en elle-même, un montant de net assets désigné comme investissement net au sens de ce modèle.

**Implications pratiques**: Cette exposition de dividende intragroupe ne relève pas du modèle de couverture d'investissement net.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16.2
    >The item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.
 - ifric-16.10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation