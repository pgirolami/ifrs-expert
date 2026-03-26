{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré de sorte qu'il donne naissance à une créance et à une dette intragroupe constituant un élément monétaire comptabilisé dans l'analyse de couverture consolidée."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidé, un dividende intragroupe est en principe exclu comme élément couvert, sauf si la créance/dette correspond à un élément monétaire intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Sous cette réserve, et avec une désignation/documentation conforme à IFRS 9 6.4.1, une relation de couverture peut être documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende déjà comptabilisée est un actif reconnu, ce qui cadre avec une couverture de juste valeur d'un risque particulier.\nMais, en comptes consolidés, les éléments intragroupe sont en principe exclus; il faut donc que l'exception visant le risque de change d'un élément monétaire intragroupe s'applique.\nLa désignation n'est possible que si les écarts de change sur cette créance/dette ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.",
        "Les écarts de change afférents ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture est formellement désignée et documentée dès l'origine.",
        "Les critères d'efficacité de la couverture, y compris le ratio de couverture, sont respectés."
      ],
      "practical_implication_fr": "La documentation doit viser la créance de dividende reconnue, le risque de change couvert et la démonstration que ce risque subsiste au niveau consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation of the hedging relationship"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss."
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi qu'un actif reconnu soit l'élément couvert d'une couverture de flux si la variabilité de ses flux liée au change peut affecter le résultat.\nPour un dividende intragroupe, cette voie n'est recevable en consolidé que si la créance monétaire génère un risque de change qui subsiste à la consolidation.\nLa relation doit en outre être formellement désignée et satisfaire aux critères d'efficacité; à défaut, ce traitement ne s'applique pas ici.",
      "conditions_fr": [
        "La créance de dividende reconnue expose le groupe à une variabilité de flux en monnaie fonctionnelle du fait du change.",
        "Le risque de change sur l'élément monétaire intragroupe affecte le résultat consolidé et n'est pas totalement éliminé en consolidation.",
        "La relation de couverture est désignée et documentée dès l'origine avec le risque couvert clairement identifié.",
        "Les tests d'efficacité et le ratio de couverture sont cohérents avec la gestion du risque."
      ],
      "practical_implication_fr": "La documentation doit démontrer que la variabilité des encaissements liée au change sur la créance de dividende affecte bien le résultat consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability ... and could affect profit or loss."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d'abord si la créance de dividende est bien un élément monétaire en devise entre entités à monnaies fonctionnelles différentes; sinon l'exception IFRS 9 6.3.6 ne joue pas.",
    "La question clé en consolidé est l'effet sur le résultat consolidé: si les écarts de change sont totalement éliminés, la désignation n'est pas recevable.",
    "Une documentation initiale complète est indispensable: instrument de couverture, élément couvert, risque de change, ratio de couverture et méthode d'appréciation de l'efficacité.",
    "Parmi les deux traitements retenus, la couverture de juste valeur est la lecture la plus directe pour une créance de dividende déjà comptabilisée; la couverture de flux reste possible si la variabilité de flux liée au change est correctement documentée."
  ]
}
