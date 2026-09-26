---
id: L15
materia: M14
orden: 15
titulo: Refactor P3 — módulo legacy antes y después
horas: 5
semana: 4
lectura: "Refactoring Fowler (intro)"
evidencia: "projects/m14-patrones/refactor-notas.md"
---

# L15 — Refactor P3 — módulo legacy antes y después

**~5 h · Semana 4**

## Objetivo

Refactorizar un módulo propio (spike previo o archivo `legacy-citas.ts`) sin cambiar comportamiento observable.

## Por qué importa

P3 demuestra que entiendes patrones como herramienta, no decoración.

## Conceptos

- refactor seguro.
- tests antes.
- diff.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Tests de caracterización → refactor → mismos tests verdes. `refactor-notas.md` con antes/después.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m14): l15 refactor-p3-modulo-legacy-antes-y-despue"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Ficha | ../M14-patrones.md | P3 |
| Catálogo | Entrada M14 | [Bibliografía · M14](../../../bibliografia.md#m14-patrones) |


## Hecho cuando

1. refactor-notas.md.
2. Tests verdes antes/después.
3. Diff o commits.

## Errores comunes

- Refactor sin tests.
- Cambiar comportamiento silencioso.

## Siguiente

[L16 — Cierre M14 — cinco patrones e integración M17](L16-cierre-m14-cinco-patrones-e-integracion-m17.md)
