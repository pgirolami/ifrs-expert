import {
  extractIfrsDocumentNavigationToken,
  normalizeIfrsVariantPathStem,
} from "./ifrs_import.mjs";
import {
  createImportProgressState,
  reduceImportProgressState,
} from "./progress_state.mjs";

export const LOG_PREFIX = "[IFRS Expert Extract]";
export const ROOT_PREFIX = "ifrs-expert";
export const HTML_MIME_TYPE = "text/html;charset=utf-8";
export const JSON_MIME_TYPE = "application/json;charset=utf-8";
export const PAGE_TOAST_DURATION_MS = 4000;
export const ACTION_TITLE = "Extract";
export const UNSUPPORTED_ACTION_TITLE = "Extract (available only on supported sources)";
export const IMPORT_PROGRESS_STORAGE_KEY = "importProgressState";
export const SUPPORTED_ACTION_ICON_PATHS = {
  16: "icons/ifrs-red-16.png",
  24: "icons/ifrs-red-24.png",
  32: "icons/ifrs-red-32.png",
};
export const UNSUPPORTED_ACTION_ICON_PATHS = {
  16: "icons/ifrs-grey-16.png",
  24: "icons/ifrs-grey-24.png",
  32: "icons/ifrs-grey-32.png",
};

let importProgressState = createImportProgressState();
let importCancellationRequested = false;

export function openImportSidePanel(tabId) {
  if (chrome.sidePanel === undefined) {
    return;
  }

  void chrome.sidePanel.open({ tabId }).catch((error) => {
    logWarn("Unable to open extraction side panel.", {
      tabId,
      error: formatErrorMessage(error),
    });
  });
}

export async function updateImportProgress(event) {
  importProgressState = reduceImportProgressState(importProgressState, event);
  await chrome.storage.session.set({ [IMPORT_PROGRESS_STORAGE_KEY]: importProgressState });
}

export async function requestImportCancellation() {
  if (importProgressState.status !== "running" || importProgressState.cancelRequested) {
    return;
  }
  importCancellationRequested = true;
  await updateImportProgress({
    type: "cancelRequested",
    logMessage: "Stop requested by user",
  });
}

export function isImportCancellationError(error) {
  return formatErrorMessage(error) === "Extraction cancelled by user";
}

export function throwIfImportCancelled() {
  if (importCancellationRequested) {
    throw new Error("Extraction cancelled by user");
  }
}

export async function resetImportProgress() {
  importProgressState = createImportProgressState();
  importCancellationRequested = false;
  await chrome.storage.session.set({ [IMPORT_PROGRESS_STORAGE_KEY]: importProgressState });
}

export function sleepMs(durationMs) {
  return new Promise((resolve) => {
    setTimeout(resolve, durationMs);
  });
}

export async function reloadTab(tabId) {
  await chrome.tabs.reload(tabId);
}

export async function waitForTabComplete(tabId, timeoutMs = 15000) {
  const currentTab = await chrome.tabs.get(tabId);
  if (currentTab.status === "complete") {
    return;
  }

  await new Promise((resolve, reject) => {
    let resolved = false;
    const timeoutId = setTimeout(() => {
      if (resolved) {
        return;
      }
      resolved = true;
      chrome.tabs.onUpdated.removeListener(listener);
      reject(new Error(`Timed out while waiting for tab ${tabId} to finish loading`));
    }, timeoutMs);

    const listener = (updatedTabId, changeInfo, updatedTab) => {
      if (updatedTabId !== tabId) {
        return;
      }
      if (changeInfo.status !== "complete" && updatedTab.status !== "complete") {
        return;
      }
      if (resolved) {
        return;
      }
      resolved = true;
      clearTimeout(timeoutId);
      chrome.tabs.onUpdated.removeListener(listener);
      resolve();
    };

    chrome.tabs.onUpdated.addListener(listener);
  });
}

