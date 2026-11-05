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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Programa que `malloc` / usa / `free`, y notas de
      use-after-free y leak.


      El heap vive hasta `free` (o fin del proceso). Hoy practicas lifetime
      explícito.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: '`malloc`, `free`, `NULL` check básico.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Heap: malloc, free y lifetime" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/heap_demo.c
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
      ¿Es buena práctica en esta lección? “`malloc` sin revisar `NULL` en código
      “serio”."
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
          Programa que `malloc` / usa / `free`, y notas de use-after-free y
          leak.
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
      Alloca un array de `int`, llénalo, imprímelo, `free`. Intenta (en rama
      comentada) use-after-free y explica por qué es UB.
  - id: s7
    tipo: explicacion
    titulo: 3. Leak consciente
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
