import {
  buildIfrsVariantNavigationUrl,
  selectIfrsCaptureTargets,
  selectIfrsCorpusTargets,
} from "./ifrs_import.mjs";
import { resolveIfrsDocumentType } from "./ifrs_document_types.mjs";
import {
  ACTION_TITLE,
  downloadCaptureArtifacts,
  formatErrorMessage,
  getSourceFamily,
  logInfo,
  logWarn,
  navigateTabToUrl,
  reloadTab,
  showToastInTab,
  sleepMs,
  throwIfImportCancelled,
  updateImportProgress,
  waitForTabComplete,
} from "./background_common.mjs";

const IFRS_CORPUS_ACTION_TITLE = "Extract IFRS corpus";
const IFRS_SECTION_LOAD_DELAY_MS = 1000;
const IFRS_PAGE_TASK_MAX_ATTEMPTS = 3;
const IFRS_PAGE_TASK_RETRY_DELAY_MS = 750;
const IFRS_CORPUS_SKIPPED_PAGE_TITLES = new Set([
  "Conceptual Framework",
  "Conceptual Framework for Financial Reporting",
]);

export async function resolveIfrsActionState(tabId) {
  const context = await executeIfrsPageTask(tabId, { type: "inspectContext" });
  return {
    enabled: true,
    title: context.mode === "corpus" ? IFRS_CORPUS_ACTION_TITLE : ACTION_TITLE,
    mode: context.mode,
  };
}

export async function captureIfrsSource(tabId, tabUrl) {
  throwIfImportCancelled();
  const context = await executeIfrsPageTaskWithRetry(tabId, { type: "inspectContext" });
  if (context.mode === "corpus") {
    await captureIfrsCorpus(tabId, tabUrl, context);
    return;
  }
  await captureIfrsImport(tabId, tabUrl, {
    jobConfig: {
      sourceFamily: "ifrs",
      jobType: "ifrs-page",
      title: "IFRS page extraction",
      totalPages: 1,
    },
  });
}

async function captureIfrsCorpus(tabId, tabUrl, context) {
  const corpusTargets = selectIfrsCorpusTargets(context.corpusTargets ?? []);
  if (corpusTargets.length === 0) {
    throw new Error("No IFRS document links were found on the corpus page");
  }

  const savedBasenames = [];
  const failedTargets = [];
  logInfo("Starting IFRS corpus capture.", {
    tabId,
    url: tabUrl,
    documentCount: corpusTargets.length,
    corpusTargets,
  });
  await updateImportProgress({
    type: "jobStarted",
    sourceFamily: "ifrs",
    jobType: "ifrs-corpus",
    title: "IFRS corpus extraction",
    totalPages: corpusTargets.length,
    startedAt: new Date().toISOString(),
    logMessage: `Starting IFRS corpus extraction (${corpusTargets.length} pages)`,
  });

  for (const [documentIndex, corpusTarget] of corpusTargets.entries()) {
    throwIfImportCancelled();
    if (IFRS_CORPUS_SKIPPED_PAGE_TITLES.has(corpusTarget.title)) {
      logInfo("Skipping IFRS corpus page by title.", {
        tabId,
        documentIndex: documentIndex + 1,
        documentCount: corpusTargets.length,
        documentTitle: corpusTarget.title,
        documentUrl: corpusTarget.url,
      });
      await updateImportProgress({
        type: "pageSkipped",
        pageTitle: corpusTarget.title,
        logMessage: `Skipped ${corpusTarget.title}`,
      });
      continue;
    }

    logInfo("Capturing IFRS document page from corpus.", {
      tabId,
      documentIndex: documentIndex + 1,
      documentCount: corpusTargets.length,
      documentTitle: corpusTarget.title,
      documentUrl: corpusTarget.url,
    });
    await updateImportProgress({
      type: "pageStarted",
      pageTitle: corpusTarget.title,
      pageUrl: corpusTarget.url,
      pageIndex: documentIndex + 1,
      logMessage: `Page ${documentIndex + 1}/${corpusTargets.length}: ${corpusTarget.title}`,
    });
    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Navigating…",
    });

    try {
      await navigateTabToUrl(tabId, corpusTarget.url);
      await sleepMs(IFRS_SECTION_LOAD_DELAY_MS);
      await waitForTabComplete(tabId);
      const documentBasenames = await captureIfrsImport(tabId, corpusTarget.url, {
        showCompletionToast: false,
        skipJobStart: true,
        corpusProgress: {
          documentIndex: documentIndex + 1,
          documentCount: corpusTargets.length,
          documentTitle: corpusTarget.title,
        },
      });
      savedBasenames.push(...documentBasenames);
      await updateImportProgress({
        type: "pageCompleted",
        pageTitle: corpusTarget.title,
        logMessage: `Completed ${corpusTarget.title}`,
      });
    } catch (error) {
      const errorMessage = formatErrorMessage(error);
      failedTargets.push({
        title: corpusTarget.title,
        url: corpusTarget.url,
        error: errorMessage,
      });
      logInfo("IFRS corpus document capture failed.", {
        tabId,
        documentTitle: corpusTarget.title,
        documentUrl: corpusTarget.url,
        error: errorMessage,
      });
      throwIfImportCancelled();
      await updateImportProgress({
        type: "pageFailed",
        pageTitle: corpusTarget.title,
        pageUrl: corpusTarget.url,
        error: errorMessage,
      });
    }
  }

  if (savedBasenames.length === 0) {
    throw new Error("IFRS corpus capture did not save any documents");
  }

  const summaryMessage = failedTargets.length === 0
    ? `Saved ${savedBasenames.length} IFRS captures from ${corpusTargets.length} pages`
    : `Saved ${savedBasenames.length} IFRS captures; ${failedTargets.length} pages failed`;
  await updateImportProgress({
    type: "jobCompleted",
    finishedAt: new Date().toISOString(),
    completedPages: corpusTargets.length,
    summary: summaryMessage,
  });
  await showToastInTab(tabId, summaryMessage, failedTargets.length === 0 ? "success" : "error");
}

