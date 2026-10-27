---
id: L02
materia: M12
orden: 2
titulo: Entrevista y notas timestamp
horas: 5.0
semana: 1
lectura: Técnicas elicitación (plantilla + tu guion)
evidencia: entrevistas/notas-YYYY-MM-DD.md
---

# L02 — Entrevista y notas timestamp

**~5.0 h · Semana 1**

P1 exige evidencia de entrevista. Hoy la corres y dejas notas auditables.

## Objetivo

Completar una sesión con notas timestamp en `entrevistas/`.

## Pasos

### 1. Prep (20 min)

Imprime o ten abierto `guion-v1.md`. Acuerda duración (~45 min). Si es simulación: briefing escrito del personaje (dueño de X).

### 2. Sesión (45–60 min)

Formato de notas:

```markdown
# Entrevista — 2026-09-26 — Partner A
## 00:00–00:05 Rapport
…
## 00:05–00:20 Flujo actual
> pedido textual breve
Interpretación: …
```

### 3. Debrief (45 min)

Al final del archivo: insights, dolores rankeados, datos sensibles mencionados, contradicciones, follow-ups.

### 4. Commit (15 min)

```bash
git add projects/m12-srs/entrevistas
git commit -m "docs(m12): l02 notas entrevista"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| IEEE 830 adaptada (repo) | Notas con timestamp; separar pedido textual vs interpretación | [plantilla SRS](../../../../projects/m12-srs/plantilla.md) |
| Catálogo | Entrada de esta materia | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

Marca la lección **solo si**:

1. Archivo `entrevistas/notas-YYYY-MM-DD.md` con ≥30 min de sesión (real o roleplay serio).
2. Cada bloque marca tiempo + texto; al final: 5 insights y 5 preguntas abiertas.
3. Commit `docs(m12): l02 notas entrevista`.

## Errores comunes

- Notas que solo dicen “quiere una app”.
- Mezclar lo que dijo con lo que tú inventaste.
- Grabar sin consentimiento si es persona real.

## Siguiente

[L03 — Problemas observados y glosario](L03-problemas-observados-y-glosario.md)
