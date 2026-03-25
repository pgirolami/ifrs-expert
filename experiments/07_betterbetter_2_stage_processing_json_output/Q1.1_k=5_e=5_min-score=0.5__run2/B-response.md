{
  "assumptions_fr": [
    "La créance de dividende est un élément monétaire intragroupe libellé en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes ; les écarts de change correspondants ne sont donc pas totalement éliminés en consolidation.",
    "Toute relation de couverture envisagée ne désigne que la composante risque de change et satisfait aux exigences formelles de désignation, de documentation et d’efficacité."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans cette situation, deux voies réelles existent en consolidation pour documenter la partie change de la créance déjà comptabilisée : la couverture de juste valeur et la couverture de flux de trésorerie, grâce à l’exception visant les éléments monétaires intragroupe. La couverture d’investissement net ne répond pas au fait décrit, car elle vise les net assets d’une activité étrangère et non la créance de dividende elle-même."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "La créance de dividende est déjà comptabilisée ; cela correspond au champ d’une couverture de juste valeur portant sur un actif reconnu. Sous l’hypothèse qu’il s’agit d’un élément monétaire intragroupe en devise dont l’effet de change n’est pas totalement éliminé en consolidation, IFRS 9 autorise la désignation de ce risque de change comme élément couvert.",
      "conditions_fr": [],
      "practical_implication_fr": "Vous documentez en consolidation la composante change de la créance comme élément couvert d’une couverture de juste valeur.",
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
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "La question vise la partie change d’une créance déjà reconnue ; IFRS 9 permet aussi une couverture de flux de trésorerie sur la variabilité des cash flows d’un actif reconnu. Avec l’hypothèse d’un élément monétaire intragroupe en devise dont le risque de change affecte encore le résultat consolidé, cette voie reste ouverte en consolidation sur la composante change.",
      "conditions_fr": [],
      "practical_implication_fr": "Vous documentez la variabilité en monnaie fonctionnelle des encaissements futurs liés à la créance, attribuable au change.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Cette documentation répond à un autre objet couvert : un investissement net dans une activité étrangère, c’est-à-dire un montant de net assets. Ici, les faits et les hypothèses portent sur une créance de dividende intragroupe déjà comptabilisée ; recadrer l’exposition au niveau de l’activité étrangère changerait le fait générateur et ne couvrirait pas la créance elle-même.",
      "conditions_fr": [],
      "practical_implication_fr": "Dans cette situation, une documentation de net investment hedge ne sécurise pas la partie change de la créance de dividende déjà constatée.",
      "references": [
        {
          "section": "8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, l’ouverture du hedge accounting repose ici sur l’exception visant le risque de change d’un élément monétaire intragroupe non totalement éliminé.",
    "La documentation doit être établie à l’inception de chaque relation de couverture et identifier explicitement la composante change comme risque couvert.",
    "Le fait que la créance soit déjà comptabilisée n’empêche pas une désignation en couverture de juste valeur ou de flux de trésorerie, car IFRS 9 vise expressément les actifs reconnus.",
    "Une documentation de net investment hedge exigerait un objet couvert différent, fondé sur les net assets d’une activité étrangère ; elle ne remplace pas la couverture de la créance de dividende."
  ]
}
