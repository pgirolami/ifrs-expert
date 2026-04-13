# Plan — Navis chapter-bundled capture on top of the existing ingestion plan

## Relationship to the existing plan

This plan is a **follow-on** to:

- `plans/2026-04-13--navis-efl-ingestion-plan.md`

That existing plan remains the base ingestion/refactor plan.

This new plan adds one important product decision on top of it:

- for Lefebvre/Navis, the extension should no longer capture one selected page as one stored document
- instead, the extension should produce **one stored document per TOC `CHAPITRE`**

So this plan is mostly about:

- extension enablement rules
- TOC traversal rules
- chapter crawl orchestration
- synthetic bundled HTML output for ingestion
- the resulting navis document identity contract

## Goal

Change the Navis capture workflow so IFRS Expert stores Lefebvre content at the `CHAPITRE` level rather than at the currently selected page level.

Desired result:

- if the user is on a `CHAPITRE`, capture only that chapter
- if the user is at the corpus root `N24F9F491387ED-EFL`, capture the whole corpus by iterating all chapters
- in both cases, persist **one HTML + JSON capture pair per chapter**

## Fixed product decisions

### 1. Document boundary

For Lefebvre/Navis, the persisted document boundary is:

- **one TOC `CHAPITRE` = one IFRS Expert document**

Not:

- one selected leaf page
- one selected section
- one full corpus file

If the user launches from the top/root node, the extension should still emit **multiple captures** — one per chapter.

### 2. Enablement rules

The extension should be enabled on `abonnes.efl.fr` only when the currently selected TOC node is one of:

- the corpus root `N24F9F491387ED-EFL`
- a `CHAPITRE` node

The extension should be disabled when the selected node is:

- a leaf topic
- a section
- an editorial grouping such as `L'ESSENTIEL ...`
- any other non-chapter internal node

### 3. Invocation behavior

When invoked from a selected node:

- root `N24F9F491387ED-EFL` -> crawl all chapters, emit one capture per chapter
- `CHAPITRE ...` -> crawl only that chapter, emit one capture

### 4. Capture format

The extension should no longer save only a raw `document.documentElement.outerHTML` dump for Navis chapter imports.

Instead, for Navis chapter capture it should generate a **synthetic bundled HTML document** that contains the ordered DOM fragments for all leaf pages that belong to the chapter.

IFRS.org capture behavior can remain unchanged.

## Why this is necessary

The two current Navis HTML examples show that:

- the left TOC describes a much larger corpus than the current page content
- a single saved HTML file does not contain the same realized TOC expansion state as another file
- leaf nodes are only visible for the currently expanded branch, not for the whole corpus at once

That means:

- one raw page capture is too granular for retrieval
- one raw page capture is also incomplete as a discovery mechanism for the corpus
- the extension must explicitly traverse and expand the TOC to reconstruct a full chapter

## What the extension must detect

## 1. Selected node identity

From the current page DOM, the extension must determine:

- the selected TOC node `refId`
- whether the selected node is the top/root node
- whether the selected node is a `CHAPITRE`
- the selected node title

Good signals in the samples include:

- `a.lienSommaireSelected`
- `li.liSommaireSelected`
- `data-ref-id`
- displayed title text beginning with `CHAPITRE `

### 2. Root detection

Use the explicit root id:

- `N24F9F491387ED-EFL`

For this corpus, that should be treated as the full-book entry point.

### 3. Chapter detection

I checked the current sample TOCs with this question in mind.

In the saved TOC markup, `CHAPITRE` nodes do **not** appear to have a dedicated CSS class that cleanly distinguishes them from all other node types.

What is available in the samples:

- the selected-state classes: `liSommaireSelected` / `lienSommaireSelected`
- generic tree-state classes such as `opened`, `closed`, and `nochild`
- `data-ref-id`
- the displayed title text
- the structural position in the TOC hierarchy

What is **not** visible in the TOC samples as a reliable chapter-only marker:

- a dedicated chapter class on the TOC `<li>` or `<a>`

So a node should be treated as a chapter target when a combination of the following holds:

- its displayed title starts with `CHAPITRE `
- its `data-ref-id` is chapter-like (for example `C...-EFL`) as a corroborating signal
- its structural position in the TOC is consistent with a chapter node

If later samples reveal a stronger chapter-specific marker, we should switch to that.

## Crawl strategy

## 1. High-level algorithm

### If launched from a chapter

1. identify the selected chapter node
2. expand that chapter subtree completely
3. collect all descendant leaf pages in DOM order
4. visit each leaf page in order
5. capture the relevant content fragment from each visited page
6. build one synthetic bundled HTML document for the chapter
7. write one sidecar JSON file for the chapter

### If launched from root

1. expand the root subtree enough to enumerate all chapter nodes
2. collect chapters in DOM order
3. for each chapter, call the **same chapter-capture routine** used when the user launches directly from a selected chapter

Important implementation constraint:

- root-batch mode should be a thin wrapper around chapter capture
- there should be one reusable routine such as `capture_chapter(chapter_target)` that both entry paths call
- root mode should not duplicate the logic for subtree expansion, leaf collection, page navigation, fragment capture, bundling, or file emission

