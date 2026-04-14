import {
  ACTION_TITLE,
  SUPPORTED_ACTION_ICON_PATHS,
  UNSUPPORTED_ACTION_ICON_PATHS,
  UNSUPPORTED_ACTION_TITLE,
  formatErrorMessage,
  getSourceFamily,
  isImportCancellationError,
  logError,
  isSupportedTabUrl,
  logInfo,
  logWarn,
  openImportSidePanel,
  requestImportCancellation,
  resetImportProgress,
  runTask,
  showToastInTab,
  updateImportProgress,
} from "./background_common.mjs";
import {
  captureIfrsSource,
  resolveIfrsActionState,
} from "./ifrs_background.mjs";
import {
  captureNavisImport,
  resolveNavisActionState,
} from "./navis_background.mjs";

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

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message?.type !== "cancelImport") {
    return false;
  }

  void requestImportCancellation().then(() => {
    sendResponse({ ok: true });
  }).catch((error) => {
    sendResponse({ ok: false, error: formatErrorMessage(error) });
  });
  return true;
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

  openImportSidePanel(tab.id);
  await updateImportProgress({
    type: "jobStarted",
    sourceFamily,
    jobType: "initializing",
    title: "Starting extraction",
    totalPages: 0,
    startedAt: new Date().toISOString(),
    logMessage: `Preparing ${sourceFamily.toUpperCase()} extraction`,
  });

  try {
    if (sourceFamily === "navis") {
      await captureNavisImport(tab.id, tab.url ?? "");
      return;
    }

    await captureIfrsSource(tab.id, tab.url ?? "");
  } catch (error) {
    const errorMessage = formatErrorMessage(error);
    if (isImportCancellationError(error)) {
      logInfo("IFRS Expert extraction cancelled.", {
        tabId: tab.id,
        url: tab.url,
        error: errorMessage,
      });
      await updateImportProgress({
        type: "jobCancelled",
        finishedAt: new Date().toISOString(),
        summary: errorMessage,
      });
      await showToastInTab(tab.id, errorMessage, "success");
    } else {
      logError("IFRS Expert extraction failed.", {
        tabId: tab.id,
        url: tab.url,
        error: errorMessage,
      });
      await updateImportProgress({
        type: "jobFailed",
        finishedAt: new Date().toISOString(),
        error: errorMessage,
      });
      await showToastInTab(tab.id, `Extraction failed: ${errorMessage}`, "error");
    }
  } finally {
    logInfo("Extraction attempt finished.");
  }
});

async function initializeActionState(reason) {
  logInfo("Initializing action state.", { reason });
  await resetImportProgress();
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
    try {
      const ifrsActionState = await resolveIfrsActionState(tabId);
      return {
        ...ifrsActionState,
        iconPaths: SUPPORTED_ACTION_ICON_PATHS,
        sourceFamily,
      };
    } catch (error) {
      logWarn("Unable to inspect IFRS page state while resolving action state.", {
        tabId,
        tabUrl,
        error: formatErrorMessage(error),
      });
      return {
        enabled: true,
        title: ACTION_TITLE,
        iconPaths: SUPPORTED_ACTION_ICON_PATHS,
        sourceFamily,
        mode: "page",
      };
    }
  }

  const navisActionState = await resolveNavisActionState(tabId, tabUrl);
  return {
    ...navisActionState,
    iconPaths: navisActionState.enabled ? SUPPORTED_ACTION_ICON_PATHS : UNSUPPORTED_ACTION_ICON_PATHS,
    sourceFamily,
  };
}

