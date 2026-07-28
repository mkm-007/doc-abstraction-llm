from __future__ import annotations

from pathlib import Path

from doc_abstraction.chunking import schematic_chunk
from doc_abstraction.store import LocalVectorStore

STORE = LocalVectorStore()


def llm_abstract(question: str, context: str) -> str:
    """Placeholder LLM — replace with LangChain + real model in extensions."""
    snippet = context.replace("\n", " ")[:220]
    return f"Based on the document: {snippet}"


def ingest_document(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    chunks = schematic_chunk(text, doc_id=path.stem)
    for c in chunks:
        STORE.add(c.section, c.text)
    return len(chunks)


def abstract_document(question: str) -> dict:
    hits = STORE.query(question, k=2)
    top = hits[0].text if hits else ""
    return {
        "query": question,
        "top_chunk": top,
        "abstract": llm_abstract(question, top) if top else "No relevant context",
        "hit_count": len(hits),
    }
