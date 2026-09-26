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

Helmet (o equivalente) + CORS restrictivo; `docs/seguridad-http.md`.

## Pasos (hazlos en orden)

### 1. Headers (60–80 min)

Activa en staging; verifica con curl/`securityheaders` mental checklist.

### 2. CORS (40 min)

Solo origen del front. Documenta preflight.

### 3. Doc (20 min)

Valores y cómo probarlos.

### 4. Commit

`feat(m17): l26 headers cors seguridad`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | MDN security headers | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Headers activos prod (artefacto: `helmet o equivalente`).
2. CORS no `*`.
3. Doc (artefacto: `helmet o equivalente`).
4. Commit `docs(m17): L26 headers-de-seguridad-y-cors-prod`.

## Errores comunes

- CORS abierto.
- CSP rota sin probar.

## Siguiente

[L27 — Rate limit en login](L27-rate-limit-en-login.md)
