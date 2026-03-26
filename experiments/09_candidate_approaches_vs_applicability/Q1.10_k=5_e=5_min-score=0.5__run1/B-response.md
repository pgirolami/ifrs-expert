{
  "assumptions_fr": [
    "L’analyse est faite du point de vue des états financiers consolidés du groupe.",
    "Le dividende intragroupe comptabilisé à recevoir / à payer est un poste monétaire reconnu et libellé dans une devise créant une exposition de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, mais seulement si le dividende intragroupe constitue un poste monétaire en devise dont les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé. Dans ce cas, la couverture de juste valeur est la voie la plus directe; une couverture de flux de trésorerie peut aussi être documentée selon l’objectif retenu."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation de consolidation, la règle générale exclut les postes intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe.\nSi le dividende à recevoir en devise génère des écarts de change non totalement éliminés en consolidation, il peut être désigné comme élément couvert; le modèle de juste valeur correspond directement à un actif reconnu.",
      "conditions_fr": [
        "la créance ou dette de dividende intragroupe est un poste monétaire en devise",
        "les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé"
      ],
      "practical_implication_fr": "Documenter le dividende intragroupe à recevoir comme élément couvert limité au risque de change, avec suivi des écarts résiduels au niveau consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le même régime d’exception pour le poste monétaire intragroupe peut, dans ce cas précis, permettre une désignation en couverture du risque de change sous l’angle de la variabilité des flux d’encaissement.\nCela n’est pertinent que si la documentation vise bien les flux en monnaie fonctionnelle liés à l’encaissement du dividende; sans effet résiduel sur le résultat consolidé, cette voie ne s’applique pas.",
      "conditions_fr": [
        "la créance ou dette de dividende intragroupe est un poste monétaire en devise",
        "les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé",
        "la relation est documentée comme couverture de la variabilité des flux d’encaissement du dividende en monnaie fonctionnelle"
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la documentation doit viser l’encaissement futur du dividende en devise et non l’investissement net dans la filiale.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Ce traitement ne correspond pas aux faits: le poste visé est une créance de dividende intragroupe reconnue, non un montant de net assets d’une opération étrangère.\nIFRIC 16 réserve ce modèle au risque de change sur l’investissement net dans l’opération étrangère elle-même, mesuré entre monnaies fonctionnelles pertinentes.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter le dividende intragroupe à recevoir comme couverture d’investissement net, car l’objet couvert serait mal identifié.",
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
    "Vérifier que les entités concernées ont des monnaies fonctionnelles différentes et que le dividende en devise produit bien un écart de change non totalement éliminé en consolidation.",
    "Documenter dès l’inception l’élément couvert, l’instrument de couverture et le fait que seul le risque de change du dividende intragroupe est visé.",
    "Choisir explicitement le modèle de couverture: juste valeur pour un actif reconnu; flux de trésorerie seulement si la documentation cible la variabilité des flux d’encaissement.",
    "Écarter le modèle d’investissement net, qui vise les actifs nets d’une opération étrangère et non un dividende intragroupe à recevoir."
  ]
}
