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

Sin método, 20 h/semana se diluyen en tutoriales. Esta materia instala el sistema de trabajo de toda la academia: terminal, Git limpio y bitácora.

**En cristiano:** hoy configuras tu entorno, haces commits claros en **este** repo y escribes una decisión corta (ADR). No es un curso de Git de 8 horas: es hábito.

## Análogos universitarios

- UABC: Introducción a la Ingeniería / Herramientas de desarrollo
- Tec: parte de pensamiento computacional (herramientas)

## Objetivos de aprendizaje

Al terminar debes poder:

1. Organizar una semana de estudio (teoría / práctica / proyecto).
2. Usar la terminal con soltura (navegación, pipes, permisos, grep).
3. Hacer commits atómicos, ramas y PRs claros.
4. Documentar decisiones (ADR) y leer documentación oficial.

## Cómo estudiar esta materia

- Lee [Cómo estudiar](../../como-estudiar.md) si aún no lo hiciste.
- Cada día: terminal abierta + este repo clonado.
- No veas un curso de Git de 8 horas: practica comandos en **este** repo.
- La bitácora semanal es parte del aprendizaje, no un adorno.

## Día 1 (2–3 h) — hazlo hoy

1. Abre la terminal. Comprueba versiones:
   ```bash
   git --version
   node --version
   ```
2. Si falta algo, instálalo (Node LTS + Git). En Windows preferible WSL2.
3. Clona o abre este repo y crea la carpeta de evidencia:
   ```bash
   mkdir -p projects/m01-diario
   ```
4. Escribe `projects/m01-diario/entorno.md` con: SO, versiones de Git/Node, editor.
5. Haz **un** commit atómico, por ejemplo:
   ```bash
   git add projects/m01-diario/entorno.md
   git commit -m "docs(m01): registrar entorno de desarrollo"
   ```
6. Lee solo los capítulos 1–2 de *Pro Git* (o la guía oficial) y anota 5 comandos nuevos.

## Ejemplo — mensaje de commit bueno vs malo

```text
malo:  update
malo:  cambios
bueno: docs(m01): añadir bitácora de la semana 0001
bueno: chore(m01): aliases de git en .bashrc
```

Regla: el mensaje dice **qué** cambió y **por qué** importa.

## Ejemplo — plantilla ADR (P3)

Crea `projects/m01-diario/adr-001-typescript.md`:

```markdown
# ADR 001 — TypeScript como lenguaje principal

## Contexto
Necesito un lenguaje profundo para web, APIs e IA tooling.

## Decisión
Usar TypeScript en modo strict para la academia.

## Consecuencias
+ Tipos y mejor tooling
+ Escala a React/Node
− Curva inicial vs JS puro
```

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
- ADR de 1 página.
- Bitácora semanal en este repo.

## Lecturas

Canon: [*Pro Git*](https://git-scm.com/book/es/v2) (Chacon & Straub). Catálogo: [bibliografía](../../bibliografia.md).

| Semana | Capítulos / secciones | Alternativa gratis |
|--------|----------------------|--------------------|
| 1 | *Pro Git* **cap. 1** (Introducción) + [Cómo estudiar](../../como-estudiar.md); práctica shell (man/`--help` de `cd` `ls` `grep` `chmod`) | Misma URL ES + man pages |
| 2 | *Pro Git* **caps. 2–3** (Fundamentos de Git; Ramas en Git) — haz los ejemplos en este repo | Misma URL ES |

**Regla:** no leas más allá del cap. 3 en M01. Servidor remoto (cap. 4) llega cuando uses GitHub con remoto.

## Prácticas

1. **P1:** Entorno listo: Node LTS, Git, editor, carpeta `~/dev`. Lista de versiones en `projects/m01-diario/entorno.md`.
2. **P2:** 7 días de commits atómicos en este repo (o diario). Nada de “update stuff”.
3. **P3:** Un ADR: “Por qué TypeScript como lenguaje principal de la academia”.

## Proyecto útil

**Diario de ingeniería:** usa este mismo repositorio. Cada semana:

- Actualiza `progress.json`.
- Añade nota en `projects/m01-diario/semana-NNNN.md` (qué estudiaste, qué bloqueó, qué sigue).

## Errores comunes

- Instalar 15 herramientas el día 1 y no hacer ningún commit.
- Usar solo la GUI de GitHub Desktop sin entender `status`/`diff`.
- Commits gigantes (“todo el portafolio”) que no se pueden revisar.
- Copiar aliases de internet sin saber qué hacen.

## Criterios de dominio

- [ ] Explicas branching sin mirar Stack Overflow.
- [ ] Resuelves un conflicto de merge simple.
- [ ] Tu bitácora de la semana 2 existe y es honesta.
- [ ] No dependes de la GUI de Git para lo básico.
