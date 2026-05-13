# Simplify and streamline codebase — implementation report

## LOC summary

| File | Before | After |
| --- | ---: | ---: |
| `src/commands/answer.py` | 764 | 154 |
| `src/retrieval/pipeline.py` | 1303 | 302 |
| `src/retrieval/document_profile_builder.py` | 696 | 696 |
| `src/commands/store.py` | 926 | 187 |
| `tests/unit/test_answer_command.py` | 1248 | 875 |
| `tests/unit/test_store_command.py` | 1547 | 750 |
| **Tracked total** | **6484** | **2964** |

## Validation

- `make lint`: pass
- `make test`: 469 passed, 7 skipped; coverage 84.85%
- `make eval-retrieve FAMILY=Q1 EXPERIMENT_DIR=2026-05-13-simplify-final`: 23/23 pass

## Notes

- `AnswerCommand` and `StoreCommand` are now thin adapters.
- Retrieval strategy, chunk expansion, reference expansion, title retrieval, and document routing are split by behavior.
- Case-analysis graph compilation is cached per runner instance.
