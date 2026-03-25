{
  "assumptions_fr": [
    "Le dividende intragroupe à recevoir est un élément monétaire intragroupe reconnu et libellé en devise.",
    "La créance et la dette correspondante existent entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Toute relation de couverture envisagée satisfait aux exigences de désignation formelle, de documentation et d'efficacité d'IFRS 9.6.4.1."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans les hypothèses retenues, l'exception d'IFRS 9 pour le risque de change d'un élément monétaire intragroupe en consolidation permet de documenter une relation de couverture. La lecture la plus directe est la couverture de juste valeur, avec une possibilité de couverture de flux si la documentation vise la variabilité des flux de règlement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Le dividende intragroupe à recevoir est ici supposé être un actif monétaire reconnu en devise, dont les écarts de change affectent encore le résultat consolidé. IFRS 9 exclut en principe les éléments intragroupe en consolidation, mais l'exception de 6.3.6 permet précisément de couvrir le risque de change d'un tel élément monétaire. Comme l'élément est déjà reconnu, la couverture de juste valeur est la qualification la plus directe dans cette situation.",
      "conditions_fr": [
        "Le dividende à recevoir est un actif monétaire intragroupe reconnu et libellé en devise.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation est désignée et documentée conformément à IFRS 9.6.4.1."
      ],
      "practical_implication_fr": "C'est l'approche la plus naturelle pour un dividende intragroupe déjà comptabilisé à recevoir.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le même dividende à recevoir peut aussi être envisagé sous l'angle de la variabilité des flux futurs en monnaie fonctionnelle jusqu'à son encaissement. IFRS 9.6.5.2(b) admet un cash flow hedge sur un actif reconnu, mais ici cette qualification n'est pertinente que si la documentation vise bien les flux exposés au change et non seulement la réévaluation de la créance. Dans cette situation, l'exception intragroupe de 6.3.6 reste indispensable.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux de règlement en monnaie fonctionnelle attribuable au change.",
        "L'élément doit relever de l'exception d'IFRS 9.6.3.6 pour les éléments monétaires intragroupe.",
        "Les critères de désignation, de documentation et d'efficacité d'IFRS 9.6.4.1 doivent être respectés."
      ],
      "practical_implication_fr": "Cette voie est possible si l'exposition couverte est formulée comme une variabilité de flux liée au change jusqu'au règlement du dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability ... and could affect profit or loss"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, le point décisif est l'exception d'IFRS 9.6.3.6 ; sans écarts de change non totalement éliminés, l'élément intragroupe ne peut pas être désigné.",
    "La documentation doit être en place dès l'origine de la relation et identifier l'instrument de couverture, l'élément couvert, le risque de change et la manière d'apprécier l'efficacité.",
    "Pour un dividende déjà comptabilisé à recevoir, la couverture de juste valeur est la qualification la plus directe ; la couverture de flux exige une formulation explicite de l'exposition en termes de flux futurs."
  ]
}
