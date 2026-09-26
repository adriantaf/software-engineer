---
id: M16
titulo: Interacción humano-computadora
etapa: disciplinaria
orden: 16
semanas: 3
horas: 60
practicas:
  - id: p1
    titulo: Heurísticas de Nielsen aplicadas a tu UI
  - id: p2
    titulo: Test de usabilidad con 5 personas
  - id: p3
    titulo: Iteración de UI basada en hallazgos
proyecto:
  id: proj
  titulo: Informe de usabilidad del piloto Agenda Ops
---

# M16 — Interacción humano-computadora

## Por qué existe

Una UI confusa en Agenda Ops genera soporte eterno y abandono del piloto: el dueño del negocio no tiene paciencia para “adivinar” tu producto. La usabilidad no es solo estética: estados vacíos, errores claros y flujos cortos para agendar citas impactan retención. Los errores de UX tampoco deben **filtrar datos ajenos** (mostrar IDs internos, mensajes que revelan existencia de recursos prohibidos).

**En resumen:** dejas de diseñar solo para ti: heurísticas, test con 5 personas e iteración documentada sobre el piloto Agenda Ops.


## Objetivos de aprendizaje

Al terminar debes poder:

1. Evaluar una UI con las heurísticas de Nielsen (u equivalente) con severidad y recomendación.
2. Preparar un guion de test de usabilidad de 15–30 minutos para tareas del piloto (crear cita, ver agenda).
3. Facilitar al menos 5 sesiones con consentimiento básico y notas estructuradas.
4. Priorizar hallazgos (impacto × frecuencia) y traducirlos a cambios concretos.
5. Iterar la UI (prototipo o implementación) y documentar antes/después.
6. Redactar informe de usabilidad enlazado a `projects/m16-ihc/` para guiar M17.

## Cómo estudiar esta materia (lecciones)

M16 pone al usuario del piloto **Agenda Ops** en el centro: L01–L12.

