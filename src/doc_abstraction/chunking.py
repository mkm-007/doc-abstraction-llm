"""Heading-aware bounded chunks with source identity and stable offsets."""
import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Chunk:
    doc_id: str
    section: str
    text: str
    chunk_id: str = ''
    start: int = 0
    end: int = 0


def schematic_chunk(text, doc_id, max_chars=800):
    if not isinstance(max_chars, int) or max_chars < 80:
        raise ValueError('max_chars must be an integer >= 80')
    if not doc_id:
        raise ValueError('doc_id is required')
    boundaries = [0] + [m.start() for m in re.finditer(r'(?m)^(?:#+\s|\d+\.\s)', text) if m.start() > 0] + [len(text)]
    chunks = []
    for a, b in zip(boundaries, boundaries[1:]):
        section = text[a:b].strip().split('\n')[0][:80] if text[a:b].strip() else 'body'
        start = a
        while start < b:
            end = min(start + max_chars, b)
            if end < b:
                split = text.rfind(' ', start + max_chars // 2, end)
                if split > start:
                    end = split
            raw = text[start:end]
            left = len(raw) - len(raw.lstrip())
            right = len(raw.rstrip())
            if raw.strip():
                chunks.append(Chunk(doc_id, section, raw.strip(), f'{doc_id}#{len(chunks)+1}', start+left, start+right))
            start = end
    return chunks
