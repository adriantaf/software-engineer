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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** Llenar la sección “Plan (antes…)” de `explain-notas.md`.

      El plan de ejecución es la radiografía. Hoy lees una de **tu** query.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```sql
      EXPLAIN (ANALYZE, BUFFERS)
      SELECT …;
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "EXPLAIN ANALYZE en consultas reales" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: explain-notas.md con plan ANTES pegado
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
      ¿Es buena práctica en esta lección? “Solo `EXPLAIN` sin `ANALYZE` y hablar
      de tiempos reales."
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
        texto: Llenar la sección “Plan (antes…)” de `explain-notas.md`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Elige query
    xp: 10
    cuerpo: Copia tu reporte diario o agg a `sql/explain-reporte-diario.sql`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Corre EXPLAIN
    xp: 10
    cuerpo: |-
      ```sql
      EXPLAIN (ANALYZE, BUFFERS)
      SELECT …;
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - 'Corres `EXPLAIN (ANALYZE, BUFFERS)` sobre una query de reporte.'
      - Pegas el plan en `explain-notas.md` (sección antes).
      - Explicas en llano Seq Scan vs Index Scan.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
