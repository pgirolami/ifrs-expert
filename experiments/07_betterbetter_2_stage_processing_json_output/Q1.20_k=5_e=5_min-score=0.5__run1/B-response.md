{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un poste monétaire reconnu entre des entités du groupe ayant des monnaies fonctionnelles différentes, et les écarts de change qui en résultent ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, les éléments intragroupe sont en principe exclus comme éléments couverts, mais IFRS 9 prévoit une exception explicite pour le risque de change d’un poste monétaire intragroupe non totalement éliminé à la consolidation. Dans ce cadre, une documentation de fair value hedge ou de cash flow hedge peut être mise en place pour cette créance."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "En consolidation, la règle de 6.3.5 exclut en principe les éléments intragroupe, mais 6.3.6 ouvre explicitement une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés, ce qui correspond à l’hypothèse.\nComme la créance est déjà comptabilisée, elle peut être désignée comme actif reconnu dans une fair value hedge du risque de change, sous la documentation et les tests d’efficacité exigés par 6.4.1.",
      "conditions_fr": [
        "Désigner et documenter formellement la relation de couverture à son inception",
        "Identifier l’instrument de couverture, le risque de change couvert et démontrer une relation économique avec un hedge ratio cohérent"
      ],
      "practical_implication_fr": "Il faut documenter la couverture du risque de change du poste monétaire intragroupe et suivre l’efficacité de la relation pendant sa durée.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items"
        },
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
      "reasoning_fr": "Sur les mêmes faits et la même hypothèse d’un poste monétaire intragroupe dont le risque de change subsiste en consolidation, l’exception de 6.3.6 rend la créance éligible comme hedged item malgré son caractère intragroupe.\nIFRS 9 admet aussi une cash flow hedge d’un risque affectant les flux de trésorerie d’un actif reconnu ; ici, cela vise la variabilité en monnaie fonctionnelle des flux de règlement de la créance déjà reconnue, sous la documentation et les tests d’efficacité de 6.4.1.",
      "conditions_fr": [
        "Désigner et documenter formellement la relation de couverture à son inception",
        "Identifier l’instrument de couverture, la variabilité de change des flux couverts et démontrer une relation économique avec un hedge ratio cohérent"
      ],
      "practical_implication_fr": "Il faut documenter la variabilité de change des flux de règlement de la créance et aligner l’instrument de couverture sur cette exposition.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif est l’exception de 6.3.6 : elle permet la couverture en consolidation seulement parce qu’il s’agit, selon l’hypothèse, d’un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé.",
    "La documentation de hedge accounting doit être formalisée à l’inception de la relation de couverture, même si la créance elle-même est déjà reconnue dans les états financiers consolidés.",
    "Le dossier de couverture doit identifier l’instrument de couverture, l’élément couvert, le risque de change visé et la méthode d’évaluation de l’efficacité, conformément à 6.4.1.",
    "Le choix entre fair value hedge et cash flow hedge doit être cohérent avec le risque formellement désigné : variation de valeur du poste reconnu ou variabilité des flux de règlement en monnaie fonctionnelle."
  ]
}
