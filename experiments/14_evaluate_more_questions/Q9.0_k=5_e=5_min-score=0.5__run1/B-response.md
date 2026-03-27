# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>Company A has received an unsecured, interest free loan from one of its shareholders. The loan has no fixed repayment period. How do I recognize its fair value by measuring the present value of all future cashflows from this instrument.

**Documentation consultée**
   - `ifrs-9-financial-instruments 2025 required`
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`

## Hypothèses
   - La question porte sur la comptabilisation initiale du prêt d'actionnaire en tant qu'instrument financier.
   - La demande est limitée à la comptabilisation et à l'évaluation initiales, y compris l'écart éventuel entre le prix de transaction et la juste valeur.

## Recommandation

**OUI SOUS CONDITIONS**

IFRS 9 permet de comptabiliser initialement un prêt sans intérêt / hors marché à la juste valeur par actualisation des flux futurs au taux de marché d'un instrument similaire.
Ici, l'absence d'échéance fixe impose de documenter l'hypothèse de remboursement; si la juste valeur diffère du montant reçu et n'est pas étayée uniquement par des données observables, l'écart est différé.

## Points Opérationnels

   - À la comptabilisation initiale, déterminer les flux de remboursement retenus et les actualiser avec un taux de marché pour un instrument similaire.
   - Documenter explicitement l'hypothèse de période de remboursement, car le prêt n'a pas d'échéance fixe.
   - Comparer ensuite la juste valeur obtenue au montant reçu pour déterminer s'il faut différer un écart au jour 1.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation initiale au prix de transaction | NON | - (non spécifiées) |
| 2. Comptabilisation initiale à la juste valeur | OUI SOUS CONDITIONS | - déterminer un calendrier de remboursement ou des flux futurs utilisables pour l'actualisation<br>- utiliser un taux de marché pour un instrument similaire avec un risque de crédit similaire |
| 3. Gain ou perte immédiat(e) au jour 1 | NON | - (non spécifiées) |
| 4. Différé de l'écart au jour 1 | OUI SOUS CONDITIONS | - la juste valeur initiale déterminée diffère du montant reçu<br>- l'évaluation n'est pas fondée uniquement sur des données de marché observables |

### 1. Comptabilisation initiale au prix de transaction
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette méthode est la règle normale, mais elle n'est pas la mieux adaptée aux faits décrits.
Le prêt est sans intérêt et consenti par un actionnaire, ce qui suggère que le montant reçu peut ne pas refléter uniquement l'instrument financier; le contexte fourni renvoie alors à une mesure à la juste valeur.

**Implications pratiques**: Ne pas retenir automatiquement le nominal reçu comme valeur initiale du prêt.

**Référence**:
 - B5.1.1
    >The fair value of a financial instrument at initial recognition is normally the transaction price
 - B5.1.1
    >if part of the consideration given or received is for something other than the financial instrument

### 2. Comptabilisation initiale à la juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - déterminer un calendrier de remboursement ou des flux futurs utilisables pour l'actualisation
   - utiliser un taux de marché pour un instrument similaire avec un risque de crédit similaire

**Raisonnment**:
Cette approche correspond aux faits: IFRS 9 illustre qu'un prêt sans intérêt ou à taux hors marché est comptabilisé initialement à la juste valeur par actualisation des flux futurs.
Toutefois, ici il n'existe pas de période de remboursement fixe; il faut donc disposer d'une hypothèse documentée de calendrier de remboursement pour pouvoir calculer la valeur actuelle.

**Implications pratiques**: Constater initialement le prêt à la juste valeur calculée par actualisation, et non automatiquement au nominal.

**Référence**:
 - B5.1.1
    >the fair value of a long-term loan or receivable that carries no interest can be measured as the present value of all future cash receipts
 - B5.1.1
    >discounted using the prevailing market rate(s) of interest for a similar instrument
 - B5.1.2
    >the entity recognises the loan at its fair value

### 3. Gain ou perte immédiat(e) au jour 1
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce traitement n'est permis que si la juste valeur est prouvée par un prix coté de niveau 1 ou par une technique utilisant uniquement des données de marché observables.
Dans cette situation, l'absence d'échéance fixe rend probable l'utilisation d'hypothèses de remboursement; sur les faits fournis, la condition d'observabilité intégrale n'est donc pas établie.

**Implications pratiques**: Ne pas comptabiliser immédiatement en résultat l'écart entre montant reçu et juste valeur sur la seule base des faits donnés.

**Référence**:
 - B5.1.2A
    >uses only data from observable markets
 - B5.1.2A
    >recognise the difference between the fair value at initial recognition and the transaction price as a gain or loss

### 4. Différé de l'écart au jour 1
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la juste valeur initiale déterminée diffère du montant reçu
   - l'évaluation n'est pas fondée uniquement sur des données de marché observables

**Raisonnment**:
Si la juste valeur initiale obtenue par actualisation diffère du montant reçu, IFRS 9 impose de différer l'écart lorsque cette juste valeur n'est pas étayée par des données entièrement observables.
Dans ce dossier, cette issue est pertinente dès lors que l'évaluation du prêt sans échéance fixe repose sur des hypothèses de remboursement.

**Implications pratiques**: L'écart entre le montant reçu et la juste valeur n'est pas comptabilisé immédiatement en résultat; il est différé.

**Référence**:
 - B5.1.2A
    >in all other cases
 - B5.1.2A
    >adjusted to defer the difference between the fair value at initial recognition and the transaction price
