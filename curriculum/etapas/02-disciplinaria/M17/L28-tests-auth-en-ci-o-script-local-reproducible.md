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

Deploy sin tests = regresión garantizada.

## Objetivo

Workflow CI o `npm run test:ci` documentado; suite auth+roles en verde.

## Pasos (hazlos en orden)

### 1. Pipeline (80–100 min)

GitHub Actions (u otro) con install + test. Secrets de CI ≠ prod.

### 2. README (20 min)

Badge o instrucción. Enlace a m15 si reutilizas.

### 3. Cierre semana 7 (20 min)

`docs/semana-07.md`.

### 4. Commit

`ci(m17): l28 tests auth en pipeline`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | m15 pipeline | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. CI verde (artefacto: `.github/workflows en m17`).
2. Auth en pipeline (artefacto: `.github/workflows en m17`).
3. Cierre semana 7 (artefacto: `.github/workflows en m17`).
4. Commit `docs(m17): L28 tests-auth-en-ci-o-script-local-reproducible`.

## Errores comunes

- Tests skipped en CI.
- Solo local.

## Siguiente

[L29 — ADR tenant_id y modelo multi-negocio](L29-adr-tenant-id-y-modelo-multi-negocio.md)
