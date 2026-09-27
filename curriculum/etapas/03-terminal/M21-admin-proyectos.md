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

Agenda Ops ya es código, deploy y seguridad; sin **gestión explícita**, tus 20 h/semana se diluyen en “arreglar cositas” sin avanzar hacia multi-tenant, trials (M22) ni egreso (M26). Esta materia te obliga a planificar en el **mismo repo** donde vive el producto: roadmap priorizado, sprints con retrospectiva honesta y riesgos — incluidos los de [seguridad](../../hilos/seguridad.md) y aislamiento entre tenants.

No es teoría de gestión desconectada: es operar tu SaaS como un proyecto real con un solo desarrollador principal (tú) y un mentor ocasional.

**En resumen:** dejas de “hacer lo que salga”: roadmap, sprints y riesgos (incluye seguridad) en el repo.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Redactar un roadmap trimestral de Agenda Ops alineado con [producto-saas](../../producto-saas.md) (piloto → tenants → billing → FAQ M23).
2. Planificar y cerrar sprints de 1–2 semanas con meta, entregables, hecho real y aprendizaje.
3. Estimar en **rangos** (optimista/realista/pesimista) y documentar desviaciones sin autoengaño.
4. Mantener un tablero de issues/milestones (GitHub Projects, Linear, o markdown estructurado) visible y actualizado.
5. Identificar riesgos técnicos y de producto (seguridad, dependencia de un solo design partner, scope creep) con mitigaciones accionables.
6. Definir “hecho” (Definition of Done) que incluya evidencia en `projects/` y CI verde cuando aplique.

## Cómo estudiar esta materia (lecciones)

M21 opera **Agenda Ops** como proyecto real en el repo: L01–L12 (3 semanas × 4 lecciones).

