# Document Abstraction with LLM (RAG)

Retrieval-grounded document Q&A and abstraction for policy and ops text.

**Background:** Centre for Advanced Technology Solutions, GITAM · May 2024 – Dec 2024  
**Stack:** Python · schematic chunking · local vector-style store · LLM interface (mockable) · LangChain / Chroma-ready hooks

---

## Problem

Staff documents (policies, handbooks) were hard to search. Summaries and answers needed to stay tied to retrieved text — not unconstrained generation.

## What it does

1. Ingest and schematically chunk documents  
2. Index for retrieval  
3. Produce retrieval-grounded abstracts / Q&A  

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

Demo output: [`demo_output.txt`](./demo_output.txt)

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

[mkm-007/MKM](https://github.com/mkm-007/MKM) · [Live site](https://mkm-007.github.io/MKM/)
