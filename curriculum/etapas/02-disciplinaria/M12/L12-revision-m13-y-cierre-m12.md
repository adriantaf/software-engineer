---
id: L12
materia: M12
orden: 12
titulo: Revisión M13 y cierre M12
horas: 5.0
semana: 3
lectura: Ficha M12 + handoff diseño
evidencia: nota-handoff-m13.md
---

# L12 — Revisión M13 y cierre M12

**~5.0 h · Semana 3**

Dejas el testigo listo para diseño (Larman/UML en M13).

## Objetivo

Handoff explícito + cierre de evidencias.

## Pasos

### 1. Relectura SRS (40 min)

Lee `srs-v1.md` como si fueras M13: marca ambigüedades.

### 2. Handoff (75 min)

`nota-handoff-m13.md`:

- Entidades candidatas (Cliente, Servicio, Cita, Usuario…)
- Casos de uso Must
- Reglas de conflicto de horario
- Preguntas abiertas
- Riesgos (alcance, datos, auth)

### 3. Dominio (30 min)

Auto-check de la ficha: ¿puedes decir “no” con alternativa escrita? ¿3 RNF? ¿Must con criterios?

### 4. Commit (15 min)

```bash
git add projects/m12-srs
git commit -m "docs(m12): cierre handoff m13"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Handoff a análisis/diseño: entidades, casos de uso, riesgos | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. `nota-handoff-m13.md` lista entidades candidatas, 5 preguntas abiertas y riesgos.
2. README m12 con checklist P1–P3 y proyecto cerrados.
3. Commit `docs(m12): cierre handoff m13`.

## Errores comunes

- Handoff vacío “lee el SRS”.
- Reabrir alcance Must sin versión.
- No enlazar stories/SRS desde README.

## Siguiente

Cierra la [ficha M12](../M12-requerimientos.md). Siguiente: [M13 — Análisis y diseño](../M13-analisis-y-diseno.md).
