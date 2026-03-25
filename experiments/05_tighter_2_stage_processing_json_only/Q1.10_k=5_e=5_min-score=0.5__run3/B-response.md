{
  "assumptions": [
    "La question vise des états financiers consolidés IFRS ordinaires d'une entité non qualifiée d'entité d'investissement.",
    "Le dividende intragroupe reste une créance/dette non réglée et peut donc être apprécié comme un poste monétaire intragroupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe est en principe exclu comme élément couvert. Toutefois, IFRS 9 admet une exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation, sous réserve d'une désignation formelle et du respect des critères d'efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d'un poste monétaire intragroupe admissible",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 prévoit expressément qu'en consolidation le risque de change d'un poste monétaire intragroupe peut être un élément couvert. Donc, si le dividende à recevoir correspond à un tel poste et crée des écarts de change non totalement éliminés, la relation peut être documentée. Il faut en plus satisfaire aux exigences de documentation et d'efficacité de la relation de couverture.",
      "conditions_fr": [
        "Le dividende à recevoir / à payer constitue un poste monétaire intragroupe.",
        "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La relation est formellement désignée et documentée à l'origine et respecte les critères d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "La documentation doit être montée comme une couverture de risque de change sur poste monétaire intragroupe, avec preuve des écarts résiduels en consolidation.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "IFRS 9 6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation ... and the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "intragroup_item_exclusion",
      "label_fr": "Exclusion générale des éléments intragroupe",
      "applicability": "non",
      "reasoning_fr": "La règle générale d'IFRS 9 en consolidation limite les éléments couverts aux expositions envers des parties externes au groupe. Pris isolément, un dividende intragroupe ne répond donc pas à cette règle générale. Cette voie ne fonctionne pas sauf à entrer dans l'exception spécifique des postes monétaires intragroupe.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter la couverture en se fondant seulement sur l'existence d'un flux intragroupe en consolidation.",
      "references": [
        {
          "section": "IFRS 9 6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "forecast_transaction_hedge",
      "label_fr": "Couverture d'une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Cette exception vise une transaction intragroupe future hautement probable dont le risque de change affectera le résultat consolidé. Or la question porte sur un dividende déjà comptabilisé à recevoir, donc sur un poste reconnu et non sur une transaction future. Ce cadre n'est donc pas le bon fondement pour documenter la relation.",
      "conditions_fr": [
        "La transaction doit être hautement probable et non déjà comptabilisée.",
        "Elle doit être libellée dans une monnaie autre que la monnaie fonctionnelle de l'entité qui y entre.",
        "Le risque de change doit affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Ne pas utiliser la mécanique de couverture de transaction prévue si le dividende est déjà enregistré en créance.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "IFRS 9 B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite uniquement des couvertures du risque de change sur un investissement net dans une activité étrangère. Il précise que ce dispositif ne doit pas être appliqué par analogie à d'autres relations de couverture. Un dividende intragroupe à recevoir n'est pas un montant de net assets d'une activité étrangère.",
      "conditions_fr": [
        "L'élément couvert devrait être un montant d'actifs nets d'une activité étrangère.",
        "La relation devrait satisfaire aux exigences de désignation, de documentation et d'efficacité propres à une couverture d'investissement net."
      ],
      "practical_implication_fr": "Écarter le modèle de couverture d'investissement net pour une créance de dividende intragroupe.",
      "references": [
        {
          "section": "IFRIC 16 7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "IFRIC 16 8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier à la date de désignation que le dividende à recevoir / à payer demeure un poste monétaire intragroupe non réglé.",
    "Démontrer que les écarts de change liés à ce poste ne sont pas totalement éliminés en consolidation du fait de monnaies fonctionnelles différentes.",
    "Constituer dès l'origine la documentation IFRS 9: instrument de couverture, élément couvert, risque couvert, ratio de couverture et sources d'inefficacité.",
    "Écarter la voie des transactions intragroupe prévues si le dividende est déjà comptabilisé, ainsi que la voie des couvertures d'investissement net."
  ]
}