async function captureIfrsImport(tabId, tabUrl, options = {}) {
  throwIfImportCancelled();
  logInfo("Starting IFRS extraction.", { tabId, url: tabUrl, corpusProgress: options.corpusProgress });
  await updateImportProgress({
    type: "phaseUpdated",
    phaseLabel: "Inspecting page…",
  });
  const captureContext = await executeIfrsPageTaskWithRetry(tabId, { type: "inspectCaptureTargets" });
  const captureTargets = selectIfrsCaptureTargets(captureContext.availableDocuments ?? []);

  if (captureTargets.length === 0) {
    throw new Error("No selectable IFRS documents were found on the current page");
  }

  if (options.skipJobStart !== true) {
    await updateImportProgress({
      type: "jobStarted",
      sourceFamily: "ifrs",
      jobType: options.jobConfig?.jobType ?? "ifrs-page",
      title: options.jobConfig?.title ?? "IFRS page extraction",
      totalPages: options.jobConfig?.totalPages ?? 1,
      startedAt: new Date().toISOString(),
      logMessage: `Starting ${options.jobConfig?.title ?? "IFRS page extraction"}`,
    });
    await updateImportProgress({
      type: "pageStarted",
      pageTitle: captureContext.availableDocuments.find((target) => target.checked)?.label ?? "IFRS document",
      pageUrl: captureContext.currentUrl || tabUrl,
      pageIndex: 1,
      logMessage: `Page 1/1: ${captureContext.availableDocuments.find((target) => target.checked)?.label ?? "IFRS document"}`,
    });
  }

  let currentVariantValue = captureContext.currentVariantValue || captureTargets[0].value;
  let currentUrl = captureContext.currentUrl || tabUrl;
  const shellCanonicalUrl = captureContext.shellCanonicalUrl;
  const savedBasenames = [];

  logInfo("Starting IFRS batch capture.", {
    tabId,
    currentUrl,
    currentVariantValue,
    shellCanonicalUrl,
    documentCount: captureTargets.length,
    documentLabels: captureTargets.map((target) => target.label),
    availableDocuments: captureContext.availableDocuments,
  });

  for (const [documentIndex, captureTarget] of captureTargets.entries()) {
    throwIfImportCancelled();
    const targetUrl = buildIfrsVariantNavigationUrl({
      currentUrl,
      currentVariantValue,
      targetVariantValue: captureTarget.value,
      shellCanonicalUrl,
    });
    logInfo("Capturing IFRS variant.", {
      tabId,
      documentIndex: documentIndex + 1,
      documentCount: captureTargets.length,
      targetLabel: captureTarget.label,
      targetVariantValue: captureTarget.value,
      targetUrl,
      corpusProgress: options.corpusProgress,
    });
    await updateImportProgress({
      type: "variantStarted",
      variantLabel: captureTarget.label,
      variantIndex: documentIndex + 1,
      variantCount: captureTargets.length,
      logMessage: options.corpusProgress
        ? `Variant ${documentIndex + 1}/${captureTargets.length} for ${options.corpusProgress.documentTitle}: ${captureTarget.label}`
        : `Variant ${documentIndex + 1}/${captureTargets.length}: ${captureTarget.label}`,
    });
    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Selecting variant…",
    });

    try {
      const selectionResult = await executeIfrsPageTaskWithRetry(tabId, {
        type: "selectVariant",
        targetVariantValue: captureTarget.value,
      });
      currentUrl = selectionResult.currentUrl || currentUrl;
      currentVariantValue = selectionResult.currentVariantValue || captureTarget.value;
      logInfo("Switched IFRS variant via in-page interaction.", {
        tabId,
        targetLabel: captureTarget.label,
        targetVariantValue: captureTarget.value,
        currentUrl,
        currentVariantValue,
      });
      await sleepMs(250);
      await waitForTabComplete(tabId);
    } catch (error) {
      logWarn("Unable to switch IFRS variant via in-page interaction; falling back to URL navigation.", {
        tabId,
        targetLabel: captureTarget.label,
        targetVariantValue: captureTarget.value,
        targetUrl,
        error: formatErrorMessage(error),
      });
      await navigateTabToIfrsVariant(tabId, targetUrl, captureTarget.value);
      await sleepMs(IFRS_SECTION_LOAD_DELAY_MS);
      currentUrl = targetUrl;
      currentVariantValue = captureTarget.value;
    }

    let result;
    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Parsing…",
    });
    try {
      result = await executeIfrsPageTaskWithRetry(tabId, {
        type: "captureCurrentVariant",
        expectedVariantValue: captureTarget.value,
      });
    } catch (error) {
      logWarn("IFRS variant capture failed; retrying after hard reload.", {
        tabId,
        targetLabel: captureTarget.label,
        targetVariantValue: captureTarget.value,
        targetUrl,
        error: formatErrorMessage(error),
      });
      await updateImportProgress({
        type: "phaseUpdated",
        phaseLabel: "Retrying after reload…",
        logMessage: `Retrying ${captureTarget.label} after reload`,
      });
      await reloadTab(tabId);
      await waitForTabComplete(tabId);
      await sleepMs(IFRS_SECTION_LOAD_DELAY_MS);
      await navigateTabToIfrsVariant(tabId, targetUrl, captureTarget.value);
      await waitForTabComplete(tabId);
      await sleepMs(IFRS_SECTION_LOAD_DELAY_MS);
      result = await executeIfrsPageTaskWithRetry(tabId, {
        type: "captureCurrentVariant",
        expectedVariantValue: captureTarget.value,
      });
    }

    currentUrl = result.sidecar.url || currentUrl;
    currentVariantValue = captureTarget.value;

    logInfo("Captured IFRS variant successfully.", {
      tabId,
      targetLabel: captureTarget.label,
      canonicalUrl: result.sidecar.canonical_url,
      title: result.sidecar.title,
      sourceFamily: getSourceFamily(result.sidecar.url),
      htmlLength: result.html.length,
    });

    await updateImportProgress({
      type: "phaseUpdated",
      phaseLabel: "Downloading…",
    });
    const basename = await downloadCaptureArtifacts(result);
    savedBasenames.push(basename);
    await updateImportProgress({
      type: "artifactSaved",
      basename,
      count: 1,
      logMessage: `Saved ${basename}`,
    });
  }

  const summaryMessage = savedBasenames.length === 1
    ? `Saved ${savedBasenames[0]}.html and ${savedBasenames[0]}.json`
    : `Saved ${savedBasenames.length} IFRS captures to ifrs-expert/`;
  if (options.skipJobStart !== true) {
    await updateImportProgress({
      type: "pageCompleted",
      pageTitle: captureContext.availableDocuments.find((target) => target.checked)?.label ?? "IFRS document",
      logMessage: summaryMessage,
    });
    await updateImportProgress({
      type: "jobCompleted",
      finishedAt: new Date().toISOString(),
      completedPages: 1,
      summary: summaryMessage,
    });
  }
  if (options.showCompletionToast !== false) {
    await showToastInTab(tabId, summaryMessage, "success");
  }
  return savedBasenames;
}

