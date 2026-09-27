---
id: L01
materia: M15
orden: 1
titulo: Entorno M15 y pirámide de tests
horas: 5.0
semana: 1
lectura: Pirámide de tests; Vitest setup Agenda Ops
evidencia: projects/m15-calidad/ + piramide.md + Vitest verde
---

# L01 — Entorno M15 y pirámide de tests

**~5.0 h · Semana 1**

Sin suite local, CI es teatro. Hoy levantas Vitest y decides la pirámide del piloto.

## Objetivo

`projects/m15-calidad/` ejecutable + `piramide.md` concreto.

## Por qué empieza así

M14 te dejó reglas/services; M15 los blindan. M17 heredará este pipeline.

## Pasos (hazlos en orden)

### 1. Scaffold (50–70 min)

```bash
cd projects/m15-calidad
npm init -y
npm install -D typescript vitest @types/node
# scripts.test = "vitest run"
```

Estructura:

```text
src/domain/
src/application/
tests/
piramide.md
```

Puedes reutilizar lógica de `projects/m14-patrones` (copia o path documentado).

### 2. Smoke test (30 min)

`tests/smoke.test.ts` assert `1+1` o import de un módulo dominio.

### 3. piramide.md (60–70 min)

| Capa | Ejemplos Agenda Ops | Cantidad relativa |
|------|---------------------|-------------------|
| Unit | solape, precio, DTO validate | mayoría |
| Integración | repo + Postgres test | media |
| HTTP/API | 401/403 crear cita | menos |
| E2E UI | 1–2 flujos | mínimo |

### 4. Commit

`docs(m15): entorno y piramide de tests`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Pirámide: muchos unit, menos integración, pocos E2E | [Vitest — Getting Started](https://vitest.dev/guide/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `projects/m15-calidad/` con Vitest y un test smoke verde.
2. `piramide.md` dibuja capas y qué irá en cada una para citas/auth.
3. Commit `docs(m15): entorno y piramide de tests`.

## Errores comunes

- Pirámide invertida (todo E2E).
- Proyecto sin script `test`.
- Copiar pirámide genérica sin mapear a Agenda Ops.

## Siguiente

[L02 — Tests unitarios puros de reglas de cita](L02-tests-unitarios-puros-de-reglas-de-cita.md)
