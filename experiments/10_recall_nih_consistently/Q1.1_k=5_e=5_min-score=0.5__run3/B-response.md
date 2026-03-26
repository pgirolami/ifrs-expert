{
  "assumptions_fr": [
    "La créance de dividende intragroupe génère, dans les comptes consolidés, une exposition de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais essentiellement via une couverture de juste valeur de la créance intragroupe sur sa composante change.\nCela suppose que le risque de change sur ce poste monétaire ne soit pas totalement éliminé en consolidation. Les deux autres voies identifiées ne correspondent pas aux faits actuels."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur d'un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende est déjà comptabilisé en créance, donc il s'agit d'un actif reconnu.\nLe contexte prévoit qu'un poste monétaire intragroupe peut être un élément couvert en consolidation pour le risque de change s'il crée un écart de change non totalement éliminé.\nLa documentation de couverture pertinente est donc, ici, la couverture de juste valeur sur la partie change.",
      "conditions_fr": [
        "La créance de dividende est un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "C'est la voie à analyser en priorité pour documenter la couverture d'une créance de dividende déjà comptabilisée.",
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
      "label_fr": "Couverture de flux de trésorerie d'une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, le dividende n'est plus une transaction intragroupe prévue : il a déjà donné lieu à une créance comptabilisée.\nOr l'approche identifiée vise une transaction intragroupe hautement probable, non encore comptabilisée.\nElle ne correspond donc pas aux faits actuels.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie aurait du sens avant la comptabilisation de la créance, pas une fois le dividende reconnu en receivable.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
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
      "label_fr": "Couverture d'un investissement net dans une activité à l'étranger",
      "applicability": "non",
      "reasoning_fr": "La question porte sur une créance de dividende intragroupe, pas sur les net assets d'une activité étrangère.\nLe hedge de net investment vise le risque de change attaché à un investissement net dans une foreign operation.\nCette documentation n'est donc pas adaptée au poste décrit.",
      "conditions_fr": [],
      "practical_implication_fr": "À écarter pour cette créance de dividende ; ce modèle vise une exposition de type investissement net.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Comme la créance est déjà née, la voie à documenter en priorité est la couverture de juste valeur, pas la couverture de flux de trésorerie d'une transaction prévue.",
    "En consolidation, le point décisif est de vérifier que le risque de change sur la créance intragroupe n'est pas totalement éliminé ; sinon il n'y a pas d'élément couvert admissible sur cette base.",
    "La couverture d'investissement net doit rester cantonnée aux expositions sur net assets d'une activité étrangère et ne doit pas être utilisée pour une simple créance de dividende.",
    "La relation de couverture retenue doit être formellement désignée et documentée à l'inception conformément à IFRS 9 6.4.1."
  ]
}
