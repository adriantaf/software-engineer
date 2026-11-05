# Lecciones paso a paso (formato Duolingo)

**Todas las 27 materias** (526 lecciones) usan `formato: pasos` al estilo M01.

- **M01** curada a mano.
- **M02–M27** re-curadas con `npm run curate:lessons` (`academia/scripts/curate-lessons-m01-style.mjs`):
  - explicación propia (objetivo + por qué)
  - 2–3 ejemplos del contenido original
  - quizzes de dificultad creciente + retos de terminal
  - resumen con «Hecho cuando»
  - **última lección de cada materia** = proyecto de cierre con rúbrica (prácticas + proyecto de la ficha)
  - detalle largo / libros = lectura complementaria

Para regenerar: `cd academia && npm run curate:lessons` (no toca M01). Migrador legacy: `npm run migrate:lessons`.

## Frontmatter

```yaml
formato: pasos
xpLeccion: 80          # opcional
pasos:                 # 5–8
  - id: s1
    tipo: explicacion | ejemplo | quiz | codigo | terminal | proyecto | resumen
    titulo: …
    xp: 10
    # campos según tipo
```

Validación: `cd academia && npm run validate:lessons`.

## Tipos de paso

| Tipo | Avance |
|------|--------|
| `explicacion` / `ejemplo` / `resumen` | Botón **Entendido** |
| `quiz` | Opción múltiple, V/F o completar → **Comprobar** |
| `terminal` | Comando esperado (normalizado) |
| `codigo` | Tests JS en el navegador |
| `proyecto` | Rúbrica checklist (honor + evidencia en repo) |

## Progreso

Se guarda en `localStorage` (`academia-progress-v1`): `pasos`, `pasoActual`, `xp`, `racha`, `repaso`. Compatible con sync Firebase (merge OR de pasos, max XP).

## Lectura complementaria

El **body** Markdown de la lección (bajo el frontmatter) se muestra al final como lectura complementaria (libros, plantillas, checklists offline).
