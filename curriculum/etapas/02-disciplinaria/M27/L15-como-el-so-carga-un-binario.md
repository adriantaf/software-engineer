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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      `./out/hello` pide al kernel un `exec`. Hoy unes M11 (procesos) con el
      formato ELF.


      **Objetivo de esta lección:** Narrativa paso a paso: shell → `execve` →
      loader → `_start` → `main` → `exit`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```bash
      strace -e execve,exit_group ./out/hello
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Observa
    xp: 10
    cuerpo: |-
      ```bash
      strace -e execve,exit_group ./out/hello
      ```

      (o `strace ./out/hello 2>&1 | head`).
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Cómo el SO carga un binario», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Cómo el SO carga un
          binario
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: quiz
    titulo: Evita el error común
    xp: 15
    variante: verdadero_falso
    pregunta: >-
      ¿Es recomendable en esta lección? “Decir que el compilador “ejecuta” el
      programa."
    opciones:
      - id: t
        texto: Verdadero
      - id: f
        texto: Falso
    respuesta: f
    explicacionError: 'Eso está listado como error común: no lo hagas.'
    explicacionOk: Correcto — es un anti-patrón.
  - id: s6
    tipo: quiz
    titulo: Foco (dificultad media)
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      ¿Cuál describe mejor lo que debes ser capaz de hacer al cerrar esta
      lección?
    opciones:
      - id: a
        texto: >-
          Narrativa paso a paso: shell → `execve` → loader → `_start` → `main` →
          `exit`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Escribe
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
