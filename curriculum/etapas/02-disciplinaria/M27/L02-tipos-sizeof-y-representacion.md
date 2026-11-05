---
id: L02
materia: M27
orden: 2
titulo: 'Tipos, sizeof y representación'
horas: 5
semana: 1
lectura: 'CSAPP: data sizes / integer representation intro'
evidencia: src/sizes.c + notas/sizes.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Programa que imprime `sizeof` de tipos comunes y notas sobre
      signed vs unsigned.


      C hace visibles los anchos de tipo. Hoy mides y relacionas con M05
      (enteros / overflow).
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura corta
    xp: 10
    cuerpo: |-
      ```c
      #include <stdio.h>
      #include <stdint.h>

      int main(void) {
        printf("char=%zu int=%zu long=%zu\n", sizeof(char), sizeof(int), sizeof(long));
        printf("void*=%zu size_t=%zu\n", sizeof(void*), sizeof(size_t));
        printf("int32=%zu int64=%zu\n", sizeof(int32_t), sizeof(int64_t));
        return 0;
      }
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Tipos, sizeof y representación" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/sizes.c + notas/sizes.md
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
    pregunta: ¿Es buena práctica en esta lección? “Asumir que `int` siempre es 32 bits."
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
          Programa que imprime `sizeof` de tipos comunes y notas sobre signed vs
          unsigned.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `sizes.c`
    xp: 10
    cuerpo: >-
      ```c

      #include <stdio.h>

      #include <stdint.h>


      int main(void) {
        printf("char=%zu int=%zu long=%zu\n", sizeof(char), sizeof(int), sizeof(long));
        printf("void*=%zu size_t=%zu\n", sizeof(void*), sizeof(size_t));
        printf("int32=%zu int64=%zu\n", sizeof(int32_t), sizeof(int64_t));
        return 0;
      }

      ```


      Compila y pega la salida en `notas/sizes.md`. Explica por qué `long` puede
      diferir entre plataformas.
  - id: s7
    tipo: explicacion
    titulo: 3. Overflow consciente
    xp: 10
    cuerpo: >-
      Añade un ejemplo signed overflow (con comentario de que es UB en C) y uno
      unsigned que wrappea bien definido. Documenta la diferencia.
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`sizes.c` corre; salida pegada en notas.'
      - Explicas al menos una diferencia de tamaño entre plataformas.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L02 — Tipos, sizeof y representación

**~5.0 h · Semana 1**

C hace visibles los anchos de tipo. Hoy mides y relacionas con M05 (enteros / overflow).

## Objetivo

Programa que imprime `sizeof` de tipos comunes y notas sobre signed vs unsigned.

## Pasos

### 1. Lectura corta (40 min)

CSAPP (tamaños de datos) o equivalen docs. Relaciona con lo que viste en M05.

### 2. `sizes.c` (90 min)

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
  printf("char=%zu int=%zu long=%zu\n", sizeof(char), sizeof(int), sizeof(long));
  printf("void*=%zu size_t=%zu\n", sizeof(void*), sizeof(size_t));
  printf("int32=%zu int64=%zu\n", sizeof(int32_t), sizeof(int64_t));
  return 0;
}
```

Compila y pega la salida en `notas/sizes.md`. Explica por qué `long` puede diferir entre plataformas.

### 3. Overflow consciente (60 min)

Añade un ejemplo signed overflow (con comentario de que es UB en C) y uno unsigned que wrappea bien definido. Documenta la diferencia.

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: data sizes / integer representation intro | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `sizes.c` corre; salida pegada en notas.
2. Explicas al menos una diferencia de tamaño entre plataformas.
3. Commit.

## Errores comunes

- Asumir que `int` siempre es 32 bits.
- Ignorar `stdint.h` cuando necesitas anchos fijos.
- Tratar overflow signed como “siempre wrappea”.

## Siguiente

[L03 — Punteros y direcciones](L03-punteros-y-direcciones.md)
