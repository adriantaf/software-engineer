#!/usr/bin/env python3
"""Build M21–M26 lesson dicts at M01/M09 quality from enriched specs.

Eliminates boilerplate ("Lee la sección indicada"). Each lesson has concrete
timed steps, numbered Hecho cuando, and bibliografía anchors.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from .common import make_lesson
from .overlays import evidencia_for, lab_overlay, objetivo_for

ROOT = Path(__file__).resolve().parents[2]
CURR = ROOT / "curriculum/etapas/03-terminal"
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_specs(key: str) -> list[dict]:
    """Load lesson specs from the existing generate_* modules (source of titles/labs)."""
    if key in ("m21", "m22", "m23"):
        from generate_m21_m23_lessons import m21, m22, m23

        return {"m21": m21, "m22": m22, "m23": m23}[key]()
    from generate_m24_m26_lessons import _m24, _m25, _m26

    return {"m24": _m24, "m25": _m25, "m26": _m26}[key]()

# Default primary sources / deep links per materia
DEFAULTS = {
    "M21": {
        "fuente": "Guía Scrum 2020 (ES)",
        "biblio": "../../../bibliografia.md#m21-admin-proyectos",
        "biblio_label": "Bibliografía · M21",
        "enlace_titulo": "Scrum Guide 2020 (PDF ES)",
        "enlace": "https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf",
        "project": "projects/m21-proyectos",
        "tag": "m21",
    },
    "M22": {
        "fuente": "*El método Lean Startup* — Eric Ries (ed. ES)",
        "biblio": "../../../bibliografia.md#m22-emprendimiento",
        "biblio_label": "Bibliografía · M22",
        "enlace_titulo": "producto-saas (Agenda Ops)",
        "enlace": "../../../producto-saas.md",
        "project": "projects/m22-bektor",
        "tag": "m22",
    },
    "M23": {
        "fuente": "Docs API LLM elegida + política de datos",
        "biblio": "../../../bibliografia.md#m23-ia-datos",
        "biblio_label": "Bibliografía · M23",
        "enlace_titulo": "producto-saas · FAQ por tenant",
        "enlace": "../../../producto-saas.md",
        "project": "projects/m23-ia",
        "tag": "m23",
    },
    "M24": {
        "fuente": "Docs oficiales del candidato + ficha M24",
        "biblio": "../../../bibliografia.md#m24-tecnologias-emergentes",
        "biblio_label": "Bibliografía · M24",
        "enlace_titulo": "producto-saas (encaje ICP)",
        "enlace": "../../../producto-saas.md",
        "project": "projects/m24-emergentes",
        "tag": "m24",
    },
    "M25": {
        "fuente": "OWASP WSTG / Testing Guide",
        "biblio": "../../../bibliografia.md#m25-ciberseguridad-aplicada",
        "biblio_label": "Bibliografía · M25",
        "enlace_titulo": "OWASP Web Security Testing Guide",
        "enlace": "https://owasp.org/www-project-web-security-testing-guide/",
        "project": "projects/m25-ciber",
        "tag": "m25",
    },
    "M26": {
        "fuente": "Memoria propia + producto-saas + egreso",
        "biblio": "../../../bibliografia.md#m26-proyecto-integrador",
        "biblio_label": "Bibliografía · M26",
        "enlace_titulo": "Rúbrica de egreso",
        "enlace": "../../../egreso.md",
        "project": "projects/m26-capstone",
        "tag": "m26",
    },
}


def disk_filenames(materia: str) -> dict[int, str]:
    d = CURR / materia
    out: dict[int, str] = {}
    for p in sorted(d.glob("L*.md")):
        m = re.match(r"L(\d+)-", p.name)
        if m:
            out[int(m.group(1))] = p.name
    return out


def next_link(filenames: dict[int, str], orden: int, titles: dict[int, str]) -> str:
    nxt = orden + 1
    if nxt not in filenames:
        return "Cierre de esta materia — vuelve a la [ficha](../) o avanza según el plan."
    return f"[L{nxt:02d} — {titles[nxt]}]({filenames[nxt]})"


def _is_redundant_read(chunk: str) -> bool:
    low = chunk.lower()
    if "lee la sección indicada" in low:
        return True
    # Duplicate full-book reads already covered by reading_step
    if chunk.startswith("Lee la [Guía Scrum") and "completa" in low:
        return True
    if low.startswith("lee capítulos") or low.startswith("lee el capítulo"):
        return True
    return False


def split_pasos(pasos_extra: str) -> list[str]:
    """Split lab prose into chunks on blank lines / headings."""
    text = pasos_extra.strip()
    parts: list[str] = []
    buf: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            buf.append(line)
            continue
        if not in_fence and line.strip() == "" and buf:
            chunk = "\n".join(buf).strip()
            if chunk and not _is_redundant_read(chunk):
                parts.append(chunk)
            buf = []
            continue
        buf.append(line)
    if buf:
        chunk = "\n".join(buf).strip()
        if chunk and not _is_redundant_read(chunk):
            parts.append(chunk)
    return parts or ([text] if text and not _is_redundant_read(text) else [])


def reading_step(materia: str, spec: dict, cfg: dict) -> tuple[str, str, str]:
    lect = spec["lectura"]
    if materia == "M21":
        body = f"""Abre la [Guía Scrum 2020 (ES)]({cfg['enlace']}) y lee **solo** lo nombrado hoy: _{lect}_.

