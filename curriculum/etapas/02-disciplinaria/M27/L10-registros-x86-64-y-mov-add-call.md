---
id: L10
materia: M27
orden: 10
titulo: Registros x86-64 y mov/add/call
horas: 5
semana: 3
lectura: 'CSAPP machine-level: mov, add, call/ret'
evidencia: notas/asm-basico.md
formato: pasos
xpLeccion: 120
pasos:
  - id: s1
    tipo: explicacion
    titulo: Por qué esta lección
    xp: 10
    cuerpo: >-
      Pocas instrucciones bastan para leer el 80% del asm de estudiantes.


      **Objetivo de esta lección:** Glosario propio: `mov`, `add`, `sub`,
      `call`, `ret`, `push`/`pop` (idea), registros `rax`…`r9`.


      Los libros y el detalle largo quedan como **lectura complementaria** al
      final. Aquí el foco es entender y demostrar.
  - id: s2
    tipo: ejemplo
    titulo: Lectura
    xp: 10
    cuerpo: Enfócate en transferencias y llamadas.
  - id: s3
    tipo: ejemplo
    titulo: Anota tu `sum3.s`
    xp: 10
    cuerpo: >-
      Comenta 8–12 líneas en una copia `asm/sum3-anotado.s` o en markdown lado a
      lado.
  - id: s4
    tipo: quiz
    titulo: Comprueba lo básico
    xp: 10
    variante: opcion_multiple
    pregunta: >-
      Al terminar «Registros x86-64 y mov/add/call», ¿qué demuestra que
      cumpliste el criterio mínimo?
    opciones:
      - id: a
        texto: 'Marca la lección solo si:'
      - id: b
        texto: >-
          Instalar herramientas al azar sin evidencia de Registros x86-64 y
          mov/add/call
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
    pregunta: ¿Es recomendable en esta lección? “Memorizar encoding de opcodes."
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
          Glosario propio: `mov`, `add`, `sub`, `call`, `ret`, `push`/`pop`
          (idea), registros `rax`…`r9`.
      - id: b
        texto: Saltar a otra materia dejando esta a medias
      - id: c
        texto: Memorizar el índice del libro sin practicar
    respuesta: a
    explicacionError: El objetivo de la lección define el foco — no el consumo pasivo.
    explicacionOk: Correcto.
  - id: s7
    tipo: explicacion
    titulo: Quiz auto
    xp: 10
    cuerpo: 'Sin mirar: ¿dónde está el return value? ¿primer argumento?'
  - id: s8
    tipo: resumen
    titulo: Cierre
    xp: 10
    puntos:
      - 'Marca la lección solo si:'
      - Asm anotado o notas equivalentes.
      - Respondiste el auto-quiz en notas.
      - Commit.
    siguiente: Sigue al siguiente nodo del camino o abre la lectura complementaria.
---
## Lectura complementaria

Detalle original, lecturas de libro y plantillas. Úsalo mientras avanzas los pasos interactivos.

# L10 — Registros x86-64 y mov/add/call

**~5.0 h · Semana 3**

Pocas instrucciones bastan para leer el 80% del asm de estudiantes.

## Objetivo

Glosario propio: `mov`, `add`, `sub`, `call`, `ret`, `push`/`pop` (idea), registros `rax`…`r9`.

## Pasos

### 1. Lectura (60 min)

Enfócate en transferencias y llamadas.

### 2. Anota tu `sum3.s` (90 min)

Comenta 8–12 líneas en una copia `asm/sum3-anotado.s` o en markdown lado a lado.

### 3. Quiz auto (30 min)

Sin mirar: ¿dónde está el return value? ¿primer argumento?

### 4. Commit (15 min)

## Lectura de esta lección

| Fuente | Qué leer | Enlace |
|--------|----------|--------|
| *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron (CSAPP) | CSAPP machine-level: mov, add, call/ret | [Compiler Explorer](https://godbolt.org/) |
| Catálogo | Entrada de esta materia | [Bibliografía · M27](../../../bibliografia.md#m27-sistemas-a-bajo-nivel) |


## Hecho cuando

Marca la lección **solo si**:

1. Asm anotado o notas equivalentes.
2. Respondiste el auto-quiz en notas.
3. Commit.

## Errores comunes

- Memorizar encoding de opcodes.
- Ignorar que AT&T (`gcc -S`) pone dest a la derecha.

## Siguiente

[L11 — Optimización -O0 vs -O2](L11-optimizacion-o0-vs-o2.md)
