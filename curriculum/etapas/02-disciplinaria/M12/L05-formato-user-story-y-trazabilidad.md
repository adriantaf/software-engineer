---
id: L05
materia: M12
orden: 5
titulo: Formato user story y trazabilidad
horas: 5.0
semana: 2
lectura: Plantilla + historias INVEST
evidencia: stories.md inicio
---

# L05 — Formato user story y trazabilidad

**~5.0 h · Semana 2**

Las stories son el puente entrevista → SRS → tests (M15/M17).

## Objetivo

Arrancar `stories.md` con historias trazables.

## Pasos

### 1. Plantilla de story (30 min)

```markdown
## US-01 — …
**Como** owner **quiero** … **para** …
**Problema:** P-01
**Prioridad:** (luego MoSCoW)
```

### 2. Escribe ≥4 (90 min)

Cobertura mínima: agendar cita, ver agenda del día, alta de cliente, cancelar/reagendar. Lenguaje del glosario.

### 3. Mapa (30 min)

Tabla `US-xx → P-xx → sección SRS futura`.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/stories.md
git commit -m "docs(m12): l05 user stories base"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Como/quiero/para; INVEST; trazabilidad story→problema→SRS | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `stories.md` con ≥4 stories en formato estándar + ID (US-01…).
2. Cada story enlaza a un problema P-xx o insight de entrevista.
3. Commit `docs(m12): l05 user stories base`.

## Errores comunes

- Stories técnicas (“como desarrollador quiero Postgres”).
- Sin ID ni trazabilidad.
- Épicas enormes sin partir.

## Siguiente

[L06 — Criterios de aceptación verificables](L06-criterios-de-aceptacion-verificables.md)
