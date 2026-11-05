---
id: L23
materia: M08
orden: 23
titulo: Dataset Agenda Ops y demo CLI
horas: 5
semana: 6
lectura: Dataset realista + CLI de demostración
evidencia: CSV/JSON demo + CLI
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cargar un dataset tipo Agenda Ops y exponer un CLI
      reproducible.


      Sin datos y sin demo, el autocomplete no es evidencia de proyecto.
  - id: s2
    tipo: ejemplo
    titulo: 1. Dataset
    xp: 10
    cuerpo: >-
      ```bash

      npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
      --prefix ti --k 5

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Dataset Agenda Ops y demo CLI" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: CSV/JSON demo + CLI
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
    enunciado: >-
      Escribe este comando tal cual (es el de práctica de la lección):


      `npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
      --prefix ti --k 5`
    comandoEsperado:
      - >-
        npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
        --prefix ti --k 5
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: >-
      Esperado: npx tsx autocomplete/cli.ts --data
      autocomplete/data/servicios.json --prefix ti --k 5
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: Cargar un dataset tipo Agenda Ops y exponer un CLI reproducible.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Loader
    xp: 10
    cuerpo: Función `loadAndBuild(path)` inserta todos los términos.
  - id: s7
    tipo: ejemplo
    titulo: 3. CLI
    xp: 10
    cuerpo: >-
      ```bash

      npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
      --prefix ti --k 5

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Dataset `autocomplete/data/` (CSV o JSON) con clientes/servicios demo
        (≥100 filas; ideal ≥1000).
      - >-
        CLI `npx tsx autocomplete/cli.ts --prefix cor` (o similar) imprime
        sugerencias.
      - >-
        README autocomplete con comando y nota de latencia; commit `feat(m08):
        dataset y CLI autocomplete`.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L23 — Dataset Agenda Ops y demo CLI

**~5.0 h · Semana 6**

Sin datos y sin demo, el autocomplete no es evidencia de proyecto.

## Objetivo

Cargar un dataset tipo Agenda Ops y exponer un CLI reproducible.

## Pasos

### 1. Dataset (50 min)

`autocomplete/data/servicios.json` (o csv): nombres realistas (corte, barba, tinte…). Genera ≥100 entradas (script corto aceptable).

### 2. Loader (40 min)

Función `loadAndBuild(path)` inserta todos los términos.

### 3. CLI (70 min)

`autocomplete/cli.ts`:

```bash
npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json --prefix ti --k 5
```

### 4. Latencia (40 min)

Cronometra suggest en frío/caliente; pega ms en `autocomplete/README.md` junto a N y estructura.

### 5. Commit (15 min)

```bash
git add projects/m08-algoritmos/autocomplete
git commit -m "feat(m08): dataset y CLI autocomplete"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Introducción a los algoritmos* — CLRS (ed. ES) | Cargar N términos; latencia de suggest en máquina local | [VisuAlgo](https://visualgo.net/en) |
| Catálogo | Entrada de esta materia | [Bibliografía · M08](../../../bibliografia.md#m08-analisis-de-algoritmos) |


## Hecho cuando

Marca la lección **solo si**:

1. Dataset `autocomplete/data/` (CSV o JSON) con clientes/servicios demo (≥100 filas; ideal ≥1000).
2. CLI `npx tsx autocomplete/cli.ts --prefix cor` (o similar) imprime sugerencias.
3. README autocomplete con comando y nota de latencia; commit `feat(m08): dataset y CLI autocomplete`.

## Errores comunes

- Dataset de 5 filas presentado como demo seria.
- CLI sin documentar en README.
- Medir latencia una sola vez con N minúscula y generalizar.

## Siguiente

[L24 — Cierre M08 y evidencias](L24-cierre-m08-y-evidencias.md)
