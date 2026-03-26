{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré, de sorte qu'une créance à recevoir et une dette à payer intragroupe ont été comptabilisées.",
    "La créance de dividende est libellée dans une monnaie différente de la monnaie fonctionnelle d'au moins l'une des entités concernées.",
    "L'analyse est faite au niveau des comptes consolidés du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : une créance de dividende intragroupe peut être désignée en couverture dans les comptes consolidés si elle constitue un élément monétaire intragroupe dont les écarts de change ne sont pas intégralement éliminés en consolidation et affectent le résultat consolidé. En revanche, ce fait ne relève pas d'une couverture d'investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende déjà comptabilisée est un actif reconnu, ce qui cadre avec le modèle de juste valeur pour un risque particulier affectant le résultat.\nDans cette situation consolidée, l'obstacle intragroupe est levé seulement si la créance est un élément monétaire dont les écarts de change ne sont pas totalement éliminés à la consolidation.",
      "conditions_fr": [
        "La créance de dividende constitue un élément monétaire intragroupe.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change sur cette créance ne sont pas intégralement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Documenter la créance de dividende comme élément couvert et cibler explicitement le risque de change dans la relation de couverture.",
      "references": [
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le contexte IFRS 9 admet une couverture de flux de trésorerie sur un actif reconnu lorsqu'un risque particulier crée une variabilité des flux.\nPour cette créance de dividende intragroupe en devise, l'approche n'est recevable en consolidation que si le risque de change de l'élément monétaire affecte le résultat consolidé et n'est pas entièrement éliminé.",
      "conditions_fr": [
        "La créance de dividende est libellée en devise et expose le groupe à une variabilité de flux en monnaie fonctionnelle.",
        "La créance est un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.",
        "Les écarts de change correspondants affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, il faut démontrer la variabilité des flux liée au change sur la créance reconnue et l'articuler avec le ratio de couverture.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
        },
        {
          "section": "6.3.6",
          "excerpt": "are not fully eliminated on consolidation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net dans une activité à l'étranger",
      "applicability": "non",
      "reasoning_fr": "Le modèle de couverture d'investissement net vise le risque de change lié aux net assets d'une activité étrangère dans les états financiers consolidés.\nUne créance de dividende intragroupe née d'une distribution n'est pas, dans cette situation, un montant de net assets désigné comme investissement net.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter la créance de dividende comme une couverture d'investissement net ; ce modèle vise un autre objet couvert.",
      "references": [
        {
          "section": "2",
          "excerpt": "foreign currency risk arising from a net investment in a foreign operation"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets"
        },
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier au moment de la déclaration du dividende qu'une créance et une dette monétaires intragroupe existent bien.",
    "Confirmer que les deux entités ont des monnaies fonctionnelles différentes ; sinon, l'exception intragroupe de change ne fonctionne pas.",
    "Démontrer que les écarts de change sur la créance de dividende ne sont pas intégralement éliminés en consolidation et affectent le résultat consolidé.",
    "Préparer dès l'inception la documentation exigée par IFRS 9 : instrument de couverture, élément couvert, risque de change visé et hedge ratio.",
    "Si le dividende n'est pas encore déclaré, l'analyse bascule d'une créance reconnue vers une transaction intragroupe prévue, avec un cadre différent."
  ]
}
