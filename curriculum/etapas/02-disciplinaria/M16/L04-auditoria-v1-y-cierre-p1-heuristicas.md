---
id: L04
materia: M16
orden: 4
titulo: auditoria-v1 y cierre P1 heurísticas
horas: 5
semana: 1
lectura: Consolidar auditoría v1; evidencia P1
evidencia: heuristicas/auditoria-v1.md (P1)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `auditoria-v1.md` listo para marcar P1.

      P1 = auditoría con severidad. Hoy empaquetas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Merge L01–L03
    xp: 10
    cuerpo: Una tabla maestra de hallazgos + apéndice de método.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "auditoria-v1 y cierre P1 heurísticas" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: heuristicas/auditoria-v1.md (P1)
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Archivo parcial renombrado sin
      consolidar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: '`auditoria-v1.md` listo para marcar P1.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Commit
    xp: 10
    cuerpo: '`docs(m16): auditoria-v1 cierre P1`'
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        `heuristicas/auditoria-v1.md` consolida hallazgos (incl. estados) con
        severidad y fix propuesto.
      - README enlaza P1.
      - 'Commit `docs(m16): auditoria-v1 cierre P1`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L04 — auditoria-v1 y cierre P1 heurísticas

**~5.0 h · Semana 1**

P1 = auditoría con severidad. Hoy empaquetas.

## Objetivo

`auditoria-v1.md` listo para marcar P1.

## Pasos (hazlos en orden)

### 1. Merge L01–L03 (70–90 min)

Una tabla maestra de hallazgos + apéndice de método.

### 2. Top riesgos (40 min)

### 3. Commit

`docs(m16): auditoria-v1 cierre P1`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *No me hagas pensar* — Steve Krug (ed. ES) | Cierre P1: auditoria-v1 con severidad | [Heurísticas Nielsen (NN/g)](https://www.nngroup.com/articles/ten-usability-heuristics/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M16](../../../bibliografia.md#m16-ihc) |


## Hecho cuando

Marca la lección **solo si**:

1. `heuristicas/auditoria-v1.md` consolida hallazgos (incl. estados) con severidad y fix propuesto.
2. README enlaza P1.
3. Commit `docs(m16): auditoria-v1 cierre P1`.

## Errores comunes

- Archivo parcial renombrado sin consolidar.
- Sin severidades.
- P1 marcado con fricciones sueltas únicamente.

## Siguiente

[L05 — Prototipo navegable y tareas del SRS](L05-prototipo-navegable-y-tareas-del-srs.md)
