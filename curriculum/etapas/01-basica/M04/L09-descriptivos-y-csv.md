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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Pipeline reproducible: CSV → parse → `media`/`mediana` →
      tabla Markdown commiteada.


      Bajas o inventas un CSV de pedidos diarios, limpias columnas básicas y
      calculas media, mediana y conteos — inicio formal de **P2**.
  - id: s2
    tipo: ejemplo
    titulo: 1. Dataset
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Descriptivos y primer pipeline CSV" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: >-
          projects/m04-stats/data/pedidos.csv + src/csv-descriptivos.ts +
          salida/tabla-descriptivos.md
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
    titulo: Método
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      Debes producir algo verificable (código, nota, commit) además de leer,
      antes de dar la lección por hecha.
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: 'Verdadero: práctica deliberada + evidencia.'
    explicacionOk: Exacto.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Pipeline reproducible: CSV → parse → `media`/`mediana` → tabla
          Markdown commiteada.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Parser
    xp: 10
    cuerpo: >-
      `src/csv-descriptivos.ts` lee el archivo ( `fs.readFileSync` + split o
      librería ligera), convierte `pedidos` a número, ignora filas inválidas con
      log.
  - id: s7
    tipo: ejemplo
    titulo: 3. Tabla de salida
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
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - CSV en `data/` con fuente documentada.
      - 'Script genera tabla con n, media, mediana.'
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
