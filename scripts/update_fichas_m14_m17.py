#!/usr/bin/env python3
"""Inject M01-style Lecciones section into M14–M17 fichas."""
from __future__ import annotations

import re
from pathlib import Path

from update_fichas_m10_m13 import lesson_table, patch_ficha

ROOT = Path(__file__).resolve().parents[1]
DISC = ROOT / "curriculum" / "etapas" / "02-disciplinaria"

FICHAS = {
    "M14": {
        "file": "M14-patrones.md",
        "weeks": [
            "Patrones creacionales y Strategy",
            "Patrones estructurales y regresión",
            "Patrones de comportamiento y P1",
            "Repository, Service y proyecto",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M14 aplica patrones con justificación en el dominio **Agenda Ops**: L01–L16 en orden.

1. Un patrón por lección: leer → implementar en TypeScript → test → ADR o nota.
2. Marca la lección solo si cumples “Hecho cuando”.
3. Evidencia en `projects/m14-patrones/` (o repo producto enlazado en README).
4. Cada patrón sin justificación escrita **no cuenta** para el proyecto.
5. [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Lectura patrones | 6–8 | Lecciones de la semana (4× ~5 h) |
| Implementar + tests | 6–8 | Código en `src/` |
| ADR / fichas | 4–6 | Por qué cada patrón |
| Retro | 1 | Anti-patrón que evitaste |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la lectura de esa lección.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *Patrones de diseño* — GoF (ed. ES si hay). Alternativa: [Refactoring.Guru ES](https://refactoring.guru/es/design-patterns). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Patrones / capítulos | Alternativa |
|--------|-----------|----------------------|-------------|
| 1 | L01–L04 | **Creacionales** + Strategy precios | Refactoring.Guru Factory / Singleton (cuándo NO) |
| 2 | L05–L08 | **Estructurales**: Adapter, Decorator, Facade | Tests de regresión en API pública |
| 3 | L09–L12 | **Comportamiento**: Observer, Command; cierre P1 | Strategy + Observer + Factory documentados |
| 4 | L13–L16 | **Repository / Service** + refactor P3 + ≥5 patrones | `projects/m14-patrones/README.md` |

**Regla:** patrón sin justificación escrita = no cuenta.""",
    },
    "M15": {
        "file": "M15-vv-calidad.md",
        "weeks": [
            "Pirámide y tests de dominio",
            "Integración, fakes y API",
            "CI en GitHub Actions",
            "Review, regresión y cierre",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M15 deja la calidad del piloto **Agenda Ops** automatizada: L01–L16.

1. Cada bug encontrado → test de regresión el mismo día (regla del plan).
2. Trabaja sobre spike en `projects/m15-calidad/` o el repo M17 cuando exista.
3. CI debe ser obligatoria para merge; no “corro tests a mano cuando me acuerdo”.
4. Marca lecciones al cumplir “Hecho cuando”.
5. [Cómo estudiar](../../como-estudiar.md) y [hilo seguridad](../../hilos/seguridad.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Tests | 6–8 | Lecciones unit/API de la semana |
| CI | 6–8 | Workflow Actions lint+test+audit |
| Review | 4–6 | Checklist en PR real o simulado |
| Retro | 1 | Bug → test documentado |

Si un día solo tienes 2 h: **una lección práctica**. No saltes la lectura de esa lección.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *Código limpio* (cap. pruebas) + *El programador pragmático* (testing) + docs Vitest. Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos / docs | Alternativa |
|--------|-----------|------------------|-------------|
| 1 | L01–L04 | *Código limpio* **cap. 9** + `piramide.md` | [Vitest](https://vitest.dev) |
| 2 | L05–L08 | Mocks/fakes + tests HTTP 401/403 | OWASP Auth (selecto) |
| 3 | L09–L12 | GitHub Actions + lint + `npm audit` | Workflow en repo |
| 4 | L13–L16 | Checklist review + regresiones + cierre | OWASP Testing Guide (selecto) |

**Regla:** un bug encontrado → test de regresión el mismo día.""",
    },
    "M16": {
        "file": "M16-ihc.md",
        "weeks": [
            "Heurísticas y evaluación experta",
            "Prototipo y tests con usuarios",
            "Iteración e informe",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M16 pone al usuario del piloto **Agenda Ops** en el centro: L01–L12.

1. Usa prototipo o UI parcial; si no existe, HTML estático en `projects/m16-ihc/prototipo/`.
2. Tests con personas reales (design partner o usuarios del sub-vertical); no solo auto-evaluación.
3. Tareas del test alineadas al SRS M12 (historias Must).
4. Marca lecciones al cumplir “Hecho cuando”.
5. [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Heurísticas | 6–8 | 4 lecciones semana 1 |
| Tests usuarios | 6–8 | Guion + 5 sesiones (semana 2) |
| Iteración | 4–6 | Fixes + informe (semana 3) |
| Retro | 1 | Hallazgo que te sorprendió |

Si un día solo tienes 2 h: **una lección** con artefacto en git.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: *No me hagas pensar* — Steve Krug (ed. ES). Alternativa: [heurísticas Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Capítulos (Krug) / recursos | Alternativa |
|--------|-----------|----------------------------|-------------|
| 1 | L01–L04 | Usabilidad y escaneo + estados UI | NN/g heurísticas |
| 2 | L05–L08 | Navegación, formularios, test de pasillo | `projects/m16-ihc/prototipo/` |
| 3 | L09–L12 | Iteración → `informe-usabilidad.md` | Handoff UX a M17 |

**Regla:** prototipo → test con personas reales → cambios documentados.""",
    },
    "M17": {
        "file": "M17-aplicaciones-web.md",
        "weeks": [
            "Auth, usuarios y fundación",
            "CRUD citas, clientes y servicios",
            "Roles owner/staff y admin",
            "Front serio y estados UX",
            "WhatsApp e integración",
            "Deploy HTTPS y smoke tests",
            "Hardening ligero y CI",
            "Checklist camino a SaaS y cierre",
        ],
        "estudio": """## Cómo estudiar esta materia (lecciones)

M17 construye el **MVP web Agenda Ops** con profundidad: L01–L32 (8 semanas × 4 lecciones).

1. Lee [producto-saas.md](../../producto-saas.md) y el paquete M13 antes de la semana 2.
2. **Vertical slices:** cada semana una historia completa (API + UI + test mínimo cuando aplique).
3. Cada endpoint sensible: test 401/403 antes de pulir CSS.
4. Evidencia en `projects/m17-agenda-ops/`; stack fijo en `stack.md`.
5. [Cómo estudiar](../../como-estudiar.md).""",
        "semana_tipo": """## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Auth + API | 6–8 | 4 lecciones de la semana |
| Front / integración | 6–8 | Rutas, estados, WhatsApp según semana |
| Tests + docs | 4–6 | ADR, deploy, checklist |
| Retro | 1 | Gap honesto hacia M18/M19 |

Si un día solo tienes 2 h: **una lección** con commit demostrable.""",
        "lecturas": """## Lecturas (mapa rápido)

Canon: MDN Web Docs (ES) + docs del framework + OWASP Top 10 overview + [producto-saas](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lecciones | Lectura | Alternativa |
|--------|-----------|---------|-------------|
| 1 | L01–L04 | MDN auth/cookies + ADR sesión M13 | OWASP Auth Cheat Sheet |
| 2 | L05–L08 | SRS M12 + modelo citas M13/M09 | — |
| 3 | L09–L12 | Control de acceso / `permisos.md` | OWASP Access Control |
| 4 | L13–L16 | MDN forms/a11y + handoff M16 | `ui-estados.md` |
| 5 | L17–L20 | WhatsApp / deep links (docs oficiales) | `integracion-whatsapp.md` |
| 6 | L21–L24 | Deploy PaaS + HTTPS | `smoke-test.md` |
| 7 | L25–L28 | OWASP Top 10 mapa + rate limit | hilo seguridad |
| 8 | L29–L32 | Multi-tenant ADR + checklist ficha | Demo design partner |

**Regla:** cada semana deja el piloto más demoable; la lectura sirve al commit.""",
    },
}


def fix_frontmatter_crm(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = text.replace("en el CRM", "en Agenda Ops")
    text = text.replace("del CRM", "del piloto Agenda Ops")
    text = text.replace("Usabilidad del CRM", "Usabilidad del piloto Agenda Ops")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for mid, spec in FICHAS.items():
        patch_ficha(mid, spec)
        fix_frontmatter_crm(DISC / spec["file"])
        print("patched", spec["file"])


if __name__ == "__main__":
    main()
