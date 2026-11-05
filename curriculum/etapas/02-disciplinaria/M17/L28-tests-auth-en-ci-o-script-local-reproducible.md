---
id: L28
materia: M17
orden: 28
titulo: Tests auth en CI o script local reproducible
horas: 5
semana: 7
lectura: m15 pipeline
evidencia: .github/workflows en m17
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Asegurar que suite auth+roles corre en CI o script
      documentado `npm run test:ci`.


      - CI

      - regresión

      - auth tests
  - id: s2
    tipo: ejemplo
    titulo: 1. CI o script reproducible
    xp: 10
    cuerpo: |-
      ```yaml
      # .github/workflows/m17-auth.yml (si usas GH Actions)
      name: m17-auth
      on: [push, pull_request]
      jobs:
        test:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4
            - run: npm ci
            - run: npm test -- auth
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tests auth en CI o script local reproducible" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: .github/workflows en m17
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
    pregunta: ¿Es buena práctica en esta lección? “‘Corre en mi laptop’ sin script/CI."
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
          Asegurar que suite auth+roles corre en CI o script documentado `npm
          run test:ci`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Evidencia + commit
    xp: 10
    cuerpo: |-
      ```bash
      bash scripts/ci-auth.sh   # o mira el run verde en Actions
      git add .github/workflows projects/m17-vitrina/scripts 2>/dev/null || true
      git add projects/m17-vitrina
      git commit -m "ci(m17): L28 tests auth reproducibles"
      ```
  - id: s7
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        Workflow CI o `scripts/ci-auth.sh` deja suite auth verde de forma
        reproducible.
      - 'Commit `docs(m17): L28 tests-auth-en-ci-o-script-local-reproducible`.'
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L28 — Tests auth en CI o script local reproducible

**~5.0 h · Semana 7**

Deploy sin tests es regresión garantizada.

## Objetivo

Asegurar que suite auth+roles corre en CI o script documentado `npm run test:ci`.

## Conceptos clave

- CI
- regresión
- auth tests

## Pasos (hazlos en orden)

### 1. CI o script reproducible (70–90 min)

```yaml
# .github/workflows/m17-auth.yml (si usas GH Actions)
name: m17-auth
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test -- auth
```

Alternativa local documentada:

```bash
# scripts/ci-auth.sh
set -euo pipefail
npm ci
npm test -- auth
```

### 2. Evidencia + commit (30 min)

```bash
bash scripts/ci-auth.sh   # o mira el run verde en Actions
git add .github/workflows projects/m17-vitrina/scripts 2>/dev/null || true
git add projects/m17-vitrina
git commit -m "ci(m17): L28 tests auth reproducibles"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m15 pipeline | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Workflow CI **o** `scripts/ci-auth.sh` deja suite auth verde de forma reproducible.
2. Commit `docs(m17): L28 tests-auth-en-ci-o-script-local-reproducible`.

## Errores comunes

- ‘Corre en mi laptop’ sin script/CI.
- CI que no ejecuta tests auth.

## Siguiente

[L29 — ADR tenant_id y modelo multi-negocio](L29-adr-tenant-id-y-modelo-multi-negocio.md)
