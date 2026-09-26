---
id: L07
materia: M12
orden: 7
titulo: Historias de vacío, duplicados y conflicto
horas: 5.0
semana: 2
lectura: Casos borde negocio citas
evidencia: stories.md ampliado
---

# L07 — Historias de vacío, duplicados y conflicto

**~5.0 h · Semana 2**

El piloto se rompe en los bordes. Hoy los conviertes en stories.

## Objetivo

Ampliar `stories.md` hacia ≥8 con casos de borde del dominio.

## Pasos

### 1. Brainstorm bordes (40 min)

Lista: agenda vacía, slot ocupado, cliente duplicado por teléfono, cancelación tardía, no-show, nota privada, staff sin permiso.

### 2. Escribe stories (90 min)

Cada una con criterios. Ejemplo conflicto:

```text
When intento crear cita que solapa servicio+recurso
Then API responde 409 y no persiste
```

### 3. Conteo P2 (20 min)

Cuenta stories con criterios; anota cuántas faltan para ≥8.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l07 stories borde"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Agenda vacía, cliente duplicado, conflicto de horario, no-show | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. ≥3 stories nuevas de borde (vacío/duplicado/conflicto/no-show).
2. Total de stories camino a ≥8 (completa faltantes si hace falta).
3. Commit `docs(m12): l07 stories borde`.

## Errores comunes

- Solo happy path.
- Conflicto de horario sin regla explícita.
- Duplicados de cliente sin criterio de match (teléfono/nombre).

## Siguiente

[L08 — RNF seguridad, privacidad y P2](L08-rnf-seguridad-privacidad-y-p2.md)
