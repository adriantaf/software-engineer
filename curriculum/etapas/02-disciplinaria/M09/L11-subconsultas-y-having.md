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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      “Clientes con más de 2 pedidos completadas” pide filtrar **grupos**, no
      filas.


      **Objetivo de esta lección:** Crear `sql/subq-clientes-frecuentes.sql` con
      `HAVING` y al menos una subconsulta.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: HAVING
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Subconsultas y HAVING», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Subconsultas y HAVING
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
      ¿Es recomendable en esta lección? “Usar `WHERE count(*) > 1` en lugar de
      `HAVING`."
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
        texto: >-
          Crear `sql/subq-clientes-frecuentes.sql` con `HAVING` y al menos una
          subconsulta.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Subconsulta
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
