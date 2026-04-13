const LOG_PREFIX = "[IFRS Expert Import]";
const ROOT_PREFIX = "ifrs-expert";
const HTML_MIME_TYPE = "text/html;charset=utf-8";
const JSON_MIME_TYPE = "application/json;charset=utf-8";
const PAGE_TOAST_DURATION_MS = 4000;
const ACTION_TITLE = "Import to IFRS Expert";
const UNSUPPORTED_ACTION_TITLE = "Import to IFRS Expert (available only on supported sources)";
const NAVIS_ROOT_ACTION_TITLE = "Import all chapters to IFRS Expert";
const NAVIS_CHAPTER_ACTION_TITLE = "Import this chapter to IFRS Expert";
const NAVIS_UNSUPPORTED_ACTION_TITLE = "Import available only on Navis root or CHAPITRE nodes";
const NAVIS_ROOT_REF_ID = "N24F9F491387ED-EFL";
const NAVIS_BUNDLE_CAPTURE_FORMAT = "navis-chapter-bundle/v1";
const NAVIS_SECTION_LOAD_DELAY_MS = 1000;
const NAVIS_PAGE_TASK_MAX_ATTEMPTS = 3;
const NAVIS_PAGE_TASK_RETRY_DELAY_MS = 750;
const SUPPORTED_ACTION_ICON_PATHS = {
  16: "icons/ifrs-red-16.png",
  24: "icons/ifrs-red-24.png",
  32: "icons/ifrs-red-32.png",
};
const UNSUPPORTED_ACTION_ICON_PATHS = {
  16: "icons/ifrs-grey-16.png",
  24: "icons/ifrs-grey-24.png",
  32: "icons/ifrs-grey-32.png",
};

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

  const sourceFamily = getSourceFamily(tab.url);
  if (sourceFamily === "unknown") {
    logWarn("Ignoring click on unsupported URL.", { tabId: tab.id, url: tab.url });
    return;
  }

  try {
    if (sourceFamily === "navis") {
      await captureNavisImport(tab.id, tab.url ?? "");
      return;
    }

    await captureStandardRenderedPage(tab.id, tab.url ?? "");
  } catch (error) {
    const errorMessage = formatErrorMessage(error);
    logError("IFRS Expert import failed.", {
      tabId: tab.id,
      url: tab.url,
      error: errorMessage,
    });
    await showToastInTab(tab.id, `Import failed: ${errorMessage}`, "error");
  } finally {
    logInfo("Import attempt finished.");
  }
});

async function initializeActionState(reason) {
  logInfo("Initializing action state.", { reason });
  await chrome.action.setIcon({ path: UNSUPPORTED_ACTION_ICON_PATHS });
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
  const actionState = await resolveActionState(tabId, tabUrl);

  await chrome.action.setIcon({
    tabId,
    path: actionState.iconPaths,
  });
  await chrome.action.setTitle({ tabId, title: actionState.title });

  if (actionState.enabled) {
    await chrome.action.enable(tabId);
  } else {
    await chrome.action.disable(tabId);
  }

  logInfo("Updated action presentation.", {
    tabId,
    tabUrl,
    sourceFamily: actionState.sourceFamily,
    supported: actionState.enabled,
    enabled: actionState.enabled,
    reason,
    mode: actionState.mode,
  });
}

async function resolveActionState(tabId, tabUrl) {
  if (!isSupportedTabUrl(tabUrl)) {
    return {
      enabled: false,
      title: UNSUPPORTED_ACTION_TITLE,
      iconPaths: UNSUPPORTED_ACTION_ICON_PATHS,
      sourceFamily: "unknown",
      mode: "unsupported",
    };
  }

  const sourceFamily = getSourceFamily(tabUrl);
  if (sourceFamily === "ifrs") {
    return {
      enabled: true,
      title: ACTION_TITLE,
      iconPaths: SUPPORTED_ACTION_ICON_PATHS,
      sourceFamily,
      mode: "page",
    };
  }

  const urlMode = getNavisActionModeFromUrl(tabUrl);

  try {
    const context = await executeNavisPageTask(tabId, { type: "inspectContext" });
    if (context.mode === "root") {
      return {
        enabled: true,
        title: NAVIS_ROOT_ACTION_TITLE,
        iconPaths: SUPPORTED_ACTION_ICON_PATHS,
        sourceFamily,
        mode: context.mode,
      };
    }
    if (context.mode === "chapter") {
      return {
        enabled: true,
        title: NAVIS_CHAPTER_ACTION_TITLE,
        iconPaths: SUPPORTED_ACTION_ICON_PATHS,
        sourceFamily,
        mode: context.mode,
      };
    }
  } catch (error) {
    logWarn("Unable to inspect Navis page state while resolving action state.", {
      tabId,
      tabUrl,
      error: formatErrorMessage(error),
    });
  }

  if (urlMode === "root") {
    return {
      enabled: true,
      title: NAVIS_ROOT_ACTION_TITLE,
      iconPaths: SUPPORTED_ACTION_ICON_PATHS,
      sourceFamily,
      mode: urlMode,
    };
  }
  if (urlMode === "chapter") {
    return {
      enabled: true,
      title: NAVIS_CHAPTER_ACTION_TITLE,
      iconPaths: SUPPORTED_ACTION_ICON_PATHS,
      sourceFamily,
      mode: urlMode,
    };
  }

  return {
    enabled: false,
    title: NAVIS_UNSUPPORTED_ACTION_TITLE,
    iconPaths: UNSUPPORTED_ACTION_ICON_PATHS,
    sourceFamily,
    mode: "unsupported",
  };
}

