---
id: L15
materia: M09
orden: 15
titulo: Optimizar query lenta de reporte
horas: 5
semana: 4
lectura: Elmasri selectividad / PG Index-Only Scans intro
evidencia: Plan DESPUÉS + cambio (índice o reescritura)
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Una pasada de EXPLAIN no basta: cambias algo y vuelves a medir.


      **Objetivo de esta lección:** Completar “Plan (después)” y la conclusión
      en `explain-notas.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Hipótesis
    xp: 10
    cuerpo: >-
      Ejemplos: falta índice en `(tenant_id, inicia_en)`; `WHERE date(inicia_en)
      = …` impide uso de índice; SELECT * innecesario.
  - id: s3
    tipo: ejemplo
    titulo: Cambia una sola cosa
    xp: 10
    cuerpo: >-
      Índice **o** reescritura (mejor `inicia_en >= @start AND inicia_en < @end`
      que casteos).
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Optimizar query lenta de reporte», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Optimizar query lenta
          de reporte
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
      ¿Es recomendable en esta lección? “Declarar victoria sin segunda
      medición."
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
        texto: Completar “Plan (después)” y la conclusión en `explain-notas.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Remide
    xp: 10
    cuerpo: 'Mismo `EXPLAIN (ANALYZE, BUFFERS)`. Pega en la sección después.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Aplicas un cambio (índice, filtro, reescritura).'
      - Vuelves a correr EXPLAIN ANALYZE.
      - Documentas comparación antes/después.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L15 — Optimizar query lenta de reporte

**~5.0 h · Semana 4**

Una pasada de EXPLAIN no basta: cambias algo y vuelves a medir.

## Objetivo

Completar “Plan (después)” y la conclusión en `explain-notas.md`.

## Pasos

### 1. Hipótesis (30 min)

Ejemplos: falta índice en `(tenant_id, inicia_en)`; `WHERE date(inicia_en) = …` impide uso de índice; SELECT * innecesario.

### 2. Cambia una sola cosa (60–90 min)

Índice **o** reescritura (mejor `inicia_en >= @start AND inicia_en < @end` que casteos).

### 3. Remide (45 min)

Mismo `EXPLAIN (ANALYZE, BUFFERS)`. Pega en la sección después.

### 4. Criterio de éxito (30 min)

Si con seeds pequeños no hay diferencia, dilo honestamente y explica qué pasaríacon 100k pedidos (orden de magnitud).

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri selectividad / PG Index-Only Scans intro | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Aplicas un cambio (índice, filtro, reescritura).
2. Vuelves a correr EXPLAIN ANALYZE.
3. Documentas comparación antes/después.

## Errores comunes

- Declarar victoria sin segunda medición.
- Índice que no se usa (tipo de dato / función sobre columna).
- Optimizar una query que nadie corre.

## Siguiente

[L16 — Documentar planes de ejecución](L16-documentar-planes-de-ejecucion.md)
