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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Cada llamada crea un marco. Hoy lo ves con variables locales y una función
      anidada.


      **Objetivo de esta lección:** Explicar en tus palabras qué hay en un stack
      frame y demostrarlo con direcciones de locales.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: 'Return address, saved frame pointer (idea), locals, arguments (visión).'
  - id: s3
    tipo: ejemplo
    titulo: Demo
    xp: 10
    cuerpo: >-
      `stack_demo.c`: `main` llama `f` llama `g`; imprime `&` de locales en cada
      una. Observa si las direcciones crecen hacia abajo (típico x86-64).
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Stack frames intro», ¿qué demuestra que cumpliste el criterio
      mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Stack frames intro
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
      ¿Es recomendable en esta lección? “Creer que “el stack” es una estructura
      de datos de C."
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
          Explicar en tus palabras qué hay en un stack frame y demostrarlo con
          direcciones de locales.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Nota
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
