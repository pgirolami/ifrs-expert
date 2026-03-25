{
  "assumptions_fr": [
    "La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des parties.",
    "La question vise la comptabilité de couverture selon IFRS 9 dans les comptes consolidés, et non dans les comptes individuels ou séparés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Sur les faits donnés, la seule voie potentiellement applicable à la créance déjà comptabilisée est une couverture de juste valeur du risque de change d’un élément monétaire intragroupe. Elle n’est possible en consolidation que si l’exception IFRS 9 pour les éléments monétaires intragroupe s’applique et si la documentation d’inception et l’efficacité sont remplies."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le fait générateur décrit est une créance intragroupe déjà comptabilisée, donc un actif reconnu, ce qui correspond au bon stade pour une couverture de juste valeur et non à une transaction future. En consolidation, l’approche n’est recevable, selon les hypothèses, que si le risque de change de cet élément monétaire intragroupe génère des écarts non totalement éliminés et si la relation est formellement désignée et documentée dès l’inception de la couverture.",
      "conditions_fr": [
        "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur la créance ne soient pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée à l’inception, avec identification du risque couvert, de l’instrument de couverture et de la méthode d’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "Il faut documenter une fair value hedge ciblée sur le seul risque de change de la créance de dividende déjà reconnue.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
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
      "label_fr": "Couverture de flux de trésorerie d’un dividende prévu",
      "applicability": "non",
      "reasoning_fr": "Cette voie vise un dividende intragroupe encore prévu et hautement probable, alors que la question porte sur un dividende déjà comptabilisé en créance. L’appliquer ici supposerait de revenir à un stade antérieur de la transaction, ce qui contredit les faits et le timing donnés.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette documentation n’est pas disponible pour la créance déjà reconnue ; elle aurait dû être mise en place avant la comptabilisation.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "If a hedged item is a forecast transaction ... that transaction must be highly probable."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... or a highly probable forecast transaction"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Le modèle IFRIC 16 traite du risque de change sur un investissement net dans les actifs nets d’une activité étrangère, pas d’une créance de dividende intragroupe déjà constatée. Les hypothèses et le fait décrit portent sur un poste monétaire reconnu distinct de l’investissement net ; cette approche exige donc un autre objet couvert.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle est distinct et ne permet pas de documenter en consolidation la partie change de la créance de dividende elle-même.",
      "references": [
        {
          "section": "7",
          "excerpt": "This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "hedge_ineligibility",
      "label_fr": "Absence de comptabilité de couverture en consolidation",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, la règle générale exclut les transactions intragroupe comme éléments couverts. Pour la créance de dividende déjà comptabilisée, cette issue s’impose si l’exception relative au risque de change d’un élément monétaire intragroupe n’est pas satisfaite, ou si les conditions de désignation, de documentation et d’efficacité ne sont pas remplies.",
      "conditions_fr": [
        "Les écarts de change sur la créance intragroupe sont totalement éliminés en consolidation, de sorte que l’exception de l’élément monétaire intragroupe ne s’applique pas.",
        "Les critères de désignation, de documentation et d’efficacité prévus par IFRS 9.6.4.1 ne sont pas satisfaits."
      ],
      "practical_implication_fr": "À défaut d’éligibilité ou de documentation conforme, les écarts de change restent traités sans hedge accounting en consolidation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify"
        },
        {
          "section": "6.4.1",
          "excerpt": "A hedging relationship qualifies for hedge accounting only if all of the following criteria are met"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif est le timing : le dividende est déjà en créance, donc la piste \"transaction prévue\" ne peut plus être retenue.",
    "En consolidation, il faut d’abord établir si la créance intragroupe crée encore un risque de change non totalement éliminé, ce qui dépend notamment des monnaies fonctionnelles des entités concernées.",
    "Si la couverture de juste valeur est retenue, la documentation doit être mise en place à l’inception de la relation de couverture, avec identification précise du risque de change couvert et de la méthode d’efficacité.",
    "Si ces conditions ne sont pas réunies, la conclusion opérationnelle est l’absence de comptabilité de couverture en consolidation sur cette créance."
  ]
}
