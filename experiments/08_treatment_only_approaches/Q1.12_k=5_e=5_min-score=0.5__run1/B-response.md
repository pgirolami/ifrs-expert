{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et comptabilisé en créance/dette intragroupe ; il s’agit donc d’un élément monétaire intragroupe reconnu, et non d’une transaction future.",
    "La créance/dette est libellée dans une devise générant des écarts de change qui ne sont pas totalement éliminés en consolidation parce que les entités concernées ont des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. Au niveau consolidé, l’exception IFRS 9 pour le risque de change d’un élément monétaire intragroupe permet de viser formellement la créance de dividende si les écarts de change ne sont pas totalement éliminés. La voie la plus directe est la couverture de juste valeur, avec désignation, documentation et critères d’efficacité satisfaits dès l’origine."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Au consolidé, un poste intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe non totalement éliminé en consolidation.\nIci, le dividende déjà comptabilisé en créance correspond à un actif monétaire reconnu ; la couverture de juste valeur est donc la qualification la plus directe, sous réserve de la documentation et de l’efficacité.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe déjà comptabilisé.",
        "Le risque de change crée des gains ou pertes non totalement éliminés en consolidation.",
        "La relation de couverture est formellement désignée et documentée à l’origine.",
        "Les critères d’efficacité de l’IFRS 9 sont respectés."
      ],
      "practical_implication_fr": "Le dossier de couverture peut viser la créance intragroupe déjà reconnue comme élément couvert du risque de change au niveau consolidé.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items."
        },
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
      "reasoning_fr": "IFRS 9 n’exclut pas qu’une couverture de flux de trésorerie vise un actif ou un passif reconnu, et l’exception intragroupe sur le risque de change reste pertinente au consolidé.\nToutefois, dans ce cas précis, l’exposition provient d’une créance de dividende déjà comptabilisée ; cette qualification n’est défendable que si la relation est expressément documentée comme une variabilité des flux de règlement liée au change et qu’elle satisfait aux tests IFRS 9.",
      "conditions_fr": [
        "La documentation décrit la variabilité des flux de règlement en monnaie fonctionnelle liée au change.",
        "La créance reste un élément monétaire intragroupe dont le risque de change affecte le résultat consolidé.",
        "La désignation et la documentation sont établies dès l’origine de la relation.",
        "Les exigences d’efficacité de l’IFRS 9 sont satisfaites."
      ],
      "practical_implication_fr": "Cette voie est possible mais demande une justification documentaire plus serrée que la couverture de juste valeur pour une créance déjà reconnue.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé de qualification est que le dividende est déjà comptabilisé en créance intragroupe ; on n’est pas dans une transaction future intragroupe.",
    "Au consolidé, il faut démontrer que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés.",
    "La documentation doit être en place dès l’inception et identifier l’instrument de couverture, l’élément couvert, le risque de change et le test d’efficacité.",
    "En pratique, la couverture de juste valeur est la voie la plus directement alignée avec une créance de dividende intragroupe déjà reconnue."
  ]
}
