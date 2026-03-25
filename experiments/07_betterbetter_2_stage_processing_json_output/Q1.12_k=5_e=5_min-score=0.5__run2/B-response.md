{
  "assumptions_fr": [
    "La créance/dette de dividende intragroupe déjà comptabilisée est un poste monétaire intragroupe libellé dans une devise créant une exposition de change entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, au niveau consolidé, sous les hypothèses données, car l’exception IFRS 9 sur les postes monétaires intragroupe peut rendre la créance de dividende éligible comme élément couvert. La qualification formelle dépend ensuite du modèle retenu et du respect de la désignation, de la documentation et des critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du poste monétaire intragroupe reconnu",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà été comptabilisé en créance à recevoir : on est donc bien au stade d’un actif reconnu, ce qui correspond au champ d’une fair value hedge. Sous les hypothèses retenues, l’exception d’IFRS 9 pour le risque de change d’un poste monétaire intragroupe au niveau consolidé rend cette voie possible, à condition de formaliser la relation de couverture à son inception et de satisfaire aux critères d’efficacité.",
      "conditions_fr": [
        "Mettre en place un instrument de couverture éligible.",
        "Désigner formellement et documenter la relation de couverture dès son inception.",
        "Démontrer la relation économique, l’absence de domination du risque de crédit et un hedge ratio cohérent."
      ],
      "practical_implication_fr": "Il faut documenter la créance de dividende déjà reconnue comme élément couvert et suivre au niveau consolidé la compensation de sa variation liée au change avec l’instrument de couverture.",
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
      "label_fr": "Couverture de flux de trésorerie du poste monétaire intragroupe reconnu",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La question porte sur une créance de dividende intragroupe déjà reconnue ; cette approche n’est donc recevable que comme couverture de la variabilité des flux de règlement en monnaie fonctionnelle du poste reconnu, et non comme couverture d’un dividende futur. Sous les hypothèses données, l’exception IFRS 9 sur le poste monétaire intragroupe permet cette qualification au niveau consolidé si la variabilité de change affectant le résultat consolidé est la composante couverte dûment documentée et efficace.",
      "conditions_fr": [
        "Mettre en place un instrument de couverture éligible.",
        "Désigner formellement et documenter, dès l’inception, la variabilité des flux de règlement en monnaie fonctionnelle comme risque couvert.",
        "Démontrer la relation économique, l’absence de domination du risque de crédit et un hedge ratio cohérent."
      ],
      "practical_implication_fr": "Il faut cadrer la documentation sur les flux de règlement du dividende déjà comptabilisé et suivre spécifiquement l’exposition de change qui affecte le résultat consolidé.",
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
    "L’analyse doit rester au stade actuel : une créance de dividende intragroupe déjà comptabilisée, et non une transaction intragroupe future.",
    "Au niveau consolidé, le point clé est l’exception IFRS 9 visant le risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés en consolidation.",
    "Quel que soit le modèle retenu, la désignation et la documentation doivent être établies à l’inception de la relation de couverture, avec tests d’efficacité à l’appui.",
    "Le choix entre fair value hedge et cash flow hedge dépend de l’exposition précisément documentée sur la créance intragroupe déjà reconnue."
  ]
}
