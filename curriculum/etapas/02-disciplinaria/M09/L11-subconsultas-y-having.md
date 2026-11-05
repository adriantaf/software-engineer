---
id: L11
materia: M09
orden: 11
titulo: Subconsultas y HAVING
horas: 5
semana: 3
lectura: 'Elmasri: subconsultas; HAVING'
evidencia: sql/subq-clientes-frecuentes.sql
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Crear `sql/subq-clientes-frecuentes.sql` con `HAVING` y al
      menos una subconsulta.


      “Clientes con más de 2 pedidos completadas” pide filtrar **grupos**, no
      filas.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```sql
      SELECT cl.nombre, count(*) AS completadas
      FROM pedidos c
      JOIN clientes cl ON cl.id = c.cliente_id
      WHERE c.estado = 'completada'
      GROUP BY cl.id, cl.nombre
      HAVING count(*) >= 2
      ORDER BY completadas DESC;
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Subconsultas y HAVING" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: sql/subq-clientes-frecuentes.sql
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
      ¿Es buena práctica en esta lección? “Usar `WHERE count(*) > 1` en lugar de
      `HAVING`."
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
          Crear `sql/subq-clientes-frecuentes.sql` con `HAVING` y al menos una
          subconsulta.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. HAVING
    xp: 10
    cuerpo: |-
      ```sql
      SELECT cl.nombre, count(*) AS completadas
      FROM pedidos c
      JOIN clientes cl ON cl.id = c.cliente_id
      WHERE c.estado = 'completada'
      GROUP BY cl.id, cl.nombre
      HAVING count(*) >= 2
      ORDER BY completadas DESC;
      ```
  - id: s7
    tipo: explicacion
    titulo: 3. Subconsulta
    xp: 10
    cuerpo: >-
      Lista servicios que **nunca** se han agendado (`NOT EXISTS` o `LEFT JOIN …
      IS NULL`). Prefiere `EXISTS` y explica por qué en un comentario.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Una query con `HAVING` y otra con subconsulta (`IN` / `EXISTS` /
        escalar).
      - Ambas ejecutadas con comentario de salida.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L11 — Subconsultas y HAVING

**~5.0 h · Semana 3**

“Clientes con más de 2 pedidos completadas” pide filtrar **grupos**, no filas.

## Objetivo

Crear `sql/subq-clientes-frecuentes.sql` con `HAVING` y al menos una subconsulta.

## Pasos

### 1. Lectura (40 min)

Subconsultas escalares, `IN`/`EXISTS`, y `HAVING`.

### 2. HAVING (60 min)

```sql
SELECT cl.nombre, count(*) AS completadas
FROM pedidos c
JOIN clientes cl ON cl.id = c.cliente_id
WHERE c.estado = 'completada'
GROUP BY cl.id, cl.nombre
HAVING count(*) >= 2
ORDER BY completadas DESC;
```

### 3. Subconsulta (60 min)

Lista servicios que **nunca** se han agendado (`NOT EXISTS` o `LEFT JOIN … IS NULL`). Prefiere `EXISTS` y explica por qué en un comentario.

### 4. Compara mentalmente con JOIN (30 min)

Reescribe una de las dos con puro JOIN. ¿Más legible? Anota preferencia.

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: subconsultas; HAVING | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Una query con `HAVING` y otra con subconsulta (`IN` / `EXISTS` / escalar).
2. Ambas ejecutadas con comentario de salida.
3. Commit.

## Errores comunes

- Usar `WHERE count(*) > 1` en lugar de `HAVING`.
- Subconsulta correlacionada innecesariamente lenta sin mirar el plan (eso es L14; hoy solo correctness).
- Clientes frecuentes incluyendo solo canceladas.

## Siguiente

[L12 — Cinco consultas P2 comentadas](L12-cinco-consultas-p2-comentadas.md)
