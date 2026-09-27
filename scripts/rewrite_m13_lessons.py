#!/usr/bin/env python3
"""Thin wrapper: rewrite only M13 lessons."""
from rewrite_m13_m16_lessons import MODULES, write_via

# keep import path simple when run as script
if __name__ == "__main__":
    import runpy
    import sys

    sys.argv = [sys.argv[0], "--only", "m13"]
    runpy.run_path(
        str(__import__("pathlib").Path(__file__).with_name("rewrite_m13_m16_lessons.py")),
        run_name="__main__",
    )
