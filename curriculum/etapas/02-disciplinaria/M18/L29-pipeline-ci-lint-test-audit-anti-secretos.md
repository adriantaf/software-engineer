---
id: L29
materia: M18
orden: 29
titulo: 'Pipeline CI: lint, test, audit, anti-secretos'
horas: 5
semana: 8
lectura: Secure SDLC + CI guides
evidencia: projects/m18-appsec/ci-appsec.yml snippet o enlace workflow
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      P3: cada PR corre lint+test+audit (+ grep secretos).


      **Objetivo de esta lección:** Workflow documentado en
      `projects/m18-appsec/ci/ci-appsec.yml` (o enlace) +
      `projects/m18-appsec/ci/README.md` con run id.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Scaffold workflow
    xp: 10
    cuerpo: |-
      ```bash
      mkdir -p projects/m18-appsec/ci
      cat > projects/m18-appsec/ci/ci-appsec.yml <<'EOF'
      # Copiar a .github/workflows/appsec.yml del repo producto
      name: appsec
      on: [pull_request, push]
      jobs:
        check:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-node@v4
              with: { node-version: "20" }
            - run: npm ci
            - run: npm run lint
            - run: npm test
            - run: npm audit --audit-level=high
            - name: anti-secrets
              run: |
                ! git ls-files | rg -i '\.env$|id_rsa|\.pem$'
      EOF
      ```
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s3
    tipo: ejemplo
    titulo: Ejecuta en branch de prueba
    xp: 10
    cuerpo: >-
      ```bash

      cat > projects/m18-appsec/ci/README.md <<'EOF'

      # CI AppSec

      - Workflow: .github/workflows/appsec.yml

      - Run id / URL:

      - Jobs: lint, test, audit, anti-secrets

      EOF

      ```


      Copia al repo producto, push, pega run id en
      `projects/m18-appsec/ci/README.md`.
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Pipeline CI: lint, test, audit, anti-secretos», ¿qué
      demuestra que cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Pipeline CI: lint,
          test, audit, anti-se…
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `mkdir -p projects/m18-appsec/ci`
    comandoEsperado:
      - mkdir -p projects/m18-appsec/ci
      - git add projects/m18-appsec/ci
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: mkdir -p projects/m18-appsec/ci'
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
          Workflow documentado en `projects/m18-appsec/ci/ci-appsec.yml` (o
          enlace) + `projects/m18-appsec/ci/README.md` con run id.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Commit
    xp: 10
    cuerpo: |-
      ```bash
      git add projects/m18-appsec/ci
      git commit -m "ci(m18): l29 pipeline p3"
      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - >-
        CI documentado (artefacto: `projects/m18-appsec/ci-appsec.yml snippet o
        enlace workflow`).
      - >-
        Audit en pipeline (artefacto: `projects/m18-appsec/ci-appsec.yml snippet
        o enlace workflow`).
      - 'Commit `docs(m18): L29 pipeline-ci-lint-test-audit-anti-secretos`.'
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L29 — Pipeline CI: lint, test, audit, anti-secretos

**~5.0 h · Semana 8**

P3: cada PR corre lint+test+audit (+ grep secretos).

## Objetivo

Workflow documentado en `projects/m18-appsec/ci/ci-appsec.yml` (o enlace) + `projects/m18-appsec/ci/README.md` con run id.

## Pasos

### 1. Scaffold workflow (40–50 min)

```bash
mkdir -p projects/m18-appsec/ci
cat > projects/m18-appsec/ci/ci-appsec.yml <<'EOF'
# Copiar a .github/workflows/appsec.yml del repo producto
name: appsec
on: [pull_request, push]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm audit --audit-level=high
      - name: anti-secrets
        run: |
          ! git ls-files | rg -i '\.env$|id_rsa|\.pem$'
EOF
```
### 2. Ejecuta en branch de prueba (60–80 min)

Copia al repo producto, push, pega run id en `projects/m18-appsec/ci/README.md`.

```bash
cat > projects/m18-appsec/ci/README.md <<'EOF'
# CI AppSec
- Workflow: .github/workflows/appsec.yml
- Run id / URL:
- Jobs: lint, test, audit, anti-secrets
EOF
```
### 3. Commit (10 min)

```bash
git add projects/m18-appsec/ci
git commit -m "ci(m18): l29 pipeline p3"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Secure SDLC + CI guides | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. CI documentado (artefacto: `projects/m18-appsec/ci-appsec.yml snippet o enlace workflow`).
2. Audit en pipeline (artefacto: `projects/m18-appsec/ci-appsec.yml snippet o enlace workflow`).
3. Commit `docs(m18): L29 pipeline-ci-lint-test-audit-anti-secretos`.

## Errores comunes

- CI que nunca falla.
- Secretos en workflow logs.

## Siguiente

[L30 — Estructura del informe AppSec](L30-estructura-del-informe-appsec.md)
