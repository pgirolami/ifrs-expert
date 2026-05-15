"""In-memory fakes for testing."""

from __future__ import annotations

from dataclasses import replace
from typing import TYPE_CHECKING, Self

from src.interfaces import ChunkStoreProtocol, DocumentStoreProtocol, ReferenceStoreProtocol, SearchResult, VectorStoreProtocol
from src.models.document import resolve_document_kind, resolve_document_type

if TYPE_CHECKING:
    from src.case_analysis.models import ApplicabilityAnalysisOutput, ApproachIdentificationOutput
    from src.models.chunk import Chunk
    from src.models.document import DocumentRecord
    from src.models.reference import ContentReference
    from src.models.section import SectionClosureRow, SectionRecord


class InMemoryChunkStore(ChunkStoreProtocol):
    """In-memory implementation of chunk storage for testing."""

    def __init__(self) -> None:
        self._chunks: list[Chunk] = []
        self._next_id = 1

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def insert_chunks(self, chunks: list[Chunk]) -> list[int]:
        ids: list[int] = []
        for chunk in chunks:
            row_id = chunk.id if chunk.id is not None else self._next_id
            self._next_id = max(self._next_id, row_id + 1)
            stored_chunk = replace(chunk, id=row_id)
            chunk.id = row_id
            self._chunks.append(stored_chunk)
            ids.append(row_id)
        return ids

    def get_chunks_by_doc(self, doc_uid: str) -> list[Chunk]:
        return [replace(chunk) for chunk in self._chunks if chunk.doc_uid == doc_uid]

    def get_all_docs(self) -> list[str]:
        return sorted({chunk.doc_uid for chunk in self._chunks})

    def delete_chunks_by_doc(self, doc_uid: str) -> int:
        original_count = len(self._chunks)
        self._chunks = [chunk for chunk in self._chunks if chunk.doc_uid != doc_uid]
        return original_count - len(self._chunks)

    def sync_containing_section_db_ids(
        self,
        doc_uid: str,
        section_db_id_by_source_id: dict[str, int],
    ) -> int:
        updated_count = 0
        updated_chunks: list[Chunk] = []
        for chunk in self._chunks:
            if chunk.doc_uid != doc_uid:
                updated_chunks.append(chunk)
                continue
            containing_section_db_id = None
            if chunk.containing_section_id is not None:
                containing_section_db_id = section_db_id_by_source_id.get(chunk.containing_section_id)
            updated_chunks.append(replace(chunk, containing_section_db_id=containing_section_db_id))
            updated_count += 1
        self._chunks = updated_chunks
        return updated_count

    def clear(self) -> None:
        self._chunks.clear()
        self._next_id = 1


