import test from "node:test";
import assert from "node:assert/strict";

import {
  calculateProgressPercent,
  createImportProgressState,
  reduceImportProgressState,
} from "./progress_state.mjs";

test("job lifecycle tracks page progress and artifacts", () => {
  let state = createImportProgressState();

  state = reduceImportProgressState(state, {
    type: "jobStarted",
    sourceFamily: "ifrs",
    jobType: "ifrs-corpus",
    title: "IFRS corpus import",
    totalPages: 3,
    startedAt: "2026-04-14T12:00:00Z",
  });
  state = reduceImportProgressState(state, {
    type: "pageStarted",
    pageTitle: "IFRS 1",
    pageUrl: "https://example.com/ifrs1",
    pageIndex: 1,
  });
  state = reduceImportProgressState(state, {
    type: "variantStarted",
    variantLabel: "Standard",
    variantIndex: 1,
    variantCount: 3,
  });
  state = reduceImportProgressState(state, {
    type: "artifactSaved",
    basename: "20260414T120000Z--ifrs1",
  });
  state = reduceImportProgressState(state, {
    type: "pageCompleted",
    pageTitle: "IFRS 1",
  });
  state = reduceImportProgressState(state, {
    type: "jobCompleted",
    finishedAt: "2026-04-14T12:10:00Z",
    summary: "Saved 1 IFRS capture",
  });

  assert.equal(state.status, "success");
  assert.equal(state.completedPages, 1);
  assert.equal(state.savedArtifacts, 1);
  assert.equal(calculateProgressPercent(state), 33);
  assert.equal(state.logs.at(-1)?.message, "Saved 1 IFRS capture");
});

test("page failures mark the run as partial on completion", () => {
  let state = reduceImportProgressState(createImportProgressState(), {
    type: "jobStarted",
    sourceFamily: "ifrs",
    jobType: "ifrs-corpus",
    title: "IFRS corpus import",
    totalPages: 2,
    startedAt: "2026-04-14T12:00:00Z",
  });

  state = reduceImportProgressState(state, {
    type: "pageFailed",
    pageTitle: "Conceptual Framework",
    pageUrl: "https://example.com/cf",
    error: "capture failed",
  });
  state = reduceImportProgressState(state, {
    type: "jobCompleted",
    finishedAt: "2026-04-14T12:10:00Z",
    summary: "Saved 0 IFRS captures; 1 page failed",
  });

  assert.equal(state.status, "partial");
  assert.equal(state.failedPages, 1);
  assert.equal(state.failures[0]?.pageTitle, "Conceptual Framework");
  assert.equal(calculateProgressPercent(state), 50);
});

test("phase updates track the current page activity", () => {
  let state = reduceImportProgressState(createImportProgressState(), {
    type: "jobStarted",
    sourceFamily: "ifrs",
    jobType: "ifrs-corpus",
    title: "IFRS corpus import",
    totalPages: 2,
    startedAt: "2026-04-14T12:00:00Z",
  });

  state = reduceImportProgressState(state, {
    type: "phaseUpdated",
    phaseLabel: "Parsing…",
    logMessage: "Parsing Standard",
  });

  assert.equal(state.currentPhaseLabel, "Parsing…");
  assert.equal(state.logs.at(-1)?.message, "Parsing Standard");
});

test("page skips advance progress without failures", () => {
  let state = reduceImportProgressState(createImportProgressState(), {
    type: "jobStarted",
    sourceFamily: "ifrs",
    jobType: "ifrs-corpus",
    title: "IFRS corpus import",
    totalPages: 2,
    startedAt: "2026-04-14T12:00:00Z",
  });

  state = reduceImportProgressState(state, {
    type: "pageSkipped",
    pageTitle: "Conceptual Framework for Financial Reporting",
    logMessage: "Skipped Conceptual Framework for Financial Reporting",
  });

  assert.equal(state.completedPages, 1);
  assert.equal(state.failedPages, 0);
  assert.equal(state.logs.at(-1)?.message, "Skipped Conceptual Framework for Financial Reporting");
});

test("job failures preserve the error state", () => {
  const state = reduceImportProgressState(
    reduceImportProgressState(createImportProgressState(), {
      type: "jobStarted",
      sourceFamily: "ifrs",
      jobType: "ifrs-page",
      title: "IFRS page import",
      totalPages: 1,
      startedAt: "2026-04-14T12:00:00Z",
    }),
    {
      type: "jobFailed",
      finishedAt: "2026-04-14T12:01:00Z",
      error: "Import failed",
    },
  );

  assert.equal(state.status, "error");
  assert.equal(state.logs.at(-1)?.message, "Import failed");
});
