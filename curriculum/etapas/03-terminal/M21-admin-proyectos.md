---
id: M21
titulo: Administración de proyectos de software
etapa: terminal
orden: 21
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Roadmap trimestral del producto
  - id: p2
    titulo: 4 sprints documentados (meta/hecho/aprendizaje)
  - id: p3
    titulo: Riesgos (incluye seguridad) y mitigaciones
proyecto:
  id: proj
  titulo: Tablero de proyecto vivo en el repo
---

# M21 — Administración de proyectos de software

## Por qué existe
Sin gestión, 20 h/semana se evaporan. Los riesgos de seguridad entran al backlog ([hilo](../../hilos/seguridad.md)).

**En cristiano:** dejas de “hacer lo que salga”: roadmap, sprints y riesgos (incluye seguridad) en el repo.

## Día 1 (2–3 h)
Crea milestones de 4 semanas. Mueve 5 issues reales (uno de seguridad). Define “hecho”.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Roadmap | 6–8 | Trimestre Agenda Ops |
| Sprints | 6–8 | Meta/hecho/aprendizaje |
| Riesgos | 4–6 | Mitigaciones |
| Retro | 1 | Estimación vs real |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Temario
Roadmap → sprints → riesgos → métricas simples.

## Lecturas

Canon: [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf). Preparación Lean Startup → M22. Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Entrega |
|--------|---------|---------|
| 1 | Guía Scrum completa (es corta) — roles, eventos, artefactos | Roadmap Agenda Ops |
| 2 | Misma guía: foco en Sprint + Definition of Done | Plan de 2–3 sprints reales |
| 3 | Notas de riesgos + métricas simples (lectura M21 / bitácora) | Tablero vivo + retrospectiva |

**Regla:** estima en rangos; si fallas, documenta el porqué.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Roadmap:** Markdown trimestral priorizado.
- **P2 — 4 sprints:** Registro meta/hecho/aprendizaje.
- **P3 — Riesgos:** Tabla con mitigaciones de seguridad.
- **Proyecto — Tablero:** Board vivo en el repo.

## Criterios de dominio
- [ ] Estimas en rangos; cumples o aprendes por qué no.
