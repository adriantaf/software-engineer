---
id: L08
materia: M17
orden: 8
titulo: Seeds demo y datos design partner
horas: 5.0
semana: 2
lectura: Fixtures reproducibles
evidencia: projects/m17-agenda-ops/scripts/seed.ts
---

# L08 — Seeds demo y datos design partner

**~5.0 h · Semana 2**

Demo reproducible > “en mi máquina hay datos”.

## Objetivo

`scripts/seed.ts` (o SQL) idempotente: negocio, owner, staff, citas ejemplo — sin PII real.

## Pasos (hazlos en orden)

### 1. Diseño seed (25 min)

Usuarios test `owner@agenda.test` / `staff@agenda.test` con passwords solo en `.env.example` como placeholders.

### 2. Script idempotente (80–100 min)

Correr dos veces no duplica. README: cómo seedear y limpiar.

### 3. Cierre semana 2 (30 min)

`docs/semana-02.md` + captura de `\dt` o conteos.

### 4. Commit

`feat(m17): l08 seeds demo design partner`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| MDN Web Docs + docs del framework elegido | Fixtures reproducibles | [MDN Web Docs (ES)](https://developer.mozilla.org/es/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M17](../../../bibliografia.md#m17-aplicaciones-web) |


## Hecho cuando

Marca la lección **solo si**:

1. Seed corre (artefacto: `projects/m17-agenda-ops/scripts/seed.ts`).
2. README creds test (artefacto: `projects/m17-agenda-ops/scripts/seed.ts`).
3. Cierre semana 2 (artefacto: `projects/m17-agenda-ops/scripts/seed.ts`).
4. Commit `docs(m17): L08 seeds-demo-y-datos-design-partner`.

## Errores comunes

- Datos reales en git.
- Seed no repetible.

## Siguiente

[L09 — Matriz de permisos owner y staff](L09-matriz-de-permisos-owner-y-staff.md)
