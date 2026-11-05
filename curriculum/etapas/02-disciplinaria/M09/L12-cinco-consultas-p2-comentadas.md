---
id: L12
materia: M09
orden: 12
titulo: Cinco consultas P2 comentadas
horas: 5
semana: 3
lectura: Repaso Elmasri SQL + tutorial PG
evidencia: sql/ con ≥5 archivos .sql comentados — avanza P2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Dejar ≥5 SQL comentados, ejecutables, orientados a Vitrina.


      Cierras el paquete de consultas de la práctica **P2** (falta EXPLAIN en
      semana 4).
  - id: s2
    tipo: ejemplo
    titulo: 1. Inventario
    xp: 10
    cuerpo: |-
      ```bash
      ls projects/m09-bases-datos/sql/*.sql
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cinco consultas P2 comentadas" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: sql/ con ≥5 archivos .sql comentados — avanza P2
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `ls projects/m09-bases-datos/sql/*.sql`
    comandoEsperado:
      - ls projects/m09-bases-datos/sql/*.sql
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: ls projects/m09-bases-datos/sql/*.sql'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: 'Dejar ≥5 SQL comentados, ejecutables, orientados a Vitrina.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Completa el set
    xp: 10
    cuerpo: >-
      Mínimo sugerido:


      1. `joins-pedidos-cliente.sql` (L09)

      2. `agg-pedidos-por-servicio.sql` (L10)

      3. `subq-clientes-frecuentes.sql` (L11)

      4. `reporte-pedido abandonados.sql` — tasa o listado de pedido abandonado

      5. `reporte-agenda-del-dia.sql` — pedidos de un día (`\set dia
      '''2026-09-26'''` o literal)


      Cada archivo: encabezado con pregunta de negocio + comentario de salida.
  - id: s7
    tipo: explicacion
    titulo: 3. Smoke test
    xp: 10
    cuerpo: Corre los cinco seguidos; arregla los que fallen.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Hay ≥5 archivos `.sql` en `sql/` (joins, agg, subq, +2 reportes o
        variantes).
      - Cada uno tiene comentario de propósito + salida ejemplo.
      - Commit de paquete P2 queries.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L12 — Cinco consultas P2 comentadas

**~5.0 h · Semana 3**

Cierras el paquete de consultas de la práctica **P2** (falta EXPLAIN en semana 4).

## Objetivo

Dejar ≥5 SQL comentados, ejecutables, orientados a Vitrina.

## Pasos

### 1. Inventario (20 min)

```bash
ls projects/m09-bases-datos/sql/*.sql
```

### 2. Completa el set (150 min)

Mínimo sugerido:

1. `joins-pedidos-cliente.sql` (L09)
2. `agg-pedidos-por-servicio.sql` (L10)
3. `subq-clientes-frecuentes.sql` (L11)
4. `reporte-pedido abandonados.sql` — tasa o listado de pedido abandonado
5. `reporte-agenda-del-dia.sql` — pedidos de un día (`\set dia '''2026-09-26'''` o literal)

Cada archivo: encabezado con pregunta de negocio + comentario de salida.

### 3. Smoke test (40 min)

Corre los cinco seguidos; arregla los que fallen.

### 4. Commit (20 min)

```bash
git add projects/m09-bases-datos/sql
git commit -m "feat(m09): cinco consultas P2 comentadas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Repaso Elmasri SQL + tutorial PG | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Hay ≥5 archivos `.sql` en `sql/` (joins, agg, subq, +2 reportes o variantes).
2. Cada uno tiene comentario de propósito + salida ejemplo.
3. Commit de paquete P2 queries.

## Errores comunes

- Cinco archivos vacíos o idénticos.
- Queries que no corren.
- Sin relación con preguntas de negocio del salón.

## Siguiente

[L13 — Índices B-tree intro](L13-indices-b-tree-intro.md)
