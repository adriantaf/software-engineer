---
id: L10
materia: M09
orden: 10
titulo: Agregaciones y GROUP BY
horas: 5
semana: 3
lectura: 'Elmasri: agregación GROUP BY; PG aggregate functions'
evidencia: sql/agg-pedidos-por-servicio.sql
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El dueño pregunta: “¿qué servicio se agenda más?”. Eso es `GROUP BY`.


      **Objetivo de esta lección:** Entregar `sql/agg-pedidos-por-servicio.sql`
      con al menos dos agregaciones ejecutadas.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```sql
      -- sql/agg-pedidos-por-servicio.sql
      SELECT s.nombre,
             count(*) AS total_citas,
             count(*) FILTER (WHERE c.estado = 'completada') AS completadas,
             coalesce(sum(s.precio_centavos) FILTER (WHERE c.estado = 'completada'), 0) AS ingresos_centavos
      FROM pedidos c
      JOIN servicios s ON s.id = c.servicio_id
      GROUP BY s.id, s.nombre
      ORDER BY total_citas DESC;
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Escribe y corre
    xp: 10
    cuerpo: |-
      ```sql
      -- sql/agg-pedidos-por-servicio.sql
      SELECT s.nombre,
             count(*) AS total_citas,
             count(*) FILTER (WHERE c.estado = 'completada') AS completadas,
             coalesce(sum(s.precio_centavos) FILTER (WHERE c.estado = 'completada'), 0) AS ingresos_centavos
      FROM pedidos c
      JOIN servicios s ON s.id = c.servicio_id
      GROUP BY s.id, s.nombre
      ORDER BY total_citas DESC;
      ```

      (Ajusta si usas snapshot de precio en la pedido.)
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Agregaciones y GROUP BY», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Agregaciones y GROUP BY
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
      ¿Es recomendable en esta lección? “Seleccionar columnas no agregadas fuera
      del `GROUP BY`."
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
          Entregar `sql/agg-pedidos-por-servicio.sql` con al menos dos
          agregaciones ejecutadas.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Segunda query
    xp: 10
    cuerpo: 'Pedidos por día (`date_trunc(''day'', inicia_en)`) de los últimos 14 días.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Existe y corre un SQL con `GROUP BY` + `COUNT`/`SUM`.
      - Interpretas el resultado en una frase de negocio.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Agregaciones y GROUP BY

**~5.0 h · Semana 3**

El dueño pregunta: “¿qué servicio se agenda más?”. Eso es `GROUP BY`.

## Objetivo

Entregar `sql/agg-pedidos-por-servicio.sql` con al menos dos agregaciones ejecutadas.

## Pasos

### 1. Lectura (40 min)

Funciones de agregación y `GROUP BY` / `WHERE` vs filtros de grupo.

### 2. Escribe y corre (90 min)

```sql
-- sql/agg-pedidos-por-servicio.sql
SELECT s.nombre,
       count(*) AS total_citas,
       count(*) FILTER (WHERE c.estado = 'completada') AS completadas,
       coalesce(sum(s.precio_centavos) FILTER (WHERE c.estado = 'completada'), 0) AS ingresos_centavos
FROM pedidos c
JOIN servicios s ON s.id = c.servicio_id
GROUP BY s.id, s.nombre
ORDER BY total_citas DESC;
```

(Ajusta si usas snapshot de precio en la pedido.)

### 3. Segunda query (45 min)

Pedidos por día (`date_trunc('day', inicia_en)`) de los últimos 14 días.

### 4. Frase de negocio (20 min)

En comentario del SQL: “El servicio más agendado esta semana es X con N pedidos”.

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: agregación GROUP BY; PG aggregate functions | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Existe y corre un SQL con `GROUP BY` + `COUNT`/`SUM`.
2. Interpretas el resultado en una frase de negocio.
3. Commit.

## Errores comunes

- Seleccionar columnas no agregadas fuera del `GROUP BY`.
- Sumar `precio` en float.
- Reportar conteos sin filtrar `cancelada` cuando la pregunta es “atendidas”.

## Siguiente

[L11 — Subconsultas y HAVING](L11-subconsultas-y-having.md)