async function captureStandardRenderedPage(tabId, tabUrl) {
  logInfo("Starting rendered page capture.", { tabId, url: tabUrl });
  const result = await executePageCaptureTask(tabId, captureRenderedPage);

  logInfo("Captured page successfully.", {
    tabId,
    canonicalUrl: result.sidecar.canonical_url,
    title: result.sidecar.title,
    sourceFamily: getSourceFamily(result.sidecar.url),
    htmlLength: result.html.length,
  });

  const basename = await downloadCaptureArtifacts(result);
  await showToastInTab(tabId, `Saved ${basename}.html and ${basename}.json`, "success");
}

async function captureNavisImport(tabId, tabUrl) {
  const urlMode = getNavisActionModeFromUrl(tabUrl);
  let context = null;

  try {
    context = await executeNavisPageTask(tabId, { type: "inspectContext" });
  } catch (error) {
    logWarn("Unable to inspect Navis page state while starting capture; falling back to URL mode.", {
      tabId,
      tabUrl,
      error: formatErrorMessage(error),
    });
  }

  const effectiveMode = context?.mode === "root" || context?.mode === "chapter"
    ? context.mode
    : urlMode;
  const effectiveSelectedRefId = context?.selectedRefId || getNavisRefIdFromUrl(tabUrl) || "";
  const effectiveSelectedTitle = context?.selectedTitle || "";
  const effectiveProductKey = context?.productKey || getQueryParamValue(tabUrl, "key") || "";

  if (effectiveMode !== "root" && effectiveMode !== "chapter") {
    throw new Error("Navis import is available only on the root node or a CHAPITRE node");
  }

  const discoveredChapterTargets = effectiveMode === "root"
    ? await discoverNavisRootChapterTargets(tabId)
    : [{ refId: effectiveSelectedRefId, title: effectiveSelectedTitle }];

  const chapterTargets = [];
  let skippedChapterCount = 0;
  for (const chapterTarget of discoveredChapterTargets) {
    const alreadyDownloaded = effectiveMode === "root"
      ? await navisChapterCaptureExists(effectiveProductKey, chapterTarget.refId)
      : false;
    if (alreadyDownloaded) {
      skippedChapterCount += 1;
      logInfo("Skipping already-downloaded Navis chapter in root-batch mode.", {
        tabId,
        chapterRefId: chapterTarget.refId,
        chapterTitle: chapterTarget.title,
      });
      continue;
    }
    chapterTargets.push(chapterTarget);
  }

  if (chapterTargets.length === 0) {
    if (effectiveMode === "root") {
      throw new Error("No remaining CHAPITRE nodes need downloading in root-batch mode");
    }
    throw new Error("No CHAPITRE nodes were found in the Navis TOC");
  }

  const batchMode = effectiveMode === "root" ? "root-batch" : "chapter";
  const savedBasenames = [];
  const baseUrl = tabUrl;

  logInfo("Starting Navis chapter capture.", {
    tabId,
    mode: batchMode,
    discoveredChapterCount: discoveredChapterTargets.length,
    skippedChapterCount,
    chapterCount: chapterTargets.length,
    rootRefId: NAVIS_ROOT_REF_ID,
  });

  for (const [chapterIndex, chapterTarget] of chapterTargets.entries()) {
    logInfo("Capturing Navis chapter.", {
      tabId,
      chapterIndex: chapterIndex + 1,
      chapterCount: chapterTargets.length,
      chapterRefId: chapterTarget.refId,
      chapterTitle: chapterTarget.title,
    });

    const capture = await captureNavisChapter(tabId, {
      baseUrl,
      rootRefId: NAVIS_ROOT_REF_ID,
      productKey: effectiveProductKey,
      chapterRefId: chapterTarget.refId,
      chapterTitle: chapterTarget.title,
      captureMode: batchMode,
    });
    const basename = await downloadCaptureArtifacts(capture);
    savedBasenames.push(basename);
  }

  const summaryMessage = savedBasenames.length === 1
    ? `Saved ${savedBasenames[0]}.html and ${savedBasenames[0]}.json`
    : `Saved ${savedBasenames.length} chapter captures to ${ROOT_PREFIX}/`;
  await showToastInTab(tabId, summaryMessage, "success");
}

