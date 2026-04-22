import test from "node:test";
import assert from "node:assert/strict";

import {
  buildIfrsVariantNavigationUrl,
  extractIfrsDocumentNavigationToken,
  selectIfrsCaptureTargets,
  selectIfrsCorpusTargets,
} from "./ifrs_import.mjs";
import { resolveIfrsDocumentType } from "./ifrs_document_types.mjs";

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

test("resolveIfrsDocumentType maps IAS document UIDs to exact IAS variants", () => {
  assert.equal(resolveIfrsDocumentType("ias21", "Standard"), "IAS-S");
  assert.equal(resolveIfrsDocumentType("ias21-bc", "Basis for Conclusions"), "IAS-BC");
  assert.equal(resolveIfrsDocumentType("ias21-bc", "Basis for Conclusions IASC"), "IAS-BCIASC");
  assert.equal(resolveIfrsDocumentType("ias21-ie", "Illustrative Examples"), "IAS-IE");
  assert.equal(resolveIfrsDocumentType("ias21-ig", "Implementation Guidance"), "IAS-IG");
  assert.equal(resolveIfrsDocumentType("ias28-sm", "Supporting Materials"), "IAS-SM");
  assert.equal(resolveIfrsDocumentType("ias28-sm", "Supporting material"), "IAS-SM");
});

test("resolveIfrsDocumentType maps IFRIC, SIC, and PS variants to the same types as Python", () => {
  assert.equal(resolveIfrsDocumentType("ifric16", "Standard"), "IFRIC");
  assert.equal(resolveIfrsDocumentType("ifric16-bc", "Basis for Conclusions"), "IFRIC-BC");
  assert.equal(resolveIfrsDocumentType("ifric16-ie", "Illustrative Examples"), "IFRIC-IE");
  assert.equal(resolveIfrsDocumentType("ifric16-ig", "Implementation Guidance"), "IFRIC-IG");
  assert.equal(resolveIfrsDocumentType("sic25", "Standard"), "SIC");
  assert.equal(resolveIfrsDocumentType("sic25-bc", "Basis for Conclusions"), "SIC-BC");
  assert.equal(resolveIfrsDocumentType("sic25-ie", "Illustrative Examples"), "SIC-IE");
  assert.equal(resolveIfrsDocumentType("ps1", "Standard"), "PS");
  assert.equal(resolveIfrsDocumentType("ps1-bc", "Basis for Conclusions"), "PS-BC");
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
