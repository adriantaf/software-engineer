---
id: L27
materia: M17
orden: 27
titulo: Rate limit en login
horas: 5.0
semana: 7
lectura: OWASP brute force
evidencia: rate limit middleware
---

# L27 — Rate limit en login

**~5.0 h · Semana 7**

Piloto en internet ⇒ mínimo anti-fuerza bruta.

## Objetivo

Rate limit login → 429 documentado; no romper CI.

## Pasos (hazlos en orden)

### 1. Middleware (70–90 min)

Por IP y/o email; ventana corta; mensaje claro.

### 2. Prueba (40 min)

N intentos → 429. Config de test con umbral bajo.

### 3. Doc (15 min)

Úsalo en owasp-mapa (A07).

### 4. Commit

`feat(m17): l27 rate limit login`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | OWASP brute force | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Rate limit (artefacto: `rate limit middleware`).
2. 429 test o manual (artefacto: `rate limit middleware`).
3. Commit (artefacto: `rate limit middleware`).

## Errores comunes

- Sin límite.
- Lockout permanente sin doc.

## Siguiente

[L28 — Tests auth en CI o script local reproducible](L28-tests-auth-en-ci-o-script-local-reproducible.md)
