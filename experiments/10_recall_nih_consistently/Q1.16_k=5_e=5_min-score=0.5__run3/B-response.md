{
  "assumptions_fr": [
    "On suppose que le solde de dividende intragroupe ou la transaction correspondante est libellé dans une devise différente de la monnaie fonctionnelle pertinente, ce qui crée une exposition au risque de change.",
    "On suppose que la question se limite à l’identification des modèles de comptabilité de couverture pertinents dans les états financiers consolidés au regard du contexte IFRS fourni."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous réserve que la créance de dividende soit un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Les modèles de couverture de juste valeur et, selon la désignation retenue, de flux de trésorerie peuvent être envisagés; la couverture d’un investissement net n’est pas adaptée à ce fait."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est déjà un actif comptabilisé. IFRS 9 admet, en consolidation, qu’un élément monétaire intragroupe exposé au change puisse être un élément couvert si les gains ou pertes de change ne sont pas totalement éliminés. Une documentation en couverture de juste valeur est donc possible pour cette créance en devise.",
      "conditions_fr": [
        "la créance de dividende constitue un élément monétaire intragroupe",
        "les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation doit viser le risque de change sur la valeur de la créance au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 prévoit aussi une couverture de flux de trésorerie pour un actif comptabilisé lorsque le risque couvert porte sur la variabilité des flux. Ici, la créance en devise peut faire varier le montant encaissé en monnaie fonctionnelle jusqu’au règlement. Cette approche n’est recevable que si l’exposition de change subsiste en consolidation sur cet élément intragroupe.",
      "conditions_fr": [
        "la créance de dividende en devise expose le groupe à une variabilité des flux d’encaissement en monnaie fonctionnelle jusqu’au règlement",
        "les écarts de change sur cet élément intragroupe affectent le résultat consolidé parce qu’ils ne sont pas totalement éliminés"
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la documentation doit viser les flux d’encaissement de la créance en devise jusqu’à son règlement.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "Cette approche vise le risque de change attaché à un investissement net dans une activité étrangère, c’est-à-dire à des actifs nets. Une créance de dividende intragroupe est un solde monétaire distinct et non un montant de net assets de l’activité étrangère. IFRIC 16 précise en outre que son champ ne doit pas être étendu par analogie à d’autres couvertures.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette exposition ne doit pas être documentée comme une couverture d’investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        },
        {
          "section": "12",
          "excerpt": "The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie au niveau consolidé dès l’origine de la relation de couverture.",
    "Le point décisif est de démontrer que la créance de dividende génère des écarts de change non totalement éliminés en consolidation, ce qui renvoie en pratique à des monnaies fonctionnelles différentes entre les entités.",
    "Il faut choisir un seul modèle cohérent pour cette exposition donnée: juste valeur ou flux de trésorerie, mais pas investissement net."
  ]
}
