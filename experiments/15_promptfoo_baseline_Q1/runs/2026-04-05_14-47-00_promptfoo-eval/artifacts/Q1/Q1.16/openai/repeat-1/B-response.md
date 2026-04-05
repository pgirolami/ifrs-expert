# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Au niveau consolidé, l’entité constate une créance liée à des dividendes intragroupe et supporte, de ce fait, une exposition au risque de change. Cette exposition peut-elle faire l’objet d’une documentation de couverture conforme aux IFRS ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La créance de dividendes intragroupe est libellée dans une devise créant un risque de change en comptes consolidés.
   - La créance est un poste monétaire intragroupe et les écarts de change correspondants ne sont pas totalement éliminés en consolidation.
   - La question porte sur l'éligibilité de cette exposition à la comptabilité de couverture au niveau consolidé selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, une exposition de change sur une créance de dividendes intragroupe peut être documentée en couverture uniquement si elle entre dans l'exception IFRS 9 visant les postes monétaires intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Dans cette situation, l'approche la plus cohérente est la couverture de juste valeur ; la couverture de flux de trésorerie et la couverture d'investissement net ne correspondent pas aux faits décrits.

## Points Opérationnels

   - La documentation doit être préparée au niveau consolidé, car l'analyse d'éligibilité dépend de l'effet résiduel en consolidation.
   - Le point clé de faisabilité est de démontrer que la créance de dividendes constitue bien un poste monétaire intragroupe générant un risque de change non totalement éliminé.
   - Si le dividende n'est qu'une transaction intragroupe future et non encore comptabilisée, l'analyse basculerait vers les règles spécifiques des transactions intragroupe hautement probables.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit constituer un poste monétaire intragroupe.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit constituer un poste monétaire intragroupe.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.

**Raisonnment**:
La créance de dividendes est, dans les faits décrits, un actif reconnu exposé au risque de change affectant le résultat. IFRS 9 interdit en principe les éléments intragroupe en couverture au consolidé, mais prévoit une exception pour le risque de change d'un poste monétaire intragroupe s'il génère des écarts non totalement éliminés en consolidation. Si cette condition est remplie, une documentation de couverture est possible.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé en ciblant le risque de change du poste monétaire intragroupe.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrivent une créance déjà comptabilisée au titre d'un dividende intragroupe, et non une transaction future hautement probable. L'exception IFRS 9 visant les transactions intragroupe en cash flow hedge concerne la transaction intragroupe prévue, pas une créance déjà née. Dans cette situation précise, ce modèle n'est donc pas le bon véhicule de documentation.

**Implications pratiques**: Ne pas retenir ce modèle pour une créance de dividendes intragroupe déjà reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe, pas le risque de change attaché à un investissement net dans une activité à l'étranger. IFRIC 16 réserve ce modèle au risque de change sur les net assets d'une activité étrangère inclus dans les états financiers. Les faits décrits ne portent pas sur ce type d'élément couvert.

**Implications pratiques**: Écarter ce modèle sauf si l'élément couvert est réellement l'investissement net dans l'activité étrangère.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets