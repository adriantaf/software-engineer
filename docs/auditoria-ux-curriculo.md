# Auditoría UX/UI y completitud del plan

**Fecha:** 2026-10-27  
**Alcance:** `curriculum/`, `academia/`, `projects/`, `progress.json`  
**Informe interactivo:** canvas de auditoría en el run del agente

## Veredicto

| Área | Estado |
|------|--------|
| Currículo (lecciones/materias) | Casi completo — 27/27 módulos, 526 lecciones L01…Ln, evidencia + «Hecho cuando» |
| Revisión de emergencia / cram | No existe en el repo |
| UX/UI de `academia/` | Débil — shell DaisyUI genérico sin identidad |
| Evidencia en `projects/` | Mayormente scaffolds (1:1 con materias) |

El contenido lectivo está listo para estudiar. La app web no comunicaba marca ni composición de producto.

## Completitud

- 526 lecciones, 0 stubs, 0 gaps de numeración, 0 sin criterios de evidencia.
- M27 = 18 lecciones (patrón 4/sem pediría 20) — documentado como intencional.
- Exámenes de etapa presentes (formativos, breves).
- Labs: solo índice.

## Remediaciones en este PR

1. Links rotos a `hilos/seguridad.md` (M21/L10, M23/L05).
2. README de etapa básica actualizado.
3. Duración disciplinaria alineada a 12–14 meses en `catalog.json`.
4. Nota en ficha M27 sobre 18 lecciones.
5. Rediseño «Atelier técnico»: tokens, tipografía, home brand-first, des-cardificar docs, a11y, motion.

## Fuera de alcance

Modo cram, llenar `projects/` con evidencia real, exámenes interactivos, paridad horas catálogo↔lecciones, reescritura de lecciones.
