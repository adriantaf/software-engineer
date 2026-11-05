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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar “Plan (después)” y la conclusión en
      `explain-notas.md`.


      Una pasada de EXPLAIN no basta: cambias algo y vuelves a medir.
  - id: s2
    tipo: ejemplo
    titulo: 1. Hipótesis
    xp: 10
    cuerpo: >-
      Ejemplos: falta índice en `(tenant_id, inicia_en)`; `WHERE date(inicia_en)
      = …` impide uso de índice; SELECT * innecesario.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Optimizar query lenta de reporte" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: Plan DESPUÉS + cambio (índice o reescritura)
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
      ¿Es buena práctica en esta lección? “Declarar victoria sin segunda
      medición."
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
        texto: Completar “Plan (después)” y la conclusión en `explain-notas.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Cambia una sola cosa
    xp: 10
    cuerpo: >-
      Índice **o** reescritura (mejor `inicia_en >= @start AND inicia_en < @end`
      que casteos).
  - id: s7
    tipo: explicacion
    titulo: 3. Remide
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
