# Plan — align shared CLI defaults in `src/cli.py`

## Goal

Make the default story for shared CLI arguments consistent across, while keeping the current `answer` command values unchanged:

- `src/cli.py`
- `src/commands/constants.py`
- the `*Options` dataclasses in `src/commands/*.py`
- help text and tests

The table below records the **current effective CLI defaults**.  
Conventions:

- `required` = positional argument, so no default exists
- `False (store_true)` = implicit argparse default
- `const NAME (= value)` = default comes from `src/commands/constants.py`
- `hard-coded value` = literal in `src/cli.py` or a command module
- `·` = command does not use that argument

For a few options, `argparse` starts with `None` and the command class applies the real fallback internally. In those cases, the table shows the effective fallback value.

## Current default matrix

| argument \ command | chunk | store | ingest | list | query | query-documents | retrieve | query-titles | answer | llm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pdf` | required | · | · | · | · | · | · | · | · | · |
| `source` | · | required | · | · | · | · | · | · | · | · |
| `doc-uid` | · | `None` | · | `None` | · | · | · | · | · | · |
| `scope` | · | hard-coded `"all"` | hard-coded `"all"` | · | · | · | · | · | · | · |
| `k` | · | · | · | · | hard-coded `5` | · | `const DEFAULT_RETRIEVAL_K (= 5)` | hard-coded `5` | `const DEFAULT_RETRIEVAL_K (= 5)` | · |
| `json` | · | · | · | · | `False (store_true)` | `False (store_true)` | `False (store_true)` | `False (store_true)` | · | · |
| `min-score` | · | · | · | · | `const DEFAULT_MIN_SCORE (= 0.55)` | `const DEFAULT_MIN_SCORE_FOR_DOCUMENTS (= 0.50)` | · | `hard-coded 0.6` | `const DEFAULT_RETRIEVE_CONTENT_MIN_SCORE (= 0.53)` | · |
| `d` | · | · | · | · | · | hard-coded `5` | `const DEFAULT_RETRIEVE_DOCUMENT_D (= 25)` | · | `const DEFAULT_RETRIEVE_DOCUMENT_D (= 25)` | · |
| `document-type` | · | · | · | · | · | required | · | · | · | · |
| `expand` | · | · | · | · | hard-coded `0` | hard-coded `0` | hard-coded `0` | · | hard-coded `0` | · |
| `full-doc-threshold` | · | · | · | · | hard-coded `0` | hard-coded `0` | hard-coded `0` | · | hard-coded `0` | · |
| `doc-min-score` | · | · | · | · | · | · | `None` | · | `None` | · |
| `ifrs-d` | · | · | · | · | · | · | `const DEFAULT_D_FOR_IFRS_DOCUMENTS (= 4)` | · | `const DEFAULT_D_FOR_IFRS_DOCUMENTS (= 4)` | · |
| `ias-d` | · | · | · | · | · | · | `const DEFAULT_D_FOR_IAS_DOCUMENTS (= 4)` | · | `const DEFAULT_D_FOR_IAS_DOCUMENTS (= 4)` | · |
| `ifric-d` | · | · | · | · | · | · | `const DEFAULT_D_FOR_IFRIC_DOCUMENTS (= 6)` | · | `const DEFAULT_D_FOR_IFRIC_DOCUMENTS (= 6)` | · |
| `sic-d` | · | · | · | · | · | · | `const DEFAULT_D_FOR_SIC_DOCUMENTS (= 6)` | · | `const DEFAULT_D_FOR_SIC_DOCUMENTS (= 6)` | · |
| `ps-d` | · | · | · | · | · | · | `const DEFAULT_D_FOR_PS_DOCUMENTS (= 1)` | · | `const DEFAULT_D_FOR_PS_DOCUMENTS (= 1)` | · |
| `navis-d` | · | · | · | · | · | · | · | · | · | · |
| `ifrs-min-score` | · | · | · | · | · | · | `const DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS (= 0.53)` | · | `const DEFAULT_MIN_SCORE_FOR_IFRS_DOCUMENTS (= 0.53)` | · |
| `ias-min-score` | · | · | · | · | · | · | `const DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS (= 0.4)` | · | `const DEFAULT_MIN_SCORE_FOR_IAS_DOCUMENTS (= 0.4)` | · |
| `ifric-min-score` | · | · | · | · | · | · | `const DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS (= 0.48)` | · | `const DEFAULT_MIN_SCORE_FOR_IFRIC_DOCUMENTS (= 0.48)` | · |
| `sic-min-score` | · | · | · | · | · | · | `const DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS (= 0.4)` | · | `const DEFAULT_MIN_SCORE_FOR_SIC_DOCUMENTS (= 0.4)` | · |
| `ps-min-score` | · | · | · | · | · | · | `const DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS (= 0.4)` | · | `const DEFAULT_MIN_SCORE_FOR_PS_DOCUMENTS (= 0.4)` | · |
| `navis-min-score` | · | · | · | · | · | · | · | · | · | · |
| `content-min-score` | · | · | · | · | · | · | `const DEFAULT_RETRIEVE_CONTENT_MIN_SCORE (= 0.53)` | · | `const DEFAULT_RETRIEVE_CONTENT_MIN_SCORE (= 0.53)` | · |
| `expand-to-section` | · | · | · | · | · | · | `True` | · | `True` | · |
| `retrieval-mode` | · | · | · | · | · | · | `documents` | · | `documents` | · |
| `output-dir` | · | · | · | · | · | · | · | · | `None` | · |
| `save-all` | · | · | · | · | · | · | · | · | `False (store_true)` | · |

Once the NAVIS flags are exposed, the `navis-d` and `navis-min-score` rows should no longer be `·` for `retrieve` and `answer`; they should use the shared NAVIS constants there too.

## Notable mismatches to fix

1. `query --min-score` help text says `0.6`, but the effective default is `DEFAULT_MIN_SCORE (= 0.55)`.
2. `query-documents --min-score` help text says `0.55`, but the effective default is `DEFAULT_MIN_SCORE_FOR_DOCUMENTS (= 0.50)`.
3. `QueryOptions.expand`, `RetrieveOptions.expand`, and `AnswerOptions.expand` default to `DEFAULT_EXPAND (= 5)`, but `src/cli.py` passes `0`.
4. `RetrieveOptions.expand_to_section` and `AnswerOptions.expand_to_section` default to `False`, but the CLI currently passes `True`.
5. `RetrieveOptions.retrieval_mode` and `AnswerOptions.retrieval_mode` default to `"text"`, but the CLI currently passes `"documents"`.
6. `answer --content-min-score` is effectively `DEFAULT_RETRIEVE_CONTENT_MIN_SCORE (= 0.53)`, even though the parser default is `None`.
7. `navis-d` and `navis-min-score` exist in `RetrieveOptions` and `AnswerOptions`, but the CLI does not expose them yet.

The `answer` command values above should remain exactly as they are now; the cleanup should make those current values explicit and consistent, not change them.

## Suggestion for alignment

### 1. Make constants the single source of truth

Move every shared default into `src/commands/constants.py` and reference those constants everywhere:

- `src/cli.py`
- the `*Options` dataclasses
- any help text that prints a default value

That includes adding missing constants for values that are currently literals, such as:

- `DEFAULT_SCOPE = "all"`
- `DEFAULT_QUERY_TITLES_MIN_SCORE = 0.6`
- `DEFAULT_RETRIEVE_EXPAND = 0` for `retrieve` and `answer`
- `DEFAULT_RETRIEVE_EXPAND_TO_SECTION = True`
- `DEFAULT_RETRIEVE_MODE = "documents"`
- `DEFAULT_NAVIS_D = 2`
- `DEFAULT_NAVIS_MIN_SCORE = 0.6`

Keep the existing `DEFAULT_EXPAND = 5` for the query-style commands; the retrieval pipeline should use its own retrieval-specific constants instead of reusing that value.

### 2. Decide on one canonical behavior for `expand`, `expand-to-section`, and `retrieval-mode`

Right now the parser and the options classes disagree.

Use the current `answer`/`retrieve` CLI behavior as the canonical behavior and keep it unchanged:

- `expand = 0`
- `expand_to_section = True`
- `retrieval_mode = "documents"`

Write those values once as constants, then make both the parser and the `*Options` dataclasses reference the same constants. That preserves the existing `answer` behavior while removing the drift.

### 3. Make parser defaults mirror dataclass defaults

For every shared argument, the parser should import the same default value that the command class uses.

Examples:

- `query --min-score` should use the same constant as `QueryOptions.min_score`
- `query-documents --min-score` should use the same constant as `QueryDocumentsOptions.min_score`
- `retrieve/answer --expand` should use the same constant as the options class, not a separate literal
- `retrieve/answer --expand-to-section` should use one shared constant
- `retrieve/answer --retrieval-mode` should use one shared constant and the dataclass default should match it

### 4. Expose the missing NAVIS options

Add `--navis-d` and `--navis-min-score` to both `retrieve` and `answer` so the CLI surfaces the same knobs that already exist in the options dataclasses and retrieval pipeline.

Use the shared constants for their defaults and include them in the default matrix and tests.

### 5. Add exhaustive parser-vs-options default tests

Add a test module that checks **every argument for every command**.

For each command parser, assert:

- parser default == command option default
- help text matches the same constant
- parser arguments match the command constructor path

That matrix should cover every argument exposed by:

- `chunk`
- `store`
- `ingest`
- `list`
- `query`
- `query-documents`
- `retrieve`
- `query-titles`
- `answer`
- `llm`

Include positional arguments, booleans, hidden defaults, and the NAVIS options once they are exposed.

### 6. Keep the CLI help text generated from the same source

Where the help string prints a default value, build it from the same constant rather than duplicating the number in prose.

That will prevent the kind of drift already visible in the `query` and `query-documents` help text.

## Outcome

After this cleanup, the CLI matrix should collapse to one truth source:

- constants define the defaults
- the dataclasses use those constants
- the parser uses those constants
- tests enforce the match

That should make future changes to shared command arguments much safer.
