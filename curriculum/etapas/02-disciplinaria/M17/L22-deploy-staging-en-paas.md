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

Desplegar API+front o API primero en staging con build reproducible.

## Conceptos clave

- deploy
- staging
- build

## Pasos (hazlos en orden)

### 1. Elige PaaS y despliega (90–120 min)

Fly/Render/Railway/etc. Build desde Dockerfile o buildpack. Secrets en el panel, no en git.

```bash
# ejemplo genérico — sustituye por CLI real
# fly launch / render blueprint / railway up
curl -sS https://TU-STAGING.example/health
```

### 2. Documenta URL (30 min)

```bash
mkdir -p projects/m17-vitrina/docs
echo "Staging: https://TU-STAGING.example" > projects/m17-vitrina/docs/deploy.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/deploy.md
git commit -m "docs(m17): L22 deploy staging paas"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Docs PaaS elegido | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m17-vitrina/docs/deploy.md` incluye URL staging alcanzable.
2. Commit `docs(m17): L22 deploy-staging-en-paas`.

## Errores comunes

- URL staging solo en chat, no en `docs/deploy.md`.
- Secrets en variables del Dockerfile.

## Siguiente

[L23 — HTTPS y health checks](L23-https-y-health-checks.md)
