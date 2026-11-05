# Lecciones paso a paso (formato Duolingo)

Piloto: **M01**. Otras materias siguen el formato legacy (Markdown + “Hecho cuando”) hasta migrarlas.

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