1. Orden **L01 → L12**; marca solo con “Hecho cuando” cumplido.
2. Issues y milestones en el **repo producto**, evidencia de gestión en `projects/m21-proyectos/`.
3. Estima en rangos; documenta desviaciones en sprints, no las borres.
4. Cada sprint: meta única, retrospectiva escrita, ≥1 issue de seguridad/multi-tenant visible en backlog.
5. [Cómo estudiar](../../como-estudiar.md) y [producto-saas](../../producto-saas.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Roadmap / backlog | 6–8 | 4 lecciones (~5 h c/u) |
| Sprints + métricas flujo | 6–8 | Registros honestos en `sprints/` |
| Riesgos + tablero | 4–6 | `riesgos.md`, `board.md` vivo |
| Retro | 1 | Estimación vs real |

Si un día solo tienes 2 h: **una lección** con artefacto en git. No saltes la lectura de esa lección.

## Lecciones

### Semana 1 — Roadmap y backlog (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Entorno M21, Scrum de uno y Definition of Done](M21/L01-entorno-m21-scrum-de-uno-y-definition-of-done.md) | 5 |
| L02 | [Milestones y cinco issues reales del producto](M21/L02-milestones-y-cinco-issues-reales-del-producto.md) | 5 |
| L03 | [Roadmap trimestral alineado a producto-saas](M21/L03-roadmap-trimestral-alineado-a-producto-saas.md) | 5 |
| L04 | [Backlog refinado y criterios de aceptación](M21/L04-backlog-refinado-y-criterios-de-aceptacion.md) | 5 |

### Semana 2 — Sprints y métricas de flujo (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Sprint planning — meta única del sprint 1](M21/L05-sprint-planning-meta-unica-del-sprint-1.md) | 5 |
| L06 | [Ejecutar sprint 1 y registro honesto](M21/L06-ejecutar-sprint-1-y-registro-honesto.md) | 5 |
| L07 | [Estimación en rangos y métricas de flujo](M21/L07-estimacion-en-rangos-y-metricas-de-flujo.md) | 5 |
| L08 | [Sprint 2 documentado y avance P2](M21/L08-sprint-2-documentado-y-avance-p2.md) | 5 |

### Semana 3 — Riesgos, dependencias y cierre (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Matriz de riesgos del producto y del proyecto](M21/L09-matriz-de-riesgos-del-producto-y-del-proyecto.md) | 5 |
| L10 | [Riesgos de seguridad, privacidad y multi-tenant](M21/L10-riesgos-de-seguridad-privacidad-y-multi-tenant.md) | 5 |
| L11 | [Tablero vivo, sprints 3–4 y DoD en práctica](M21/L11-tablero-vivo-sprints-3-4-y-dod-en-practica.md) | 5 |
| L12 | [Cierre M21 — P1–P3, dominio y handoff comercial](M21/L12-cierre-m21-p1-p3-dominio-y-handoff-comercial.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf). Preparación comercial → M22. Ver [bibliografía](../../bibliografia.md#m21-admin-proyectos).

| Semana | Lecciones | Lectura | Entrega ligada |
|--------|-----------|---------|----------------|
| 1 | L01–L04 | Scrum completa — roles, eventos, artefactos | `roadmap-trimestre.md`, DoD, board |
| 2 | L05–L08 | Sprint Planning, Review, Retro | `sprints/sprint-01.md`, `sprint-02.md`, flujo |
| 3 | L09–L12 | Riesgos + métricas simples | `riesgos.md`, sprints 3–4, cierre |

**Regla:** estima en rangos; si fallas, documenta el porqué en el sprint, no lo borres.



## Ejemplo — entrada de sprint (honesta)

```markdown
## Sprint 2 — 2026-04-07 → 2026-04-20

**Meta:** Alta de segundo tenant en staging + test IDOR cross-tenant.

| Planeado | Hecho | Aprendizaje |
|----------|-------|-------------|
| Migración `tenant_id` | Sí, con rollback doc | Subestimé datos legacy del piloto |
| 3 tests cross-tenant | 2/3 | Falta caso staff de otro tenant |
| Demo interna | No | Prioricé fix deploy |

**Estimación:** 24–32 h · **Real:** ~38 h (migración manual de filas piloto).
```



## Prácticas

1. **P1 — Roadmap:** `projects/m21-proyectos/roadmap-trimestre.md` con objetivos, fechas orientativas y vínculo a milestones.
2. **P2 — 4 sprints:** `projects/m21-proyectos/sprints/sprint-01.md` … `sprint-04.md` (o equivalente) con meta/hecho/aprendizaje.
3. **P3 — Riesgos:** `projects/m21-proyectos/riesgos.md` con ≥5 riesgos y mitigaciones; ≥2 de seguridad o privacidad.

## Proyecto útil

**Tablero de proyecto vivo:** documentado en `projects/m21-proyectos/board.md` con enlace al board real (GitHub Projects u otro). Debe reflejar el estado actual del SaaS, no un ejercicio ficticio.

## Errores comunes

- Roadmap de 40 features sin orden ni criterio de corte.
- Cerrar issues sin PR ni evidencia (“ya quedó” sin commit).
- Sprints sin retrospectiva (“no tuve tiempo” — justamente ahí está el aprendizaje).
- Ignorar deuda de seguridad hasta M25.
- Mezclar tareas de aprendizaje genéricas con el backlog del producto sin etiquetar.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Roadmap:** `projects/m21-proyectos/roadmap-trimestre.md`.
- **P2 — 4 sprints:** `projects/m21-proyectos/sprints/sprint-01.md` … `sprint-04.md`.
- **P3 — Riesgos:** `projects/m21-proyectos/riesgos.md`.
- **Proyecto — Tablero:** `projects/m21-proyectos/board.md` + enlace verificable actualizado en la última semana.

## Criterios de dominio

- [ ] Estimas en rangos; cumples o explicas la desviación con datos del sprint.
- [ ] Definition of Done escrita y usada al cerrar al menos 3 issues.
- [ ] El backlog tiene trabajo de seguridad/multi-tenant visible, no solo UI.
- [ ] Puedes enseñar el roadmap a alguien no técnico en 5 minutos.
- [ ] El tablero coincide con la realidad del repo (no aspiracional).
