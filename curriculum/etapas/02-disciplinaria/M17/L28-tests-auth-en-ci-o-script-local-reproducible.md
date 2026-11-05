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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      - CI

      - regresión

      - auth tests


      **Objetivo de esta lección:** Asegurar que suite auth+roles corre en CI o
      script documentado `npm run test:ci`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: CI o script reproducible
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

      Alternativa local documentada:
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Evidencia + commit
    xp: 10
    cuerpo: |-
      ```bash
      bash scripts/ci-auth.sh   # o mira el run verde en Actions
      git add .github/workflows projects/m17-vitrina/scripts 2>/dev/null || true
      git add projects/m17-vitrina
      git commit -m "ci(m17): L28 tests auth reproducibles"
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tests auth en CI o script local reproducible», ¿qué demuestra
      que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tests auth en CI o
          script local reprodu…
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
    pregunta: ¿Es recomendable en esta lección? “‘Corre en mi laptop’ sin script/CI."
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
          Asegurar que suite auth+roles corre en CI o script documentado `npm
          run test:ci`.
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
    pregunta: ¿Debes hacer esto? “CI que no ejecuta tests auth."
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
        Workflow CI o `scripts/ci-auth.sh` deja suite auth verde de forma
        reproducible.
      - 'Commit `docs(m17): L28 tests-auth-en-ci-o-script-local-reproducible`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
