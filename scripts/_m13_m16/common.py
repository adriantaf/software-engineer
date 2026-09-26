"""Shared helpers for M13–M16 lesson rewrites (M01/M09 quality)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def fm(**kw) -> str:
    lines = ["---"]
    for k, v in kw.items():
        if isinstance(v, str) and (":" in v or v.startswith("*") or '"' in v or "'" in v):
            safe = v.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{k}: "{safe}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def lectura_block(
    fuente: str,
    que: str,
    biblio: str,
    biblio_label: str,
    enlace_titulo: str,
    enlace: str,
) -> str:
    return f"""## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| {fuente} | {que} | [{enlace_titulo}]({enlace}) |
| Catálogo | Entrada de esta materia | [{biblio_label}]({biblio}) |
"""


def render(
    *,
    materia: str,
    lesson: dict,
    fuente: str,
    biblio: str,
    biblio_label: str,
    default_enlace_titulo: str,
    default_enlace: str,
) -> str:
    pub = {
        "id": lesson["id"],
        "materia": materia,
        "orden": lesson["orden"],
        "titulo": lesson["titulo"],
        "horas": lesson["horas"],
        "semana": lesson["semana"],
        "lectura": lesson["lectura"],
        "evidencia": lesson["evidencia"],
    }
    enlace_titulo = lesson.get("_enlace_titulo", default_enlace_titulo)
    enlace = lesson.get("_enlace", default_enlace)
    hecho = lesson["_hecho"].strip()
    errores = lesson["_errores"].strip()
    return f"""{fm(**pub)}

{lesson["body"].strip()}

{lectura_block(fuente, lesson.get("_lectura_corta", lesson["lectura"]), biblio, biblio_label, enlace_titulo, enlace)}

## Hecho cuando

Marca la lección **solo si**:

{hecho}

## Errores comunes

{errores}

## Siguiente

{lesson["siguiente"]}
"""


def write_lessons(
    out: Path,
    filenames: dict[int, str],
    lessons: list[dict],
    *,
    materia: str,
    fuente: str,
    biblio: str,
    biblio_label: str,
    default_enlace_titulo: str,
    default_enlace: str,
) -> int:
    out.mkdir(parents=True, exist_ok=True)
    for lesson in lessons:
        path = out / filenames[lesson["orden"]]
        text = render(
            materia=materia,
            lesson=lesson,
            fuente=fuente,
            biblio=biblio,
            biblio_label=biblio_label,
            default_enlace_titulo=default_enlace_titulo,
            default_enlace=default_enlace,
        )
        path.write_text(text.rstrip() + "\n", encoding="utf-8")
        print("wrote", path.relative_to(ROOT), "lines", len(text.splitlines()))
    print(f"{materia} total", len(lessons))
    return len(lessons)
