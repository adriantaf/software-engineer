---
id: L26
materia: M17
orden: 26
titulo: Headers de seguridad y CORS prod
horas: 5.0
semana: 7
lectura: MDN security headers
evidencia: helmet o equivalente
---

# L26 — Headers de seguridad y CORS prod

**~5.0 h · Semana 7**

Reduce superficie antes de abrir al partner.

## Objetivo

Configurar headers básicos y CORS restrictivo a dominio front.

## Conceptos clave

- helmet
- CORS
- CSP intro

## Pasos (hazlos en orden)

### 1. Headers seguridad (60–80 min)

```ts
// helmet() o equivalentes: CSP básica, nosniff, frameguard
```

```bash
curl -sSI https://TU-STAGING.example/health | rg -i 'content-security|x-frame|x-content-type|strict-transport'
```

### 2. CORS prod (40 min)

Allowlist `CORS_ORIGIN` de staging/prod — no `*`. Documenta en `docs/deploy.md`.

```bash
git add projects/m17-agenda-ops
git commit -m "feat(m17): L26 headers seguridad cors"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN security headers | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Headers de seguridad visibles en `curl -sSI`; CORS allowlist (no `*`).
2. Commit `docs(m17): L26 headers-de-seguridad-y-cors-prod`.

## Errores comunes

- `Access-Control-Allow-Origin: *` en prod.
- Sin `helmet`/equivalente y sin nota.

## Siguiente

[L27 — Rate limit en login](L27-rate-limit-en-login.md)
