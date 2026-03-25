{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un poste monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, IFRS 9 pose une règle générale d’exclusion des postes intragroupe, mais prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat. Dans ce cadre, la documentation de hedge accounting peut viser cette exposition, en fair value hedge ou en cash flow hedge."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "La créance de dividendes est déjà un actif reconnu dans les états financiers consolidés, ce qui correspond bien au point de départ d’un fair value hedge. Sous les hypothèses retenues, son risque de change sur poste monétaire intragroupe entre dans l’exception de 6.3.6, car les écarts ne sont pas totalement éliminés en consolidation et affectent le résultat. La voie est donc ouverte, sous réserve de documenter formellement la relation de couverture et de satisfaire aux critères d’efficacité à l’inception de la relation.",
      "conditions_fr": [
        "Documenter à l’inception la désignation de la créance, de l’instrument de couverture, du risque de change couvert et du hedge ratio.",
        "Démontrer une relation économique entre l’élément couvert et l’instrument de couverture, sans domination du risque de crédit."
      ],
      "practical_implication_fr": "Il faut formaliser une relation de couverture sur la créance existante et en suivre l’efficacité pendant sa durée.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui",
      "reasoning_fr": "Dans la situation décrite, la créance figure déjà en consolidation mais IFRS 9 permet aussi un cash flow hedge pour un actif reconnu exposé à une variabilité de flux liée à un risque particulier. Sous les hypothèses retenues, l’exception de 6.3.6 rend le poste monétaire intragroupe éligible en tant qu’élément couvert pour son risque de change. Cette désignation est donc possible si la documentation définit dès l’inception la variabilité de flux couverte et si les critères d’efficacité IFRS 9 sont respectés.",
      "conditions_fr": [
        "Documenter à l’inception que l’exposition couverte est la variabilité des flux de la créance attribuable au risque de change.",
        "Démontrer une relation économique, un hedge ratio cohérent et l’absence de domination du risque de crédit."
      ],
      "practical_implication_fr": "Il faut construire une documentation centrée sur la variabilité de change des flux de la créance et assurer un suivi d’efficacité cohérent.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de qualification décisif est de démontrer que les écarts de change sur cette créance intragroupe ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
    "La documentation doit être mise en place à l’inception de la relation de couverture, même si la créance elle-même est déjà comptabilisée.",
    "Le choix entre fair value hedge et cash flow hedge doit rester cohérent avec la manière dont l’exposition de change de la créance est précisément définie dans la documentation."
  ]
}
