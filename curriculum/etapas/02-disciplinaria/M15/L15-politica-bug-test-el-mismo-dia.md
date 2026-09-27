---
id: L15
materia: M15
orden: 15
titulo: Política bug → test el mismo día
horas: 5.0
semana: 4
lectura: Regresión inmediata; ejemplo real
evidencia: docs/bug-test-mismo-dia.md + test de regresión
---

# L15 — Política bug → test el mismo día

**~5.0 h · Semana 4**

Regla del plan: el bug no se cierra solo con el fix.

## Objetivo

Política + una regresión demostrable.

## Pasos (hazlos en orden)

### 1. Escribe la política (40 min)

### 2. Inyecta o usa un bug (60–80 min)

Red (test falla) → fix → green.

### 3. Commit

`test(m15): regresion bug mismo dia`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Todo bug encontrado genera test el mismo día | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. Política escrita en el repo.
2. Al menos un bug (real o inyectado) con test de regresión añadido el mismo día (documentado).
3. Commit `test(m15): regresion bug mismo dia`.

## Errores comunes

- Política sin ejemplo.
- Fix sin test.
- Test que no falla ante el bug.

## Siguiente

[L16 — Cierre M15 — pipeline, coverage dominio, dominio](L16-cierre-m15-pipeline-coverage-dominio-dominio.md)
