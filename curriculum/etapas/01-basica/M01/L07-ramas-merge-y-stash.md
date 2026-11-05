---
id: L07
materia: M01
orden: 7
titulo: Ramas, merge y stash
horas: 3
semana: 2
lectura: "Pro Git cap. 3 (ramas) — complementaria"
evidencia: "Rama de práctica mergeada o documentada en bitácora"
formato: pasos
xpLeccion: 95
pasos:
  - id: s1
    tipo: explicacion
    titulo: Rama = puntero móvil
    xp: 10
    cuerpo: |
      Una **rama** es un puntero a un commit. `main` no es mágica: es la línea que eliges como estable.

      Flujo típico:
      1. Crear rama para un experimento.
      2. Commits ahí.
      3. Volver a `main` y **merge**.
      4. Si interrumpes un trabajo sucio: `stash`.
  - id: s2
    tipo: ejemplo
    titulo: Mini laboratorio
    xp: 10
    cuerpo: |
      ```bash
      git branch
      git switch -c practica/m01-rama
      # edita + commit
      git switch main
      git merge practica/m01-rama
      git branch -d practica/m01-rama
      ```

      Stash:

      ```bash
      git stash push -m "wip bitacora"
      git stash list
      git stash pop
      ```
  - id: s3
    tipo: terminal
    titulo: Crear y cambiar de rama
    xp: 15
    enunciado: "Crea y cambia a la rama `practica/m01-rama` en un solo comando moderno (`switch -c`)."
    comandoEsperado:
      - git switch -c practica/m01-rama
      - git checkout -b practica/m01-rama
    explicacionError: "`git switch -c practica/m01-rama` (o `checkout -b`)."
  - id: s4
    tipo: terminal
    titulo: Merge
    xp: 15
    enunciado: "Estás en `main`. Integra la rama `practica/m01-rama`."
    comandoEsperado:
      - git merge practica/m01-rama
    explicacionError: "`git merge practica/m01-rama`"
  - id: s5
    tipo: quiz
    titulo: "¿Para qué stash?"
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Cuándo usas `git stash`?"
    opciones:
      - id: a
        texto: Para borrar para siempre un commit de main
      - id: b
        texto: Para guardar cambios locales sucios y limpiar el working tree un momento
      - id: c
        texto: Para subir la rama al remoto
    respuesta: b
    explicacionError: Stash = aparcar cambios locales temporales.
    explicacionOk: Correcto.
  - id: s6
    tipo: quiz
    titulo: Conflicto
    xp: 15
    variante: verdadero_falso
    pregunta: "Un conflicto de merge significa que Git no pudo combinar automáticamente el mismo trozo de archivo; tú debes editar y completar el merge."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: "Verdadero — resuelves el archivo, `add`, y cierras el merge."
    explicacionOk: Sí.
  - id: s7
    tipo: resumen
    titulo: Cierre L07
    xp: 15
    puntos:
      - Creas ramas, merges y borras ramas locales con criterio.
      - Sabes aparcar trabajo con stash.
      - Entiendes qué es un conflicto (aunque aún practiques pocos).
      - "Lectura: Pro Git cap. 3."
    siguiente: "Siguiente → L08 ADR, bitácora y cierre."
---

## Lectura complementaria

*Pro Git* cap. 3. Haz el laboratorio en este repo (puedes borrar la rama de práctica después).
