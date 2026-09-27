---
id: L28
materia: M17
orden: 28
titulo: Tests auth en CI o script local reproducible
horas: 5.0
semana: 7
lectura: m15 pipeline
evidencia: .github/workflows en m17
---

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
git add .github/workflows projects/m17-agenda-ops/scripts 2>/dev/null || true
git add projects/m17-agenda-ops
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