Subraya 3–5 frases que puedas aplicar en Agenda Ops (no resúmenes genéricos). Anótalas en `{cfg['project']}/bitacora-m21.md` bajo fecha de hoy."""
    elif materia == "M22":
        body = f"""Lee en *El método Lean Startup* (ed. ES) lo indicado: _{lect}_.

Traduce a Agenda Ops: 5 bullets en `{cfg['project']}/bitacora-m22.md` con una **acción** comercial de esta lección (demo, outreach, pricing)."""
    elif materia == "M23":
        body = f"""Lee la fuente de hoy: _{lect}_. Si es docs de proveedor LLM, abre la página oficial del modelo/API que usarás.

Anota en `{cfg['project']}/bitacora-m23.md`: qué **no** enviarás a la API (PII, dumps, secretos) y qué sí (texto FAQ del tenant)."""
    elif materia == "M24":
        body = f"""Lee fuentes **primarias** (docs oficiales / pricing / límites): _{lect}_.

En la bitácora de la semana, lista URLs + 3 límites duros (rate, región, costo). Prohibido basarte solo en blogs."""
    elif materia == "M25":
        body = f"""Abre [OWASP WSTG]({cfg['enlace']}) (o la sección citada) y lee: _{lect}_.

Escribe 3 checks que aplicarás **hoy** a tu staging/prod de Agenda Ops (nombres de endpoint o activo)."""
    else:  # M26
        body = f"""Relee [producto-saas](../../../producto-saas.md) y/o [egreso](../../../egreso.md) según: _{lect}_.

Marca en `{cfg['project']}/egreso-checklist.md` (o créalo) qué ítem de egreso toca esta lección."""
    return ("Lectura concreta de la fuente", "40–60 min", body)


def lab_steps(chunks: list[str], evidencia: str) -> list[tuple[str, str, str]]:
    titles = [
        ("Prepara evidencia y carpetas", "20–30 min"),
        ("Laboratorio principal", "90–120 min"),
        ("Endurece el entregable", "40–60 min"),
        ("Cruza con Agenda Ops", "25–40 min"),
    ]
    steps: list[tuple[str, str, str]] = []
    for i, chunk in enumerate(chunks[:4]):
        title, time = titles[i] if i < len(titles) else (f"Trabajo adicional {i+1}", "30–45 min")
        # First chunk: ensure mkdir / path awareness
        if i == 0 and "mkdir" not in chunk and evidencia:
            path_hint = evidencia.split()[0].rstrip(",")
            parent = str(Path(path_hint).parent) if "/" in path_hint else path_hint
            chunk = f"Confirma rutas bajo `{parent}`.\n\n{chunk}"
        steps.append((title, time, chunk))
    if len(chunks) > 4:
        rest = "\n\n".join(chunks[4:])
        steps.append(("Completa el resto del laboratorio", "30–45 min", rest))
    return steps


def commit_step(tag: str, orden: int, titulo: str) -> tuple[str, str, str]:
    slug = re.sub(r"[^a-z0-9]+", "-", titulo.lower())
    slug = (
        slug.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
    )
    slug = re.sub(r"[^a-z0-9-]+", "", slug)[:40].strip("-")
    msg = f"docs({tag}): l{orden:02d} {slug}"
    return (
        "Commit atómico",
        "15 min",
        f"""```bash
git add projects/
git status
git commit -m "{msg}"
```

