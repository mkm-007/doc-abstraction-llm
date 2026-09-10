"""In-memory lexical retrieval baseline, not an embedding/vector database."""
from dataclasses import dataclass
import math
import re
from collections import Counter

STOP = set('a an the is are what how of to for in and do does it on'.split())
def tokens(text):
    return [t for t in re.findall(r'\w+', text.lower()) if t not in STOP]

@dataclass(frozen=True)
class Hit:
    score: float
    text: str
    section: str
    doc_id: str
    chunk_id: str
    start: int
    end: int

class LocalVectorStore:
    """Legacy class name retained for compatibility; implementation is lexical."""
    def __init__(self):
        self._docs = {}

    def replace_document(self, doc_id, chunks):
        if any(c.doc_id != doc_id for c in chunks):
            raise ValueError('Chunk source mismatch')
        self._docs[doc_id] = list(chunks)

    def query(self, question, k=2):
        if not isinstance(k, int) or k < 1:
            raise ValueError('k must be positive')
        q = set(tokens(question))
        chunks = [c for values in self._docs.values() for c in values]
        counts = [Counter(tokens(c.text)) for c in chunks]
        scored = []
        for c, words in zip(chunks, counts):
            score = sum((1 + math.log(words[t])) * math.log(1 + len(chunks)/(1 + sum(t in other for other in counts))) for t in q if t in words)
            score /= math.sqrt(max(1, sum(words.values())))
            if score > 0:
                scored.append(Hit(score, c.text, c.section, c.doc_id, c.chunk_id, c.start, c.end))
        return sorted(scored, key=lambda h: (-h.score, h.chunk_id))[:k]
