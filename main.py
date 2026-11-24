#!/usr/bin/env python3
"""One-Liner Laugh Lab: write the winning one-liner to entry.txt.

Stdlib only. The entry is a single line, at most 200 characters, with no
trailing newline. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt, per the house harness program/v1).
"""

import os
import sys

ENTRY = "The dryer started it. I just finished the job."


def main() -> int:
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
