# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I have a question in relation to the accounting for a profit participating loan liability. For instance, a limited recourse loan where principal is payable on maturity but the interest on such loan is linked to profits i.e. based on a priority of payments if there is any residual profits that is the interest expense on the loan for the period.

Now, per my understanding I believe this amounts to the case for an embedded derivative i.e. the host contract being principal payments and interest being paid only if there is residual profit left per the waterfall priority of payments. Thus, the loan liability should be held at fair value through profit or loss.

I have come across many opinions for it to be accounted on an amortised cost basis at EIR, however, given the payments of interest are variable and based on if there is residual profit left, would it be accounted for at FVTPL or amortised cost.

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - On suppose que l’instrument est analysé du point de vue de l’émetteur comme un passif financier relevant d’IFRS 9.
   - On suppose que la question porte sur l’évaluation ultérieure du passif et de la clause de rémunération liée aux profits, et non sur la comptabilité de couverture, la décomptabilisation ou les transferts d’actifs.
   - On suppose que la rémunération variable dépend des profits résiduels de l’emprunteur/émetteur selon la cascade contractuelle décrite.

## Recommandation

**OUI**

Dans cette situation, le traitement le plus étayé est le coût amorti. IFRS 9 mesure par défaut les passifs financiers au coût amorti, et le lien aux profits de l’émetteur ne démontre pas ici un dérivé incorporé séparé ni une mesure obligatoire à la juste valeur par résultat.

## Points Opérationnels

   - Documenter à l’origine que la clause de participation aux profits est indexée sur les profits de l’émetteur, donc sur une variable spécifique à une partie au contrat.
   - Déterminer le TIE initial sur la base des flux contractuels estimés, puis réviser les estimations de paiements futurs lorsque les attentes changent, avec ajustement immédiat en résultat.
   - Vérifier séparément s’il existe, à la date initiale, un motif formel de désignation à la juste valeur par résultat; à défaut, conserver le coût amorti.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI | - (non spécifiées) |
| 2. Juste valeur par résultat | NON | - (non spécifiées) |
| 3. Séparation du dérivé incorporé | NON | - (non spécifiées) |

### 1. Coût amorti
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, il s’agit d’un prêt-passif chez l’émetteur, et IFRS 9 pose le coût amorti comme règle générale pour les passifs financiers.
Le fait que l’intérêt soit variable et payable sur profits résiduels n’impose pas, à lui seul, la juste valeur par résultat; les réestimations de flux peuvent être reflétées via le TIE et l’ajustement du coût amorti en résultat.

**Implications pratiques**: Comptabiliser le passif au coût amorti et ajuster les estimations de flux contractuels via le TIE, avec impact en résultat.

**Référence**:
 - 4.2.1
    >An entity shall classify all financial liabilities as subsequently measured at amortised cost, except for:
 - 5.7.2
    >shall be recognised in profit or loss when the financial liability is derecognised and through the amortisation process.
 - B5.4.6
    >shall adjust the gross carrying amount of the financial asset or amortised cost of a financial liability

### 2. Juste valeur par résultat
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits donnés, rien n’indique une désignation initiale à la juste valeur par résultat pour éliminer un mismatch comptable ou parce que le passif serait géré sur une base de juste valeur.
Le seul fait que l’intérêt dépende des profits résiduels ne fait pas automatiquement basculer l’intégralité du prêt en juste valeur par résultat.

**Implications pratiques**: Ne pas mesurer l’intégralité du prêt à la juste valeur par résultat sur ce seul motif.

**Référence**:
 - 4.2.1
    >financial liabilities at fair value through profit or loss
 - 4.2.2
    >may, at initial recognition, irrevocably designate a financial liability as measured at fair value through profit or loss
 - B4.3.9
    >permits the entire hybrid contract to be designated as at fair value through profit or loss.

### 3. Séparation du dérivé incorporé
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La clause variable décrite est liée aux profits résiduels de l’emprunteur/émetteur, donc à une variable non financière spécifique à une partie au contrat.
Or IFRS 9 ne traite comme dérivé qu’une variable non financière qui n’est pas spécifique à une partie; sur ces faits, la bifurcation d’un dérivé incorporé n’est donc pas établie.

**Implications pratiques**: Ne pas séparer, sur les faits donnés, une composante dérivée incorporée du prêt.

**Référence**:
 - 4.3.1
    >provided in the case of a non-financial variable that the variable is not specific to a party to the contract.
 - 4.3.3
    >an embedded derivative shall be separated from the host and accounted for as a derivative under this Standard if, and only if:
