{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et comptabilisé comme une créance/dette monétaire intragroupe.",
    "La créance/dette est libellée dans une devise générant des écarts de change qui ne sont pas entièrement éliminés en consolidation, car les entités concernées ont des monnaies fonctionnelles différentes.",
    "L’analyse vise les états financiers consolidés IFRS, et non les états financiers séparés ou individuels."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change sur un élément monétaire intragroupe dont les écarts ne sont pas entièrement éliminés.\nDans les faits supposés, un dividende intragroupe comptabilisé à recevoir peut donc être documenté en couverture, sous réserve de la désignation formelle et des tests d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe est supposé être une créance/dette monétaire déjà comptabilisée.\nLa règle générale d’exclusion des éléments intragroupe en consolidation est levée par l’exception d’IFRS 9 pour le risque de change sur un élément monétaire intragroupe non entièrement éliminé.\nComme il s’agit d’un actif/passif comptabilisé, une couverture de juste valeur peut être documentée si la relation satisfait aussi aux exigences de documentation et d’efficacité.",
      "conditions_fr": [
        "Le dividende à recevoir/payable doit constituer un élément monétaire intragroupe déjà comptabilisé.",
        "Les écarts de change correspondants ne doivent pas être entièrement éliminés en consolidation.",
        "La désignation et la documentation formelles doivent être établies dès l’origine de la relation.",
        "La relation doit démontrer un lien économique, un risque de crédit non dominant et un hedge ratio conforme."
      ],
      "practical_implication_fr": "Le groupe peut documenter une relation de couverture en consolidation sur la créance/dette de dividende au titre du risque de change, si l’exception intragroupe et les critères de 6.4.1 sont respectés.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette même situation, l’exception de 6.3.6 rend aussi éligible l’élément monétaire intragroupe en consolidation pour son risque de change.\nLe texte de 6.5.2(b) admet un cash flow hedge sur un actif ou passif comptabilisé; ici, cela suppose que la relation soit documentée comme couvrant la variabilité des flux de règlement due au change.\nCette voie n’est recevable que si la documentation initiale et les tests d’efficacité d’IFRS 9 sont remplis.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux de règlement liée au risque de change sur la créance/dette comptabilisée.",
        "L’élément intragroupe doit rester couvert par l’exception applicable aux éléments monétaires intragroupe en consolidation.",
        "La désignation formelle, l’objectif de gestion du risque et la méthode d’évaluation de l’efficacité doivent être documentés à l’origine.",
        "La relation doit satisfaire au lien économique, au test de crédit et au hedge ratio requis."
      ],
      "practical_implication_fr": "Une documentation en cash flow hedge est envisageable en consolidation si le groupe formalise la couverture comme portant sur la variabilité de change des flux de règlement du dividende intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l’origine l’instrument de couverture, l’élément couvert, le risque de change visé et la méthode de test d’efficacité.",
    "Vérifier que la créance/dette de dividende est bien un élément monétaire intragroupe et que les écarts de change correspondants ne sont pas entièrement éliminés en consolidation.",
    "Choisir et formaliser un seul modèle de couverture cohérent avec l’objectif de gestion du risque retenu pour ce dividende intragroupe."
  ]
}
