{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà donné naissance à une créance et à une dette intragroupe comptabilisées.",
    "La question porte sur le risque de change dans les états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, ce risque peut être formellement documenté en consolidation si la créance/dette de dividende constitue un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés. Dans les faits décrits, la voie la plus cohérente est une relation de couverture du risque de change sur l'élément comptabilisé, avec documentation formelle à l'inception."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà créé une créance/dette comptabilisée. Le contexte prévoit précisément qu'en consolidation le risque de change d'un poste monétaire intragroupe peut être un élément couvert s'il génère des écarts de change non totalement éliminés; cela s'aligne avec une couverture de juste valeur d'un actif ou passif comptabilisé.",
      "conditions_fr": [
        "la créance/dette de dividende est un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes",
        "les écarts de change correspondants ne sont pas totalement éliminés en consolidation",
        "la relation de couverture est formellement désignée et documentée à son inception"
      ],
      "practical_implication_fr": "La documentation peut viser la créance/dette de dividende déjà comptabilisée comme élément couvert du risque de change en consolidation.",
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
      "applicability": "non",
      "reasoning_fr": "Le contexte rattache expressément l'exception intragroupe de cash flow hedge aux transactions intragroupe prévues et hautement probables. Or, dans la situation posée, le dividende a déjà été reconnu en créance/dette intragroupe; il ne s'agit plus d'une transaction future à couvrir comme flux futurs.",
      "conditions_fr": [],
      "practical_implication_fr": "Sur ces faits, il ne faut pas documenter le cas comme une couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "B6.3.5",
          "excerpt": "a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
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
      "label_fr": "Couverture d'un investissement net",
      "applicability": "non",
      "reasoning_fr": "La question vise une créance de dividende intragroupe déjà comptabilisée, pas un montant de net assets d'une activité étrangère. Les extraits IFRIC 16 limitent cette couverture au risque de change lié à un investissement net dans une activité étrangère; ce n'est pas le fait décrit ici.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas fonder la documentation sur un hedge de net investment pour ce poste de dividende intragroupe.",
      "references": [
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        },
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture d'un composant de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, l'exposition pertinente est le seul risque de change attaché à la créance/dette de dividende intragroupe. Le contexte autorise la désignation d'un composant de risque d'un élément, à condition qu'il soit séparément identifiable et fiable à mesurer; c'est donc une manière cohérente de documenter le risque couvert ici.",
      "conditions_fr": [
        "le risque de change désigné est séparément identifiable et fiable à mesurer",
        "l'élément sous-jacent est lui-même admissible en consolidation comme poste monétaire intragroupe au titre du paragraphe 6.3.6"
      ],
      "practical_implication_fr": "La documentation peut viser uniquement le composant risque de change de la créance/dette, et non l'intégralité de l'élément.",
      "references": [
        {
          "section": "6.3.7(a)",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
        },
        {
          "section": "6.3.7",
          "excerpt": "An entity may designate an item in its entirety or a component of an item as the hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter à l'inception de la relation l'instrument de couverture, la créance/dette de dividende couverte, le risque de change visé, la méthode d'efficacité et le hedge ratio.",
    "Vérifier en consolidation que les écarts de change sur le poste monétaire intragroupe ne sont pas totalement éliminés; sinon l'élément n'est pas admissible.",
    "Traiter le cas comme un poste monétaire déjà comptabilisé; la logique de transaction intragroupe future hautement probable n'est pas adaptée aux faits décrits."
  ]
}
