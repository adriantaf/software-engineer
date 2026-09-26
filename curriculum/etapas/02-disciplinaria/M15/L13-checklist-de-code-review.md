---
id: L13
materia: M15
orden: 13
titulo: Checklist de code review
horas: 5.0
semana: 4
lectura: "Checklist review: calidad + seguridad"
evidencia: checklist-review.md (P3)
---

# L13 — Checklist de code review

**~5.0 h · Semana 4**

P3 empieza aquí: lo que mirarás en cada PR del piloto.

## Objetivo

`projects/m15-calidad/checklist-review.md` usable.

## Pasos (hazlos en orden)

### 1. Borrador por secciones (70–90 min)

Estilo · Tests · Authz · Validación · Migraciones · Secrets · Observabilidad mínima.

### 2. Alinea a M13 boundaries (30 min)

### 3. Commit

`docs(m15): checklist de code review`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Código limpio* (pruebas) + Vitest docs | Checklist PR: tests, auth, secrets, migraciones | [Vitest](https://vitest.dev/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M15](../../../bibliografia.md#m15-v-v-y-calidad) |


## Hecho cuando

Marca la lección **solo si**:

1. `checklist-review.md` con ítems de estilo, tests, seguridad (auth/IDOR/validación), secrets.
2. Ítems accionables (sí/no), no vagos.
3. Commit `docs(m15): checklist de code review`.

## Errores comunes

- Lista de 80 ítems inusable.
- Cero ítems de seguridad.
- Copiar checklist enterprise sin adaptar al piloto.

## Siguiente

[L14 — Review simulado en PR o notas](L14-review-simulado-en-pr-o-notas.md)
