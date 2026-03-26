{
  "assumptions_fr": [
    "La question est analysée au regard d'IFRS 9 dans des états financiers consolidés.",
    "Le dividende intragroupe est libellé en devise et crée une exposition au risque de change au sein du groupe.",
    "Le dividende a déjà été comptabilisé en créance à recevoir ; il s'agit donc d'un poste intragroupe reconnu."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions : au niveau consolidé, une créance de dividende intragroupe en devise peut être désignée formellement pour le risque de change si elle constitue un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés. Le modèle le plus cohérent dans ce cas est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d'investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d'un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende déjà comptabilisé en créance à recevoir crée un couple créance/dette intragroupe. IFRS 9 admet, en consolidation, qu'un risque de change sur un poste monétaire intragroupe soit un élément couvert si les écarts de change correspondants ne sont pas totalement éliminés, ce qui vise précisément les relations entre entités à monnaies fonctionnelles différentes.",
      "conditions_fr": [
        "La créance de dividende et la dette correspondante sont des postes monétaires entre entités à monnaies fonctionnelles différentes.",
        "Les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Il faut d'abord démontrer que la créance de dividende en devise reste une exposition de change pertinente au niveau consolidé.",
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
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La situation porte sur une créance déjà reconnue, donc sur un actif comptabilisé et non sur un flux futur encore à naître. Le modèle de couverture de juste valeur est cohérent avec un risque de change sur un actif reconnu pouvant affecter le résultat consolidé, sous réserve que la créance soit éligible en consolidation comme poste monétaire intragroupe.",
      "conditions_fr": [
        "La créance de dividende est déjà reconnue et reste en cours au moment de la désignation.",
        "Le risque de change sur cette créance affecte le résultat consolidé parce que l'exception relative aux postes monétaires intragroupe est satisfaite."
      ],
      "practical_implication_fr": "La voie formelle la plus défendable est de documenter la créance reconnue comme élément couvert dans une relation de couverture de juste valeur.",
      "references": [
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
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans les faits posés, le dividende n'est plus une transaction future intragroupe hautement probable : il a déjà été comptabilisé en créance à recevoir. Le contexte rattache surtout ce modèle, au niveau consolidé, aux transactions intragroupe futures hautement probables ; il ne correspond donc pas au mieux à une créance de dividende déjà reconnue.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle ne doit pas être retenu pour ce cas précis de créance de dividende déjà comptabilisée.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "B6.3.5",
          "excerpt": "a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "La couverture d'un investissement net vise un montant de net assets d'une activité étrangère et le risque de change qui s'y rattache. Une créance de dividende intragroupe déjà reconnue est un poste monétaire isolé, pas un montant de net assets d'une activité étrangère ; ce modèle n'est donc pas adapté à la situation décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas qualifier la créance de dividende comme couverture d'investissement net au niveau consolidé.",
      "references": [
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier les monnaies fonctionnelles des deux entités et établir que la créance de dividende intragroupe génère des écarts de change non totalement éliminés en consolidation.",
    "Documenter dès l'origine la relation de couverture, l'instrument de couverture, la créance couverte, le risque de change désigné et la manière d'apprécier l'efficacité.",
    "Privilégier une qualification en couverture de juste valeur pour une créance de dividende déjà comptabilisée.",
    "Ne pas retenir la couverture de flux de trésorerie si le dividende n'est plus une transaction future hautement probable mais un poste déjà reconnu.",
    "Ne pas utiliser la couverture d'investissement net, sauf si l'élément couvert est un montant de net assets d'une activité étrangère, ce qui n'est pas le cas ici."
  ]
}
