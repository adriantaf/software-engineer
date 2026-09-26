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

## Cómo estudiar esta materia

- Elige **un** sub-vertical (barbería, consultorio, taller…) y no lo cambies en estas tres semanas.
- Cada sesión: entrevista o story → criterio de aceptación → línea en el SRS (`projects/m12-srs/`).
- Lee [producto-saas.md](../../producto-saas.md) una vez al inicio; el SRS debe alinearse con el piloto single-tenant, no con el SaaS multi-tenant completo.
- La “lectura” principal es la plantilla del repo, rellenada con evidencia real o simulación seria.

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Entrevistas | 6–8 | Guion + notas + síntesis |
| Stories + RNF | 6–8 | Aceptación + seguridad/privacidad |
| SRS v1 | 4–6 | Plantilla llenada + priorización MVP |
| Retro | 1 | Un “no” dicho con alternativa documentada |

Si un día solo tienes 2 h: **práctica + proyecto**. La fila de Lecturas de esa semana no se salta.

## Día 1 (2–3 h) — hazlo hoy

1. Crea la estructura de evidencia:
   ```bash
   mkdir -p projects/m12-srs/entrevistas
   cp projects/m12-srs/plantilla.md projects/m12-srs/srs-borrador.md
   ```
2. Elige el sub-vertical de tu design partner (un negocio real o personaje documentado con seriedad).
3. Escribe `projects/m12-srs/entrevistas/guion-v1.md` con al menos 10 preguntas abiertas (flujo de citas, clientes, roles, qué duele hoy).
4. Realiza la entrevista (presencial, llamada o simulación con guion y notas timestamp) y guarda `projects/m12-srs/entrevistas/notas-YYYY-MM-DD.md`.
5. Lista **5 problemas observados** (sin proponer pantallas todavía) en `projects/m12-srs/problemas.md`.
6. Commit: `docs(m12): guion y notas de entrevista inicial`.

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

## Lecturas

Canon: plantilla IEEE 830 adaptada en el repo + [producto-saas.md](../../producto-saas.md). Ver [bibliografía](../../bibliografia.md).

| Semana | Lectura obligatoria | Entrega ligada |
|--------|--------------------|----------------|
| 1 | [`projects/m12-srs/plantilla.md`](../../../projects/m12-srs/plantilla.md) (estructura) + notas de entrevista | `guion-v1.md` + `notas-*.md` + `problemas.md` |
| 2 | Misma plantilla: secciones **funcionales** + **RNF** (seguridad, privacidad, performance) | `stories.md` (≥8) + borrador SRS |
| 3 | Priorización MVP (MoSCoW) + freeze de alcance 4 semanas de build | `projects/m12-srs/srs-v1.md` firmado por ti (fecha en el doc) |

**Regla:** no hay novela de libro esta materia: la lectura es la plantilla + rellenar con evidencia de entrevistas y decisiones explícitas.

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
