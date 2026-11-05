---
id: L13
materia: M09
orden: 13
titulo: Índices B-tree intro
horas: 5
semana: 4
lectura: 'Elmasri: índices; PG docs Indexes / CREATE INDEX'
evidencia: Índice nuevo documentado + \d pedidos
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Entender B-tree en la práctica y dejar un índice justificado
      por una query tuya.


      Un índice no es un logro: es una apuesta sobre lecturas vs escrituras.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```sql
      SELECT indexname, indexdef
      FROM pg_indexes
      WHERE tablename = 'pedidos';
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Índices B-tree intro" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: Índice nuevo documentado + \d pedidos
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
    pregunta: ¿Es buena práctica en esta lección? “Indexar todas las columnas."
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
          Entender B-tree en la práctica y dejar un índice justificado por una
          query tuya.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Inventario actual
    xp: 10
    cuerpo: |-
      ```sql
      SELECT indexname, indexdef
      FROM pg_indexes
      WHERE tablename = 'pedidos';
      ```

      Compara con lo que ya creó `001_init.sql`.
  - id: s7
    tipo: ejemplo
    titulo: 3. Elige una query lenta potencial
    xp: 10
    cuerpo: |-
      ```sql
      CREATE INDEX IF NOT EXISTS idx_citas_estado_inicia
        ON pedidos (estado, inicia_en);
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Creas (o justificas) al menos un índice adicional alineado a un reporte.
      - Documentas en `explain-notas.md` o migración por qué existe.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L13 — Índices B-tree intro

**~5.0 h · Semana 4**

Un índice no es un logro: es una apuesta sobre lecturas vs escrituras.

## Objetivo

Entender B-tree en la práctica y dejar un índice justificado por una query tuya.

## Pasos

### 1. Lectura (50 min)

Elmasri (índices) + [PG CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) (solo B-tree por ahora).

### 2. Inventario actual (30 min)

```sql
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'pedidos';
```

Compara con lo que ya creó `001_init.sql`.

### 3. Elige una query lenta potencial (60 min)

Ej. filtrar por `estado` + rango de `inicia_en`. Diseña:

```sql
CREATE INDEX IF NOT EXISTS idx_citas_estado_inicia
  ON pedidos (estado, inicia_en);
```

Ponlo en `migrations/002_auditoria_y_indices.sql` (o archivo nuevo) si aún no está.

### 4. Aplica y verifica (40 min)

```bash
psql "..." -f migrations/002_auditoria_y_indices.sql
psql "..." -c '\d pedidos'
```

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Fundamentos de BD* — Elmasri & Navathe (ed. ES) | Elmasri: índices; PG docs Indexes / CREATE INDEX | [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M09](../../../bibliografia.md#m09-bases-de-datos) |


## Hecho cuando

Marca la lección **solo si**:

1. Creas (o justificas) al menos un índice adicional alineado a un reporte.
2. Documentas en `explain-notas.md` o migración por qué existe.
3. Commit.

## Errores comunes

- Indexar todas las columnas.
- Índice único accidental que rompe inserts legítimos.
- No saber qué es B-tree vs “magia del motor”.

## Siguiente

[L14 — EXPLAIN ANALYZE en consultas reales](L14-explain-analyze-en-consultas-reales.md)
