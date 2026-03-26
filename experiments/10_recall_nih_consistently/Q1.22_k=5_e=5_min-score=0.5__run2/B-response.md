{
  "assumptions_fr": [
    "L'analyse est effectuée au niveau des comptes consolidés.",
    "L'exposition visée provient d'un dividende intragroupe devenu une créance ou une dette monétaire."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, IFRS 9 exclut en principe les éléments intragroupe, mais admet par exception le risque de change d'un poste monétaire intragroupe lorsqu'il génère des écarts non entièrement éliminés. La composante de change du dividende devenu créance ou dette peut donc être documentée; la couverture d'investissement net n'est pas la bonne voie ici."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende est supposé déjà reconnu en créance ou dette; il s'agit donc d'un actif ou passif comptabilisé. La règle générale d'exclusion des éléments intragroupe en consolidation est levée, pour le seul risque de change, par l'exception visant les postes monétaires intragroupe dont les écarts ne sont pas totalement éliminés. Une documentation en couverture de juste valeur est donc permise dans cette situation.",
      "conditions_fr": [
        "La créance ou dette de dividende constitue un poste monétaire intragroupe.",
        "Les écarts de change correspondants ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "Désigner la créance ou dette de dividende reconnue comme élément couvert et limiter le risque désigné au change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
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
      "reasoning_fr": "La créance ou dette de dividende sera réglée et son montant en monnaie fonctionnelle varie avec le change. Le texte admet une couverture de flux sur un actif ou passif reconnu, et l'exception de 6.3.6 permet précisément, en consolidation, de viser le risque de change d'un poste monétaire intragroupe. Cette approche est donc aussi ouverte si l'exposition documentée est la variabilité des flux de règlement due au change.",
      "conditions_fr": [
        "La relation couvre la variabilité des flux de règlement due au change sur la créance ou dette reconnue.",
        "Les écarts de change de ce poste monétaire intragroupe ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit rattacher le risque couvert aux flux de règlement du dividende intragroupe reconnu.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
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
      "reasoning_fr": "La question porte sur une créance ou dette de dividende intragroupe reconnue, pas sur les actifs nets d'une activité étrangère. IFRIC 16 limite cette technique au risque de change lié à un investissement net dans une activité étrangère et précise qu'elle ne doit pas être appliquée par analogie à d'autres couvertures. Cette voie ne correspond donc pas à la situation décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas traiter la créance de dividende comme une couverture d'investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "10",
          "excerpt": "only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture d'une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le risque visé est précisément la composante de change d'une créance ou dette intragroupe reconnue. IFRS 9 autorise la désignation d'un composant de risque d'un élément, à condition qu'il soit séparément identifiable et mesurable de façon fiable; combiné à l'exception applicable aux postes monétaires intragroupe, cela permet de documenter la seule composante de change dans ce cas.",
      "conditions_fr": [
        "La composante de change est séparément identifiable et mesurable de façon fiable.",
        "Le poste couvert reste le risque de change d'un poste monétaire intragroupe dont les écarts ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "Isoler explicitement la seule composante de change dans la désignation du poste couvert.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "may designate an item in its entirety or a component of an item as the hedged item"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie dès l'inception de la relation et identifier l'instrument de couverture, la créance ou dette de dividende, le risque de change couvert et la façon d'apprécier l'efficacité.",
    "Le point décisif est que le dividende intragroupe reconnu crée bien un poste monétaire entre entités de monnaies fonctionnelles différentes, avec des écarts de change encore pertinents en consolidation.",
    "La base la plus solide ici est la combinaison de l'exception sur les postes monétaires intragroupe et de la désignation d'une composante de risque; la couverture d'investissement net doit être écartée."
  ]
}
