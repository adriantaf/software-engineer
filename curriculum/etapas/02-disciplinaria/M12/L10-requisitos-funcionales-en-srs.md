---
id: L10
materia: M12
orden: 10
titulo: Requisitos funcionales en SRS
horas: 5.0
semana: 3
lectura: plantilla.md — requisitos funcionales
evidencia: srs-borrador.md funcionales
---

# L10 — Requisitos funcionales en SRS

**~5.0 h · Semana 3**

El SRS habla RF-xx; las stories alimentan pero no sustituyen.

## Objetivo

Completar §3.1 Requisitos funcionales del borrador.

## Pasos

### 1. Deriva RF (90–110 min)

| ID | Descripción | Prioridad | Criterio / US |
|----|-------------|-----------|---------------|
| RF-01 | Owner autenticado gestiona clientes | Alta | US-0x |

Cubre clientes, pedidos, agenda, auth, roles básicos.

### 2. Fuera de alcance (30 min)

§4 con bullets concretos (no “todo lo demás”).

### 3. Commit (15 min)

```bash
git add projects/m12-srs/srs-borrador.md
git commit -m "docs(m12): l10 requisitos funcionales"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | RF-xx con prioridad y criterio; trazabilidad a US | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla §3.1 con ≥8 RF derivados de Must/Should.
2. Cada RF tiene criterio de aceptación o enlace a US.
3. Commit `docs(m12): l10 requisitos funcionales`.

## Errores comunes

- Copiar stories verbatim sin IDs RF.
- RF sin prioridad.
- Mezclar RNF en la tabla funcional.

## Siguiente

[L11 — SRS v1, freeze y P3](L11-srs-v1-freeze-y-p3.md)
