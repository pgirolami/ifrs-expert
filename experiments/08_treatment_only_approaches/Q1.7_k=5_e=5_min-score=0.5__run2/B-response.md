{
  "assumptions_fr": [
    "Le dividende intragroupe est libellé dans une devise créant une exposition de change au sein du groupe, car les entités concernées ont des monnaies fonctionnelles différentes.",
    "La question porte sur la comptabilité de couverture en comptes consolidés IFRS 9, pour un solde monétaire intragroupe lié à un dividende et restant en cours."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, le risque de change d’un poste monétaire intragroupe peut être un risque couvert si les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. La documentation formelle à l’inception et les critères d’efficacité IFRS 9 sont indispensables."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà reconnue correspond à un actif reconnu. IFRS 9 admet, en consolidation, qu’un poste monétaire intragroupe soit un élément couvert pour le risque de change si les écarts de change ne sont pas totalement éliminés. La couverture de juste valeur est donc recevable si ce risque de change peut affecter le résultat consolidé et si la relation est documentée dès l’origine.",
      "conditions_fr": [
        "La créance de dividende constitue un poste monétaire intragroupe en devise entre entités à monnaies fonctionnelles différentes.",
        "Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture est formellement désignée et documentée à l’inception, avec démonstration de l’efficacité et d’un hedge ratio conforme."
      ],
      "practical_implication_fr": "Documenter la relation comme couverture du risque de change d’un actif reconnu et suivre l’inefficacité selon IFRS 9.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item ... if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2(a)",
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 permet aussi une couverture de flux de trésorerie sur un actif reconnu lorsque la variabilité des flux est attribuable à un risque particulier et peut affecter le résultat. Dans cette situation, cela n’est recevable que si la créance de dividende en devise est documentée comme générant une variabilité des encaissements au règlement, tout en remplissant l’exception applicable aux postes monétaires intragroupe en consolidation.",
      "conditions_fr": [
        "L’exposition désignée porte sur la variabilité des flux de trésorerie de la créance en devise jusqu’à son règlement.",
        "Le risque de change sur le poste monétaire intragroupe affecte le résultat consolidé car les écarts ne sont pas totalement éliminés en consolidation.",
        "La désignation, la documentation et l’évaluation de l’efficacité respectent IFRS 9 dès l’inception."
      ],
      "practical_implication_fr": "Il faut démontrer que le risque couvert est bien la variabilité des encaissements en devise sur la créance reconnue.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé n’est pas le caractère intragroupe du dividende, mais le fait qu’il existe un poste monétaire en devise dont les écarts de change ne sont pas totalement éliminés en consolidation.",
    "La documentation doit être en place à l’inception de la relation de couverture, avec identification du risque couvert, de l’instrument de couverture et du mode d’évaluation de l’efficacité.",
    "En pratique, la couverture de juste valeur est la lecture la plus directe pour une créance déjà reconnue; la couverture de flux de trésorerie exige une désignation très claire de la variabilité des encaissements au règlement.",
    "Si l’exposition de change n’affecte pas le résultat consolidé, la couverture comptable n’est pas recevable dans cette situation."
  ]
}
