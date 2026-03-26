{
  "assumptions_fr": [
    "La créance de dividende intragroupe est libellée dans une devise différente de la devise fonctionnelle pertinente, de sorte qu'une exposition de change existe dans les comptes consolidés.",
    "La réponse est limitée aux traitements comptables identifiables à partir des extraits fournis d'IFRS 9 et d'IFRIC 16."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, la partie change peut être documentée en couverture au niveau consolidé, mais seulement via une relation de couverture formalisée sur cette exposition. Au vu des extraits fournis, les voies plausibles sont la couverture de juste valeur ou de flux de trésorerie; à défaut, la différence de change reste en résultat, et la couverture d'investissement net ne correspond pas aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fx_profit_or_loss",
      "label_fr": "Réévaluation de change en résultat",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende a déjà été comptabilisé en créance et, selon les hypothèses retenues, cette créance est un actif monétaire en devise dans les comptes consolidés. En l'absence d'une relation de couverture qualifiée, l'extrait IFRS 9 renvoie au traitement de base : les écarts de change sont comptabilisés en résultat.",
      "conditions_fr": [],
      "practical_implication_fr": "Si aucune documentation de couverture n'est retenue ou qualifiée, la composante change du dividende passe en résultat.",
      "references": [
        {
          "section": "B5.7.2",
          "excerpt": "IAS 21 requires any foreign exchange gains and losses on monetary assets and monetary liabilities to be recognised in profit or loss."
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La situation porte sur la partie change d'une créance de dividende déjà comptabilisée dans les comptes consolidés. Les extraits fournis permettent qu'un actif financier devienne un élément couvert relevant de la section 6; une documentation de couverture de juste valeur est donc envisageable si elle vise explicitement cette créance reconnue et son risque de change.",
      "conditions_fr": [
        "La couverture est documentée au niveau consolidé sur la créance de dividende déjà comptabilisée.",
        "Un instrument de couverture distinct couvre cette exposition de change."
      ],
      "practical_implication_fr": "Voie possible si le groupe formalise la couverture de la variation liée au change sur la créance reconnue.",
      "references": [
        {
          "section": "5.7.3",
          "excerpt": "hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        },
        {
          "section": "6.1.1",
          "excerpt": "The objective of hedge accounting is to represent, in the financial statements, the effect of an entity’s risk management activities"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende à encaisser en devise expose le groupe à une variabilité des flux de règlement en monnaie fonctionnelle dans les comptes consolidés. Les extraits identifient la cash flow hedge comme issue distincte en matière de risque de change; cette voie est donc possible si la documentation cible les flux d'encaissement de ce dividende.",
      "conditions_fr": [
        "La documentation vise les flux d'encaissement en devise du dividende à recevoir.",
        "L'exposition de change subsiste dans les comptes consolidés jusqu'au règlement."
      ],
      "practical_implication_fr": "Voie possible si le risque couvert est décrit comme la variabilité de change des flux d'encaissement du dividende.",
      "references": [
        {
          "section": "B5.7.2",
          "excerpt": "An exception is a monetary item that is designated as a hedging instrument in a cash flow hedge"
        },
        {
          "section": "5.7.3",
          "excerpt": "hedged items in a hedging relationship shall be recognised in accordance with paragraphs 6.5.8–6.5.14"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 vise uniquement le risque de change d'un investissement net dans une activité étrangère et d'un montant de net assets dans les états financiers consolidés. Ici, les faits décrivent un dividende intragroupe comptabilisé en créance, pas un investissement net dans une activité étrangère; sur ces faits, cette documentation ne correspond donc pas.",
      "conditions_fr": [],
      "practical_implication_fr": "À écarter pour ce dividende: cette mécanique vise les net investments, pas une créance de dividende déclarée.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Sans relation de couverture qualifiée, la différence de change sur la créance de dividende est comptabilisée en résultat.",
    "La documentation pertinente doit être portée dans les comptes consolidés sur l'exposition de change de la créance de dividende.",
    "Au vu des extraits fournis, le choix praticable se fait entre une logique de juste valeur et une logique de flux de trésorerie pour cette créance déjà reconnue.",
    "La couverture d'investissement net doit être exclue tant que l'exposition visée reste celle d'un dividende intragroupe en créance et non celle d'un investissement net dans une activité étrangère."
  ]
}
