---
id: L08
materia: M27
orden: 8
titulo: UB y sanitizers ASan/UBSan (P2)
horas: 5
semana: 2
lectura: Clang/GCC sanitizers docs
evidencia: notas/sanitizer-p2.md — cierra P2
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los sanitizers transforman UB en errores ruidosos. Hoy cazas un bug a
      propósito.


      **Objetivo de esta lección:** Cerrar **P2**: reproducir un error de
      memoria y ver el reporte de ASan o UBSan.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: >-
      ```bash

      gcc -Wall -Wextra -g -O0 -fsanitize=address,undefined -o out/bug
      src/bug_demo.c

      ./out/bug

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: Bug deliberado
    xp: 10
    cuerpo: >-
      ```bash

      gcc -Wall -Wextra -g -O0 -fsanitize=address,undefined -o out/bug
      src/bug_demo.c

      ./out/bug

      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «UB y sanitizers ASan/UBSan (P2)», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de UB y sanitizers
          ASan/UBSan (P2)
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
      ¿Es recomendable en esta lección? “Dejar el bug sin arreglar como único
      artefacto."
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
          Cerrar P2: reproducir un error de memoria y ver el reporte de ASan o
          UBSan.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Compila con sanitizer
    xp: 10
    cuerpo: >-
      Pega el resumen del reporte en `notas/sanitizer-p2.md` (sin dumps
      enormes).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Tienes reporte de sanitizer + versión arreglada.
      - Notas P2 completas.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L08 — UB y sanitizers ASan/UBSan (P2)

**~5.0 h · Semana 2**

Los sanitizers transforman UB en errores ruidosos. Hoy cazas un bug a propósito.

## Objetivo

Cerrar **P2**: reproducir un error de memoria y ver el reporte de ASan o UBSan.

## Pasos

### 1. Lectura (30 min)

AddressSanitizer y UndefinedBehaviorSanitizer (idea).

### 2. Bug deliberado (60 min)

Programa con OOB write o UAF **solo en** `src/bug_demo.c` (nunca en libs).

### 3. Compila con sanitizer (60 min)

```bash
gcc -Wall -Wextra -g -O0 -fsanitize=address,undefined -o out/bug src/bug_demo.c
./out/bug
```

Pega el resumen del reporte en `notas/sanitizer-p2.md` (sin dumps enormes).

### 4. Arregla y verifica limpio (40 min)

### 5. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Clang/GCC sanitizers docs | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Tienes reporte de sanitizer + versión arreglada.
2. Notas P2 completas.
3. Commit.

## Errores comunes

- Dejar el bug sin arreglar como único artefacto.
- Correr sin `-g` y no entender el stack trace.
- Pensar que sanitizer = antivirus.

## Siguiente

[L09 — De C a asm con -S y objdump](L09-de-c-a-asm-con-s-y-objdump.md)
