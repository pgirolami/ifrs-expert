# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Est-il recevable, au regard des IFRS, de documenter une couverture du risque de change sur des dividendes intragroupe ayant donné lieu à la reconnaissance d’une créance dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les comptes consolidés établis selon les IFRS.
   - Le dividende intragroupe a donné lieu à une créance monétaire intragroupe exposée à un risque de change.
   - La créance de dividende est encore pertinente en consolidation au titre du risque de change, c’est-à-dire qu’elle génère potentiellement des écarts de change non totalement éliminés en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

C’est recevable seulement si la créance de dividende constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, la voie pertinente est la couverture de juste valeur; les modèles de cash flow hedge et de net investment hedge ne correspondent pas à ce fait précis.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que la créance de dividende est un poste monétaire intragroupe générant des écarts de change non totalement éliminés.
   - La documentation doit être faite dès l’origine de la relation de couverture et inclure l’instrument de couverture, l’élément couvert, le risque de change couvert et le test d’efficacité.
   - Si la créance/dividende est intégralement éliminé en consolidation sans effet de change résiduel en résultat consolidé, la comptabilité de couverture n’est pas recevable pour ce poste.
   - En pratique, si les conditions IFRS 9 ne sont pas remplies, le dérivé restera à la juste valeur par résultat sans hedge accounting.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un poste monétaire intragroupe.<br>- Les écarts de change sur ce poste doivent ne pas être totalement éliminés en consolidation, notamment entre entités de devises fonctionnelles différentes.<br>- La relation de couverture doit être formellement désignée et documentée dès l’origine conformément à IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un poste monétaire intragroupe.
   - Les écarts de change sur ce poste doivent ne pas être totalement éliminés en consolidation, notamment entre entités de devises fonctionnelles différentes.
   - La relation de couverture doit être formellement désignée et documentée dès l’origine conformément à IFRS 9.

**Raisonnment**:
La créance de dividende reconnue est, dans les faits décrits, un actif reconnu. IFRS 9 permet une fair value hedge d’un actif reconnu pour un risque particulier affectant le résultat. En consolidation, un poste monétaire intragroupe peut être un élément couvert pour le risque de change si les écarts de change ne sont pas totalement éliminés.

**Implications pratiques**: Si ces conditions sont remplies, la documentation IFRS est envisageable en fair value hedge du risque de change de la créance.

**Référence**:
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, le fait exposé porte sur une créance de dividende déjà reconnue, donc sur un montant monétaire déterminé. Le modèle de cash flow hedge vise une variabilité de flux de trésorerie sur un élément reconnu ou une transaction future hautement probable; ce n’est pas la caractéristique centrale d’une créance de dividende déjà constatée.

**Implications pratiques**: La documentation de couverture ne devrait pas être structurée en cash flow hedge pour cette créance de dividende reconnue.

**Référence**:
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - B6.3.5
    >This is usually the case for royalty payments, interest payments or management charges between members of the same group

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque couvert dans la question est celui d’une créance de dividende intragroupe, non celui d’un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change sur les net assets d’une activité étrangère; il ne doit pas être transposé à d’autres situations.

**Implications pratiques**: La relation ne doit pas être documentée comme couverture d’investissement net pour un dividende intragroupe à recevoir.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation

### 4. Comptabilisation sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture recevable et documentée, le dérivé suit la règle générale IFRS 9: variations de juste valeur en résultat. La créance suit son traitement propre, avec comptabilisation en résultat des effets pertinents hors hedge accounting.

**Implications pratiques**: C’est le traitement de repli si les conditions de la fair value hedge sur poste monétaire intragroupe ne sont pas démontrées.

**Référence**:
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss unless
 - 5.7.2
    >A gain or loss on a financial liability that is measured at amortised cost ... shall be recognised in profit or loss
 - 251
    >an entity recognises all of its contractual rights and obligations under derivatives in its statement of financial position