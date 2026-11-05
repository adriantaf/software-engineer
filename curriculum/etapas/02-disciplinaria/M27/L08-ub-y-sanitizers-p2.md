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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cerrar **P2**: reproducir un error de memoria y ver el
      reporte de ASan o UBSan.


      Los sanitizers transforman UB en errores ruidosos. Hoy cazas un bug a
      propósito.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: >-
      ```bash

      gcc -Wall -Wextra -g -O0 -fsanitize=address,undefined -o out/bug
      src/bug_demo.c

      ./out/bug

      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "UB y sanitizers ASan/UBSan (P2)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/sanitizer-p2.md — cierra P2
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
      ¿Es buena práctica en esta lección? “Dejar el bug sin arreglar como único
      artefacto."
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
          Cerrar **P2**: reproducir un error de memoria y ver el reporte de ASan
          o UBSan.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Bug deliberado
    xp: 10
    cuerpo: Programa con OOB write o UAF **solo en** `src/bug_demo.c` (nunca en libs).
  - id: s7
    tipo: ejemplo
    titulo: 3. Compila con sanitizer
    xp: 10
    cuerpo: >-
      ```bash

      gcc -Wall -Wextra -g -O0 -fsanitize=address,undefined -o out/bug
      src/bug_demo.c

      ./out/bug

      ```
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Tienes reporte de sanitizer + versión arreglada.
      - Notas P2 completas.
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
