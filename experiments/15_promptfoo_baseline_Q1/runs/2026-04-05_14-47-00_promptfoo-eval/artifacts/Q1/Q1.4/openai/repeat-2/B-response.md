# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les états financiers consolidés soumis à IFRS 9.
   - La créance de dividende intragroupe reconnue est un élément monétaire intragroupe.
   - La créance est libellée dans une devise telle que des écarts de change ne sont pas entièrement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende reconnue constitue un élément monétaire intragroupe générant des écarts de change non entièrement éliminés en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point de départ pertinent est la date de reconnaissance de la créance de dividende, car l’analyse porte alors sur un élément monétaire reconnu.
   - En consolidation, il faut vérifier explicitement que les écarts de change sur la créance intragroupe ne sont pas entièrement éliminés du fait de devises fonctionnelles différentes.
   - La documentation de couverture doit identifier le risque couvert comme le seul risque de change affectant le résultat consolidé.
   - Si la situation visée est encore au stade du dividende futur non reconnu, le raisonnement ci-dessus ne s’applique pas de la même manière.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un élément monétaire intragroupe.<br>- Le risque de change doit entraîner des gains ou pertes non entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un élément monétaire intragroupe.
   - Le risque de change doit entraîner des gains ou pertes non entièrement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende déjà reconnue est un actif reconnu. IFRS 9 permet de désigner le risque de change d’un élément monétaire intragroupe en consolidation s’il crée des gains ou pertes de change non entièrement éliminés ; ce risque peut alors être couvert comme risque affectant le résultat.

**Implications pratiques**: La documentation doit viser la créance reconnue et le seul risque de change qui affecte le résultat consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le fait générateur évoqué est la reconnaissance d’une créance de dividende intragroupe, donc un poste déjà comptabilisé et non une transaction intragroupe future hautement probable. En consolidation, IFRS 9 n’admet les transactions intragroupe futures qu’à titre d’exception lorsque le risque de change affecte le résultat consolidé ; le contexte fourni ne soutient pas ce traitement pour un dividende déjà constaté.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une couverture de flux de trésorerie une fois la créance reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >the intragroup transaction cannot qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur la composante change d’une créance de dividende intragroupe reconnue, non sur le risque de change d’un investissement net dans une activité à l’étranger. Les textes IFRIC 16 visent la couverture d’un montant de net assets d’une foreign operation ; cela ne correspond pas à une créance de dividende intercompagnie.

**Implications pratiques**: Il ne faut pas documenter cette relation comme une couverture d’investissement net.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 13
    >A derivative or a non-derivative instrument ... may be designated as a hedging instrument in a hedge of a net investment