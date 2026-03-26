{
  "assumptions_fr": [
    "La question vise les comptes consolidés.",
    "La créance ou dette de dividende intragroupe est libellée en devise étrangère et crée une exposition au change.",
    "La problématique posée concerne uniquement la composante de risque de change de ce solde intragroupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si le dividende intragroupe reconnu en créance/dette constitue un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. La base la plus directe est l’exception d’IFRS 9 sur le risque de change des éléments monétaires intragroupe, avec désignation possible de la seule composante change."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe fait naître un risque de change au niveau consolidé. IFRS 9 prévoit précisément, par exception, que le risque de change d’un élément monétaire intragroupe peut être désigné comme élément couvert si les écarts de change ne sont pas totalement éliminés en consolidation.",
      "conditions_fr": [
        "La créance/dette de dividende est un élément monétaire intragroupe.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation peut viser directement le risque de change du solde intragroupe reconnu.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
        },
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture d’une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question vise explicitement la seule composante change du solde de dividende intragroupe, et non l’intégralité de la créance. IFRS 9 permet de désigner une composante de risque d’un item, à condition qu’elle soit séparément identifiable et mesurable de façon fiable, ce qui cadre avec une composante change sur un solde en devise.",
      "conditions_fr": [
        "La composante change est séparément identifiable.",
        "La composante change est mesurable de façon fiable.",
        "Le solde intragroupe sous-jacent est admissible en consolidation au titre de l’exception des éléments monétaires intragroupe."
      ],
      "practical_implication_fr": "La relation de couverture peut être documentée sur la seule composante change, sans couvrir tout le solde.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "B6.3.8",
          "excerpt": "separately identifiable and reliably measurable"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà matérialisé par une créance ou dette reconnue. Le modèle de couverture de juste valeur est donc cohérent avec un actif ou passif reconnu lorsque la composante change de ce solde est la composante désignée et que cette exposition affecte le résultat consolidé.",
      "conditions_fr": [
        "La relation est documentée sur la composante change d’une créance/dette déjà reconnue.",
        "L’exposition de change affecte le résultat consolidé."
      ],
      "practical_implication_fr": "C’est le modèle le plus naturel si l’objectif est de couvrir le risque de change porté par le solde déjà comptabilisé.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Les extraits n’excluent pas une couverture de flux de trésorerie sur un actif ou passif reconnu. Dans ce cas précis, cette voie n’est recevable que si la relation est documentée comme couverture de la variabilité des flux de règlement en monnaie fonctionnelle liée au change sur la créance/dette intragroupe, avec effet sur le résultat consolidé.",
      "conditions_fr": [
        "La couverture vise la variabilité des flux de règlement en monnaie fonctionnelle du solde reconnu.",
        "Cette variabilité de change affecte le résultat consolidé."
      ],
      "practical_implication_fr": "Cette voie est possible, mais sa documentation doit être centrée sur les flux futurs de règlement du dividende.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2",
          "excerpt": "associated with all, or a component of, a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord que le solde de dividende intragroupe crée bien des écarts de change non totalement éliminés en consolidation, ce qui suppose en pratique des monnaies fonctionnelles différentes.",
    "La documentation doit être établie dès l’origine de la relation et inclure l’instrument de couverture, le solde couvert, la composante de risque de change, le hedge ratio et les sources d’inefficacité.",
    "Si la créance de dividende est déjà reconnue, la couverture de juste valeur est la lecture la plus directe ; la couverture de flux de trésorerie exige une documentation explicite de la variabilité des flux de règlement en monnaie fonctionnelle."
  ]
}
