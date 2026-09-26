---
id: L14
materia: M19
orden: 14
titulo: Prueba de restore en entorno aislado
horas: 5.0
semana: 4
lectura: Restore docs
evidencia: projects/m19-ops/restore-test.md
---

# L14 — Prueba de restore en entorno aislado

**~5.0 h · Semana 4**

P3: restore real documentado.

## Objetivo

`restore-test.md` con fecha, tamaño dump, tiempo, resultado.

## Pasos (hazlos en orden)

### 1. Entorno aislado (40 min)

DB temporal/local.

### 2. Restore (80–100 min)

`pg_restore` / pipe. Verifica conteo citas seed.

### 3. Registra (20 min)

### 4. Commit

`docs(m19): l14 restore test p3`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | Restore docs | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Restore real documentado (artefacto: `projects/m19-ops/restore-test.md`).
2. Verificación datos (artefacto: `projects/m19-ops/restore-test.md`).
3. Fecha (artefacto: `projects/m19-ops/restore-test.md`).
4. Commit `docs(m19): L14 prueba-de-restore-en-entorno-aislado`.

## Errores comunes

- Solo teoría.
- Restore sobre prod.

## Siguiente

[L15 — Runbook completo de producción](L15-runbook-completo-de-produccion.md)
