const INBOX_PREFIX = "ifrs-expert/inbox";
const HTML_MIME_TYPE = "text/html;charset=utf-8";
const JSON_MIME_TYPE = "application/json;charset=utf-8";

chrome.action.onClicked.addListener(async (tab) => {
  if (tab.id === undefined) {
    return;
  }

  try {
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: captureRenderedPage,
    });

    const basename = buildCaptureBasename(result);
    const htmlPartFilename = `${INBOX_PREFIX}/${basename}.html.part`;
    const jsonPartFilename = `${INBOX_PREFIX}/${basename}.json.part`;
    const htmlFilename = `${INBOX_PREFIX}/${basename}.html`;
    const jsonFilename = `${INBOX_PREFIX}/${basename}.json`;

    const htmlBlobUrl = URL.createObjectURL(new Blob([result.html], { type: HTML_MIME_TYPE }));
    const jsonBlobUrl = URL.createObjectURL(
      new Blob([JSON.stringify(result.sidecar, null, 2)], { type: JSON_MIME_TYPE }),
    );

    const htmlPartDownloadId = await downloadBlob(htmlBlobUrl, htmlPartFilename);
    const jsonPartDownloadId = await downloadBlob(jsonBlobUrl, jsonPartFilename);
    await Promise.all([waitForDownload(htmlPartDownloadId), waitForDownload(jsonPartDownloadId)]);

    const finalHtmlBlobUrl = URL.createObjectURL(new Blob([result.html], { type: HTML_MIME_TYPE }));
    const finalJsonBlobUrl = URL.createObjectURL(
      new Blob([JSON.stringify(result.sidecar, null, 2)], { type: JSON_MIME_TYPE }),
    );

    const finalHtmlDownloadId = await downloadBlob(finalHtmlBlobUrl, htmlFilename);
    const finalJsonDownloadId = await downloadBlob(finalJsonBlobUrl, jsonFilename);
    await Promise.all([waitForDownload(finalHtmlDownloadId), waitForDownload(finalJsonDownloadId)]);

    await removeDownloadedFile(htmlPartDownloadId);
    await removeDownloadedFile(jsonPartDownloadId);

    URL.revokeObjectURL(htmlBlobUrl);
    URL.revokeObjectURL(jsonBlobUrl);
    URL.revokeObjectURL(finalHtmlBlobUrl);
    URL.revokeObjectURL(finalJsonBlobUrl);

    console.info(`Saved ${basename}.html and ${basename}.json to Downloads/${INBOX_PREFIX}`);
  } catch (error) {
    console.error("IFRS Expert import failed", error);
  }
});

function captureRenderedPage() {
  const canonicalUrl = document.querySelector('link[rel="canonical"]')?.href ?? window.location.href;
  const title = document.title || canonicalUrl;

  return {
    html: document.documentElement.outerHTML,
    sidecar: {
      url: window.location.href,
      title,
      captured_at: new Date().toISOString().replace(/\.\d{3}Z$/, "Z"),
      source_domain: window.location.hostname,
      canonical_url: canonicalUrl,
      extension_version: chrome.runtime.getManifest().version,
      content_type: document.contentType || "text/html",
    },
  };
}

function buildCaptureBasename(result) {
  const timestamp = result.sidecar.captured_at.replace(/[-:]/g, "").replace(/\.\d{3}Z$/, "Z");
  const candidate = deriveSlug(result.sidecar.canonical_url, result.sidecar.title);
  return `${timestamp}--${candidate}`;
}

function deriveSlug(canonicalUrl, title) {
  try {
    const url = new URL(canonicalUrl);
    const pathnamePart = url.pathname.split("/").filter(Boolean).at(-1) ?? "ifrs-capture";
    const filenameStem = pathnamePart.replace(/\.html?$/i, "");
    return slugify(filenameStem || title);
  } catch {
    return slugify(title);
  }
}

function slugify(value) {
  return value
    .normalize("NFKD")
    .replace(/[^a-zA-Z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase() || "ifrs-capture";
}

function downloadBlob(blobUrl, filename) {
  return chrome.downloads.download({
    url: blobUrl,
    filename,
    saveAs: false,
    conflictAction: "uniquify",
  });
}

function waitForDownload(downloadId) {
  return new Promise((resolve, reject) => {
    const listener = (delta) => {
      if (delta.id !== downloadId || delta.state === undefined) {
        return;
      }
      if (delta.state.current === "complete") {
        chrome.downloads.onChanged.removeListener(listener);
        resolve();
      }
      if (delta.state.current === "interrupted") {
        chrome.downloads.onChanged.removeListener(listener);
        reject(new Error(`Download ${downloadId} was interrupted`));
      }
    };

    chrome.downloads.onChanged.addListener(listener);
  });
}

async function removeDownloadedFile(downloadId) {
  try {
    await chrome.downloads.removeFile(downloadId);
  } catch (error) {
    console.warn(`Unable to remove temporary download ${downloadId}`, error);
  }
}
