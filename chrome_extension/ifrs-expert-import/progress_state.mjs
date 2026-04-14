const MAX_LOG_ENTRIES = 200;

export function createImportProgressState() {
  return {
    status: "idle",
    sourceFamily: "",
    jobType: "",
    title: "No active import",
    totalPages: 0,
    completedPages: 0,
    failedPages: 0,
    savedArtifacts: 0,
    currentPageTitle: "",
    currentPageUrl: "",
    currentPageIndex: 0,
    currentVariantLabel: "",
    currentVariantIndex: 0,
    currentVariantCount: 0,
    currentPhaseLabel: "",
    cancelRequested: false,
    startedAt: "",
    finishedAt: "",
    logs: [],
    failures: [],
  };
}

export function reduceImportProgressState(currentState, event) {
  const state = currentState ?? createImportProgressState();
  switch (event.type) {
    case "jobStarted":
      return appendLog(
        {
          ...createImportProgressState(),
          status: "running",
          sourceFamily: event.sourceFamily,
          jobType: event.jobType,
          title: event.title,
          totalPages: event.totalPages,
          cancelRequested: false,
          startedAt: event.startedAt,
        },
        {
          level: "info",
          message: event.logMessage ?? event.title,
        },
      );
    case "pageStarted":
      return appendLog(
        {
          ...state,
          currentPageTitle: event.pageTitle,
          currentPageUrl: event.pageUrl,
          currentPageIndex: event.pageIndex,
          currentVariantLabel: "",
          currentVariantIndex: 0,
          currentVariantCount: 0,
          currentPhaseLabel: "",
        },
        {
          level: "info",
          message: event.logMessage ?? `Started ${event.pageTitle}`,
        },
      );
    case "variantStarted":
      return appendLog(
        {
          ...state,
          currentVariantLabel: event.variantLabel,
          currentVariantIndex: event.variantIndex,
          currentVariantCount: event.variantCount,
        },
        {
          level: "info",
          message: event.logMessage ?? `Importing ${event.variantLabel}`,
        },
      );
    case "phaseUpdated":
      return event.logMessage
        ? appendLog(
            {
              ...state,
              currentPhaseLabel: event.phaseLabel,
            },
            {
              level: event.level ?? "info",
              message: event.logMessage,
            },
          )
        : {
            ...state,
            currentPhaseLabel: event.phaseLabel,
          };
    case "cancelRequested":
      return appendLog(
        {
          ...state,
          cancelRequested: true,
          currentPhaseLabel: "Stopping…",
        },
        {
          level: event.level ?? "info",
          message: event.logMessage ?? "Stop requested by user",
        },
      );
    case "artifactSaved":
      return appendLog(
        {
          ...state,
          savedArtifacts: state.savedArtifacts + (event.count ?? 1),
        },
        {
          level: "info",
          message: event.logMessage ?? `Saved ${event.basename}`,
        },
      );
    case "pageCompleted":
      return appendLog(
        {
          ...state,
          completedPages: Math.min(state.completedPages + 1, state.totalPages || state.completedPages + 1),
          currentVariantLabel: "",
          currentVariantIndex: 0,
          currentVariantCount: 0,
          currentPhaseLabel: "",
        },
        {
          level: "info",
          message: event.logMessage ?? `Completed ${event.pageTitle}`,
        },
      );
    case "pageFailed":
      return appendLog(
        {
          ...state,
          completedPages: Math.min(state.completedPages + 1, state.totalPages || state.completedPages + 1),
          failedPages: state.failedPages + 1,
          failures: [
            ...state.failures,
            {
              pageTitle: event.pageTitle,
              pageUrl: event.pageUrl,
              error: event.error,
            },
          ],
          currentVariantLabel: "",
          currentVariantIndex: 0,
          currentVariantCount: 0,
          currentPhaseLabel: "",
        },
        {
          level: "error",
          message: event.logMessage ?? `Failed ${event.pageTitle}: ${event.error}`,
        },
      );
    case "pageSkipped":
      return appendLog(
        {
          ...state,
          completedPages: Math.min(state.completedPages + 1, state.totalPages || state.completedPages + 1),
          currentVariantLabel: "",
          currentVariantIndex: 0,
          currentVariantCount: 0,
          currentPhaseLabel: "",
        },
        {
          level: "info",
          message: event.logMessage ?? `Skipped ${event.pageTitle}`,
        },
      );
    case "logAppended":
      return appendLog(state, {
        level: event.level,
        message: event.message,
      });
    case "jobCompleted": {
      const finalStatus = state.failedPages > 0 ? "partial" : "success";
      return appendLog(
        {
          ...state,
          status: finalStatus,
          finishedAt: event.finishedAt,
          completedPages: state.totalPages > 0 ? Math.max(state.completedPages, Math.min(event.completedPages ?? state.completedPages, state.totalPages)) : state.completedPages,
          currentVariantLabel: "",
          currentVariantIndex: 0,
          currentVariantCount: 0,
          currentPhaseLabel: "",
          cancelRequested: false,
        },
        {
          level: finalStatus === "success" ? "info" : "error",
          message: event.logMessage ?? event.summary,
        },
      );
    }
    case "jobCancelled":
      return appendLog(
        {
          ...state,
          status: "cancelled",
          finishedAt: event.finishedAt,
          currentPhaseLabel: "",
          cancelRequested: false,
        },
        {
          level: "info",
          message: event.logMessage ?? event.summary ?? "Import cancelled by user",
        },
      );
    case "jobFailed":
      return appendLog(
        {
          ...state,
          status: "error",
          finishedAt: event.finishedAt,
          currentPhaseLabel: "",
          cancelRequested: false,
        },
        {
          level: "error",
          message: event.logMessage ?? event.error,
        },
      );
    default:
      return state;
  }
}

export function calculateProgressPercent(state) {
  if (state.totalPages <= 0) {
    return 0;
  }
  return Math.max(0, Math.min(100, Math.round((state.completedPages / state.totalPages) * 100)));
}

function appendLog(state, logEntry) {
  const timestamp = new Date().toISOString();
  return {
    ...state,
    logs: [...state.logs, { ...logEntry, timestamp }].slice(-MAX_LOG_ENTRIES),
  };
}
