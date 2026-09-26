---
id: L07
materia: M19
orden: 7
titulo: "Smoke test: login, cita y health externo"
horas: 5.0
semana: 2
lectura: Runbook borrador
evidencia: projects/m19-ops/smoke-staging.md
---

# L07 — Smoke test: login, cita y health externo

**~5.0 h · Semana 2**

Health solo no basta: login + crear cita.

## Objetivo

Corrida fechada en `deploy-log.md` o `smoke-staging.md`.

## Pasos (hazlos en orden)

### 1. Script/checklist (50 min)

### 2. Ejecuta contra staging (70–90 min)

Registra pass/fail.

### 3. Commit

`docs(m19): l07 smoke staging`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Runbook borrador | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Smoke completo (artefacto: `projects/m19-ops/smoke-staging.md`).
2. health externo (artefacto: `projects/m19-ops/smoke-staging.md`).
3. Fecha registrada (artefacto: `projects/m19-ops/smoke-staging.md`).
4. Commit `docs(m19): L07 smoke-test-login-cita-y-health-externo`.

## Errores comunes

- Solo health sin login.
- Smoke nunca repetido.

## Siguiente

[L08 — Dominios y deploy-log semana 2](L08-dominios-y-deploy-log-semana-2.md)
