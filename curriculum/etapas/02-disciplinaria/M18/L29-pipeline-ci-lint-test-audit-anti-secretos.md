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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Workflow documentado en
      `projects/m18-appsec/ci/ci-appsec.yml` (o enlace) +
      `projects/m18-appsec/ci/README.md` con run id.


      P3: cada PR corre lint+test+audit (+ grep secretos).
  - id: s2
    tipo: ejemplo
    titulo: 1. Scaffold workflow
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
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Pipeline CI: lint, test, audit, anti-secretos" como hecha,
      ¿qué cuenta de verdad?
    opciones:
      - id: a
        texto: projects/m18-appsec/ci-appsec.yml snippet o enlace workflow
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
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `mkdir -p projects/m18-appsec/ci`
    comandoEsperado:
      - mkdir -p projects/m18-appsec/ci
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: mkdir -p projects/m18-appsec/ci'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Workflow documentado en `projects/m18-appsec/ci/ci-appsec.yml` (o
          enlace) + `projects/m18-appsec/ci/README.md` con run id.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Ejecuta en branch de prueba
    xp: 10
    cuerpo: >-
      Copia al repo producto, push, pega run id en
      `projects/m18-appsec/ci/README.md`.


      ```bash

      cat > projects/m18-appsec/ci/README.md <<'EOF'

      CI AppSec

      - Workflow: .github/workflows/appsec.yml

      - Run id / URL:

      - Jobs: lint, test, audit, anti-secrets

      EOF

      ```
  - id: s7
    tipo: ejemplo
    titulo: 3. Commit
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
