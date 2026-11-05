---
id: L01
materia: M01
orden: 1
titulo: Entorno y primer commit
horas: 2.5
semana: 1
lectura: "Pro Git cap. 1 (complementaria) — después de practicar"
evidencia: "projects/m01-diario/entorno.md + commit docs(m01): registrar entorno"
formato: pasos
xpLeccion: 85
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué empieza aquí
    xp: 10
    cuerpo: |
      Sin entorno y sin hábito de commit, el resto del plan se diluye en “luego lo configuro”.

      Hoy instalas **poco** y **demuestras** con un archivo + un commit en **este** repo.

      Usarás Git como **receta** (`status` → `add` → `commit`). No hace falta entender staging a fondo todavía: eso llega en L05–L07.
  - id: s2
    tipo: ejemplo
    titulo: El flujo mínimo de evidencia
    xp: 10
    caption: "Receta del Día 1 — memoriza el orden."
    cuerpo: |
      ```bash
      git status
      git add projects/m01-diario/entorno.md
      git commit -m "docs(m01): registrar entorno de desarrollo"
      git log -1 --oneline
      ```

      Si Git pide nombre/email la primera vez:

      ```bash
      git config --global user.name "Tu Nombre"
      git config --global user.email "tu@email.com"
      ```
  - id: s3
    tipo: quiz
    titulo: Qué cuenta como evidencia
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Qué demuestra que “existes” en este plan el Día 1?"
    opciones:
      - id: a
        texto: Tener VS Code instalado y un tema oscuro
      - id: b
        texto: Un archivo entorno.md en projects/ + un commit que lo registra
      - id: c
        texto: Haber leído Pro Git cap. 1 completo sin tocar la terminal
    respuesta: b
    explicacionError: La evidencia es archivo en projects/ + commit. Herramientas o lectura sola no bastan.
    explicacionOk: "Correcto — evidencia = archivo + historial en git."
  - id: s4
    tipo: terminal
    titulo: Comprueba Git
    xp: 15
    enunciado: |
      Escribe el comando que muestra la **versión** de Git instalada.
    comandoEsperado:
      - git --version
    pistas:
      - "Empieza por git y pide la versión."
    explicacionError: "El comando es git --version (con dos guiones)."
  - id: s5
    tipo: terminal
    titulo: Primer commit (comando)
    xp: 15
    enunciado: |
      Tras crear `projects/m01-diario/entorno.md`, ¿qué comando **añade ese archivo** al área de staging?

      (En la vida real créalo con SO, Git, Node, editor y fecha; aquí compruebas el comando.)
    comandoEsperado:
      - git add projects/m01-diario/entorno.md
    pistas:
      - "git add + ruta del archivo"
    explicacionError: "Usa git add projects/m01-diario/entorno.md"
  - id: s6
    tipo: quiz
    titulo: Verdadero o falso
    xp: 10
    variante: verdadero_falso
    pregunta: "Hoy debes instalar 15 herramientas (Docker, k8s, 3 IDEs…) antes del primer commit."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: "Falso — el error común es instalar de más y no hacer el commit."
    explicacionOk: Exacto. Poco entorno, mucha evidencia.
  - id: s7
    tipo: resumen
    titulo: Cierre L01
    xp: 10
    puntos:
      - "Git + Node LTS en PATH; versiones anotadas."
      - "Existe projects/m01-diario/entorno.md con SO / Git / Node / editor."
      - "Commit con mensaje que menciona el entorno (ideal docs(m01): registrar entorno)."
      - "Lectura complementaria: Pro Git cap. 1 al final, para nombrar lo que ya corriste."
    siguiente: "Siguiente → L02 Método y práctica deliberada."
---

## Lectura complementaria

| Fuente | Qué leer | Alternativa |
|--------|----------|-------------|
| *Pro Git* | Cap. 1 | [URL en español](https://git-scm.com/book/es/v2) |
| Este plan | [Cómo estudiar](../../../como-estudiar.md) (una pasada) | — |

## Checklist offline (evidencia real)

1. `git --version` y `node --version` OK.
2. Archivo `projects/m01-diario/entorno.md` completo.
3. Commit `docs(m01): registrar entorno de desarrollo` (o equivalente claro).

Esto alimenta la **P1** de la materia.
