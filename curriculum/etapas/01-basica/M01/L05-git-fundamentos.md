---
id: L05
materia: M01
orden: 5
titulo: Git fundamentos
horas: 3
semana: 2
lectura: "Pro Git cap. 2 (Fundamentos de Git) — working tree, staging, commit"
evidencia: "git status/diff/log usados en este repo; notas de 5 comandos nuevos"
---

# L05 — Git fundamentos

**~3 h · Semana 2**

Entras a la semana de Git. Aquí el libro manda: lees *Pro Git* y **reproduces** en este repo, no en un playground aparte.

## Objetivo

Dominar el ciclo working tree → staging → commit, y leer `status`, `diff` y `log` sin miedo.

## Mapa mental

```text
archivos modificados  →  git add  →  staging  →  git commit  →  historial
                           ↑
                     git status / git diff
```

## Pasos

### 1. Lectura activa — Pro Git cap. 2 (60–75 min)

Lee el **capítulo 2** de [*Pro Git*](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Obteniendo-un-repositorio-Git) (Fundamentos).

Mientras lees, ten la terminal abierta. Cada vez que el libro muestre un comando, **pruébalo** aquí (con archivos de `projects/m01-diario/`, no inventes otro repo).

### 2. Ciclo mínimo a mano (40–50 min)

Haz un cambio pequeño (por ejemplo una línea en `shell-notas.md` o en la bitácora):

```bash
git status
git diff
git add -p    # o git add <archivo>
git status
git diff --staged
git commit -m "docs(m01): anotar práctica de git status/diff"
git log -3 --oneline
git show HEAD
```

Si `add -p` te confunde, usa `git add <archivo>` y vuelve a `add -p` otro día.

### 3. Vocabulario que debes poder explicar (20 min)

Sin mirar el libro, escribe en `projects/m01-diario/git-notas.md`:

- Working tree
- Staging area (index)
- Commit
- Qué responde `git status` en 3 estados típicos

### 4. Cinco comandos nuevos (15–20 min)

Lista 5 comandos/flags del cap. 2 que no usabas (ej. `git log --stat`, `git rm`, `git mv`) y prueba al menos 2.

## Lectura de esta lección

| Fuente | Capítulos | Alternativa |
|--------|-----------|-------------|
| *Pro Git* | **Cap. 2** | [ES](https://git-scm.com/book/es/v2) |

**Regla M01:** no pases al cap. 4 (servidor remoto) todavía. Remotos cuando uses GitHub de verdad en el flujo diario.

## Hecho cuando

1. Leíste (o trabajaste) el cap. 2 con ejercicios en **este** repo.
2. Existe al menos un commit nuevo de práctica con mensaje claro.
3. `git-notas.md` define working tree / staging / commit con tus palabras.

## Errores comunes

- Leer el capítulo entero sin un solo `git status`.
- Hacer commits basura (`asdf`, `update`) “porque es práctica”.
- Usar solo la GUI del editor y no mirar el diff.

## Siguiente

[L06 — Commits atómicos y mensajes](L06-commits-atomicos-y-mensajes.md)
