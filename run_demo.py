"""Retrieve cited excerpts from one or more local UTF-8 documents."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))
from doc_abstraction.pipeline import DocumentIndex

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--document', type=Path, action='append')
    parser.add_argument('--question', default='What is the annual leave entitlement?')
    args = parser.parse_args()
    index = DocumentIndex()
    try:
        for path in args.document or [Path(__file__).parent / 'sample_docs/leave_policy.txt']:
            index.ingest(path)
        result = index.answer(args.question)
        # Source IDs are local-index identities, not content hashes.
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, UnicodeError) as exc:
        print(json.dumps({'status': 'error', 'error': str(exc)}))
        return 2
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
