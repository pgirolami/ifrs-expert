{
  "assumptions_fr": [
    "Le dividende a déjà été déclaré et comptabilisé en créance/dette intragroupe au niveau des entités.",
    "La créance/dette de dividende est libellée dans une devise générant une exposition de change au sein du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, au niveau consolidé, si la créance de dividende constitue un élément monétaire intragroupe dont le risque de change génère des écarts non entièrement éliminés en consolidation. Dans les extraits fournis, le modèle pertinent est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les faits décrits, le dividende déclaré a déjà donné lieu à une créance/dette intragroupe reconnue, donc à un poste monétaire intragroupe. IFRS 9 prévoit, par exception en consolidation, que le risque de change d’un tel poste peut être un élément couvert s’il crée des écarts de change non entièrement éliminés. Dans cette situation, la qualification la plus cohérente est une couverture de juste valeur d’un actif/passif reconnu.",
      "conditions_fr": [
        "La créance/dette de dividende doit être un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.",
        "Le risque de change doit donner lieu à des gains ou pertes de change non entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "Si ces conditions sont remplies, la documentation formelle de couverture au niveau consolidé doit être établie dès la désignation de la relation de couverture.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Ici, le dividende intragroupe n’est plus une transaction future hautement probable : il est déjà comptabilisé en créance à recevoir. Le risque visé porte donc sur la revalorisation d’un poste monétaire reconnu en devise, plutôt que sur une variabilité de flux futurs au sens du modèle de cash flow hedge. Sur les faits décrits, ce modèle ne correspond pas à la situation à documenter en consolidation.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe ne devrait pas fonder sa qualification formelle sur un cash flow hedge pour une créance de dividende déjà reconnue.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "La question vise une créance de dividende intragroupe déjà comptabilisée, et non un montant de net assets d’une activité étrangère. Or IFRIC 16 encadre la couverture d’investissement net par référence au risque de change sur l’investissement net lui-même. Dans cette situation, la créance de dividende est distincte de l’investissement net et ne relève pas de ce modèle.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe ne devrait pas qualifier cette couverture comme une couverture d’investissement net sur la seule base de la créance de dividende.",
      "references": [
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        },
        {
          "section": "6.5.2",
          "excerpt": "hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord si la créance/dette de dividende est bien un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.",
    "Documenter explicitement, au niveau consolidé, que le risque de change sur ce poste crée des écarts affectant le résultat consolidé et n’est pas entièrement éliminé en consolidation.",
    "Si la relation est désignée, la voie à documenter est la couverture de juste valeur, avec désignation et documentation formelles à l’origine de la relation de couverture."
  ]
}
