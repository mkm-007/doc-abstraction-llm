# Document Abstraction with LLM (RAG)

**Resume project · SPT work unit**  
**Capability:** retrieval-grounded document Q&A and abstraction for policy/ops text  
**Background:** Centre for Advanced Technology Solutions, GITAM · May 2024 – Dec 2024  
**Stack:** Python · schematic chunking · local vector-style store · LLM interface (mockable) · LangChain / Chroma-ready hooks

---

## Problem

Staff documents (policies, handbooks) were hard to search. Summaries and answers needed to stay tied to retrieved text — not unconstrained generation.

## What I built

1. Ingest and schematically chunk documents  
2. Index for retrieval  
3. Produce retrieval-grounded abstracts / Q&A  

Resume anchor: *Implemented schematic chunking, vector indexing, and LLM summarization for document Q&A. Delivered retrieval-grounded abstracts with a reproducible pipeline and handoff documentation.*

## SPT bar (junior standard)

| Step | Artifact |
|------|----------|
| Build | `src/doc_abstraction/` |
| Verify | `python -m pytest -q` |
| Demo | `python run_demo.py` · [`demo_output.txt`](./demo_output.txt) |
| Document | this README |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

## Design notes

- Schematic chunking favors structured policy sections over blind fixed windows  
- Local store fallback keeps demos runnable without cloud vector DB setup  
- Abstract text is built from retrieved chunks to keep answers grounded  

## Layout

```
src/doc_abstraction/
sample_docs/
tests/
extensions/
run_demo.py
demo_output.txt
```

## Portfolio

Full Experience · Projects · SPT → [mkm-007/MKM](https://github.com/mkm-007/MKM)
