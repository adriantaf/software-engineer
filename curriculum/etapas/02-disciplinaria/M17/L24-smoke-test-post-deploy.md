---
id: L24
materia: M17
orden: 24
titulo: Smoke test post-deploy
horas: 5.0
semana: 6
lectura: Checklist smoke
evidencia: projects/m17-agenda-ops/docs/smoke-test.md
---

# L24 — Smoke test post-deploy

**~5.0 h · Semana 6**

Detecta config rota antes de la demo.

## Objetivo

`docs/smoke-test.md` con corrida fechada: login + crear cita (+ health).

## Pasos (hazlos en orden)

### 1. Escribe checklist/script (50 min)

Pasos curl o Playwright mínimo contra staging.

### 2. Ejecuta y registra (60–80 min)

Fecha, resultado, fallos. No uses datos del partner real.

### 3. Cierre semana 6 (20 min)

Enlace smoke desde README.

### 4. Commit

`docs(m17): l24 smoke test staging`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Checklist smoke | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. smoke-test.md (artefacto: `projects/m17-agenda-ops/docs/smoke-test.md`).
2. Corrida fechada (artefacto: `projects/m17-agenda-ops/docs/smoke-test.md`).
3. Cierre semana 6 (artefacto: `projects/m17-agenda-ops/docs/smoke-test.md`).
4. Commit `docs(m17): L24 smoke-test-post-deploy`.

## Errores comunes

- Smoke solo health.
- Olvidar auth.

## Siguiente

[L25 — Mapa OWASP Top 10 en el piloto](L25-mapa-owasp-top-10-en-el-piloto.md)