1. Usa prototipo o UI parcial; si no existe, HTML estático en `projects/m16-ihc/prototipo/`.
2. Tests con personas reales (design partner o usuarios del sub-vertical); no solo auto-evaluación.
3. Tareas del test alineadas al SRS M12 (historias Must).
4. Marca lecciones al cumplir “Hecho cuando”.
5. [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Heurísticas | 6–8 | 4 lecciones semana 1 |
| Tests usuarios | 6–8 | Guion + 5 sesiones (semana 2) |
| Iteración | 4–6 | Fixes + informe (semana 3) |
| Retro | 1 | Hallazgo que te sorprendió |

Si un día solo tienes 2 h: **una lección** con artefacto en git.

## Lecciones

### Semana 1 — Heurísticas y evaluación experta (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L01 | [Recorrido persona nueva y fricciones día 1](M16/L01-recorrido-persona-nueva-y-fricciones-dia-1.md) | 5 |
| L02 | [Auditoría Nielsen — tres heurísticas profundas](M16/L02-auditoria-nielsen-tres-heuristicas-profundas.md) | 5 |
| L03 | [Estados vacío, carga y error en agenda](M16/L03-estados-vacio-carga-y-error-en-agenda.md) | 5 |
| L04 | [auditoria-v1 y cierre P1 heurísticas](M16/L04-auditoria-v1-y-cierre-p1-heuristicas.md) | 5 |

### Semana 2 — Prototipo y tests con usuarios (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L05 | [Prototipo navegable y tareas del SRS](M16/L05-prototipo-navegable-y-tareas-del-srs.md) | 5 |
| L06 | [Guion de test de usabilidad 15–30 min](M16/L06-guion-de-test-de-usabilidad-15-30-min.md) | 5 |
| L07 | [Sesiones 1–3 — notas de participantes](M16/L07-sesiones-1-3-notas-de-participantes.md) | 5 |
| L08 | [Sesiones 4–5 y resumen agregado P2](M16/L08-sesiones-4-5-y-resumen-agregado-p2.md) | 5 |

### Semana 3 — Iteración e informe (~20 h)

| ID | Lección | ~h |
|----|---------|-----|
| L09 | [Priorizar top 5 hallazgos](M16/L09-priorizar-top-5-hallazgos.md) | 5 |
| L10 | [Iteración UI — antes y después](M16/L10-iteracion-ui-antes-y-despues.md) | 5 |
| L11 | [Informe de usabilidad para stakeholders](M16/L11-informe-de-usabilidad-para-stakeholders.md) | 5 |
| L12 | [Cierre M16 — handoff M17 y criterios dominio](M16/L12-cierre-m16-handoff-m17-y-criterios-dominio.md) | 5 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: *No me hagas pensar* — Steve Krug (ed. ES). Alternativa: [heurísticas Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/). Ver [bibliografía](../../bibliografia.md#m16-ihc).

| Semana | Lecciones | Capítulos (Krug) / recursos | Alternativa |
|--------|-----------|----------------------------|-------------|
| 1 | L01–L04 | Usabilidad y escaneo + estados UI | NN/g heurísticas |
| 2 | L05–L08 | Navegación, formularios, test de pasillo | `projects/m16-ihc/prototipo/` |
| 3 | L09–L12 | Iteración → `informe-usabilidad.md` | Handoff UX a M17 |

**Regla:** prototipo → test con personas reales → cambios documentados.



## Ejemplo — fila de hallazgo con severidad

| ID | Heurística | Hallazgo | Severidad | Fix propuesto |
|----|------------|----------|-----------|---------------|
| H-03 | Prevención de errores | Fecha pasada permitida en formulario | Alta | Validación inline + deshabilitar pasado |
| H-07 | Flexibilidad | Staff no puede deshacer cita cancelada por error | Media | Confirmación + papelera 24 h |

## Ejemplo — guion de sesión (extracto)

```text
Contexto: piloto Agenda Ops para [sub-vertical]. No me defiendas; piensa en voz alta.
Tarea 1: Agenda una cita nueva para un cliente que no existe (15 min).
Tarea 2: Encuentra las citas de hoy y cancela una (10 min).
Al final: ¿qué fue lo más confuso? (2 min)
```

## Temario semanal

### Semana 1 — Heurísticas y evaluación experta (~20 h)

- Las 10 heurísticas de Nielsen (lectura + aplicación).
- Escaneo de páginas: jerarquía visual, CTAs, formularios.
- Estados vacíos, carga y error en flujos de citas.
- Entregable: `projects/m16-ihc/heuristicas/auditoria-v1.md` con severidad.

### Semana 2 — Prototipo y tests con usuarios (~20 h)

- Prototipo navegable (Figma, HTML o rama del front M17 si existe).
- Consentimiento básico y anonimización en notas (`sesiones/participante-N.md`).
- 5 sesiones mínimo; síntesis de patrones (no solo anécdotas).
- Entregable: `projects/m16-ihc/sesiones/resumen-5-usuarios.md`.

### Semana 3 — Iteración e informe (~20 h)

- Priorizar top 5 hallazgos; implementar o wireframear fixes.
- Antes/después en `projects/m16-ihc/iteracion/` (capturas o diff).
- Informe final para stakeholders del piloto.
- Entregable: `projects/m16-ihc/informe-usabilidad.md`.


## Prácticas

1. **P1 — Heurísticas:** `projects/m16-ihc/heuristicas/auditoria-v1.md` con hallazgos y severidad.
2. **P2 — 5 usuarios:** Notas en `projects/m16-ihc/sesiones/` + resumen agregado.
3. **P3 — Iteración:** `projects/m16-ihc/iteracion/` con evidencia antes/después y commits si aplica.

## Proyecto útil

**Informe de usabilidad del piloto Agenda Ops** (`projects/m16-ihc/informe-usabilidad.md`):

- Resumen ejecutivo para el design partner (1 página).
- Método, participantes, tareas, hallazgos principales.
- Cambios implementados o planificados para M17.
- Riesgos de UX que podrían convertirse en bugs de seguridad (mensajes verbosos, IDOR visual).

## Errores comunes

- Diseñar solo para ti (desarrollador con atajos de teclado).
- Ignorar estados de carga, error y vacío en agenda/citas.
- Tests sin guion (sesiones que no reproducen tareas del SRS).
- Mostrar IDs internos o datos de otros clientes en mensajes de error.
- Informe sin cambios concretos (“haríamos mejoras”).

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Heurísticas:** `projects/m16-ihc/heuristicas/auditoria-v1.md`.
- **P2 — 5 usuarios:** `projects/m16-ihc/sesiones/` (≥5 archivos o tabla) + `resumen-5-usuarios.md`.
- **P3 — Iteración:** `projects/m16-ihc/iteracion/` con antes/después.
- **Proyecto — Informe:** `projects/m16-ihc/informe-usabilidad.md` + índice en `projects/m16-ihc/README.md`.

## Criterios de dominio

- [ ] Informe con hallazgos, método y cambios hechos o planificados con prioridad.
- [ ] Al menos un hallazgo de severidad alta abordado en la iteración.
- [ ] Guion de test reutilizable para el siguiente ciclo post-M17.
- [ ] Mensajes de error no revelan datos de otros usuarios o existencia indebida de recursos.
