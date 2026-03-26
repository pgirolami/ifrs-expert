{
  "assumptions_fr": [
    "La question est analysée dans le cadre d’états financiers consolidés préparés selon IFRS 9.",
    "Le dividende intragroupe est libellé en devise et donne lieu, une fois la créance constatée, à un solde monétaire intragroupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, la documentation peut porter sur la seule composante change d’une créance de dividende intragroupe reconnue via une couverture de juste valeur, si cette créance est un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés. Ce n’est ni une cash flow hedge du dividende, ni une couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est déjà comptabilisée : il s’agit donc d’un actif reconnu et non d’une transaction future.\nEn consolidation, IFRS 9 admet par exception le risque de change d’un poste monétaire intragroupe comme élément couvert si les écarts de change ne sont pas totalement éliminés ; la documentation peut donc viser cette créance.",
      "conditions_fr": [
        "la créance doit être un poste monétaire intragroupe exposé au risque de change",
        "les écarts de change sur cette créance doivent ne pas être totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La relation de couverture peut être documentée de façon prospective sur la créance reconnue, en couvrant son exposition de change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "applicability": "non",
      "reasoning_fr": "Le cas posé porte sur une créance déjà reconnue, alors que la cash flow hedge visée dans le contexte concerne une transaction future hautement probable.\nL’exception intragroupe en consolidation pour les transactions prévisionnelles ne correspond donc pas à ce fait générateur déjà survenu.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette situation comme une couverture de flux de trésorerie du dividende intragroupe.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture d’une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 permet de désigner une composante de risque plutôt que l’élément entier. Dans votre cas, la composante change de la créance de dividende est identifiable et mesurable.\nCette désignation n’est toutefois recevable en consolidation que si la créance intragroupe elle-même entre dans l’exception applicable aux postes monétaires intragroupe.",
      "conditions_fr": [
        "la couverture doit se limiter à la composante change de la créance",
        "la créance intragroupe doit pouvoir être qualifiée d’élément couvert en consolidation au titre de l’exception des postes monétaires intragroupe"
      ],
      "practical_implication_fr": "La documentation peut isoler la seule composante change, sans couvrir l’intégralité de la créance.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component of the financial or the non-financial item, and the changes in the cash flows or the fair value of the item attributable to changes in that risk component must be reliably measurable"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Le dividende intragroupe devenu créance est un solde monétaire intragroupe ; ce n’est pas un montant de net assets constituant un investissement net dans une activité étrangère.\nIFRIC 16 réserve ce modèle aux couvertures d’investissement net et précise qu’il ne doit pas être appliqué par analogie à d’autres couvertures.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation ne doit pas être fondée sur le modèle de couverture d’investissement net pour ce cas.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que la créance de dividende est bien un poste monétaire intragroupe générant des écarts de change non totalement éliminés en consolidation.",
    "Documenter la relation de couverture de façon prospective à compter de la reconnaissance de la créance, en pratique sous forme de couverture de juste valeur limitée à la composante change.",
    "Écarter, sur ces faits, une documentation en cash flow hedge du dividende intragroupe ou en net investment hedge."
  ]
}
