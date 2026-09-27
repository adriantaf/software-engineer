---
id: M12
titulo: Ingeniería de requerimientos
etapa: disciplinaria
orden: 12
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Entrevista a un negocio real (o simulado serio)
  - id: p2
    titulo: User stories + criterios de aceptación
  - id: p3
    titulo: SRS v1 con requisitos de seguridad
proyecto:
  id: proj
  titulo: SRS de Agenda Ops (piloto single-tenant)
---

# M12 — Ingeniería de requerimientos

## Por qué existe

Construir sin requisitos es adivinar. A partir de esta materia el producto del plan deja de ser abstracto: documentas **Agenda Ops** ([producto-saas.md](../../producto-saas.md)) — citas, clientes y panel para un negocio de servicios local. Los requisitos **no funcionales de seguridad y privacidad** entran desde el SRS, no como parche en M18 ([hilo seguridad](../../hilos/seguridad.md)).

**En resumen:** congelas qué construir: entrevistas, stories y un SRS con seguridad; no pantallas bonitas primero.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Elicitar necesidades con un guion de entrevista (problemas observados, no soluciones prematuras).
2. Separar deseo, requisito y supuesto; registrar ambigüedades y preguntas abiertas.
3. Escribir user stories con criterios de aceptación verificables (incluidos casos de error y permisos).
4. Completar un SRS v1 con alcance MVP acotado (~4 semanas de build hacia M17).
5. Priorizar con MoSCoW (o equivalente) y decir “no” con alternativa.
6. Incluir al menos tres RNF de seguridad/privacidad trazables a historias y tests futuros.

## Cómo estudiar esta materia (lecciones)

M12 arranca el hilo de producto **Agenda Ops** ([producto-saas.md](../../producto-saas.md)): L01–L12 en orden.

