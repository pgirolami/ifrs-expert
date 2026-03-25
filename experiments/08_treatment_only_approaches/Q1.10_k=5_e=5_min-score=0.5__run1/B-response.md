{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et a créé une créance/dette intragroupe comptabilisée, libellée dans une devise différente d'au moins une monnaie fonctionnelle pertinente.",
    "La question vise les états financiers consolidés, et les écarts de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation.",
    "La relation de couverture envisagée respecterait aussi les exigences IFRS 9 de désignation formelle, de documentation et d'efficacité."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation de consolidation, si le dividende à recevoir constitue un élément monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés. La relation doit être formellement documentée et satisfaire aux critères d'efficacité d'IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe déclaré est supposé avoir créé une créance/dette intragroupe reconnue en devise.\nIFRS 9 permet, par exception en consolidation, de désigner le risque de change d'un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés.\nComme il s'agit d'un actif ou passif reconnu, la couverture de juste valeur est documentable ici, sous réserve de la documentation initiale et des critères d'efficacité.",
      "conditions_fr": [
        "Le dividende à recevoir/payable est un élément monétaire intragroupe comptabilisé.",
        "Les écarts de change correspondants affectent encore le résultat consolidé.",
        "La désignation et la documentation sont établies à l'origine de la relation.",
        "La relation respecte l'existence d'une relation économique, l'absence de domination du risque de crédit et un hedge ratio approprié."
      ],
      "practical_implication_fr": "Documenter le dividende intragroupe à recevoir comme élément couvert au titre du risque de change dans une relation de couverture de juste valeur.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende en devise est aussi un actif reconnu dont le montant de règlement en monnaie fonctionnelle varie avec le change.\nIFRS 9 définit la couverture de flux de trésorerie pour la variabilité des flux associés à un actif ou passif reconnu pouvant affecter le résultat.\nCe traitement peut donc aussi être documenté ici, mais seulement si l'entité formalise le risque couvert comme une variabilité de flux et satisfait aux critères d'efficacité.",
      "conditions_fr": [
        "Le dividende à recevoir/payable est un actif ou passif reconnu en devise.",
        "La variabilité des flux de règlement due au change peut affecter le résultat consolidé.",
        "Les écarts de change sur l'élément intragroupe ne sont pas totalement éliminés en consolidation.",
        "La désignation, la documentation et les tests d'efficacité IFRS 9 sont respectés."
      ],
      "practical_implication_fr": "Documenter explicitement la variabilité des flux de règlement du dividende en devise comme risque couvert dans une relation de couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en consolidation que la créance/dette de dividende intragroupe en devise génère bien des écarts de change non totalement éliminés.",
    "Préparer dès l'origine la documentation IFRS 9 : instrument de couverture, élément couvert, risque de change couvert, méthode d'évaluation de l'efficacité et hedge ratio.",
    "Choisir le modèle cohérent avec le risque documenté : variation de valeur du poste reconnu pour la juste valeur, ou variabilité des flux de règlement pour les flux de trésorerie."
  ]
}
