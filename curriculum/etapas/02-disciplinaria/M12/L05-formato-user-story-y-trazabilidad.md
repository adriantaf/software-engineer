---
id: L05
materia: M12
orden: 5
titulo: Formato user story y trazabilidad
horas: 5
semana: 2
lectura: "Plantilla + historias INVEST"
evidencia: "stories.md inicio"
---

# L05 — Formato user story y trazabilidad

**~5 h · Semana 2**

## Objetivo

Escribir primeras stories con rol, necesidad y beneficio; enlazar a problemas.md.

## Por qué importa

Stories son puente a tests en M15/M17.

## Conceptos

- INVEST.
- trazabilidad.
- rol.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

≥4 stories iniciales en `stories.md` con ID (US-01…).

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m12): l05 formato-user-story-y-trazabilidad"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Plantilla | req funcionales | — |
| Catálogo | Entrada M12 | [Bibliografía · M12](../../../bibliografia.md#m12-requerimientos) |


## Hecho cuando

1. ≥4 stories.
2. Enlace a problema.
3. IDs estables.

## Errores comunes

- Stories técnicas (“crear tabla”).
- Sin rol.

## Siguiente

[L06 — Criterios de aceptación verificables](L06-criterios-de-aceptacion-verificables.md)
