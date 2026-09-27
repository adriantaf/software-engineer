#!/usr/bin/env python3
"""Polish M17 lessons to M09 depth (concrete commands/code fences).

Run from repo root:
  python3 scripts/polish_m17_lessons.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _m17_m20.builder import write_module  # noqa: E402
from _m17_m20 import m17_lessons, polish_m17  # noqa: E402


def main() -> None:
    n = write_module(
        materia="M17",
        out_rel="curriculum/etapas/02-disciplinaria/M17",
        filenames=m17_lessons.FILENAMES,
        raw_lessons=polish_m17.patched_raw(),
        body_overrides=polish_m17.build_bodies(),
        fuente="MDN Web Docs + docs del framework elegido",
        biblio="../../../bibliografia.md#m17-aplicaciones-web",
        biblio_label="Bibliografía · M17",
        default_enlace_titulo="MDN Web Docs (ES)",
        default_enlace="https://developer.mozilla.org/es/",
        proj="projects/m17-agenda-ops",
        final_siguiente="Materia siguiente: [M18 — Seguridad AppSec](../M18-seguridad.md) (en paralelo práctico con deploy M19).",
    )
    # Keep lesson module BODIES in sync for rewrite_m17_m20_lessons.py
    m17_lessons.BODIES.clear()
    m17_lessons.BODIES.update(polish_m17.build_bodies())
    print("polished M17", n)


if __name__ == "__main__":
    main()
