{
  "assumptions_fr": [
    "On suppose que le dividende intragroupe déclaré fait naître une créance/dette intragroupe libellée en devise.",
    "On suppose que la question vise l’application du hedge accounting selon IFRS 9 dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si le dividende déclaré a créé un élément monétaire intragroupe en devise dont les écarts de change ne sont pas entièrement éliminés en consolidation.\nDans ce cas, une relation de couverture peut être documentée sur ce solde reconnu; en revanche, la couverture d’un investissement net n’est pas la bonne qualification pour une créance de dividende."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, après déclaration du dividende, l’exposition porte sur une créance/dette intragroupe reconnue en devise.\nDans les comptes consolidés, IFRS 9 admet par exception le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés; cela cadre avec une couverture de juste valeur d’un actif/passif reconnu.",
      "conditions_fr": [
        "la créance/dette de dividende est libellée dans une devise pertinente pour le risque de change couvert",
        "les écarts de change sur cet élément monétaire intragroupe ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation doit viser le solde de dividende reconnu comme élément couvert et le risque de change correspondant en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Une fois la créance de dividende comptabilisée, le risque de change peut aussi être appréhendé comme une variabilité des flux en monnaie fonctionnelle jusqu’au règlement.\nCette voie n’est recevable en consolidation que si le solde reconnu est bien un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé; il ne s’agit plus d’un dividende simplement forecast.",
      "conditions_fr": [
        "la désignation porte sur la variabilité de flux du solde de dividende déjà reconnu, et non sur un dividende non encore déclaré",
        "les écarts de change sur cet élément monétaire intragroupe ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "La relation doit être documentée sur le risque de change affectant les flux de règlement du solde intragroupe reconnu.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of, a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net",
      "applicability": "non",
      "reasoning_fr": "La situation décrite concerne une créance/dette de dividende intragroupe enregistrée, pas un montant de net assets d’une activité étrangère.\nLe modèle IFRIC 16 vise exclusivement le risque de change attaché à un investissement net dans une activité étrangère; il ne vise pas la créance de dividende elle-même.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette exposition comme une couverture d’investissement net.",
      "references": [
        {
          "section": "2",
          "excerpt": "will apply only when the net assets of that foreign operation are included in the financial statements"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé en consolidation est de démontrer que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés, typiquement entre entités de monnaies fonctionnelles différentes.",
    "La documentation de couverture doit être en place à l’inception de la relation et identifier le solde intragroupe, le risque de change couvert et le mode d’évaluation de l’efficacité.",
    "Si le dividende n’est pas encore déclaré, l’analyse ne porte plus sur une créance enregistrée mais sur une transaction forecast, ce qui change la qualification.",
    "En pratique, la couverture d’un investissement net doit être écartée pour cette exposition spécifique de dividende intragroupe."
  ]
}
