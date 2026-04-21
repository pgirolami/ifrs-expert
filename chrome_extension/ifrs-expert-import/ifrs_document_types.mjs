export function resolveIfrsDocumentType(docUid, variantLabel) {
  const normalizedDocUid = String(docUid).trim().toLowerCase();
  if (!normalizedDocUid) {
    throw new Error('IFRS page is missing meta[name="DC.Identifier"] content');
  }

  const normalizedVariantLabel = normalizeVariantLabel(variantLabel);

  if (normalizedDocUid.startsWith("ifrs")) {
    const variantDocumentTypes = {
      standard: "IFRS-S",
      "basis for conclusions": "IFRS-BC",
      "basis for conclusions iasc": "IFRS-BC",
      "illustrative examples": "IFRS-IE",
      "implementation guidance": "IFRS-IG",
    };
    const resolvedDocumentType = variantDocumentTypes[normalizedVariantLabel];
    if (!resolvedDocumentType) {
      throw new Error(`Unsupported IFRS variant label: ${variantLabel}`);
    }
    return resolvedDocumentType;
  }

  if (normalizedDocUid.startsWith("ias")) {
    const variantDocumentTypes = {
      standard: "IAS-S",
      "basis for conclusions": "IAS-BC",
      "basis for conclusions iasc": "IAS-BCIASC",
      "illustrative examples": "IAS-IE",
      "implementation guidance": "IAS-IG",
      "supporting materials": "IAS-SM",
    };
    const resolvedDocumentType = variantDocumentTypes[normalizedVariantLabel];
    if (!resolvedDocumentType) {
      throw new Error(`Unsupported IAS variant label: ${variantLabel}`);
    }
    return resolvedDocumentType;
  }
  if (normalizedDocUid.startsWith("ifric")) {
    const variantDocumentTypes = {
      standard: "IFRIC",
      "basis for conclusions": "IFRIC-BC",
      "illustrative examples": "IFRIC-IE",
      "implementation guidance": "IFRIC-IG",
    };
    const resolvedDocumentType = variantDocumentTypes[normalizedVariantLabel];
    if (!resolvedDocumentType) {
      throw new Error(`Unsupported IFRIC variant label: ${variantLabel}`);
    }
    return resolvedDocumentType;
  }
  if (normalizedDocUid.startsWith("sic")) {
    const variantDocumentTypes = {
      standard: "SIC",
      "basis for conclusions": "SIC-BC",
      "illustrative examples": "SIC-IE",
    };
    const resolvedDocumentType = variantDocumentTypes[normalizedVariantLabel];
    if (!resolvedDocumentType) {
      throw new Error(`Unsupported SIC variant label: ${variantLabel}`);
    }
    return resolvedDocumentType;
  }
  if (normalizedDocUid.startsWith("ps")) {
    const variantDocumentTypes = {
      standard: "PS",
      "basis for conclusions": "PS-BC",
    };
    const resolvedDocumentType = variantDocumentTypes[normalizedVariantLabel];
    if (!resolvedDocumentType) {
      throw new Error(`Unsupported PS variant label: ${variantLabel}`);
    }
    return resolvedDocumentType;
  }

  throw new Error(`Unsupported IFRS-side document identifier: ${docUid}`);
}

function normalizeVariantLabel(variantLabel) {
  return String(variantLabel).trim().toLowerCase().replace(/\s+/g, " ");
}
