---
id: L11
materia: M21
orden: 11
titulo: Tablero vivo, sprints 3–4 y DoD en práctica
horas: 5
semana: 3
lectura: "Scrum Guide — transparencia del incremento"
evidencia: "projects/m21-proyectos/sprints/sprint-03.md + sprint-04.md"
---

# L11 — Tablero vivo, sprints 3–4 y DoD en práctica

**~5 h · Semana 3**

## Objetivo

Actualizar board.md, esbozar sprints 3–4 y cerrar ≥3 issues con DoD completa.

## Por qué importa

El proyecto de la materia es un tablero que refleja la realidad del SaaS, no un ejercicio.

## Conceptos

- Transparencia.
- Issues zombie.
- Handoff M22.
- Incremento demoable.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Actualiza `projects/m21-proyectos/board.md` (fecha ≤7 días).

Crea `projects/m21-proyectos/sprints/sprint-03.md` y `sprint-04.md` con meta y al menos encabezado de tabla (pueden solapar semanas calendario si ya iterabas).

Añade al backlog issues etiquetados **demo-comercial** para M22. Cierra ≥3 issues con DoD.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l11 tablero-vivo-sprints-3-4-y-dod-en-practi"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M22-emprendimiento.md | ../../../producto-saas.md |

## Hecho cuando

1. board.md reciente.
2. sprint-03/04 existen.
3. ≥3 issues con DoD.
4. Issues demo M22.

## Errores comunes

- Board sin URL.
- Sprints sin fechas ni meta.

## Siguiente

[L12 — Cierre M21 — P1–P3, dominio y handoff comercial](L12-cierre-m21-p1-p3-dominio-y-handoff-comercial.md)