## 2. TOC expansion behavior

The extension should not assume a chapter subtree is already present in the DOM.

It should:

- detect closed/open branch controls
- expand closed nodes recursively as needed
- wait for async TOC content to load after each expansion
- only then continue traversal

The samples show that `#tocTree` is stateful and lazily realized, so deterministic expansion is mandatory.

## 3. Leaf-node collection

For a given chapter, collect descendant leaves in displayed TOC order.

The important output is an ordered list of page targets:

- `page_ref_ids`
- `page_titles`
- optional TOC ancestry path for debugging

Those leaf nodes become crawl targets, not persisted document identities.

## 4. Page navigation

For each leaf node, the extension should navigate through the site in the same way the UI does.

The safest v1 approach is:

- click the TOC node or invoke the same page navigation behavior the page uses internally
- wait until the selected TOC node changes to the expected leaf
- wait until `#documentContent` settles
- then capture the content fragment

Success should not be judged only by URL change, because this UI behaves like an in-page application.

## Bundled HTML output design

## 1. Output contract

For Navis chapter capture, emit:

- one synthetic `.html`
- one `.json` sidecar

per chapter.

If run from root, repeat this once per chapter.

## 2. Synthetic HTML structure

A good v1 structure is:

```html
<html data-ifrs-expert-source="navis" data-ifrs-expert-capture="chapter-bundle">
  <head>
    <meta charset="utf-8">
    <title>...</title>
  </head>
  <body>
    <script id="ifrs-expert-navis-manifest" type="application/json">...</script>

    <div id="ifrs-expert-navis-bundle" data-chapter-ref-id="...">
      <section class="ifrs-expert-navis-page" data-page-ref-id="..." data-page-title="...">
        <!-- preserved DOM fragment from #documentContent .question.question-export -->
      </section>
      <section class="ifrs-expert-navis-page" data-page-ref-id="..." data-page-title="...">
        ...
      </section>
    </div>
  </body>
</html>
```

The important properties are:

- one explicit bundle wrapper
- one embedded machine-readable manifest
- one preserved content fragment per crawled page
- deterministic page order
- enough metadata to recover provenance

## 3. What DOM to preserve per page

For each crawled leaf page, preserve only the relevant content DOM, not the whole browser page chrome.

Preferred payload per page:

- `#documentContent .question.question-export`

This is better than storing the full page repeatedly because it:

- removes noisy site chrome
- keeps file size smaller
- makes parsing more deterministic
- avoids repeated TOC/sidebar/header markup in every page fragment

## 4. TOC snapshot handling

Optional but useful:

- include a TOC snapshot or structured TOC manifest for the chapter

This would help with:

- debugging traversal failures
- auditability
- future provenance features

But the ingester should still derive chunks/sections from the bundled body fragments, not from TOC ancestry alone.

## Sidecar JSON contract

For Navis chapter bundles, the sidecar should include at least:

```json
{
  "capture_format": "navis-chapter-bundle/v1",
  "capture_mode": "chapter",
  "source_domain": "abonnes.efl.fr",
  "product_key": "QRIFRS",
  "root_ref_id": "N24F9F491387ED-EFL",
  "chapter_ref_id": "C2A8E6F292F99E-EFL",
  "chapter_title": "CHAPITRE 4 ...",
  "page_ref_ids": ["P...", "P..."],
  "page_titles": ["Généralités", "Présentation du Cadre conceptuel"],
  "captured_at": "2026-...Z",
  "extension_version": "0.1.0",
  "url": "https://abonnes.efl.fr/...",
  "canonical_url": "https://abonnes.efl.fr/..."
}
```

If launched from root, `capture_mode` can be:

- `root-batch`

while each emitted chapter file still carries its own `chapter_ref_id`.

## Naming and identity

## 1. `doc_uid`

The persisted navis `doc_uid` should be chapter-based and should preserve the original Navis casing for identifiers:

```text
navis-<product-key>-<chapter-refid>
```

Example:

```text
navis-QRIFRS-C2A8E6F292F99E-EFL
```

## 2. Filenames

The download basename should also be chapter-oriented and should preserve identifier casing.

A good pattern is:

```text
<timestamp>--navis-<product-key>-<chapter-refid>--<sanitized-chapter-title>
```

Where `sanitized-chapter-title` should at minimum:

- replace spaces with underscores
- remove or replace filename-unsafe characters
- preserve the visible chapter wording as much as practical

Example:

```text
20260413T120000Z--navis-QRIFRS-C2A8E6F292F99E-EFL--CHAPITRE_4_Cadre_conceptuel_de_l_information_financiere
```

The stable component remains the chapter ref id; the sanitized title is there for operator readability.

## Ingestion implications

This plan changes the **capture contract** for Navis ingestion, but not the core conceptual model of ingestion.

The important difference is only this:

- before: one raw page capture in -> one document out
- now: one chapter bundle capture in -> one document out

The resulting document is still a normal document containing:

