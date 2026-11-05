---
id: L17
materia: M27
orden: 17
titulo: Documentar un stack frame real
horas: 5
semana: 5
lectura: Repaso stack + ABI
evidencia: notas/frame-real.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Qué vas a lograr
    xp: 10
    cuerpo: >-
      **Objetivo:** Paquete corto: fuente, asm `-O0`, diagrama, lista de slots
      (retorno, regs, locals).


      Síntesis parcial: un frame de **tu** función con evidencias cruzadas (C +
      asm + diagrama).
  - id: s2
    tipo: ejemplo
    titulo: 1. Elige función
    xp: 10
    cuerpo: Una de P3 o `sum3`.
  - id: s3
    tipo: quiz
    titulo: Evidencia de la lección
    xp: 15
    variante: opcion_multiple
    pregunta: >-
      Para marcar "Documentar un stack frame real" como hecha, ¿qué cuenta de
      verdad?
    opciones:
      - id: a
        texto: notas/frame-real.md
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
    pregunta: ¿Es buena práctica en esta lección? “Diagrama que no coincide con el asm."
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
          Paquete corto: fuente, asm `-O0`, diagrama, lista de slots (retorno,
          regs, locals).
      - id: b
        texto: Instalar herramientas al azar sin evidencia
      - id: c
        texto: Saltar a otra materia sin terminar esta
    respuesta: a
    explicacionError: 'El foco está en el objetivo de la lección, no en atajos.'
    explicacionOk: Correcto.
  - id: s6
    tipo: explicacion
    titulo: 2. Empaqueta
    xp: 10
    cuerpo: '`notas/frame-real.md` con los tres artefactos.'
  - id: s7
    tipo: explicacion
    titulo: 3. Revisión
    xp: 10
    cuerpo: ¿Podrías explicarlo en voz alta en 5 minutos?
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - '`frame-real.md` completo.'
      - Commit.
    siguiente: Continúa en el mapa de la materia o abre la lectura complementaria abajo.
---
## Lectura complementaria

Contenido original de la lección (pasos detallados, lecturas y plantillas). Úsalo mientras avanzas los pasos interactivos.

# L17 — Documentar un stack frame real

**~5.0 h · Semana 5**

Síntesis parcial: un frame de **tu** función con evidencias cruzadas (C + asm + diagrama).

## Objetivo

Paquete corto: fuente, asm `-O0`, diagrama, lista de slots (retorno, regs, locals).

## Pasos

### 1. Elige función (20 min)

Una de P3 o `sum3`.

### 2. Empaqueta (150 min)

`notas/frame-real.md` con los tres artefactos.

### 3. Revisión (40 min)

¿Podrías explicarlo en voz alta en 5 minutos?

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | Repaso stack + ABI | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. `frame-real.md` completo.
2. Commit.

## Errores comunes

- Diagrama que no coincide con el asm.
- Mezclar -O2 en la evidencia del frame didáctico.

## Siguiente

[L18 — Viaje de un binario y cierre M27](L18-viaje-de-un-binario-y-cierre.md)
