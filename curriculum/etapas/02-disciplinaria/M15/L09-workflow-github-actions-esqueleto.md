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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: |-
      **Objetivo:** `.github/workflows/` con job de test para M15.

      P2: CI real. Hoy el esqueleto que falla si los tests fallan.
  - id: s2
    tipo: ejemplo
    titulo: 1. Escribe YAML
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Workflow GitHub Actions — esqueleto" como hecha, ¿qué cuenta
      de verdad?
    opciones:
      - id: a
        texto: .github/workflows/m15-ci.yml (o documentado) verde
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
    pregunta: ¿Es buena práctica en esta lección? “Workflow solo en docs sin YAML."
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
        texto: '`.github/workflows/` con job de test para M15.'
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 3. Commit + push cuando puedas verificar
    xp: 10
    cuerpo: '`ci(m15): workflow esqueleto github actions`'
  - id: s7
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
