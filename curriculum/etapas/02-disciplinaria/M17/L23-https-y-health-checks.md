---
id: L23
materia: M17
orden: 23
titulo: HTTPS y health checks
horas: 5.0
semana: 6
lectura: "TLS Let's Encrypt / proveedor"
evidencia: HTTPS + /health
---

# L23 — HTTPS y health checks

**~5.0 h · Semana 6**

Design partner no debe ver “no seguro”.

## Objetivo

Forzar HTTPS en prod/staging y health check para monitor.

## Conceptos clave

- TLS
- HSTS
- health

## Pasos (hazlos en orden)

### 1. Fuerza HTTPS (40–50 min)

```bash
curl -sSI https://TU-STAGING.example/health | head -20
# sin -k; certificado válido
curl -sS -o /dev/null -w "%{http_code}\n" http://TU-STAGING.example/health
# redirect 301/308 a https o rechazo
```

### 2. Health externo (40 min)

```bash
curl -sS https://TU-STAGING.example/health
# pega JSON (sin secrets) en docs/deploy.md
```

### 3. Commit (15 min)

```bash
git add projects/m17-vitrina/docs/deploy.md
git commit -m "docs(m17): L23 https y health checks"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | TLS Let's Encrypt / proveedor | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. HTTPS válido en staging; `GET /health` externo 200 documentado en deploy.md.
2. Commit `docs(m17): L23 https-y-health-checks`.

## Errores comunes

- Usar `curl -k` como ‘HTTPS OK’.
- Health solo en localhost.

## Siguiente

[L24 — Smoke test post-deploy](L24-smoke-test-post-deploy.md)
