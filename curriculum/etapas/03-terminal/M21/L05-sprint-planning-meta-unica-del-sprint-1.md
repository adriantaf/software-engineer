---
id: L05
materia: M21
orden: 5
titulo: Sprint planning — meta única del sprint 1
horas: 5
semana: 2
lectura: "Scrum Guide — Sprint Planning"
evidencia: "projects/m21-proyectos/sprints/sprint-01.md"
---

# L05 — Sprint planning — meta única del sprint 1

**~5 h · Semana 2**

## Objetivo

Planificar sprint 1 con **una meta** clara, WIP limitado y lista de entregables enlazados a issues.

## Por qué importa

Multi-tasking sin meta única es la causa #1 de carry-over; M21 te entrena a decir no.

## Conceptos

- Meta de sprint.
- WIP.
- Compromiso realista.
- Definition of Done aplicada.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m21-proyectos/sprints/sprint-01.md` con plantilla de la ficha (fechas, meta, tabla Planeado/Hecho/Aprendizaje vacía).

Elige **1 meta** (ej. ‘segundo tenant en staging + 1 test cross-tenant’). Máximo **3 issues** en progreso.

Documenta estimación **24–32 h** (rango) y riesgos del sprint (1 párrafo).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l05 sprint-planning-meta-unica-del-sprint-1"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Scrum Guide | Sprint Planning | DoD local |
| Catálogo | Entrada M21 | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

1. sprint-01.md con meta única.
2. ≤3 issues WIP.
3. Rango horas documentado.

## Errores comunes

- Meta lista de 10 verbos.
- Sin fechas de sprint.

## Siguiente

[L06 — Ejecutar sprint 1 y registro honesto](L06-ejecutar-sprint-1-y-registro-honesto.md)
