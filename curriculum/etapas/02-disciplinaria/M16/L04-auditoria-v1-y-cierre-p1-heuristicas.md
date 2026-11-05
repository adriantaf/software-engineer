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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P1 = auditoría con severidad. Hoy empaquetas.


      **Objetivo de esta lección:** `auditoria-v1.md` listo para marcar P1.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Merge L01–L03
    xp: 10
    cuerpo: Una tabla maestra de hallazgos + apéndice de método.
  - id: s3
    tipo: ejemplo
    titulo: Commit
    xp: 10
    cuerpo: '`docs(m16): auditoria-v1 cierre P1`'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «auditoria-v1 y cierre P1 heurísticas», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de auditoria-v1 y cierre
          P1 heurísticas
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Archivo parcial renombrado sin
      consolidar."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: '`auditoria-v1.md` listo para marcar P1.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “Sin severidades."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