async function discoverNavisRootChapterTargets(tabId) {
  const discovery = await executeNavisPageTask(tabId, { type: "discoverChapters" });
  if (!Array.isArray(discovery.chapters)) {
    throw new Error("Navis chapter discovery did not return a chapter list");
  }
  return discovery.chapters;
}

async function captureNavisChapter(tabId, options) {
  const chapterUrl = buildNavisDocumentUrl(options.baseUrl, options.chapterRefId);
  await navigateTabToUrl(tabId, chapterUrl, options.chapterRefId);
  await sleepMs(NAVIS_SECTION_LOAD_DELAY_MS);

  const chapterDiscovery = await executeNavisPageTaskWithRetry(tabId, {
    type: "discoverChapterLeafTargets",
    chapterRefId: options.chapterRefId,
  });
  if (chapterDiscovery === null || chapterDiscovery === undefined) {
    throw new Error(`Navis chapter discovery returned no result for chapterRefId=${options.chapterRefId}`);
  }
  const pageTargets = Array.isArray(chapterDiscovery.pageTargets) ? chapterDiscovery.pageTargets : [];
  const effectiveChapterTitle = chapterDiscovery.chapterTitle || options.chapterTitle;
  const effectiveProductKey = chapterDiscovery.productKey || options.productKey || getQueryParamValue(chapterUrl, "key") || "NAVIS";
  const effectiveChapterUrl = chapterDiscovery.chapterUrl || chapterUrl;

  const pageFragments = [];
  if (pageTargets.length === 0) {
    logWarn("No Navis leaf targets were found for chapter; capturing the current chapter page as a fallback.", {
      tabId,
      chapterRefId: options.chapterRefId,
      chapterTitle: effectiveChapterTitle,
    });
    const fragment = await executeNavisPageTaskWithRetry(tabId, {
      type: "captureCurrentFragment",
      expectedRefId: options.chapterRefId,
    });
    pageFragments.push(fragment);
  } else {
    for (const [pageIndex, pageTarget] of pageTargets.entries()) {
      logInfo("Capturing Navis page fragment.", {
        tabId,
        chapterRefId: options.chapterRefId,
        pageIndex: pageIndex + 1,
        pageCount: pageTargets.length,
        pageRefId: pageTarget.refId,
        pageTitle: pageTarget.title,
      });
      const pageUrl = buildNavisDocumentUrl(options.baseUrl, pageTarget.refId);
      await navigateTabToUrl(tabId, pageUrl, pageTarget.refId);
      await sleepMs(NAVIS_SECTION_LOAD_DELAY_MS);
      const fragment = await executeNavisPageTaskWithRetry(tabId, {
        type: "captureCurrentFragment",
        expectedRefId: pageTarget.refId,
      });
      pageFragments.push(fragment);
    }
  }

  const pageRefIds = pageFragments.map((fragment) => fragment.pageRefId);
  const pageTitles = pageFragments.map((fragment) => fragment.pageTitle);
  const sidecar = {
    url: effectiveChapterUrl,
    title: effectiveChapterTitle,
    captured_at: new Date().toISOString().replace(/\.\d{3}Z$/, "Z"),
    source_domain: "abonnes.efl.fr",
    canonical_url: effectiveChapterUrl,
    extension_version: chrome.runtime.getManifest().version,
    content_type: "text/html",
    capture_format: NAVIS_BUNDLE_CAPTURE_FORMAT,
    capture_mode: options.captureMode,
    product_key: effectiveProductKey,
    root_ref_id: options.rootRefId,
    chapter_ref_id: options.chapterRefId,
    chapter_title: effectiveChapterTitle,
    page_ref_ids: pageRefIds,
    page_titles: pageTitles,
  };

  return {
    html: buildNavisChapterBundleHtml(sidecar, pageFragments),
    sidecar,
  };
}

