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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Contrastar una llamada de biblioteca con la syscall
      subyacente vista en `strace`.


      `printf` no es syscall: es libc que eventualmente llama `write`.
  - id: s2
    tipo: ejemplo
    titulo: 1. strace write
    xp: 10
    cuerpo: 'Programa con `write(1, …)` vs `puts`. Compara rastros.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Syscalls vs libc" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: notas/syscall-vs-libc.md
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
      ¿Es buena práctica en esta lección? “Llamar “syscall” a cualquier función
      de libc."
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
          Contrastar una llamada de biblioteca con la syscall subyacente vista
          en `strace`.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Notas
    xp: 10
    cuerpo: 'Tabla: API C → libc → syscall (ejemplos: open/read/write/exit).'
  - id: s7
    tipo: explicacion
    titulo: 3. Puente AppSec
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