export async function navigateTabToUrl(tabId, url, expectedRefId = null) {
  const currentTab = await chrome.tabs.get(tabId);
  if (isNavigationTargetReached(currentTab.url, url, expectedRefId) && currentTab.status === "complete") {
    return;
  }

  await new Promise((resolve, reject) => {
    let resolved = false;
    const timeoutId = setTimeout(() => {
      if (resolved) {
        return;
      }
      resolved = true;
      chrome.tabs.onUpdated.removeListener(listener);
      reject(new Error(`Timed out while navigating tab ${tabId} to ${url}`));
    }, 15000);

    const listener = (updatedTabId, changeInfo, updatedTab) => {
      if (updatedTabId !== tabId) {
        return;
      }
      if (changeInfo.status !== "complete") {
        return;
      }
      const updatedUrl = updatedTab.url ?? updatedTab.pendingUrl;
      if (!isNavigationTargetReached(updatedUrl, url, expectedRefId)) {
        return;
      }
      if (resolved) {
        return;
      }
      resolved = true;
      clearTimeout(timeoutId);
      chrome.tabs.onUpdated.removeListener(listener);
      resolve();
    };

    chrome.tabs.onUpdated.addListener(listener);
    chrome.tabs.update(tabId, { url }).catch((error) => {
      if (resolved) {
        return;
      }
      resolved = true;
      clearTimeout(timeoutId);
      chrome.tabs.onUpdated.removeListener(listener);
      reject(error);
    });
  });
}

export async function downloadCaptureArtifacts(result) {
  throwIfImportCancelled();
  const basename = buildCaptureBasename(result);
  const htmlPartFilename = `${ROOT_PREFIX}/${basename}.html.part`;
  const jsonPartFilename = `${ROOT_PREFIX}/${basename}.json.part`;
  const htmlFilename = `${ROOT_PREFIX}/${basename}.html`;
  const jsonFilename = `${ROOT_PREFIX}/${basename}.json`;
  const sidecarJson = JSON.stringify(result.sidecar, null, 2);

  logInfo("Prepared filenames.", {
    basename,
    htmlPartFilename,
    jsonPartFilename,
    htmlFilename,
    jsonFilename,
  });

  const htmlDownloadResource = await createDownloadResource(result.html, HTML_MIME_TYPE);
  const jsonDownloadResource = await createDownloadResource(sidecarJson, JSON_MIME_TYPE);

  try {
    const htmlPartDownloadId = await downloadBlob(htmlDownloadResource.url, htmlPartFilename);
    const jsonPartDownloadId = await downloadBlob(jsonDownloadResource.url, jsonPartFilename);
    await Promise.all([
      waitForDownload(htmlPartDownloadId, htmlPartFilename),
      waitForDownload(jsonPartDownloadId, jsonPartFilename),
    ]);

    logInfo("Temporary downloads completed.", {
      htmlPartDownloadId,
      jsonPartDownloadId,
      basename,
    });

    const finalHtmlDownloadId = await downloadBlob(htmlDownloadResource.url, htmlFilename);
    const finalJsonDownloadId = await downloadBlob(jsonDownloadResource.url, jsonFilename);
    await Promise.all([
      waitForDownload(finalHtmlDownloadId, htmlFilename),
      waitForDownload(finalJsonDownloadId, jsonFilename),
    ]);

    logInfo("Final downloads completed.", {
      finalHtmlDownloadId,
      finalJsonDownloadId,
      basename,
    });

    await removeDownloadedFile(htmlPartDownloadId, htmlPartFilename);
    await removeDownloadedFile(jsonPartDownloadId, jsonPartFilename);
  } finally {
    await releaseDownloadResource(htmlDownloadResource);
    await releaseDownloadResource(jsonDownloadResource);
  }

  logInfo("Extraction completed successfully.", {
    basename,
    rootPrefix: ROOT_PREFIX,
  });

  return basename;
}

function buildCaptureBasename(result) {
  if (result.sidecar.capture_format === "navis-chapter-bundle/v1") {
    return buildNavisCaptureBasename(result.sidecar);
  }

  const timestamp = result.sidecar.captured_at.replace(/[-:]/g, "").replace(/\.\d{3}Z$/, "Z");
  const candidate = deriveSlug(result.sidecar.canonical_url, result.sidecar.title);
  return `${timestamp}--${candidate}`;
}

