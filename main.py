#!/usr/bin/env python3
"""news-image-20261122 entrypoint (Python 3.13, standard library only).

The entry image is drawn at build time by draw_entry_v2.py (kept outside this
repository) and shipped here as entry.png: a one-page newspaper front page
summing up Sunday 22 November 2026 -- COP31 deadlocked in overtime,
the Sparta II still burning in the Baltic, the AI-assisted Riemann
proof, and France seeking UN action on Myanmar.

This program only copies that image to the grader's output directory
and verifies its bytes, so both runs write identical output.
"""
import hashlib
import os
import shutil
import sys

# sha256 of the entry.png shipped in this repository (filled in after the
# image is drawn; the copy is refused if the bytes ever differ).
EXPECTED_SHA256 = "e2230cb56b188712f7e9b5c72c7e18d90ea64bd54af9bc6a327702a49f943c00"

MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "out"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry.png sha256 mismatch: got {digest}", file=sys.stderr)
        return 1
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
