# IFRS Expert Import Chrome extension

This Chrome-only extension adds the toolbar action **Import to IFRS Expert**.

It supports two source families:

- `https://ifrs.org/*` and `https://*.ifrs.org/*`
- `https://abonnes.efl.fr/*`

The toolbar icon is grey and disabled on unsupported pages and switches to IFRS red on supported pages.

## What it does

### IFRS pages

When clicked on an authenticated IFRS page, it captures:

- the rendered DOM via `document.documentElement.outerHTML`
- the canonical URL via `document.querySelector('link[rel="canonical"]')?.href`
- the agreed JSON sidecar metadata

### Navis / Lefebvre pages

For `abonnes.efl.fr`, the extension now captures at the **chapter** level.

The behavior is:

- enabled only when the selected TOC node is:
  - the corpus root `N24F9F491387ED-EFL`, or
  - a `CHAPITRE` node
- if clicked on a selected `CHAPITRE`, it captures **that chapter only**
- if clicked on the corpus root, it captures **all chapters**, emitting one HTML + JSON pair per chapter

To do that, the extension:

- traverses and expands the left TOC
- discovers leaf pages for the target chapter
- navigates those leaf pages in TOC order
- extracts the relevant DOM fragment from each page
- writes one **synthetic chapter-bundle HTML** plus one sidecar JSON file

The synthetic Navis chapter bundle preserves one page fragment per crawled leaf page and includes a machine-readable manifest for chapter metadata and page order.

## Output location

The extension writes files under:

```text
~/Downloads/ifrs-expert/
```

## Filename shape

### IFRS pages

```text
YYYYMMDDTHHMMSSZ--<slug>.html
YYYYMMDDTHHMMSSZ--<slug>.json
```

### Navis chapter bundles

```text
YYYYMMDDTHHMMSSZ--navis-<PRODUCT_KEY>-<CHAPTER_REF_ID>--<CHAPTER_TITLE>.html
YYYYMMDDTHHMMSSZ--navis-<PRODUCT_KEY>-<CHAPTER_REF_ID>--<CHAPTER_TITLE>.json
```

Where the chapter title is sanitized for filesystem safety and spaces are replaced with underscores.

## Temporary file behavior

The service worker first downloads `.html.part` and `.json.part`, waits for both to complete, then downloads the final `.html` and `.json` files and removes the temporary files.

Chrome extensions do not expose a true filesystem rename primitive for arbitrary local paths, so the implementation uses the Downloads API to approximate the `.part` to final handoff while keeping `.part` files out of the ingest glob.

## Install locally

1. Open `chrome://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select this directory: `chrome_extension/ifrs-expert-import/`

## Workflow

### IFRS workflow

1. Sign in to the IFRS site in Chrome.
2. Open the target `ifrs.org` standard page.
3. Click **Import to IFRS Expert**.
4. Run:

```bash
uv run python -m src.cli ingest
```

### Navis workflow

1. Sign in to `abonnes.efl.fr` in Chrome.
2. Open the Mémento IFRS content page.
3. In the left TOC, select either:
   - the root corpus node `N24F9F491387ED-EFL`, or
   - a `CHAPITRE` node
4. Click **Import to IFRS Expert**.
5. Wait for the extension to traverse the TOC and emit one file pair per captured chapter.
6. In root-batch mode, chapters that already have a downloaded chapter-bundle HTML file in `Downloads/ifrs-expert/` are skipped so the batch resumes from the first chapter not already downloaded.
7. Run:

```bash
uv run python -m src.cli ingest
```

## Toolbar behavior

On Navis pages, the toolbar title changes with context:

- root selected: `Import all chapters to IFRS Expert`
- chapter selected: `Import this chapter to IFRS Expert`
- anything else selected: `Import available only on Navis root or CHAPITRE nodes`

The extension primarily determines this from the current Navis `refId` in the page URL, with DOM inspection as an additional refinement when available. This makes enablement more robust even when the site does not visibly mark the selected TOC node consistently.

You can see this text when hovering the toolbar button and in the extensions menu entry.

## Logging and feedback

The extension logs its execution in the extension service worker console and shows in-page toasts on success or error.

For longer Navis captures, those logs are the main way to follow progress chapter by chapter.
