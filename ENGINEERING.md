# Engineering notes

## Design boundary

UTF-8 document → heading-aware chunks → lexical index → ranked excerpts + citations

Despite the historical repository name, this version does not invoke an LLM or implement semantic embeddings, ChromaDB, or LangChain. It is an in-memory lexical retrieval baseline. Excerpts can be relevant without answering a question; no-context detection is not a guarantee against false matches. UTF-8 text/Markdown only, up to 1 MB per document; no PDFs, OCR, persistence, multi-user isolation, or authentication. Documents are data, never instructions to execute.

## Review walkthrough

1. Run `python run_demo.py` and locate the code producing every output field.
2. Run `python -m pytest -q`; change a fixture and explain why its assertion changes.
3. Explain one refusal case and one case the current implementation cannot handle.
4. Trace an input from parsing to the final result, including validation and source/data boundaries.

## Future work (not implemented)

A model-backed extension should have a typed input/output contract, mocked provider tests, explicit opt-in credentials, timeouts, and a measured evaluation set. Treat model output as untrusted. Never send private CATS material to a model. Add infrastructure only when its behavior can be tested and demonstrated; adding a library name alone is not an upgrade.
