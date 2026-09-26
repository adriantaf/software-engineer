---
id: L22
materia: M17
orden: 22
titulo: Deploy staging en PaaS
horas: 5.0
semana: 6
lectura: Docs PaaS elegido
evidencia: URL staging
---

# L22 — Deploy staging en PaaS

**~5.0 h · Semana 6**

Piloto invisible no es piloto.

## Objetivo

URL staging + `docs/deploy.md` paso a paso (build, env, migraciones).

## Pasos (hazlos en orden)

### 1. Elige PaaS (20 min)

Render/Fly/Railway/etc. Anota límites free tier.

### 2. Deploy (100–130 min)

Build reproducible; secrets en panel; migra DB staging.

### 3. Documenta (30 min)

URL en README (staging). `docs/deploy.md`.

### 4. Commit

`docs(m17): l22 deploy staging paas`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Docs PaaS elegido | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Staging URL (artefacto: `URL staging`).
2. deploy.md (artefacto: `URL staging`).
3. Build CI opcional (artefacto: `URL staging`).
4. Commit `docs(m17): L22 deploy-staging-en-paas`.

## Errores comunes

- Deploy manual sin doc.
- Solo localhost.

## Siguiente

[L23 — HTTPS y health checks](L23-https-y-health-checks.md)
