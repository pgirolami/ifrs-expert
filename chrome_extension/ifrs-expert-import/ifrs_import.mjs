export function normalizeIfrsVariantPathStem(variantValue) {
  return String(variantValue).trim().replace(/\.html?$/i, "").replace(/\/$/, "");
}

export function normalizeIfrsVariantPathForNavigation(variantValue) {
  return `${normalizeIfrsVariantPathStem(variantValue)}/`;
}

export function selectIfrsCaptureTargets(availableDocuments) {
  return availableDocuments.filter((documentOption) => {
    return Boolean(documentOption?.value) && documentOption.disabled !== true;
  });
}

export function buildIfrsVariantNavigationUrl({
  currentUrl,
  currentVariantValue,
  targetVariantValue,
  shellCanonicalUrl,
}) {
  const normalizedCurrentVariantPath = normalizeIfrsVariantPathForNavigation(currentVariantValue);
  const normalizedTargetVariantPath = normalizeIfrsVariantPathForNavigation(targetVariantValue);
  const currentVariantStem = normalizeIfrsVariantPathStem(currentVariantValue);
  const targetVariantStem = normalizeIfrsVariantPathStem(targetVariantValue);
  const trimmedCurrentVariantValue = String(currentVariantValue).trim();
  const trimmedTargetVariantValue = String(targetVariantValue).trim();

  const rewriteCandidates = [
    [trimmedCurrentVariantValue, trimmedTargetVariantValue],
    [normalizedCurrentVariantPath, normalizedTargetVariantPath],
    [currentVariantStem, targetVariantStem],
  ];
  for (const [sourceToken, targetToken] of rewriteCandidates) {
    if (sourceToken && currentUrl.includes(sourceToken)) {
      return currentUrl.replace(sourceToken, targetToken);
    }
  }

  return `${shellCanonicalUrl}${trimmedTargetVariantValue}`;
}
