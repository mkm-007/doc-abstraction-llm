from pathlib import Path

from doc_abstraction.chunking import schematic_chunk
from doc_abstraction.pipeline import abstract_document, ingest_document


def test_schematic_chunk():
    text = Path(__file__).resolve().parents[1] / "sample_docs" / "leave_policy.txt"
    chunks = schematic_chunk(text.read_text(), "leave")
    assert len(chunks) >= 2


def test_abstract():
    path = Path(__file__).resolve().parents[1] / "sample_docs" / "leave_policy.txt"
    ingest_document(path)
    result = abstract_document("What is the annual leave entitlement?")
    assert result["hit_count"] >= 1
    assert "20" in result["top_chunk"] or "annual" in result["top_chunk"].lower()
