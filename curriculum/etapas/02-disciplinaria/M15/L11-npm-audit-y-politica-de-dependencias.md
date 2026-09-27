---
id: L11
materia: M15
orden: 11
titulo: npm audit y política de dependencias
horas: 5.0
semana: 3
lectura: npm audit; política high/critical
evidencia: audit en CI + docs/politica-deps.md
---

# L11 — npm audit y política de dependencias

**~5.0 h · Semana 3**

El piloto también tiene supply chain. Hoy el audit deja de ser opcional.

## Objetivo

Audit en pipeline + política escrita (P2 completo con lint+test+audit).

## Pasos (hazlos en orden)

### 1. Corre audit local (30 min)

### 2. Añade a CI (40 min)

### 3. política-deps.md (50 min)

### 4. Commit

`ci(m15): npm audit y politica deps`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Audit en CI; excepciones con ticket/motivo | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `npm audit --audit-level=high` (o equivalente) en workflow o script CI.
2. `docs/politica-deps.md` describe qué hacer con vulns y excepciones.
3. Commit `ci(m15): npm audit y politica deps`.

## Errores comunes

- `--audit-level=critical` sin mirar high.
- Silenciar audit con flag oculto permanente.
- No pinear versiones y vivir en builds flaky.

## Siguiente

[L12 — Badge README y artefacto de test](L12-badge-readme-y-artefacto-de-test.md)