El mensaje debe mencionar el artefacto de hoy; no mezcles lecciones distintas en el mismo commit.""",
    )


def enrich_hecho(spec: dict, cfg: dict, orden: int, evidencia: str) -> list[str]:
    items = []
    for h in spec["hecho"]:
        # Rewrite vague “archivo de evidencia” lines
        if "según lección" in h or h.startswith("Archivo de evidencia"):
            continue
        if h.startswith("Artefacto indicado existe:"):
            items.append(f"Existe `{evidencia}`.")
            continue
        items.append(h)
    if not any(evidencia in h or f"`{evidencia}`" in h for h in items):
        items.insert(0, f"Existe el entregable: `{evidencia}`.")
    if not any("ommit" in h.lower() or "git" in h.lower() for h in items):
        items.append(f"Commit `docs({cfg['tag']}): l{orden:02d} …` en el historial.")
    return items[:5]


def enrich_errores(spec: dict) -> list[str]:
    errs = list(spec["errores"])
    # Drop generic if any; ensure ≥3
    while len(errs) < 3:
        errs.append("Marcar la lección en la UI sin archivo en git.")
    return errs[:5]


def default_m25_m26_labs(materia: str, evidencia: str, pasos_extra: str) -> list[tuple[str, str, str]]:
    """Ensure thin generator labs still have ≥3 concrete timed steps."""
    chunks = split_pasos(pasos_extra)
    parent = str(Path(evidencia).parent)
    mkdir = f"""```bash
mkdir -p {parent}
```"""
    lab_body = "\n\n".join(chunks) if chunks else f"Produce el entregable `{evidencia}` con contenido verificable (no placeholder)."
    return [
        ("Prepara carpetas", "15–25 min", mkdir + f"\n\nConfirma que escribirás `{evidencia}`."),
        ("Laboratorio principal", "100–130 min", lab_body),
        (
            "Criterio de calidad",
            "30–45 min",
            f"""Relee `{evidencia}`: ¿un mentor externo entendería el resultado sin preguntarte?

Añade enlace a issue/PR/URL de staging si aplica. Bitácora de la semana: 5 líneas de horas y bloqueos.""",
        ),
    ]


def build_materia(materia: str, key: str) -> tuple[dict[int, str], list[dict], dict]:
    cfg = DEFAULTS[materia]
    specs = load_specs(key)
    filenames = disk_filenames(materia)
    titles = {i + 1: s["titulo"] for i, s in enumerate(specs)}
    lessons: list[dict] = []
    for i, spec in enumerate(specs):
        orden = i + 1
        evidencia = evidencia_for(materia, orden, spec["evidencia"])
        objetivo = objetivo_for(materia, orden, spec["objetivo"])
        steps = [reading_step(materia, spec, cfg)]
        overlay = lab_overlay(materia, orden)
        if overlay:
            steps.extend(overlay)
        elif materia in ("M25", "M26"):
            steps.extend(default_m25_m26_labs(materia, evidencia, spec["pasos_extra"]))
        else:
            chunks = split_pasos(spec["pasos_extra"])
            steps.extend(lab_steps(chunks, evidencia))
        steps.append(commit_step(cfg["tag"], orden, spec["titulo"]))

        intro = (
            f"Hoy entregas **`{evidencia}`**. "
            f"Sin ese artefacto en git, la lección no cuenta para el dominio de {materia}."
        )
        if materia == "M21":
            intro = f"Agenda Ops se gestiona en el mismo repo. {intro}"
        elif materia == "M22":
            intro = f"Vendes suscripción SaaS, no agencia. {intro}"
        elif materia == "M23":
            intro = f"Métricas e IA **por tenant**, sin mezclar datos. {intro}"
        elif materia == "M24":
            intro = f"Evalúas tecnología emergente con decisión escrita. {intro}"
        elif materia == "M25":
            intro = f"El bug #1 a cazar es IDOR cross-tenant. {intro}"
        else:
            intro = f"Capstone: SaaS multi-tenant en producción. {intro}"

        # Mutable copy for enrich_hecho
        spec_local = dict(spec)
        spec_local["evidencia"] = evidencia

        lesson = make_lesson(
            orden=orden,
            titulo=spec["titulo"],
            horas=float(spec.get("horas", 5)),
            semana=int(spec["semana"]),
            lectura=spec["lectura"],
            evidencia=evidencia,
            intro=intro,
            objetivo=objetivo,
            porque=spec["porque"],
            steps=steps,
            hecho=enrich_hecho(spec_local, cfg, orden, evidencia),
            errores=enrich_errores(spec),
            siguiente=next_link(filenames, orden, titles),
            lectura_corta=spec["lectura"],
            conceptos=spec.get("conceptos"),
        )
        rows = spec.get("lectura_rows") or []
        if rows:
            for a, b, c in rows:
                for cell in (b, c):
                    if isinstance(cell, str) and cell.startswith("http"):
                        lesson["_enlace_titulo"] = a
                        lesson["_enlace"] = cell
                        break
        lessons.append(lesson)
    return filenames, lessons, cfg


def all_modules() -> dict[str, dict]:
    """Return MODULES config for the rewriter entrypoint."""
    mapping = {
        "m21": "M21",
        "m22": "M22",
        "m23": "M23",
        "m24": "M24",
        "m25": "M25",
        "m26": "M26",
    }
    modules = {}
    for key, materia in mapping.items():
        filenames, lessons, cfg = build_materia(materia, key)
        modules[key] = dict(
            out=CURR / materia,
            filenames=filenames,
            lessons=lessons,
            materia=materia,
            fuente=cfg["fuente"],
            biblio=cfg["biblio"],
            biblio_label=cfg["biblio_label"],
            default_enlace_titulo=cfg["enlace_titulo"],
            default_enlace=cfg["enlace"],
        )
    return modules
