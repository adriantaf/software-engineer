---
id: L10
materia: M15
orden: 10
titulo: Lint y formato en pipeline
horas: 5.0
semana: 3
lectura: ESLint/Prettier o oxlint; fail on lint
evidencia: script lint en CI
---

# L10 — Lint y formato en pipeline

**~5.0 h · Semana 3**

CI sin lint deja pasar basura que los tests no ven.

## Objetivo

Lint (y opcional format check) en local + Actions.

## Pasos (hazlos en orden)

### 1. Config ESLint o equivalente (60–70 min)

### 2. Añade step al workflow (30 min)

### 3. Commit

`ci(m15): lint en pipeline`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Lint en CI: mismo estándar local y remoto | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Script `npm run lint` local verde.
2. Paso de lint en el workflow (falla el job si lint falla).
3. Commit `ci(m15): lint en pipeline`.

## Errores comunes

- Lint solo warning ignorado.
- Reglas tan estrictas que nadie corre local.
- Formatear en CI sin config en repo.

## Siguiente

[L11 — npm audit y política de dependencias](L11-npm-audit-y-politica-de-dependencias.md)
