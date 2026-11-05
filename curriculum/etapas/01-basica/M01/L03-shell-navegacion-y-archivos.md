---
id: L03
materia: M01
orden: 3
titulo: "Shell: navegación y archivos"
horas: 3
semana: 1
lectura: "man + --help de pwd, ls, cd, mkdir, touch, mv, cp, rm, cat"
evidencia: "Comandos practicados en bitácora o transcript corto"
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: La shell es tu IDE de operaciones
    xp: 10
    cuerpo: |
      La terminal no es un castigo: es el lugar donde **navegas**, **creas** y **inspeccionas** sin GUI.

      Hoy: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `mv`/`cp`, `cat`. Mañana (L04): pipes, permisos y docs.
  - id: s2
    tipo: ejemplo
    titulo: Tour por este repo
    xp: 10
    caption: Practica en la raíz del plan.
    cuerpo: |
      ```bash
      pwd
      ls
      ls -la
      cd projects
      mkdir -p m01-diario/tmp-shell
      touch m01-diario/tmp-shell/hola.txt
      cat m01-diario/tmp-shell/hola.txt
      cd ..
      ```
  - id: s3
    tipo: terminal
    titulo: "¿Dónde estoy?"
    xp: 15
    enunciado: "Escribe el comando que imprime el **directorio de trabajo actual**."
    comandoEsperado: pwd
    explicacionError: "Es `pwd` (print working directory)."
  - id: s4
    tipo: terminal
    titulo: Listar con detalle
    xp: 15
    enunciado: "Lista archivos **incluyendo ocultos** y con detalle (permisos, fechas)."
    comandoEsperado:
      - ls -la
      - ls -al
      - ls -a -l
      - ls -l -a
    explicacionError: "Combina `-l` (largo) y `-a` (ocultos): `ls -la`."
  - id: s5
    tipo: terminal
    titulo: Crear carpeta anidada
    xp: 15
    enunciado: |
      Crea la ruta `projects/m01-diario/tmp-shell` aunque falten padres.
      (Un solo comando.)
    comandoEsperado:
      - mkdir -p projects/m01-diario/tmp-shell
    pistas:
      - "Flag -p crea padres."
    explicacionError: "mkdir -p projects/m01-diario/tmp-shell"
  - id: s6
    tipo: quiz
    titulo: mv vs cp
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Qué hace mv notas.txt archivo.txt?"
    opciones:
      - id: a
        texto: Copia notas.txt a archivo.txt y deja el original
      - id: b
        texto: Renombra o mueve notas.txt a archivo.txt
      - id: c
        texto: Borra notas.txt
    respuesta: b
    explicacionError: "mv mueve/renombra. cp copia. rm borra."
    explicacionOk: Correcto.
  - id: s7
    tipo: resumen
    titulo: Cierre L03
    xp: 10
    puntos:
      - "Navegas con `pwd` / `cd` / `ls` sin miedo."
      - "Creas rutas con `mkdir -p` y archivos con `touch`."
      - "Distingues `mv`, `cp` y `rm`."
      - Anota 3 comandos nuevos en la bitácora (evidencia).
    siguiente: "Siguiente → L04 pipes, permisos y docs."
---

## Lectura complementaria

Usa `man ls` o `ls --help`. No memorices flags: aprende a **consultar**.
