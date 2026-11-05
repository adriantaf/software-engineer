---
id: L15
materia: M27
orden: 15
titulo: Cómo el SO carga un binario
horas: 5
semana: 4
lectura: 'CSAPP: loading; man execve'
evidencia: notas/loader.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Narrativa paso a paso: shell → `execve` → loader → `_start`
      → `main` → `exit`.


      `./out/hello` pide al kernel un `exec`. Hoy unes M11 (procesos) con el
      formato ELF.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```bash
      strace -e execve,exit_group ./out/hello
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Cómo el SO carga un binario" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/loader.md
      - id: b
        texto: Solo leer el título y pasar a la siguiente
      - id: c
        texto: Marcar el checkbox sin producir nada
    respuesta: a
    explicacionError: >-
      Sin evidencia en el repo (o criterio cumplido) no cuenta. Si no está en
      git, no existe.
    explicacionOk: Correcto — evidencia primero.
  - id: s4
    tipo: quiz
    titulo: Error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es buena práctica en esta lección? “Decir que el compilador “ejecuta” el
      programa."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso figura como error común: evítalo.'
    explicacionOk: Bien — ese es un anti-patrón de la lección.
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Narrativa paso a paso: shell → `execve` → loader → `_start` → `main` →
          `exit`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Observa
    xp: 10
    cuerpo: |-
      ```bash
      strace -e execve,exit_group ./out/hello
      ```

      (o `strace ./out/hello 2>&1 | head`).
  - id: s7
    tipo: explicacion
    titulo: 3. Escribe
    xp: 10
    cuerpo: '`notas/loader.md` con el viaje. Enlaza M11.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Nota loader completa.
      - Al menos una línea real de `strace` o equivalente.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L15 — Cómo el SO carga un binario

**~5.0 h · Semana 4**

`./out/hello` pide al kernel un `exec`. Hoy unes M11 (procesos) con el formato ELF.

## Objetivo

Narrativa paso a paso: shell → `execve` → loader → `_start` → `main` → `exit`.

## Pasos

### 1. Lectura (50 min)

Loading / process image.

### 2. Observa (60 min)

```bash
strace -e execve,exit_group ./out/hello
```

(o `strace ./out/hello 2>&1 | head`).

### 3. Escribe (70 min)

`notas/loader.md` con el viaje. Enlaza M11.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: loading; man execve | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Nota loader completa.
2. Al menos una línea real de `strace` o equivalente.
3. Commit.

## Errores comunes

- Decir que el compilador “ejecuta” el programa.
- Ignorar que el dynamic linker también carga libc.

## Siguiente

[L16 — Syscalls vs libc](L16-syscalls-vs-libc.md)
