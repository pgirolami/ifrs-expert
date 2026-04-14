import {
  ROOT_PREFIX,
  downloadCaptureArtifacts,
  escapeHtmlAttribute,
  escapeHtmlText,
  escapeScriptJson,
  formatErrorMessage,
  getQueryParamValue,
  logError,
  logInfo,
  logWarn,
  navigateTabToUrl,
  sanitizeChapterTitleForFilename,
  sanitizeFilenameComponent,
  showToastInTab,
  sleepMs,
  throwIfImportCancelled,
  updateImportProgress,
} from "./background_common.mjs";

const NAVIS_ROOT_ACTION_TITLE = "Extract all Navis chapters";
const NAVIS_CHAPTER_ACTION_TITLE = "Extract this Navis chapter";
const NAVIS_UNSUPPORTED_ACTION_TITLE = "Extract available only on Navis root or CHAPITRE nodes";
const NAVIS_ROOT_REF_ID = "N24F9F491387ED-EFL";
const NAVIS_BUNDLE_CAPTURE_FORMAT = "navis-chapter-bundle/v1";
const NAVIS_SECTION_LOAD_DELAY_MS = 1000;
const NAVIS_PAGE_TASK_MAX_ATTEMPTS = 3;
const NAVIS_PAGE_TASK_RETRY_DELAY_MS = 750;

export async function resolveNavisActionState(tabId, tabUrl) {
  const urlMode = getNavisActionModeFromUrl(tabUrl);

  try {
    const context = await executeNavisPageTask(tabId, { type: "inspectContext" });
    if (context.mode === "root") {
      return {
        enabled: true,
        title: NAVIS_ROOT_ACTION_TITLE,
        mode: context.mode,
      };
    }
    if (context.mode === "chapter") {
      return {
        enabled: true,
        title: NAVIS_CHAPTER_ACTION_TITLE,
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
      mode: urlMode,
    };
  }
  if (urlMode === "chapter") {
    return {
      enabled: true,
      title: NAVIS_CHAPTER_ACTION_TITLE,
      mode: urlMode,
    };
  }

  return {
    enabled: false,
    title: NAVIS_UNSUPPORTED_ACTION_TITLE,
    mode: "unsupported",
  };
}

export async function captureNavisImport(tabId, tabUrl) {
  throwIfImportCancelled();
  await updateImportProgress({
    type: "phaseUpdated",
    phaseLabel: "Inspecting Navis page…",
  });
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
    throw new Error("Navis extraction is available only on the root node or a CHAPITRE node");
  }

  await updateImportProgress({
    type: "phaseUpdated",
    phaseLabel: effectiveMode === "root" ? "Discovering chapters…" : "Preparing chapter…",
  });
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

  await updateImportProgress({
    type: "jobStarted",
    sourceFamily: "navis",
    jobType: batchMode,
    title: batchMode === "root-batch" ? "Navis root extraction" : "Navis chapter extraction",
    totalPages: chapterTargets.length,
    startedAt: new Date().toISOString(),
    logMessage: batchMode === "root-batch"
      ? `Starting Navis root extraction (${chapterTargets.length} chapters)`
      : `Starting Navis chapter extraction (${chapterTargets.length} chapter)`,
  });

  logInfo("Starting Navis chapter capture.", {
    tabId,
    mode: batchMode,
    discoveredChapterCount: discoveredChapterTargets.length,
    skippedChapterCount,
    chapterCount: chapterTargets.length,
    rootRefId: NAVIS_ROOT_REF_ID,
  });

  for (const [chapterIndex, chapterTarget] of chapterTargets.entries()) {
    throwIfImportCancelled();
    logInfo("Capturing Navis chapter.", {
      tabId,
      chapterIndex: chapterIndex + 1,
      chapterCount: chapterTargets.length,
      chapterRefId: chapterTarget.refId,
      chapterTitle: chapterTarget.title,
    });
    await updateImportProgress({
      type: "pageStarted",
      pageTitle: chapterTarget.title,
      pageUrl: buildNavisDocumentUrl(baseUrl, chapterTarget.refId),
      pageIndex: chapterIndex + 1,
      logMessage: `Chapter ${chapterIndex + 1}/${chapterTargets.length}: ${chapterTarget.title}`,
    });
    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Navigating…",
    });

    const capture = await captureNavisChapter(tabId, {
      baseUrl,
      rootRefId: NAVIS_ROOT_REF_ID,
      productKey: effectiveProductKey,
      chapterRefId: chapterTarget.refId,
      chapterTitle: chapterTarget.title,
      captureMode: batchMode,
    });
    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Downloading…",
    });
    const basename = await downloadCaptureArtifacts(capture);
    savedBasenames.push(basename);
    await updateImportProgress({
      type: "artifactSaved",
      basename,
      count: 1,
      logMessage: `Saved ${basename}`,
    });
    await updateImportProgress({
      type: "pageCompleted",
      pageTitle: chapterTarget.title,
      logMessage: `Completed ${chapterTarget.title}`,
    });
  }

  const summaryMessage = savedBasenames.length === 1
    ? `Saved ${savedBasenames[0]}.html and ${savedBasenames[0]}.json`
    : `Saved ${savedBasenames.length} chapter captures to ${ROOT_PREFIX}/`;
  await updateImportProgress({
    type: "jobCompleted",
    finishedAt: new Date().toISOString(),
    completedPages: chapterTargets.length,
    summary: summaryMessage,
  });
  await showToastInTab(tabId, summaryMessage, "success");
}

