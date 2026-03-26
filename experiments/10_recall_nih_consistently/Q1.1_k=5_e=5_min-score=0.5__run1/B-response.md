{
  "assumptions_fr": [
    "La créance de dividende intragroupe génère une exposition de change dans les états financiers consolidés.",
    "Les entités du groupe concernées ont des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Sous ces hypothèses, la partie change de la créance de dividende intragroupe peut être documentée en couverture dans les comptes consolidés via une couverture de juste valeur ou une couverture de flux de trésorerie. En revanche, la couverture d’investissement net ne correspond pas ici à une créance de dividende mais à des net assets d’une activité étrangère."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé en créance, donc il s'agit d'un actif reconnu. Sous les hypothèses données, le risque de change sur cet élément monétaire intragroupe subsiste en consolidation; il peut donc être désigné comme élément couvert, et le modèle de couverture de juste valeur vise précisément un actif reconnu exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [],
      "practical_implication_fr": "Modèle cohérent avec une créance déjà reconnue dont la composante change affecte le résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "La créance de dividende donnera lieu à un encaissement futur, et la question posée vise précisément la partie change de cet encaissement. Sous les hypothèses données, IFRS 9 permet aussi de documenter une couverture de la variabilité des flux de trésorerie liée à un risque particulier associé à un actif reconnu, y compris dans le contexte d'un élément monétaire intragroupe dont le change reste exposé en consolidation.",
      "conditions_fr": [],
      "practical_implication_fr": "Modèle possible si la documentation vise la variabilité en monnaie fonctionnelle de l'encaissement futur de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, l'élément visé est une créance de dividende intragroupe déjà comptabilisée, et non un montant de net assets d'une activité étrangère. Or la couverture d'investissement net est réservée au risque de change attaché à l'investissement net dans une opération étrangère; elle ne vise pas, sur ces faits, une créance de dividende à recevoir.",
      "conditions_fr": [],
      "practical_implication_fr": "À écarter pour cette créance; ce modèle vise les net assets d'une opération étrangère.",
      "references": [
        {
          "section": "2",
          "excerpt": "The item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l'inception l'instrument de couverture, la créance couverte, le risque de change couvert et la manière d'évaluer l'efficacité.",
    "En consolidation, l'analyse doit porter sur l'exposition de change qui subsiste après éliminations intragroupe; c'est ce point qui rend l'élément intragroupe éligible sur la partie change.",
    "Si l'objectif porte sur la créance de dividende déjà comptabilisée, la couverture d'investissement net n'est pas le bon véhicule documentaire."
  ]
}
