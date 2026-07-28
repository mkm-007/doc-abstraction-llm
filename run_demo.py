"""Demo: chunk → index → abstract a sample policy doc."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from doc_abstraction.pipeline import abstract_document, ingest_document


def main() -> None:
    path = Path(__file__).parent / "sample_docs" / "leave_policy.txt"
    ingest_document(path)
    result = abstract_document("What is the annual leave entitlement?")
    print("Query:", result["query"])
    print("Top chunk:", result["top_chunk"][:160], "...")
    print("Abstract:", result["abstract"])


if __name__ == "__main__":
    main()
