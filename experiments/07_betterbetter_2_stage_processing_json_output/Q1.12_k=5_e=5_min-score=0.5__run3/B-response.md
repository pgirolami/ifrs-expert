{
  "assumptions_fr": [
    "La créance de dividende est un poste monétaire intragroupe libellé dans une devise différente de la monnaie fonctionnelle de l’entité concernée.",
    "Les écarts de change sur ce poste monétaire intragroupe ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Le groupe est en mesure de satisfaire, dès l’inception de la relation de couverture, aux exigences de désignation, de documentation et d’efficacité d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui, au niveau consolidé, si la créance de dividende est bien un poste monétaire intragroupe dont le risque de change affecte le résultat consolidé. La voie la plus directe est la couverture de juste valeur; la couverture de flux de trésorerie reste envisageable sous une désignation plus stricte."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "La question porte sur des dividendes intragroupe déjà comptabilisés en créance à recevoir : au stade décrit, l’élément couvert est donc un actif reconnu. Sous les hypothèses retenues, IFRS 9 admet en consolidation la couverture du risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés, et la couverture de juste valeur vise précisément les variations de valeur d’un actif reconnu pouvant affecter le résultat. La qualification formelle est donc possible dans ce schéma, avec la documentation à l’inception.",
      "conditions_fr": [
        "Formaliser dès l’inception la désignation de la créance, du risque de change couvert, de l’instrument de couverture et du hedge ratio.",
        "Suivre l’efficacité de la relation au niveau consolidé sur la base du risque de change qui affecte effectivement le résultat consolidé."
      ],
      "practical_implication_fr": "Le groupe peut documenter la relation comme une couverture de juste valeur de la créance intragroupe en devise et faire refléter symétriquement en résultat l’élément couvert et l’instrument de couverture selon IFRS 9.",
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
      "reasoning_fr": "Le fait pattern reste celui d’une créance de dividende déjà reconnue; il ne faut donc pas requalifier l’opération comme un simple dividende futur. IFRS 9 permet aussi une couverture de flux de trésorerie sur un actif reconnu, mais ici la qualification n’est tenable que si la désignation vise explicitement la variabilité, en monnaie de consolidation, des encaissements en devise liés à cette créance intragroupe, tout en restant dans l’exception de 6.3.6 et les exigences de 6.4.1.",
      "conditions_fr": [
        "La documentation doit désigner la variabilité des flux de trésorerie en devise de la créance reconnue, sans revenir à un stade antérieur de transaction seulement prévue.",
        "Le groupe doit démontrer que cette variabilité liée au change peut affecter le résultat consolidé et que la relation satisfait aux tests d’efficacité."
      ],
      "practical_implication_fr": "Cette voie est plus exigeante en documentation, car il faut relier la créance déjà comptabilisée à des flux futurs variables en devise et organiser le suivi OCI/reclassement propre à une couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
    "Au niveau consolidé, la règle générale d’externalité est écartée seulement parce qu’il s’agit d’un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé.",
    "Le timing est déterminant : l’objet couvert est une créance déjà comptabilisée, pas un dividende intragroupe encore seulement prévu.",
    "La documentation doit être posée à l’inception de la relation de couverture et décrire l’élément couvert, le risque de change, l’instrument, le hedge ratio et les tests d’efficacité.",
    "En pratique, la couverture de juste valeur est la qualification la plus directe pour une créance reconnue; la couverture de flux de trésorerie demande une justification plus serrée de la variabilité des flux en devise."
  ]
}