async function discoverNavisRootChapterTargets(tabId) {
  const discovery = await executeNavisPageTask(tabId, { type: "discoverChapters" });
  if (!Array.isArray(discovery.chapters)) {
    throw new Error("Navis chapter discovery did not return a chapter list");
  }
  logInfo("Discovered Navis root chapters.", {
    tabId,
    chapterCount: discovery.chapters.length,
    tocAnchorCount: discovery.tocAnchorCount,
    expandedNodeCount: discovery.expandedNodeCount,
  });
  return discovery.chapters;
}

async function captureNavisChapter(tabId, options) {
  throwIfImportCancelled();
  await updateImportProgress({
    type: "phaseUpdated",
    phaseLabel: "Navigating…",
  });
  const chapterUrl = buildNavisDocumentUrl(options.baseUrl, options.chapterRefId);
  await navigateTabToUrl(tabId, chapterUrl, options.chapterRefId);
  await sleepMs(NAVIS_SECTION_LOAD_DELAY_MS);

  await updateImportProgress({
    type: "phaseUpdated",
    phaseLabel: "Discovering chapter pages…",
  });
  const chapterDiscovery = await executeNavisPageTaskWithRetry(tabId, {
    type: "discoverChapterLeafTargets",
    chapterRefId: options.chapterRefId,
  });
  if (chapterDiscovery === null || chapterDiscovery === undefined) {
    throw new Error(`Navis chapter discovery returned no result for chapterRefId=${options.chapterRefId}`);
  }
  const pageTargets = Array.isArray(chapterDiscovery.pageTargets) ? chapterDiscovery.pageTargets : [];
  const effectiveChapterTitle = chapterDiscovery.chapterTitle || options.chapterTitle;
  logInfo("Discovered Navis chapter leaf targets.", {
    tabId,
    chapterRefId: options.chapterRefId,
    chapterTitle: effectiveChapterTitle,
    pageTargetCount: pageTargets.length,
    tocAnchorCount: chapterDiscovery.tocAnchorCount,
    expandedNodeCount: chapterDiscovery.expandedNodeCount,
  });
  const effectiveProductKey = chapterDiscovery.productKey || options.productKey || getQueryParamValue(chapterUrl, "key") || "NAVIS";
  const effectiveChapterUrl = chapterDiscovery.chapterUrl || chapterUrl;

  const pageFragments = [];
  if (pageTargets.length === 0) {
    logWarn("No Navis leaf targets were found for chapter; capturing the current chapter page as a fallback.", {
      tabId,
      chapterRefId: options.chapterRefId,
      chapterTitle: effectiveChapterTitle,
    });
    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Parsing…",
      logMessage: `Fallback fragment for ${effectiveChapterTitle}`,
    });
    const fragment = await executeNavisPageTaskWithRetry(tabId, {
      type: "captureCurrentFragment",
      expectedRefId: options.chapterRefId,
    });
    logInfo("Captured fallback Navis fragment.", {
      tabId,
      chapterRefId: options.chapterRefId,
      fragmentHtmlLength: fragment.fragmentHtmlLength,
      contentChildCount: fragment.contentChildCount,
    });
    pageFragments.push(fragment);
  } else {
    for (const [pageIndex, pageTarget] of pageTargets.entries()) {
      throwIfImportCancelled();
      logInfo("Capturing Navis page fragment.", {
        tabId,
        chapterRefId: options.chapterRefId,
        pageIndex: pageIndex + 1,
        pageCount: pageTargets.length,
        pageRefId: pageTarget.refId,
        pageTitle: pageTarget.title,
      });
      await updateImportProgress({
        type: "phaseUpdated",
        phaseLabel: "Parsing…",
        logMessage: `Page fragment ${pageIndex + 1}/${pageTargets.length}: ${pageTarget.title}`,
      });
      const pageUrl = buildNavisDocumentUrl(options.baseUrl, pageTarget.refId);
      await updateImportProgress({
        type: "phaseUpdated",
        phaseLabel: "Navigating…",
      });
      await navigateTabToUrl(tabId, pageUrl, pageTarget.refId);
      await sleepMs(NAVIS_SECTION_LOAD_DELAY_MS);
      await updateImportProgress({
        type: "phaseUpdated",
        phaseLabel: "Parsing…",
        logMessage: `Page fragment ${pageIndex + 1}/${pageTargets.length}: ${pageTarget.title}`,
      });
      const fragment = await executeNavisPageTaskWithRetry(tabId, {
        type: "captureCurrentFragment",
        expectedRefId: pageTarget.refId,
      });
      logInfo("Captured Navis fragment.", {
        tabId,
        chapterRefId: options.chapterRefId,
        pageRefId: pageTarget.refId,
        fragmentHtmlLength: fragment.fragmentHtmlLength,
        contentChildCount: fragment.contentChildCount,
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
    '<html data-ifrs-expert-source="navis" data-ifrs-expert-capture="chapter-bundle">',
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
    throwIfImportCancelled();
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

  function getQueryParamValueInPage(key) {
    try {
      const url = new URL(window.location.href);
      return url.searchParams.get(key) ?? "";
    } catch {
      return "";
    }
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
    const contentChildren = getContentRootChildren(contentRoot);
    const firstChild = contentChildren.at(0) ?? null;
    const lastChild = contentChildren.at(-1) ?? null;
    const firstText = normalizeWhitespace(firstChild?.textContent || "").slice(0, 80);
    const lastText = normalizeWhitespace(lastChild?.textContent || "").slice(0, 80);
    return [
      window.location.href,
      String(contentRoot.childElementCount),
      firstChild?.id || "",
      lastChild?.id || "",
      firstText,
      lastText,
    ].join("::");
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
      return refreshedToggleAnchor.classList.contains("opened");
    }, 6000, `Timed out while expanding Navis TOC node ${titleAnchor.id}`);
    await sleep(150);
    return true;
  }

  async function discoverChapterTargets() {
    await waitForTocReady();

    let changed = true;
    let expandedNodeCount = 0;
    while (changed) {
      changed = false;
      for (const titleAnchor of getTocTitleAnchors()) {
        if (isLeafNode(titleAnchor) || isChapterNode(titleAnchor) || hasChapterAncestor(titleAnchor)) {
          continue;
        }
        const expanded = await expandNodeIfClosed(titleAnchor);
        if (expanded) {
          changed = true;
          expandedNodeCount += 1;
        }
      }
    }

    const tocTitleAnchors = getTocTitleAnchors();
    return {
      chapters: deduplicateTargets(
        tocTitleAnchors
          .filter((titleAnchor) => isChapterNode(titleAnchor))
          .map((titleAnchor) => ({ refId: titleAnchor.dataset.refId ?? "", title: getTitleAnchorText(titleAnchor) })),
      ),
      tocAnchorCount: tocTitleAnchors.length,
      expandedNodeCount,
    };
  }

  async function discoverChapterLeafTargets(chapterRefId) {
    await waitForTocReady();
    await waitForSelectedRefId(chapterRefId);

    const chapterAnchor = getTitleAnchorByRefId(chapterRefId);
    if (chapterAnchor === null) {
      throw new Error(`Could not locate Navis CHAPITRE refId=${chapterRefId}`);
    }

    let expandedNodeCount = 0;
    if (await expandNodeIfClosed(chapterAnchor)) {
      expandedNodeCount += 1;
    }

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
          expandedNodeCount += 1;
        }
      }
    }

    const tocTitleAnchors = getTocTitleAnchors();
    const pageTargets = deduplicateTargets(
      tocTitleAnchors
        .filter((titleAnchor) => titleAnchor.id.startsWith(`${chapterAnchor.id}-`) && isLeafNode(titleAnchor))
        .map((titleAnchor) => ({ refId: titleAnchor.dataset.refId ?? "", title: getTitleAnchorText(titleAnchor) })),
    );

    return {
      chapterRefId,
      chapterTitle: getTitleAnchorText(chapterAnchor),
      chapterUrl: window.location.href,
      productKey: getQueryParamValueInPage("key"),
      pageTargets,
      tocAnchorCount: tocTitleAnchors.length,
      expandedNodeCount,
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
        productKey: getQueryParamValueInPage("key"),
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
        productKey: getQueryParamValueInPage("key"),
        url: window.location.href,
      };
    }
    if (isChapterNode(selectedAnchor)) {
      return {
        mode: "chapter",
        selectedRefId,
        selectedTitle,
        productKey: getQueryParamValueInPage("key"),
        url: window.location.href,
      };
    }
    return {
      mode: "unsupported",
      selectedRefId,
      selectedTitle,
      productKey: getQueryParamValueInPage("key"),
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

    const fragmentHtml = buildCapturedFragmentHtml(contentRoot, selectedAnchor);
    return {
      pageRefId: selectedRefId,
      pageTitle: getTitleAnchorText(selectedAnchor),
      url: window.location.href,
      canonicalUrl: window.location.href,
      fragmentHtml,
      fragmentHtmlLength: fragmentHtml.length,
      contentChildCount: contentRoot.childElementCount,
    };
  }

  switch (task.type) {
    case "inspectContext":
      return inspectContext();
    case "discoverChapters":
      return discoverChapterTargets();
    case "discoverChapterLeafTargets":
      return discoverChapterLeafTargets(task.chapterRefId);
    case "captureCurrentFragment":
      return captureCurrentFragment(task.expectedRefId);
    default:
      throw new Error(`Unsupported Navis page task: ${task.type}`);
  }
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

function buildNavisDocumentUrl(baseUrl, refId) {
  const url = new URL(baseUrl);
  url.searchParams.set("refId", refId);
  return url.toString();
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
