{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance/dette en devise déjà comptabilisée, constituant un poste monétaire.",
    "Les écarts de change sur ce poste monétaire intragroupe ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidé, les opérations intragroupe sont en principe exclues comme éléments couverts, mais IFRS 9 prévoit une exception explicite pour le risque de change d’un poste monétaire intragroupe non totalement éliminé en consolidation. Une créance de dividende en devise déjà comptabilisée peut donc être désignée, avec documentation formelle et tests d’efficacité à l’inception de la relation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "Ici, la question porte sur une créance intragroupe en devise déjà comptabilisée; selon les hypothèses, il s’agit d’un poste monétaire dont les écarts de change affectent encore le résultat consolidé.\nMême si 6.3.5 pose une exclusion générale en consolidé, 6.3.6 admet expressément le risque de change d’un poste monétaire intragroupe; et 6.5.2(a) vise un actif/passif comptabilisé exposé à un risque particulier affectant le résultat.\nCette voie est donc ouverte à ce stade, à condition de documenter la relation de couverture à son inception et de satisfaire aux critères de 6.4.1.",
      "conditions_fr": [
        "Documenter dès l’inception de la relation l’instrument de couverture, la créance/dette couverte, le risque de change couvert et la méthode de test d’efficacité.",
        "Vérifier que la relation respecte les critères de 6.4.1: instrument et élément éligibles, relation économique, risque de crédit non dominant et hedge ratio cohérent."
      ],
      "practical_implication_fr": "Il faut mettre en place une relation de fair value hedge sur le poste monétaire intragroupe déjà comptabilisé et en suivre l’efficacité pendant sa durée de vie.",
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
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui",
      "reasoning_fr": "Le fait pattern reste celui d’une créance intragroupe en devise déjà reconnue; les hypothèses posent que son risque de change n’est pas totalement neutralisé en consolidation et peut affecter le résultat consolidé.\nDans ce cadre, 6.3.6 rend éligible le risque de change du poste monétaire intragroupe en consolidé, et 6.5.2(b) autorise un cash flow hedge d’un risque particulier associé à un actif/passif comptabilisé.\nCette approche est donc également disponible à ce stade de reconnaissance, sous désignation formelle à l’inception de la couverture et respect des critères d’efficacité de 6.4.1.",
      "conditions_fr": [
        "Formaliser à l’inception la désignation du risque de change couvert sur la créance/dette intragroupe et la méthode de mesure de l’efficacité.",
        "Démontrer le respect continu des critères de 6.4.1, notamment la relation économique et un hedge ratio aligné sur la gestion du risque."
      ],
      "practical_implication_fr": "Il faut documenter la variabilité des flux en monnaie fonctionnelle liée au règlement du poste monétaire intragroupe et suivre l’efficacité jusqu’au dénouement.",
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
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé en consolidé n’est pas le dividende intragroupe en lui-même, mais la créance/dette monétaire en devise déjà enregistrée et son risque de change résiduel.",
    "La documentation doit être établie à l’inception de la relation de couverture sur la créance déjà comptabilisée; elle ne couvre pas rétroactivement des périodes antérieures.",
    "Le dossier de hedge accounting doit démontrer que l’écart de change du poste monétaire intragroupe n’est pas totalement éliminé en consolidation et qu’il affecte le résultat consolidé.",
    "Les deux voies techniques identifiées restent possibles dans ce cas: fair value hedge ou cash flow hedge, sous réserve des exigences générales de désignation, documentation et efficacité de 6.4.1."
  ]
}
