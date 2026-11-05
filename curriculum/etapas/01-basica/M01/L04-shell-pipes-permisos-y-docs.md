---
id: L04
materia: M01
orden: 4
titulo: "Shell: pipes, permisos y docs"
horas: 3
semana: 1
lectura: "man + --help de grep, find, chmod, pipe |"
evidencia: "Pipeline anotado en bitácora + permiso entendido"
formato: pasos
xpLeccion: 90
pasos:
  - id: s1
    tipo: explicacion
    titulo: Pipes = componer herramientas
    xp: 10
    cuerpo: |
      Un **pipe** (`|`) conecta la salida de un comando a la entrada de otro.

      Idea: programas pequeños + composición > un monolito mágico.

      También hoy: `grep`, `find`, permisos (`ls -l`, `chmod`) y el hábito de leer `--help` / `man`.
  - id: s2
    tipo: ejemplo
    titulo: Pipeline típico
    xp: 10
    cuerpo: |
      ```bash
      ls -la | head
      git log --oneline | head -n 5
      grep -R "M01" curriculum --include="*.md" | head
      find projects -name "*.md" | head
      ```

      Permisos (lectura):

      ```bash
      ls -l projects/m01-diario/entorno.md
      # -rw-r--r--  → usuario lee/escribe; grupo y otros solo leen
      ```
  - id: s3
    tipo: terminal
    titulo: Pipe a head
    xp: 15
    enunciado: |
      Escribe un pipeline que liste el directorio en formato largo y muestre solo las **primeras líneas** con `head`.
    comandoEsperado:
      - "ls -la | head"
      - "ls -l | head"
      - "ls -la | head -n 10"
    explicacionError: "Algo como `ls -la | head` (el pipe es `|`)."
  - id: s4
    tipo: terminal
    titulo: Buscar texto
    xp: 15
    enunciado: "Comando para buscar la cadena `M01` dentro de archivos (grep básico sobre un path o stdin está bien). Escribe `grep M01` como mínimo viable."
    comandoEsperado:
      - grep M01
      - grep -R M01 .
      - grep -R "M01" curriculum
      - grep -r M01 .
    explicacionError: "Empieza con `grep` y el patrón `M01`."
  - id: s5
    tipo: quiz
    titulo: Qué es un pipe
    xp: 15
    variante: opcion_multiple
    pregunta: "¿Qué hace el símbolo `|` en la shell?"
    opciones:
      - id: a
        texto: Ejecuta el comando de la derecha solo si el de la izquierda falla
      - id: b
        texto: Conecta stdout del comando izquierdo al stdin del derecho
      - id: c
        texto: Redirige la salida a un archivo llamado pipe
    respuesta: b
    explicacionError: "`|` es pipe: salida → entrada del siguiente."
    explicacionOk: Exacto.
  - id: s6
    tipo: quiz
    titulo: Permisos
    xp: 15
    variante: verdadero_falso
    pregunta: "En -rw-r--r--, el dueño puede leer y escribir el archivo."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: t
    explicacionError: "`rw-` para el usuario = read + write."
    explicacionOk: Correcto.
  - id: s7
    tipo: resumen
    titulo: Cierre L04
    xp: 10
    puntos:
      - "Compones comandos con `|`."
      - "Usas `grep` / `find` sin pánico."
      - "Lees un renglón de `ls -l` y entiendes permisos básicos."
      - "Sabes abrir `man` o `--help` antes de Stack Overflow."
    siguiente: "Semana 2 → L05 Git fundamentos."
---

## Lectura complementaria

Practica en este repo. Anota un pipeline útil en `semana-0001.md`.
