{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un poste monétaire intragroupe libellé en devise entre entités ayant des monnaies fonctionnelles différentes, de sorte que ses effets de change ne sont pas totalement éliminés en consolidation.",
    "La documentation de couverture viserait uniquement la composante risque de change de la créance déjà reconnue."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous ces hypothèses, IFRS 9 permet en consolidation de documenter le risque de change d'une créance intragroupe reconnue relevant de l'exception sur les postes monétaires intragroupe. La voie la plus directe est la couverture de juste valeur; une couverture de flux de trésorerie reste possible si elle vise uniquement les flux futurs de règlement encore exposés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Le dividende est déjà comptabilisé en créance : la temporalité correspond donc à un actif reconnu, ce qui cadre directement avec la définition d'une couverture de juste valeur. Sous l'hypothèse d'un poste monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation, l'exception de 6.3.6 permet de désigner la composante change de cette créance, avec une documentation et des tests d'efficacité mis en place à l'inception de la relation de couverture.",
      "conditions_fr": [
        "Désignation et documentation formelles à l'inception de la relation de couverture",
        "Identification de la seule composante change comme risque couvert",
        "Démonstration de la relation économique, du ratio de couverture et de l'absence de domination du risque de crédit"
      ],
      "practical_implication_fr": "Vous pouvez documenter la créance existante comme élément couvert pour sa seule composante change au niveau consolidé, avec un suivi prospectif de la relation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
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
      "label_fr": "Couverture de flux de trésorerie du règlement en devise de la créance",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les faits donnés, cette approche ne peut viser que la variabilité des flux futurs de règlement de la créance déjà reconnue; elle ne couvre pas rétrospectivement les écarts de change antérieurs à la désignation. Sous la même hypothèse de poste monétaire intragroupe en devise dont l'effet de change subsiste en consolidation, IFRS 9 admet une couverture de flux de trésorerie sur un actif reconnu si la documentation cible explicitement le risque de change des flux futurs et si les critères de 6.4.1 sont remplis.",
      "conditions_fr": [
        "La créance doit rester non réglée à la date de désignation pour qu'il subsiste des flux futurs à couvrir",
        "La documentation doit viser la variabilité des flux futurs de règlement attribuable au change de la créance reconnue",
        "Les critères de désignation, d'efficacité et de ratio de couverture de IFRS 9 6.4.1 doivent être satisfaits"
      ],
      "practical_implication_fr": "La documentation se concentre sur les encaissements futurs en devise liés à la créance existante et impose un suivi prospectif jusqu'au règlement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "L'éligibilité en consolidation repose ici sur l'exception IFRS 9 relative au risque de change d'un poste monétaire intragroupe dont les écarts ne sont pas totalement éliminés.",
    "La relation de couverture doit être désignée et documentée à l'inception de la relation; l'application est prospective et non rétrospective.",
    "La documentation doit identifier la créance couverte, la composante change couverte, l'instrument de couverture, le ratio de couverture et la méthode d'appréciation de l'efficacité.",
    "Le fait pattern à respecter est celui d'une créance déjà reconnue en consolidation; il ne faut pas reformuler l'analyse comme une couverture d'un dividende avant comptabilisation."
  ]
}
