"""Interactive local demo. Run with Python 3.11 or newer; no dependencies."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))

from doc_abstraction.pipeline import DocumentIndex

def main():
    index = DocumentIndex()
    sample = Path(__file__).resolve().parent / 'sample_docs/leave_policy.txt'
    index.ingest(sample)
    sources = [sample]
    print('Document search')
    print('Loaded sample: leave_policy.txt')
    print('Try: What is the annual leave entitlement?')
    print('Commands: load <file path> | sources | quit\n')
    while True:
        try:
            question = input('Question> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye.'); return
        if question.lower() in {'quit', 'exit'}:
            print('Goodbye.'); return
        if not question:
            continue
        if question.lower() == 'sources':
            print('\n'.join(str(p) for p in sources), '\n'); continue
        try:
            if question.startswith('load '):
                path = Path(question[5:].strip().strip('"').strip("'")).expanduser().resolve()
                count = index.ingest(path)
                if path not in sources:
                    sources.append(path)
                print(f'Loaded {path.name}: {count} passages.\n'); continue
            result = index.answer(question)
            print(result['abstract'])
            for i, citation in enumerate(result['citations'], 1):
                print(f"[{i}] {citation['source']} | {citation['section']} | characters {citation['start']}-{citation['end']}")
            print()
        except (ValueError, OSError, UnicodeError) as exc:
            print(f'Could not process that input: {exc}\n')

if __name__ == '__main__':
    main()
