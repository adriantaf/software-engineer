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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      C hace visibles los anchos de tipo. Hoy mides y relacionas con M05
      (enteros / overflow).


      **Objetivo de esta lección:** Programa que imprime `sizeof` de tipos
      comunes y notas sobre signed vs unsigned.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura corta
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
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`sizes.c`'
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
    caption: Practícalo en tu entorno; no te limites a leerlo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Tipos, sizeof y representación», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Tipos, sizeof y
          representación
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
    pregunta: ¿Es recomendable en esta lección? “Asumir que `int` siempre es 32 bits."
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
          Programa que imprime `sizeof` de tipos comunes y notas sobre signed vs
          unsigned.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Overflow consciente
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
