---
id: L07
materia: M27
orden: 7
titulo: 'Heap: malloc, free y lifetime'
horas: 5
semana: 2
lectura: man malloc; CSAPP dynamic memory intro
evidencia: src/heap_demo.c
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      El heap vive hasta `free` (o fin del proceso). Hoy practicas lifetime
      explícito.


      **Objetivo de esta lección:** Programa que `malloc` / usa / `free`, y
      notas de use-after-free y leak.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: '`malloc`, `free`, `NULL` check básico.'
  - id: s3
    tipo: ejemplo
    titulo: Demo
    xp: 10
    cuerpo: >-
      Alloca un array de `int`, llénalo, imprímelo, `free`. Intenta (en rama
      comentada) use-after-free y explica por qué es UB.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Heap: malloc, free y lifetime», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Heap: malloc, free y
          lifetime
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
      ¿Es recomendable en esta lección? “`malloc` sin revisar `NULL` en código
      “serio”."
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
          Programa que `malloc` / usa / `free`, y notas de use-after-free y
          leak.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Leak consciente
    xp: 10
    cuerpo: Omite un `free` a propósito; documenta cómo lo verías con sanitizer (L08).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`heap_demo.c` correcto compila y corre.'
      - Notas de UAF/leak.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L07 — Heap: malloc, free y lifetime

**~5.0 h · Semana 2**

El heap vive hasta `free` (o fin del proceso). Hoy practicas lifetime explícito.

## Objetivo

Programa que `malloc` / usa / `free`, y notas de use-after-free y leak.

## Pasos

### 1. Lectura (30 min)

`malloc`, `free`, `NULL` check básico.

### 2. Demo (100 min)

Alloca un array de `int`, llénalo, imprímelo, `free`. Intenta (en rama comentada) use-after-free y explica por qué es UB.

### 3. Leak consciente (40 min)

Omite un `free` a propósito; documenta cómo lo verías con sanitizer (L08).

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | man malloc; CSAPP dynamic memory intro | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `heap_demo.c` correcto compila y corre.
2. Notas de UAF/leak.
3. Commit.

## Errores comunes

- `malloc` sin revisar `NULL` en código “serio”.
- Double-free.
- Devolver puntero a local (stack) pensando que es heap.

## Siguiente

[L08 — UB y sanitizers ASan/UBSan (P2)](L08-ub-y-sanitizers-p2.md)
