#!/usr/bin/env python3
"""Polish M20 lessons to M09 depth (concrete commands/code fences).

Run from repo root:
  python3 scripts/polish_m20_lessons.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _m17_m20.builder import write_module  # noqa: E402
from _m17_m20 import m20_lessons, polish_m20  # noqa: E402


def main() -> None:
    n = write_module(
        materia="M20",
        out_rel="curriculum/etapas/02-disciplinaria/M20",
        filenames=m20_lessons.FILENAMES,
        raw_lessons=polish_m20.patched_raw(),
        body_overrides=polish_m20.build_bodies(),
        fuente="Docs Flutter o React Native (stack elegido)",
        biblio="../../../bibliografia.md#m20-aplicaciones-moviles",
        biblio_label="Bibliografía · M20",
        default_enlace_titulo="Flutter get started",
        default_enlace="https://docs.flutter.dev/get-started/install",
        proj="projects/m20-movil",
        final_siguiente="Etapa terminal: [M21 — Admin. proyectos](../../03-terminal/M21-admin-proyectos.md).",
    )
    m20_lessons.BODIES.clear()
    m20_lessons.BODIES.update(polish_m20.build_bodies())
    print("polished M20", n)


if __name__ == "__main__":
    main()
