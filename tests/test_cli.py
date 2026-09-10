import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_demo_and_invalid_input():
    good = subprocess.run([sys.executable, str(ROOT / 'run_demo.py')], cwd=ROOT, text=True, capture_output=True)
    assert good.returncode == 0
    assert isinstance(json.loads(good.stdout), dict)
    bad = subprocess.run([sys.executable, str(ROOT / 'run_demo.py'), '--document', 'missing-document.txt'], cwd=ROOT, text=True, capture_output=True)
    assert bad.returncode == 2
    assert 'error' in json.loads(bad.stdout)
