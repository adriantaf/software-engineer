---
id: L14
materia: M13
orden: 14
titulo: ADR persistencia y modelo de datos
horas: 5.0
semana: 4
lectura: Elección Postgres + acceso a datos; modelo MVP
evidencia: adr/002-persistencia.md
---

# L14 — ADR persistencia y modelo de datos

**~5.0 h · Semana 4**

Agenda Ops vive de consultas de agenda y FKs. Hoy firmas cómo persistir.

## Objetivo

`adr/002-persistencia.md` alineado a M09 y al diagrama de clases.

## Pasos (hazlos en orden)

### 1. Escribe el ADR (90–110 min)

```markdown
# ADR 002 — PostgreSQL + migraciones versionadas

## Contexto
Citas con rangos de tiempo, FKs, reportes simples, posible tenant_id luego.

## Decisión
PostgreSQL; migraciones SQL (o Prisma migrate — elige una) en repo.

## Consecuencias
+ Constraints e índices reales
+ Coincide con M09
− Ops de backups (M19)
```

Incluye acceso: Repository en infra (M14), no SQL en controllers.

### 2. Actualiza índice ADR (15 min)

### 3. Commit (15 min)

```bash
git add projects/m13-diseno/adr
git commit -m "docs(m13): ADR 002 persistencia"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *UML y patrones* — Larman (ed. ES) | Decisión de persistencia: Postgres, migraciones, acceso | [C4 model (apoyo diagramas)](https://c4model.com/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M13](../../../bibliografia.md#m13-analisis-y-diseno) |


## Hecho cuando

Marca la lección **solo si**:

1. ADR 002 elige Postgres (o justifica excepción) y cómo migrarás (SQL files / herramienta).
2. Alternativas rechazadas (p. ej. Mongo “porque JSON”) con motivo.
3. Commit `docs(m13): ADR 002 persistencia`.

## Errores comunes

- Elegir DB por moda sin relación al reporte de citas.
- “Usaremos un ORM” sin decir cuál ni migración.
- Contradecir cardinalidades de L06 sin actualizar clases.

## Siguiente

[L15 — Extensibilidad tenant_id sin implementar](L15-extensibilidad-tenant-id-sin-implementar.md)
