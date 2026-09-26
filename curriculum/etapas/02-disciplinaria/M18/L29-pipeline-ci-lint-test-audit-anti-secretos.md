---
id: L29
materia: M18
orden: 29
titulo: "Pipeline CI: lint, test, audit, anti-secretos"
horas: 5.0
semana: 8
lectura: Secure SDLC + CI guides
evidencia: projects/m18-appsec/ci-appsec.yml snippet o enlace workflow
---

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
