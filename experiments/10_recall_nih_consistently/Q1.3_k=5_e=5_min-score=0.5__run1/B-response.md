{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé, au sein du groupe, une créance ou une dette monétaire libellée en devise.",
    "La question vise l'application de la comptabilité de couverture dans les états financiers consolidés selon IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si le dividende déclaré crée une créance monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans ce cas, le risque de change peut être désigné dans une relation de couverture documentée; en revanche, le modèle de couverture d’un investissement net ne correspond pas à cette situation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La situation décrite porte sur une créance de dividende déjà comptabilisée; il s’agit donc d’un actif reconnu, ce qui entre dans le champ d’une couverture de juste valeur.\nEn consolidé, l’élément intragroupe est en principe exclu, mais l’exception visant le risque de change d’un élément monétaire intragroupe permet l’application si les écarts de change ne sont pas totalement éliminés.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe.",
        "Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit viser la créance de dividende comme élément monétaire intragroupe couvert contre son risque de change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende est aussi un actif reconnu dont le montant de règlement en monnaie fonctionnelle varie avec le change, ce qui peut relever d’une couverture de flux de trésorerie.\nDans cette situation précise, cela n’est recevable en consolidé que si la créance répond à l’exception applicable aux éléments monétaires intragroupe dont le risque de change affecte encore le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe exposé au change jusqu’à son règlement.",
        "Les écarts de change sur cette créance affectent le résultat consolidé et ne sont pas totalement éliminés."
      ],
      "practical_implication_fr": "Le modèle n’est pertinent que si l’exposition documentée est bien la variabilité du montant de règlement en monnaie fonctionnelle.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Le cas décrit ne porte pas sur un montant de net assets d’une activité à l’étranger, mais sur une créance intragroupe née d’un dividende déclaré.\nLa couverture d’un investissement net vise le risque de change sur l’investissement net dans l’activité étrangère; elle ne convient donc pas à une créance de dividende intragroupe.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette créance de dividende comme une couverture d’investissement net.",
      "references": [
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé est l’exception de l’élément monétaire intragroupe en consolidation; sans écarts de change non totalement éliminés, la désignation échoue.",
    "Le moment déterminant est après la déclaration du dividende, lorsque la créance à recevoir est comptabilisée.",
    "La relation documentée doit choisir explicitement un modèle cohérent avec l’exposition retenue: juste valeur ou flux de trésorerie, mais pas investissement net."
  ]
}
