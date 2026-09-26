---
id: L04
materia: M21
orden: 4
titulo: Backlog refinado y criterios de aceptación
horas: 5
semana: 1
lectura: "Scrum Guide — refinamiento del Product Backlog"
evidencia: "projects/m21-proyectos/roadmap-trimestre.md sección backlog"
---

# L04 — Backlog refinado y criterios de aceptación

**~5 h · Semana 1**

## Objetivo

Refinar las historias del backlog: criterios de aceptación testeables y tamaño ≤ un sprint para las top 5.

## Por qué importa

Cierras semana 1 con P1 casi listo: el roadmap debe ser ejecutable, no aspiracional.

## Conceptos

- Historia de usuario.
- Criterio Given/When/Then.
- INVEST (selecto).
- Deuda etiquetada.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

Para las **5 issues** prioritarias añade en el issue (o anexo `projects/m21-proyectos/backlog-refinado.md`) criterios de aceptación numerados.

Verifica que cada criterio sea **observable** (URL, test, archivo). Etiqueta deuda técnica explícita.

Retro semana 1 en `bitacora-m21.md`: estimación inicial en rangos (optimista/realista/pesimista) para la issue #1.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l04 backlog-refinado-y-criterios-de-aceptaci"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Scrum Guide | Refinamiento | Ficha M21 semana 1 |
| Catálogo | Entrada M21 | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

1. 5 historias con criterios.
2. Retro semana 1 escrita.
3. P1 roadmap revisable.

## Errores comunes

- Criterios ‘funciona bien’.
- Historias gigantes multi-sprint sin split.

## Siguiente

[L05 — Sprint planning — meta única del sprint 1](L05-sprint-planning-meta-unica-del-sprint-1.md)
