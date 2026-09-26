---
id: L06
materia: M19
orden: 6
titulo: Deploy staging con HTTPS
horas: 5.0
semana: 2
lectura: "Proveedor: deploy + TLS"
evidencia: projects/m19-ops/deploy-log.md
---

# L06 — Deploy staging con HTTPS

**~5.0 h · Semana 2**

Staging HTTPS estable usando la decisión del ADR.

## Objetivo

URL HTTPS en `deploy-log.md`; secretos solo en el hosting.

## Pasos (hazlos en orden)

### 1. Deploy (100–130 min)

Build, migraciones, env. Reusa o mejora M17 staging.

### 2. Verifica TLS (30 min)

### 3. Commit

`docs(m19): l06 deploy staging https`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Proveedor: deploy + TLS | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. URL HTTPS viva.
2. deploy-log entrada (artefacto: `projects/m19-ops/deploy-log.md`).
3. Sin secretos en repo (artefacto: `projects/m19-ops/deploy-log.md`).
4. Commit `docs(m19): L06 deploy-staging-con-https`.

## Errores comunes

- HTTP plano.
- TLS solo en front.

## Siguiente

[L07 — Smoke test: login, cita y health externo](L07-smoke-test-login-cita-y-health-externo.md)