async function executeIfrsPageTask(tabId, task) {
  await waitForTabComplete(tabId);
  const injectionResults = await chrome.scripting.executeScript({
    target: { tabId },
    func: runIfrsPageTask,
    args: [task],
  });
  const firstResult = injectionResults.at(0);
  if (firstResult === undefined) {
    throw new Error(`IFRS page task returned no injection result for task=${task.type}`);
  }
  return firstResult.result;
}

async function executeIfrsPageTaskWithRetry(tabId, task) {
  let lastError = null;
  for (let attempt = 1; attempt <= IFRS_PAGE_TASK_MAX_ATTEMPTS; attempt += 1) {
    throwIfImportCancelled();
    try {
      const result = await executeIfrsPageTask(tabId, task);
      if (result !== null && result !== undefined) {
        return result;
      }
      throw new Error(`IFRS page task returned an empty result for task=${task.type}`);
    } catch (error) {
      lastError = error;
      logWarn("IFRS page task attempt failed.", {
        tabId,
        taskType: task.type,
        attempt,
        maxAttempts: IFRS_PAGE_TASK_MAX_ATTEMPTS,
        error: formatErrorMessage(error),
      });
      if (attempt < IFRS_PAGE_TASK_MAX_ATTEMPTS) {
        await sleepMs(IFRS_PAGE_TASK_RETRY_DELAY_MS);
      }
    }
  }
  throw lastError;
}