function buildNavisCaptureBasename(sidecar) {
  const timestamp = sidecar.captured_at.replace(/[-:]/g, "").replace(/\.\d{3}Z$/, "Z");
  const productKey = sanitizeFilenameComponent(sidecar.product_key || "NAVIS");
  const chapterRefId = sanitizeFilenameComponent(sidecar.chapter_ref_id || "document");
  const chapterTitle = sanitizeChapterTitleForFilename(sidecar.chapter_title || sidecar.title || "CHAPITRE");
  return `${timestamp}--navis-${productKey}-${chapterRefId}--${chapterTitle}`;
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

export function sanitizeFilenameComponent(value) {
  return String(value)
    .normalize("NFKD")
    .replace(/[^A-Za-z0-9_-]+/g, "-")
    .replace(/^-+|-+$/g, "") || "document";
}

export function sanitizeChapterTitleForFilename(value) {
  return String(value)
    .normalize("NFKD")
    .replace(/\s+/g, "_")
    .replace(/[^A-Za-z0-9_-]+/g, "_")
    .replace(/_+/g, "_")
    .replace(/^_+|_+$/g, "") || "CHAPITRE";
}

function isNavigationTargetReached(currentUrl, targetUrl, expectedRefId = null) {
  if (currentUrl === undefined || currentUrl === null) {
    return false;
  }

  if (expectedRefId !== null) {
    return getQueryParamValue(currentUrl, "refId") === expectedRefId;
  }

  if (getSourceFamily(currentUrl) === "ifrs" && getSourceFamily(targetUrl) === "ifrs") {
    const targetToken = extractIfrsDocumentNavigationToken(targetUrl);
    if (!targetToken) {
      return currentUrl === targetUrl;
    }
    try {
      const currentPathname = new URL(currentUrl).pathname;
      return currentPathname.includes(`/${targetToken}/`) || currentPathname.includes(`/${targetToken}.html`);
    } catch {
      return currentUrl.includes(`/${targetToken}/`) || currentUrl.includes(`/${targetToken}.html`);
    }
  }

  return currentUrl === targetUrl;
}

export function getQueryParamValue(url, key) {
  try {
    return new URL(url).searchParams.get(key);
  } catch {
    return null;
  }
}

async function createDownloadResource(content, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  if (typeof URL.createObjectURL === "function") {
    const url = URL.createObjectURL(blob);
    logInfo("Created blob download URL.", {
      mimeType,
      byteLength: blob.size,
      strategy: "blob-url",
    });
    return {
      url,
      strategy: "blob-url",
    };
  }

  const bytes = new TextEncoder().encode(content);
  const base64 = bytesToBase64(bytes);
  const downloadUrl = `data:${mimeType};base64,${base64}`;
  logInfo("Created data download URL.", {
    mimeType,
    byteLength: bytes.byteLength,
    urlLength: downloadUrl.length,
    strategy: "data-url",
  });
  return {
    url: downloadUrl,
    strategy: "data-url",
  };
}

async function releaseDownloadResource(resource) {
  if (resource.strategy === "blob-url") {
    URL.revokeObjectURL(resource.url);
    logInfo("Revoked blob download URL.", {
      strategy: resource.strategy,
    });
  }
}

function bytesToBase64(bytes) {
  const chunkSize = 0x8000;
  let binary = "";

  for (let offset = 0; offset < bytes.length; offset += chunkSize) {
    const chunk = bytes.subarray(offset, offset + chunkSize);
    binary += String.fromCharCode(...chunk);
  }

  return btoa(binary);
}

async function downloadBlob(blobUrl, filename) {
  const downloadId = await chrome.downloads.download({
    url: blobUrl,
    filename,
    saveAs: false,
    conflictAction: "uniquify",
  });

  logInfo("Started download.", { downloadId, filename });
  return downloadId;
}

function waitForDownload(downloadId, filename) {
  return new Promise((resolve, reject) => {
    const listener = (delta) => {
      if (delta.id !== downloadId || delta.state === undefined) {
        return;
      }

      if (delta.state.current === "complete") {
        chrome.downloads.onChanged.removeListener(listener);
        logInfo("Download completed.", { downloadId, filename });
        resolve();
      }

      if (delta.state.current === "interrupted") {
        chrome.downloads.onChanged.removeListener(listener);
        const error = new Error(`Download ${downloadId} for ${filename} was interrupted`);
        logError("Download interrupted.", {
          downloadId,
          filename,
          interruptReason: delta.error?.current,
        });
        reject(error);
      }
    };

    chrome.downloads.onChanged.addListener(listener);
  });
}

async function removeDownloadedFile(downloadId, filename) {
  try {
    await chrome.downloads.removeFile(downloadId);
    logInfo("Removed temporary download.", { downloadId, filename });
  } catch (error) {
    logWarn("Unable to remove temporary download.", {
      downloadId,
      filename,
      error: formatErrorMessage(error),
    });
  }
}

export async function showToastInTab(tabId, message, tone) {
  try {
    await chrome.scripting.executeScript({
      target: { tabId },
      func: showPageToast,
      args: [message, tone, PAGE_TOAST_DURATION_MS],
    });
    logInfo("Displayed page toast.", { tabId, tone, message });
  } catch (error) {
    logWarn("Unable to display page toast.", {
      tabId,
      tone,
      message,
      error: formatErrorMessage(error),
    });
  }
}

function showPageToast(message, tone, durationMs) {
  const toastId = "ifrs-expert-import-toast";
  const existingToast = document.getElementById(toastId);
  if (existingToast !== null) {
    existingToast.remove();
  }

  const mountNode = document.body ?? document.documentElement;
  if (mountNode === null) {
    console.warn("[IFRS Expert Extract] Unable to display toast because the page has no mount node.");
    return;
  }

  const toast = document.createElement("div");
  toast.id = toastId;
  toast.setAttribute("role", "status");
  toast.setAttribute("aria-live", "polite");
  toast.textContent = message;

  const backgroundColor = tone === "success"
    ? "#166534"
    : tone === "info"
      ? "#1d4ed8"
      : "#b91c1c";
  toast.style.position = "fixed";
  toast.style.top = "20px";
  toast.style.right = "20px";
  toast.style.zIndex = "2147483647";
  toast.style.maxWidth = "420px";
  toast.style.padding = "12px 16px";
  toast.style.borderRadius = "10px";
  toast.style.background = backgroundColor;
  toast.style.color = "#ffffff";
  toast.style.fontFamily = "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif";
  toast.style.fontSize = "14px";
  toast.style.lineHeight = "1.4";
  toast.style.boxShadow = "0 10px 30px rgba(0, 0, 0, 0.25)";

  mountNode.appendChild(toast);
  console.info("[IFRS Expert Extract] Toast displayed in page.", { tone, message });

  window.setTimeout(() => {
    toast.remove();
  }, durationMs);
}

export function escapeScriptJson(value) {
  return value.replace(/<\//g, "<\\/");
}

export function escapeHtmlAttribute(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

export function escapeHtmlText(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

export function formatErrorMessage(error) {
  if (error instanceof Error) {
    return error.message;
  }

  if (typeof error === "string") {
    return error;
  }

  try {
    return JSON.stringify(error);
  } catch {
    return String(error);
  }
}

export function runTask(taskName, task) {
  void task().catch((error) => {
    logError("Background task failed.", {
      taskName,
      error: formatErrorMessage(error),
    });
  });
}

export function isSupportedTabUrl(tabUrl) {
  if (tabUrl === undefined) {
    return false;
  }

  try {
    const url = new URL(tabUrl);
    if (url.protocol !== "https:") {
      return false;
    }
    return isSupportedHostname(url.hostname);
  } catch {
    return false;
  }
}

function isSupportedHostname(hostname) {
  return hostname === "ifrs.org" || hostname.endsWith(".ifrs.org") || hostname === "abonnes.efl.fr";
}

export function getSourceFamily(tabUrl) {
  try {
    const hostname = new URL(tabUrl).hostname;
    if (hostname === "abonnes.efl.fr") {
      return "navis";
    }
    if (hostname === "ifrs.org" || hostname.endsWith(".ifrs.org")) {
      return "ifrs";
    }
  } catch {
    return "unknown";
  }

  return "unknown";
}

export function logInfo(message, details = undefined) {
  if (details === undefined) {
    console.info(LOG_PREFIX, message);
    return;
  }

  console.info(LOG_PREFIX, message, details);
}

export function logWarn(message, details = undefined) {
  if (details === undefined) {
    console.warn(LOG_PREFIX, message);
    return;
  }

  console.warn(LOG_PREFIX, message, details);
}

export function logError(message, details = undefined) {
  if (details === undefined) {
    console.error(LOG_PREFIX, message);
    return;
  }

  console.error(LOG_PREFIX, message, details);
}
