from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Chunk:
    doc_id: str
    section: str
    text: str


def schematic_chunk(text: str, doc_id: str) -> list[Chunk]:
    """Split on markdown-ish headings / numbered sections (schematic chunking)."""
    parts = re.split(r"\n(?=#+\s|\d+\.\s)", text.strip())
    chunks: list[Chunk] = []
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        first = part.split("\n", 1)[0][:80]
        chunks.append(Chunk(doc_id=doc_id, section=first or f"section-{i}", text=part))
    return chunks or [Chunk(doc_id=doc_id, section="body", text=text.strip())]