async function navigateTabToIfrsVariant(tabId, url, targetVariantValue) {
  const currentTab = await chrome.tabs.get(tabId);
  if (isIfrsNavigationTargetReached(currentTab.url, targetVariantValue) && currentTab.status === "complete") {
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
      reject(new Error(`Timed out while navigating tab ${tabId} to IFRS variant ${targetVariantValue}`));
    }, 15000);

    const listener = (updatedTabId, changeInfo, updatedTab) => {
      if (updatedTabId !== tabId) {
        return;
      }
      if (changeInfo.status !== "complete") {
        return;
      }
      const updatedUrl = updatedTab.url ?? updatedTab.pendingUrl;
      if (!isIfrsNavigationTargetReached(updatedUrl, targetVariantValue)) {
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

function isIfrsNavigationTargetReached(currentUrl, targetVariantValue) {
  if (currentUrl === undefined || currentUrl === null) {
    return false;
  }

  const targetVariantStem = targetVariantValue.trim().replace(/\.html?$/i, "").replace(/\/$/, "");
  try {
    const currentPathname = new URL(currentUrl).pathname;
    return currentPathname.includes(targetVariantStem);
  } catch {
    return currentUrl.includes(targetVariantStem);
  }
}

async function runIfrsPageTask(task) {
  function normalizeWhitespace(value) {
    return (value ?? "").replace(/\s+/g, " ").trim();
  }

  function getShellCanonicalUrl() {
    const shellCanonicalUrl = document.querySelector('link[rel="canonical"]')?.href;
    if (!shellCanonicalUrl) {
      throw new Error("IFRS page is missing link[rel=\"canonical\"]");
    }
    return shellCanonicalUrl;
  }

  function getCheckedVariantInput() {
    const checkedInput = Array.from(document.querySelectorAll('input[name="documentType"]'))
      .find((input) => input instanceof HTMLInputElement && input.checked);
    return checkedInput instanceof HTMLInputElement ? checkedInput : null;
  }

  function resolveVariantLabel(checkedInput) {
    const labelNode = checkedInput.nextElementSibling;
    if (!(labelNode instanceof HTMLElement)) {
      throw new Error("IFRS page is missing the checked documentType label element");
    }
    const label = normalizeWhitespace(labelNode.textContent || "");
    if (!label) {
      throw new Error("IFRS page is missing the checked documentType label text");
    }
    return label;
  }

  function getAvailableDocuments() {
    return Array.from(document.querySelectorAll('input[name="documentType"]'))
      .filter((input) => input instanceof HTMLInputElement)
      .map((input) => ({
        value: normalizeWhitespace(input.value),
        label: resolveVariantLabel(input),
        disabled: input.disabled,
        checked: input.checked,
      }));
  }

  function getCorpusTargets() {
    return Array.from(document.querySelectorAll("div.ifrs-cmp-standards__group__tile"))
      .map((tile, index) => {
        const anchor = tile.querySelector("a[href]");
        if (!(anchor instanceof HTMLAnchorElement)) {
          return null;
        }
        const rawHref = normalizeWhitespace(anchor.getAttribute("href") || "");
        if (!rawHref || rawHref.startsWith("#") || rawHref.toLowerCase().startsWith("javascript:")) {
          return null;
        }
        const url = new URL(rawHref, window.location.href).toString();
        const title = normalizeWhitespace(anchor.textContent || tile.textContent || `document-${index + 1}`);
        return {
          url,
          title,
        };
      })
      .filter((target) => target !== null);
  }

  function getAnnotationCheckbox() {
    const checkbox = document.querySelector("#annotation-checkbox");
    return checkbox instanceof HTMLInputElement ? checkbox : null;
  }

  function getAnnotationToggleLabel() {
    const checkbox = getAnnotationCheckbox();
    if (checkbox === null) {
      return null;
    }
    const label = checkbox.closest("label");
    return label instanceof HTMLElement ? label : null;
  }

  function getDcIdentifier() {
    return document.querySelector('meta[name="DC.Identifier"]')?.getAttribute("content") ?? "";
  }

  function getContentRoot() {
    return document.querySelector(".ifrs-cmp-htmlviewer")
      ?? document.querySelector("main")
      ?? document.body;
  }

  function buildPageSignature() {
    const checkedVariantInput = getCheckedVariantInput();
    const contentRoot = getContentRoot();
    const contentText = normalizeWhitespace(contentRoot?.textContent || "").slice(0, 500);
    const annotationCheckbox = getAnnotationCheckbox();
    const annotationState = annotationCheckbox?.checked ? "on" : "off";
    const annotationTableCount = document.querySelectorAll("table.edu_fn_table").length;
    return [
      window.location.href,
      document.title,
      getDcIdentifier(),
      checkedVariantInput?.value || "",
      annotationState,
      String(annotationTableCount),
      contentText,
    ].join("::");
  }

  function sleep(durationMs) {
    return new Promise((resolve) => {
      window.setTimeout(resolve, durationMs);
    });
  }

  async function waitFor(predicate, timeoutMs, errorMessage) {
    const startedAt = Date.now();
    while (Date.now() - startedAt < timeoutMs) {
      if (predicate()) {
        return;
      }
      await sleep(100);
    }
    throw new Error(errorMessage);
  }

  async function waitForStablePage(expectedVariantValue = "") {
    if (expectedVariantValue) {
      await waitFor(
        () => getCheckedVariantInput()?.value === expectedVariantValue,
        10000,
        `Timed out while waiting for IFRS variant ${expectedVariantValue}`,
      );
    }

    await waitFor(
      () => getCheckedVariantInput() !== null && getDcIdentifier() !== "",
      10000,
      "Timed out while waiting for IFRS page metadata",
    );

    let previousSignature = buildPageSignature();
    let stableIterations = 0;
    const startedAt = Date.now();
    while (Date.now() - startedAt < 10000) {
      await sleep(150);
      const nextSignature = buildPageSignature();
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
    throw new Error("Timed out while waiting for stable IFRS content");
  }

  async function ensureAnnotationsEnabled() {
    const annotationCheckbox = getAnnotationCheckbox();
    if (annotationCheckbox === null) {
      return { annotationAvailable: false, annotationEnabled: false };
    }

    if (!annotationCheckbox.checked) {
      const annotationToggleLabel = getAnnotationToggleLabel();
      if (annotationToggleLabel !== null) {
        annotationToggleLabel.click();
      } else {
        annotationCheckbox.click();
      }
      await waitFor(
        () => getAnnotationCheckbox()?.checked === true,
        5000,
        "Timed out while enabling IFRS annotations",
      );
    }

    await waitForStablePage(getCheckedVariantInput()?.value || "");
    return { annotationAvailable: true, annotationEnabled: true };
  }

  async function selectVariant(targetVariantValue) {
    const normalizedTargetVariantValue = normalizeWhitespace(targetVariantValue);
    const targetInput = Array.from(document.querySelectorAll('input[name="documentType"]'))
      .find((input) => input instanceof HTMLInputElement && normalizeWhitespace(input.value) === normalizedTargetVariantValue);
    if (!(targetInput instanceof HTMLInputElement)) {
      throw new Error(`IFRS page is missing documentType option ${normalizedTargetVariantValue}`);
    }
    if (targetInput.disabled) {
      throw new Error(`IFRS documentType option is disabled: ${normalizedTargetVariantValue}`);
    }
    if (!targetInput.checked) {
      const optionContainer = targetInput.closest(".custom-select-option");
      const priorSignature = buildPageSignature();
      if (optionContainer instanceof HTMLElement) {
        optionContainer.click();
      }
      if (!targetInput.checked) {
        targetInput.click();
      }
      if (!targetInput.checked) {
        targetInput.checked = true;
        targetInput.dispatchEvent(new Event("input", { bubbles: true }));
        targetInput.dispatchEvent(new Event("change", { bubbles: true }));
      }
      await waitFor(
        () => getCheckedVariantInput()?.value === normalizedTargetVariantValue,
        10000,
        `Timed out while selecting IFRS variant ${normalizedTargetVariantValue}`,
      );
      await waitForStablePage(normalizedTargetVariantValue);
      await waitFor(
        () => buildPageSignature() !== priorSignature || getCheckedVariantInput()?.value === normalizedTargetVariantValue,
        5000,
        `Timed out while waiting for IFRS variant ${normalizedTargetVariantValue} to apply`,
      );
    } else {
      await waitForStablePage(normalizedTargetVariantValue);
    }

    return {
      currentUrl: window.location.href,
      currentVariantValue: normalizedTargetVariantValue,
    };
  }

  function captureCurrentVariant() {
    const shellCanonicalUrl = getShellCanonicalUrl();
    const checkedVariantInput = getCheckedVariantInput();
    if (!(checkedVariantInput instanceof HTMLInputElement)) {
      throw new Error("IFRS page is missing a checked documentType input");
    }

    const variantValue = normalizeWhitespace(checkedVariantInput.value);
    if (!variantValue) {
      throw new Error("IFRS page has an empty checked documentType value");
    }

    const variantLabel = resolveVariantLabel(checkedVariantInput);
    const dcIdentifier = getDcIdentifier();
    const documentType = resolveIfrsDocumentType(dcIdentifier, variantLabel);
    const canonicalUrl = `${shellCanonicalUrl}${variantValue}`;
    const baseTitle = normalizeWhitespace(document.title || shellCanonicalUrl);
    const title = variantLabel === "Standard" ? baseTitle : `${baseTitle} - ${variantLabel}`;

    return {
      html: document.documentElement.outerHTML,
      sidecar: {
        url: window.location.href,
        title,
        captured_at: new Date().toISOString().replace(/\.\d{3}Z$/, "Z"),
        source_domain: window.location.hostname,
        canonical_url: canonicalUrl,
        document_type: documentType,
        extension_version: chrome.runtime.getManifest().version,
        content_type: document.contentType || "text/html",
      },
    };
  }

  switch (task.type) {
    case "inspectContext": {
      const corpusTargets = getCorpusTargets();
      if (corpusTargets.length > 1) {
        return {
          mode: "corpus",
          currentUrl: window.location.href,
          corpusTargets,
        };
      }
      return {
        mode: "page",
        currentUrl: window.location.href,
      };
    }
    case "inspectCaptureTargets": {
      await waitForStablePage();
      const checkedVariantInput = getCheckedVariantInput();
      if (checkedVariantInput === null) {
        throw new Error("IFRS page is missing a checked documentType input");
      }
      return {
        currentUrl: window.location.href,
        shellCanonicalUrl: getShellCanonicalUrl(),
        currentVariantValue: normalizeWhitespace(checkedVariantInput.value),
        availableDocuments: getAvailableDocuments(),
      };
    }
    case "selectVariant":
      return selectVariant(task.targetVariantValue ?? "");
    case "captureCurrentVariant": {
      await waitForStablePage(task.expectedVariantValue ?? "");
      await ensureAnnotationsEnabled();
      await waitForStablePage(task.expectedVariantValue ?? "");
      const capture = captureCurrentVariant();
      console.info("[IFRS Expert Extract] Capturing IFRS page in tab.", {
        url: capture.sidecar.url,
        canonicalUrl: capture.sidecar.canonical_url,
        title: capture.sidecar.title,
        documentType: capture.sidecar.document_type,
      });
      return capture;
    }
    default:
      throw new Error(`Unsupported IFRS page task: ${task.type}`);
  }
}
