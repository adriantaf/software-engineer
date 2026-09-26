---
id: L06
materia: M01
orden: 6
titulo: Commits atómicos y mensajes
horas: 2.5
semana: 2
lectura: "Pro Git cap. 2 (secciones de commit) + convención qué/porqué"
evidencia: "Cadena de commits atómicos en marcha (meta P2: 7 días)"
---

# L06 — Commits atómicos y mensajes

**~2.5 h · Semana 2**

Un commit atómico = **una** idea revisable. El mensaje dice **qué** cambió y **por qué** importa.

## Objetivo

Escribir mensajes claros y partir el trabajo en commits pequeños. Empezar (o continuar) la racha de **7 días** de la P2.

## Bueno vs malo

```text
malo:  update
malo:  cambios
malo:  fix
bueno: docs(m01): añadir bitácora de la semana 0001
bueno: chore(m01): aliases de git en .bashrc
bueno: docs(m01): anotar pipeline grep en shell-notas
```

Patrón útil: `tipo(ambito): resumen en imperativo`

Tipos comunes aquí: `docs`, `chore`, `feat`, `fix`.

## Pasos

### 1. Audita tu historial reciente (20 min)

```bash
git log -10 --oneline
```

Marca mentalmente cuáles mensajes no te servirían en 3 meses. Reescribe la regla en `git-notas.md`.

### 2. Practica el split (40–50 min)

Haz **dos** cambios distintos (ej. una línea en bitácora + una línea en `git-notas.md`) y **dos** commits separados:

```bash
git add projects/m01-diario/semana-0001.md
git commit -m "docs(m01): actualizar bitácora semana 0001"

git add projects/m01-diario/git-notas.md
git commit -m "docs(m01): aclarar regla de mensajes de commit"
```

Si ya los mezclaste en staging: `git restore --staged <archivo>` y vuelve a añadir por partes.

### 3. Arranca o continúa P2 (45–60 min)

**P2:** 7 días con ≥1 commit atómico/día (mensajes qué/porqué).

- Hoy cuenta como un día si haces un commit real de progreso.
- Pega en la bitácora (cuando cierres la semana): salida de `git log --oneline` relevante.

No inventes commits vacíos (`git commit --allow-empty`) para “cumplir”: el plan pide honestidad.

### 4. Checklist de mensaje (10 min)

Antes de cada `commit`, pregúntate:

1. ¿Qué archivo(s) toca?
2. ¿Por qué alguien del futuro debería importarle?
3. ¿Se puede revisar en <5 minutos?

## Lectura

Repasa en *Pro Git* cap. 2 las secciones de registrar cambios / historial. No avances al cap. 3 todavía si no terminaste esta práctica.

## Hecho cuando

1. Hiciste al menos 2 commits separados con mensajes claros en esta sesión.
2. Entiendes la meta de P2 (7 días) y ya tienes al menos el día de hoy (o documentaste el plan de racha).
3. Actualizaste `git-notas.md` con la regla qué/porqué.

## Errores comunes

- Un solo commit gigante “toda la semana M01”.
- Mensajes que describen el mood (`wip`, `tmp`) sin contenido.
- Marcar P2 en la UI sin los 7 días.

## Siguiente

[L07 — Ramas, merge y stash](L07-ramas-merge-y-stash.md)
