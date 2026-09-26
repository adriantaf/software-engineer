---
id: L23
materia: M18
orden: 23
titulo: Deserialización y JSON peligroso
horas: 5.0
semana: 6
lectura: Deserialization + API hardening
evidencia: projects/m18-appsec/json-trust.md
---

# L23 — Deserialización y JSON peligroso

**~5.0 h · Semana 6**

`JSON.parse` de fuentes no confiables + prototipos / eval.

## Objetivo

Grep de `eval|deserialize|yaml.load` peligroso; endurece parsers.

## Pasos (hazlos en orden)

### 1. Caza (50 min)

### 2. Hardening (60–70 min)

Schema validation en boundaries. Hallazgo o clean bill.

### 3. Commit

`fix(m18): l23 json boundaries`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| OWASP Top 10 + Cheat Sheets | Deserialization + API hardening | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M18](../../../bibliografia.md#m18-seguridad-appsec) |


## Hecho cuando

Marca la lección **solo si**:

1. Lista endpoints + validación (artefacto: `projects/m18-appsec/json-trust.md`).
2. Límite tamaño body (artefacto: `projects/m18-appsec/json-trust.md`).
3. ≥1 mejora commitada (artefacto: `projects/m18-appsec/json-trust.md`).

## Errores comunes

- Aceptar cualquier JSON.
- Confiar en tipos TS solo compile-time.

## Siguiente

[L24 — Consolidar hallazgos semana 6 en P2](L24-consolidar-hallazgos-semana-6-en-p2.md)