function buildNavisChapterBundleHtml(sidecar, pageFragments) {
  const manifest = {
    capture_format: sidecar.capture_format,
    capture_mode: sidecar.capture_mode,
    product_key: sidecar.product_key,
    root_ref_id: sidecar.root_ref_id,
    chapter_ref_id: sidecar.chapter_ref_id,
    chapter_title: sidecar.chapter_title,
    page_ref_ids: sidecar.page_ref_ids,
    page_titles: sidecar.page_titles,
  };
  const manifestJson = escapeScriptJson(JSON.stringify(manifest, null, 2));
  const pageSections = pageFragments.map((fragment) => {
    const pageRefId = escapeHtmlAttribute(fragment.pageRefId);
    const pageTitle = escapeHtmlAttribute(fragment.pageTitle);
    const pageUrl = escapeHtmlAttribute(fragment.url);
    return [
      `<section class="ifrs-expert-navis-page" data-page-ref-id="${pageRefId}" data-page-title="${pageTitle}" data-page-url="${pageUrl}">`,
      fragment.fragmentHtml,
      "</section>",
    ].join("\n");
  }).join("\n");

  return [
    "<!DOCTYPE html>",
    `<html data-ifrs-expert-source="navis" data-ifrs-expert-capture="chapter-bundle">`,
    "<head>",
    '  <meta charset="utf-8">',
    `  <title>${escapeHtmlText(sidecar.chapter_title)}</title>`,
    "</head>",
    "<body>",
    `  <script id="ifrs-expert-navis-manifest" type="application/json">${manifestJson}</script>`,
    `  <div id="ifrs-expert-navis-bundle" data-chapter-ref-id="${escapeHtmlAttribute(sidecar.chapter_ref_id)}">`,
    pageSections,
    "  </div>",
    "</body>",
    "</html>",
  ].join("\n");
}

async function downloadCaptureArtifacts(result) {
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

  logInfo("Import completed successfully.", {
    basename,
    rootPrefix: ROOT_PREFIX,
  });

  return basename;
}

async function executePageCaptureTask(tabId, taskFunction) {
  const [{ result }] = await chrome.scripting.executeScript({
    target: { tabId },
    func: taskFunction,
  });
  return result;
}

async function executeNavisPageTask(tabId, task) {
  const injectionResults = await chrome.scripting.executeScript({
    target: { tabId },
    func: runNavisPageTask,
    args: [task],
  });
  const firstResult = injectionResults.at(0);
  if (firstResult === undefined) {
    throw new Error(`Navis page task returned no injection result for task=${task.type}`);
  }
  return firstResult.result;
}

async function executeNavisPageTaskWithRetry(tabId, task) {
  let lastError = null;
  for (let attempt = 1; attempt <= NAVIS_PAGE_TASK_MAX_ATTEMPTS; attempt += 1) {
    try {
      const result = await executeNavisPageTask(tabId, task);
      if (result !== null && result !== undefined) {
        return result;
      }
      throw new Error(`Navis page task returned an empty result for task=${task.type}`);
    } catch (error) {
      lastError = error;
      logWarn("Navis page task attempt failed.", {
        tabId,
        taskType: task.type,
        attempt,
        maxAttempts: NAVIS_PAGE_TASK_MAX_ATTEMPTS,
        error: formatErrorMessage(error),
      });
      if (attempt < NAVIS_PAGE_TASK_MAX_ATTEMPTS) {
        await sleepMs(NAVIS_PAGE_TASK_RETRY_DELAY_MS);
      }
    }
  }
  throw lastError;
}

function sleepMs(durationMs) {
  return new Promise((resolve) => {
    setTimeout(resolve, durationMs);
  });
}

