---
id: L07
materia: M21
orden: 7
titulo: Estimación en rangos y métricas de flujo
horas: 5
semana: 2
lectura: "Notas lean/kanban — throughput y carry-over"
evidencia: "projects/m21-proyectos/metricas-flujo.md"
---

# L07 — Estimación en rangos y métricas de flujo

**~5 h · Semana 2**

## Objetivo

Documentar estimaciones en tres rangos y calcular throughput simple (issues cerrados/semana) y carry-over.

## Por qué importa

Sin métricas de flujo repites el mismo error de estimación en M22 (demos) y M26 (capstone).

## Conceptos

- Optimista/realista/pesimista.
- Throughput.
- Lead time (idea).
- Carry-over.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Crea `projects/m21-proyectos/metricas-flujo.md` con definiciones y **números reales** del sprint 1.

Tabla: issue, estimación (3 columnas), horas reales si las tienes, estado.

Calcula: issues cerrados esta semana / issues arrastrados. Una frase: qué cambiarás en sprint 2.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l07 estimacion-en-rangos-y-metricas-de-flujo"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M21-admin-proyectos.md | Scrum Guide DoD |
| Catálogo | Entrada M21 | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

1. metricas-flujo.md con números.
2. Rangos en ≥3 issues.
3. Acción para sprint 2.

## Errores comunes

- Solo horas planeadas sin real.
- Vanity ‘100% productividad’.

## Siguiente

[L08 — Sprint 2 documentado y avance P2](L08-sprint-2-documentado-y-avance-p2.md)
