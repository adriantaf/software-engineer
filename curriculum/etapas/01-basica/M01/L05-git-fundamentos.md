---
id: L05
materia: M01
orden: 5
titulo: Git fundamentos
horas: 3
semana: 2
lectura: "Pro Git cap. 2 (fundamentos) — lectura complementaria guiada"
evidencia: "status/diff/log usados con intención en este repo"
formato: pasos
xpLeccion: 95
pasos:
  - id: s1
    tipo: explicacion
    titulo: Tres árboles mentales
    xp: 10
    cuerpo: |
      Git no es “guardar archivos”. Piensa en tres zonas:

      1. **Working tree** — tus archivos editados.
      2. **Staging (index)** — lo que irá en el próximo commit (`git add`).
      3. **Repository** — historial de commits.

      Comandos núcleo: `status`, `diff`, `add`, `commit`, `log`.
  - id: s2
    tipo: ejemplo
    titulo: Ciclo de un cambio
    xp: 10
    cuerpo: |
      ```bash
      git status
      # edita un archivo…
      git diff                 # working vs staging
      git add ruta/archivo
      git diff --staged        # lo que vas a committear
      git commit -m "docs(m01): nota corta"
      git log --oneline -5
      ```
  - id: s3
    tipo: quiz
    titulo: "¿Dónde está el cambio?"
    xp: 15
    variante: opcion_multiple
    pregunta: "Editaste un archivo pero aún no corriste `git add`. ¿Dónde está el cambio?"
    opciones:
      - id: a
        texto: Solo en staging
      - id: b
        texto: En el working tree (sin staged)
      - id: c
        texto: Ya está en un commit nuevo
    respuesta: b
    explicacionError: "Sin `add`, el cambio vive en el working tree."
    explicacionOk: Correcto.
  - id: s4
    tipo: terminal
    titulo: Ver estado
    xp: 15
    enunciado: Comando para ver archivos modificados / staged / untracked.
    comandoEsperado: git status
    explicacionError: "Es `git status`."
  - id: s5
    tipo: terminal
    titulo: Diff staged
    xp: 15
    enunciado: "Comando para ver el diff de lo **ya en staging** (listo para commit)."
    comandoEsperado:
      - git diff --staged
      - git diff --cached
    explicacionError: "`git diff --staged` (o `--cached`)."
  - id: s6
    tipo: quiz
    titulo: Completar
    xp: 15
    variante: completar
    pregunta: "El área intermedia entre working tree y el historial se llama ____ (staging o index)."
    respuesta:
      - staging
      - index
      - staging area
      - el index
    explicacionError: Se llama staging area (index).
    explicacionOk: Bien.
  - id: s7
    tipo: resumen
    titulo: Cierre L05
    xp: 15
    puntos:
      - Explicas working / staging / repo sin memes.
      - "Usas `status`, `diff`, `diff --staged`, `log`."
      - "Lectura: Pro Git cap. 2 (complementaria) para reforzar nombres."
    siguiente: "Siguiente → L06 commits atómicos."
---

## Lectura complementaria

*Pro Git* capítulo 2. Practica cada sección en **este** repo, no en un playground vacío.
