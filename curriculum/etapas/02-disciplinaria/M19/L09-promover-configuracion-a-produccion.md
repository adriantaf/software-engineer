---
id: L09
materia: M19
orden: 9
titulo: Promover configuración a producción
horas: 5.0
semana: 3
lectura: 12-factor config
evidencia: projects/m19-ops/ambientes.md actualizado
---

# L09 — Promover configuración a producción

**~5.0 h · Semana 3**

Prod ≠ staging con el mismo secret.

## Objetivo

Ambiente prod (o “prod-candidato”) con secretos y URL distintos documentados.

## Pasos (hazlos en orden)

### 1. Checklist promoción (40 min)

### 2. Configura prod (100–120 min)

Migraciones cuidadosas. Smoke mínimo.

### 3. Commit

`docs(m19): l09 promover produccion`

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| Docs Docker + PaaS/VPS elegido | 12-factor config | [Docker docs](https://docs.docker.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M19](../../../bibliografia.md#m19-nube-devops) |


## Hecho cuando

Marca la lección **solo si**:

1. Prod URL (artefacto: `projects/m19-ops/ambientes.md actualizado`).
2. Diff documentado (artefacto: `projects/m19-ops/ambientes.md actualizado`).
3. Datos separados (artefacto: `projects/m19-ops/ambientes.md actualizado`).
4. Commit `docs(m19): L09 promover-configuracion-a-produccion`.

## Errores comunes

- Migrar en prod primero.
- Misma DB staging/prod.

## Siguiente

[L10 — Logs, rollback y versión desplegada](L10-logs-rollback-y-version-desplegada.md)
