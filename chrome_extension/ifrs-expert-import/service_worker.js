const LOG_PREFIX = "[IFRS Expert Import]";
const INBOX_PREFIX = "ifrs-expert/inbox";
const HTML_MIME_TYPE = "text/html;charset=utf-8";
const JSON_MIME_TYPE = "application/json;charset=utf-8";
const PAGE_TOAST_DURATION_MS = 4000;
const SUPPORTED_ICON_COLOR = "#b30938";
const UNSUPPORTED_ICON_COLOR = "#9ca3af";
const ICON_SIZES = [16, 24, 32];
const ACTION_TITLE = "Import to IFRS Expert";
const UNSUPPORTED_ACTION_TITLE = "Import to IFRS Expert (available only on ifrs.org)";
const ACTION_ICON_CACHE = new Map();

chrome.runtime.onInstalled.addListener(() => {
  runTask("runtime.onInstalled", () => initializeActionState("runtime.onInstalled"));
});

chrome.runtime.onStartup.addListener(() => {
  runTask("runtime.onStartup", () => initializeActionState("runtime.onStartup"));
});

chrome.tabs.onActivated.addListener(({ tabId }) => {
  runTask("tabs.onActivated", () => updateActionForTabId(tabId, "tabs.onActivated"));
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === undefined && changeInfo.url === undefined) {
    return;
  }

  runTask("tabs.onUpdated", () => syncActionStateForTab(tabId, tab.url ?? changeInfo.url, "tabs.onUpdated"));
});

chrome.windows.onFocusChanged.addListener((windowId) => {
  if (windowId === chrome.windows.WINDOW_ID_NONE) {
    return;
  }

  runTask("windows.onFocusChanged", () => refreshActiveTabActionState("windows.onFocusChanged"));
});

chrome.action.onClicked.addListener(async (tab) => {
  logInfo("Toolbar action clicked", { tabId: tab.id, url: tab.url });

  if (tab.id === undefined) {
    logWarn("Ignoring click because tab.id is undefined.");
    return;
  }

  if (!isSupportedTabUrl(tab.url)) {
    logWarn("Ignoring click on unsupported URL.", { tabId: tab.id, url: tab.url });
    return;
  }

  const blobUrls = [];

  try {
    logInfo("Starting rendered page capture.", { tabId: tab.id, url: tab.url });
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: captureRenderedPage,
    });

    logInfo("Captured page successfully.", {
      tabId: tab.id,
      canonicalUrl: result.sidecar.canonical_url,
      title: result.sidecar.title,
      htmlLength: result.html.length,
    });

    const basename = buildCaptureBasename(result);
    const htmlPartFilename = `${INBOX_PREFIX}/${basename}.html.part`;
    const jsonPartFilename = `${INBOX_PREFIX}/${basename}.json.part`;
    const htmlFilename = `${INBOX_PREFIX}/${basename}.html`;
    const jsonFilename = `${INBOX_PREFIX}/${basename}.json`;

    logInfo("Prepared filenames.", {
      basename,
      htmlPartFilename,
      jsonPartFilename,
      htmlFilename,
      jsonFilename,
    });

    const htmlBlobUrl = createBlobUrl(blobUrls, result.html, HTML_MIME_TYPE);
    const jsonBlobUrl = createBlobUrl(blobUrls, JSON.stringify(result.sidecar, null, 2), JSON_MIME_TYPE);

    const htmlPartDownloadId = await downloadBlob(htmlBlobUrl, htmlPartFilename);
    const jsonPartDownloadId = await downloadBlob(jsonBlobUrl, jsonPartFilename);
    await Promise.all([
      waitForDownload(htmlPartDownloadId, htmlPartFilename),
      waitForDownload(jsonPartDownloadId, jsonPartFilename),
    ]);

    logInfo("Temporary downloads completed.", {
      htmlPartDownloadId,
      jsonPartDownloadId,
      basename,
    });

    const finalHtmlBlobUrl = createBlobUrl(blobUrls, result.html, HTML_MIME_TYPE);
    const finalJsonBlobUrl = createBlobUrl(
      blobUrls,
      JSON.stringify(result.sidecar, null, 2),
      JSON_MIME_TYPE,
    );

    const finalHtmlDownloadId = await downloadBlob(finalHtmlBlobUrl, htmlFilename);
    const finalJsonDownloadId = await downloadBlob(finalJsonBlobUrl, jsonFilename);
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

    logInfo("Import completed successfully.", {
      basename,
      inboxPrefix: INBOX_PREFIX,
    });

    await showToastInTab(tab.id, `Saved ${basename}.html and ${basename}.json`, "success");
  } catch (error) {
    const errorMessage = formatErrorMessage(error);
    logError("IFRS Expert import failed.", {
      tabId: tab.id,
      url: tab.url,
      error: errorMessage,
    });
    await showToastInTab(tab.id, `Import failed: ${errorMessage}`, "error");
  } finally {
    for (const blobUrl of blobUrls) {
      URL.revokeObjectURL(blobUrl);
    }

    logInfo("Revoked temporary blob URLs.", { count: blobUrls.length });
  }
});

async function initializeActionState(reason) {
  logInfo("Initializing action state.", { reason });
  await chrome.action.setIcon({ imageData: getActionIconImageData(UNSUPPORTED_ICON_COLOR) });
  await chrome.action.setTitle({ title: UNSUPPORTED_ACTION_TITLE });
  await chrome.action.disable();
  await refreshActiveTabActionState(reason);
}

