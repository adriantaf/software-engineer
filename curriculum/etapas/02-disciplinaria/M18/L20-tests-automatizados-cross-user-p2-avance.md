---
id: L20
materia: M18
orden: 20
titulo: Tests automatizados cross-user (P2 avance)
horas: 5.0
semana: 5
lectura: Testing access control
evidencia: tests en repo producto + projects/m18-appsec/findings-table.md
---

# L20 — Tests automatizados cross-user (P2 avance)

**~5.0 h · Semana 5**

P2 avanza con tests que fallen si vuelve el IDOR.

## Objetivo

≥2 tests cross-user en CI local; tabla hallazgos con ≥3 filas PoC→fix→test.

## Pasos (hazlos en orden)

### 1. Escribe tests (90–110 min)

Usuario A no lee/edita recurso B.

### 2. Tabla P2 (40 min)

`hallazgos.md` columnas requeridas.

### 3. Commit

`test(m18): l20 cross-user p2 avance`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Testing access control | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥2 tests authz verdes (artefacto: `tests en repo producto`).
2. findings-table ≥3 filas (artefacto: `tests en repo producto`).
3. Commits referenciados (artefacto: `tests en repo producto`).

## Errores comunes

- Tests que mockean auth siempre true.
- Un solo usuario en tests.

## Siguiente

[L21 — SSRF: superficie en webhooks e integraciones](L21-ssrf-superficie-en-webhooks-e-integraciones.md)
