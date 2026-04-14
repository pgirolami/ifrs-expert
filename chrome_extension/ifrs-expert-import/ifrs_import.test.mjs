import test from "node:test";
import assert from "node:assert/strict";

import {
  buildIfrsVariantNavigationUrl,
  extractIfrsDocumentNavigationToken,
  selectIfrsCaptureTargets,
  selectIfrsCorpusTargets,
} from "./ifrs_import.mjs";

test("selectIfrsCaptureTargets keeps selectable IFRS variants in DOM order", () => {
  const targets = selectIfrsCaptureTargets([
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
      label: "Standard",
      disabled: false,
    },
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-ie.html",
      label: "Illustrative Examples",
      disabled: true,
    },
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-ig.html",
      label: "Implementation Guidance",
      disabled: false,
    },
    {
      value: "",
      label: "Broken option",
      disabled: false,
    },
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-bc.html",
      label: "Basis for Conclusions",
      disabled: false,
    },
  ]);

  assert.deepEqual(targets, [
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
      label: "Standard",
      disabled: false,
    },
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-ig.html",
      label: "Implementation Guidance",
      disabled: false,
    },
    {
      value: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-bc.html",
      label: "Basis for Conclusions",
      disabled: false,
    },
  ]);
});

test("buildIfrsVariantNavigationUrl swaps the active IFRS variant in the pretty URL", () => {
  const currentUrl = "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-ig/";
  const currentVariantValue = "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-ig.html";
  const targetVariantValue = "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-bc.html";
  const shellCanonicalUrl = "https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-9-financial-instruments.html";

  const targetUrl = buildIfrsVariantNavigationUrl({
    currentUrl,
    currentVariantValue,
    targetVariantValue,
    shellCanonicalUrl,
  });

  assert.equal(
    targetUrl,
    "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-bc/",
  );
});

test("extractIfrsDocumentNavigationToken handles content and pretty IFRS URLs", () => {
  assert.equal(
    extractIfrsDocumentNavigationToken(
      "https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-1.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs1.html",
    ),
    "ifrs1",
  );
  assert.equal(
    extractIfrsDocumentNavigationToken(
      "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-1.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs1/",
    ),
    "ifrs1",
  );
});

test("selectIfrsCorpusTargets keeps unique document links in order", () => {
  const targets = selectIfrsCorpusTargets([
    {
      url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-1.html",
      title: "IFRS 1",
    },
    {
      url: "",
      title: "Broken tile",
    },
    {
      url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-2.html",
      title: "IFRS 2",
    },
    {
      url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-1.html",
      title: "Duplicate IFRS 1",
    },
  ]);

  assert.deepEqual(targets, [
    {
      url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-1.html",
      title: "IFRS 1",
    },
    {
      url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-2.html",
      title: "IFRS 2",
    },
  ]);
});

test("buildIfrsVariantNavigationUrl falls back to shell canonical when the current URL cannot be rewritten", () => {
  const targetUrl = buildIfrsVariantNavigationUrl({
    currentUrl: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html",
    currentVariantValue: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-ig.html",
    targetVariantValue: "/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
    shellCanonicalUrl: "https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-9-financial-instruments.html",
  });

  assert.equal(
    targetUrl,
    "https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
  );
});
