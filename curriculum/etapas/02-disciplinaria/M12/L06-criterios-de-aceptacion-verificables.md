---
id: L06
materia: M12
orden: 6
titulo: Criterios de aceptación verificables
horas: 5.0
semana: 2
lectura: Given/When/Then intro
evidencia: stories.md criterios
---

# L06 — Criterios de aceptación verificables

**~5.0 h · Semana 2**

Si no puedes convertirlo en test, no es criterio.

## Objetivo

Endurecer `stories.md` con aceptación verificable.

## Pasos

### 1. Reglas (20 min)

Cada criterio: sujeto observable + condición + resultado. Preferible Given/When/Then.

### 2. Reescribe (90–110 min)

Ejemplo:

```text
Given un owner autenticado
When crea una cita en un slot libre
Then la cita aparece en GET /api/citas?fecha=… con status 201 al crear
```

Incluye 401/403 donde aplique (aunque el RNF formal llegue en L08).

### 3. Revisión cruzada (30 min)

Marca en amarillo (comentario) criterios vagos y corrígelos.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l06 criterios aceptacion"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Criterios testeables; happy path + error; nada de “se ve bien” | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Cada story existente tiene ≥3 criterios verificables (Given/When/Then o lista numerada).
2. Al menos un criterio de error/permiso en 2 stories.
3. Commit `docs(m12): l06 criterios aceptacion`.

## Errores comunes

- “Que sea intuitivo”.
- Criterios solo de UI visual.
- Sin casos de error.

## Siguiente

[L07 — Historias de vacío, duplicados y conflicto](L07-historias-de-vacio-duplicados-y-conflicto.md)
