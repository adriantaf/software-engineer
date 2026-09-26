---
id: L03
materia: M15
orden: 3
titulo: Qué no testear y carpetas de coverage
horas: 5.0
semana: 1
lectura: Coverage útil; exclusiones conscientes
evidencia: vitest coverage en domain/ + docs/no-testear.md
---

# L03 — Qué no testear y carpetas de coverage

**~5.0 h · Semana 1**

Coverage es brújula, no religión. Hoy apuntas el medidor al dominio.

## Objetivo

Config de coverage + política escrita.

## Pasos (hazlos en orden)

### 1. Instala provider (30 min)

`npm i -D @vitest/coverage-v8` y script `test:cov`.

### 2. include domain (40 min)

### 3. no-testear.md (50 min)

Ejemplos: wrappers del framework, generados, `main.ts` de boot.

### 4. Commit

`test(m15): coverage dominio y politica no-testear`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | No perseguir 100% en boilerplate; coverage en domain/ | [Vitest — Coverage](https://vitest.dev/guide/coverage.html) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Coverage configurado enfocando `src/domain/**` (o carpeta equivalente).
2. `docs/no-testear.md` lista ≥3 cosas que no testearás (ORM glue, framework).
3. Commit `test(m15): coverage dominio y politica no-testear`.

## Errores comunes

- 100% en DTOs vacíos y 0% en solape.
- Excluir `domain/` “porque es difícil”.
- Subir reportes HTML enormes al repo sin necesidad.

## Siguiente

[L04 — Cierre semana 1 — suite dominio y bitácora](L04-cierre-semana-1-suite-dominio-y-bitacora.md)
