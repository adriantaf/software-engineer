---
id: L09
materia: M15
orden: 9
titulo: Workflow GitHub Actions — esqueleto
horas: 5.0
semana: 3
lectura: GitHub Actions basics; ci.yml
evidencia: .github/workflows/m15-ci.yml (o documentado) verde
---

# L09 — Workflow GitHub Actions — esqueleto

**~5.0 h · Semana 3**

P2: CI real. Hoy el esqueleto que falla si los tests fallan.

## Objetivo

`.github/workflows/` con job de test para M15.

## Pasos (hazlos en orden)

### 1. Escribe YAML (60–70 min)

```yaml
name: m15-ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: projects/m15-calidad
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: npm
          cache-dependency-path: projects/m15-calidad/package-lock.json
      - run: npm ci
      - run: npm test
```

Ajusta si aún no hay lockfile (`npm install`).

### 2. Documenta ruta (30 min)

### 3. Commit + push cuando puedas verificar

`ci(m15): workflow esqueleto github actions`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Workflow CI: checkout, node, npm test | [GitHub Actions — Quickstart](https://docs.github.com/es/actions/writing-workflows/quickstart) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Workflow YAML que corre en push/PR e instala deps + `npm test` en `projects/m15-calidad` (o monorepo doc).
2. README M15 enlaza al workflow / badge path.
3. Commit `ci(m15): workflow esqueleto github actions`.

## Errores comunes

- Workflow solo en docs sin YAML.
- `npm test` en raíz sin `working-directory`.
- Secrets pegados en el YAML.

## Siguiente

[L10 — Lint y formato en pipeline](L10-lint-y-formato-en-pipeline.md)
