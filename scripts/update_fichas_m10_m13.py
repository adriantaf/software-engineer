#!/usr/bin/env python3
"""Inject M01-style Lecciones section into M10–M13 fichas."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DISC = ROOT / "curriculum" / "etapas" / "02-disciplinaria"


def lesson_table(materia: str, week_titles: list[str]) -> str:
    folder = DISC / materia
    files = sorted(folder.glob("L*.md"))
    by_week: dict[int, list[tuple[str, str, float]]] = {i: [] for i in range(1, len(week_titles) + 1)}
    for f in files:
        raw = f.read_text(encoding="utf-8")
        m = re.search(r"^semana:\s*(\d+)", raw, re.M)
        h = re.search(r"^horas:\s*([\d.]+)", raw, re.M)
        t = re.search(r"^titulo:\s*(.+)$", raw, re.M)
        lid = re.search(r"^id:\s*(L\d+)", raw, re.M)
        if not (m and h and t and lid):
            continue
        sem = int(m.group(1))
        by_week.setdefault(sem, []).append((lid.group(1), t.group(1).strip(), float(h.group(1)), f.name))

    parts = ["## Lecciones\n"]
    for i, wtitle in enumerate(week_titles, start=1):
        parts.append(f"### Semana {i} — {wtitle} (~20 h)\n")
        parts.append("| ID | Lección | ~h |")
        parts.append("|----|---------|-----|")
        for lid, tit, hrs, fname in by_week.get(i, []):
            parts.append(f"| {lid} | [{tit}]({materia}/{fname}) | {hrs:g} |")
        parts.append("")
    parts.append("Empieza por **L01** hoy.\n")
    return "\n".join(parts)


FICHAS = {
    "M10": {
        "file": "M10-redes.md",
        "weeks": [
            "Capas, IP, TCP/UDP y puertos",
            "DNS y HTTP",
            "TLS y certificados",
            "Cookies, sesiones y CORS",
            "Superficie de ataque y proyecto",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M10 sigue el formato de lecciones completas (como M01): marcas una a una en la UI.

1. Abre las lecciones **en orden** (L01 → L20).
2. Cada lección trae objetivo, pasos, lectura y criterio “Hecho cuando”.
3. Marca la lección solo si cumple ese criterio.
4. Las **prácticas / proyecto** exigen evidencia en `projects/m10-redes/`.
5. Relaciona labs con el piloto **Agenda Ops** (M12+) y la API de M17.
6. Método general: [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura + labs | 10–12 | Lecciones de la semana (4× ~5 h) |
| Bitácora P1 | 4–6 | `projects/m10-redes/labs/` |
| Proyecto / P2–P3 | 4–6 | TCP echo, superficie, amenazas |
| Retro | 1 | Qué protege TLS y qué no |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la lectura de esa lección.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *Redes de computadoras* — Tanenbaum & Wetherall (ed. ES) + MDN HTTP (ES). Ver [bibliografía](../../bibliografia.md) y [hilo de seguridad](../../hilos/seguridad.md).

| Semana | Lecciones | Capítulos / recursos | Alternativa |
|--------|-----------|---------------------|-------------|
| 1 | L01–L04 | Tanenbaum: **intro + red/transporte** (IP, TCP/UDP, puertos) | `curl`, `ping`, `ss` |
| 2 | L05–L08 | **Capa de aplicación** + HTTP; MDN overview + status codes | MDN ES HTTP |
| 3 | L09–L12 | **Seguridad / TLS** (selecto) + labs certificados | MDN TLS |
| 4 | L13–L16 | MDN **Cookies**, sesiones, CORS, security headers | Hilo seguridad |
| 5 | L17–L20 | Superficie de ataque → doc proyecto + cierre | [Hilo seguridad](../../hilos/seguridad.md) |

**Regla:** cada capítulo → un lab en terminal el mismo día.""",
    },
    "M11": {
        "file": "M11-sistemas-operativos.md",
        "weeks": [
            "Procesos, hilos y señales",
            "Memoria y contenedores (cgroups)",
            "Archivos, permisos y scripts ops",
            "Docker y playbook local",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M11 usa lecciones L01–L16 (como M01): terminal, scripts y Docker con evidencia en `projects/m11-so/`.

1. Orden **L01 → L16**; marca solo con “Hecho cuando” cumplido.
2. Cada concepto del libro → **un comando o experimento** el mismo día.
3. Piensa en el stack de **Agenda Ops** (API Node + Postgres en contenedor).
4. Prácticas P1–P3 y playbook se distribuyen en las lecciones indicadas.
5. [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Procesos / memoria / FS | 10–12 | 4 lecciones (~5 h c/u) |
| Scripts ops (P2) | 4–6 | Backup, rotación, restore |
| Docker + playbook (P3) | 4–6 | Imagen no-root, compose |
| Retro | 1 | Permiso o señal que evitó un incidente |

Si un día solo tienes 2 h: **una lección práctica**. No saltes la lectura de esa lección.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *Fundamentos de sistemas operativos* — Silberschatz, Galvin, Gagne (ed. ES). Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos (por tema) | Alternativa / práctica |
|--------|-----------|----------------------|-------------------------|
| 1 | L01–L04 | **Procesos e hilos** + señales | `ps`, `top`, Node + SIGTERM |
| 2 | L05–L08 | **Memoria** virtual, OOM, cgroups | RSS Node, límites Docker |
| 3 | L09–L12 | **Sistema de archivos** + protección | Permisos, backup P2 |
| 4 | L13–L16 | **Contenedores** + síntesis | Dockerfile, compose, playbook |

**Regla:** un experimento documentado por semana en `projects/m11-so/`.""",
    },
    "M12": {
        "file": "M12-requerimientos.md",
        "weeks": [
            "Elicitación y contexto Agenda Ops",
            "Historias y RNF",
            "SRS v1 y freeze",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M12 arranca el hilo de producto **Agenda Ops** ([producto-saas.md](../../producto-saas.md)): L01–L12 en orden.

1. Elige **un** sub-vertical y no lo cambies en estas tres semanas.
2. Cada sesión: entrevista o story → criterio → línea en el SRS (`projects/m12-srs/`).
3. Seguridad y privacidad entran como RNF y criterios 401/403, no “luego en M18”.
4. Marca lecciones solo con evidencia en git.
5. [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Elicitación / stories | 10–12 | Lecciones L01–L08 |
| SRS y freeze | 6–8 | L09–L12, `srs-v1.md` |
| Retro | 1 | Un “no” con alternativa documentada |

Si un día solo tienes 2 h: **una lección** (guion, notas o stories). No saltes la plantilla SRS.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: plantilla IEEE 830 adaptada en el repo + [producto-saas.md](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura obligatoria | Entrega ligada |
|--------|-----------|--------------------|----------------|
| 1 | L01–L04 | [`plantilla.md`](../../../projects/m12-srs/plantilla.md) + entrevistas | guion, notas, problemas, contexto SRS |
| 2 | L05–L08 | Plantilla **funcionales + RNF** | `stories.md` (≥8) + RNF trazables |
| 3 | L09–L12 | MoSCoW + freeze MVP 4 semanas | `projects/m12-srs/srs-v1.md` |

**Regla:** la lectura es la plantilla rellenada con evidencia de entrevistas y decisiones explícitas.""",
    },
    "M13": {
        "file": "M13-analisis-y-diseno.md",
        "weeks": [
            "Del SRS a casos de uso",
            "Modelo y UML práctico",
            "Arquitectura en capas",
            "ADRs de diseño",
            "Paquete para M17",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M13 traduce el SRS de **Agenda Ops** a diseño implementable: L01–L20.

1. Abre `projects/m12-srs/srs-v1.md` cada sesión.
2. Si un diagrama no cambia una decisión, bórralo.
3. Mermaid en Markdown dentro del repo.
4. Marca lecciones al cumplir “Hecho cuando” en `projects/m13-diseno/`.
5. [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Flujos / diagramas | 10–12 | 4 lecciones de la semana |
| Arquitectura + ADRs | 6–8 | Capas, boundaries, decisiones |
| Retro | 1 | Por qué monolito modular ahora |

Si un día solo tienes 2 h: **una lección** con artefacto en git.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *UML y patrones* — Larman (ed. ES) **o** guía UML en español + ADRs. Apoyo: *Código limpio* (módulos). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / secciones | Alternativa |
|--------|-----------|----------------------|-------------|
| 1 | L01–L04 | Casos de uso desde SRS Agenda Ops | `casos-de-uso.md` |
| 2 | L05–L08 | UML clases y secuencia | Mermaid en `diagramas/` |
| 3 | L09–L12 | Capas + trust boundaries | `arquitectura.md` |
| 4 | L13–L16 | ADRs (plantilla M01) | `projects/m13-diseno/adr/` |
| 5 | L17–L20 | Paquete + [producto-saas.md](../../producto-saas.md) | README índice M13 |

**Regla:** cada diagrama debe trazarse a un requisito del SRS.""",
    },
}


def patch_ficha(materia: str, spec: dict) -> None:
    path = DISC / spec["file"]
    text = path.read_text(encoding="utf-8")
    # Replace desde "## Cómo estudiar" hasta antes de "## Prácticas" o "## Ejemplo"
    table = lesson_table(materia, spec["weeks"])
    block = (
        spec["estudio"]
        + "\n\n"
        + spec["semana_tipo"]
        + "\n\n"
        + table
        + "\n"
        + spec["lecturas"]
    )
    pattern = re.compile(
        r"## Cómo estudiar esta materia.*?(?=\n## (?:Prácticas|Ejemplo|Temario|Lecturas|Día 1))",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise SystemExit(f"No patch anchor in {path}")
    text = pattern.sub(block + "\n\n", text, count=1)
    # Remove Día 1 section if present
    text = re.sub(r"\n## Día 1 \(2–3 h\).*?(?=\n## )", "\n", text, flags=re.DOTALL)
    # Remove duplicate Temario semanal if right after (optional cleanup)
    text = re.sub(r"\n## Temario semanal\n\n\| Semana.*?(?=\n## )", "\n", text, flags=re.DOTALL)
    # Remove old ## Lecturas block if still duplicated
    text = re.sub(
        r"\n## Lecturas\n\nCanon:.*?(?=\n## Prácticas)",
        "\n",
        text,
        flags=re.DOTALL,
        count=1,
    )
    # M10: Agenda Ops wording
    if materia == "M10":
        text = text.replace("tu futuro CRM (M17)", "el piloto **Agenda Ops** (M12–M17)")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for mid, spec in FICHAS.items():
        patch_ficha(mid, spec)
        print("patched", spec["file"])


if __name__ == "__main__":
    main()
