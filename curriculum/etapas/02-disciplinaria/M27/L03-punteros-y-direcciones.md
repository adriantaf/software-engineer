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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Código que muestra `&x`, `*p`, aritmética básica de punteros
      a `int`, y un diagrama tuyo.


      Un puntero es una dirección con tipo. Hoy dejas de temerle imprimiendo
      direcciones reales.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: 'Punteros: declaración, `*`, `&`, `NULL`.'
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: 'Para marcar "Punteros y direcciones" como hecha, ¿qué cuenta de verdad?'
    opciones:
      - id: a
        texto: src/pointers.c + diagrama en notas/
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
    pregunta: ¿Es buena práctica en esta lección? “Dereferenciar `NULL`."
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
          Código que muestra `&x`, `*p`, aritmética básica de punteros a `int`,
          y un diagrama tuyo.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Experimentos
    xp: 10
    cuerpo: >-
      En `src/pointers.c`: variable local, puntero a ella, modificar vía `*p`,
      array + aritmética `p+1`. Imprime valores y direcciones con `%p`.
  - id: s7
    tipo: explicacion
    titulo: 3. Diagrama
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
