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
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Síntesis parcial: un frame de **tu** función con evidencias cruzadas (C +
      asm + diagrama).


      **Objetivo de esta lección:** Paquete corto: fuente, asm `-O0`, diagrama,
      lista de slots (retorno, regs, locals).


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Elige función
    xp: 10
    cuerpo: Una de P3 o `sum3`.
  - id: s3
    tipo: ejemplo
    titulo: Empaqueta
    xp: 10
    cuerpo: '`notas/frame-real.md` con los tres artefactos.'
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Documentar un stack frame real», ¿qué demuestra que cumpliste
      el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Documentar un stack
          frame real
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
    pregunta: ¿Es recomendable en esta lección? “Diagrama que no coincide con el asm."
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
          Paquete corto: fuente, asm `-O0`, diagrama, lista de slots (retorno,
          regs, locals).
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Revisión
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
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

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
