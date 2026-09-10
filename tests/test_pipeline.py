import pytest
from doc_abstraction.chunking import schematic_chunk
from doc_abstraction.pipeline import DocumentIndex

def test_chunks_are_bounded_and_offsets_exact():
    text = '# Policy\n' + 'annual leave allowance '*100
    chunks = schematic_chunk(text, 'policy', 100)
    assert len(chunks) > 1
    assert all(len(c.text) <= 100 and text[c.start:c.end] == c.text for c in chunks)
    assert len({c.chunk_id for c in chunks}) == len(chunks)

def test_empty_document():
    assert schematic_chunk('  \n', 'empty') == []

@pytest.mark.parametrize('size', [0, -1, 79])
def test_bad_chunk_size(size):
    with pytest.raises(ValueError): schematic_chunk('hello', 'x', size)

def test_reingest_replaces_and_cites(tmp_path):
    path = tmp_path / 'policy.txt'
    path.write_text('# Leave\nAnnual leave entitlement is 20 days.')
    index = DocumentIndex()
    index.ingest(path); index.ingest(path)
    result = index.answer('annual leave?')
    assert result['hit_count'] == 1
    assert result['citations'][0]['source'] == 'policy.txt'
    assert '20' in result['abstract']
    path.write_text('# Leave\nAnnual leave entitlement is 25 days.')
    index.ingest(path)
    assert '20' not in index.answer('annual leave')['abstract']

def test_unrelated_question_abstains(tmp_path):
    path = tmp_path / 'policy.txt'; path.write_text('Annual leave is 20 days.')
    index = DocumentIndex(); index.ingest(path)
    assert index.answer('What is the orbital velocity?')['status'] == 'no_context'

def test_same_filename_different_directories(tmp_path):
    index = DocumentIndex()
    for folder, text in [('a', 'Leave is 20 days'), ('b', 'Leave is 25 days')]:
        path = tmp_path / folder / 'policy.txt'; path.parent.mkdir(); path.write_text(text); index.ingest(path)
    assert index.answer('leave')['hit_count'] == 2

def test_indexes_are_isolated(tmp_path):
    path = tmp_path / 'a.txt'; path.write_text('Annual leave')
    first = DocumentIndex(); first.ingest(path)
    assert DocumentIndex().answer('leave')['hit_count'] == 0

@pytest.mark.parametrize('q', ['', 'x'*1001])
def test_invalid_question(q):
    with pytest.raises(ValueError): DocumentIndex().answer(q)
