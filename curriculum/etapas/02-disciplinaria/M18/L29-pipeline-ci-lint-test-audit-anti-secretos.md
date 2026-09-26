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

P3: CI con lint+test+audit+grep secretos.

## Objetivo

Workflow verde documentado en `projects/m18-appsec/ci/`.

## Pasos (hazlos en orden)

### 1. Pipeline (100–120 min)

Enlace al workflow del repo app. Job anti-secretos básico.

### 2. Evidencia (30 min)

Log CI o script local reproducible.

### 3. Commit

`ci(m18): l29 pipeline p3`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Secure SDLC + CI guides | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. CI documentado (artefacto: `projects/m18-appsec/ci-appsec.yml snippet o enlace workflow`).
2. Audit en pipeline (artefacto: `projects/m18-appsec/ci-appsec.yml snippet o enlace workflow`).
3. Run verde o excepciones justificadas (artefacto: `projects/m18-appsec/ci-appsec.yml snippet o enlace workflow`).
4. Commit `docs(m18): L29 pipeline-ci-lint-test-audit-anti-secretos`.

## Errores comunes

- CI que nunca falla.
- Secretos en workflow logs.

## Siguiente

[L30 — Estructura del informe AppSec](L30-estructura-del-informe-appsec.md)
