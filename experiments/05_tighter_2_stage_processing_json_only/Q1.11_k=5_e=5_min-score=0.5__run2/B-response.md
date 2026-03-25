{
  "assumptions": [
    "Le dividende intragroupe déclaré a créé une créance/dette intragroupe déjà comptabilisée, donc un poste monétaire.",
    "La question vise des comptes consolidés ordinaires, sauf si l'exception propre aux entités d'investissement est pertinente."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d'un poste monétaire intragroupe si les écarts de change ne sont pas totalement éliminés à la consolidation. La relation doit aussi être formellement désignée, documentée et satisfaire aux critères d'efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "monetary_item_hedge",
      "label_fr": "Couverture d'un poste monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "C'est la voie pertinente pour une créance de dividende déjà enregistrée. IFRS 9 permet, par exception en consolidation, de désigner le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. La couverture n'est recevable que si la créance/dette est bien un poste monétaire entre entités à monnaies fonctionnelles différentes et si la documentation et l'efficacité IFRS 9 sont respectées.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe est un poste monétaire entre entités du groupe.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture respecte les exigences de désignation, de documentation et d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "La documentation doit viser la créance de dividende comme élément couvert de change et démontrer la non-élimination totale des écarts de change en consolidation.",
      "references": [
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "IFRS 9 6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "intragroup_item_exclusion",
      "label_fr": "Exclusion générale des éléments intragroupe",
      "applicability": "non",
      "reasoning_fr": "La règle générale en comptes consolidés est négative: seuls les éléments avec une partie externe au groupe peuvent être désignés comme éléments couverts. Pris isolément, un dividende intragroupe ne serait donc pas admissible. Cette approche est toutefois supplantée ici si l'exception spécifique des postes monétaires intragroupe de change est satisfaite.",
      "conditions_fr": [
        "L'interdiction générale ne cède qu'en présence d'une exception spécifique d'IFRS 9.",
        "Une exception distincte existe pour les entités d'investissement concernant des transactions avec des filiales mesurées à la juste valeur par résultat."
      ],
      "practical_implication_fr": "Par défaut, un élément intragroupe est exclu; il faut donc fonder le dossier sur l'exception adéquate et non sur la règle générale.",
      "references": [
        {
          "section": "IFRS 9 6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture d'une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise une transaction encore future et hautement probable, pas une créance déjà comptabilisée. Une fois le dividende déclaré et la créance enregistrée, le sujet devient un poste monétaire existant. La base technique n'est donc plus la couverture d'un flux futur intragroupe mais, le cas échéant, l'exception des postes monétaires intragroupe.",
      "conditions_fr": [
        "La transaction doit être hautement probable.",
        "Elle doit être libellée dans une monnaie autre que la monnaie fonctionnelle de l'entité qui y entre.",
        "Le risque de change doit affecter le résultat consolidé."
      ],
      "practical_implication_fr": "Ne pas documenter le cas comme une cash flow hedge d'une transaction prévue si la créance de dividende est déjà reconnue.",
      "references": [
        {
          "section": "IFRS 9 6.3.3",
          "excerpt": "If a hedged item is a forecast transaction (or a component thereof), that transaction must be highly probable."
        },
        {
          "section": "IFRS 9 B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item."
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 traite d'un autre modèle: la couverture du risque de change sur les actifs nets d'une activité étrangère. Une créance intragroupe de dividende déjà comptabilisée n'est pas un montant de net assets de l'activité étrangère. Cette approche n'est donc pas la bonne qualification pour le cas posé.",
      "conditions_fr": [
        "L'élément couvert est un montant d'actifs nets d'une activité étrangère.",
        "Le risque couvert est celui entre la monnaie fonctionnelle de l'activité étrangère et celle d'une entité mère.",
        "La même exposition d'investissement net ne peut qualifier qu'une seule fois dans les comptes consolidés de la mère ultime."
      ],
      "practical_implication_fr": "Il faut distinguer strictement la créance de dividende intragroupe d'une net investment hedge, qui obéit à une logique et à une documentation différentes.",
      "references": [
        {
          "section": "IFRIC 16 10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        },
        {
          "section": "IFRIC 16 11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Qualifier d'abord la créance de dividende comme poste monétaire intragroupe; si ce n'est pas le cas, la conclusion devient négative.",
    "Vérifier que les sociétés concernées ont des monnaies fonctionnelles différentes et que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Formaliser dès l'origine la désignation, l'objectif de gestion du risque, l'élément couvert, l'instrument de couverture et la méthode d'appréciation de l'efficacité.",
    "Ne pas utiliser la voie de la transaction intragroupe prévue si la créance est déjà enregistrée; cette exception joue avant comptabilisation du poste.",
    "Ne pas confondre ce cas avec une couverture d'investissement net, qui porte sur les actifs nets d'une activité étrangère et suit IFRIC 16."
  ]
}
