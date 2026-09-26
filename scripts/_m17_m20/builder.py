"""Build M01/M09-quality lesson markdown from structured specs."""
from __future__ import annotations

from pathlib import Path

from .common import ROOT, write_lessons


def slug_commit(titulo: str) -> str:
    import re

    t = titulo.lower()
    for a, b in (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    ):
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:48]


def numbered_hecho(items: list[str], commit_msg: str, evidencia: str = "") -> str:
    ev = ""
    if evidencia:
        # Prefer the primary path before " + …"
        ev = evidencia.split(" + ")[0].strip().rstrip(".")
    lines = []
    for i, h in enumerate(items, 1):
        text = h.strip().rstrip(".")
        if ev and len(text) < 56 and "`" not in text and "http" not in text.lower():
            text = f"{text} (artefacto: `{ev}`)"
        lines.append(f"{i}. {text}.")
    if not any("commit" in h.lower() for h in items):
        lines.append(f"{len(lines) + 1}. Commit `{commit_msg}`.")
    return "\n".join(lines)


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {e.strip().rstrip('.')}." for e in items)


def default_body(spec: dict, *, materia: str, orden: int, proj: str) -> str:
    """Expand a generate-script spec into timed, concrete steps (no boilerplate)."""
    lid = f"L{orden:02d}"
    titulo = spec["titulo"]
    horas = spec.get("horas", 5.0)
    semana = spec["semana"]
    objetivo = spec["objetivo"].rstrip(".")
    porque = spec["porque"]
    conceptos = spec.get("conceptos") or []
    lab = (spec.get("pasos_extra") or "").strip()
    evidencia = spec["evidencia"]
    commit = f"docs({materia.lower()}): {lid.lower()} {slug_commit(titulo)}"

    conceptos_md = ""
    if conceptos:
        conceptos_md = "\n## Conceptos clave\n\n" + "\n".join(
            f"- {c.rstrip('.')}" for c in conceptos
        ) + "\n"

    return f"""
# {lid} — {titulo}

**~{horas:g} h · Semana {semana}**

{porque}

## Objetivo

{objetivo}.

{conceptos_md}
## Pasos (hazlos en orden)

### 1. Ancla la lectura al producto (25–40 min)

Abre la fuente de la tabla de abajo. Subraya **solo** lo que vas a demostrar hoy en `{proj}/` o en la API del piloto. Anota 3 bullets: qué cambia en Agenda Ops (citas, clientes, auth, deploy o móvil).

### 2. Prepara evidencia (10–15 min)

```bash
mkdir -p {proj}/docs
ls {proj}
```

Si no existe README usable, amplía el scaffold de esta materia. La evidencia de hoy debe quedar en: `{evidencia}`.

### 3. Laboratorio principal (100–140 min)

{lab}

### 4. Verifica contra Agenda Ops (25–40 min)

Demuestra el resultado con un flujo del piloto (login, cita, rol, deploy o app). Anota comando, URL o captura **sin secretos ni PII real** en `docs/` o en el artefacto de evidencia.

### 5. Commit atómico (10–15 min)

```bash
git add {proj} curriculum/etapas/02-disciplinaria/{materia}/ 2>/dev/null || git add {proj}
git status   # sin .env, keystores ni dumps con PII
git commit -m "{commit}"
```
""".strip()


def enrich_spec(
    raw: dict,
    *,
    materia: str,
    orden: int,
    filenames: dict[int, str],
    fuente_default: str,
    enlace_titulo: str,
    enlace: str,
    siguiente: str,
    proj: str,
    body_override: str | None = None,
    lectura_corta: str | None = None,
    hecho_extra: list[str] | None = None,
) -> dict:
    titulo = raw["titulo"]
    # Fix ugly title artifact from generator
    if titulo.endswith(".md") and "stack.md" in titulo:
        titulo = "Scaffold Agenda Ops — API, DB y stack"
    commit = f"docs({materia.lower()}): L{orden:02d} {slug_commit(titulo)}"
    hecho_items = list(raw["hecho"])
    if hecho_extra:
        hecho_items.extend(hecho_extra)
    body = body_override or default_body(
        {**raw, "titulo": titulo}, materia=materia, orden=orden, proj=proj
    )
    return dict(
        id=f"L{orden:02d}",
        orden=orden,
        titulo=titulo,
        horas=float(raw.get("horas", 5)),
        semana=int(raw["semana"]),
        lectura=raw["lectura"],
        evidencia=raw["evidencia"],
        _lectura_corta=lectura_corta or raw["lectura"],
        _enlace_titulo=enlace_titulo,
        _enlace=enlace,
        _hecho=numbered_hecho(hecho_items, commit, evidencia=raw["evidencia"]),
        _errores=bullets(raw["errores"]),
        siguiente=siguiente,
        body=body,
    )


def next_link(
    orden: int,
    filenames: dict[int, str],
    titles: dict[int, str],
    *,
    final: str,
) -> str:
    nxt = orden + 1
    if nxt not in filenames:
        return final
    return f"[{titles[nxt]}]({filenames[nxt]})"


def write_module(
    *,
    materia: str,
    out_rel: str,
    filenames: dict[int, str],
    raw_lessons: list[dict],
    fuente: str,
    biblio: str,
    biblio_label: str,
    default_enlace_titulo: str,
    default_enlace: str,
    proj: str,
    final_siguiente: str,
    body_overrides: dict[int, str] | None = None,
) -> int:
    body_overrides = body_overrides or {}
    titles = {}
    for i, raw in enumerate(raw_lessons, 1):
        t = raw["titulo"]
        if t.endswith(".md") and "stack.md" in t:
            t = "Scaffold Agenda Ops — API, DB y stack"
        titles[i] = f"L{i:02d} — {t}"

    lessons = []
    for i, raw in enumerate(raw_lessons, 1):
        lessons.append(
            enrich_spec(
                raw,
                materia=materia,
                orden=i,
                filenames=filenames,
                fuente_default=fuente,
                enlace_titulo=default_enlace_titulo,
                enlace=default_enlace,
                siguiente=next_link(i, filenames, titles, final=final_siguiente),
                proj=proj,
                body_override=body_overrides.get(i),
            )
        )

    return write_lessons(
        ROOT / out_rel,
        filenames,
        lessons,
        materia=materia,
        fuente=fuente,
        biblio=biblio,
        biblio_label=biblio_label,
        default_enlace_titulo=default_enlace_titulo,
        default_enlace=default_enlace,
    )
