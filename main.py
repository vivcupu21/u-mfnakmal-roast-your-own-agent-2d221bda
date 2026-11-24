"""Roast Your Own Agent — entry program.

Reads the single-line roast stored in entry.txt (next to this script)
and writes it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network, no randomness, no clocks: two runs produce
byte-identical output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
