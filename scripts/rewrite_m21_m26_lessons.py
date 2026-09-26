#!/usr/bin/env python3
"""Rewrite M21–M26 lessons to M01/M09 quality (concrete timed steps, no boilerplate).

Run from repo root:
  python3 scripts/rewrite_m21_m26_lessons.py
  python3 scripts/rewrite_m21_m26_lessons.py --only m23
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _m21_m26.common import ROOT as _ROOT, write_lessons  # noqa: E402
from _m21_m26.build_lessons import all_modules  # noqa: E402

assert _ROOT == ROOT


def main() -> None:
    modules = all_modules()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        choices=sorted(modules),
        help="Rewrite a single materia (default: all M21–M26)",
    )
    args = parser.parse_args()
    keys = [args.only] if args.only else list(modules)
    total = 0
    for key in keys:
        cfg = modules[key]
        n = write_lessons(
            cfg["out"],
            cfg["filenames"],
            cfg["lessons"],
            materia=cfg["materia"],
            fuente=cfg["fuente"],
            biblio=cfg["biblio"],
            biblio_label=cfg["biblio_label"],
            default_enlace_titulo=cfg["default_enlace_titulo"],
            default_enlace=cfg["default_enlace"],
        )
        total += n
    print("grand_total", total)


if __name__ == "__main__":
    main()
