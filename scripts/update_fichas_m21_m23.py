#!/usr/bin/env python3
"""Inject M01-style Lecciones section into M21–M23 fichas (03-terminal)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TERM = ROOT / "curriculum" / "etapas" / "03-terminal"


def lesson_table(materia: str, week_titles: list[str]) -> str:
    folder = TERM / materia
    files = sorted(folder.glob("L*.md"))
    by_week: dict[int, list[tuple[str, str, float, str]]] = {
        i: [] for i in range(1, len(week_titles) + 1)
    }
    for f in files:
        raw = f.read_text(encoding="utf-8")
        m = re.search(r"^semana:\s*(\d+)", raw, re.M)
        h = re.search(r"^horas:\s*([\d.]+)", raw, re.M)
        t = re.search(r"^titulo:\s*(.+)$", raw, re.M)
        lid = re.search(r"^id:\s*(L\d+)", raw, re.M)
        if not (m and h and t and lid):
            continue
        sem = int(m.group(1))
        by_week.setdefault(sem, []).append(
            (lid.group(1), t.group(1).strip(), float(h.group(1)), f.name)
        )

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
    "M21": {
        "file": "M21-admin-proyectos.md",
        "weeks": [
            "Roadmap y backlog",
            "Sprints y métricas de flujo",
            "Riesgos, dependencias y cierre",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M21 opera **Agenda Ops** como proyecto real en el repo: L01–L12 (3 semanas × 4 lecciones).

1. Orden **L01 → L12**; marca solo con “Hecho cuando” cumplido.
2. Issues y milestones en el **repo producto**, evidencia de gestión en `projects/m21-proyectos/`.
3. Estima en rangos; documenta desviaciones en sprints, no las borres.
4. Cada sprint: meta única, retrospectiva escrita, ≥1 issue de seguridad/multi-tenant visible en backlog.
5. [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Roadmap / backlog | 6–8 | 4 lecciones (~5 h c/u) |
| Sprints + métricas flujo | 6–8 | Registros honestos en `sprints/` |
| Riesgos + tablero | 4–6 | `riesgos.md`, `board.md` vivo |
| Retro | 1 | Estimación vs real |

Si un día solo tienes 2 h: **una lección** con artefacto en git. No saltes la lectura de esa lección.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf). Preparación comercial → M22. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura | Entrega ligada |
|--------|-----------|---------|----------------|
| 1 | L01–L04 | Scrum completa — roles, eventos, artefactos | `roadmap-trimestre.md`, DoD, board |
| 2 | L05–L08 | Sprint Planning, Review, Retro | `sprints/sprint-01.md`, `sprint-02.md`, flujo |
| 3 | L09–L12 | Riesgos + métricas simples | `riesgos.md`, sprints 3–4, cierre |

**Regla:** estima en rangos; si fallas, documenta el porqué en el sprint, no lo borres.""",
    },
    "M22": {
        "file": "M22-emprendimiento.md",
        "weeks": [
            "Visión y oferta",
            "Validated learning y guion",
            "Experimentos de pricing e ICP",
            "Métricas accionables",
            "Acelerar outreach",
            "Cierre comercial de la materia",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M22 vende **suscripción Agenda Ops** con conversaciones reales: L01–L24 (6 semanas × 4 lecciones).

1. Orden **L01 → L24**; cada lectura Lean → **acción** (demo, lista, pricing).
2. ICP **único** seis semanas; pivote solo documentado al final.
3. Demos sobre **staging/prod** (M19), nunca `localhost`.
4. Registra cada conversación el mismo día en `projects/m22-bektor/demos/`.
5. [producto-saas](../../producto-saas.md) + [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Oferta / outreach | 6–8 | 4 lecciones de la semana |
| Demos reales | 6–8 | Fichas en `demos/` |
| Pricing / métricas | 4–6 | MXN Free/Pro, trials |
| Retro | 1 | Objeción más frecuente |

Si un día solo tienes 2 h: **una lección** (demo o outreach documentado). No saltes la lectura.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *El método Lean Startup* — Eric Ries (ed. ES). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos (por tema de tu ed.) | Práctica |
|--------|-----------|-------------------------------|----------|
| 1 | L01–L04 | Visión / start / build-measure-learn | `oferta-saas.md`, outreach, guion |
| 2 | L05–L08 | Validated learning | demos 1–4, pivote borrador |
| 3 | L09–L12 | Experimentación / pivote | pricing, demos 5–6 |
| 4 | L13–L16 | Medir (accionable vs vanity) | `metricas-trials.md`, demos 7–8 |
| 5 | L17–L20 | Acelerar / lotes pequeños | demos 9–10, landing, pivote |
| 6 | L21–L24 | Cierre comercial + handoff | pricing final, pitch, cierre |

**Regla:** cada capítulo → una conversación o demo real, no solo subrayado.""",
    },
    "M23": {
        "file": "M23-ia-datos.md",
        "weeks": [
            "Métricas del SaaS",
            "LLM API y primeros prompts",
            "Evaluación",
            "Diseño RAG por tenant",
            "Implementación FAQ",
            "Integración producto y límites",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M23 añade métricas, LLM evaluado y RAG **por tenant** a Agenda Ops: L01–L24 (6 semanas × 4).

1. Orden **L01 → L24**; escribe `politica-datos-llm.md` **antes** de pegar datos en APIs.
2. No envíes PII, dumps crudos ni secretos a proveedores LLM.
3. Cada prompt: versión en archivo + resultado en rúbrica.
4. Demo obligatoria: tenant A no lee corpus de B (test automatizado preferido).
5. [producto-saas](../../producto-saas.md), [hilo seguridad](../../hilos/seguridad.md), [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Métricas / LLM / RAG | 10–12 | 4 lecciones (~5 h) |
| Evaluación + tests | 4–6 | CSV, rúbrica, CI |
| Producto FAQ | 4–6 | staging, README asistente |
| Retro | 1 | Costo vs valor |

Si un día solo tienes 2 h: **una lección** con evidencia en `projects/m23-ia/`.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: docs API LLM elegida + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura | Enfoque |
|--------|-----------|---------|---------|
| 1 | L01–L04 | Métricas SaaS (plan + M23) | `metricas/` pipeline |
| 2 | L05–L08 | API LLM: auth, modelos, costos | `llm-eval/` + política |
| 3 | L09–L12 | Evaluación + rúbrica | resultados v1/v2 |
| 4 | L13–L16 | RAG vendor docs + filtro tenant | `rag/diseno.md`, corpus A/B |
| 5 | L17–L20 | Implementación + tests cross-tenant | FAQ staging |
| 6 | L21–L24 | Costos, planes Pro, cierre | política actualizada |

**Regla:** demo obligatoria de que el tenant A no ve corpus del B.""",
    },
}


def patch_ficha(materia: str, spec: dict) -> None:
    path = TERM / spec["file"]
    text = path.read_text(encoding="utf-8")
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
    text = re.sub(r"\n## Día 1 \(2–3 h\).*?(?=\n## )", "\n", text, flags=re.DOTALL)
    text = re.sub(r"\n## Temario semanal\n\n(?:### Semana|\| Semana).*?(?=\n## )", "\n", text, flags=re.DOTALL)
    text = re.sub(
        r"\n## Lecturas\n\nCanon:.*?(?=\n## Prácticas)",
        "\n",
        text,
        flags=re.DOTALL,
        count=1,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for mid, spec in FICHAS.items():
        patch_ficha(mid, spec)
        print("patched", spec["file"])


if __name__ == "__main__":
    main()
