# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Company A has received an unsecured, interest free loan from one of its shareholders. The loan has no fixed repayment period. How do I recognize its fair value by measuring the present value of all future cashflows from this instrument.

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - La question porte sur la comptabilisation initiale de l'instrument selon IFRS 9.
   - Le prêt est traité comme un instrument financier relevant du champ des extraits IFRS 9 fournis.

## Recommandation

**OUI SOUS CONDITIONS**

L'approche pertinente est l'évaluation initiale à la juste valeur par actualisation pour un prêt sans intérêt, mais seulement si les flux futurs et leur échéancier peuvent être établis malgré l'absence de terme fixe. Si cette juste valeur diffère du montant reçu et n'est pas étayée uniquement par des données observables, l'écart initial est différé et non comptabilisé immédiatement en résultat.

## Points Opérationnels

   - À la comptabilisation initiale, partir du montant reçu puis le comparer à la juste valeur éventuellement calculée.
   - Si l'actualisation est utilisée, l'absence de période de remboursement fixe est la contrainte centrale : il faut documenter les flux futurs attendus et leur échéancier.
   - Le taux d'actualisation doit être un taux de marché pour un instrument similaire, en tenant compte notamment de la devise, du terme, du type de taux et de facteurs comparables de crédit.
   - Si la juste valeur calculée diffère du montant reçu et que la valorisation n'utilise pas uniquement des données observables, l'écart initial doit être différé.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation initiale au prix de transaction | OUI SOUS CONDITIONS | - si le montant reçu correspond à la juste valeur du prêt |
| 2. Évaluation initiale à la juste valeur par actualisation | OUI SOUS CONDITIONS | - si les flux futurs et leur échéancier peuvent être déterminés<br>- si le taux d'actualisation reflète un instrument similaire |
| 3. Gain ou perte immédiat au jour 1 | NON | - (non spécifiées) |
| 4. Différence de jour 1 différée | OUI SOUS CONDITIONS | - si la juste valeur calculée diffère du prix de transaction<br>- si la valorisation n'est pas étayée uniquement par des données de marché observables |

### 1. Comptabilisation initiale au prix de transaction
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - si le montant reçu correspond à la juste valeur du prêt

**Raisonnment**:
IFRS 9 pose le prix de transaction comme point de départ normal à la comptabilisation initiale. Dans cette situation, il n'est applicable que si le montant reçu représente bien la juste valeur du prêt, ce qui n'est pas automatique pour un prêt non garanti et sans intérêt.

**Implications pratiques**: Utiliser d'abord le montant reçu comme référence initiale, puis vérifier s'il coïncide avec la juste valeur.

**Référence**:
 - B5.1.1
    >The fair value of a financial instrument at initial recognition is normally the transaction price
 - B5.1.1
    >if part of the consideration given or received is for something other than the financial instrument

### 2. Évaluation initiale à la juste valeur par actualisation
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - si les flux futurs et leur échéancier peuvent être déterminés
   - si le taux d'actualisation reflète un instrument similaire

**Raisonnment**:
Cette méthode est celle visée par l'extrait pour un instrument sans intérêt. Elle ne devient toutefois opérationnelle ici que si, malgré l'absence d'échéance fixe, les flux futurs et leur calendrier peuvent être estimés puis actualisés avec un taux de marché pour un instrument similaire.

**Implications pratiques**: Calculer la valeur actuelle des flux futurs attendus avec un taux de marché comparable.

**Référence**:
 - B5.1.1
    >the fair value of a long-term loan or receivable that carries no interest can be measured as the present value of all future cash receipts
 - B5.1.1
    >discounted using the prevailing market rate(s) of interest for a similar instrument

### 3. Gain ou perte immédiat au jour 1
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Un gain ou une perte de jour 1 n'est admis que si la juste valeur est étayée par un prix coté de niveau 1 ou par une technique n'utilisant que des données de marché observables. Pour ce prêt d'actionnaire non garanti, sans intérêt et sans terme fixe, les faits fournis n'indiquent pas une telle base observable.

**Implications pratiques**: Ne pas passer immédiatement l'écart initial en résultat sur la seule base des faits fournis.

**Référence**:
 - B5.1.2A
    >quoted price in an active market for an identical asset
 - B5.1.2A
    >uses only data from observable markets
 - B5.1.2A
    >recognise the difference between the fair value at initial recognition and the transaction price as a gain or loss

### 4. Différence de jour 1 différée
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - si la juste valeur calculée diffère du prix de transaction
   - si la valorisation n'est pas étayée uniquement par des données de marché observables

**Raisonnment**:
Si vous calculez une juste valeur par actualisation différente du montant reçu, et que cette juste valeur n'est pas étayée uniquement par des données observables, IFRS 9 impose de différer l'écart initial. Dans cette situation, c'est l'issue la plus cohérente si l'approche d'actualisation est retenue.

**Implications pratiques**: Constater l'instrument à la mesure requise puis différer l'écart initial au lieu de le reconnaître immédiatement en résultat.

**Référence**:
 - B5.1.2A
    >in all other cases, at the measurement required by paragraph 5.1.1, adjusted to defer the difference
 - B5.1.2A
    >recognise that deferred difference as a gain or loss only to the extent
