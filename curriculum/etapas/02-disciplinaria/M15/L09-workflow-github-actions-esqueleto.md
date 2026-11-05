---
id: L09
materia: M15
orden: 9
titulo: Workflow GitHub Actions — esqueleto
horas: 5
semana: 3
lectura: GitHub Actions basics; ci.yml
evidencia: .github/workflows/m15-ci.yml (o documentado) verde
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P2: CI real. Hoy el esqueleto que falla si los tests fallan.


      **Objetivo de esta lección:** `.github/workflows/` con job de test para
      M15.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Escribe YAML
    xp: 10
    cuerpo: |-
      ```yaml
      name: m15-ci
      on: [push, pull_request]
      jobs:
        test:
          runs-on: ubuntu-latest
          defaults:
            run:
              working-directory: projects/m15-calidad
          steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-node@v4
              with:
                node-version: "20"
                cache: npm
                cache-dependency-path: projects/m15-calidad/package-lock.json
            - run: npm ci
            - run: npm test
      ```

      Ajusta si aún no hay lockfile (`npm install`).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Commit + push cuando puedas verificar
    xp: 10
    cuerpo: |-
      ```yaml
      name: m15-ci
      on: [push, pull_request]
      jobs:
        test:
          runs-on: ubuntu-latest
          defaults:
            run:
              working-directory: projects/m15-calidad
          steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-node@v4
              with:
                node-version: "20"
                cache: npm
                cache-dependency-path: projects/m15-calidad/package-lock.json
            - run: npm ci
            - run: npm test
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Workflow GitHub Actions — esqueleto», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Workflow GitHub Actions
          — esqueleto
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
    pregunta: ¿Es recomendable en esta lección? “Workflow solo en docs sin YAML."
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
        texto: '`.github/workflows/` con job de test para M15.'
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: quiz
    titulo: Segundo error común
    xp: 10
    variante: verdadero_falso
    pregunta: ¿Debes hacer esto? “`npm test` en raíz sin `working-directory`."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: No — es otro anti-patrón de la lección.
    explicacionOk: Bien.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Workflow YAML que corre en push/PR e instala deps + `npm test` en
        `projects/m15-calidad` (o monorepo doc).
      - README M15 enlaza al workflow / badge path.
      - 'Commit `ci(m15): workflow esqueleto github actions`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L09 — Workflow GitHub Actions — esqueleto

**~5.0 h · Semana 3**

P2: CI real. Hoy el esqueleto que falla si los tests fallan.

## Objetivo

`.github/workflows/` con job de test para M15.

## Pasos (hazlos en orden)

### 1. Escribe YAML (60–70 min)

```yaml
name: m15-ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: projects/m15-calidad
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: npm
          cache-dependency-path: projects/m15-calidad/package-lock.json
      - run: npm ci
      - run: npm test
```

Ajusta si aún no hay lockfile (`npm install`).

### 2. Documenta ruta (30 min)

### 3. Commit + push cuando puedas verificar

`ci(m15): workflow esqueleto github actions`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Workflow CI: checkout, node, npm test | [GitHub Actions — Quickstart](https://docs.github.com/es/actions/writing-workflows/quickstart) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Workflow YAML que corre en push/PR e instala deps + `npm test` en `projects/m15-calidad` (o monorepo doc).
2. README M15 enlaza al workflow / badge path.
3. Commit `ci(m15): workflow esqueleto github actions`.

## Errores comunes

- Workflow solo en docs sin YAML.
- `npm test` en raíz sin `working-directory`.
- Secrets pegados en el YAML.

## Siguiente

[L10 — Lint y formato en pipeline](L10-lint-y-formato-en-pipeline.md)
