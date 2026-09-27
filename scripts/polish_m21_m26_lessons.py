#!/usr/bin/env python3
"""Spot-polish M21–M26: rebuild lessons from enriched overlays (no redundant mkdir labs).

Run from repo root:
  python3 scripts/polish_m21_m26_lessons.py
  python3 scripts/polish_m21_m26_lessons.py --only m25 m26
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from rewrite_m21_m26_lessons import main as rewrite_main  # noqa: E402


def count_stats(materias: list[str]) -> None:
    base = ROOT / "curriculum/etapas/03-terminal"
    print("\n=== Verificación mkdir / fences ===")
    total_mkdir_files = 0
    for m in materias:
        d = base / m
        lessons = sorted(d.glob("L*.md"))
        mkdir_files = [p for p in lessons if "mkdir -p" in p.read_text(encoding="utf-8")]
        fences = sum(
            len(re.findall(r"^```", p.read_text(encoding="utf-8"), flags=re.M))
            for p in lessons
        )
        prepara = sum(
            1
            for p in lessons
            if "Prepara carpetas" in p.read_text(encoding="utf-8")
        )
        total_mkdir_files += len(mkdir_files)
        print(
            f"{m}: lessons={len(lessons)} mkdir_files={len(mkdir_files)} "
            f"Prepara_carpetas={prepara} fence_openers={fences}"
        )
        for p in mkdir_files:
            print(f"  mkdir: {p.name}")
    print(f"TOTAL lessons with mkdir -p: {total_mkdir_files}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        nargs="+",
        choices=["m21", "m22", "m23", "m24", "m25", "m26"],
        default=["m25", "m26"],
        help="Materias to rewrite (default: m25 m26)",
    )
    parser.add_argument(
        "--stats-only",
        action="store_true",
        help="Only print mkdir/fence stats for M21–M26",
    )
    args = parser.parse_args()
    if args.stats_only:
        count_stats([f"M{n}" for n in range(21, 27)])
        return

    # Reuse rewriter for each selected key
    for key in args.only:
        sys.argv = ["rewrite_m21_m26_lessons.py", "--only", key]
        rewrite_main()

    count_stats([f"M{n}" for n in range(21, 27)])


if __name__ == "__main__":
    main()
