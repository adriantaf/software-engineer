#!/usr/bin/env python3
"""Rewrite M13–M16 lessons to M01/M09 quality (concrete steps, Agenda Ops).

Run from repo root:
  python3 scripts/rewrite_m13_m16_lessons.py
  python3 scripts/rewrite_m13_m16_lessons.py --only m13
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _m13_m16.common import ROOT as _ROOT, write_lessons  # noqa: E402
from _m13_m16 import m13_lessons, m14_lessons, m15_lessons, m16_lessons  # noqa: E402

assert _ROOT == ROOT


MODULES = {
    "m13": dict(
        out=ROOT / "curriculum/etapas/02-disciplinaria/M13",
        filenames=m13_lessons.FILENAMES,
        lessons=m13_lessons.LESSONS,
        materia="M13",
        fuente="*UML y patrones* — Larman (ed. ES)",
        biblio="../../../bibliografia.md#m13-analisis-y-diseno",
        biblio_label="Bibliografía · M13",
        default_enlace_titulo="C4 model (apoyo diagramas)",
        default_enlace="https://c4model.com/",
    ),
    "m14": dict(
        out=ROOT / "curriculum/etapas/02-disciplinaria/M14",
        filenames=m14_lessons.FILENAMES,
        lessons=m14_lessons.LESSONS,
        materia="M14",
        fuente="*Patrones de diseño* — GoF / Refactoring.Guru ES",
        biblio="../../../bibliografia.md#m14-patrones",
        biblio_label="Bibliografía · M14",
        default_enlace_titulo="Refactoring.Guru — Patrones (ES)",
        default_enlace="https://refactoring.guru/es/design-patterns",
    ),
    "m15": dict(
        out=ROOT / "curriculum/etapas/02-disciplinaria/M15",
        filenames=m15_lessons.FILENAMES,
        lessons=m15_lessons.LESSONS,
        materia="M15",
        fuente="*Código limpio* (pruebas) + Vitest docs",
        biblio="../../../bibliografia.md#m15-v-v-y-calidad",
        biblio_label="Bibliografía · M15",
        default_enlace_titulo="Vitest",
        default_enlace="https://vitest.dev/",
    ),
    "m16": dict(
        out=ROOT / "curriculum/etapas/02-disciplinaria/M16",
        filenames=m16_lessons.FILENAMES,
        lessons=m16_lessons.LESSONS,
        materia="M16",
        fuente="*No me hagas pensar* — Steve Krug (ed. ES)",
        biblio="../../../bibliografia.md#m16-ihc",
        biblio_label="Bibliografía · M16",
        default_enlace_titulo="Heurísticas Nielsen (NN/g)",
        default_enlace="https://www.nngroup.com/articles/ten-usability-heuristics/",
    ),
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        choices=sorted(MODULES),
        help="Rewrite a single materia (default: all M13–M16)",
    )
    args = parser.parse_args()
    keys = [args.only] if args.only else list(MODULES)
    total = 0
    for key in keys:
        cfg = MODULES[key]
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
