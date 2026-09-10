"""Source-attributed extractive retrieval. No live LLM or Chroma dependency."""
from pathlib import Path
from hashlib import sha256
from dataclasses import asdict
from doc_abstraction.chunking import schematic_chunk
from doc_abstraction.store import LocalVectorStore

class DocumentIndex:
    def __init__(self):
        self.store = LocalVectorStore()

    def ingest(self, path):
        path = Path(path).resolve()
        if path.stat().st_size > 1_000_000:
            raise ValueError('Documents must be <= 1 MB')
        text = path.read_text(encoding='utf-8')
        # Full path internally prevents identical filenames overwriting one another.
        chunks = schematic_chunk(text, str(path))
        self.store.replace_document(str(path), chunks)
        return len(chunks)

    def answer(self, question, k=2):
        if not isinstance(question, str) or not question.strip() or len(question) > 1000:
            raise ValueError('Question must contain 1-1000 characters')
        hits = self.store.query(question, k)
        citations = []
        for h in hits:
            citation = asdict(h)
            citation['source'] = Path(h.doc_id).name
            citation['source_id'] = sha256(h.doc_id.encode()).hexdigest()[:12]
            # Local filesystem paths are not included in returned citations.
            citation.pop('doc_id')
            citation['chunk_id'] = citation['source_id'] + '#' + h.chunk_id.rsplit('#', 1)[1]
            citations.append(citation)
        return {'query': question, 'mode': 'extractive', 'status': 'ok' if hits else 'no_context',
                'top_chunk': hits[0].text if hits else '',
                'abstract': '\n\n'.join(f'[{i}] {h.text}' for i, h in enumerate(hits, 1)) if hits else 'No relevant context',
                'hit_count': len(hits), 'citations': citations}

_DEFAULT = DocumentIndex()
def ingest_document(path):
    return _DEFAULT.ingest(path)
def abstract_document(question):
    return _DEFAULT.answer(question)
