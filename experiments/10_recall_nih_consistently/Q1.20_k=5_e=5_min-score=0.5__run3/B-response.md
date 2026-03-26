{
  "assumptions_fr": [
    "La question porte sur l’application d’IFRS 9 dans les états financiers consolidés.",
    "L’exposition visée est un risque de change attaché à une créance ou transaction intragroupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance de dividende est un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, une documentation de hedge accounting peut viser ce risque de change sur la créance; en revanche, la couverture d’un investissement net n’est pas adaptée aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe. Une créance de dividende déjà comptabilisée et sensible au change peut donc être désignée si les écarts de change correspondants ne sont pas entièrement éliminés et affectent le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende constitue un élément monétaire intragroupe.",
        "Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "Documenter la créance comme élément couvert et cibler uniquement le risque de change qui subsiste au niveau consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Cette voie n’est pertinente ici que si l’exposition documentée est la variabilité du règlement futur de la créance en monnaie fonctionnelle, et non un simple reclassement intragroupe. Elle reste soumise à la même exception: le risque de change sur cet élément monétaire intragroupe doit survivre à la consolidation et affecter le résultat consolidé.",
      "conditions_fr": [
        "L’exposition couverte est la variabilité du règlement futur de la créance en monnaie fonctionnelle.",
        "Le risque de change sur la créance intragroupe affecte le résultat consolidé parce qu’il n’est pas totalement éliminé en consolidation."
      ],
      "practical_implication_fr": "N’utiliser cette voie que si la relation de couverture vise explicitement le règlement futur de la créance et sa variabilité de change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise le risque de change attaché à un montant de net assets d’une activité étrangère. Les faits décrits portent sur une créance de dividende intragroupe comptabilisée, pas sur un montant d’investissement net dans les actifs nets d’une opération étrangère.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette exposition comme une couverture d’investissement net sur la base des seuls faits fournis.",
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
    "Vérifier d’abord que la créance de dividende est bien un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.",
    "Confirmer que les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé.",
    "À l’inception, la documentation doit identifier l’instrument de couverture, la créance couverte, le risque de change couvert et la manière d’évaluer l’efficacité de la relation."
  ]
}
