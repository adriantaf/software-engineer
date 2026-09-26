---
id: L31
materia: M18
orden: 31
titulo: Tests de regresión de seguridad (≥3)
horas: 5.0
semana: 8
lectura: Security unit tests patterns
evidencia: ≥3 tests en repo producto
---

# L31 — Tests de regresión de seguridad (≥3)

**~5.0 h · Semana 8**

≥3 tests que fallen si reabres agujeros.

## Objetivo

Suite seguridad documentada: IDOR, XSS escape, authz rol (o equivalentes).

## Pasos (hazlos en orden)

### 1. Selecciona 3 (20 min)

### 2. Implementa/verde (100–120 min)

Nombres claros `security.*.test.ts`.

### 3. Commit

`test(m18): l31 regresion seguridad`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Security unit tests patterns | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥3 tests listados (artefacto: `≥3 tests en repo producto`).
2. CI los ejecuta (artefacto: `≥3 tests en repo producto`).
3. Todos verdes (artefacto: `≥3 tests en repo producto`).
4. Commit `docs(m18): L31 tests-de-regresion-de-seguridad-3`.

## Errores comunes

- Tests skipped.
- Solo manual.

## Siguiente

[L32 — Cierre M18 — dominio y riesgo residual](L32-cierre-m18-dominio-y-riesgo-residual.md)
