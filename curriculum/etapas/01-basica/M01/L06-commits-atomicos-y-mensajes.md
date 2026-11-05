---
id: L06
materia: M01
orden: 6
titulo: Commits atómicos y mensajes
horas: 2.5
semana: 2
lectura: "Convencional commits (idea) + Pro Git cap. 2 (mensajes)"
evidencia: "≥1 commit atómico con mensaje qué/porqué en este repo"
formato: pasos
xpLeccion: 80
pasos:
  - id: s1
    tipo: explicacion
    titulo: Atómico = revisable
    xp: 10
    cuerpo: |
      Un commit **atómico** cambia **una** idea: un fix, un doc, un refactor pequeño.

      Mensaje útil = **qué** cambió + **por qué** (no “update stuff”).

      Estilo del plan (Conventional Commits light):

      `docs(m01): registrar entorno de desarrollo`
  - id: s2
    tipo: ejemplo
    titulo: Buenos vs malos
    xp: 10
    cuerpo: |
      **Mal:**
      - `update`
      - `fixes`
      - `asdf`

      **Bien:**
      - `docs(m01): plan semana 0001 en bitácora`
      - `fix(m01): corregir typo en entorno.md`
      - `chore: ignorar archivo temporal de shell`
  - id: s3
    tipo: quiz
    titulo: "¿Cuál es atómico?"
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Cuál commit es más atómico?"
    opciones:
      - id: a
        texto: "feat: agregar CLI + docs + renombrar 40 archivos + bump deps"
      - id: b
        texto: "docs(m01): añadir notas de Pro Git cap. 2 a la bitácora"
      - id: c
        texto: "update stuff"
    respuesta: b
    explicacionError: Atómico = una intención clara. (b) es un solo cambio de docs.
    explicacionOk: Correcto.
  - id: s4
    tipo: quiz
    titulo: Mensaje
    xp: 15
    variante: verdadero_falso
    pregunta: "El mensaje debe explicar el 'por qué' cuando no es obvio, no solo listar archivos."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: "Verdadero — el diff ya muestra el qué; el mensaje aporta contexto."
    explicacionOk: Sí.
  - id: s5
    tipo: terminal
    titulo: Commit con mensaje
    xp: 20
    enunciado: |
      Escribe un `git commit` con mensaje `docs(m01): nota de practica deliberada`
      (asume que ya hiciste `git add`).
    comandoEsperado:
      - "git commit -m \"docs(m01): nota de practica deliberada\""
      - "git commit -m 'docs(m01): nota de practica deliberada'"
    explicacionError: "`git commit -m \"docs(m01): nota de practica deliberada\"`"
  - id: s6
    tipo: resumen
    titulo: Cierre L06
    xp: 10
    puntos:
      - Prefieres commits pequeños y revisables.
      - "Mensajes con alcance (`docs`/`fix`/`chore`) + descripción."
      - "Evidencia: al menos un commit atómico real en este repo (P2 en curso)."
    siguiente: "Siguiente → L07 ramas, merge y stash."
---

## Lectura complementaria

Evita commits gigantes. Si mezclaste cosas, `git add -p` (más adelante) o deshaz y vuelve a partir.