class InMemorySectionStore:
    """In-memory implementation of section storage for testing."""

    def __init__(self) -> None:
        self._sections_by_key: dict[tuple[str, str], SectionRecord] = {}
        self._descendant_db_ids_by_ancestor_db_id: dict[int, list[int]] = {}
        self._closure_rows: list[SectionClosureRow] = []
        self._next_db_id = 1

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def insert_sections(self, sections: list[SectionRecord]) -> None:
        assigned_sections_by_key: dict[tuple[str, str], SectionRecord] = {}
        for section in sections:
            key = (section.doc_uid, section.section_id)
            if key in assigned_sections_by_key or key in self._sections_by_key:
                msg = f"Duplicate section business key: doc_uid={section.doc_uid}, section_id={section.section_id}"
                raise ValueError(msg)
            section_db_id = section.db_id if section.db_id is not None else self._next_db_id
            self._next_db_id = max(self._next_db_id, section_db_id + 1)
            assigned_sections_by_key[key] = replace(section, db_id=section_db_id, parent_section_db_id=None)

        self._sections_by_key.update(assigned_sections_by_key)

        updated_sections_by_key: dict[tuple[str, str], SectionRecord] = {}
        for key, section in self._sections_by_key.items():
            parent_section_db_id = None
            if section.parent_section_id is not None:
                parent_key = (section.doc_uid, section.parent_section_id)
                parent_section = self._sections_by_key.get(parent_key)
                if parent_section is not None:
                    parent_section_db_id = parent_section.db_id
            updated_sections_by_key[key] = replace(section, parent_section_db_id=parent_section_db_id)
        self._sections_by_key = updated_sections_by_key

    def insert_closure_rows(self, doc_uid: str, closure_rows: list[SectionClosureRow]) -> None:
        section_db_id_by_source_id = self.map_source_ids_to_db_ids(
            doc_uid=doc_uid,
            section_ids=[section_id for row in closure_rows for section_id in (row.ancestor_section_id, row.descendant_section_id)],
        )
        for row in closure_rows:
            ancestor_section_db_id = section_db_id_by_source_id[row.ancestor_section_id]
            descendant_section_db_id = section_db_id_by_source_id[row.descendant_section_id]
            translated_row = replace(
                row,
                ancestor_section_db_id=ancestor_section_db_id,
                descendant_section_db_id=descendant_section_db_id,
            )
            self._closure_rows.append(translated_row)
            self._descendant_db_ids_by_ancestor_db_id.setdefault(ancestor_section_db_id, [])
            if descendant_section_db_id not in self._descendant_db_ids_by_ancestor_db_id[ancestor_section_db_id]:
                self._descendant_db_ids_by_ancestor_db_id[ancestor_section_db_id].append(descendant_section_db_id)

    def get_sections_by_doc(self, doc_uid: str) -> list[SectionRecord]:
        sections = [section for section in self._sections_by_key.values() if section.doc_uid == doc_uid]
        return sorted(sections, key=lambda section: section.position)

    def get_section_by_source_id(self, doc_uid: str, section_id: str) -> SectionRecord | None:
        section = self._sections_by_key.get((doc_uid, section_id))
        if section is None:
            return None
        return replace(section)

    def get_descendant_section_db_ids(self, section_db_id: int) -> list[int]:
        return list(self._descendant_db_ids_by_ancestor_db_id.get(section_db_id, [section_db_id]))

    def map_source_ids_to_db_ids(self, doc_uid: str, section_ids: list[str]) -> dict[str, int]:
        section_db_id_by_source_id: dict[str, int] = {}
        for section_id in section_ids:
            section = self._sections_by_key.get((doc_uid, section_id))
            if section is None or section.db_id is None:
                continue
            section_db_id_by_source_id[section_id] = section.db_id
        return section_db_id_by_source_id

    def delete_sections_by_doc(self, doc_uid: str) -> int:
        keys_to_delete = [key for key, section in self._sections_by_key.items() if section.doc_uid == doc_uid]
        deleted_db_ids = {section.db_id for key, section in self._sections_by_key.items() if key in keys_to_delete and section.db_id is not None}
        for key in keys_to_delete:
            self._sections_by_key.pop(key, None)
        self._descendant_db_ids_by_ancestor_db_id = {
            ancestor_db_id: [descendant_db_id for descendant_db_id in descendant_db_ids if descendant_db_id not in deleted_db_ids]
            for ancestor_db_id, descendant_db_ids in self._descendant_db_ids_by_ancestor_db_id.items()
            if ancestor_db_id not in deleted_db_ids
        }
        self._closure_rows = [row for row in self._closure_rows if row.ancestor_section_db_id not in deleted_db_ids and row.descendant_section_db_id not in deleted_db_ids]
        return len(keys_to_delete)

    def add_descendant_mapping(
        self,
        section_id: str,
        descendant_ids: list[str],
        doc_uid: str | None = None,
    ) -> None:
        resolved_doc_uid = self._resolve_doc_uid(section_id=section_id, doc_uid=doc_uid)
        ancestor_section = self._sections_by_key.get((resolved_doc_uid, section_id))
        if ancestor_section is None or ancestor_section.db_id is None:
            msg = f"Unknown ancestor section: doc_uid={resolved_doc_uid}, section_id={section_id}"
            raise ValueError(msg)

        descendant_db_ids: list[int] = []
        for descendant_id in descendant_ids:
            descendant_section = self._sections_by_key.get((resolved_doc_uid, descendant_id))
            if descendant_section is None or descendant_section.db_id is None:
                msg = f"Unknown descendant section: doc_uid={resolved_doc_uid}, section_id={descendant_id}"
                raise ValueError(msg)
            descendant_db_ids.append(descendant_section.db_id)
        self._descendant_db_ids_by_ancestor_db_id[ancestor_section.db_id] = descendant_db_ids

    def _resolve_doc_uid(self, section_id: str, doc_uid: str | None) -> str:
        if doc_uid is not None:
            return doc_uid
        matching_doc_uids = sorted(stored_doc_uid for stored_doc_uid, stored_section_id in self._sections_by_key if stored_section_id == section_id)
        if len(matching_doc_uids) != 1:
            msg = f"Ambiguous section id without doc_uid: section_id={section_id}"
            raise ValueError(msg)
        return matching_doc_uids[0]


class InMemoryDocumentStore(DocumentStoreProtocol):
    """In-memory implementation of document storage for testing."""

    def __init__(self) -> None:
        self._documents: dict[str, DocumentRecord] = {}

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def upsert_document(self, document: DocumentRecord) -> None:
        document_type = resolve_document_type(document.doc_uid, document.document_type)
        document_kind = resolve_document_kind(document_type, document.document_kind)
        self._documents[document.doc_uid] = replace(
            document,
            document_type=document_type,
            document_kind=document_kind,
        )

    def get_document(self, doc_uid: str) -> DocumentRecord | None:
        document = self._documents.get(doc_uid)
        if document is None:
            return None
        return replace(document)


