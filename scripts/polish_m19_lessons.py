#!/usr/bin/env python3
"""Polish M19 lessons to M09 depth (concrete commands/code fences).

Run from repo root:
  python3 scripts/polish_m19_lessons.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _m17_m20.builder import write_module  # noqa: E402
from _m17_m20 import m19_lessons, polish_m19  # noqa: E402


def main() -> None:
    n = write_module(
        materia="M19",
        out_rel="curriculum/etapas/02-disciplinaria/M19",
        filenames=m19_lessons.FILENAMES,
        raw_lessons=polish_m19.patched_raw(),
        body_overrides=polish_m19.build_bodies(),
        fuente="Docs Docker + PaaS/VPS elegido",
        biblio="../../../bibliografia.md#m19-nube-devops",
        biblio_label="Bibliografía · M19",
        default_enlace_titulo="Docker docs",
        default_enlace="https://docs.docker.com/",
        proj="projects/m19-ops",
        final_siguiente="Materia siguiente: [M20 — Aplicaciones móviles](../M20-aplicaciones-moviles.md) (consume tu staging).",
    )
    m19_lessons.BODIES.clear()
    m19_lessons.BODIES.update(polish_m19.build_bodies())
    print("polished M19", n)


if __name__ == "__main__":
    main()
