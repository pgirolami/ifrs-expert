{
  "assumptions_fr": [
    "La créance/dividende intragroupe comptabilisée est un poste monétaire libellé dans une devise qui crée une exposition de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "La question porte uniquement sur la comptabilité de couverture, dans les comptes consolidés, du risque de change attaché à cette créance comptabilisée."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, si la créance de dividende est un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé et affecte le résultat consolidé. Dans cette situation, la couverture en juste valeur est la voie la plus directement alignée; une couverture de flux de trésorerie peut aussi être envisagée si la désignation vise la variabilité des flux de règlement en devise fonctionnelle."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, un élément intragroupe n’est en principe pas éligible, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsqu’il génère des écarts de change non totalement éliminés en consolidation. Ici, la créance de dividende est déjà comptabilisée comme actif reconnu, ce qui cadre directement avec une couverture de juste valeur du risque de change affectant le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende intragroupe est un poste monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.",
        "Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Documenter la créance de dividende comptabilisée comme élément couvert pour son risque de change dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception ... there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même exception permet, en consolidation, de retenir le risque de change d’un poste monétaire intragroupe comme élément couvert. Dans votre cas, si la désignation porte sur la variabilité des flux d’encaissement en monnaie fonctionnelle lors du règlement de la créance de dividende, et que cette variabilité affecte le résultat consolidé, une couverture de flux de trésorerie est défendable pour cette situation.",
      "conditions_fr": [
        "La créance de dividende intragroupe est un poste monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.",
        "La variabilité de change sur les flux de règlement de cette créance affecte le résultat consolidé parce qu’elle n’est pas totalement éliminée en consolidation."
      ],
      "practical_implication_fr": "Documenter la variabilité en monnaie fonctionnelle des flux de règlement de la créance comme risque couvert en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception ... there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé n’est pas la nature “dividende”, mais le fait qu’une créance intragroupe comptabilisée constitue un poste monétaire exposé au change en consolidation.",
    "Avant de documenter la couverture, vérifier que l’écart de change sur cette créance n’est pas totalement éliminé en consolidation et qu’il affecte bien le résultat consolidé.",
    "La relation de couverture doit être formellement désignée et documentée dès l’origine, avec l’identification de l’instrument de couverture, de la créance couverte, du risque de change et de la manière d’apprécier l’efficacité.",
    "En pratique, la couverture de juste valeur est généralement la plus directement alignée avec une créance déjà comptabilisée; la couverture de flux de trésorerie demande de bien cadrer que le risque couvert est la variabilité des flux de règlement."
  ]
}