1. Elige **un** sub-vertical y no lo cambies en estas tres semanas.
2. Cada sesión: entrevista o story → criterio → línea en el SRS (`projects/m12-srs/`).
3. Seguridad y privacidad entran como RNF y criterios 401/403, no “luego en M18”.
4. Marca lecciones solo con evidencia en git.
5. [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Elicitación / stories | 10–12 | Lecciones L01–L08 |
| SRS y freeze | 6–8 | L09–L12, `srs-v1.md` |
| Retro | 1 | Un “no” con alternativa documentada |

Si un día solo tienes 2 h: **una lección** (guion, notas o stories). No saltes la plantilla SRS.

## Lecciones

### Semana 1 — Elicitación y contexto Agenda Ops (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Design partner y guion de entrevista](M12/L01-design-partner-y-guion-de-entrevista.md) | 5 |
| L02 | [Entrevista y notas timestamp](M12/L02-entrevista-y-notas-timestamp.md) | 5 |
| L03 | [Problemas observados y glosario](M12/L03-problemas-observados-y-glosario.md) | 5 |
| L04 | [Stakeholders y contexto Agenda Ops](M12/L04-stakeholders-y-contexto-agenda-ops.md) | 5 |

### Semana 2 — Historias y RNF (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Formato user story y trazabilidad](M12/L05-formato-user-story-y-trazabilidad.md) | 5 |
| L06 | [Criterios de aceptación verificables](M12/L06-criterios-de-aceptacion-verificables.md) | 5 |
| L07 | [Historias de vacío, duplicados y conflicto](M12/L07-historias-de-vacio-duplicados-y-conflicto.md) | 5 |
| L08 | [RNF seguridad, privacidad y P2](M12/L08-rnf-seguridad-privacidad-y-p2.md) | 5 |

### Semana 3 — SRS v1 y freeze (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Alcance MVP y MoSCoW](M12/L09-alcance-mvp-y-moscow.md) | 5 |
| L10 | [Requisitos funcionales en SRS](M12/L10-requisitos-funcionales-en-srs.md) | 5 |
| L11 | [SRS v1, freeze y P3](M12/L11-srs-v1-freeze-y-p3.md) | 5 |
| L12 | [Revisión M13 y cierre M12](M12/L12-revision-m13-y-cierre-m12.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: plantilla IEEE 830 adaptada en el repo + [producto-saas.md](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md#m12-requerimientos).

| Semana | Lecciones | Lectura obligatoria | Entrega ligada |
|--------|-----------|--------------------|----------------|
| 1 | L01–L04 | [`plantilla.md`](../../../projects/m12-srs/plantilla.md) + entrevistas | guion, notas, problemas, contexto SRS |
| 2 | L05–L08 | Plantilla **funcionales + RNF** | `stories.md` (≥8) + RNF trazables |
| 3 | L09–L12 | MoSCoW + freeze MVP 4 semanas | `projects/m12-srs/srs-v1.md` |

**Regla:** la lectura es la plantilla rellenada con evidencia de entrevistas y decisiones explícitas.



## Ejemplo — historia con seguridad y criterio verificable

```text
Como dueño del negocio, quiero que solo yo vea notas privadas de clientes
para proteger su información personal.

Criterios de aceptación:
- Usuario con rol staff no puede GET /api/clientes/:id/notas-privadas (403).
- Usuario staff sí puede ver datos de contacto operativos según matriz de roles en SRS.
- Intento de acceso queda registrado en log de auditoría (RNF).
```

## Ejemplo — requisito no funcional en el SRS

```text
RNF-SEC-02 (privacidad): Los datos de clientes del negocio piloto no se mezclan
con otros negocios en el diseño futuro; el SRS documenta supuesto single-tenant
y campos PII mínimos necesarios.
```

## Temario semanal

### Semana 1 — Elicitación y contexto (~20 h)

- Stakeholders del piloto Agenda Ops: dueño, staff, cliente final (indirecto).
- Técnicas: entrevista semiestructurada, observación del flujo actual (WhatsApp, libreta).
- Glosario del dominio: cita, servicio, cliente, no-show, recordatorio.
- Entregable: guion + notas + lista de problemas en `projects/m12-srs/`.

### Semana 2 — Historias y trazabilidad (~20 h)

- Formato user story + criterios Given/When/Then o lista numerada verificable.
- Historias de error y vacío (sin citas, cliente duplicado, horario inválido).
- RNF: seguridad, privacidad, rendimiento mínimo, disponibilidad razonable para piloto.
- ≥8 stories con criterios; mapa story → sección del SRS.

### Semana 3 — SRS v1 y freeze de alcance (~20 h)

- Completar [`plantilla.md`](../../../projects/m12-srs/plantilla.md) → `srs-v1.md`.
- Priorización MoSCoW del MVP de 4 semanas de build (auth, citas, clientes, admin básico).
- Supuestos, fuera de alcance explícito (multi-tenant, billing, IA).
- Revisión de coherencia con M13 (diseño) y M17 (implementación).


## Prácticas

1. **P1 — Entrevista:** Notas de negocio real o simulado serio en `projects/m12-srs/entrevistas/` (mínimo una sesión completa).
2. **P2 — Stories:** Archivo `projects/m12-srs/stories.md` con ≥8 user stories y criterios de aceptación cada una.
3. **P3 — SRS:** `projects/m12-srs/srs-v1.md` con ≥3 RNF de seguridad/privacidad numerados y trazables.

## Proyecto útil

**SRS de Agenda Ops (piloto):** el documento en `projects/m12-srs/srs-v1.md` es la fuente de verdad para M13 (diseño) y M17 (build). Debe incluir:

- Alcance MVP acotado y lista de “no haremos todavía”.
- Roles owner/staff y reglas de acceso a datos sensibles.
- Referencia al ICP elegido y al design partner.

## Errores comunes

- Empezar por mockups de UI antes de problemas y criterios.
- Omitir seguridad (“luego en M18”) sin RNF ni criterios 403/401.
- MVP infinito: todo es Must; no hay fecha de freeze.
- Cambiar de sub-vertical cada semana y tirar el SRS anterior.
- Criterios de aceptación no testeables (“que se vea bien”).

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Entrevista:** `projects/m12-srs/entrevistas/notas-*.md` + `guion-v1.md`.
- **P2 — Stories:** `projects/m12-srs/stories.md` (≥8 stories con criterios).
- **P3 — SRS:** `projects/m12-srs/srs-v1.md` con ≥3 RNF seguridad/privacidad.
- **Proyecto — SRS Agenda Ops:** carpeta `projects/m12-srs/` lista (README actualizado si añades índice) para M13/M17.

## Criterios de dominio

- [ ] Sabes decir “no” a un requisito con alternativa y queda escrito en el SRS.
- [ ] El SRS incluye al menos 3 RNF de seguridad/privacidad verificables.
- [ ] Cada historia Must del MVP tiene criterio de aceptación que podría convertirse en test en M15/M17.
- [ ] El alcance de 4 semanas de build es creíble y está priorizado.
