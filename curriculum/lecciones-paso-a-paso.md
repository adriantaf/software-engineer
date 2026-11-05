# Lecciones paso a paso (formato Duolingo)

**Todas las 27 materias** (526 lecciones) usan `formato: pasos`.

- **M01** está curada a mano (explicaciones propias, quizzes y terminal pensados).
- **M02–M27** se migraron desde el Markdown legacy con `academia/scripts/migrate-lessons-to-pasos.mjs`: conservan el contenido original como lectura complementaria y generan 5–8 pasos interactivos (explicación, ejemplo, quizzes, terminal si había bash). Se pueden re-curar lección a lección sin cambiar el schema.

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
