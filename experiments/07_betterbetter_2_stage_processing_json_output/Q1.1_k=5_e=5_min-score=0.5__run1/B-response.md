{
  "assumptions_fr": [
    "La créance et la dette de dividende intragroupe sont des postes monétaires libellés en devise.",
    "Les écarts de change liés à ce poste monétaire intragroupe ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, deux voies de documentation existent en consolidation sur la composante change du dividende intragroupe comptabilisé en créance : fair value hedge et cash flow hedge. Elles ne sont recevables que prospectivement si l’exception IFRS 9 pour les postes monétaires intragroupe est satisfaite et si la désignation/documentation ainsi que les critères d’efficacité du paragraphe 6.4.1 sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change sur la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende intragroupe a déjà été comptabilisé en créance, donc le fait générateur d’un actif reconnu est bien présent pour un fair value hedge. En consolidation, sous les hypothèses retenues, l’exception IFRS 9 permet de désigner le risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat consolidé. La mise en œuvre reste toutefois prospective, avec documentation formelle à l’inception de la relation de couverture et respect des critères d’efficacité.",
      "conditions_fr": [
        "désigner et documenter dès l’inception de la relation de couverture la créance, l’instrument de couverture, le risque de change couvert et le ratio de couverture",
        "utiliser un instrument de couverture éligible et démontrer la relation économique requise",
        "établir que le risque de crédit ne domine pas et que le hedge ratio retenu est cohérent"
      ],
      "practical_implication_fr": "En consolidation, il faut suivre prospectivement la variation de change de la créance couverte et celle de l’instrument de couverture selon la logique de fair value hedge.",
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
      "label_fr": "Couverture de flux de trésorerie du risque de change sur la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le texte IFRS 9 admet un cash flow hedge sur un actif reconnu pour une variabilité de flux attribuable à un risque particulier. Sous les hypothèses données, la créance intragroupe en devise est un poste monétaire dont le risque de change peut être qualifié en consolidation parce que les écarts ne sont pas totalement éliminés et peuvent affecter le résultat consolidé. L’application suppose néanmoins une désignation/documentation prospective de la relation de couverture et le respect continu des tests d’efficacité.",
      "conditions_fr": [
        "documenter à l’inception de la relation la créance couverte, l’instrument de couverture, le risque de change et la manière d’apprécier l’efficacité",
        "démontrer que la variabilité de flux liée au change sur la créance est bien l’exposition couverte en consolidation",
        "respecter les critères d’éligibilité, de relation économique et de hedge ratio du paragraphe 6.4.1"
      ],
      "practical_implication_fr": "En consolidation, le dossier de couverture devra cibler la variabilité des flux liée au change jusqu’au règlement de la créance, avec suivi prospectif de l’efficacité.",
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
          "excerpt": "the documentation shall include identification of the hedging instrument, the hedged item, the nature of the risk being hedged"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La base IFRS en consolidation est l’exception relative au risque de change d’un poste monétaire intragroupe lorsque l’effet n’est pas totalement éliminé.",
    "La documentation doit être établie à l’inception de la relation de couverture ; elle ne sécurise pas rétroactivement des écarts de change déjà comptabilisés.",
    "Le dossier doit identifier précisément la créance de dividende, la composante change couverte, l’instrument de couverture, le ratio de couverture et la méthode d’appréciation de l’efficacité."
  ]
}
