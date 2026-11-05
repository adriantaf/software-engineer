---
id: L16
materia: M27
orden: 16
titulo: Syscalls vs libc
horas: 5
semana: 4
lectura: man 2 write; man 3 printf
evidencia: notas/syscall-vs-libc.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      `printf` no es syscall: es libc que eventualmente llama `write`.


      **Objetivo de esta lección:** Contrastar una llamada de biblioteca con la
      syscall subyacente vista en `strace`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: strace write
    xp: 10
    cuerpo: 'Programa con `write(1, …)` vs `puts`. Compara rastros.'
  - id: s3
    tipo: ejemplo
    titulo: Notas
    xp: 10
    cuerpo: 'Tabla: API C → libc → syscall (ejemplos: open/read/write/exit).'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Syscalls vs libc», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Syscalls vs libc
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
      ¿Es recomendable en esta lección? “Llamar “syscall” a cualquier función de
      libc."
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
          Contrastar una llamada de biblioteca con la syscall subyacente vista
          en `strace`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Puente AppSec
    xp: 10
    cuerpo: 'Una frase: validar en tu código no basta si pasas buffers mal a APIs C.'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Tabla syscall vs libc.
      - Evidencia strace.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L16 — Syscalls vs libc

**~5.0 h · Semana 4**

`printf` no es syscall: es libc que eventualmente llama `write`.

## Objetivo

Contrastar una llamada de biblioteca con la syscall subyacente vista en `strace`.

## Pasos

### 1. strace write (60 min)

Programa con `write(1, …)` vs `puts`. Compara rastros.

### 2. Notas (90 min)

Tabla: API C → libc → syscall (ejemplos: open/read/write/exit).

### 3. Puente AppSec (30 min)

Una frase: validar en tu código no basta si pasas buffers mal a APIs C.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man 2 write; man 3 printf | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Tabla syscall vs libc.
2. Evidencia strace.
3. Commit.

## Errores comunes

- Llamar “syscall” a cualquier función de libc.
- Usar syscall numbers crudos sin necesidad.

## Siguiente

[L17 — Documentar un stack frame real](L17-documentar-un-stack-frame-real.md)
