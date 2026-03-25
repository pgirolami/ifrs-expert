{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà été comptabilisé comme une créance/dette monétaire intragroupe.",
    "Cette créance/dette est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités, et les écarts de change correspondants affectent le résultat consolidé au lieu d’être entièrement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans ce cas, IFRS 9 permet en consolidation de couvrir le seul risque de change d’un poste monétaire intragroupe lorsqu’il crée des écarts non entièrement éliminés. Cette composante de change peut être désignée soit en couverture de juste valeur, soit en couverture de flux de trésorerie, sous réserve de la documentation et de l’efficacité requises."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la composante change",
      "applicability": "oui",
      "reasoning_fr": "Le dividende intragroupe est déjà comptabilisé, selon les hypothèses, comme une créance/dette monétaire intragroupe. Même si la règle générale exclut les éléments intragroupe en consolidation, IFRS 9 admet en exception le seul risque de change d’un poste monétaire intragroupe lorsqu’il génère des écarts non totalement éliminés en résultat consolidé. Comme IFRS 9 autorise aussi la désignation d’une composante de risque spécifique, la seule composante de change peut être couverte en fair value hedge à ce stade de reconnaissance.",
      "conditions_fr": [
        "Documenter formellement dès l’origine l’instrument de couverture, le poste couvert, le risque de change visé et le hedge ratio.",
        "Démontrer une relation économique entre l’instrument et la composante de change couverte, sans domination du risque de crédit."
      ],
      "practical_implication_fr": "Le groupe peut viser uniquement l’exposition de change du dividende intragroupe reconnu et appliquer la mécanique comptable d’une couverture de juste valeur.",
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
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie de la composante change",
      "applicability": "oui",
      "reasoning_fr": "Le même poste monétaire intragroupe déjà reconnu peut aussi entrer dans une cash flow hedge, car IFRS 9 vise la variabilité de flux d’un actif ou passif comptabilisé attribuable à un risque particulier. Sous les hypothèses retenues, le règlement en devise du dividende intragroupe continue d’exposer le groupe à un effet de change qui affecte le résultat consolidé. Dans cette situation, la seule composante de change peut donc être désignée en couverture de flux de trésorerie, sans revenir à un stade antérieur de la transaction.",
      "conditions_fr": [
        "Documenter formellement dès l’origine l’instrument de couverture, le poste couvert, le risque de change visé et le hedge ratio.",
        "Démontrer une relation économique entre l’instrument et la composante de change couverte, sans domination du risque de crédit.",
        "Définir clairement que la variabilité couverte porte sur les flux de règlement en devise de la créance/dette reconnue."
      ],
      "practical_implication_fr": "Le groupe peut couvrir la variabilité en monnaie fonctionnelle des flux de règlement du dividende intragroupe reconnu sans couvrir d’autres composantes du poste.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de timing décisif est que le dividende est déjà comptabilisé : l’analyse porte sur un poste monétaire intragroupe reconnu, non sur un dividende futur.",
    "En consolidation, il faut établir et tracer que l’écart de change sur ce poste n’est pas entièrement éliminé et qu’il affecte bien le résultat consolidé.",
    "La désignation peut viser la seule composante de change, à condition qu’elle soit séparément identifiable et fiable à mesurer.",
    "Le choix entre fair value hedge et cash flow hedge doit être aligné sur l’objectif de gestion du risque et figurer dans la documentation initiale."
  ]
}
