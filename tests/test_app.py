# Run the tests with: pytest tests/test_app.py

from __future__ import annotations
import os, subprocess, sys
from pathlib import Path

def test_app_writes_file(tmp_path: Path) -> None:
    env = os.environ.copy()
    env["OUT_DIR"] = str(tmp_path)
    out = subprocess.check_output([sys.executable, "app.py"], env=env, text=True).strip()
    p = Path(out)
    assert p.exists()
    assert "hello from" in p.read_text(encoding="utf-8")
