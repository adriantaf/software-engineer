---
id: L06
materia: M21
orden: 6
titulo: Ejecutar sprint 1 y registro honesto
horas: 5
semana: 2
lectura: "Scrum Guide — Daily Scrum (adaptado a bitácora)"
evidencia: "projects/m21-proyectos/sprints/sprint-01.md tabla hecho"
---

# L06 — Ejecutar sprint 1 y registro honesto

**~5 h · Semana 2**

## Objetivo

Trabajar el sprint 1 sobre Agenda Ops y registrar **hecho real** vs planeado sin borrar desviaciones.

## Por qué importa

La retrospectiva útil exige datos honestos; inflar ‘hecho’ destruye P2.

## Conceptos

- Daily de 3 líneas.
- Bloqueo documentado.
- Carry-over explícito.
- Demo a ti mismo.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Durante el sprint, añade notas diarias de 3 líneas en `sprint-01.md` (ayer/hoy/bloqueo).

Al cerrar parcialmente la semana, llena la tabla **Planeado | Hecho | Aprendizaje** aunque falte trabajo.

Si subestimaste migración o deploy, escribe **horas reales** aproximadas.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l06 ejecutar-sprint-1-y-registro-honesto"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Scrum Guide | Daily + Review | ../../../como-estudiar.md |

## Hecho cuando

1. Tabla parcialmente llena.
2. ≥3 notas diarias.
3. Desviación explicada.

## Errores comunes

- Borrar filas ‘no hecho’.
- Cerrar issues sin DoD.

## Siguiente

[L07 — Estimación en rangos y métricas de flujo](L07-estimacion-en-rangos-y-metricas-de-flujo.md)
