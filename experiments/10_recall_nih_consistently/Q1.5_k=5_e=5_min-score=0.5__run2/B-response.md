{
  "assumptions_fr": [
    "La créance de dividende intragroupe est déjà comptabilisée et elle porte un risque de change.",
    "L’analyse est conduite au niveau des états financiers consolidés du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance de dividende intragroupe entre dans l’exception IFRS 9 applicable aux postes monétaires intragroupe, c’est-à-dire si le risque de change crée des gains ou pertes non totalement éliminés en consolidation. Dans ce cas, une relation de couverture formellement documentée est possible; la couverture d’investissement net ne correspond pas à ce fait."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende est ici un actif reconnu, ce qui correspond au champ d’une couverture de juste valeur. En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans ce cas précis, une relation de couverture documentée peut être mise en place au niveau consolidé.",
      "conditions_fr": [
        "La créance de dividende intragroupe génère des écarts de change non totalement éliminés en consolidation.",
        "La créance est entre des entités du groupe ayant des devises fonctionnelles différentes."
      ],
      "practical_implication_fr": "Le périmètre de la documentation doit viser la créance reconnue et le risque de change jusqu’au règlement.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "IFRS 9 admet aussi la couverture de la variabilité des flux de trésorerie d’un actif reconnu. Pour cette créance de dividende intragroupe, ce modèle n’est envisageable en consolidation que si l’exception relative au poste monétaire intragroupe est satisfaite, donc si le risque de change affecte encore le résultat consolidé. À défaut, la règle générale d’exclusion des transactions intragroupe en consolidation l’emporte.",
      "conditions_fr": [
        "Le risque de change sur la créance affecte encore le résultat consolidé jusqu’au règlement.",
        "La créance de dividende relève d’un poste monétaire intragroupe entre entités à devises fonctionnelles différentes."
      ],
      "practical_implication_fr": "La désignation doit cibler la variabilité en monnaie fonctionnelle des flux de règlement de la créance au niveau consolidé.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.5",
          "excerpt": "Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Les textes fournis réservent cette couverture au risque de change sur un investissement net dans une activité étrangère, c’est-à-dire sur un montant de net assets. Une créance intragroupe de dividende déjà comptabilisée n’est pas, dans la situation posée, un investissement net dans une activité étrangère. Ce traitement ne s’applique donc pas ici.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette créance ne doit pas être documentée comme élément couvert d’une couverture d’investissement net.",
      "references": [
        {
          "section": "2",
          "excerpt": "The item being hedged with respect to the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        },
        {
          "section": "14",
          "excerpt": "may be designated as a hedging instrument in a hedge of a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord si les entités concernées ont des devises fonctionnelles différentes et si les écarts de change sur la créance subsistent en consolidation.",
    "Au niveau consolidé, l’élément couvert doit être identifié comme la créance de dividende reconnue; un dividende futur non encore comptabilisé relèverait d’une autre analyse.",
    "La documentation doit être établie dès l’inception de la relation et préciser l’instrument de couverture, le risque de change couvert et l’évaluation de l’efficacité."
  ]
}
