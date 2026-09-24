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

Sin método, 20 h/semana se diluyen en tutoriales. Esta materia instala el sistema de trabajo de toda la academia.

## Análogos universitarios

- UABC: Introducción a la Ingeniería / Herramientas de desarrollo
- Tec: parte de pensamiento computacional (herramientas)

## Objetivos de aprendizaje

Al terminar debes poder:

1. Organizar una semana de estudio (teoría / práctica / proyecto).
2. Usar la terminal con soltura (navegación, pipes, permisos, grep).
3. Hacer commits atómicos, ramas y PRs claros.
4. Documentar decisiones (ADR) y leer documentación oficial.

## Temario semanal

### Semana 1 — Método + Linux (~20 h)

- Deliberate practice vs consumo pasivo.
- Regla 40/30/30 (teoría / práctica / proyecto).
- Shell: `cd`, `ls`, `pwd`, `mkdir`, `rm`, `cp`, `mv`, `chmod`, redirecciones, pipes.
- Editores: VS Code / Cursor; extensiones mínimas.
- Cómo leer docs oficiales (MDN, Node, Astro).

### Semana 2 — Git + escritura técnica (~20 h)

- `status`, `add`, `commit`, `diff`, `log`, `branch`, `merge`, `rebase` (intro), `stash`.
- Mensajes de commit: qué y por qué.
- Issues y PRs como conversación.
- ADR (Architecture Decision Record) de 1 página.
- Bitácora semanal en este repo.

## Libros y recursos (español)

- *Pro Git* (Scott Chacon) — capítulos 1–3 (hay edición/traducción ES y web).
- Documentación oficial de Git en español.
- Guía de método de esta academia (`curriculum/INDEX.md`).

## Prácticas

1. **P1:** Entorno listo: Node LTS, Git, editor, carpeta `~/dev`. Captura o lista de versiones en `projects/m01-diario/entorno.md`.
2. **P2:** 7 días de commits atómicos en este repo (o diario). Nada de “update stuff”.
3. **P3:** Un ADR: “Por qué TypeScript como lenguaje principal de la academia”.

## Proyecto útil

**Diario de ingeniería:** usa este mismo repositorio. Cada semana:

- Actualiza `progress.json`.
- Añade nota en `projects/m01-diario/semana-NNNN.md` (qué estudiaste, qué bloqueó, qué sigue).

## Criterios de dominio

- [ ] Explicas branching sin mirar Stack Overflow.
- [ ] Resuelves un conflicto de merge simple.
- [ ] Tu bitácora de la semana 2 existe y es honesta.
- [ ] No dependes de la GUI de Git para lo básico.
