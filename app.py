from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import os

USERNAME = "mustapha_mbengue"

def main() -> None:
    out_dir = Path(os.environ.get("OUT_DIR", "/app/data"))
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"{USERNAME}_{ts}.txt"
    path.write_text(f"hello from {USERNAME} at {ts}\n", encoding="utf-8")
    print(str(path))

if __name__ == "__main__":
    main()
