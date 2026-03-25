{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà créé une créance et une dette intragroupe comptabilisées ; l’exposition analysée est donc celle d’un poste monétaire reconnu, et non celle d’une transaction future.",
    "La créance et la dette existent entre des entités du groupe ayant des monnaies fonctionnelles différentes et elles génèrent des écarts de change qui ne sont pas totalement éliminés en consolidation.",
    "La désignation de couverture viserait uniquement le risque de change et satisferait aux exigences de désignation formelle, de documentation et d’efficacité prévues par IFRS 9.6.4.1."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous vos hypothèses, la créance ou dette de dividende est un poste monétaire intragroupe dont le risque de change peut être désigné en comptes consolidés grâce à l’exception d’IFRS 9.6.3.6. Le fair value hedge est la voie la plus directe ; un cash flow hedge peut aussi être documenté si la désignation porte clairement sur la variabilité des flux de règlement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Dans cette situation, le dividende déclaré a déjà créé une créance ou dette intragroupe reconnue : il s’agit donc d’un actif ou passif monétaire existant. IFRS 9.6.3.5 l’exclut en principe en consolidation, mais 6.3.6 admet explicitement le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés ; c’est précisément votre hypothèse. Le fair value hedge est donc applicable ici, car le risque couvert est la variation de valeur liée au change d’un poste reconnu affectant le résultat consolidé.",
      "conditions_fr": [
        "La créance ou dette de dividende est déjà comptabilisée comme poste monétaire intragroupe.",
        "Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée dès l’origine selon IFRS 9.6.4.1."
      ],
      "practical_implication_fr": "La documentation doit viser le risque de change de la créance ou dette enregistrée, avec une désignation dès l’inception de la relation de couverture.",
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
      "reasoning_fr": "Dans cette situation, le même poste monétaire reconnu expose aussi le groupe à une variabilité du montant de règlement en monnaie fonctionnelle jusqu’au paiement du dividende. Le texte de 6.5.2(b) couvre la variabilité de cash flows d’un actif ou passif reconnu pouvant affecter le résultat, et 6.3.6 rend ce poste intragroupe éligible en consolidation sous vos hypothèses. Cette voie est donc possible ici, mais seulement si la documentation désigne clairement la variabilité des flux de règlement liée au change comme risque couvert.",
      "conditions_fr": [
        "La désignation de couverture vise explicitement la variabilité des flux de règlement liée au change.",
        "Le poste intragroupe remplit l’exception de 6.3.6 parce que les écarts de change affectent le résultat consolidé.",
        "Les exigences de documentation, de relation économique et de hedge ratio d’IFRS 9.6.4.1 sont respectées."
      ],
      "practical_implication_fr": "Cette option exige une rédaction de documentation plus précise sur les flux de règlement couverts et sur la façon de mesurer l’efficacité.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1(c)",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif en consolidation est de démontrer que les écarts de change sur la créance ou dette intragroupe ne sont pas totalement éliminés.",
    "La documentation doit être établie à l’inception et identifier l’instrument de couverture, le poste couvert, le risque de change et le hedge ratio.",
    "Le fait générateur ici est l’enregistrement de la créance de dividende ; l’analyse repose donc sur un poste monétaire reconnu et non sur une transaction intragroupe future."
  ]
}
