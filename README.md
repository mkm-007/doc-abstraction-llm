# Document Abstraction with LLM (RAG)

Ingest documents, chunk schematically, index for retrieval, and produce retrieval-grounded abstracts / Q&A answers.

**Origin:** Centre for Advanced Technology Solutions, GITAM University (May 2024 – Dec 2024)  
**Stack:** Python · schematic chunking · local vector-style store (JSON fallback) · LLM interface (mockable offline) · LangChain / Chroma-ready hooks

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

## What it does

1. Ingest a sample policy document
2. Chunk and index content
3. Answer a query with a grounded abstract from retrieved chunks

See [`demo_output.txt`](./demo_output.txt) for a captured run.

## Layout

```
src/doc_abstraction/   # chunking, store, pipeline
sample_docs/
tests/
extensions/            # real Chroma, Snowflake metadata, LangChain LLM
run_demo.py
demo_output.txt
```

## Resume anchor

Implemented schematic chunking, vector indexing, and LLM summarization for document Q&A. Delivered retrieval-grounded abstracts with a reproducible pipeline and handoff documentation.

## License

Personal portfolio / educational use.
