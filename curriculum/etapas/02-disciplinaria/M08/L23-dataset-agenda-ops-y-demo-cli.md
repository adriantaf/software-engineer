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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Sin datos y sin demo, el autocomplete no es evidencia de proyecto.


      **Objetivo de esta lección:** Cargar un dataset tipo Agenda Ops y exponer
      un CLI reproducible.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Dataset
    xp: 10
    cuerpo: >-
      ```bash

      npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
      --prefix ti --k 5

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Loader
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m08-algoritmos/autocomplete
      git commit -m "feat(m08): dataset y CLI autocomplete"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Dataset Agenda Ops y demo CLI», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Dataset Agenda Ops y
          demo CLI
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: >-
      Escribe el comando de práctica de esta lección:


      `npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
      --prefix ti --k 5`
    comandoEsperado:
      - >-
        npx tsx autocomplete/cli.ts --data autocomplete/data/servicios.json
        --prefix ti --k 5
      - git add projects/m08-algoritmos/autocomplete
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: >-
      Esperado: npx tsx autocomplete/cli.ts --data
      autocomplete/data/servicios.json --prefix ti --k 5
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
        texto: Cargar un dataset tipo Agenda Ops y exponer un CLI reproducible.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: CLI
    xp: 10
    cuerpo: '`autocomplete/cli.ts`:'
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
