{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et comptabilisé en créance/dette intragroupe, de sorte qu’il constitue un item monétaire.",
    "Les entités concernées ont des monnaies fonctionnelles différentes, si bien que les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Les exigences générales d’IFRS 9 en matière de désignation, de documentation et d’efficacité de la couverture sont respectées."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. Une fois le dividende intragroupe comptabilisé en créance/dette, il entre dans l’exception IFRS 9 visant les items monétaires intragroupe en consolidation si le risque de change affecte le résultat consolidé. La relation de couverture doit en outre être formellement désignée, documentée et efficace."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe déjà comptabilisé est un actif/passif intragroupe monétaire. IFRS 9 autorise en consolidation, par exception, la désignation du risque de change d’un item monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat consolidé; le modèle de couverture de juste valeur est donc directement pertinent pour cette créance reconnue.",
      "conditions_fr": [
        "Le dividende doit être déjà comptabilisé en créance/dette intragroupe monétaire.",
        "Les écarts de change correspondants doivent ne pas être totalement éliminés en consolidation et affecter le résultat consolidé.",
        "La relation doit être formellement désignée et documentée dès l’inception, avec démonstration de l’efficacité et d’un hedge ratio approprié."
      ],
      "practical_implication_fr": "C’est le modèle le plus directement aligné avec une créance de dividende intragroupe déjà reconnue et exposée au change en consolidation.",
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le texte d’IFRS 9 permet aussi une couverture de flux de trésorerie sur un actif ou passif comptabilisé. Ici, si l’objectif documenté est de couvrir la variabilité du montant de règlement en monnaie fonctionnelle de la créance de dividende, et si l’exception applicable aux items monétaires intragroupe en consolidation est satisfaite, ce traitement peut également s’appliquer dans ce cas précis.",
      "conditions_fr": [
        "Le risque couvert doit être formulé comme une variabilité des flux de règlement en monnaie fonctionnelle de la créance/dette de dividende.",
        "Le dividende intragroupe comptabilisé doit relever de l’exception de l’item monétaire intragroupe affectant le résultat consolidé.",
        "La désignation, la documentation et l’évaluation de l’efficacité doivent satisfaire IFRS 9."
      ],
      "practical_implication_fr": "Ce modèle est envisageable si la documentation vise explicitement la variabilité des flux de règlement jusqu’au paiement du dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif en consolidation est l’exception d’IFRS 9 pour le risque de change d’un item monétaire intragroupe; sans effet sur le résultat consolidé, la désignation ne tient pas.",
    "Le timing compte: la relation de couverture doit être formellement désignée et documentée dès son inception, avec identification de l’instrument, de l’item couvert, du risque couvert et du hedge ratio.",
    "IFRIC 16 n’est pas la base de cette conclusion, car elle vise uniquement les couvertures de net investment et ne doit pas être appliquée par analogie aux autres couvertures."
  ]
}
