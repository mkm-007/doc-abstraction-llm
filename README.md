# Document Abstraction with LLM — Offline Retrieval Baseline

Retrieve relevant document excerpts with source citations, bounded chunks, and explicit no-context responses.

> **Independent portfolio reconstruction.** Inspired by project categories I worked on while gaining practical experience at CATS, GITAM. I do not have access to the original CATS codebases. This repository was created later with AI coding assistance (Cursor/Codex), uses demonstration inputs, and is not original institutional code or evidence of a production deployment. Features and tests below describe this reconstruction only.

## Try it

Python 3.11+; the runtime uses only Python's standard library. No API keys or paid services are needed.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
python run_demo.py --question "What is the annual leave entitlement?"
```

The checked-in [demo output](demo_output.txt) is generated from the current implementation. Tests run automatically on pushes and pull requests.

## Architecture

```text
UTF-8 document → heading-aware chunks → lexical index → ranked excerpts + citations
```

## Implemented

- Bounded heading-aware chunks with exact source character offsets.
- Document replacement on re-ingestion, avoiding duplicates and stale content.
- Independent index instances and distinct source identity for same-named files.
- Case/punctuation-normalized lexical ranking, source IDs, section labels, and chunk citations.
- Extractive responses preserve source text instead of inventing answers; empty matches abstain.

## Scope and limitations

Despite the historical repository name, this version does not invoke an LLM or implement semantic embeddings, ChromaDB, or LangChain. It is an in-memory lexical retrieval baseline. Excerpts can be relevant without answering a question; no-context detection is not a guarantee against false matches. UTF-8 text/Markdown only, up to 1 MB per document; no PDFs, OCR, persistence, multi-user isolation, or authentication. Documents are data, never instructions to execute.

## Verification

`tests/` covers successful requests and failure cases. Read the tests alongside the source; test counts are evidence of exercised cases, not a claim of production readiness. [Engineering notes](ENGINEERING.md) explain boundaries and review prompts.

## Background and attribution

The historical CATS work involved Angular, Python, LLM consumption, database querying, document retrieval, and agent-oriented UI workflows, as described by the portfolio owner. Those historical technologies are not automatically dependencies or implemented capabilities here. Public reconstruction work must be described separately from institutional experience in resumes and interviews. Do not backdate these commits or claim institutional adoption.

AI tools assisted implementation. The portfolio owner should run the demo, inspect the code, and be able to explain its decisions and limitations before presenting it as personal proficiency. No confidential CATS code, data, or documents are included.

[Portfolio](https://github.com/mkm-007/MKM)
