---
id: L09
materia: M04
orden: 9
titulo: Descriptivos y primer pipeline CSV
horas: 5
semana: 3
lectura: Walpole cap. 1 + descriptivos · OpenStax Ch. 1–2
evidencia: >-
  projects/m04-stats/data/pedidos.csv + src/csv-descriptivos.ts +
  salida/tabla-descriptivos.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Bajas o inventas un CSV de pedidos diarios, limpias columnas básicas y
      calculas media, mediana y conteos — inicio formal de **P2**.


      **Objetivo de esta lección:** Pipeline reproducible: CSV → parse →
      `media`/`mediana` → tabla Markdown commiteada.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dataset
    xp: 10
    cuerpo: |-
      ```markdown
      # Descriptivos — pedidos

      | Métrica | pedidos | ingresos_mxn |
      |---------|---------|--------------|
      | n | | |
      | media | | |
      | mediana | | |
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Parser
    xp: 10
    cuerpo: >-
      ```bash

      git add projects/m04-stats/data projects/m04-stats/salida
      projects/m04-stats/src/csv-descriptivos.ts

      git commit -m "feat(m04): pipeline CSV descriptivos L09"

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Descriptivos y primer pipeline CSV», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: CSV en `data/` con fuente documentada.
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Descriptivos y primer
          pipeline CSV
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Práctica deliberada
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      Además de leer, debes producir algo verificable (código, nota, commit o
      ejercicio) antes de dar la lección por hecha.
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: 'Verdadero: sin evidencia no hay progreso real.'
    explicacionOk: Exacto.
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
          Pipeline reproducible: CSV → parse → `media`/`mediana` → tabla
          Markdown commiteada.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Tabla de salida
    xp: 10
    cuerpo: '`salida/tabla-descriptivos.md`:'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - CSV en `data/` con fuente documentada.
      - 'Script genera tabla con n, media, mediana.'
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Descriptivos y primer pipeline CSV

**~5 h · Semana 3**

Bajas o inventas un CSV de pedidos diarios, limpias columnas básicas y calculas media, mediana y conteos — inicio formal de **P2**.

## Objetivo

Pipeline reproducible: CSV → parse → `media`/`mediana` → tabla Markdown commiteada.

## Pasos

### 1. Dataset (45 min)

Crea `data/pedidos.csv` con ≥30 filas, columnas sugeridas:

`fecha, pedidos, ingresos_mxn, canal`

O descarga un CSV pequeño de [datos.gob.mx](https://datos.gob.mx) y documenta la fuente en `data/README.md`.

### 2. Parser (60 min)

`src/csv-descriptivos.ts` lee el archivo ( `fs.readFileSync` + split o librería ligera), convierte `pedidos` a número, ignora filas inválidas con log.

### 3. Tabla de salida (40 min)

`salida/tabla-descriptivos.md`:

```markdown
# Descriptivos — pedidos

| Métrica | pedidos | ingresos_mxn |
|---------|---------|--------------|
| n | | |
| media | | |
| mediana | | |
```

### 4. Lectura (90 min)

Walpole cap. 1 (datos) + medidas de tendencia central.

### 5. Commit

```bash
git add projects/m04-stats/data projects/m04-stats/salida projects/m04-stats/src/csv-descriptivos.ts
git commit -m "feat(m04): pipeline CSV descriptivos L09"
```

## Hecho cuando

1. CSV en `data/` con fuente documentada.
2. Script genera tabla con n, media, mediana.
3. Commit.

## Siguiente

[L10 — Dispersión, percentiles y outliers](L10-dispersion-percentiles-outliers.md)
