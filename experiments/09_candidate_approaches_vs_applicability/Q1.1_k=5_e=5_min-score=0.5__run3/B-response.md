{
  "assumptions_fr": [
    "La créance/dette de dividende intragroupe est un élément monétaire libellé dans une devise créant une exposition de change entre des entités du groupe.",
    "Les gains et pertes de change correspondants ne sont pas totalement éliminés en consolidation, de sorte que l’exception relative aux éléments monétaires intragroupe en comptes consolidés est pertinente.",
    "Si une couverture d’investissement net est envisagée, le dividende s’inscrit dans une structure parent / activité étrangère incluse dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement si l’exception IFRS 9 sur les éléments monétaires intragroupe en consolidation est effectivement remplie. Dans la situation décrite, la voie pertinente est la couverture de juste valeur du risque de change sur la créance; la couverture de flux de trésorerie et la couverture d’investissement net ne correspondent pas à la créance de dividende elle-même."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé en créance, donc l’exposition porte sur un actif monétaire reconnu. En consolidation, IFRS 9 admet exceptionnellement le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés. Dans ce cas précis, la couverture de juste valeur est le modèle le plus directement aligné avec la réévaluation de change de la créance.",
      "conditions_fr": [
        "La créance et la dette intragroupe sont des éléments monétaires entre entités ayant des monnaies fonctionnelles différentes.",
        "Les écarts de change sur cet intragroupe ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La variation de change de la créance couverte et celle de l’instrument de couverture seront suivies en résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans les faits donnés, le dividende est déjà constaté en créance pour un montant nominal fixé. L’exposition identifiée est donc la réévaluation de change d’un poste monétaire reconnu, et non une variabilité de flux futurs du dividende telle que posée par la question. Le modèle de cash flow hedge ne correspond donc pas à cette situation précise.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne devrait pas être retenu pour documenter le change de cette créance de dividende déjà comptabilisée.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "La question porte sur la partie change d’une créance de dividende intragroupe déjà enregistrée. Or la couverture d’investissement net vise le risque de change sur des net assets d’une activité étrangère, pas sur une créance intercompany isolée. Dans cette situation, l’exposition décrite relève d’un poste monétaire intragroupe, non d’un investissement net.",
      "conditions_fr": [],
      "practical_implication_fr": "Le schéma OCI/FCTR d’une couverture d’investissement net ne convient pas pour couvrir la créance de dividende elle-même.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ en consolidation est IFRS 9 6.3.6 : sans exposition de change non totalement éliminée, la créance intragroupe ne peut pas être désignée comme élément couvert.",
    "Comme le dividende est déjà comptabilisé en créance, la documentation doit viser la créance monétaire existante et sa composante de change, et non un flux futur de dividende.",
    "La documentation formelle doit être en place dès l’origine de la relation de couverture et identifier l’élément couvert, l’instrument de couverture et le risque de change couvert.",
    "Si l’objectif du groupe est en réalité de couvrir une activité étrangère, il faut documenter un hedge de net investment sur les net assets concernés, pas sur la créance de dividende."
  ]
}
