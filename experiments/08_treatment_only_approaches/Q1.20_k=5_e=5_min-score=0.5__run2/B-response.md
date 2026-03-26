{
  "assumptions_fr": [
    "La créance de dividendes et la dette correspondante sont des éléments monétaires intragroupe reconnus.",
    "La créance est exposée à un risque de change car elle est libellée dans une devise qui génère des écarts de change en consolidation.",
    "Les gains ou pertes de change correspondants ne sont pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "La relation de couverture satisferait par ailleurs aux exigences d’IFRS 9 en matière de désignation, de documentation et d’efficacité."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : IFRS 9 admet en consolidation le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés. Dans cette situation, la voie la plus directe est la couverture de juste valeur, sous réserve de la documentation et des tests d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En principe, IFRS 9 limite les éléments couverts aux expositions avec des tiers, mais une exception vise le risque de change d’un élément monétaire intragroupe dans les comptes consolidés si les écarts de change ne sont pas totalement éliminés. Ici, la créance de dividendes est déjà reconnue et l’exposition décrite est celle d’un actif monétaire existant ; le modèle de juste valeur est donc applicable dans cette situation, sous réserve de la documentation et de l’efficacité.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe dont le risque de change n’est pas entièrement éliminé en consolidation.",
        "Le risque couvert doit pouvoir affecter le résultat consolidé.",
        "La relation doit être formellement désignée et documentée dès l’origine.",
        "La relation doit satisfaire aux critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "La documentation peut viser le risque de change porté par la créance intragroupe reconnue dans les comptes consolidés.",
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
      "reasoning_fr": "IFRS 9 ouvre aussi la couverture de flux de trésorerie à un actif ou passif reconnu lorsque la variabilité des flux, attribuable à un risque particulier, peut affecter le résultat. Dans cette situation, cela reste possible seulement si la documentation vise bien la variabilité des encaissements en monnaie fonctionnelle causée par le change sur cette créance intragroupe reconnue, tout en respectant l’exception de consolidation pour les éléments monétaires intragroupe.",
      "conditions_fr": [
        "La documentation doit viser la variabilité des flux liée au risque de change sur la créance reconnue.",
        "Les effets de change doivent pouvoir affecter le résultat consolidé et ne pas être totalement éliminés.",
        "La relation doit être formellement désignée et documentée dès l’origine.",
        "La relation doit satisfaire aux critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la documentation doit décrire explicitement la variabilité de flux couverte et son lien avec le change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
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
    "Documenter dès l’inception que la créance est un élément monétaire intragroupe dont les écarts de change subsistent en consolidation et affectent le résultat consolidé.",
    "Choisir explicitement le modèle de couverture dans la documentation ; au vu des faits, la couverture de juste valeur est la plus directe.",
    "Identifier dans la documentation l’instrument de couverture, l’élément couvert, le risque de change, le hedge ratio et la méthode d’évaluation de l’efficacité."
  ]
}
