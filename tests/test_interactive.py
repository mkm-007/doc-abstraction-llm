import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_interactive_example_and_exit():
    run = subprocess.run([sys.executable, '-S', str(ROOT / 'start.py')], input='What is the annual leave entitlement?'+'\nquit\n', text=True, capture_output=True, cwd=ROOT, timeout=10)
    assert run.returncode == 0
    assert '20 days' in run.stdout
    assert 'Goodbye' in run.stdout

def test_eof_exits_cleanly():
    run = subprocess.run([sys.executable, '-S', str(ROOT / 'start.py')], input='', text=True, capture_output=True, cwd=ROOT, timeout=10)
    assert run.returncode == 0
