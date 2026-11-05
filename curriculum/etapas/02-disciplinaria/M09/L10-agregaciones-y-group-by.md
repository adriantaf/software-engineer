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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entregar `sql/agg-pedidos-por-servicio.sql` con al menos dos
      agregaciones ejecutadas.


      El dueño pregunta: “¿qué servicio se agenda más?”. Eso es `GROUP BY`.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Agregaciones y GROUP BY" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: sql/agg-pedidos-por-servicio.sql
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
      ¿Es buena práctica en esta lección? “Seleccionar columnas no agregadas
      fuera del `GROUP BY`."
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
          Entregar `sql/agg-pedidos-por-servicio.sql` con al menos dos
          agregaciones ejecutadas.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Escribe y corre
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
  - id: s7
    tipo: explicacion
    titulo: 3. Segunda query
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
