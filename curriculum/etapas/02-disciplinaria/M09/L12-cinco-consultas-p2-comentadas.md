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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cierras el paquete de consultas de la práctica **P2** (falta EXPLAIN en
      semana 4).


      **Objetivo de esta lección:** Dejar ≥5 SQL comentados, ejecutables,
      orientados a Vitrina.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Inventario
    xp: 10
    cuerpo: |-
      ```bash
      ls projects/m09-bases-datos/sql/*.sql
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Completa el set
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m09-bases-datos/sql
      git commit -m "feat(m09): cinco consultas P2 comentadas"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cinco consultas P2 comentadas», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cinco consultas P2
          comentadas
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

      `ls projects/m09-bases-datos/sql/*.sql`
    comandoEsperado:
      - ls projects/m09-bases-datos/sql/*.sql
      - git add projects/m09-bases-datos/sql
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: ls projects/m09-bases-datos/sql/*.sql'
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
        texto: 'Dejar ≥5 SQL comentados, ejecutables, orientados a Vitrina.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Smoke test
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