async function navigateTabToUrl(tabId, url, expectedRefId = null) {
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

async function runNavisPageTask(task) {
  const navisRootRefId = "N24F9F491387ED-EFL";
  const questionSelector = "#documentContent .question.question-export";

  function normalizeWhitespace(value) {
    return (value ?? "").replace(/\s+/g, " ").trim();
  }

  function getTitleAnchorText(anchor) {
    return normalizeWhitespace(anchor.getAttribute("title") || anchor.textContent || "");
  }

  function getTocTitleAnchors() {
    return Array.from(document.querySelectorAll("#tocTree a[data-ref-id][id]"));
  }

  function getTitleAnchorByRefId(refId) {
    return getTocTitleAnchors().find((anchor) => anchor.dataset.refId === refId) ?? null;
  }

  function getTitleAnchorById(anchorId) {
    return getTocTitleAnchors().find((anchor) => anchor.id === anchorId) ?? null;
  }

  function getSelectedTitleAnchor() {
    return document.querySelector("#tocTree a.lienSommaireSelected[data-ref-id], #sommaire a.lienSommaireSelected[data-ref-id]")
      ?? document.querySelector("#tocTree li.liSommaireSelected a[data-ref-id][id], #sommaire li.liSommaireSelected a[data-ref-id][id]");
  }

  function getNodePrefixElement(titleAnchor) {
    return titleAnchor.previousElementSibling;
  }

  function getNodeToggleAnchor(titleAnchor) {
    const prefixElement = getNodePrefixElement(titleAnchor);
    if (prefixElement === null || prefixElement.tagName !== "A") {
      return null;
    }
    if (!prefixElement.classList.contains("closed") && !prefixElement.classList.contains("opened")) {
      return null;
    }
    return prefixElement;
  }

  function isLeafNode(titleAnchor) {
    const prefixElement = getNodePrefixElement(titleAnchor);
    return prefixElement !== null && prefixElement.tagName === "SPAN" && prefixElement.classList.contains("nochild");
  }

  function isChapterNode(titleAnchor) {
    return getTitleAnchorText(titleAnchor).startsWith("CHAPITRE ");
  }

  function isRootNode(titleAnchor) {
    return titleAnchor.dataset.refId === navisRootRefId;
  }

  function buildAnchorPrefixes(anchorId) {
    const parts = anchorId.split("-");
    const prefixes = [];
    for (let index = 0; index < parts.length; index += 1) {
      prefixes.push(parts.slice(0, index + 1).join("-"));
    }
    return prefixes;
  }

  function hasChapterAncestor(titleAnchor) {
    if (!titleAnchor.id.includes("-")) {
      return false;
    }
    const prefixes = buildAnchorPrefixes(titleAnchor.id).slice(0, -1);
    return prefixes.some((prefix) => {
      const ancestorAnchor = getTitleAnchorById(prefix);
      return ancestorAnchor !== null && isChapterNode(ancestorAnchor);
    });
  }

  function getQueryParamValue(key) {
    try {
      const url = new URL(window.location.href);
      return url.searchParams.get(key) ?? "";
    } catch {
      return "";
    }
  }

  function countVisibleDescendants(anchorId) {
    return getTocTitleAnchors().filter((anchor) => anchor.id.startsWith(`${anchorId}-`)).length;
  }

  function getContentRoot() {
    return document.querySelector(questionSelector);
  }

  function getContentRootChildren(contentRoot) {
    return Array.from(contentRoot.children);
  }

  function isContentAnchor(node) {
    return node instanceof HTMLElement && node.tagName === "A" && node.id !== "";
  }

  function isHeadingBlock(node) {
    return node instanceof HTMLElement && node.tagName === "DIV" && node.classList.contains("qw-level");
  }

  function getHeadingLevel(node) {
    if (!isHeadingBlock(node)) {
      return null;
    }
    const levelClass = Array.from(node.classList).find((className) => /^qw-level-\d+$/.test(className));
    if (levelClass === undefined) {
      return null;
    }
    const parsedLevel = Number.parseInt(levelClass.replace("qw-level-", ""), 10);
    return Number.isNaN(parsedLevel) ? null : parsedLevel;
  }

  function getDirectChildAnchorIndexById(contentRoot, anchorId) {
    return getContentRootChildren(contentRoot).findIndex((node) => isContentAnchor(node) && node.id === anchorId);
  }

  function getPathTitleAnchors(titleAnchor) {
    if (!titleAnchor.id.includes("-")) {
      return [titleAnchor];
    }
    return buildAnchorPrefixes(titleAnchor.id)
      .map((anchorId) => getTitleAnchorById(anchorId))
      .filter((anchor) => anchor !== null);
  }

  function buildCapturedFragmentHtml(contentRoot, selectedAnchor) {
    // Some Navis leaf selections only scroll within an already-rendered chapter view.
    // Capture the selected section slice, not the full question-export subtree, while
    // prepending the minimal ancestor heading chain needed to preserve hierarchy.
    if (isChapterNode(selectedAnchor)) {
      return contentRoot.outerHTML;
    }

    const selectedRefId = selectedAnchor.dataset.refId ?? "";
    if (selectedRefId === "") {
      return contentRoot.outerHTML;
    }

    const selectedStartIndex = getDirectChildAnchorIndexById(contentRoot, selectedRefId);
    if (selectedStartIndex < 0) {
      return contentRoot.outerHTML;
    }

    const contentChildren = getContentRootChildren(contentRoot);
    const selectedHeadingLevel = getHeadingLevel(contentChildren[selectedStartIndex + 1] ?? null);
    if (selectedHeadingLevel === null) {
      return contentRoot.outerHTML;
    }

    const nodesToClone = [];
    const appendedNodeIndexes = new Set();
    const pathAnchors = getPathTitleAnchors(selectedAnchor);
    const ancestorRefIds = pathAnchors
      .filter((anchor) => !isRootNode(anchor) && !isChapterNode(anchor))
      .map((anchor) => anchor.dataset.refId ?? "")
      .filter((refId) => refId && refId !== selectedRefId);

    for (const ancestorRefId of ancestorRefIds) {
      const ancestorIndex = getDirectChildAnchorIndexById(contentRoot, ancestorRefId);
      if (ancestorIndex < 0 || appendedNodeIndexes.has(ancestorIndex)) {
        continue;
      }
      const ancestorAnchor = contentChildren[ancestorIndex];
      const ancestorAnchorClone = ancestorAnchor.cloneNode(true);
      ancestorAnchorClone.dataset.ifrsExpertContextRefId = ancestorRefId;
      ancestorAnchorClone.dataset.ifrsExpertContextOnly = "true";
      ancestorAnchorClone.removeAttribute("id");
      nodesToClone.push(ancestorAnchorClone);
      appendedNodeIndexes.add(ancestorIndex);
      const ancestorHeading = contentChildren[ancestorIndex + 1] ?? null;
      if (isHeadingBlock(ancestorHeading) && !appendedNodeIndexes.has(ancestorIndex + 1)) {
        nodesToClone.push(ancestorHeading.cloneNode(true));
        appendedNodeIndexes.add(ancestorIndex + 1);
      }
    }

    for (let index = selectedStartIndex; index < contentChildren.length; index += 1) {
      const node = contentChildren[index];
      if (index > selectedStartIndex && isContentAnchor(node)) {
        const nextNode = contentChildren[index + 1] ?? null;
        const nextHeadingLevel = getHeadingLevel(nextNode);
        if (nextHeadingLevel !== null && nextHeadingLevel <= selectedHeadingLevel) {
          break;
        }
      }
      if (appendedNodeIndexes.has(index)) {
        continue;
      }
      nodesToClone.push(node.cloneNode(true));
      appendedNodeIndexes.add(index);
    }

    const fragmentRoot = contentRoot.cloneNode(false);
    for (const node of nodesToClone) {
      fragmentRoot.appendChild(node);
    }
    return fragmentRoot.outerHTML;
  }

  function buildContentSignature() {
    const contentRoot = getContentRoot();
    if (contentRoot === null) {
      return "";
    }
    return `${window.location.href}::${normalizeWhitespace(contentRoot.textContent || "").slice(0, 400)}::${contentRoot.childElementCount}`;
  }

  function deduplicateTargets(targets) {
    const seenRefIds = new Set();
    const deduplicatedTargets = [];
    for (const target of targets) {
      if (!target.refId || seenRefIds.has(target.refId)) {
        continue;
      }
      seenRefIds.add(target.refId);
      deduplicatedTargets.push(target);
    }
    return deduplicatedTargets;
  }

  function sleep(durationMs) {
    return new Promise((resolve) => {
      window.setTimeout(resolve, durationMs);
    });
  }

  async function waitFor(predicate, timeoutMs, errorMessage = "Timed out while waiting for Navis page state") {
    const startedAt = Date.now();
    while (Date.now() - startedAt < timeoutMs) {
      if (predicate()) {
        return;
      }
      await sleep(100);
    }
    throw new Error(errorMessage);
  }

  async function waitForTocReady() {
    await waitFor(
      () => getTocTitleAnchors().length > 0,
      10000,
      "Timed out while waiting for the Navis TOC to become available",
    );
  }

  async function waitForSelectedRefId(expectedRefId) {
    await waitFor(
      () => getSelectedTitleAnchor()?.dataset.refId === expectedRefId,
      10000,
      `Timed out while waiting for selected Navis refId=${expectedRefId}`,
    );
  }

  async function waitForStableContent(expectedRefId) {
    if (expectedRefId) {
      await waitForSelectedRefId(expectedRefId);
    }
    await waitFor(
      () => getContentRoot() !== null,
      10000,
      "Timed out while waiting for the Navis content root",
    );

    let previousSignature = buildContentSignature();
    let stableIterations = 0;
    const startedAt = Date.now();
    while (Date.now() - startedAt < 10000) {
      await sleep(150);
      const nextSignature = buildContentSignature();
      if (nextSignature !== "" && nextSignature === previousSignature) {
        stableIterations += 1;
        if (stableIterations >= 2) {
          return;
        }
      } else {
        stableIterations = 0;
      }
      previousSignature = nextSignature;
    }
    throw new Error("Timed out while waiting for stable Navis content");
  }

  async function expandNodeIfClosed(titleAnchor) {
    const toggleAnchor = getNodeToggleAnchor(titleAnchor);
    if (toggleAnchor === null || toggleAnchor.classList.contains("opened")) {
      return false;
    }

    const beforeDescendantCount = countVisibleDescendants(titleAnchor.id);
    toggleAnchor.click();
    await waitFor(() => {
      const refreshedAnchor = getTitleAnchorById(titleAnchor.id);
      if (refreshedAnchor === null) {
        return false;
      }
      const refreshedToggleAnchor = getNodeToggleAnchor(refreshedAnchor);
      if (refreshedToggleAnchor === null) {
        return false;
      }
      const afterDescendantCount = countVisibleDescendants(titleAnchor.id);
      return refreshedToggleAnchor.classList.contains("opened") && afterDescendantCount >= beforeDescendantCount;
    }, 6000, `Timed out while expanding Navis TOC node ${titleAnchor.id}`);
    await sleep(150);
    return true;
  }

  async function discoverChapterTargets() {
    await waitForTocReady();

    let changed = true;
    while (changed) {
      changed = false;
      for (const titleAnchor of getTocTitleAnchors()) {
        if (isLeafNode(titleAnchor) || isChapterNode(titleAnchor) || hasChapterAncestor(titleAnchor)) {
          continue;
        }
        const expanded = await expandNodeIfClosed(titleAnchor);
        if (expanded) {
          changed = true;
        }
      }
    }

    return deduplicateTargets(
      getTocTitleAnchors()
        .filter((titleAnchor) => isChapterNode(titleAnchor))
        .map((titleAnchor) => ({ refId: titleAnchor.dataset.refId ?? "", title: getTitleAnchorText(titleAnchor) })),
    );
  }

  async function discoverChapterLeafTargets(chapterRefId) {
    await waitForTocReady();
    await waitForSelectedRefId(chapterRefId);

    const chapterAnchor = getTitleAnchorByRefId(chapterRefId);
    if (chapterAnchor === null) {
      throw new Error(`Could not locate Navis CHAPITRE refId=${chapterRefId}`);
    }

    await expandNodeIfClosed(chapterAnchor);

    let changed = true;
    while (changed) {
      changed = false;
      for (const titleAnchor of getTocTitleAnchors()) {
        if (!titleAnchor.id.startsWith(`${chapterAnchor.id}-`)) {
          continue;
        }
        if (isLeafNode(titleAnchor)) {
          continue;
        }
        const expanded = await expandNodeIfClosed(titleAnchor);
        if (expanded) {
          changed = true;
        }
      }
    }

    const pageTargets = deduplicateTargets(
      getTocTitleAnchors()
        .filter((titleAnchor) => titleAnchor.id.startsWith(`${chapterAnchor.id}-`) && isLeafNode(titleAnchor))
        .map((titleAnchor) => ({ refId: titleAnchor.dataset.refId ?? "", title: getTitleAnchorText(titleAnchor) })),
    );

    return {
      chapterRefId,
      chapterTitle: getTitleAnchorText(chapterAnchor),
      chapterUrl: window.location.href,
      productKey: getQueryParamValue("key"),
      pageTargets,
    };
  }

  async function inspectContext() {
    await waitForTocReady();

    const selectedAnchor = getSelectedTitleAnchor();
    if (selectedAnchor === null) {
      return {
        mode: "unsupported",
        selectedRefId: "",
        selectedTitle: "",
        productKey: getQueryParamValue("key"),
        url: window.location.href,
      };
    }

    const selectedRefId = selectedAnchor.dataset.refId ?? "";
    const selectedTitle = getTitleAnchorText(selectedAnchor);
    if (selectedRefId === navisRootRefId) {
      return {
        mode: "root",
        selectedRefId,
        selectedTitle,
        productKey: getQueryParamValue("key"),
        url: window.location.href,
      };
    }
    if (isChapterNode(selectedAnchor)) {
      return {
        mode: "chapter",
        selectedRefId,
        selectedTitle,
        productKey: getQueryParamValue("key"),
        url: window.location.href,
      };
    }
    return {
      mode: "unsupported",
      selectedRefId,
      selectedTitle,
      productKey: getQueryParamValue("key"),
      url: window.location.href,
    };
  }

  async function captureCurrentFragment(expectedRefId) {
    await waitForStableContent(expectedRefId);

    const selectedAnchor = getSelectedTitleAnchor();
    if (selectedAnchor === null) {
      throw new Error("Could not determine the selected Navis TOC node");
    }
    const selectedRefId = selectedAnchor.dataset.refId ?? "";
    if (expectedRefId && selectedRefId !== expectedRefId) {
      throw new Error(`Expected selected refId=${expectedRefId}, got ${selectedRefId}`);
    }

    const contentRoot = getContentRoot();
    if (contentRoot === null) {
      throw new Error("Could not locate #documentContent .question.question-export");
    }

    return {
      pageRefId: selectedRefId,
      pageTitle: getTitleAnchorText(selectedAnchor),
      url: window.location.href,
      canonicalUrl: window.location.href,
      fragmentHtml: buildCapturedFragmentHtml(contentRoot, selectedAnchor),
    };
  }

  switch (task.type) {
    case "inspectContext":
      return inspectContext();
    case "discoverChapters":
      return discoverChapterTargets().then((chapters) => ({ chapters }));
    case "discoverChapterLeafTargets":
      return discoverChapterLeafTargets(task.chapterRefId);
    case "captureCurrentFragment":
      return captureCurrentFragment(task.expectedRefId);
    default:
      throw new Error(`Unsupported Navis page task: ${task.type}`);
  }
}

function buildCaptureBasename(result) {
  if (result.sidecar.capture_format === NAVIS_BUNDLE_CAPTURE_FORMAT) {
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

function sanitizeFilenameComponent(value) {
  return String(value)
    .normalize("NFKD")
    .replace(/[^A-Za-z0-9_-]+/g, "-")
    .replace(/^-+|-+$/g, "") || "document";
}

async function navisChapterCaptureExists(productKey, chapterRefId) {
  const sanitizedProductKey = sanitizeFilenameComponent(productKey || "NAVIS");
  const sanitizedChapterRefId = sanitizeFilenameComponent(chapterRefId || "document");
  const chapterToken = `--navis-${sanitizedProductKey}-${sanitizedChapterRefId}--`;
  const downloads = await chrome.downloads.search({
    query: [chapterToken],
    state: "complete",
  });
  return downloads.some((downloadItem) => {
    const filename = downloadItem.filename || "";
    return filename.includes(`${ROOT_PREFIX}/`) && filename.includes(chapterToken) && filename.endsWith(".html");
  });
}

function sanitizeChapterTitleForFilename(value) {
  return String(value)
    .normalize("NFKD")
    .replace(/\s+/g, "_")
    .replace(/[^A-Za-z0-9_-]+/g, "_")
    .replace(/_+/g, "_")
    .replace(/^_+|_+$/g, "") || "CHAPITRE";
}

function buildNavisDocumentUrl(baseUrl, refId) {
  const url = new URL(baseUrl);
  url.searchParams.set("refId", refId);
  return url.toString();
}

function isNavigationTargetReached(currentUrl, targetUrl, expectedRefId = null) {
  if (currentUrl === undefined || currentUrl === null) {
    return false;
  }

  if (expectedRefId !== null) {
    return getQueryParamValue(currentUrl, "refId") === expectedRefId;
  }

  return currentUrl === targetUrl;
}

function getQueryParamValue(url, key) {
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

function escapeScriptJson(value) {
  return value.replace(/<\//g, "<\\/");
}

function escapeHtmlAttribute(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function escapeHtmlText(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
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

function getSourceFamily(tabUrl) {
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

function getNavisRefIdFromUrl(tabUrl) {
  return getQueryParamValue(tabUrl, "refId");
}

function getNavisActionModeFromUrl(tabUrl) {
  const refId = getNavisRefIdFromUrl(tabUrl);
  if (refId === NAVIS_ROOT_REF_ID) {
    return "root";
  }
  if (refId !== null && /^C[0-9A-Z-]+-EFL$/.test(refId)) {
    return "chapter";
  }
  return "unsupported";
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
