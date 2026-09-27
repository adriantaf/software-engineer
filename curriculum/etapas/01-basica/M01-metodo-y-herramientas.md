---
id: M01
titulo: Método, Git, Linux y documentación
etapa: basica
orden: 1
semanas: 2
horas: 40
practicas:
  - id: p1
    titulo: Configurar entorno Linux/WSL y aliases útiles
  - id: p2
    titulo: Repo con historial limpio (commits atómicos 7 días)
  - id: p3
    titulo: Escribir ADR corto de una decisión técnica
proyecto:
  id: proj
  titulo: Diario de ingeniería (este repo vivo)
---

# M01 — Método, Git, Linux y documentación

## Por qué existe

Sin método, 20 h/semana se diluyen en tutoriales. Esta materia instala el sistema de trabajo de todo el plan: terminal, Git limpio y bitácora.

**En resumen:** configuras tu entorno, practicas shell y Git en **este** repo, escribes un ADR corto y dejas bitácora. No es un curso de Git de 8 horas: es hábito.

## Objetivos de aprendizaje

Al terminar debes poder:

1. Organizar una semana de estudio (teoría / práctica / proyecto).
2. Usar la terminal con soltura (navegación, pipes, permisos, grep).
3. Hacer commits atómicos, ramas y PRs claros.
4. Documentar decisiones (ADR) y leer documentación oficial.

## Cómo estudiar esta materia (lecciones)

M01 usa el formato de lecciones tipo freeCodeCamp: lecciones cortas y completas que marcas una a una.

1. Abre las lecciones **en orden** (L01 → L08).
2. Cada lección trae objetivo, pasos, lectura de libro y criterio “Hecho cuando”.
3. Marca la lección en la UI solo si cumple ese criterio.
4. Las **prácticas / proyecto** de abajo siguen exigiendo evidencia en `projects/`.
5. Método general: [Cómo estudiar](../../como-estudiar.md).

## Semana tipo (20 h)

| Bloque | Horas | Qué haces |
|--------|-------|-----------|
| Método + shell | 6–8 | L01–L04, docs, bitácora |
| Git en este repo | 6–8 | L05–L07, commits atómicos, ramas |
| Proyecto diario | 4–6 | `projects/m01-diario/` + ADR (L08) |
| Retro | 1 | Qué bloqueó / qué sigue |

Si un día solo tienes 2 h: **una lección práctica** (pasos + evidencia). No saltes la fila de lectura de esa lección.

## Lecciones

### Semana 1 — Método + Linux (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L01 | [Entorno y primer commit](M01/L01-entorno-y-primer-commit.md) | 2.5 |
| L02 | [Método y práctica deliberada](M01/L02-metodo-y-practica-deliberada.md) | 2 |
| L03 | [Shell: navegación y archivos](M01/L03-shell-navegacion-y-archivos.md) | 3 |
| L04 | [Shell: pipes, permisos y docs](M01/L04-shell-pipes-permisos-y-docs.md) | 3 |

### Semana 2 — Git + escritura técnica (~20 h)

| ID | Lección | ~h |
|----|---------|----|
| L05 | [Git fundamentos](M01/L05-git-fundamentos.md) | 3 |
| L06 | [Commits atómicos y mensajes](M01/L06-commits-atomicos-y-mensajes.md) | 2.5 |
| L07 | [Ramas, merge y stash](M01/L07-ramas-merge-y-stash.md) | 3 |
| L08 | [ADR, bitácora y cierre](M01/L08-adr-bitacora-y-cierre.md) | 3 |

Empieza por **L01** hoy.

## Lecturas (mapa rápido)

Canon: [*Pro Git*](https://git-scm.com/book/es/v2) (Chacon & Straub). Catálogo: [bibliografía](../../bibliografia.md#m01-metodo-git).

| Semana | Lecciones | Capítulos / foco |
|--------|-----------|------------------|
| 1 | L01–L04 | Cap. 1 + man/`--help` + [Cómo estudiar](../../como-estudiar.md) |
| 2 | L05–L08 | Caps. 2–3 (fundamentos y ramas) — ejemplos en este repo |

**Regla:** no leas más allá del cap. 3 en M01. Servidor remoto (cap. 4) llega cuando uses GitHub con remoto.

## Prácticas

1. **P1:** Entorno listo: Node LTS, Git, editor, carpeta `~/dev`. Lista de versiones en `projects/m01-diario/entorno.md`.
2. **P2:** 7 días de commits atómicos en este repo (o diario). Nada de “update stuff”.
3. **P3:** Un ADR: “Por qué TypeScript como lenguaje principal del plan”.

## Proyecto útil

**Diario de ingeniería:** usa este mismo repositorio. Cada semana:

- Actualiza `progress.json`.
- Añade nota en `projects/m01-diario/semana-NNNN.md` (qué estudiaste, qué bloqueó, qué sigue).

## Errores comunes

- Instalar 15 herramientas en L01 y no hacer ningún commit.
- Usar solo la GUI de GitHub Desktop sin entender `status`/`diff`.
- Commits gigantes (“todo el portafolio”) que no se pueden revisar.
- Marcar lecciones sin cumplir “Hecho cuando”.

## Evidencia de hecho

Marca la práctica en la UI solo si existe **esto** (o equivalente claro):

- **P1 — Entorno:** `projects/m01-diario/entorno.md` con SO, Git, Node; commit `docs(m01): registrar entorno`.
- **P2 — Commits:** ≥7 commits atómicos en 7 días (mensajes qué/porqué); `git log --oneline` pegado en la bitácora.
- **P3 — ADR:** `projects/m01-diario/adr-001-*.md` con contexto / decisión / consecuencias.
- **Proyecto — Diario:** Al menos 2 notas `semana-NNNN.md` + `progress.json` actualizado.

## Criterios de dominio

- [ ] Explicas branching sin mirar Stack Overflow.
- [ ] Resuelves un conflicto de merge simple.
- [ ] Tu bitácora de la semana 2 existe y es honesta.
- [ ] No dependes de la GUI de Git para lo básico.
