---
id: L03
materia: M27
orden: 3
titulo: Punteros y direcciones
horas: 5
semana: 1
lectura: 'CSAPP / K&R: pointers'
evidencia: src/pointers.c + diagrama en notas/
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Un puntero es una dirección con tipo. Hoy dejas de temerle imprimiendo
      direcciones reales.


      **Objetivo de esta lección:** Código que muestra `&x`, `*p`, aritmética
      básica de punteros a `int`, y un diagrama tuyo.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: 'Punteros: declaración, `*`, `&`, `NULL`.'
  - id: s3
    tipo: ejemplo
    titulo: Experimentos
    xp: 10
    cuerpo: >-
      En `src/pointers.c`: variable local, puntero a ella, modificar vía `*p`,
      array + aritmética `p+1`. Imprime valores y direcciones con `%p`.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Punteros y direcciones», ¿qué demuestra que cumpliste el
      criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: Instalar herramientas al azar sin evidencia de Punteros y direcciones
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
    pregunta: ¿Es recomendable en esta lección? “Dereferenciar `NULL`."
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
          Código que muestra `&x`, `*p`, aritmética básica de punteros a `int`,
          y un diagrama tuyo.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Diagrama
    xp: 10
    cuerpo: '`notas/punteros.md`: dibuja stack con `x` y `p` (ASCII está bien).'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Programa corre e imprime direcciones.
      - Diagrama en notas.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L03 — Punteros y direcciones

**~5.0 h · Semana 1**

Un puntero es una dirección con tipo. Hoy dejas de temerle imprimiendo direcciones reales.

## Objetivo

Código que muestra `&x`, `*p`, aritmética básica de punteros a `int`, y un diagrama tuyo.

## Pasos

### 1. Lectura (40 min)

Punteros: declaración, `*`, `&`, `NULL`.

### 2. Experimentos (120 min)

En `src/pointers.c`: variable local, puntero a ella, modificar vía `*p`, array + aritmética `p+1`. Imprime valores y direcciones con `%p`.

### 3. Diagrama (45 min)

`notas/punteros.md`: dibuja stack con `x` y `p` (ASCII está bien).

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP / K&R: pointers | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Programa corre e imprime direcciones.
2. Diagrama en notas.
3. Commit.

## Errores comunes

- Dereferenciar `NULL`.
- Confundir `int *p` con “int que se llama *p”.
- Aritmética de punteros en `void*` sin cast.

## Siguiente

[L04 — Arrays, strings y buffers (P1)](L04-arrays-strings-y-buffers-p1.md)
