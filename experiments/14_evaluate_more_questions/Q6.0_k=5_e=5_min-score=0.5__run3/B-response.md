# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I have a question in relation to the accounting for a profit participating loan liability. For instance, a limited recourse loan where principal is payable on maturity but the interest on such loan is linked to profits i.e. based on a priority of payments if there is any residual profits that is the interest expense on the loan for the period.

Now, per my understanding I believe this amounts to the case for an embedded derivative i.e. the host contract being principal payments and interest being paid only if there is residual profit left per the waterfall priority of payments. Thus, the loan liability should be held at fair value through profit or loss.

I have come across many opinions for it to be accounted on an amortised cost basis at EIR, however, given the payments of interest are variable and based on if there is residual profit left, would it be accounted for at FVTPL or amortised cost.

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - On suppose que l'instrument est un passif financier entrant dans le champ d'application d'IFRS 9.
   - On suppose que la question porte sur la comptabilisation ultérieure d'un instrument hybride de type dette susceptible de contenir un dérivé incorporé.

## Recommandation

**OUI SOUS CONDITIONS**

Au vu des faits fournis, la dette n'est pas automatiquement comptabilisée à la juste valeur par résultat du seul fait que l'intérêt dépend des profits. Le point de départ est le coût amorti, puis il faut tester si la clause de participation aux profits doit être séparée comme dérivé incorporé; à défaut, la dette reste au coût amorti.

## Points Opérationnels

   - Vérifier la documentation initiale: une désignation à la juste valeur par résultat n'est possible qu'à la comptabilisation initiale.
   - Tester formellement la clause de participation aux profits à la date d'origine selon le paragraphe 4.3.3 avant de conclure sur la base de mesure.
   - Si la dette reste au coût amorti, estimer les flux contractuels attendus puis comptabiliser les révisions d'estimation via l'ajustement du coût amorti et le résultat.
   - Le caractère limited recourse et la subordination dans la waterfall influencent surtout l'estimation des flux et le profil de risque; ils ne suffisent pas, dans les extraits fournis, à imposer la juste valeur par résultat.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - aucune désignation irrévocable à la juste valeur par résultat n'a été faite à l'origine<br>- la clause indexée sur les profits n'est pas comptabilisée séparément comme dérivé incorporé |
| 2. Juste valeur par résultat | NON | - (non spécifiées) |
| 3. Séparation du dérivé incorporé | OUI SOUS CONDITIONS | - la clause de participation aux profits n'est pas étroitement liée au contrat de dette hôte<br>- un instrument séparé avec les mêmes termes répondrait à la définition d'un dérivé |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - aucune désignation irrévocable à la juste valeur par résultat n'a été faite à l'origine
   - la clause indexée sur les profits n'est pas comptabilisée séparément comme dérivé incorporé

**Raisonnment**:
Dans votre situation, IFRS 9 pose le coût amorti comme règle générale pour les passifs financiers. Le fait que l'intérêt soit variable et payable seulement s'il existe des profits résiduels ne suffit pas, à lui seul, à faire passer l'emprunt entier en juste valeur par résultat. Si la clause participative n'est pas séparée et si aucune désignation initiale à la juste valeur n'a été faite, l'EIR reste la base, avec ajustement des estimations de flux si elles évoluent.

**Implications pratiques**: Appliquer un taux d'intérêt effectif et ajuster le coût amorti si les flux contractuels estimés sont révisés.

**Référence**:
 - 4.2.1
    >An entity shall classify all financial liabilities as subsequently measured at amortised cost, except for:
 - 5.7.2
    >A gain or loss on a financial liability that is measured at amortised cost ... shall be recognised in profit or loss ... through the amortisation process.
 - B5.4.6
    >adjust the ... amortised cost of a financial liability ... to reflect actual and revised estimated contractual cash flows.

### 2. Juste valeur par résultat
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans les faits décrits, rien n'indique que la dette a été désignée à la juste valeur par résultat lors de la comptabilisation initiale. IFRS 9 traite cette base comme une exception à la règle du coût amorti, et la simple présence alléguée d'un dérivé incorporé n'impose pas la juste valeur par résultat de l'instrument entier. Il faut d'abord examiner le modèle de séparation des dérivés incorporés.

**Implications pratiques**: Ne pas réévaluer la dette entière à la juste valeur sur la seule base de la clause de participation aux profits.

**Référence**:
 - 4.2.1
    >financial liabilities at fair value through profit or loss
 - 4.2.2
    >An entity may, at initial recognition, irrevocably designate a financial liability as measured at fair value through profit or loss
 - B4.3.9
    >this Standard permits the entire hybrid contract to be designated as at fair value through profit or loss.

### 3. Séparation du dérivé incorporé
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la clause de participation aux profits n'est pas étroitement liée au contrat de dette hôte
   - un instrument séparé avec les mêmes termes répondrait à la définition d'un dérivé

**Raisonnment**:
Votre description peut faire envisager un instrument hybride: un prêt hôte avec une rémunération additionnelle dépendant des profits résiduels. Toutefois, IFRS 9 ne permet la séparation que si les critères du paragraphe 4.3.3 sont remplis; ce n'est donc pas automatique dans ce cas. Le point décisif est notamment de savoir si la clause de profit participation, prise isolément, répondrait à la définition d'un dérivé et n'est pas étroitement liée au prêt hôte.

**Implications pratiques**: Si la séparation est requise, la clause est comptabilisée comme dérivé et le contrat hôte suit ensuite sa base propre.

**Référence**:
 - 4.3.3
    >an embedded derivative shall be separated from the host and accounted for as a derivative
 - 4.3.3
    >if, and only if:
 - 4.3.1
    >other variable, provided in the case of a non-financial variable that the variable is not specific to a party to the contract.