async function refreshActiveTabActionState(reason) {
  const tabs = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
  const activeTab = tabs.at(0);

  if (activeTab?.id === undefined) {
    logWarn("No active tab was available while refreshing action state.", { reason });
    return;
  }

  await syncActionStateForTab(activeTab.id, activeTab.url, reason);
}

async function updateActionForTabId(tabId, reason) {
  const tab = await chrome.tabs.get(tabId);
  await syncActionStateForTab(tabId, tab.url, reason);
}

async function syncActionStateForTab(tabId, tabUrl, reason) {
  const supported = isSupportedTabUrl(tabUrl);
  const iconColor = supported ? SUPPORTED_ICON_COLOR : UNSUPPORTED_ICON_COLOR;
  const title = supported ? ACTION_TITLE : UNSUPPORTED_ACTION_TITLE;

  await chrome.action.setIcon({
    tabId,
    imageData: getActionIconImageData(iconColor),
  });
  await chrome.action.setTitle({ tabId, title });

  if (supported) {
    await chrome.action.enable(tabId);
  } else {
    await chrome.action.disable(tabId);
  }

  logInfo("Updated action presentation.", {
    tabId,
    tabUrl,
    supported,
    enabled: supported,
    reason,
  });
}

function captureRenderedPage() {
  const canonicalUrl = document.querySelector('link[rel="canonical"]')?.href ?? window.location.href;
  const title = document.title || canonicalUrl;

  console.info("[IFRS Expert Import] Capturing page in tab.", {
    url: window.location.href,
    canonicalUrl,
    title,
  });

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

function createBlobUrl(blobUrls, content, mimeType) {
  const blobUrl = URL.createObjectURL(new Blob([content], { type: mimeType }));
  blobUrls.push(blobUrl);
  logInfo("Created blob URL.", { mimeType, blobUrlCount: blobUrls.length });
  return blobUrl;
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

async function showToastInTab(tabId, message, tone) {
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
    console.warn("[IFRS Expert Import] Unable to display toast because the page has no mount node.");
    return;
  }

  const toast = document.createElement("div");
  toast.id = toastId;
  toast.setAttribute("role", "status");
  toast.setAttribute("aria-live", "polite");
  toast.textContent = message;

  const backgroundColor = tone === "success" ? "#166534" : "#b91c1c";
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
  console.info("[IFRS Expert Import] Toast displayed in page.", { tone, message });

  window.setTimeout(() => {
    toast.remove();
  }, durationMs);
}

function getActionIconImageData(color) {
  const cached = ACTION_ICON_CACHE.get(color);
  if (cached !== undefined) {
    return cached;
  }

  const imageData = {};
  for (const size of ICON_SIZES) {
    imageData[size] = createActionIconImageData(size, color);
  }

  ACTION_ICON_CACHE.set(color, imageData);
  return imageData;
}

function createActionIconImageData(size, color) {
  const canvas = new OffscreenCanvas(size, size);
  const context = canvas.getContext("2d");
  if (context === null) {
    throw new Error("Unable to create icon drawing context.");
  }

  const scale = size / 16;
  context.clearRect(0, 0, size, size);
  context.fillStyle = color;
  drawRoundedRect(context, 2 * scale, 2 * scale, 12 * scale, 12 * scale, 3 * scale);
  context.fill();

  context.strokeStyle = "#ffffff";
  context.lineWidth = Math.max(1.5 * scale, 1);
  context.lineCap = "round";
  context.lineJoin = "round";

  context.beginPath();
  context.moveTo(8 * scale, 4.5 * scale);
  context.lineTo(8 * scale, 9 * scale);
  context.moveTo(6 * scale, 7.25 * scale);
  context.lineTo(8 * scale, 9.5 * scale);
  context.lineTo(10 * scale, 7.25 * scale);
  context.moveTo(5 * scale, 11.25 * scale);
  context.lineTo(11 * scale, 11.25 * scale);
  context.stroke();

  return context.getImageData(0, 0, size, size);
}

function drawRoundedRect(context, x, y, width, height, radius) {
  context.beginPath();
  context.moveTo(x + radius, y);
  context.lineTo(x + width - radius, y);
  context.quadraticCurveTo(x + width, y, x + width, y + radius);
  context.lineTo(x + width, y + height - radius);
  context.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
  context.lineTo(x + radius, y + height);
  context.quadraticCurveTo(x, y + height, x, y + height - radius);
  context.lineTo(x, y + radius);
  context.quadraticCurveTo(x, y, x + radius, y);
  context.closePath();
}

function formatErrorMessage(error) {
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

function runTask(taskName, task) {
  void task().catch((error) => {
    logError("Background task failed.", {
      taskName,
      error: formatErrorMessage(error),
    });
  });
}

function isSupportedTabUrl(tabUrl) {
  if (tabUrl === undefined) {
    return false;
  }

  try {
    const url = new URL(tabUrl);
    return url.protocol === "https:" && (url.hostname === "ifrs.org" || url.hostname.endsWith(".ifrs.org"));
  } catch {
    return false;
  }
}

function logInfo(message, details = undefined) {
  if (details === undefined) {
    console.info(LOG_PREFIX, message);
    return;
  }

  console.info(LOG_PREFIX, message, details);
}

function logWarn(message, details = undefined) {
  if (details === undefined) {
    console.warn(LOG_PREFIX, message);
    return;
  }

  console.warn(LOG_PREFIX, message, details);
}

function logError(message, details = undefined) {
  if (details === undefined) {
    console.error(LOG_PREFIX, message);
    return;
  }

  console.error(LOG_PREFIX, message, details);
}
