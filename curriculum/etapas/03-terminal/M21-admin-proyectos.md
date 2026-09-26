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

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) y la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) — es corta; léela entera una vez.
- Adapta Scrum a **equipo de uno**: tú eres dev y “product owner” hasta que tengas clientes; el backlog es el producto, no tareas de la universidad.
- Cada viernes (o fin de sprint): 30 min de retrospectiva escrita en `projects/m21-proyectos/`.
- Un issue de seguridad o multi-tenant en el backlog vale tanto como una feature visible.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Roadmap | 6–8 | Trimestre Agenda Ops |
| Sprints | 6–8 | Meta/hecho/aprendizaje |
| Riesgos | 4–6 | Mitigaciones |
| Retro | 1 | Estimación vs real |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. `mkdir -p projects/m21-proyectos/sprints`.
2. En GitHub (o herramienta elegida), crea milestones para las próximas 4 semanas: ej. “M21-S1 Roadmap”, “M21-S2 Sprint 1”, etc.
3. Mueve **5 issues reales** del repo Agenda Ops al backlog priorizado; **al menos uno** debe ser seguridad o `tenant_id` (ej. “test cross-tenant”, “rotar secretos”, “documentar DoD”).
4. Escribe `projects/m21-proyectos/definition-of-done.md`: qué debe cumplir un issue para cerrarse (PR, test, doc, deploy staging si aplica).
5. Borrador de `projects/m21-proyectos/roadmap-trimestre.md` con 3–5 objetivos del trimestre (multi-tenant, staging estable, primeros trials).
6. Enlaza el tablero en `projects/m21-proyectos/board.md` (URL o captura semanal).

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

## Temario semanal

### Semana 1 — Roadmap y backlog (~20 h)

- Visión trimestral de Agenda Ops vs [producto-saas](../../producto-saas.md).
- Priorización: impacto en design partner y camino a ≥2 tenants (M26).
- Backlog refinado: historias pequeñas, criterios de aceptación.
- Milestones y etiquetas (feature, bug, security, ops).
- Entregable: `roadmap-trimestre.md` revisable.

### Semana 2 — Sprints y métricas de flujo (~20 h)

- Sprint planning: meta única por sprint, WIP limitado.
- Daily implícito: nota de 3 líneas en bitácora si trabajas solo.
- Review: demo a ti mismo o mentor con checklist.
- Retrospectiva: qué mantener / cambiar / probar.
- Documentar **4 sprints** (pueden solaparse semanas calendario si ya venías iterando; deben ser registros distintos).

### Semana 3 — Riesgos, dependencias y cierre (~20 h)

- Matriz de riesgos: probabilidad, impacto, mitigación, dueño, fecha revisión.
- Riesgos de seguridad obligatorios: secretos, IDOR cross-tenant, backup sin restore, dependencia de un solo host.
- Dependencias externas: proveedor PaaS, Stripe (M26), APIs LLM (M23).
- Tablero “vivo”: sin issues zombie de hace 2 meses sin etiqueta.
- Handoff a M22: issues de “demo comercial” en el backlog.

## Lecturas

Canon: [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf). Preparación Lean Startup → M22. Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura | Entrega |
|--------|---------|---------|
| 1 | Guía Scrum completa — roles, eventos, artefactos | `projects/m21-proyectos/roadmap-trimestre.md` |
| 2 | Misma guía: Sprint + Definition of Done | Plan de 2–3 sprints + 2 registros en `sprints/` |
| 3 | Notas de riesgos + métricas simples (throughput, carry-over) | `riesgos.md` + tablero actualizado |

**Regla:** estima en rangos; si fallas, documenta el porqué en el sprint, no lo borres.

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
