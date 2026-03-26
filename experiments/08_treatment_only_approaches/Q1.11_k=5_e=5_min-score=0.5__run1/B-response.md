{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance/dette intragroupe monétaire déjà comptabilisée, et non une transaction future.",
    "La créance/dette est libellée dans une devise générant des écarts de change qui ne sont pas totalement éliminés en consolidation parce que les entités du groupe ont des monnaies fonctionnelles différentes.",
    "Le groupe respecte les exigences de désignation formelle, de documentation initiale et d’efficacité de la couverture prévues par IFRS 9 paragraphe 6.4.1."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation, car l’exception d’IFRS 9 pour le risque de change d’un élément monétaire intragroupe en consolidation peut s’appliquer.\nLa couverture n’est possible que si les écarts de change ne sont pas totalement éliminés et si la relation est formellement désignée et documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende déclaré a déjà créé une créance/dette intragroupe reconnue. La règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés.\nCe schéma est cohérent avec une couverture d’un actif/passif reconnu exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [
        "La créance/dette de dividende doit être un élément monétaire intragroupe déjà comptabilisé.",
        "Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.",
        "La relation de couverture doit être désignée et documentée dès l’origine conformément à IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "Le groupe peut documenter la couverture du risque de change porté par la créance/dette de dividende déjà enregistrée dans les comptes consolidés.",
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
      "reasoning_fr": "Dans cette situation, la créance/dette de dividende est un actif/passif reconnu et son règlement en monnaie fonctionnelle reste exposé au change. IFRS 9 6.5.2(b) permet le modèle de cash flow hedge pour un actif ou passif reconnu lorsqu’il existe une variabilité des flux pouvant affecter le résultat.\nL’éligibilité en consolidation repose néanmoins sur la même exception de 6.3.6 pour les éléments monétaires intragroupe.",
      "conditions_fr": [
        "Le groupe doit documenter le risque couvert comme une variabilité des flux de règlement en monnaie fonctionnelle affectant le résultat.",
        "La créance/dette doit remplir l’exception de 6.3.6 applicable aux éléments monétaires intragroupe en consolidation.",
        "La désignation, le ratio de couverture et l’évaluation de l’efficacité doivent être formalisés selon IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "Le groupe peut aussi retenir un modèle de couverture de flux si la documentation vise la variabilité des flux de règlement liée au change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de bascule est la comptabilisation du dividende : une fois la créance/dette enregistrée, l’analyse se fait comme élément monétaire intragroupe reconnu.",
    "En consolidation, il faut démontrer que les écarts de change sur cette créance/dette ne sont pas totalement éliminés du fait de monnaies fonctionnelles différentes.",
    "La documentation initiale doit identifier l’instrument de couverture, la créance/dette de dividende, le risque de change couvert, le ratio de couverture et les sources d’inefficacité.",
    "Par prudence opérationnelle, la couverture de juste valeur est la plus directement alignée avec une créance/dette déjà comptabilisée, même si le modèle de flux reste envisageable sous documentation adaptée."
  ]
}
