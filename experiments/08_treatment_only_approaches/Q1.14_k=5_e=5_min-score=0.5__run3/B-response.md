{
  "assumptions_fr": [
    "La question est appréciée dans les états financiers consolidés du groupe.",
    "Le dividende intragroupe a déjà créé une créance et une dette intragroupe comptabilisées.",
    "Cette créance/dette est libellée de telle sorte qu'elle génère des écarts de change non totalement éliminés en consolidation, au sens du paragraphe 6.3.6 d'IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, l'exception d'IFRS 9 pour le risque de change d'un poste monétaire intragroupe permet de désigner cette exposition si les écarts de change ne sont pas totalement éliminés.\nLa couverture de juste valeur est la voie la plus directe ici; une couverture de flux de trésorerie reste envisageable si elle est formalisée sur cette base et si les critères de désignation et d'efficacité sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance/dette de dividende est déjà un poste monétaire intragroupe reconnu. Malgré la règle générale d'externalité, l'hypothèse posée reprend l'exception du paragraphe 6.3.6: le risque de change sur ce poste peut donc être désigné en consolidation.\nLe modèle de couverture de juste valeur est directement cohérent avec un actif ou passif reconnu exposé à un risque particulier affectant le résultat, sous réserve d'une documentation initiale et du respect des tests d'efficacité.",
      "conditions_fr": [
        "Le dividende intragroupe a créé un poste monétaire reconnu.",
        "Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.",
        "La relation est formellement désignée et documentée dès son inception.",
        "La relation économique, le ratio de couverture et l'absence de domination du risque de crédit sont démontrés."
      ],
      "practical_implication_fr": "Le groupe peut documenter une couverture du risque de change sur la créance/dette de dividende au niveau consolidé, si les critères IFRS 9 sont satisfaits.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette même situation, IFRS 9 permet aussi le modèle de couverture de flux de trésorerie pour un actif ou passif reconnu lorsque le risque couvert crée une variabilité de flux pouvant affecter le résultat. Sous l'hypothèse retenue, le poste monétaire intragroupe expose le groupe à un risque de change non éliminé en consolidation.\nCe traitement reste donc envisageable, mais seulement si l'entité documente la relation comme une couverture de variabilité de flux liés à ce poste et satisfait aux critères de désignation et d'efficacité.",
      "conditions_fr": [
        "Le risque de change sur ce poste entraîne une variabilité de flux affectant le résultat consolidé.",
        "Le poste couvert est fiable à mesurer.",
        "La désignation et la documentation sont établies dès l'inception de la relation.",
        "Les critères d'efficacité du paragraphe 6.4.1 sont respectés."
      ],
      "practical_implication_fr": "La documentation est possible, mais elle doit rattacher explicitement le risque de change à une variabilité de flux de trésorerie affectant le résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que la créance/dette de dividende est bien un poste monétaire entre entités ayant des monnaies fonctionnelles différentes et que les écarts de change affectent le résultat consolidé.",
    "La documentation doit être établie dès l'inception de la relation de couverture; une désignation tardive ou implicite n'est pas suffisante.",
    "Le choix du modèle doit rester cohérent avec l'objectif de gestion du risque; pour un poste déjà comptabilisé, la couverture de juste valeur est généralement la formulation la plus directe."
  ]
}