- a hierarchy of sections
- paragraph/chunk anchors
- ordered chunk text

So ingestion does **not** need a new conceptual model for hierarchy. It mainly needs a different input reader.

The Navis extractor therefore needs to:

- parse the embedded bundle manifest
- iterate ordered page fragments
- extract headings/chunks from each fragment
- preserve paragraph anchor ids as chunk locators
- produce one `DocumentRecord` for the chapter

## Bundle ordering and normalization rules

The main normalization concern is **not** repeated `TITRE` or nested `CHAPITRE` headings.

Your point is correct:

- a `TITRE` sits above a `CHAPITRE`
- a `CHAPITRE` does not contain another `CHAPITRE`
- so repeated `TITRE` / `CHAPITRE` headings should not be assumed as a default bundling problem for one chapter capture

So the normalization rules should be reframed more narrowly:

- preserve the page-fragment order captured from the TOC traversal
- preserve the section/chunk hierarchy found in the bundled content
- do not invent deduplication rules unless repeated content is actually observed in real chapter bundles
- if the site repeats overlap text across page boundaries, handle that as a targeted normalization rule backed by samples
- otherwise, the default behavior should be faithful concatenation of the chapter's ordered page fragments

## Extension UX changes

## 1. Action enablement

The toolbar action should communicate why it is disabled when on Navis pages that are not root or chapter nodes.

Suggested behavior:

- enabled on root -> title like `Import all chapters to IFRS Expert`
- enabled on chapter -> title like `Import this chapter to IFRS Expert`
- disabled elsewhere -> title like `Import available only on Navis root or CHAPITRE nodes`

These action titles are visible in the browser UI when you hover over the extension's toolbar button and also in the extensions menu entry for the action.

So they are useful as contextual hints, but they are not the main progress surface. For more visible operator feedback, page toasts and extension logs are still more important.

## 2. Progress feedback

Because root or chapter capture may take time, the extension should provide progress logs and page toasts such as:

- chapter discovery started
- chapter `x/y`
- page `n/m` within current chapter
- chapter output saved
- batch completed

## Failure handling

## 1. Per-chapter isolation

In root-batch mode, one failed chapter should not invalidate all successfully captured chapters.

Recommended behavior:

- process chapters independently
- surface a final summary of successes/failures
- emit successful chapter files even if one later chapter fails

## 2. Per-page failure policy

For v1, prefer fail-fast within a single chapter if:

- a required leaf page cannot be opened
- the content root cannot be found
- the selected leaf does not match the expected page target

This avoids silently creating incomplete chapter documents.

## Testing plan

### Unit tests

Add tests for:

1. selected-node classification: root / chapter / unsupported
2. root-id detection for `N24F9F491387ED-EFL`
3. chapter-node detection from TOC metadata/title
4. TOC traversal over lazily expanded branches
5. leaf collection in stable DOM order
6. chapter grouping logic in root-batch mode
7. bundled HTML generation shape
8. Navis sidecar manifest generation for chapter bundles
9. chapter-based filename / basename generation
10. chapter-based `doc_uid` derivation preserving original ref casing

### Integration tests

Add tests for:

1. chapter capture from a selected `CHAPITRE`
2. root-batch capture producing multiple chapter outputs
3. incomplete TOC expansion being retried correctly
4. page navigation waiting for the expected selected leaf and stable content
5. ingestion of one synthetic chapter bundle
6. skip-if-unchanged for a chapter bundle
7. replacement when a page within a chapter changes

## Implementation phases

### Phase 1 — lock the extension contract

Deliver:

- explicit enablement rules for root vs chapter vs unsupported nodes
- chapter crawl algorithm
- bundled HTML + sidecar schema
- filename and `doc_uid` conventions

Success criteria:

- we agree on the chapter-level capture contract before implementation

### Phase 2 — implement TOC traversal in the extension

Deliver:

- selected-node detection
- recursive expansion
- leaf discovery
- page navigation and waiting

Success criteria:

- the extension can reliably enumerate all leaf pages for one selected chapter

### Phase 3 — implement bundled chapter output

Deliver:

- synthetic bundled HTML generation
- chapter manifest generation
- one output file pair per chapter
- root-batch mode producing multiple chapter outputs

Success criteria:

- chapter captures are emitted deterministically and are ingestion-ready

### Phase 4 — adapt the Navis extractor to chapter bundles

Deliver:

- parsing of the bundled HTML contract
- chapter-level `doc_uid`
- deduplication of repeated headings
- chunk/section extraction across ordered page fragments

Success criteria:

- one bundled chapter capture ingests into one coherent navis document

## Recommendation

Use the existing `2026-04-13--navis-efl-ingestion-plan.md` as the base ingestion/refactor plan, and treat this new plan as the **capture-contract addendum** that changes the Navis unit of ingestion from page-level to chapter-level.

That yields a clean separation:

- existing plan = navis ingestion support in principle
- this plan = how the extension must materialize Navis content so retrieval is not broken

This is the soundest direction because it aligns the capture boundary with a meaningful editorial unit while still allowing deterministic crawl and provenance tracking.
