#!/usr/bin/env python3
"""Inject M01-style Lecciones section into M24–M26 fichas (03-terminal)."""
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
    "M24": {
        "file": "M24-tecnologias-emergentes.md",
        "weeks": [
            "Research de tres candidatos",
            "Matriz, costo y plan de spike",
            "Spike, medición y go/no-go",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M24 es **evaluación disciplinada** de tecnologías emergentes para Agenda Ops: L01–L12 (formato M01), evidencia en `projects/m24-emergentes/`.

1. Orden **L01 → L12**; marca solo con “Hecho cuando” cumplido.
2. **Fuentes primarias** (docs oficiales) antes de puntuar la matriz.
3. El spike vive aislado; no merges a prod sin go explícito en `go-no-go.md`.
4. Un “no” bien argumentado vale igual que un “go” si el spike midió costo/riesgo.
5. [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lecciones research/spike | 10–12 | 4× ~5 h (lectura + `projects/m24-emergentes/`) |
| Matriz / PoC (P2–P3) | 6–8 | Criterios + spike acotado |
| Retro | 1 | Qué descartaste y por qué |

Si un día solo tienes 2 h: **una lección** con archivo en git. No saltes la lectura del vendor.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: **docs oficiales** de los tres candidatos + notas de la matriz. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura | Entrega |
|--------|-----------|---------|---------|
| 1 | L01–L04 | 3× docs vendor + 1 crítica/candidato | `research/candidato-*.md` (P1) |
| 2 | L05–L08 | Pricing, webhooks, threat sketch | `matriz-adopcion.md` + `spike/plan.md` (P2) |
| 3 | L09–L12 | Quickstart spike + changelog seguridad | `spike/` + `go-no-go.md` (P3) |

**Regla:** sin fuente primaria no entra a la matriz; spike con hipótesis medible.""",
    },
    "M25": {
        "file": "M25-ciberseguridad-aplicada.md",
        "weeks": [
            "Inventario y clasificación multi-tenant",
            "Authn/authz y tests cross-tenant",
            "Hardening deploy y Stripe",
            "Logging, abuso y alertas",
            "Privacidad y cierre de hallazgos",
            "Tabletop y security review final",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M25 es **ciberseguridad aplicada** al SaaS Agenda Ops: L01–L24, evidencia en `projects/m25-ciber/` y fixes en el repo del producto.

1. Orden **L01 → L24**; prioriza **IDOR cross-tenant** sobre hallazgos cosméticos.
2. Solo atacas **tus** ambientes prod/staging acordados.
3. Cierra ≥2 issues críticos/altos de aislamiento con tests antes del cierre.
4. Tabletop documentado (≥30 min narrativa) sin copiar tutorial.
5. [hilo seguridad](../../hilos/seguridad.md) + [producto-saas](../../producto-saas.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lecciones + labs | 10–12 | 4× ~5 h en inventario/review/hardening |
| Fixes cross-tenant | 4–6 | PRs con tests |
| Tabletop / informe | 4–6 | `security-review.md` |
| Retro | 1 | Riesgo residual |

Si un día solo tienes 2 h: **prueba manual A vs B** o un fix con test.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: **OWASP Testing Guide** (secciones por semana) + [hilo seguridad](../../hilos/seguridad.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | OWASP / foco | Entrega |
|--------|-----------|--------------|---------|
| 1 | L01–L04 | Information gathering | `inventario.md`, tenants prueba |
| 2 | L05–L08 | Identity / authorization | Tests cross-tenant |
| 3 | L09–L12 | Configuration + Stripe | Hardening + restore |
| 4 | L13–L16 | Logging / abuse | Política logs + rate limit |
| 5 | L17–L20 | Privacy / retención | 2º hallazgo cerrado |
| 6 | L21–L24 | Reporting + tabletop | `security-review.md` |

**Regla:** al menos 2 issues críticos/altos de aislamiento cerrados con tests.""",
    },
    "M26": {
        "file": "M26-proyecto-integrador.md",
        "weeks": [
            "Alcance congelado y modelo tenancy",
            "Onboarding y dos tenants demo",
            "Features críticas — citas y catálogo",
            "Integraciones, móvil y métricas",
            "Stripe test y landing de precios",
            "M25 vigente, CI y ops",
            "Memoria técnica y comercial",
            "Demo pública y egreso",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M26 es el **capstone**: Agenda Ops SaaS en **producción** con L01–L32 (máxima profundidad del plan), evidencia en `projects/m26-capstone/` y repos de aplicación.

1. Orden **L01 → L32**; congela alcance en semana 1 y respétalo.
2. Cada semana: demo interna con **≥2 tenants** distintos.
3. Billing (Stripe test) y cross-tenant **no** se aplazan a la semana 8.
4. Memoria y video deben explicar **tu** tenancy real a un tercero.
5. [egreso.md](../../egreso.md) + [producto-saas](../../producto-saas.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Build SaaS (lecciones) | 10–12 | 4× ~5 h features/ops/billing |
| Seguridad / billing | 4–6 | M25 + Stripe webhooks |
| Memoria / demo | 4–6 | Video + rúbrica egreso |
| Retro | 1 | Gaps honestos |

Si un día solo tienes 2 h: **un entregable del sprint** (test, página, doc memoria).""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: memoria propia + [producto-saas](../../producto-saas.md) + [egreso](../../egreso.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura / relectura | Uso |
|--------|-----------|---------------------|-----|
| 1 | L01–L04 | producto-saas + egreso | `alcance.md`, tenancy |
| 2 | L05–L08 | SRS M12 / diseño M13 | Onboarding tenants |
| 3 | L09–L12 | ADRs API M17 | CRUD multi-tenant |
| 4 | L13–L16 | M24 go/no-go, M20 README | Integraciones |
| 5 | L17–L20 | Stripe Checkout + webhooks | Landing + test mode |
| 6 | L21–L24 | Informe M25 | CI cross-tenant |
| 7 | L25–L28 | Métricas M22 | Memoria v1 |
| 8 | L29–L32 | Checklist egreso | Video + README capstone |

**Regla:** cada semana demo ≥2 tenants; producción o staging público acordado.""",
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
        r"## Cómo estudiar esta materia.*?(?=\n## (?:Prácticas|Ejemplo|Temario|Lecturas|Día 1|Entregables))",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise SystemExit(f"No patch anchor in {path}")
    text = pattern.sub(block + "\n\n", text, count=1)
    text = re.sub(r"\n## Día 1 \(2–3 h\).*?(?=\n## )", "\n", text, flags=re.DOTALL)
    text = re.sub(
        r"\n## Temario semanal\n\n(?:\| Semana|\### Semana).*?(?=\n## )",
        "\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\n## Lecturas\n\n(?:Canon:.*?(?=\n## Prácticas)|\| Semana.*?(?=\n## Prácticas))",
        "\n",
        text,
        flags=re.DOTALL,
        count=1,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    import sys

    targets = sys.argv[1:] or list(FICHAS.keys())
    for mid in targets:
        if mid not in FICHAS:
            raise SystemExit(f"Unknown materia {mid}")
        patch_ficha(mid, FICHAS[mid])
        print("patched", FICHAS[mid]["file"])


if __name__ == "__main__":
    main()
