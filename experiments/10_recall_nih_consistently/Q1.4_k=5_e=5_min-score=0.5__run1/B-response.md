{
  "assumptions_fr": [
    "La question vise les états financiers consolidés du groupe.",
    "La créance de dividende intragroupe crée une exposition au change entre entités du groupe ayant des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, mais uniquement en pratique via une couverture de juste valeur de la créance intragroupe reconnue comme élément monétaire. La documentation doit être mise en place à l'inception de la relation de couverture, donc de façon prospective à compter de la reconnaissance de la créance."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur d'un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà reconnue peut être traitée comme un élément monétaire intragroupe.\nIFRS 9 admet en consolidation la couverture du risque de change d'un tel élément lorsque les écarts de change ne sont pas totalement éliminés, ce qui est cohérent avec l'hypothèse de monnaies fonctionnelles différentes.\nLa documentation doit toutefois être établie à l'inception de la relation de couverture; elle ne peut donc viser que l'exposition postérieure à la désignation.",
      "conditions_fr": [
        "le risque de change sur la créance n'est pas totalement éliminé en consolidation",
        "la relation est désignée et documentée prospectivement à compter de la reconnaissance de la créance"
      ],
      "practical_implication_fr": "Documenter la couverture sur la créance reconnue et ses écarts de change futurs, sans effet rétroactif.",
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
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie d'une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "Cette approche ne correspond pas aux faits décrits, car la question porte sur un dividende intragroupe pour lequel une créance a déjà été comptabilisée.\nLe modèle de cash flow hedge vise une transaction future hautement probable, non un actif déjà reconnu.\nEn outre, l'exception intragroupe en consolidation vise des transactions futures dont le risque de change affectera le résultat consolidé, ce que le contexte fourni ne pose pas ici.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette relation comme une couverture de flux sur un dividende intragroupe déjà constaté en créance.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify"
        },
        {
          "section": "B6.3.5",
          "excerpt": "provided that the transaction is denominated in a currency other than the functional currency ... and that the foreign currency risk will affect consolidated profit or loss"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net dans une activité étrangère",
      "applicability": "non",
      "reasoning_fr": "La situation décrite concerne la composante change d'une créance de dividende intragroupe, pas le risque de change attaché à un investissement net dans une activité étrangère.\nIFRIC 16 limite explicitement son champ aux couvertures d'investissements nets et précise qu'il ne faut pas l'appliquer par analogie à d'autres types de couverture.\nCe modèle n'est donc pas applicable à ce cas précis.",
      "conditions_fr": [],
      "practical_implication_fr": "Écarter une documentation de type couverture d'investissement net pour cette créance de dividende.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, viser la créance de dividende reconnue comme élément monétaire intragroupe, et non le dividende comme transaction future.",
    "Mettre en place la documentation à l'inception de la relation de couverture; les écarts de change antérieurs à la désignation restent hors couverture.",
    "Vérifier que l'exposition de change subsiste en consolidation du fait de monnaies fonctionnelles différentes entre les entités concernées.",
    "Ne pas utiliser, pour ce cas, ni le modèle de cash flow hedge ni celui de couverture d'investissement net."
  ]
}
