{
  "assumptions_fr": [
    "La créance de dividende intragroupe déjà comptabilisée est un élément monétaire intragroupe libellé dans une devise générant une exposition au risque de change.",
    "La créance existe entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, l’exception IFRS 9 pour le risque de change d’un élément monétaire intragroupe permet en principe de désigner la créance de dividende comme élément couvert. La désignation doit toutefois être prospective et satisfaire aux exigences de composante de risque, de documentation et d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, la créance de dividende déjà comptabilisée est un actif reconnu et un élément monétaire intragroupe. Sous les hypothèses retenues, l’exception visant le risque de change des éléments monétaires intragroupe permet que ce risque soit un élément couvert en consolidation. Une couverture de juste valeur est donc recevable pour cette créance reconnue, à compter de la désignation, si la composante de change est séparément identifiable et mesurable et si les critères IFRS 9 de documentation et d’efficacité sont respectés.",
      "conditions_fr": [
        "La composante de risque de change couverte est séparément identifiable et de manière fiable mesurable.",
        "La relation de couverture est formellement désignée et documentée au démarrage de la couverture, sans effet rétroactif sur les écarts déjà constatés.",
        "Un instrument de couverture éligible est désigné contre cette créance.",
        "La relation satisfait aux tests d’efficacité, y compris la relation économique, la non-prédominance du risque de crédit et un hedge ratio cohérent."
      ],
      "practical_implication_fr": "Il faut documenter la créance de dividende comme élément couvert de juste valeur, désigner l’instrument et suivre l’inefficacité à partir de la date de désignation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "An entity may designate an item in its entirety or a component of an item as the hedged item."
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, l’élément visé est la créance de dividende déjà reconnue, et non une transaction future encore non comptabilisée. IFRS 9 admet une couverture de flux de trésorerie d’un risque particulier associé à un actif reconnu; sous les mêmes hypothèses d’exposition de change intragroupe non totalement éliminée, la composante FX peut donc être intégrée dans une relation documentée pour la variabilité des encaissements futurs jusqu’au règlement. Cette voie n’est applicable que si la documentation vise bien cette variabilité de flux et si les critères de composante de risque, de désignation prospective et d’efficacité sont remplis.",
      "conditions_fr": [
        "La documentation identifie que le risque couvert porte sur la variabilité de change des flux futurs de règlement de la créance reconnue.",
        "La composante de risque de change est séparément identifiable et de manière fiable mesurable.",
        "La désignation est faite prospectivement au démarrage de la relation de couverture.",
        "Un instrument de couverture éligible est désigné et la relation respecte les critères IFRS 9 d’efficacité et de hedge ratio."
      ],
      "practical_implication_fr": "Il faut documenter que la couverture vise la variabilité de change des encaissements futurs de la créance jusqu’à son règlement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component of the financial or the non-financial item, and the changes in the cash flows or the fair value of the item attributable to changes in that risk component must be reliably measurable"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La règle générale d’exclusion des éléments intragroupe en consolidation est ici tempérée par l’exception relative au risque de change des éléments monétaires intragroupe, selon les hypothèses retenues.",
    "Comme la créance de dividende est déjà comptabilisée, la désignation de couverture ne peut jouer que prospectivement à compter de l’origine de la relation de couverture.",
    "La documentation doit identifier la créance, la composante de change couverte, l’instrument de couverture, le hedge ratio et la méthode d’évaluation de l’efficacité.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit correspondre à l’exposition exactement documentée sur la créance reconnue."
  ]
}
