{
  "assumptions_fr": [
    "La créance de dividende intragroupe, ou le solde associé, génère bien une exposition de change dans les comptes consolidés.",
    "La question porte sur l'application de la comptabilité de couverture selon IFRS 9 dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement si la créance de dividende est un élément monétaire intragroupe dont le risque de change n'est pas intégralement éliminé en consolidation et affecte le résultat consolidé. Dans ce cas, la voie la plus solide est la couverture de juste valeur; la couverture d'investissement net n'est pas adaptée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidé, un élément intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Ici, la question vise une créance déjà comptabilisée : si cette créance de dividende répond à cette exception et affecte le résultat consolidé, une couverture de juste valeur est cohérente avec un actif reconnu.",
      "conditions_fr": [
        "La créance de dividende doit constituer un élément monétaire intragroupe en devise.",
        "Les écarts de change correspondants doivent ne pas être intégralement éliminés en consolidation et affecter le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation doit viser la créance de dividende en devise comme élément couvert et le risque de change résiduel en résultat consolidé.",
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
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Le contexte IFRS 9 vise, pour l'intragroupe en consolidé, soit un élément monétaire existant, soit une transaction intragroupe future et hautement probable. Or ici le dividende a déjà donné lieu à une créance comptabilisée : l'exposition décrite porte sur la réévaluation d'une créance existante, pas sur une transaction future de dividende à couvrir en flux.",
      "conditions_fr": [],
      "practical_implication_fr": "Dans cette situation, documenter la relation en cash flow hedge n'est pas l'option la plus adaptée au fait générateur décrit.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise le risque de change sur un investissement net dans une activité étrangère, c'est-à-dire un montant de net assets de l'opération étrangère. Une créance de dividende intragroupe déjà comptabilisée n'est pas, dans les textes fournis, assimilée à cet investissement net.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter le change sur une créance de dividende intragroupe comme une couverture d'investissement net.",
      "references": [
        {
          "section": "6.5.2(c)",
          "excerpt": "hedge of a net investment in a foreign operation"
        },
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
    "Vérifier en premier si les écarts de change sur la créance de dividende sont réellement non intégralement éliminés en consolidation; sinon il n'y a pas d'élément couvert éligible en consolidé.",
    "Si la relation est documentée, la désignation doit intervenir à l'inception et identifier l'instrument de couverture, la créance intragroupe couverte, le risque de change et le hedge ratio.",
    "La couverture doit porter sur la créance de dividende en devise et son risque de change résiduel, pas sur le dividende intragroupe en tant que flux interne éliminé."
  ]
}
