import { calculateProgressPercent, createImportProgressState } from "./progress_state.mjs";

const STORAGE_KEY = "importProgressState";

const elements = {
  jobTitle: document.getElementById("job-title"),
  jobStatus: document.getElementById("job-status"),
  progressSummary: document.getElementById("progress-summary"),
  progressBarFill: document.getElementById("progress-bar-fill"),
  savedArtifacts: document.getElementById("saved-artifacts"),
  failedPages: document.getElementById("failed-pages"),
  currentPageTitle: document.getElementById("current-page-title"),
  currentPageMeta: document.getElementById("current-page-meta"),
  currentVariantTitle: document.getElementById("current-variant-title"),
  currentVariantMeta: document.getElementById("current-variant-meta"),
  failureList: document.getElementById("failure-list"),
  logList: document.getElementById("log-list"),
};

async function main() {
  const stored = await chrome.storage.session.get(STORAGE_KEY);
  render(stored[STORAGE_KEY] ?? createImportProgressState());
  chrome.storage.onChanged.addListener((changes, areaName) => {
    if (areaName !== "session") {
      return;
    }
    const stateChange = changes[STORAGE_KEY];
    if (stateChange?.newValue) {
      render(stateChange.newValue);
    }
  });
}

function render(state) {
  const progressPercent = calculateProgressPercent(state);
  elements.jobTitle.textContent = state.title || "No active import";
  elements.jobStatus.textContent = humanizeStatus(state.status);
  elements.jobStatus.className = `status status--${state.status || "idle"}`;
  elements.progressSummary.textContent = `${state.completedPages} / ${state.totalPages} pages`;
  elements.progressBarFill.style.width = `${progressPercent}%`;
  elements.savedArtifacts.textContent = String(state.savedArtifacts);
  elements.failedPages.textContent = String(state.failedPages);
  elements.currentPageTitle.textContent = state.currentPageTitle || "—";
  elements.currentPageMeta.textContent = state.currentPageIndex > 0 && state.totalPages > 0
    ? `Page ${state.currentPageIndex} of ${state.totalPages}`
    : "Waiting to start";
  elements.currentVariantTitle.textContent = state.currentVariantLabel || "—";
  elements.currentVariantMeta.textContent = state.currentVariantIndex > 0 && state.currentVariantCount > 0
    ? `Variant ${state.currentVariantIndex} of ${state.currentVariantCount}`
    : "No active variant";
  renderFailures(state.failures);
  renderLogs(state.logs);
}

function renderFailures(failures) {
  elements.failureList.replaceChildren();
  if (!failures.length) {
    const item = document.createElement("li");
    item.className = "muted";
    item.textContent = "No failures";
    elements.failureList.appendChild(item);
    return;
  }

  for (const failure of failures) {
    const item = document.createElement("li");
    item.innerHTML = `<strong>${escapeHtml(failure.pageTitle)}</strong><br><span class="list__error">${escapeHtml(failure.error)}</span>`;
    elements.failureList.appendChild(item);
  }
}

function renderLogs(logs) {
  elements.logList.replaceChildren();
  if (!logs.length) {
    const item = document.createElement("li");
    item.className = "muted";
    item.textContent = "No logs yet";
    elements.logList.appendChild(item);
    return;
  }

  for (const logEntry of logs.slice().reverse()) {
    const item = document.createElement("li");
    const time = new Date(logEntry.timestamp).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
    const levelClass = logEntry.level === "error" ? "list__error" : "";
    item.innerHTML = `<span class="list__time">${escapeHtml(time)}</span><span class="${levelClass}">${escapeHtml(logEntry.message)}</span>`;
    elements.logList.appendChild(item);
  }
}

function humanizeStatus(status) {
  switch (status) {
    case "running":
      return "Running";
    case "success":
      return "Completed";
    case "partial":
      return "Completed with failures";
    case "error":
      return "Failed";
    default:
      return "Idle";
  }
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

void main();
