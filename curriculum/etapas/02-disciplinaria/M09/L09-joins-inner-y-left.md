---
id: L09
materia: M09
orden: 9
titulo: Joins inner y left
horas: 5
semana: 3
lectura: Elmasri SQL joins + PG tutorial Queries
evidencia: sql/joins-pedidos-cliente.sql ejecutado
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Completar y correr `sql/joins-pedidos-cliente.sql` con datos
      reales (aunque sean seeds mínimos).


      Los reportes del salón son JOINs. Hoy ejecutas los dos patrones básicos
      contra tu BD.
  - id: s2
    tipo: ejemplo
    titulo: 1. Seeds mínimos
    xp: 10
    cuerpo: |-
      ```bash
      psql "..." -f seeds/001_demo.sql
      psql "..." -c 'SELECT count(*) FROM pedidos;'
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Joins inner y left" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: sql/joins-pedidos-cliente.sql ejecutado
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
      ¿Es buena práctica en esta lección? “Usar solo comma-join (`FROM a, b
      WHERE`) sin entender la diferencia."
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
        texto: >-
          Completar y correr `sql/joins-pedidos-cliente.sql` con datos reales
          (aunque sean seeds mínimos).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Lectura SQL
    xp: 10
    cuerpo: >-
      Elmasri: joins. Alternativa: [PG tutorial —
      Queries](https://www.postgresql.org/docs/current/tutorial-select.html).
  - id: s7
    tipo: explicacion
    titulo: 3. Ejecuta el scaffold
    xp: 10
    cuerpo: >-
      Abre `sql/joins-pedidos-cliente.sql`. Corre cada query. Ajusta columnas si
      tu esquema diverge.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Ejecutaste INNER y LEFT JOIN del archivo (o el tuyo equivalente).
      - Hay comentario con salida de ejemplo en el `.sql` o en `samples/`.
      - 'Commit `feat(m09): joins pedidos cliente`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L09 — Joins inner y left

**~5.0 h · Semana 3**

Los reportes del salón son JOINs. Hoy ejecutas los dos patrones básicos contra tu BD.

## Objetivo

Completar y correr `sql/joins-pedidos-cliente.sql` con datos reales (aunque sean seeds mínimos).

## Pasos

### 1. Seeds mínimos (30–45 min)

Si no hay filas:

```bash
psql "..." -f seeds/001_demo.sql
psql "..." -c 'SELECT count(*) FROM pedidos;'
```

### 2. Lectura SQL (40 min)

Elmasri: joins. Alternativa: [PG tutorial — Queries](https://www.postgresql.org/docs/current/tutorial-select.html).

### 3. Ejecuta el scaffold (60 min)

Abre `sql/joins-pedidos-cliente.sql`. Corre cada query. Ajusta columnas si tu esquema diverge.

### 4. Añade un tercer join útil (45 min)

Ejemplo: pedidos `completada` de la última semana con teléfono del cliente (para recordatorio manual). Guárdalo en el mismo archivo o en `sql/joins-completadas-recientes.sql`.

### 5. Evidencia + commit (30 min)

Comenta al final del SQL 3–5 líneas de resultado. Commit.

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri SQL joins + PG tutorial Queries | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Ejecutaste INNER y LEFT JOIN del archivo (o el tuyo equivalente).
2. Hay comentario con salida de ejemplo en el `.sql` o en `samples/`.
3. Commit `feat(m09): joins pedidos cliente`.

## Errores comunes

- Usar solo comma-join (`FROM a, b WHERE`) sin entender la diferencia.
- LEFT JOIN y filtrar la tabla derecha en `WHERE` convirtiendo el left en inner sin querer.
- No tener seeds: joins sobre tablas vacías no enseñan nada.

## Siguiente

[L10 — Agregaciones y GROUP BY](L10-agregaciones-y-group-by.md)
