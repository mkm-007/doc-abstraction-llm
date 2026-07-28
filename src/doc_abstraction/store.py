"""Local vector-store stand-in. Swap for ChromaDB in extensions/."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Hit:
    score: float
    text: str
    section: str


class LocalVectorStore:
    def __init__(self) -> None:
        self._docs: list[tuple[str, str, set[str]]] = []

    def add(self, section: str, text: str) -> None:
        tokens = set(text.lower().split())
        self._docs.append((section, text, tokens))

    def query(self, question: str, k: int = 2) -> list[Hit]:
        q = set(question.lower().split())
        scored: list[Hit] = []
        for section, text, tokens in self._docs:
            overlap = len(q & tokens)
            if overlap:
                scored.append(Hit(score=float(overlap), text=text, section=section))
        scored.sort(key=lambda h: h.score, reverse=True)
        return scored[:k]
