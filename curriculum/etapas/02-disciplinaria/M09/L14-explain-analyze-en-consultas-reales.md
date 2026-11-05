---
id: L14
materia: M09
orden: 14
titulo: EXPLAIN ANALYZE en consultas reales
horas: 5
semana: 4
lectura: 'PG: EXPLAIN / Using EXPLAIN'
evidencia: explain-notas.md con plan ANTES pegado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El plan de ejecución es la radiografía. Hoy lees una de **tu** query.


      **Objetivo de esta lección:** Llenar la sección “Plan (antes…)” de
      `explain-notas.md`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```sql
      EXPLAIN (ANALYZE, BUFFERS)
      SELECT …;
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Elige query
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "docs(m09): explain analyze reporte diario"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «EXPLAIN ANALYZE en consultas reales», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de EXPLAIN ANALYZE en
          consultas reales
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
      ¿Es recomendable en esta lección? “Solo `EXPLAIN` sin `ANALYZE` y hablar
      de tiempos reales."
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
        texto: Llenar la sección “Plan (antes…)” de `explain-notas.md`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Corre EXPLAIN
    xp: 10
    cuerpo: Pega salida completa en `explain-notas.md`.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Corres `EXPLAIN (ANALYZE, BUFFERS)` sobre una query de reporte.'
      - Pegas el plan en `explain-notas.md` (sección antes).
      - Explicas en llano Seq Scan vs Index Scan.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L14 — EXPLAIN ANALYZE en consultas reales

**~5.0 h · Semana 4**

El plan de ejecución es la radiografía. Hoy lees una de **tu** query.

## Objetivo

Llenar la sección “Plan (antes…)” de `explain-notas.md`.

## Pasos

### 1. Lectura (45 min)

[Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — enfócate en nodos Seq Scan, Index Scan, cost, rows, actual time.

### 2. Elige query (20 min)

Copia tu reporte diario o agg a `sql/explain-reporte-diario.sql`.

### 3. Corre EXPLAIN (60 min)

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT …;
```

Pega salida completa en `explain-notas.md`.

### 4. Traducción al español (60 min)

Escribe 5–8 líneas: qué nodo domina, estimaciones vs reality (`rows` vs `actual rows`), buffers.

### 5. Commit (15 min)

```bash
git commit -am "docs(m09): explain analyze reporte diario"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | PG: EXPLAIN / Using EXPLAIN | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Corres `EXPLAIN (ANALYZE, BUFFERS)` sobre una query de reporte.
2. Pegas el plan en `explain-notas.md` (sección antes).
3. Explicas en llano Seq Scan vs Index Scan.

## Errores comunes

- Solo `EXPLAIN` sin `ANALYZE` y hablar de tiempos reales.
- Pegar el plan sin interpretar una sola línea.
- Medir con tabla vacía.

## Siguiente

[L15 — Optimizar query lenta de reporte](L15-optimizar-query-lenta-de-reporte.md)
