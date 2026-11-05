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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los reportes del salón son JOINs. Hoy ejecutas los dos patrones básicos
      contra tu BD.


      **Objetivo de esta lección:** Completar y correr
      `sql/joins-pedidos-cliente.sql` con datos reales (aunque sean seeds
      mínimos).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Seeds mínimos
    xp: 10
    cuerpo: |-
      ```bash
      psql "..." -f seeds/001_demo.sql
      psql "..." -c 'SELECT count(*) FROM pedidos;'
      ```

      Si no hay filas:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Lectura SQL
    xp: 10
    cuerpo: |-
      ```bash
      psql "..." -f seeds/001_demo.sql
      psql "..." -c 'SELECT count(*) FROM pedidos;'
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Joins inner y left», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Joins inner y left
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `psql "..." -f seeds/001_demo.sql`
    comandoEsperado:
      - psql "..." -f seeds/001_demo.sql
      - psql "..." -c 'SELECT count(*) FROM pedidos;'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: psql "..." -f seeds/001_demo.sql'
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
        texto: >-
          Completar y correr `sql/joins-pedidos-cliente.sql` con datos reales
          (aunque sean seeds mínimos).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Ejecuta el scaffold
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
