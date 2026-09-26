#!/usr/bin/env python3
"""Rewrite M17–M20 lessons to M01/M09 quality (concrete steps, Agenda Ops).

Run from repo root:
  python3 scripts/rewrite_m17_m20_lessons.py
  python3 scripts/rewrite_m17_m20_lessons.py --only m17
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _m17_m20.common import ROOT as _ROOT  # noqa: E402
from _m17_m20 import m17_lessons, m18_lessons, m19_lessons, m20_lessons  # noqa: E402
from _m17_m20.builder import write_module  # noqa: E402

assert _ROOT == ROOT

MODULES = {
    "m17": dict(
        materia="M17",
        out_rel="curriculum/etapas/02-disciplinaria/M17",
        filenames=m17_lessons.FILENAMES,
        raw_lessons=m17_lessons.RAW,
        body_overrides=m17_lessons.BODIES,
        fuente="MDN Web Docs + docs del framework elegido",
        biblio="../../../bibliografia.md#m17-aplicaciones-web",
        biblio_label="Bibliografía · M17",
        default_enlace_titulo="MDN Web Docs (ES)",
        default_enlace="https://developer.mozilla.org/es/",
        proj="projects/m17-agenda-ops",
        final_siguiente="Materia siguiente: [M18 — Seguridad AppSec](../M18-seguridad.md) (en paralelo práctico con deploy M19).",
    ),
    "m18": dict(
        materia="M18",
        out_rel="curriculum/etapas/02-disciplinaria/M18",
        filenames=m18_lessons.FILENAMES,
        raw_lessons=m18_lessons.RAW,
        body_overrides=m18_lessons.BODIES,
        fuente="OWASP Top 10 + Cheat Sheets",
        biblio="../../../bibliografia.md#m18-seguridad-appsec",
        biblio_label="Bibliografía · M18",
        default_enlace_titulo="OWASP Top 10",
        default_enlace="https://owasp.org/www-project-top-ten/",
        proj="projects/m18-appsec",
        final_siguiente="Materia siguiente / refuerzo: [M19 — Nube/DevOps](../M19-nube-devops.md) y [hilo seguridad](../../../hilos/seguridad.md).",
    ),
    "m19": dict(
        materia="M19",
        out_rel="curriculum/etapas/02-disciplinaria/M19",
        filenames=m19_lessons.FILENAMES,
        raw_lessons=m19_lessons.RAW,
        body_overrides=m19_lessons.BODIES,
        fuente="Docs Docker + PaaS/VPS elegido",
        biblio="../../../bibliografia.md#m19-nube-devops",
        biblio_label="Bibliografía · M19",
        default_enlace_titulo="Docker docs",
        default_enlace="https://docs.docker.com/",
        proj="projects/m19-ops",
        final_siguiente="Materia siguiente: [M20 — Aplicaciones móviles](../M20-aplicaciones-moviles.md) (consume tu staging).",
    ),
    "m20": dict(
        materia="M20",
        out_rel="curriculum/etapas/02-disciplinaria/M20",
        filenames=m20_lessons.FILENAMES,
        raw_lessons=m20_lessons.RAW,
        body_overrides=m20_lessons.BODIES,
        fuente="Docs Flutter o React Native (stack elegido)",
        biblio="../../../bibliografia.md#m20-aplicaciones-moviles",
        biblio_label="Bibliografía · M20",
        default_enlace_titulo="Flutter get started",
        default_enlace="https://docs.flutter.dev/get-started/install",
        proj="projects/m20-movil",
        final_siguiente="Etapa terminal: [M21 — Admin. proyectos](../../03-terminal/M21-admin-proyectos.md).",
    ),
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        choices=sorted(MODULES),
        help="Rewrite a single materia (default: all M17–M20)",
    )
    args = parser.parse_args()
    keys = [args.only] if args.only else list(MODULES)
    total = 0
    for key in keys:
        cfg = MODULES[key]
        n = write_module(
            materia=cfg["materia"],
            out_rel=cfg["out_rel"],
            filenames=cfg["filenames"],
            raw_lessons=cfg["raw_lessons"],
            fuente=cfg["fuente"],
            biblio=cfg["biblio"],
            biblio_label=cfg["biblio_label"],
            default_enlace_titulo=cfg["default_enlace_titulo"],
            default_enlace=cfg["default_enlace"],
            proj=cfg["proj"],
            final_siguiente=cfg["final_siguiente"],
            body_overrides=cfg["body_overrides"],
        )
        total += n
    print("grand_total", total)


if __name__ == "__main__":
    main()
