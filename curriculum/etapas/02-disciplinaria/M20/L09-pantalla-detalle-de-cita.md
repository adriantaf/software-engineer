---
id: L09
materia: M20
orden: 9
titulo: Pantalla detalle de cita
horas: 5
semana: 3
lectura: "Navigation params"
evidencia: "commit pantalla detalle"
---

# L09 — Pantalla detalle de cita

**~5 h · Semana 3**

## Objetivo

Navegar a detalle con id; mostrar campos completos de la cita.

## Por qué importa

Lista sin detalle no sirve al dueño en campo.

## Conceptos

- route args
- fetch by id

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Deep link interno navigator.push con id.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m20): l09 pantalla-detalle-de-cita"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| API | GET cita/:id | — |
| Catálogo | Entrada M20 | [Bibliografía · M20](../../../bibliografia.md#m20-aplicaciones-moviles) |


## Hecho cuando

1. Detalle coincide API
2. Loading en detalle
3. Commit

## Errores comunes

- Detalle mock
- IDOR no manejado

## Siguiente

[L10 — Navegación: tabs o drawer mínimo](L10-navegacion-tabs-o-drawer-minimo.md)
