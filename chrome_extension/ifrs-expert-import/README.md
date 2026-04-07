# IFRS Expert Import Chrome extension

This Chrome-only extension adds the toolbar action **Import to IFRS Expert**.

By default, it is scoped to `https://*.ifrs.org/*` pages only.

## What it does

When clicked on an authenticated IFRS page, it captures:

- the rendered DOM via `document.documentElement.outerHTML`
- the canonical URL via `document.querySelector('link[rel="canonical"]')?.href`
- the agreed JSON sidecar metadata

It writes files under:

```text
~/Downloads/ifrs-expert/inbox/
```

with names shaped like:

```text
YYYYMMDDTHHMMSSZ--<slug>.html
YYYYMMDDTHHMMSSZ--<slug>.json
```

## Temporary file behavior

The service worker first downloads `.html.part` and `.json.part`, waits for both to complete, then downloads the final `.html` and `.json` files and removes the temporary files.

Chrome extensions do not expose a true filesystem rename primitive for arbitrary local paths, so the implementation uses the Downloads API to approximate the `.part` to final handoff while keeping `.part` files out of the ingest glob.

## Install locally

1. Open `chrome://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select this directory: `chrome_extension/ifrs-expert-import/`

## Workflow

1. Sign in to the IFRS site in Chrome.
2. Open the target `ifrs.org` standard page.
3. Click **Import to IFRS Expert**.

If you are not on an `ifrs.org` page, the extension does nothing.
4. Run:

```bash
uv run python -m src.cli ingest
```
