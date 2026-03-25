{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance et une dette intragroupe comptabilisées.",
    "La créance et la dette existent entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation selon IAS 21.",
    "Toute désignation de couverture satisferait aussi aux exigences formelles de désignation, de documentation et d'efficacité d'IFRS 9 paragraphe 6.4.1."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans cette situation, la règle générale d'exclusion des éléments intragroupe en consolidation est écartée par l'exception d'IFRS 9 6.3.6 pour un poste monétaire intragroupe exposé au change.\nSous les hypothèses retenues, l'exposition de change sur la créance/dette de dividende enregistrée peut donc être couverte et documentée en hedge accounting dans les comptes consolidés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà donné naissance à une créance/dette comptabilisée, donc à un actif/passif reconnu.\nSous les hypothèses retenues, l'exception de 6.3.6 permet de désigner ce poste monétaire intragroupe en consolidation, et le modèle de juste valeur vise précisément un actif ou passif comptabilisé exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [
        "La créance ou la dette de dividende est déjà comptabilisée comme poste monétaire intragroupe",
        "Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation",
        "La relation de couverture est formellement désignée, documentée et efficace au sens d'IFRS 9 6.4.1"
      ],
      "practical_implication_fr": "La documentation peut viser le risque de change sur la réévaluation en consolidation du poste monétaire de dividende déjà enregistré.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
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
      "applicability": "oui",
      "reasoning_fr": "Dans cette situation, le règlement futur de la créance/dette de dividende en devise crée une variabilité des flux en monnaie fonctionnelle.\nComme 6.3.6 autorise la désignation du poste monétaire intragroupe en consolidation et que les hypothèses couvrent 6.4.1, un cash flow hedge est aussi possible sur ce risque de change.",
      "conditions_fr": [
        "Le risque désigné porte sur la variabilité en monnaie fonctionnelle des flux de règlement du dividende intragroupe",
        "Les écarts de change sur le poste monétaire intragroupe affectent le résultat consolidé car ils ne sont pas totalement éliminés",
        "La relation de couverture est formellement désignée, documentée et efficace au sens d'IFRS 9 6.4.1"
      ],
      "practical_implication_fr": "La documentation doit relier l'instrument de couverture à la variabilité de change des flux de règlement du dividende intragroupe comptabilisé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de départ pratique est la date de comptabilisation de la créance/dette de dividende; la conclusion ci-dessus vise cette situation postérieure à l'enregistrement.",
    "Le dossier de consolidation doit démontrer que les entités concernées ont des monnaies fonctionnelles différentes et que les écarts de change sur le poste monétaire ne sont pas totalement éliminés.",
    "Il faut choisir et documenter un modèle de couverture cohérent avec le risque désigné: juste valeur pour la réévaluation du poste comptabilisé, ou flux de trésorerie pour la variabilité du règlement."
  ]
}
