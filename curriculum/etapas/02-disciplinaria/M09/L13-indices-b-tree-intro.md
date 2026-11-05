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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un índice no es un logro: es una apuesta sobre lecturas vs escrituras.


      **Objetivo de esta lección:** Entender B-tree en la práctica y dejar un
      índice justificado por una query tuya.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```sql
      SELECT indexname, indexdef
      FROM pg_indexes
      WHERE tablename = 'pedidos';
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Inventario actual
    xp: 10
    cuerpo: |-
      ```sql
      SELECT indexname, indexdef
      FROM pg_indexes
      WHERE tablename = 'pedidos';
      ```

      Compara con lo que ya creó `001_init.sql`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Índices B-tree intro», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Índices B-tree intro
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
    pregunta: ¿Es recomendable en esta lección? “Indexar todas las columnas."
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
          Entender B-tree en la práctica y dejar un índice justificado por una
          query tuya.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Elige una query lenta potencial
    xp: 10
    cuerpo: >-
      Ej. filtrar por `estado` + rango de `inicia_en`. Diseña: Ponlo en
      `migrations/002_auditoria_y_indices.sql` (o archivo nuevo) si aún no está.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Creas (o justificas) al menos un índice adicional alineado a un reporte.
      - Documentas en `explain-notas.md` o migración por qué existe.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
