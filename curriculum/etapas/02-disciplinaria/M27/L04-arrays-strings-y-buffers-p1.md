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
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Cerrar **P1**: arrays, `strlen`/`snprintf`, y una nota de
      por qué `gets` está prohibido.


      Los strings C son buffers con terminador. Aquí nace buena parte de los
      overflows.
  - id: s2
    tipo: ejemplo
    titulo: 1. Lectura
    xp: 10
    cuerpo: |-
      ```bash
      git commit -am "feat(m27): P1 buffers y strings"
      ```
    caption: Ejemplo migrado de la lección original — practícalo en tu entorno.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Arrays, strings y buffers (P1)" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: src/buffers.c — cierra P1
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
    tipo: terminal
    titulo: Comando clave
    xp: 15
    enunciado: |-
      Escribe este comando tal cual (es el de práctica de la lección):

      `git commit -am "feat(m27): P1 buffers y strings"`
    comandoEsperado:
      - 'git commit -am "feat(m27): P1 buffers y strings"'
    pistas:
      - Respeta el orden de los argumentos.
      - Sin prompt `$`.
    explicacionError: 'Esperado: git commit -am "feat(m27): P1 buffers y strings"'
  - id: s5
    tipo: quiz
    titulo: Foco de la lección
    xp: 10
    variante: opcion_multiple
    pregunta: ¿Cuál describe mejor el foco de esta lección?
    opciones:
      - id: a
        texto: >-
          Cerrar **P1**: arrays, `strlen`/`snprintf`, y una nota de por qué
          `gets` está prohibido.
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. `buffers.c`
    xp: 10
    cuerpo: |-
      - Copia segura con `snprintf` a un buffer fijo.
      - Función que cuenta longitud sin `strlen` (recorrido hasta `\\0`).
      - Comentario: qué pasaría con `strcpy` a buffer corto.
  - id: s7
    tipo: explicacion
    titulo: 3. Evidencia P1
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
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

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
