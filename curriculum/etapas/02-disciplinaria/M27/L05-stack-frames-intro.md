---
id: L05
materia: M27
orden: 5
titulo: Stack frames intro
horas: 5
semana: 2
lectura: 'CSAPP: stack frame / machine-level intro'
evidencia: notas/stack-frame.md + src/stack_demo.c
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Explicar en tus palabras qué hay en un stack frame y
      demostrarlo con direcciones de locales.


      Cada llamada crea un marco. Hoy lo ves con variables locales y una función
      anidada.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: 'Return address, saved frame pointer (idea), locals, arguments (visión).'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Stack frames intro" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: notas/stack-frame.md + src/stack_demo.c
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
      ¿Es buena práctica en esta lección? “Creer que “el stack” es una
      estructura de datos de C."
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
          Explicar en tus palabras qué hay en un stack frame y demostrarlo con
          direcciones de locales.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Demo
    xp: 10
    cuerpo: >-
      `stack_demo.c`: `main` llama `f` llama `g`; imprime `&` de locales en cada
      una. Observa si las direcciones crecen hacia abajo (típico x86-64).
  - id: s7
    tipo: explicacion
    titulo: 3. Nota
    xp: 10
    cuerpo: >-
      Dibuja tres frames. Relaciona con M05 (memoria) y M11 (espacio de
      direcciones del proceso).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Demo corre; anotaste el orden de direcciones.
      - Diagrama de frames en notas.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L05 — Stack frames intro

**~5.0 h · Semana 2**

Cada llamada crea un marco. Hoy lo ves con variables locales y una función anidada.

## Objetivo

Explicar en tus palabras qué hay en un stack frame y demostrarlo con direcciones de locales.

## Pasos

### 1. Lectura (45 min)

Return address, saved frame pointer (idea), locals, arguments (visión).

### 2. Demo (90 min)

`stack_demo.c`: `main` llama `f` llama `g`; imprime `&` de locales en cada una. Observa si las direcciones crecen hacia abajo (típico x86-64).

### 3. Nota (60 min)

Dibuja tres frames. Relaciona con M05 (memoria) y M11 (espacio de direcciones del proceso).

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: stack frame / machine-level intro | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Demo corre; anotaste el orden de direcciones.
2. Diagrama de frames en notas.
3. Commit.

## Errores comunes

- Creer que “el stack” es una estructura de datos de C.
- Confundir stack del proceso con call stack de JS async.

## Siguiente

[L06 — Calling convention System V AMD64](L06-calling-convention-system-v.md)
