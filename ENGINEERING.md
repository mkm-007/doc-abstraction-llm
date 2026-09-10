# Implementation notes

Heading-aware chunks preserve section context while limiting individual passage size. Ranking normalizes punctuation and case, removes a small set of common words, and weights overlapping terms. This deliberately inspectable baseline makes retrieval mistakes visible before introducing model-generated prose.

Document identity uses the resolved local path internally; public citations use a short source ID. Re-ingestion replaces the previous chunks for that identity. Tests cover exact offsets, size bounds, replacement, same-named files, independent indexes, irrelevant queries, and invalid input. Each command-line invocation creates a fresh index.
