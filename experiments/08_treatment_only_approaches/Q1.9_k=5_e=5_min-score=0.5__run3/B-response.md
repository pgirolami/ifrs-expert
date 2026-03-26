{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et comptabilisé en créance/dette intragroupe ; il s'agit donc d'un élément monétaire reconnu.",
    "La créance est libellée dans une devise qui génère des écarts de change non totalement éliminés en consolidation, car les entités concernées ont des monnaies fonctionnelles différentes.",
    "La désignation envisagée vise uniquement la composante de risque de change de cet élément reconnu."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation, l'exception d'IFRS 9 pour le risque de change d'un élément monétaire intragroupe en comptes consolidés peut s'appliquer. La désignation reste toutefois conditionnée à l'identification du seul risque de change, à sa mesurabilité fiable et au respect des critères formels de hedge accounting."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est un actif monétaire reconnu ; la règle générale d'exclusion des éléments intragroupe en consolidation est levée par l'exception visant le risque de change d'un élément monétaire intragroupe.\nLa composante de change de cette créance peut donc être désignée en couverture de juste valeur si elle est isolée comme risque spécifique, mesurable de façon fiable, et si la relation de couverture est formellement documentée et répond aux tests d'efficacité.",
      "conditions_fr": [
        "La créance de dividende est bien un élément monétaire intragroupe reconnu.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
        "La composante de risque de change est séparément identifiable et mesurable de façon fiable.",
        "La relation de couverture est désignée et documentée dès l'origine et respecte les critères de 6.4.1."
      ],
      "practical_implication_fr": "En consolidation, la créance de dividende peut être retenue comme élément couvert pour son seul risque de change dans un modèle de couverture de juste valeur, sous documentation complète.",
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
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le même élément monétaire reconnu peut aussi être analysé sous l'angle de la variabilité des flux en monnaie fonctionnelle causée par le change ; IFRS 9 admet ce modèle pour un actif ou passif reconnu.\nComme les écarts de change de la créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé selon les hypothèses, la désignation en cash flow hedge est possible, sous réserve des mêmes exigences de désignation, documentation et efficacité.",
      "conditions_fr": [
        "La couverture vise la variabilité des flux en monnaie fonctionnelle liée au risque de change de la créance.",
        "Le risque de change de cette créance affecte le résultat consolidé et n'est pas totalement éliminé en consolidation.",
        "La composante de risque de change est séparément identifiable et mesurable de façon fiable.",
        "La relation de couverture satisfait aux critères de qualification de 6.4.1."
      ],
      "practical_implication_fr": "Le modèle de couverture de flux de trésorerie est également envisageable si l'objectif est de couvrir la variabilité liée au change des flux attachés à la créance de dividende.",
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
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La conclusion dépend ici de l'exception de 6.3.6 : sans écarts de change non totalement éliminés en consolidation, la réponse basculerait vers non.",
    "Il faut documenter dès l'origine l'instrument de couverture, l'élément couvert, la nature du risque de change couvert et la méthode d'évaluation de l'efficacité.",
    "La désignation doit porter sur la seule composante de risque de change de la créance de dividende, qui doit être séparément identifiable et mesurable de façon fiable.",
    "IFRIC 16 ne doit pas être appliqué par analogie : il est limité aux couvertures d'un investissement net dans une activité à l'étranger."
  ]
}
