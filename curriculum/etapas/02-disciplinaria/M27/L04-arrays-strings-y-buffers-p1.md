---
id: L04
materia: M27
orden: 4
titulo: 'Arrays, strings y buffers (P1)'
horas: 5
semana: 1
lectura: 'CSAPP: arrays/strings; man strncpy'
evidencia: src/buffers.c — cierra P1
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Los strings C son buffers con terminador. Aquí nace buena parte de los
      overflows.


      **Objetivo de esta lección:** Cerrar **P1**: arrays, `strlen`/`snprintf`,
      y una nota de por qué `gets` está prohibido.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m27): P1 buffers y strings"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s3
    tipo: ejemplo
    titulo: '`buffers.c`'
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m27): P1 buffers y strings"
      ```
    caption: Ejemplo tomado de la lección — córrelo o adáptalo.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Arrays, strings y buffers (P1)», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Arrays, strings y
          buffers (P1)
      - id: c
        texto: Marcar la lección hecha sin producir nada verificable
    respuesta: a
    explicacionError: El criterio «Hecho cuando» / evidencia manda. Leer no basta.
    explicacionOk: Bien — evidencia verificable.
  - id: s5
    tipo: terminal
    titulo: Reto de terminal
    xp: 15
    enunciado: |-
      Escribe el comando de práctica de esta lección:

      `git commit -am "feat(m27): P1 buffers y strings"`
    comandoEsperado:
      - 'git commit -am "feat(m27): P1 buffers y strings"'
    pistas:
      - Sin el prompt `$`.
      - Respeta flags y rutas.
    explicacionError: 'Esperado: git commit -am "feat(m27): P1 buffers y strings"'
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
          Cerrar P1: arrays, `strlen`/`snprintf`, y una nota de por qué `gets`
          está prohibido.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Evidencia P1
    xp: 10
    cuerpo: >-
      README o `notas/p1.md`: lista de archivos + qué demuestra cada uno
      (L01–L04).
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`buffers.c` compila con `-Wall` sin warnings nuevos.'
      - Notas P1 enlazan L01–L04.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L04 — Arrays, strings y buffers (P1)

**~5.0 h · Semana 1**

Los strings C son buffers con terminador. Aquí nace buena parte de los overflows.

## Objetivo

Cerrar **P1**: arrays, `strlen`/`snprintf`, y una nota de por qué `gets` está prohibido.

## Pasos

### 1. Lectura (30 min)

Strings C y terminador `\\0`.

### 2. `buffers.c` (120 min)

- Copia segura con `snprintf` a un buffer fijo.
- Función que cuenta longitud sin `strlen` (recorrido hasta `\\0`).
- Comentario: qué pasaría con `strcpy` a buffer corto.

### 3. Evidencia P1 (45 min)

README o `notas/p1.md`: lista de archivos + qué demuestra cada uno (L01–L04).

### 4. Commit (15 min)

```bash
git commit -am "feat(m27): P1 buffers y strings"
```

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP: arrays/strings; man strncpy | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `buffers.c` compila con `-Wall` sin warnings nuevos.
2. Notas P1 enlazan L01–L04.
3. Commit.

## Errores comunes

- Usar `gets`.
- Olvidar espacio para `\0`.
- Cerrar P1 sin evidencia en git.

## Siguiente

[L05 — Stack frames intro](L05-stack-frames-intro.md)
