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

El design partner no debe ver “No seguro”.

## Objetivo

HTTPS en staging; `/health` usable por monitor/deploy script.

## Pasos (hazlos en orden)

### 1. Verifica TLS (40 min)

```bash
curl -vI https://TU-STAGING/health
```

Cert válido; redirige HTTP→HTTPS si aplica.

### 2. Health útil (50–60 min)

Incluye status DB o documenta por qué no. Wire al platform healthcheck.

### 3. Notas HSTS (20 min)

Opcional en staging; plan para prod.

### 4. Commit

`feat(m17): l23 https y health`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | TLS Let's Encrypt / proveedor | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. HTTPS activo.
2. Health remoto (artefacto: `HTTPS`).
3. Commit (artefacto: `HTTPS`).

## Errores comunes

- HTTP prod.
- Health sin DB check documentado.

## Siguiente

[L24 — Smoke test post-deploy](L24-smoke-test-post-deploy.md)
