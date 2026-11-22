#!/usr/bin/env python3
"""news-image-20261122 — graded entrypoint (standard library only).

The dashboard image is rendered at build time by build_image.py (which
uses Pillow) and committed to this repository as entry.png next to this
file. This entrypoint only copies that pre-rendered image into the
output directory, so it needs nothing beyond the standard library.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SRC, dest)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

# v3: data berita ditulis ulang segar; renderer dan entrypoint tidak berubah.
