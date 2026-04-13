ALTER TABLE documents ADD COLUMN source_domain TEXT;

UPDATE documents
SET source_domain = CASE
    WHEN canonical_url LIKE 'https://abonnes.efl.fr/%' THEN 'abonnes.efl.fr'
    WHEN canonical_url LIKE 'https://ifrs.org/%' THEN 'ifrs.org'
    WHEN canonical_url LIKE 'https://%.ifrs.org/%' THEN substr(
        replace(canonical_url, 'https://', ''),
        1,
        instr(replace(canonical_url, 'https://', ''), '/') - 1
    )
    ELSE NULL
END
WHERE source_domain IS NULL;