class InMemoryReferenceStore(ReferenceStoreProtocol):
    """In-memory implementation of reference storage for testing."""

    def __init__(self) -> None:
        self._references: list[ContentReference] = []
        self._next_id = 1

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def insert_references(self, references: list[ContentReference]) -> list[int]:
        ids: list[int] = []
        for reference in references:
            row_id = reference.id if reference.id is not None else self._next_id
            self._next_id = max(self._next_id, row_id + 1)
            stored_reference = replace(reference, id=row_id)
            reference.id = row_id
            self._references.append(stored_reference)
            ids.append(row_id)
        return ids

    def get_references_by_doc(self, doc_uid: str) -> list[ContentReference]:
        return [replace(reference) for reference in self._references if reference.source_doc_uid == doc_uid]

    def delete_references_by_doc(self, doc_uid: str) -> int:
        original_count = len(self._references)
        self._references = [reference for reference in self._references if reference.source_doc_uid != doc_uid]
        return original_count - len(self._references)


class RecordingVectorStore(VectorStoreProtocol):
    """Vector store fake that records operations for assertions."""

    def __init__(self, existing_doc_uids: set[str] | None = None) -> None:
        self.deleted_doc_uids: list[str] = []
        self.added_embeddings: list[tuple[str, list[int], list[str]]] = []
        self._embedding_counts: dict[str, int] = dict.fromkeys(existing_doc_uids or set(), 1)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        return []

    def delete_by_doc(self, doc_uid: str) -> int:
        self.deleted_doc_uids.append(doc_uid)
        self._embedding_counts.pop(doc_uid, None)
        return 0

    def count_embeddings_for_doc(self, doc_uid: str) -> int:
        return self._embedding_counts.get(doc_uid, 0)

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        self.added_embeddings.append((doc_uid, chunk_ids, texts))
        self._embedding_counts[doc_uid] = len(chunk_ids)


class RecordingTitleVectorStore:
    """Title vector store fake that records section embedding operations."""

    def __init__(self) -> None:
        self.deleted_doc_uids: list[str] = []
        self.added_embeddings: list[tuple[str, list[str], list[str]]] = []

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return []

    def delete_by_doc(self, doc_uid: str) -> int:
        self.deleted_doc_uids.append(doc_uid)
        return 0

    def add_embeddings(self, doc_uid: str, section_ids: list[str], texts: list[str]) -> None:
        self.added_embeddings.append((doc_uid, section_ids, texts))


class RecordingDocumentVectorStore:
    """Document vector store fake that records document embedding operations."""

    def __init__(self, existing_doc_uids: set[str] | None = None) -> None:
        self.deleted_doc_uids: list[str] = []
        self.added_embeddings: list[tuple[list[str], list[str]]] = []
        self._existing_doc_uids = set(existing_doc_uids or set())

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return []

    def has_embedding_for_doc(self, doc_uid: str) -> bool:
        return doc_uid in self._existing_doc_uids

    def delete_by_doc(self, doc_uid: str) -> int:
        self.deleted_doc_uids.append(doc_uid)
        if doc_uid in self._existing_doc_uids:
            self._existing_doc_uids.remove(doc_uid)
            return 1
        return 0

    def add_embeddings(self, doc_uids: list[str], texts: list[str]) -> None:
        self.added_embeddings.append((doc_uids, texts))
        self._existing_doc_uids.update(doc_uids)

class FakeAnswerGenerator:
    """Fake typed answer generator for approach identification and applicability analysis."""

    def __init__(self, approach_identification_output: ApproachIdentificationOutput | RuntimeError, applicability_analysis_output: ApplicabilityAnalysisOutput | RuntimeError) -> None:
        self.approach_identification_output = approach_identification_output
        self.applicability_analysis_output = applicability_analysis_output
        self.approach_identification_prompts: list[str] = []
        self.applicability_analysis_prompts: list[str] = []

    def generate_approach_identification(self, prompt_text: str) -> ApproachIdentificationOutput:
        self.approach_identification_prompts.append(prompt_text)
        if isinstance(self.approach_identification_output, RuntimeError):
            raise self.approach_identification_output
        return self.approach_identification_output

    def generate_applicability_analysis(self, prompt_text: str) -> ApplicabilityAnalysisOutput:
        self.applicability_analysis_prompts.append(prompt_text)
        if isinstance(self.applicability_analysis_output, RuntimeError):
            raise self.applicability_analysis_output
        return self.applicability_analysis_output
