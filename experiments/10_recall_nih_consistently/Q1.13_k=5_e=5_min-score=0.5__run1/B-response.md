{
  "assumptions_fr": [
    "On suppose que la créance est un poste monétaire comptabilisé qui génère une exposition au risque de change.",
    "On suppose que la question porte sur la comptabilité de couverture selon IFRS 9 dans des états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : dans les comptes consolidés, la créance de dividende intragroupe ne peut entrer dans une relation de couverture que si elle constitue un poste monétaire intragroupe dont le risque de change génère des écarts non totalement éliminés en consolidation. Dans ce cas, la composante de change — ou la créance entière — peut être désignée; pas en couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "risk_component_designation",
      "label_fr": "Désignation de la composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question vise la composante de risque de change d’une créance intragroupe déjà comptabilisée. Cette désignation est possible si la créance est un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation; sinon, l’élément ne reste pas éligible dans les comptes consolidés.",
      "conditions_fr": [
        "La créance doit être un poste monétaire intragroupe générant des écarts de change non totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit identifier explicitement la créance, la composante de change couverte et la raison pour laquelle l’exception intragroupe s’applique en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "entire_item_designation",
      "label_fr": "Désignation de l’élément entier",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Même si la question porte sur la composante de change, IFRS 9 permet aussi de désigner la créance entière comme élément couvert. Dans cette situation, cela n’est envisageable en consolidation que si la créance intragroupe bénéficie de l’exception applicable aux postes monétaires intragroupe exposés à un risque de change non totalement éliminé.",
      "conditions_fr": [
        "La créance entière doit rester éligible en consolidation au titre de l’exception visant les postes monétaires intragroupe."
      ],
      "practical_implication_fr": "Si cette voie est retenue, la relation de couverture doit viser la créance entière et non seulement sa composante de change.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "An entity may designate an item in its entirety or a component of an item as the hedged item"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance à recevoir est, selon l’hypothèse retenue, un actif comptabilisé; le modèle de juste valeur vise précisément un actif ou une composante exposé(e) à un risque particulier. Dans ce cas précis, le modèle n’est pertinent en consolidation que si les variations de change sur la créance peuvent affecter le résultat consolidé parce qu’elles ne sont pas totalement éliminées.",
      "conditions_fr": [
        "Les écarts de change sur la créance doivent pouvoir affecter le résultat consolidé et ne pas être totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "Il faut documenter la relation comme une couverture de l’exposition de la créance aux variations de valeur liées au change.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ce modèle peut convenir si la relation documentée vise la variabilité, en monnaie fonctionnelle, des flux d’encaissement liés à la créance de dividende. Dans les comptes consolidés, il faut toutefois que le risque de change sur cette créance intragroupe puisse affecter le résultat consolidé, faute de quoi l’élément n’est pas qualifiable.",
      "conditions_fr": [
        "La relation doit viser la variabilité des flux de trésorerie attribuable au change sur la créance.",
        "Le risque de change sur la créance doit affecter le résultat consolidé et ne pas être totalement éliminé en consolidation."
      ],
      "practical_implication_fr": "La documentation doit expliquer pourquoi l’exposition couverte est traitée comme une variabilité de flux de trésorerie liée au change.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_5",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Une créance de dividende intragroupe comptabilisée est une créance monétaire à régler, pas un montant de net assets d’une activité à l’étranger. Le modèle de couverture d’investissement net vise le risque de change attaché à l’investissement net dans une activité étrangère; il ne correspond donc pas à cette créance de dividende.",
      "conditions_fr": [],
      "practical_implication_fr": "Une documentation de couverture d’investissement net pour cette créance devrait être écartée au profit d’un modèle de couverture portant sur le poste monétaire lui-même, si les conditions sont remplies.",
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
    "La désignation et la documentation formelles doivent exister dès l’inception de la relation de couverture et identifier l’instrument, la créance, le risque de change et le hedge ratio.",
    "Avant toute désignation, il faut vérifier en consolidation que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés; c’est le point décisif du cas présenté.",
    "Le choix du modèle doit être cohérent avec l’exposition effectivement documentée: composante de change ou créance entière, et couverture de juste valeur ou de flux de trésorerie; pas couverture d’investissement net."
  ]
}
