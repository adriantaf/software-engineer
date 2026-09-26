---
id: L01
materia: M21
orden: 1
titulo: Entorno M21, Scrum de uno y Definition of Done
horas: 5
semana: 1
lectura: "Guía Scrum 2020 (ES) — roles y eventos"
evidencia: "projects/m21-proyectos/definition-of-done.md"
---

# L01 — Entorno M21, Scrum de uno y Definition of Done

**~5 h · Semana 1**

## Objetivo

Crear la carpeta de evidencia, leer Scrum adaptado a un solo dev-owner y redactar Definition of Done usable en issues reales de Agenda Ops.

## Por qué importa

Sin DoD escrito cierras issues con ‘ya quedó’; M22 y M26 dependen de un backlog honesto del mismo repo producto.

## Conceptos

- Product Owner de uno.
- Sprint de 1–2 semanas.
- DoD con PR, test, doc.
- Backlog ≠ lista de deseos.

## Pasos (hazlos en orden)

### 1. Lectura dirigida (60–90 min)

Lee la sección indicada en la ficha de la materia y subraya solo lo que vas a **probar** hoy en terminal o en `projects/`.

### 2. Carpeta de evidencia (15–20 min)

Crea o actualiza la carpeta del proyecto de la materia. Cada lección añade una sección en la bitácora semanal o un archivo dedicado; no disperses notas sueltas.

### 3. Laboratorio / trabajo documental (90–120 min)

```bash
mkdir -p projects/m21-proyectos/sprints
```

Lee la [Guía Scrum 2020 (ES)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf) completa una vez.

En `projects/m21-proyectos/definition-of-done.md` define checklist mínima: PR revisado (o self-review documentado), tests/CI cuando aplique, doc en `projects/` si la materia lo pide, staging si es deploy. Incluye **un ítem de seguridad** (ej. no secretos en git).

Añade `projects/m21-proyectos/bitacora-m21.md` con párrafo: cómo mapeas roles Scrum cuando eres solo tú + mentor ocasional.

### 4. Conexión con el plan (30–45 min)

Escribe un párrafo en la bitácora: cómo lo de hoy afecta al piloto **Agenda Ops** (M12 en adelante) o a la API que desplegarás en M17/M19. Si aún no tienes SRS, usa el escenario del [producto del plan](../../../producto-saas.md) (citas, clientes, panel).

### 5. Commit atómico (15 min)

```bash
git add projects/
git status
git commit -m "docs(m21): l01 entorno-m21-scrum-de-uno-y-definition-of"
```

## Lectura de esta lección

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| Scrum Guide | 2020 ES PDF | ../../../como-estudiar.md |
| Plan | ../../../producto-saas.md | ../../hilos/seguridad.md |
| Catálogo | Entrada M21 | [Bibliografía · M21](../../../bibliografia.md#m21-admin-proyectos) |


## Hecho cuando

1. DoD ≥6 ítems verificables.
2. bitacora-m21.md con roles adaptados.
3. Commit docs(m21).

## Errores comunes

- DoD genérico ‘código limpio’.
- Ignorar ítem seguridad.

## Siguiente

[L02 — Milestones y cinco issues reales del producto](L02-milestones-y-cinco-issues-reales-del-producto.md)
