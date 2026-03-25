{
  "assumptions_fr": [
    "L’exposition de change constatée en consolidation suppose que la créance de dividendes intragroupe est un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes et que les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous l’hypothèse retenue, l’exposition entre dans l’exception d’IFRS 9 6.3.6 applicable aux éléments monétaires intragroupe en consolidation. La voie la plus directe est la couverture de juste valeur; une couverture de flux peut aussi être envisagée si la variabilité des flux futurs est correctement documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change sur la créance intragroupe",
      "applicability": "oui",
      "reasoning_fr": "La créance de dividendes est déjà comptabilisée : il s’agit donc d’un actif reconnu, ce qui correspond au champ d’une couverture de juste valeur d’un risque particulier. En retenant l’hypothèse d’un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation, l’exception d’IFRS 9 6.3.6 permet sa désignation comme élément couvert. Il ne reste que les conditions ordinaires de documentation et d’efficacité de 6.4.1.",
      "conditions_fr": [
        "Documenter formellement dès l’inception la relation de couverture, l’élément couvert et le risque de change désigné.",
        "Démontrer une relation économique, l’absence de domination du risque de crédit et un hedge ratio cohérent avec la gestion du risque."
      ],
      "practical_implication_fr": "Le groupe peut traiter le risque de change sur cette créance comme élément couvert en couverture de juste valeur, avec suivi de l’inefficacité en résultat.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "label_fr": "Couverture de flux de trésorerie du risque de change sur la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les faits donnés, la créance intragroupe est un actif reconnu dont l’encaissement futur peut varier en monnaie fonctionnelle en raison du change. Sous l’hypothèse que cet élément monétaire génère des écarts de change non totalement éliminés en consolidation, 6.3.6 permet la désignation comme élément couvert, et 6.5.2(b) ouvre aussi la voie d’une couverture de flux sur un actif reconnu. Cette voie n’est applicable que si le groupe documente bien que le risque couvert est la variabilité des flux futurs liée au change, en plus des critères de 6.4.1.",
      "conditions_fr": [
        "Documenter que l’exposition couverte est la variabilité des flux d’encaissement futurs en monnaie fonctionnelle due au change.",
        "Satisfaire aux exigences de désignation formelle, de relation économique et de hedge ratio prévues par IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "Le groupe peut envisager une couverture de flux, mais la documentation devra être plus précise sur les flux futurs effectivement couverts.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "L’analyse se fait au niveau des comptes consolidés : en principe les éléments intragroupe sont exclus, sauf l’exception de 6.3.6 pour certains éléments monétaires intragroupe en devise.",
    "Comme la créance est déjà comptabilisée, la couverture de juste valeur est la lecture la plus directe; la couverture de flux exige d’identifier précisément les flux futurs d’encaissement exposés au change.",
    "Dans les deux cas, la désignation et la documentation doivent être établies dès l’inception de la relation de couverture, avec suivi de l’efficacité et de l’inefficacité."
  ]
}
