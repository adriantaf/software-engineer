---
id: L04
materia: M16
orden: 4
titulo: auditoria-v1 y cierre P1 heurísticas
horas: 5
semana: 1
lectura: "Ficha M16 P1"
evidencia: "projects/m16-ihc/heuristicas/auditoria-v1.md"
---

# L04 — auditoria-v1 y cierre P1 heurísticas

**~5 h · Semana 1**

## Objetivo

Consolidar auditoría v1 con ≥10 hallazgos, severidad y fix propuesto.

## Por qué importa

P1 alimenta iteración semana 3.

## Conceptos

- auditoría.
- prioridad.
- P1.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Promueve v0 → v1. README enlaza auditoria-v1.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m16): l04 auditoria-v1-y-cierre-p1-heuristicas"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M16-ihc.md | — |

## Hecho cuando

1. auditoria-v1.md.
2. ≥10 hallazgos.
3. P1 listo.

## Errores comunes

- Duplicar hallazgos.
- Sin fix propuesto.

## Siguiente

[L05 — Prototipo navegable y tareas del SRS](L05-prototipo-navegable-y-tareas-del-srs.md)
