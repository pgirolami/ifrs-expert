{
  "assumptions_fr": [
    "Le dividende intragroupe à recevoir/à payer est un poste monétaire comptabilisé, libellé en devise, entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
    "L’entité souhaite désigner uniquement la composante de risque de change, et cette composante est séparément identifiable et fiable à mesurer."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. Dans cette situation, IFRS 9 permet en consolidation de désigner la seule composante de change d’un poste monétaire intragroupe si l’effet de change subsiste en résultat consolidé. La couverture de juste valeur est la lecture la plus directe pour un dividende déjà comptabilisé, la couverture de flux de trésorerie restant également envisageable si elle est correctement documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe à recevoir est supposé être un poste monétaire comptabilisé dont l’effet de change n’est pas totalement éliminé en consolidation.\nL’exception d’IFRS 9 pour les postes monétaires intragroupe permet alors de le traiter comme élément couvert en comptes consolidés, malgré la règle générale visant des contreparties externes.\nComme seule la composante de change est visée et qu’elle est supposée séparément identifiable et fiable à mesurer, une couverture de juste valeur peut s’appliquer si la relation est formellement désignée et satisfait les critères d’efficacité.",
      "conditions_fr": [
        "Le dividende intragroupe est un poste monétaire en devise entre entités aux monnaies fonctionnelles différentes.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La seule composante de change est séparément identifiable et fiable à mesurer.",
        "La relation de couverture est désignée et documentée dès l’origine, avec relation économique et hedge ratio approprié."
      ],
      "practical_implication_fr": "Le suivi portera en consolidation sur la variation de valeur du dividende liée au seul change et sur l’inefficacité éventuelle de la couverture.",
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
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi de couvrir la variabilité de flux de trésorerie d’un actif comptabilisé lorsqu’elle est attribuable à un risque particulier.\nSi le dividende intragroupe en devise expose le groupe à une variabilité des encaissements en monnaie fonctionnelle et que ce risque de change affecte le résultat consolidé, l’exception relative aux postes monétaires intragroupe reste disponible.\nLa désignation de la seule composante de change est alors possible, sous réserve de la documentation initiale et du respect des critères d’efficacité de la relation.",
      "conditions_fr": [
        "Le dividende intragroupe est un actif ou passif comptabilisé dont les flux en monnaie fonctionnelle varient en raison du change.",
        "Le risque de change sur ce poste monétaire intragroupe affecte le résultat consolidé et n’est pas totalement éliminé.",
        "La composante de change désignée est séparément identifiable et fiable à mesurer.",
        "La relation de couverture est désignée et documentée dès l’origine, avec relation économique et hedge ratio approprié."
      ],
      "practical_implication_fr": "Il faut suivre en consolidation la variabilité des flux liée au change jusqu’au règlement du dividende et mesurer l’efficacité de la relation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l’origine l’instrument de couverture, le dividende intragroupe couvert, le risque de change visé et le hedge ratio.",
    "Vérifier en consolidation que l’écart de change sur le dividende intragroupe n’est pas totalement éliminé et affecte bien le résultat consolidé.",
    "Limiter la désignation à la seule composante de change si elle est séparément identifiable et fiable à mesurer.",
    "Retenir un modèle de couverture cohérent avec l’objectif de gestion du risque sur ce dividende déjà comptabilisé."
  ]
}
