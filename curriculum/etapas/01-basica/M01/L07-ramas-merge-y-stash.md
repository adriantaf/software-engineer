---
id: L07
materia: M01
orden: 7
titulo: Ramas, merge y stash
horas: 3
semana: 2
lectura: "Pro Git cap. 3 (Ramas en Git) — crear, merge, conflicto simple; stash intro"
evidencia: "Rama de práctica mergeada; notas de conflicto resuelto (o simulado)"
---

# L07 — Ramas, merge y stash

**~3 h · Semana 2**

Las ramas son conversaciones paralelas en el historial. Aquí practicas crear, fusionar y (si aparece) resolver un conflicto mínimo.

## Objetivo

Usar `branch`, `switch`/`checkout`, `merge` y un `stash` básico sin depender de la GUI.

## Pasos

### 1. Lectura — Pro Git cap. 3 (60–75 min)

Lee [*Ramas en Git*](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Qué-es-una-rama%3F) (cap. 3). Enfócate en: qué es una rama, merge fast-forward vs merge commit, conflictos.

Otra vez: terminal abierta, ejemplos en **este** repo.

### 2. Rama de práctica (40–50 min)

```bash
git status
git switch -c practica/m01-rama   # o: git checkout -b practica/m01-rama
# haz un cambio pequeño en un archivo de notes
git add -A
git commit -m "docs(m01): ejercicio de rama de práctica"
git switch main                   # o master — usa tu rama base real
git merge practica/m01-rama
git log -5 --oneline --graph
```

Si tu rama base no se llama `main`, usa el nombre real (`git branch`).

### 3. Conflicto simple (30–40 min)

Opción A — provocarlo:

1. En `main`, edita la misma línea de un archivo de notas y commit.
2. En otra rama, edita la **misma** línea distinto y commit.
3. Merge → resuelve marcadores `<<<<<<<` / `=======` / `>>>>>>>`.
4. `git add` + commit de merge.

Opción B — si no quieres ensuciar el historial: escribe en `git-notas.md` los pasos que *seguirías* y practica en un repo throwaway. Prefiere A si puedes.

### 4. Stash intro (15–20 min)

```bash
# con un cambio sin commit:
git stash push -m "wip m01"
git status
git stash list
git stash pop
```

Anota cuándo usarías stash (cambiar de rama con trabajo a medias) vs commit WIP honesto.

### 5. Limpieza (10 min)

Si la rama `practica/m01-rama` ya está mergeada:

```bash
git branch -d practica/m01-rama
```

## Lectura de esta lección

| Fuente | Capítulos |
|--------|-----------|
| *Pro Git* | **Cap. 3** (ramas). Rebase: solo intro; no reescribas historial remoto aún. |

## Hecho cuando

1. Creaste una rama, commitiste y mergeaste a tu rama base.
2. Sabes explicar un merge conflict en una frase.
3. Probaste `stash` al menos una vez (push/pop o list).

## Criterio de dominio (anticipado)

Más adelante la ficha pide: explicar branching sin Stack Overflow y resolver un conflicto simple. Esta lección es el ensayo.

## Errores comunes

- Trabajar siempre en `main` con 20 archivos mezclados.
- Tener miedo al conflicto y descartar cambios con `reset --hard` sin leer.
- Rebase agresivo en ramas compartidas (aún no toca).

## Siguiente

[L08 — ADR, bitácora y cierre](L08-adr-bitacora-y-cierre.md)
